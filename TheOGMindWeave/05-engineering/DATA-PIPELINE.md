# MindWeave Data Pipeline Architecture

## Document Information
| Field | Value |
|-------|-------|
| Document ID | ENG-008 |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Owner | Engineering Team |
| Status | Draft |
| Classification | Internal |

---

## Executive Summary

This document defines MindWeave's data pipeline architecture for collecting, processing, and analyzing Claude API usage data. The pipeline handles high-volume event streaming, real-time aggregation, and batch analytics while maintaining data quality and compliance.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DATA PIPELINE ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                       DATA COLLECTION                                │   │
│  │                                                                      │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │   │
│  │  │  SDK Events  │  │ Proxy Events │  │   Webhooks   │              │   │
│  │  │              │  │              │  │              │              │   │
│  │  │ • API calls  │  │ • Pass-thru  │  │ • External   │              │   │
│  │  │ • MCP tools  │  │ • Intercept  │  │ • Billing    │              │   │
│  │  │ • Sessions   │  │ • Transform  │  │ • Alerts     │              │   │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │   │
│  └─────────┼─────────────────┼─────────────────┼────────────────────────┘   │
│            │                 │                 │                             │
│            └─────────────────┴─────────────────┘                             │
│                              │                                               │
│  ┌───────────────────────────▼───────────────────────────────────────────┐  │
│  │                         INGESTION LAYER                                │  │
│  │  ┌────────────────────────────────────────────────────────────────┐  │  │
│  │  │              USAGE TRACKER SERVICE (Go)                         │  │  │
│  │  │                                                                  │  │  │
│  │  │  • Validation  • Enrichment  • Buffering  • Batching            │  │  │
│  │  └──────────────────────────────┬─────────────────────────────────┘  │  │
│  └─────────────────────────────────┼─────────────────────────────────────┘  │
│                                    │                                         │
│  ┌─────────────────────────────────▼─────────────────────────────────────┐  │
│  │                         STREAMING LAYER                                │  │
│  │  ┌────────────────────────────────────────────────────────────────┐  │  │
│  │  │                     APACHE KAFKA                                 │  │  │
│  │  │                                                                  │  │  │
│  │  │  Topics: usage.events | usage.aggregates | usage.alerts        │  │  │
│  │  │  Partitions: 12  |  Replication: 3  |  Retention: 7 days       │  │  │
│  │  └──────────────────────────────┬─────────────────────────────────┘  │  │
│  └─────────────────────────────────┼─────────────────────────────────────┘  │
│                                    │                                         │
│            ┌───────────────────────┼───────────────────────┐                │
│            │                       │                       │                │
│  ┌─────────▼────────┐   ┌─────────▼────────┐   ┌─────────▼────────┐       │
│  │  REAL-TIME       │   │     BATCH        │   │     ARCHIVE      │       │
│  │  PROCESSING      │   │   PROCESSING     │   │     STORAGE      │       │
│  │                  │   │                  │   │                  │       │
│  │  Kafka Streams   │   │  Apache Spark    │   │       S3         │       │
│  │  • 1-min aggs    │   │  • Daily aggs    │   │  • Long-term     │       │
│  │  • Alerts        │   │  • ML models     │   │  • Compliance    │       │
│  │  • Dashboard     │   │  • Reports       │   │  • Export        │       │
│  └──────────────────┘   └──────────────────┘   └──────────────────┘       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Data Collection

### 1.1 Event Sources

| Source | Protocol | Volume | Latency |
|--------|----------|--------|---------|
| **SDK** | HTTPS POST | 70% | < 100ms |
| **Proxy** | Inline intercept | 25% | < 15ms |
| **Webhooks** | HTTPS POST | 5% | < 500ms |

### 1.2 Event Schema

```typescript
// Core usage event schema
interface UsageEvent {
  // Identity
  eventId: string;          // UUID v4
  eventType: EventType;     // 'api_call' | 'mcp_tool' | 'streaming'
  timestamp: string;        // ISO 8601

  // Context
  orgId: string;
  projectId: string;
  userId?: string;
  apiKeyId?: string;
  sessionId?: string;

  // Request details
  requestId: string;
  model: string;            // 'claude-3-opus' | 'claude-3-sonnet' | etc.
  endpoint: string;         // '/v1/messages' | '/v1/complete'

  // Token metrics
  inputTokens: number;
  outputTokens: number;
  cacheReadTokens?: number;
  cacheWriteTokens?: number;

  // Cost (in cents for precision)
  costCents: number;

  // Performance
  latencyMs: number;
  timeToFirstTokenMs?: number;
  tokensPerSecond?: number;

  // MCP specific
  mcpServerId?: string;
  mcpToolName?: string;
  mcpToolInput?: object;

  // Status
  status: 'success' | 'error' | 'timeout' | 'rate_limited';
  errorCode?: string;
  errorMessage?: string;

  // Metadata
  metadata: {
    clientVersion?: string;
    sdkVersion?: string;
    region?: string;
    environment?: 'production' | 'staging' | 'development';
  };
}

// Event types
enum EventType {
  API_CALL = 'api_call',
  MCP_TOOL = 'mcp_tool',
  STREAMING = 'streaming',
  SESSION_START = 'session_start',
  SESSION_END = 'session_end',
}
```

### 1.3 SDK Collection

```typescript
// MindWeave SDK - Usage tracking
import { MindWeave } from '@mindweave/sdk';

const mindweave = new MindWeave({
  apiKey: 'mw_sk_live_...',
  trackingEnabled: true,
  batchSize: 100,          // Events per batch
  flushInterval: 5000,      // Flush every 5 seconds
  maxRetries: 3,
});

// Automatic tracking wrapper
const claude = mindweave.wrapClient(anthropicClient);

// Manual event tracking
mindweave.track({
  eventType: 'api_call',
  model: 'claude-3-opus',
  inputTokens: 1500,
  outputTokens: 800,
  latencyMs: 2500,
  status: 'success',
});

// Flush on shutdown
process.on('SIGTERM', async () => {
  await mindweave.flush();
});
```

---

## 2. Ingestion Layer

### 2.1 Usage Tracker Service Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    USAGE TRACKER SERVICE (Go)                               │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      HTTP INGESTION                                  │   │
│  │                                                                      │   │
│  │  POST /v1/events                                                    │   │
│  │  POST /v1/events/batch                                              │   │
│  │                                                                      │   │
│  │  • TLS termination                                                  │   │
│  │  • API key validation                                               │   │
│  │  • Rate limiting (per project)                                      │   │
│  └─────────────────────────────────┬───────────────────────────────────┘   │
│                                    │                                        │
│  ┌─────────────────────────────────▼───────────────────────────────────┐   │
│  │                      VALIDATION                                      │   │
│  │                                                                      │   │
│  │  • Schema validation (JSON Schema)                                  │   │
│  │  • Required field checks                                            │   │
│  │  • Data type coercion                                               │   │
│  │  • Timestamp normalization                                          │   │
│  │  • Deduplication (event ID check)                                   │   │
│  └─────────────────────────────────┬───────────────────────────────────┘   │
│                                    │                                        │
│  ┌─────────────────────────────────▼───────────────────────────────────┐   │
│  │                      ENRICHMENT                                      │   │
│  │                                                                      │   │
│  │  • Cost calculation (based on model pricing)                        │   │
│  │  • Organization lookup                                              │   │
│  │  • Project metadata                                                 │   │
│  │  • User attribution                                                 │   │
│  │  • Geo-IP enrichment                                                │   │
│  └─────────────────────────────────┬───────────────────────────────────┘   │
│                                    │                                        │
│  ┌─────────────────────────────────▼───────────────────────────────────┐   │
│  │                      BUFFERING                                       │   │
│  │                                                                      │   │
│  │  • In-memory ring buffer (100K events)                              │   │
│  │  • Backpressure handling                                            │   │
│  │  • Batch accumulation                                               │   │
│  │  • Timeout-based flushing (1 second)                                │   │
│  └─────────────────────────────────┬───────────────────────────────────┘   │
│                                    │                                        │
│  ┌─────────────────────────────────▼───────────────────────────────────┐   │
│  │                      KAFKA PRODUCER                                  │   │
│  │                                                                      │   │
│  │  • Async batched writes                                             │   │
│  │  • Partitioning by org_id                                           │   │
│  │  • Compression (snappy)                                             │   │
│  │  • Delivery confirmation                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  PERFORMANCE TARGETS:                                                      │
│  • Throughput: 100,000 events/second                                      │
│  • Latency: < 10ms p99 (ingestion to Kafka)                              │
│  • Memory: < 2GB per instance                                             │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Cost Calculation

```go
// Pricing configuration (per 1M tokens, in cents)
type ModelPricing struct {
    InputPerMillion  int
    OutputPerMillion int
    CacheReadPer Million int
    CacheWritePerMillion int
}

var pricing = map[string]ModelPricing{
    "claude-3-opus": {
        InputPerMillion:  1500,  // $15.00
        OutputPerMillion: 7500,  // $75.00
        CacheReadPerMillion: 150, // $1.50
        CacheWritePerMillion: 1875, // $18.75
    },
    "claude-3-sonnet": {
        InputPerMillion:  300,   // $3.00
        OutputPerMillion: 1500,  // $15.00
        CacheReadPerMillion: 30,  // $0.30
        CacheWritePerMillion: 375, // $3.75
    },
    "claude-3-haiku": {
        InputPerMillion:  25,    // $0.25
        OutputPerMillion: 125,   // $1.25
        CacheReadPerMillion: 3,   // $0.03
        CacheWritePerMillion: 31, // $0.31
    },
}

func calculateCost(event *UsageEvent) int {
    price, ok := pricing[event.Model]
    if !ok {
        return 0
    }

    inputCost := (event.InputTokens * price.InputPerMillion) / 1_000_000
    outputCost := (event.OutputTokens * price.OutputPerMillion) / 1_000_000
    cacheReadCost := (event.CacheReadTokens * price.CacheReadPerMillion) / 1_000_000
    cacheWriteCost := (event.CacheWriteTokens * price.CacheWritePerMillion) / 1_000_000

    return inputCost + outputCost + cacheReadCost + cacheWriteCost
}
```

---

## 3. Streaming Layer

### 3.1 Kafka Configuration

```yaml
# Kafka topic configuration
topics:
  usage.events.raw:
    partitions: 12
    replication_factor: 3
    retention_ms: 604800000  # 7 days
    cleanup_policy: delete
    compression_type: snappy
    min_insync_replicas: 2

  usage.events.enriched:
    partitions: 12
    replication_factor: 3
    retention_ms: 604800000
    cleanup_policy: delete
    compression_type: snappy

  usage.aggregates.1min:
    partitions: 6
    replication_factor: 3
    retention_ms: 2592000000  # 30 days
    cleanup_policy: compact,delete

  usage.alerts:
    partitions: 3
    replication_factor: 3
    retention_ms: 86400000  # 1 day
    cleanup_policy: delete
```

### 3.2 Kafka Streams Processing

```java
// Real-time aggregation with Kafka Streams
public class UsageAggregator {

    public Topology buildTopology() {
        StreamsBuilder builder = new StreamsBuilder();

        // Source stream
        KStream<String, UsageEvent> events = builder.stream(
            "usage.events.enriched",
            Consumed.with(Serdes.String(), usageEventSerde)
        );

        // 1-minute aggregation
        KTable<Windowed<String>, UsageAggregate> minuteAggs = events
            .groupBy(
                (key, event) -> event.getOrgId() + ":" + event.getProjectId(),
                Grouped.with(Serdes.String(), usageEventSerde)
            )
            .windowedBy(TimeWindows.ofSizeWithNoGrace(Duration.ofMinutes(1)))
            .aggregate(
                UsageAggregate::new,
                (key, event, agg) -> agg.add(event),
                Materialized.<String, UsageAggregate, WindowStore<Bytes, byte[]>>as("minute-aggs")
                    .withKeySerde(Serdes.String())
                    .withValueSerde(usageAggregateSerde)
            );

        // Output to aggregates topic
        minuteAggs.toStream()
            .map((windowedKey, agg) -> {
                agg.setWindowStart(windowedKey.window().startTime());
                agg.setWindowEnd(windowedKey.window().endTime());
                return KeyValue.pair(windowedKey.key(), agg);
            })
            .to("usage.aggregates.1min", Produced.with(Serdes.String(), usageAggregateSerde));

        // Alerting stream
        events
            .filter((key, event) -> event.getStatus().equals("error"))
            .mapValues(event -> new UsageAlert(event))
            .to("usage.alerts", Produced.with(Serdes.String(), alertSerde));

        return builder.build();
    }
}

// Aggregate class
public class UsageAggregate {
    private String orgId;
    private String projectId;
    private Instant windowStart;
    private Instant windowEnd;

    private long requestCount = 0;
    private long successCount = 0;
    private long errorCount = 0;
    private long inputTokens = 0;
    private long outputTokens = 0;
    private long totalCostCents = 0;
    private long totalLatencyMs = 0;
    private long uniqueUsers = 0;

    private Set<String> userIds = new HashSet<>();
    private Map<String, Long> modelCounts = new HashMap<>();

    public UsageAggregate add(UsageEvent event) {
        requestCount++;
        if ("success".equals(event.getStatus())) {
            successCount++;
        } else {
            errorCount++;
        }
        inputTokens += event.getInputTokens();
        outputTokens += event.getOutputTokens();
        totalCostCents += event.getCostCents();
        totalLatencyMs += event.getLatencyMs();

        if (event.getUserId() != null) {
            userIds.add(event.getUserId());
        }
        uniqueUsers = userIds.size();

        modelCounts.merge(event.getModel(), 1L, Long::sum);

        return this;
    }
}
```

---

## 4. Batch Processing

### 4.1 Apache Spark Jobs

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       BATCH PROCESSING JOBS                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  JOB SCHEDULE:                                                             │
│  ─────────────                                                             │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Hourly Jobs (XX:15)                                                 │   │
│  │  • Hourly aggregation rollup                                         │   │
│  │  • Anomaly detection                                                 │   │
│  │  • Usage forecasting update                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Daily Jobs (01:00 UTC)                                              │   │
│  │  • Daily aggregation rollup                                          │   │
│  │  • Cost allocation                                                   │   │
│  │  • User analytics                                                    │   │
│  │  • MCP usage analysis                                                │   │
│  │  • Data archival to S3                                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Weekly Jobs (Sunday 02:00 UTC)                                      │   │
│  │  • Weekly summary generation                                         │   │
│  │  • ML model retraining                                               │   │
│  │  • Data retention enforcement                                        │   │
│  │  • Storage optimization                                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Monthly Jobs (1st, 06:00 UTC)                                       │   │
│  │  • Monthly billing aggregation                                       │   │
│  │  • Compliance reports                                                │   │
│  │  • Historical archive                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Daily Aggregation Job

```python
# daily_aggregation.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from datetime import datetime, timedelta

def run_daily_aggregation(date: str):
    spark = SparkSession.builder \
        .appName("MindWeave Daily Aggregation") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

    # Read from TimescaleDB
    raw_events = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://timescale:5432/mindweave") \
        .option("dbtable", f"""
            (SELECT * FROM usage_events
             WHERE time >= '{date}'
             AND time < '{date}'::date + interval '1 day') as events
        """) \
        .option("driver", "org.postgresql.Driver") \
        .load()

    # Aggregate by org, project, model, user
    daily_agg = raw_events.groupBy(
        F.date_trunc("day", "time").alias("date"),
        "org_id",
        "project_id",
        "model",
        "user_id"
    ).agg(
        F.count("*").alias("request_count"),
        F.sum(F.when(F.col("status") == "success", 1).otherwise(0)).alias("success_count"),
        F.sum(F.when(F.col("status") == "error", 1).otherwise(0)).alias("error_count"),
        F.sum("input_tokens").alias("total_input_tokens"),
        F.sum("output_tokens").alias("total_output_tokens"),
        F.sum("cost_cents").alias("total_cost_cents"),
        F.avg("latency_ms").alias("avg_latency_ms"),
        F.expr("percentile_approx(latency_ms, 0.5)").alias("p50_latency_ms"),
        F.expr("percentile_approx(latency_ms, 0.95)").alias("p95_latency_ms"),
        F.expr("percentile_approx(latency_ms, 0.99)").alias("p99_latency_ms"),
    )

    # Calculate derived metrics
    daily_agg = daily_agg.withColumn(
        "success_rate",
        F.col("success_count") / F.col("request_count") * 100
    ).withColumn(
        "cost_per_request_cents",
        F.col("total_cost_cents") / F.col("request_count")
    ).withColumn(
        "tokens_per_request",
        (F.col("total_input_tokens") + F.col("total_output_tokens")) / F.col("request_count")
    )

    # Write to daily aggregates table
    daily_agg.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://timescale:5432/mindweave") \
        .option("dbtable", "usage_daily") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    # Archive raw events to S3
    raw_events.write \
        .partitionBy("org_id") \
        .parquet(f"s3://mindweave-archive/usage-events/{date}/")

    spark.stop()

if __name__ == "__main__":
    import sys
    date = sys.argv[1] if len(sys.argv) > 1 else \
        (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
    run_daily_aggregation(date)
```

---

## 5. Data Storage

### 5.1 Storage Tiers

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         DATA STORAGE TIERS                                  │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  HOT TIER (TimescaleDB)                                                    │
│  ─────────────────────                                                     │
│  Retention: 7-30 days                                                      │
│  Use: Real-time queries, dashboards                                        │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  usage_events (hypertable)                                           │   │
│  │  • Raw events                                                        │   │
│  │  • Chunk interval: 1 day                                             │   │
│  │  • Compression: After 7 days                                         │   │
│  │  • Retention: 30 days                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  WARM TIER (TimescaleDB Continuous Aggregates)                             │
│  ─────────────────────────────────────────────                             │
│  Retention: 90 days - 1 year                                               │
│  Use: Analytics, reporting                                                 │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  usage_hourly (continuous aggregate)                                 │   │
│  │  • Hourly rollups                                                    │   │
│  │  • Retention: 90 days                                                │   │
│  │                                                                      │   │
│  │  usage_daily (continuous aggregate)                                  │   │
│  │  • Daily rollups                                                     │   │
│  │  • Retention: 1 year                                                 │   │
│  │                                                                      │   │
│  │  usage_monthly (continuous aggregate)                                │   │
│  │  • Monthly rollups                                                   │   │
│  │  • Retention: Forever                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  COLD TIER (S3)                                                            │
│  ─────────────                                                             │
│  Retention: 7 years (compliance)                                           │
│  Use: Compliance, audit, historical analysis                               │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  s3://mindweave-archive/                                             │   │
│  │  ├── usage-events/                                                   │   │
│  │  │   └── YYYY-MM-DD/                                                 │   │
│  │  │       └── org_id=xxx/                                             │   │
│  │  │           └── data.parquet                                        │   │
│  │  ├── audit-logs/                                                     │   │
│  │  └── compliance-reports/                                             │   │
│  │                                                                      │   │
│  │  Storage class: S3 Intelligent-Tiering                              │   │
│  │  Encryption: AES-256 (SSE-S3)                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Data Lifecycle Management

| Data Type | Hot (Fast Query) | Warm (Archive) | Cold (Compliance) |
|-----------|-----------------|-----------------|-------------------|
| Raw Events | 7 days | 30 days | 7 years |
| 1-min Aggregates | 7 days | - | - |
| Hourly Aggregates | 90 days | 1 year | - |
| Daily Aggregates | 1 year | 3 years | 7 years |
| Monthly Aggregates | Forever | - | - |
| Audit Logs | 90 days | 1 year | 7 years |

---

## 6. Real-Time Analytics

### 6.1 Dashboard Queries

```sql
-- Real-time dashboard query (last 24 hours)
WITH hourly_stats AS (
    SELECT
        time_bucket('1 hour', bucket) as hour,
        SUM(request_count) as requests,
        SUM(total_input_tokens + total_output_tokens) as tokens,
        SUM(total_cost_cents) / 100.0 as cost_usd,
        AVG(avg_latency_ms) as avg_latency
    FROM usage_hourly
    WHERE bucket >= NOW() - INTERVAL '24 hours'
      AND org_id = :org_id
    GROUP BY 1
    ORDER BY 1
)
SELECT
    hour,
    requests,
    tokens,
    cost_usd,
    avg_latency,
    -- Calculate change from previous hour
    requests - LAG(requests) OVER (ORDER BY hour) as request_change,
    cost_usd - LAG(cost_usd) OVER (ORDER BY hour) as cost_change
FROM hourly_stats;

-- Current usage vs budget
SELECT
    SUM(total_cost_cents) / 100.0 as current_spend_usd,
    :budget_usd as budget_usd,
    (SUM(total_cost_cents) / 100.0 / :budget_usd * 100) as percent_used,
    EXTRACT(DAY FROM (DATE_TRUNC('month', NOW()) + INTERVAL '1 month' - NOW())) as days_remaining
FROM usage_daily
WHERE bucket >= DATE_TRUNC('month', NOW())
  AND org_id = :org_id;

-- Top users by cost
SELECT
    u.name,
    u.email,
    SUM(ud.total_cost_cents) / 100.0 as total_cost_usd,
    SUM(ud.request_count) as total_requests,
    SUM(ud.total_input_tokens + ud.total_output_tokens) as total_tokens
FROM usage_daily ud
JOIN users u ON ud.user_id = u.id
WHERE ud.bucket >= NOW() - INTERVAL '30 days'
  AND ud.org_id = :org_id
GROUP BY u.id, u.name, u.email
ORDER BY total_cost_usd DESC
LIMIT 10;
```

### 6.2 Forecasting

```python
# Cost forecasting using Prophet
from prophet import Prophet
import pandas as pd

def forecast_usage(org_id: str, days_ahead: int = 30):
    # Load historical daily data
    df = load_daily_usage(org_id, days_back=90)

    # Prepare for Prophet
    prophet_df = df[['date', 'total_cost_usd']].rename(
        columns={'date': 'ds', 'total_cost_usd': 'y'}
    )

    # Fit model
    model = Prophet(
        yearly_seasonality=False,
        weekly_seasonality=True,
        daily_seasonality=False,
        changepoint_prior_scale=0.05
    )
    model.fit(prophet_df)

    # Make predictions
    future = model.make_future_dataframe(periods=days_ahead)
    forecast = model.predict(future)

    # Return forecasted values
    return {
        'projected_cost_usd': forecast.tail(days_ahead)['yhat'].sum(),
        'lower_bound': forecast.tail(days_ahead)['yhat_lower'].sum(),
        'upper_bound': forecast.tail(days_ahead)['yhat_upper'].sum(),
        'daily_forecast': forecast.tail(days_ahead)[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_dict('records')
    }
```

---

## 7. Data Quality

### 7.1 Validation Rules

| Rule | Check | Action on Failure |
|------|-------|-------------------|
| Schema validation | All required fields present | Reject event |
| Timestamp range | Within ±24 hours | Flag for review |
| Token bounds | 0 < tokens < 200,000 | Cap at bounds |
| Cost calculation | Matches expected for model | Recalculate |
| Deduplication | Event ID unique | Discard duplicate |
| Org/Project exists | Valid foreign keys | Route to DLQ |

### 7.2 Dead Letter Queue

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        DEAD LETTER QUEUE                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Events that fail processing are sent to DLQ for investigation:            │
│                                                                             │
│  Topic: usage.events.dlq                                                   │
│                                                                             │
│  {                                                                         │
│    "original_event": { ... },                                              │
│    "error": {                                                              │
│      "type": "VALIDATION_ERROR",                                           │
│      "message": "Missing required field: org_id",                          │
│      "timestamp": "2024-01-15T10:30:00Z"                                   │
│    },                                                                      │
│    "processing_attempts": 3,                                               │
│    "source_topic": "usage.events.raw"                                      │
│  }                                                                         │
│                                                                             │
│  DLQ HANDLING:                                                             │
│  • Auto-retry after 1 hour (max 3 attempts)                               │
│  • Alert after 100 events/hour                                            │
│  • Manual review dashboard                                                 │
│  • Weekly cleanup of unrecoverable events                                  │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Performance Optimization

### 8.1 Query Optimization

```sql
-- Create indexes for common query patterns
CREATE INDEX idx_usage_events_org_time
ON usage_events (org_id, time DESC);

CREATE INDEX idx_usage_events_project_time
ON usage_events (project_id, time DESC);

CREATE INDEX idx_usage_events_user_time
ON usage_events (user_id, time DESC)
WHERE user_id IS NOT NULL;

-- Continuous aggregate for faster queries
CREATE MATERIALIZED VIEW usage_hourly
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', time) AS bucket,
    org_id,
    project_id,
    model,
    COUNT(*) AS request_count,
    SUM(input_tokens) AS total_input_tokens,
    SUM(output_tokens) AS total_output_tokens,
    SUM(cost_cents) AS total_cost_cents,
    AVG(latency_ms) AS avg_latency_ms
FROM usage_events
GROUP BY bucket, org_id, project_id, model
WITH NO DATA;

-- Refresh policy
SELECT add_continuous_aggregate_policy('usage_hourly',
    start_offset => INTERVAL '3 hours',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour'
);
```

### 8.2 Performance Targets

| Metric | Target | Current |
|--------|--------|---------|
| Ingestion throughput | 100K events/sec | 120K events/sec |
| Ingestion latency (p99) | < 100ms | 45ms |
| Dashboard query (p95) | < 500ms | 320ms |
| Real-time aggregation lag | < 1 minute | 30 seconds |
| Daily batch job | < 30 minutes | 18 minutes |

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | System design |
| [DATABASE-SCHEMA.md](./DATABASE-SCHEMA.md) | Schema design |
| [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md) | Monitoring |
| [API-SPECIFICATIONS.md](./API-SPECIFICATIONS.md) | API contracts |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Engineering | Initial data pipeline design |

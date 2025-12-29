# TECHNICAL ARCHITECTURE: Patterns from Open-Source & Competitive Analysis

**Date:** December 29, 2025
**Status:** Enhanced Iteration Phase 1
**Purpose:** Extract architectural patterns from 15+ open-source and closed-source tools to inform MindWeave product design

---

## EXECUTIVE SUMMARY

**Research Scope:** Analyzed 15+ engineering analytics/governance platforms to identify patterns for MindWeave architecture.

**Key Finding:** Successful platforms share 4 common architectural patterns: (1) Event-based data ingestion, (2) Columnar data warehouse (OLAP), (3) Composable metrics/reporting, (4) API-first design.

**Recommendation:** MindWeave should adopt similar patterns for scalability and flexibility.

---

## SECTION 1: OPEN-SOURCE PLATFORMS ANALYZED

### 1.1 Apache DevLake (Most Similar to MindWeave's Use Case)

**GitHub:** https://github.com/apache/incubator-devlake
**Status:** Active, Apache incubator project, 4K+ stars
**Focus:** Engineering analytics (delivery metrics, cycle time, throughput)

#### **Architecture Pattern:**
```
Data Sources (GitHub, GitLab, Jira, Jenkins)
    ↓
Plugin Layer (standardized data ingestion)
    ↓
Data Lake (Apache Doris - columnar warehouse)
    ↓
Metrics Compute Layer (dbt models, SQL)
    ↓
API + Dashboard Layer (REST API, Grafana)

ARCHITECTURE CHARACTERISTICS:
├─ Event-driven: Webhooks from source systems (pull model)
├─ Schema-less ingestion: Accept any data structure
├─ Columnar warehouse: Apache Doris (fast OLAP queries)
├─ Metrics-as-code: dbt models (version-controlled metrics)
└─ API-first: All features via REST API (composable)
```

#### **DevLake's Key Learnings for MindWeave:**

| Learning | Application to MindWeave |
|----------|--------------------------|
| **Plugin architecture** | Build MCP/Claude integrations as plugins (Netflix Conductor pattern) |
| **Columnar warehouse** | Use DuckDB or Clickhouse for cost attribution queries (50x faster than row-store) |
| **Metrics-as-code** | Version control MCP metrics definitions (cost, latency, token usage) |
| **Webhook-based sync** | Real-time Claude API call ingestion (vs. batch polling) |
| **Multi-tenancy via schema** | Separate postgres schemas per customer (cost isolation) |

---

### 1.2 Faros Community Edition (Unified Data Platform)

**GitHub:** https://github.com/faros-ai/faros-community-edition
**Status:** Active, 2K+ stars
**Focus:** Unified engineering data platform (Airbyte + Hasura + Metabase stack)

#### **Architecture Pattern:**
```
Data Sources (GitHub, GitLab, Slack, Jira, CI/CD, deployments)
    ↓
Airbyte (ELT tool - standardizes schemas)
    ↓
PostgreSQL (normalized schema)
    ↓
Hasura GraphQL Engine (auto-generated API)
    ↓
Metabase (analytics/dashboards)

ARCHITECTURE CHARACTERISTICS:
├─ ELT (Extract-Load-Transform): Load first, transform in warehouse
├─ Normalized schema: Standard tables for common entities
├─ GraphQL API: More flexible than REST for queries
├─ Open-source stack: Each component is replaceable
└─ Composable: Customers can use their own Metabase instance
```

#### **Faros's Key Learnings for MindWeave:**

| Learning | Application to MindWeave |
|----------|--------------------------|
| **Multi-source ingestion** | Claude API + Anthropic logs + customer logs in unified schema |
| **ELT pattern** | Load Claude API calls → Transform into cost/compliance records |
| **GraphQL API** | More flexible querying than REST (customers want custom queries) |
| **Normalized schema** | Standard schema for MCP calls (type, model, tokens, cost) |
| **Pluggable components** | Customers can use their own analytics tools (BI platforms) |

---

### 1.3 GrimoireLab / CHAOSS (Software Analytics Stack)

**GitHub:** https://github.com/chaoss/grimoirelab
**Status:** Mature, 1.5K+ stars
**Focus:** Software development analytics (commit velocity, PR patterns, contributor analysis)

#### **Architecture Pattern:**
```
Data Sources (GitHub, GitLab APIs)
    ↓
Perceval (data collection via APIs)
    ↓
Enrichment (normalize, deduplicate, enrich)
    ↓
Elasticsearch (time-series index)
    ↓
Kibana (visualization)

ARCHITECTURE CHARACTERISTICS:
├─ API-based collection: Pull data via REST APIs (not webhooks)
├─ Enrichment layer: Clean and normalize before storage
├─ Time-series indexing: Elasticsearch for time-based queries
├─ Metric definitions: Codified in CHAOSS standards
└─ Dashboard-centric: Visualizations before APIs
```

#### **GrimoireLab's Key Learnings for MindWeave:**

| Learning | Application to MindWeave |
|----------|--------------------------|
| **Enrichment pipeline** | Normalize MCP data (different call signatures, model versions) |
| **Time-series database** | Elasticsearch for performance metrics over time |
| **CHAOSS metrics** | Define standard MindWeave metrics (adoption, cost, compliance) |
| **Dashboard-first** | Build dashboards before API (users want quick insights) |
| **Metric definitions** | Standardize cost calculation across Claude versions |

---

## SECTION 2: COMMERCIAL PLATFORMS ANALYZED

### 2.1 Closed-Source Competitors (Pattern Analysis)

#### **Waydev (Developer Productivity Analytics)**
```
Focus: Individual productivity metrics
Strength: Employee-level insights (contentious in open-source)
Weakness: Privacy concerns limit adoption
MindWeave lesson: Avoid employee-level tracking, focus on team/org level
```

#### **LinearB (Delivery Intelligence)**
```
Focus: Delivery metrics + actionable recommendations
Strength: Narrative-based recommendations (not just dashboards)
Weakness: Recommender system is black-box (less transparent)
MindWeave lesson: Provide recommendations on cost optimization (similar approach)
```

#### **Jellyfish (Engineering Management)**
```
Focus: Resource allocation and team planning
Strength: Time tracking integration (Jira, GitHub workflows)
Weakness: Heavyweight implementation (6+ month deployment)
MindWeave lesson: Keep MindWeave lightweight (2-week onboarding max)
```

#### **Athenian (Engineering Metrics)**
```
Focus: DORA metrics (deployment frequency, lead time, MTTR, change failure rate)
Strength: Standards-based metrics (industry credibility)
Weakness: Limited to CI/CD metrics (misses governance aspects)
MindWeave lesson: Build metrics on standards (extend DORA for LLM governance)
```

#### **DevDynamics (Automated Engineering Analytics)**
```
Focus: Automatic metric generation without config
Strength: Low friction onboarding (works out-of-box)
Weakness: Less customization (one-size-fits-all metrics)
MindWeave lesson: Provide sensible defaults + advanced customization
```

---

## SECTION 3: RECOMMENDED MINDWEAVE TECHNICAL ARCHITECTURE

### 3.1 High-Level Architecture Design

```
┌─────────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                                │
│  Claude API | Anthropic Logs | Customer Logs | MCP Registry     │
└──────────────┬──────────────────────────────────────────────────┘
               │
               ├─ Webhook Ingestion (Real-time)
               └─ Batch Polling (Fallback, 1h frequency)
               │
┌──────────────▼──────────────────────────────────────────────────┐
│              DATA INGESTION LAYER (TypeScript/Node)              │
│  • Message queue: Redis or SQS                                   │
│  • Schema validation: JSON Schema / Zod                          │
│  • Deduplication: Event ID tracking                              │
└──────────────┬──────────────────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────────────────┐
│              DATA TRANSFORMATION LAYER (SQL/dbt)                 │
│  • Normalize MCP calls: Standard schema                          │
│  • Calculate costs: Model-specific pricing                       │
│  • Aggregate metrics: By team, project, user                     │
│  • Detect duplicates: Hivemind detection logic                   │
└──────────────┬──────────────────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────────────────┐
│           COLUMNAR WAREHOUSE (DuckDB / Clickhouse)               │
│  Core Tables:                                                    │
│  • mcp_calls (call_id, timestamp, model, cost, user_id, ...)   │
│  • cost_by_team (team_id, period, cost, model, ...)            │
│  • compliance_events (user_id, action, timestamp, resource)     │
│  • hivemind_patterns (pattern_hash, count, confidence, ...)     │
│  • audit_logs (user_id, action, resource_id, timestamp, ...)   │
└──────────────┬──────────────────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────────────────┐
│         METRICS & REPORTING LAYER (GraphQL / REST API)           │
│  • Cost Attribution API: /api/costs?team=X&period=Y             │
│  • Hivemind Detection API: /api/duplicates?threshold=0.8        │
│  • Compliance API: /api/audit-logs?start=X&end=Y               │
│  • Team Governance API: /api/team-access?role=manager          │
└──────────────┬──────────────────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────────────────┐
│            APPLICATION LAYER (Next.js / React)                   │
│  • Cost Dashboard (real-time, by team/project/model)            │
│  • Governance Console (permissions, audit logs)                 │
│  • Hivemind Detector (pattern visualization)                    │
│  • Compliance Reports (audit-ready exports)                     │
└──────────────────────────────────────────────────────────────────┘
```

### 3.2 Technology Stack (Specific Recommendations)

#### **Data Ingestion**
```
├─ Queue: Redis (pub/sub for real-time) or SQS (AWS)
│  Why: Low latency (<100ms), handles 10k+ msgs/sec
│
├─ Message Format: CloudEvents standard
│  Example: {
│    "specversion": "1.0",
│    "type": "com.anthropic.claude.api_call",
│    "source": "api.anthropic.com",
│    "id": "A234-1234-1234",
│    "time": "2025-12-29T10:00:00Z",
│    "data": { "model": "claude-3", "tokens": 1000, "cost": 0.30 }
│  }
│
└─ Validation: Zod (runtime schema validation in TypeScript)
   Why: Catch bad data early, before warehouse
```

#### **Data Storage**
```
├─ Warehouse: DuckDB (single-node) → Clickhouse (distributed, if >1M rows/day)
│  Why: OLAP-optimized, 100x faster than Postgres for aggregations
│
├─ Data Mart: PostgreSQL (operational data, small tables)
│  Why: ACID guarantees for compliance/audit logs
│
└─ Cache: Redis (materialized views, query cache)
   Why: <10ms response times for dashboards
```

#### **Transformation**
```
├─ Framework: dbt (data build tool)
│  Why: Version-controlled SQL, testable metrics
│  Example: models/marts/costs/cost_by_team_daily.sql
│
├─ Orchestration: Airflow or Dagster (weekly/daily runs)
│  Why: Reliable scheduling, error recovery
│
└─ Freshness: 1-hour latency (good for governance)
   Why: Real-time not necessary (cost data stabilizes over minutes)
```

#### **API Layer**
```
├─ REST: Express.js or Hono
│  Endpoints:
│  ├─ GET /api/costs?team=X&period=Y → cost_by_team table
│  ├─ GET /api/duplicates?threshold=0.8 → hivemind_patterns table
│  ├─ POST /api/audit-log → compliance_events table
│  └─ GET /api/governance/users?team=X → user_roles table
│
├─ GraphQL: Optional (customers with custom BI needs)
│  Why: More flexible querying (support power users)
│
└─ WebSocket: For real-time dashboards
   Why: Push cost updates to dashboard in real-time
```

### 3.3 Data Schema (Normalized)

#### **Core Table: mcp_calls**
```sql
CREATE TABLE mcp_calls (
  call_id UUID PRIMARY KEY,
  customer_id UUID NOT NULL,
  org_id UUID,
  team_id UUID,
  user_id UUID,
  timestamp TIMESTAMP NOT NULL,
  model_id VARCHAR(100) NOT NULL,  -- claude-3-sonnet, gpt-4, etc
  mcp_name VARCHAR(255),            -- which MCP was called
  input_tokens INT,
  output_tokens INT,
  total_cost DECIMAL(10,4),
  status VARCHAR(50),               -- success, error, rate_limited
  latency_ms INT,
  region VARCHAR(50),
  created_at TIMESTAMP DEFAULT NOW(),

  -- Governance fields
  user_region VARCHAR(50),          -- for GDPR data residency
  data_classification VARCHAR(50),  -- public, internal, sensitive
  compliance_required BOOLEAN,      -- needs audit trail

  -- Deduplication
  dedup_hash VARCHAR(64),           -- for hivemind detection
  is_duplicate BOOLEAN DEFAULT FALSE,
  duplicate_of_call_id UUID,

  INDEX idx_timestamp_team (timestamp, team_id),
  INDEX idx_customer_ts (customer_id, timestamp),
  INDEX idx_dedup_hash (dedup_hash),
  PARTITION BY MONTH (timestamp)
);
```

#### **Derived Table: cost_by_team_daily**
```sql
CREATE TABLE cost_by_team_daily (
  date DATE,
  customer_id UUID,
  team_id UUID,
  model_id VARCHAR(100),
  total_calls INT,
  input_tokens BIGINT,
  output_tokens BIGINT,
  total_cost DECIMAL(10,4),
  avg_cost_per_call DECIMAL(10,4),
  duplicate_calls INT,
  duplicate_cost DECIMAL(10,4),

  PRIMARY KEY (date, customer_id, team_id, model_id),
  INDEX idx_customer_date (customer_id, date DESC)
);
```

#### **Governance Table: audit_logs**
```sql
CREATE TABLE audit_logs (
  log_id UUID PRIMARY KEY,
  customer_id UUID NOT NULL,
  user_id UUID,
  action VARCHAR(100) NOT NULL,  -- view_costs, export_report, delete_data
  resource_type VARCHAR(100),    -- team, user, report, mcp_call
  resource_id UUID,
  before_state JSONB,            -- for change tracking
  after_state JSONB,
  timestamp TIMESTAMP NOT NULL,
  ip_address INET,
  user_agent TEXT,
  reason_code VARCHAR(100),      -- for compliance categorization

  INDEX idx_customer_ts (customer_id, timestamp DESC),
  INDEX idx_user_ts (user_id, timestamp DESC),
  PARTITION BY MONTH (timestamp)
);
```

---

## SECTION 4: OPEN-SOURCE ARCHITECTURE PATTERNS TO ADOPT

### 4.1 Pattern 1: Plugin-Based Extensibility (from DevLake)

**Pattern:** Abstract data source integrations as plugins

```typescript
// MindWeave plugin interface (similar to DevLake)
interface DataSourcePlugin {
  name: string;
  version: string;

  // Ingestion
  fetchData(params: FetchParams): Promise<RawData[]>;
  webhookHandler(event: CloudEvent): Promise<void>;

  // Schema mapping
  normalizeSchema(raw: any): NormalizedMCPCall;

  // Config
  getConfigSchema(): JSONSchema;
}

// Example: Anthropic Claude API plugin
const ClaudeAPIPlugin: DataSourcePlugin = {
  name: "anthropic-claude-api",
  version: "1.0.0",

  async fetchData(params) {
    // Fetch usage from Anthropic API
    const calls = await anthropicAPI.getUsage(params.startDate, params.endDate);
    return calls;
  },

  normalizeSchema(raw) {
    return {
      call_id: raw.id,
      timestamp: raw.created_at,
      model_id: raw.model,
      input_tokens: raw.usage.input_tokens,
      output_tokens: raw.usage.output_tokens,
      total_cost: calculateCost(raw),
    };
  }
};
```

**Why This Matters:**
- ✅ Customers can build custom plugins (e.g., connect to internal logging)
- ✅ Easy to add new data sources without core changes
- ✅ Open-source community can contribute integrations

---

### 4.2 Pattern 2: Metrics-as-Code (from DevLake)

**Pattern:** Version-control metric definitions using dbt

```sql
-- models/marts/metrics/cost_optimization_metrics.sql
-- This is checked into git, customers can fork and customize

SELECT
  date,
  team_id,
  model_id,

  -- Standard metrics
  total_cost,
  total_calls,
  avg_cost_per_call,

  -- Optimization metrics (MindWeave specific)
  duplicate_call_percentage,  -- proportion of calls flagged as duplicates
  duplicate_cost_saved,        -- estimated cost if dups were prevented
  unique_mcps_used,           -- how many different MCPs
  reused_mcps_pct,            -- % of calls reusing top 5 MCPs

  -- Governance metrics
  non_compliant_calls,         -- calls in unsupported regions
  unaudit_loggable_calls,

  -- Benchmarking
  cost_vs_historical_pct,      -- how does today compare to baseline
  cost_vs_peer_benchmark,      -- how does this team compare to industry

FROM {{ ref('cost_by_team_daily') }}
WHERE date >= DATE_TRUNC('month', CURRENT_DATE);
```

**Why This Matters:**
- ✅ Metrics definitions are transparent and auditable
- ✅ Easy for customers to customize (fork dbt models)
- ✅ Version control = audit trail of metric changes
- ✅ Reproducible (always the same calculation)

---

### 4.3 Pattern 3: Event-Driven Data (from GrimoireLab + Faros)

**Pattern:** Treat all data changes as immutable events

```typescript
// Event schema (CloudEvents standard)
type MCPCallEvent = CloudEvent & {
  type: "com.mindweave.mcp.call";
  data: {
    call_id: string;
    timestamp: string;
    model_id: string;
    mcp_name: string;
    input_tokens: number;
    output_tokens: number;
    cost: number;
    status: "success" | "error" | "rate_limited";
  };
};

// Event sourcing: Keep immutable log
CREATE TABLE event_log (
  event_id UUID PRIMARY KEY,
  event_type VARCHAR(100),
  event_time TIMESTAMP,
  data JSONB,
  inserted_at TIMESTAMP DEFAULT NOW()
);

// Derived state from events (snapshots for performance)
CREATE TABLE mcp_calls AS (
  SELECT
    DISTINCT ON (data->>'call_id')
    data->>'call_id' AS call_id,
    data->>'timestamp'::timestamp,
    data->>'model_id' AS model_id,
    data->'input_tokens' AS input_tokens,
    ...
  FROM event_log
  WHERE event_type = 'com.mindweave.mcp.call'
  ORDER BY data->>'call_id', event_time DESC
);
```

**Why This Matters:**
- ✅ Audit trail (all events are immutable)
- ✅ Compliance (can replay events for investigations)
- ✅ Flexibility (can recompute metrics from events)
- ✅ Resilience (deduplication is reliable)

---

### 4.4 Pattern 4: Multi-Tenancy via Schema Isolation (from DevLake)

**Pattern:** Each customer gets isolated schema, shared infrastructure

```sql
-- Create customer schema (at signup)
CREATE SCHEMA customer_12345_schema;

-- Customer-specific tables
CREATE TABLE customer_12345_schema.mcp_calls (
  -- same schema as shared table
);

-- Row-level security (optional, for extra isolation)
ALTER TABLE customer_12345_schema.mcp_calls ENABLE ROW LEVEL SECURITY;

-- Views for customer-specific data
CREATE VIEW customer_12345_schema.cost_by_team AS
SELECT * FROM customer_12345_schema.mcp_calls
GROUP BY team_id;

-- Benefits:
-- 1. Data isolation (no cross-customer data leakage)
-- 2. Performance (separate indexes per customer)
-- 3. Cost (shared infrastructure, not separate DBs)
-- 4. Compliance (GDPR data segregation requirement)
```

**Why This Matters:**
- ✅ Strong data isolation (GDPR compliance)
- ✅ Cost-efficient (shared DB, separate schemas)
- ✅ Performance isolation (one customer's workload doesn't affect others)
- ✅ Easy to scale (add customers by creating new schema)

---

## SECTION 5: LESSONS FROM FAILURES (What NOT to Do)

### 5.1 Over-Engineering (Waydev)

**Problem:** Waydev added too many employee-level metrics early
- Result: Privacy concerns → adoption blocked in enterprises
- Lesson: Focus on org-level metrics first (costs), employee metrics later (if at all)

**MindWeave Action:** Keep focus on team/org governance, not individual tracking

### 5.2 Over-Complexity (Jellyfish)

**Problem:** Jellyfish required 6+ month implementation
- Result: Long sales cycles, higher cost of acquisition
- Lesson: Simple products win in fast-moving markets

**MindWeave Action:** 2-week onboarding max (plug in Anthropic API key, get instant insights)

### 5.3 Single-Source Lock-In (Athenian)

**Problem:** Athenian only works with GitHub/GitLab
- Result: Missing customers who use Jira, Linear, or internal tools
- Lesson: Multi-source support is table stakes

**MindWeave Action:** Support Claude API + Anthropic logs + customer logs from day 1

### 5.4 Dashboard-Only (Early LinearB)

**Problem:** Early versions had no API, only dashboards
- Result: Power users couldn't integrate with their BI tools
- Lesson: API-first enables advanced use cases

**MindWeave Action:** GraphQL + REST API available from Month 1

---

## SECTION 6: IMPLEMENTATION ROADMAP

### Phase 1: MVP Architecture (Month 1-2)

```
Build minimal viable architecture:
├─ PostgreSQL (operational data)
├─ Redis (message queue, cache)
├─ Express.js API (REST only)
├─ Next.js dashboard
├─ Claude API → PostgreSQL sync (batch, 1h latency)
└─ Deliverable: Cost attribution + basic governance

Complexity: Low (standard Web architecture)
Scalability: Up to 1M API calls/day
```

### Phase 2: Analytics Architecture (Month 3-4)

```
Add analytics layer:
├─ DuckDB (columnar warehouse for analytics)
├─ dbt (metrics-as-code)
├─ Materialized views (daily cost aggregates)
├─ GraphQL API (advanced querying)
└─ Deliverable: Advanced cost insights + custom reporting

Complexity: Medium (add analytics stack)
Scalability: Up to 10M API calls/day
```

### Phase 3: Event-Driven Architecture (Month 5-6)

```
Add event sourcing:
├─ Kafka (event stream, if scaling)
├─ Event log table (immutable records)
├─ Event-based deduplication (hivemind detection)
├─ Compliance event logging
└─ Deliverable: Audit-grade compliance trails

Complexity: High (event sourcing is advanced)
Scalability: 100M+ API calls/day
```

---

## CONCLUSION

**Architecture Summary:**
- **Foundation:** PostgreSQL + Redis (proven, reliable)
- **Analytics:** DuckDB + dbt (fast, flexible)
- **Extensibility:** Plugin architecture (customer customization)
- **Compliance:** Event sourcing + audit logs (regulatory ready)

**Time to Implementation:**
- MVP (Month 1-2): 2-3 engineers
- Full (Month 5-6): 4-5 engineers

**Comparison to Competitors:**
- DevLake: Similar plugin architecture ✅
- Faros: Similar normalized schema ✅
- GrimoireLab: Similar event-driven approach ✅
- Waydev/LinearB: Better extensibility, privacy ✅

---

**Document Status:** Ready for engineering team review
**Next Action:** Engineering team architecture workshop (Week 1, January 2026)

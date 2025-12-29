# MindWeave Monitoring & Observability

## Document Information

| Field | Value |
|-------|-------|
| Document ID | MW-ENG-071 |
| Version | 1.0.0 |
| Last Updated | 2025-01-15 |
| Owner | Platform Engineering |
| Classification | Internal |
| Status | Active |

---

## Executive Summary

This document defines MindWeave's monitoring and observability strategy, covering the three pillars of observability: metrics, logs, and traces. Our approach ensures complete visibility into system behavior, enabling rapid incident detection, root cause analysis, and proactive performance optimization.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OBSERVABILITY ARCHITECTURE                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        DATA COLLECTION                               │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                       │   │
│  │   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐    │   │
│  │   │  Metrics  │   │   Logs    │   │  Traces   │   │  Events   │    │   │
│  │   │           │   │           │   │           │   │           │    │   │
│  │   │ Prometheus│   │  Fluent   │   │  Jaeger   │   │  Custom   │    │   │
│  │   │   Agent   │   │    Bit    │   │   Agent   │   │  Emitter  │    │   │
│  │   └─────┬─────┘   └─────┬─────┘   └─────┬─────┘   └─────┬─────┘    │   │
│  │         │               │               │               │          │   │
│  └─────────┼───────────────┼───────────────┼───────────────┼──────────┘   │
│            │               │               │               │              │
│            ▼               ▼               ▼               ▼              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     DATA AGGREGATION                                 │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                       │   │
│  │   ┌───────────────────────────────────────────────────────────┐     │   │
│  │   │                     DataDog Agent                          │     │   │
│  │   │                                                            │     │   │
│  │   │  • DogStatsD (metrics)    • Log forwarding               │     │   │
│  │   │  • APM tracing            • Process monitoring           │     │   │
│  │   │  • Network monitoring     • Container metrics            │     │   │
│  │   └───────────────────────────────────────────────────────────┘     │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                       VISUALIZATION & ALERTING                       │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                       │   │
│  │   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐    │   │
│  │   │ Dashboards│   │  Alerts   │   │   SLOs    │   │  Runbooks │    │   │
│  │   │           │   │           │   │           │   │           │    │   │
│  │   │ • Service │   │ • Slack   │   │ • Error   │   │ • Auto    │    │   │
│  │   │ • Infra   │   │ • PagerD  │   │   Rate    │   │   Link    │    │   │
│  │   │ • Business│   │ • Email   │   │ • Latency │   │           │    │   │
│  │   └───────────┘   └───────────┘   └───────────┘   └───────────┘    │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Metrics Collection

### 1.1 Prometheus Configuration

```yaml
# prometheus/prometheus.yaml

global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: mindweave-production
    region: us-east-1

rule_files:
  - /etc/prometheus/rules/*.yaml

alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - alertmanager:9093

scrape_configs:
  # Kubernetes API Server
  - job_name: 'kubernetes-apiservers'
    kubernetes_sd_configs:
      - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
        action: keep
        regex: default;kubernetes;https

  # Kubernetes Nodes
  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
      - role: node
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)

  # Kubernetes Pods
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: kubernetes_pod_name

  # Service Monitors
  - job_name: 'mindweave-services'
    kubernetes_sd_configs:
      - role: service
        namespaces:
          names:
            - mindweave-services
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_port]
        action: replace
        target_label: __meta_kubernetes_pod_container_port_number
```

### 1.2 Application Metrics

```typescript
// src/metrics/metrics.service.ts

import { Counter, Histogram, Gauge, Registry } from 'prom-client';

// Create custom registry
const register = new Registry();

// Default metrics
import { collectDefaultMetrics } from 'prom-client';
collectDefaultMetrics({ register });

// HTTP Request Metrics
export const httpRequestsTotal = new Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'path', 'status_code'],
  registers: [register],
});

export const httpRequestDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration in seconds',
  labelNames: ['method', 'path', 'status_code'],
  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10],
  registers: [register],
});

// Business Metrics
export const apiCallsTotal = new Counter({
  name: 'mindweave_api_calls_total',
  help: 'Total Claude API calls tracked',
  labelNames: ['org_id', 'project_id', 'model', 'status'],
  registers: [register],
});

export const tokensProcessed = new Counter({
  name: 'mindweave_tokens_processed_total',
  help: 'Total tokens processed',
  labelNames: ['org_id', 'model', 'token_type'],
  registers: [register],
});

export const costAccrued = new Counter({
  name: 'mindweave_cost_cents_total',
  help: 'Total cost accrued in cents',
  labelNames: ['org_id', 'project_id', 'model'],
  registers: [register],
});

// MCP Server Metrics
export const mcpServersActive = new Gauge({
  name: 'mindweave_mcp_servers_active',
  help: 'Number of active MCP servers',
  labelNames: ['org_id', 'transport_type'],
  registers: [register],
});

export const mcpToolInvocations = new Counter({
  name: 'mindweave_mcp_tool_invocations_total',
  help: 'Total MCP tool invocations',
  labelNames: ['org_id', 'server_id', 'tool_name', 'status'],
  registers: [register],
});

// Governance Metrics
export const policyEvaluations = new Counter({
  name: 'mindweave_policy_evaluations_total',
  help: 'Total policy evaluations',
  labelNames: ['org_id', 'policy_type', 'result'],
  registers: [register],
});

export const policyViolations = new Counter({
  name: 'mindweave_policy_violations_total',
  help: 'Total policy violations',
  labelNames: ['org_id', 'policy_id', 'severity'],
  registers: [register],
});

// Database Metrics
export const dbQueryDuration = new Histogram({
  name: 'db_query_duration_seconds',
  help: 'Database query duration in seconds',
  labelNames: ['query_type', 'table'],
  buckets: [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5],
  registers: [register],
});

export const dbConnectionPool = new Gauge({
  name: 'db_connection_pool_size',
  help: 'Database connection pool size',
  labelNames: ['pool', 'state'],
  registers: [register],
});

// Redis Metrics
export const redisOperations = new Counter({
  name: 'redis_operations_total',
  help: 'Total Redis operations',
  labelNames: ['operation', 'status'],
  registers: [register],
});

export const redisLatency = new Histogram({
  name: 'redis_operation_duration_seconds',
  help: 'Redis operation duration in seconds',
  labelNames: ['operation'],
  buckets: [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1],
  registers: [register],
});

// Kafka Metrics
export const kafkaMessagesProduced = new Counter({
  name: 'kafka_messages_produced_total',
  help: 'Total Kafka messages produced',
  labelNames: ['topic'],
  registers: [register],
});

export const kafkaMessagesConsumed = new Counter({
  name: 'kafka_messages_consumed_total',
  help: 'Total Kafka messages consumed',
  labelNames: ['topic', 'consumer_group'],
  registers: [register],
});

export const kafkaConsumerLag = new Gauge({
  name: 'kafka_consumer_lag',
  help: 'Kafka consumer lag',
  labelNames: ['topic', 'partition', 'consumer_group'],
  registers: [register],
});

// Export registry
export { register };

// Metrics endpoint handler
export async function metricsHandler(req: Request, res: Response) {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
}
```

### 1.3 Custom Metrics Instrumentation

```typescript
// src/metrics/instrumentation.ts

import {
  httpRequestsTotal,
  httpRequestDuration,
  apiCallsTotal,
  tokensProcessed,
  costAccrued,
  mcpToolInvocations,
  policyEvaluations,
} from './metrics.service';

// HTTP Request Middleware
export function metricsMiddleware(req: Request, res: Response, next: NextFunction) {
  const startTime = Date.now();
  const path = normalizePath(req.path);

  res.on('finish', () => {
    const duration = (Date.now() - startTime) / 1000;
    const labels = {
      method: req.method,
      path,
      status_code: res.statusCode.toString(),
    };

    httpRequestsTotal.inc(labels);
    httpRequestDuration.observe(labels, duration);
  });

  next();
}

// Normalize path for metric labels (avoid high cardinality)
function normalizePath(path: string): string {
  return path
    .replace(/\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/gi, '/:id')
    .replace(/\/\d+/g, '/:id')
    .replace(/\/mw_[a-z]+_[a-zA-Z0-9]+/g, '/:key');
}

// Track API call
export function trackApiCall(params: {
  orgId: string;
  projectId: string;
  model: string;
  inputTokens: number;
  outputTokens: number;
  costCents: number;
  status: 'success' | 'error';
}) {
  const { orgId, projectId, model, inputTokens, outputTokens, costCents, status } = params;

  apiCallsTotal.inc({
    org_id: orgId,
    project_id: projectId,
    model,
    status,
  });

  tokensProcessed.inc(
    { org_id: orgId, model, token_type: 'input' },
    inputTokens
  );

  tokensProcessed.inc(
    { org_id: orgId, model, token_type: 'output' },
    outputTokens
  );

  costAccrued.inc(
    { org_id: orgId, project_id: projectId, model },
    costCents
  );
}

// Track MCP tool invocation
export function trackMcpToolInvocation(params: {
  orgId: string;
  serverId: string;
  toolName: string;
  status: 'success' | 'error' | 'timeout';
}) {
  mcpToolInvocations.inc({
    org_id: params.orgId,
    server_id: params.serverId,
    tool_name: params.toolName,
    status: params.status,
  });
}

// Track policy evaluation
export function trackPolicyEvaluation(params: {
  orgId: string;
  policyType: 'usage' | 'access' | 'compliance';
  result: 'allow' | 'deny' | 'warn';
}) {
  policyEvaluations.inc({
    org_id: params.orgId,
    policy_type: params.policyType,
    result: params.result,
  });
}
```

---

## 2. Distributed Tracing

### 2.1 OpenTelemetry Configuration

```typescript
// src/tracing/tracing.ts

import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-grpc';
import { Resource } from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-node';
import { PeriodicExportingMetricReader } from '@opentelemetry/sdk-metrics';
import { W3CTraceContextPropagator } from '@opentelemetry/core';
import { HttpInstrumentation } from '@opentelemetry/instrumentation-http';
import { ExpressInstrumentation } from '@opentelemetry/instrumentation-express';
import { PgInstrumentation } from '@opentelemetry/instrumentation-pg';
import { RedisInstrumentation } from '@opentelemetry/instrumentation-redis-4';
import { KafkaJsInstrumentation } from '@opentelemetry/instrumentation-kafkajs';

const serviceName = process.env.SERVICE_NAME || 'api-gateway';
const serviceVersion = process.env.SERVICE_VERSION || '1.0.0';
const environment = process.env.NODE_ENV || 'development';

// Configure resource attributes
const resource = new Resource({
  [SemanticResourceAttributes.SERVICE_NAME]: serviceName,
  [SemanticResourceAttributes.SERVICE_VERSION]: serviceVersion,
  [SemanticResourceAttributes.DEPLOYMENT_ENVIRONMENT]: environment,
  [SemanticResourceAttributes.SERVICE_NAMESPACE]: 'mindweave',
  'cloud.provider': 'aws',
  'cloud.region': process.env.AWS_REGION || 'us-east-1',
});

// Configure trace exporter
const traceExporter = new OTLPTraceExporter({
  url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT || 'http://otel-collector:4317',
});

// Configure metric exporter
const metricExporter = new OTLPMetricExporter({
  url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT || 'http://otel-collector:4317',
});

// Initialize SDK
const sdk = new NodeSDK({
  resource,
  traceExporter,
  metricReader: new PeriodicExportingMetricReader({
    exporter: metricExporter,
    exportIntervalMillis: 60000,
  }),
  spanProcessor: new BatchSpanProcessor(traceExporter, {
    maxQueueSize: 2048,
    maxExportBatchSize: 512,
    scheduledDelayMillis: 5000,
    exportTimeoutMillis: 30000,
  }),
  textMapPropagator: new W3CTraceContextPropagator(),
  instrumentations: [
    new HttpInstrumentation({
      ignoreIncomingRequestHook: (req) => {
        // Ignore health checks
        return req.url === '/health/live' || req.url === '/health/ready';
      },
    }),
    new ExpressInstrumentation(),
    new PgInstrumentation({
      enhancedDatabaseReporting: true,
    }),
    new RedisInstrumentation(),
    new KafkaJsInstrumentation(),
  ],
});

// Start SDK
export async function initTracing(): Promise<void> {
  try {
    await sdk.start();
    console.log('OpenTelemetry tracing initialized');

    // Graceful shutdown
    process.on('SIGTERM', () => {
      sdk.shutdown()
        .then(() => console.log('Tracing terminated'))
        .catch((error) => console.error('Error terminating tracing', error))
        .finally(() => process.exit(0));
    });
  } catch (error) {
    console.error('Error initializing tracing', error);
  }
}
```

### 2.2 Custom Span Creation

```typescript
// src/tracing/spans.ts

import { trace, SpanKind, SpanStatusCode, context } from '@opentelemetry/api';

const tracer = trace.getTracer('mindweave-api', '1.0.0');

// Wrap async function with span
export function withSpan<T>(
  spanName: string,
  attributes: Record<string, string | number | boolean>,
  fn: () => Promise<T>
): Promise<T> {
  return tracer.startActiveSpan(
    spanName,
    { attributes },
    async (span) => {
      try {
        const result = await fn();
        span.setStatus({ code: SpanStatusCode.OK });
        return result;
      } catch (error) {
        span.setStatus({
          code: SpanStatusCode.ERROR,
          message: error instanceof Error ? error.message : 'Unknown error',
        });
        span.recordException(error as Error);
        throw error;
      } finally {
        span.end();
      }
    }
  );
}

// Claude API call span
export async function traceClaudeApiCall<T>(
  params: {
    orgId: string;
    projectId: string;
    model: string;
    endpoint: string;
  },
  fn: () => Promise<T>
): Promise<T> {
  return tracer.startActiveSpan(
    'claude.api.call',
    {
      kind: SpanKind.CLIENT,
      attributes: {
        'claude.org_id': params.orgId,
        'claude.project_id': params.projectId,
        'claude.model': params.model,
        'http.url': `https://api.anthropic.com${params.endpoint}`,
        'http.method': 'POST',
      },
    },
    async (span) => {
      const startTime = Date.now();

      try {
        const result = await fn();

        span.setAttributes({
          'http.status_code': 200,
          'claude.duration_ms': Date.now() - startTime,
        });
        span.setStatus({ code: SpanStatusCode.OK });

        return result;
      } catch (error) {
        span.setAttributes({
          'http.status_code': (error as any).statusCode || 500,
          'claude.duration_ms': Date.now() - startTime,
        });
        span.setStatus({
          code: SpanStatusCode.ERROR,
          message: error instanceof Error ? error.message : 'API call failed',
        });
        span.recordException(error as Error);
        throw error;
      } finally {
        span.end();
      }
    }
  );
}

// Database query span
export async function traceDbQuery<T>(
  queryType: string,
  table: string,
  fn: () => Promise<T>
): Promise<T> {
  return tracer.startActiveSpan(
    `db.${queryType}`,
    {
      kind: SpanKind.CLIENT,
      attributes: {
        'db.system': 'postgresql',
        'db.operation': queryType,
        'db.sql.table': table,
      },
    },
    async (span) => {
      try {
        const result = await fn();
        span.setStatus({ code: SpanStatusCode.OK });
        return result;
      } catch (error) {
        span.setStatus({ code: SpanStatusCode.ERROR });
        span.recordException(error as Error);
        throw error;
      } finally {
        span.end();
      }
    }
  );
}

// MCP tool invocation span
export async function traceMcpToolInvocation<T>(
  params: {
    serverId: string;
    toolName: string;
    transport: string;
  },
  fn: () => Promise<T>
): Promise<T> {
  return tracer.startActiveSpan(
    `mcp.tool.${params.toolName}`,
    {
      kind: SpanKind.CLIENT,
      attributes: {
        'mcp.server_id': params.serverId,
        'mcp.tool_name': params.toolName,
        'mcp.transport': params.transport,
      },
    },
    async (span) => {
      try {
        const result = await fn();
        span.setStatus({ code: SpanStatusCode.OK });
        return result;
      } catch (error) {
        span.setStatus({ code: SpanStatusCode.ERROR });
        span.recordException(error as Error);
        throw error;
      } finally {
        span.end();
      }
    }
  );
}
```

### 2.3 Jaeger Deployment

```yaml
# k8s/monitoring/jaeger.yaml

apiVersion: jaegertracing.io/v1
kind: Jaeger
metadata:
  name: mindweave-jaeger
  namespace: mindweave-monitoring
spec:
  strategy: production
  storage:
    type: elasticsearch
    options:
      es:
        server-urls: https://elasticsearch:9200
        index-prefix: jaeger
        tls:
          ca: /es/certificates/ca.crt
    secretName: jaeger-es-secret
  collector:
    replicas: 3
    maxReplicas: 10
    resources:
      requests:
        cpu: 500m
        memory: 512Mi
      limits:
        cpu: 1000m
        memory: 1Gi
    options:
      collector:
        zipkin:
          host-port: 9411
  query:
    replicas: 2
    resources:
      requests:
        cpu: 250m
        memory: 256Mi
      limits:
        cpu: 500m
        memory: 512Mi
    options:
      query:
        base-path: /jaeger
  ingress:
    enabled: true
    annotations:
      kubernetes.io/ingress.class: nginx
      cert-manager.io/cluster-issuer: letsencrypt-prod
    hosts:
      - jaeger.mindweave.io
    tls:
      - secretName: jaeger-tls
        hosts:
          - jaeger.mindweave.io
---
apiVersion: v1
kind: Secret
metadata:
  name: jaeger-es-secret
  namespace: mindweave-monitoring
type: Opaque
stringData:
  ES_PASSWORD: "${ELASTICSEARCH_PASSWORD}"
  ES_USERNAME: "elastic"
```

---

## 3. Log Aggregation

### 3.1 Fluent Bit Configuration

```yaml
# k8s/monitoring/fluent-bit-config.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  namespace: mindweave-monitoring
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush         5
        Log_Level     info
        Daemon        off
        Parsers_File  parsers.conf
        HTTP_Server   On
        HTTP_Listen   0.0.0.0
        HTTP_Port     2020

    [INPUT]
        Name              tail
        Tag               kube.*
        Path              /var/log/containers/*.log
        Parser            docker
        DB                /var/log/flb_kube.db
        Mem_Buf_Limit     50MB
        Skip_Long_Lines   On
        Refresh_Interval  10

    [FILTER]
        Name                kubernetes
        Match               kube.*
        Kube_URL            https://kubernetes.default.svc:443
        Kube_CA_File        /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        Kube_Token_File     /var/run/secrets/kubernetes.io/serviceaccount/token
        Kube_Tag_Prefix     kube.var.log.containers.
        Merge_Log           On
        Keep_Log            Off
        K8S-Logging.Parser  On
        K8S-Logging.Exclude On
        Labels              On
        Annotations         Off

    [FILTER]
        Name          nest
        Match         kube.*
        Operation     lift
        Nested_under  kubernetes
        Add_prefix    kubernetes_

    [FILTER]
        Name          modify
        Match         kube.*
        Rename        kubernetes_pod_name pod
        Rename        kubernetes_namespace_name namespace
        Rename        kubernetes_container_name container

    [FILTER]
        Name          record_modifier
        Match         kube.*
        Record        cluster mindweave-production
        Record        region us-east-1

    # Parse JSON logs from MindWeave services
    [FILTER]
        Name          parser
        Match         kube.var.log.containers.mindweave*
        Key_Name      log
        Parser        json
        Reserve_Data  On

    # Enrich with trace context
    [FILTER]
        Name          modify
        Match         kube.*
        Condition     Key_value_equals  namespace mindweave-services
        Add           service.name ${kubernetes_labels_app}

    [OUTPUT]
        Name              datadog
        Match             *
        Host              http-intake.logs.datadoghq.com
        TLS               on
        compress          gzip
        apikey            ${DD_API_KEY}
        dd_service        ${kubernetes_labels_app}
        dd_source         kubernetes
        dd_tags           env:production,cluster:mindweave-production

    [OUTPUT]
        Name              es
        Match             kube.*
        Host              elasticsearch.mindweave-monitoring
        Port              9200
        HTTP_User         elastic
        HTTP_Passwd       ${ELASTICSEARCH_PASSWORD}
        Logstash_Format   On
        Logstash_Prefix   mindweave-logs
        Retry_Limit       5
        tls               On
        tls.verify        On
        tls.ca_file       /es-certs/ca.crt

  parsers.conf: |
    [PARSER]
        Name        docker
        Format      json
        Time_Key    time
        Time_Format %Y-%m-%dT%H:%M:%S.%L
        Time_Keep   On

    [PARSER]
        Name        json
        Format      json
        Time_Key    timestamp
        Time_Format %Y-%m-%dT%H:%M:%S.%LZ
        Time_Keep   On

    [PARSER]
        Name        syslog
        Format      regex
        Regex       ^\<(?<pri>[0-9]+)\>(?<time>[^ ]* {1,2}[^ ]* [^ ]*) (?<host>[^ ]*) (?<ident>[a-zA-Z0-9_\/\.\-]*)(?:\[(?<pid>[0-9]+)\])?(?:[^\:]*\:)? *(?<message>.*)$
        Time_Key    time
        Time_Format %b %d %H:%M:%S
```

### 3.2 Structured Logging Format

```typescript
// src/logging/logger.ts

import pino from 'pino';
import { context, trace } from '@opentelemetry/api';

// Log level configuration
const level = process.env.LOG_LEVEL || 'info';

// Pino logger configuration
export const logger = pino({
  level,
  formatters: {
    level(label) {
      return { level: label };
    },
  },
  timestamp: pino.stdTimeFunctions.isoTime,
  base: {
    service: process.env.SERVICE_NAME || 'api-gateway',
    version: process.env.SERVICE_VERSION || '1.0.0',
    environment: process.env.NODE_ENV || 'development',
  },
  redact: {
    paths: [
      'password',
      'token',
      'authorization',
      'cookie',
      'api_key',
      'apiKey',
      'secret',
      'credit_card',
      'ssn',
      'email',
      '*.password',
      '*.token',
      '*.api_key',
    ],
    censor: '[REDACTED]',
  },
  serializers: {
    req: (req) => ({
      method: req.method,
      url: req.url,
      path: req.path,
      query: req.query,
      headers: {
        'user-agent': req.headers['user-agent'],
        'x-request-id': req.headers['x-request-id'],
        'x-forwarded-for': req.headers['x-forwarded-for'],
      },
    }),
    res: (res) => ({
      statusCode: res.statusCode,
    }),
    err: pino.stdSerializers.err,
  },
  mixin() {
    // Add trace context to every log
    const span = trace.getSpan(context.active());
    if (span) {
      const spanContext = span.spanContext();
      return {
        trace_id: spanContext.traceId,
        span_id: spanContext.spanId,
        trace_flags: spanContext.traceFlags,
      };
    }
    return {};
  },
});

// Create child logger with context
export function createLogger(context: Record<string, string | number | boolean>) {
  return logger.child(context);
}

// Request logger middleware
export function requestLogger(req: Request, res: Response, next: NextFunction) {
  const startTime = Date.now();
  const requestId = req.headers['x-request-id'] || crypto.randomUUID();

  // Add request ID to response headers
  res.setHeader('x-request-id', requestId);

  // Create request-scoped logger
  const reqLogger = logger.child({
    request_id: requestId,
    method: req.method,
    path: req.path,
  });

  // Log request
  reqLogger.info({ req }, 'incoming request');

  // Log response
  res.on('finish', () => {
    const duration = Date.now() - startTime;
    const logLevel = res.statusCode >= 500 ? 'error' : res.statusCode >= 400 ? 'warn' : 'info';

    reqLogger[logLevel](
      {
        res,
        duration_ms: duration,
        status_code: res.statusCode,
      },
      'request completed'
    );
  });

  // Attach logger to request
  (req as any).log = reqLogger;

  next();
}
```

### 3.3 Log Patterns and Standards

```typescript
// src/logging/log-patterns.ts

import { logger, createLogger } from './logger';

// Authentication events
export const authLogger = createLogger({ category: 'auth' });

export function logLoginAttempt(params: {
  email: string;
  success: boolean;
  reason?: string;
  ip: string;
  userAgent: string;
}) {
  const level = params.success ? 'info' : 'warn';
  authLogger[level]({
    event: params.success ? 'login.success' : 'login.failed',
    email_hash: hashEmail(params.email), // Don't log actual email
    reason: params.reason,
    ip: params.ip,
    user_agent: params.userAgent,
  });
}

export function logMfaChallenge(params: {
  userId: string;
  method: string;
  success: boolean;
}) {
  authLogger.info({
    event: params.success ? 'mfa.verified' : 'mfa.failed',
    user_id: params.userId,
    method: params.method,
  });
}

// API usage events
export const usageLogger = createLogger({ category: 'usage' });

export function logApiCall(params: {
  orgId: string;
  projectId: string;
  userId: string;
  model: string;
  inputTokens: number;
  outputTokens: number;
  costCents: number;
  latencyMs: number;
  status: string;
}) {
  usageLogger.info({
    event: 'api.call',
    org_id: params.orgId,
    project_id: params.projectId,
    user_id: params.userId,
    model: params.model,
    tokens: {
      input: params.inputTokens,
      output: params.outputTokens,
      total: params.inputTokens + params.outputTokens,
    },
    cost_cents: params.costCents,
    latency_ms: params.latencyMs,
    status: params.status,
  });
}

// Governance events
export const governanceLogger = createLogger({ category: 'governance' });

export function logPolicyViolation(params: {
  orgId: string;
  projectId: string;
  userId: string;
  policyId: string;
  policyType: string;
  violation: string;
  severity: string;
  context: Record<string, any>;
}) {
  governanceLogger.warn({
    event: 'policy.violation',
    org_id: params.orgId,
    project_id: params.projectId,
    user_id: params.userId,
    policy_id: params.policyId,
    policy_type: params.policyType,
    violation: params.violation,
    severity: params.severity,
    context: params.context,
  });
}

// MCP events
export const mcpLogger = createLogger({ category: 'mcp' });

export function logMcpServerStatus(params: {
  orgId: string;
  serverId: string;
  serverName: string;
  status: 'connected' | 'disconnected' | 'error';
  error?: string;
}) {
  const level = params.status === 'error' ? 'error' : 'info';
  mcpLogger[level]({
    event: `mcp.server.${params.status}`,
    org_id: params.orgId,
    server_id: params.serverId,
    server_name: params.serverName,
    error: params.error,
  });
}

// Audit events
export const auditLogger = createLogger({ category: 'audit' });

export function logAuditEvent(params: {
  actor: {
    type: 'user' | 'system' | 'api_key';
    id: string;
    ip?: string;
  };
  action: string;
  resource: {
    type: string;
    id: string;
  };
  orgId: string;
  result: 'success' | 'failure';
  details?: Record<string, any>;
}) {
  auditLogger.info({
    event: 'audit.action',
    actor: params.actor,
    action: params.action,
    resource: params.resource,
    org_id: params.orgId,
    result: params.result,
    details: params.details,
    timestamp: new Date().toISOString(),
  });
}

// Helper to hash email for logging
function hashEmail(email: string): string {
  const crypto = require('crypto');
  return crypto.createHash('sha256').update(email.toLowerCase()).digest('hex').substring(0, 16);
}
```

---

## 4. Alerting Configuration

### 4.1 Prometheus Alert Rules

```yaml
# prometheus/rules/mindweave-alerts.yaml

groups:
  - name: mindweave.availability
    interval: 30s
    rules:
      # High error rate
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status_code=~"5..",namespace="mindweave-services"}[5m]))
          /
          sum(rate(http_requests_total{namespace="mindweave-services"}[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }} (threshold: 5%)"
          runbook_url: "https://runbooks.mindweave.io/high-error-rate"
          dashboard_url: "https://grafana.mindweave.io/d/services/services?orgId=1"

      # Service down
      - alert: ServiceDown
        expr: |
          up{namespace="mindweave-services"} == 0
        for: 1m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "Service {{ $labels.job }} is down"
          description: "Service has been down for more than 1 minute"
          runbook_url: "https://runbooks.mindweave.io/service-down"

      # High latency
      - alert: HighLatency
        expr: |
          histogram_quantile(0.99,
            sum(rate(http_request_duration_seconds_bucket{namespace="mindweave-services"}[5m]))
            by (le, service)
          ) > 2
        for: 5m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High latency for {{ $labels.service }}"
          description: "P99 latency is {{ $value | humanizeDuration }}"
          runbook_url: "https://runbooks.mindweave.io/high-latency"

  - name: mindweave.resources
    interval: 30s
    rules:
      # High CPU usage
      - alert: HighCPUUsage
        expr: |
          sum(rate(container_cpu_usage_seconds_total{namespace="mindweave-services"}[5m]))
          by (pod)
          /
          sum(kube_pod_container_resource_limits{namespace="mindweave-services",resource="cpu"})
          by (pod) > 0.85
        for: 10m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High CPU usage for {{ $labels.pod }}"
          description: "CPU usage is {{ $value | humanizePercentage }}"

      # High memory usage
      - alert: HighMemoryUsage
        expr: |
          sum(container_memory_working_set_bytes{namespace="mindweave-services"})
          by (pod)
          /
          sum(kube_pod_container_resource_limits{namespace="mindweave-services",resource="memory"})
          by (pod) > 0.90
        for: 5m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High memory usage for {{ $labels.pod }}"
          description: "Memory usage is {{ $value | humanizePercentage }}"

      # Pod restarts
      - alert: PodRestartLoop
        expr: |
          increase(kube_pod_container_status_restarts_total{namespace="mindweave-services"}[1h]) > 5
        for: 5m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "Pod {{ $labels.pod }} is in restart loop"
          description: "Pod has restarted {{ $value }} times in the last hour"
          runbook_url: "https://runbooks.mindweave.io/pod-restart-loop"

  - name: mindweave.business
    interval: 1m
    rules:
      # Budget threshold approaching
      - alert: BudgetThresholdApproaching
        expr: |
          mindweave_budget_usage_percent > 80
        for: 5m
        labels:
          severity: warning
          team: customer-success
        annotations:
          summary: "Budget threshold approaching for org {{ $labels.org_id }}"
          description: "Budget usage is at {{ $value | humanizePercentage }}"

      # Unusual spike in API calls
      - alert: UnusualApiCallSpike
        expr: |
          rate(mindweave_api_calls_total[5m])
          /
          avg_over_time(rate(mindweave_api_calls_total[5m])[1h:5m]) > 3
        for: 10m
        labels:
          severity: info
          team: platform
        annotations:
          summary: "Unusual spike in API calls"
          description: "API call rate is {{ $value }}x the normal rate"

      # Policy violations spike
      - alert: PolicyViolationsSpike
        expr: |
          increase(mindweave_policy_violations_total[1h]) > 100
        for: 5m
        labels:
          severity: warning
          team: security
        annotations:
          summary: "High number of policy violations"
          description: "{{ $value }} policy violations in the last hour"

  - name: mindweave.infrastructure
    interval: 30s
    rules:
      # Database connection pool exhaustion
      - alert: DatabaseConnectionPoolExhausted
        expr: |
          db_connection_pool_size{state="available"} < 5
        for: 5m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "Database connection pool nearly exhausted"
          description: "Only {{ $value }} connections available"
          runbook_url: "https://runbooks.mindweave.io/db-connection-pool"

      # Kafka consumer lag
      - alert: KafkaConsumerLag
        expr: |
          kafka_consumer_lag > 10000
        for: 10m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High Kafka consumer lag"
          description: "Consumer lag is {{ $value }} messages for {{ $labels.topic }}"

      # Redis memory usage
      - alert: RedisHighMemory
        expr: |
          redis_memory_used_bytes / redis_memory_max_bytes > 0.90
        for: 5m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "Redis memory usage high"
          description: "Redis memory usage is {{ $value | humanizePercentage }}"

      # Certificate expiration
      - alert: CertificateExpiringSoon
        expr: |
          (probe_ssl_earliest_cert_expiry - time()) / 86400 < 30
        for: 1h
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "SSL certificate expiring soon"
          description: "Certificate for {{ $labels.instance }} expires in {{ $value }} days"
```

### 4.2 Alertmanager Configuration

```yaml
# alertmanager/alertmanager.yaml

global:
  resolve_timeout: 5m
  smtp_smarthost: 'smtp.sendgrid.net:587'
  smtp_from: 'alerts@mindweave.io'
  smtp_auth_username: 'apikey'
  smtp_auth_password: '${SENDGRID_API_KEY}'
  slack_api_url: '${SLACK_WEBHOOK_URL}'
  pagerduty_url: 'https://events.pagerduty.com/v2/enqueue'

templates:
  - '/etc/alertmanager/templates/*.tmpl'

route:
  group_by: ['alertname', 'namespace', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'default-receiver'
  routes:
    # Critical alerts go to PagerDuty
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
      continue: true

    # Platform team alerts
    - match:
        team: platform
      receiver: 'slack-platform'
      routes:
        - match:
            severity: critical
          receiver: 'pagerduty-platform'

    # Security team alerts
    - match:
        team: security
      receiver: 'slack-security'
      routes:
        - match:
            severity: critical
          receiver: 'pagerduty-security'

    # Customer success alerts
    - match:
        team: customer-success
      receiver: 'slack-customer-success'

receivers:
  - name: 'default-receiver'
    slack_configs:
      - channel: '#alerts-general'
        send_resolved: true
        title: '{{ template "slack.default.title" . }}'
        text: '{{ template "slack.default.text" . }}'
        actions:
          - type: button
            text: 'Runbook'
            url: '{{ (index .Alerts 0).Annotations.runbook_url }}'
          - type: button
            text: 'Dashboard'
            url: '{{ (index .Alerts 0).Annotations.dashboard_url }}'

  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_SERVICE_KEY_CRITICAL}'
        severity: critical
        description: '{{ template "pagerduty.default.description" . }}'
        details:
          firing: '{{ template "pagerduty.default.instances" .Alerts.Firing }}'
          resolved: '{{ template "pagerduty.default.instances" .Alerts.Resolved }}'
          num_firing: '{{ .Alerts.Firing | len }}'
          num_resolved: '{{ .Alerts.Resolved | len }}'

  - name: 'slack-platform'
    slack_configs:
      - channel: '#platform-alerts'
        send_resolved: true
        color: '{{ template "slack.color" . }}'
        title: '{{ template "slack.default.title" . }}'
        text: '{{ template "slack.default.text" . }}'

  - name: 'pagerduty-platform'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_SERVICE_KEY_PLATFORM}'
        severity: '{{ if eq .CommonLabels.severity "critical" }}critical{{ else }}warning{{ end }}'

  - name: 'slack-security'
    slack_configs:
      - channel: '#security-alerts'
        send_resolved: true
        color: '{{ template "slack.color" . }}'
        title: '{{ template "slack.default.title" . }}'
        text: '{{ template "slack.default.text" . }}'

  - name: 'pagerduty-security'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_SERVICE_KEY_SECURITY}'
        severity: critical

  - name: 'slack-customer-success'
    slack_configs:
      - channel: '#customer-success-alerts'
        send_resolved: true
        title: '{{ template "slack.default.title" . }}'
        text: '{{ template "slack.default.text" . }}'

inhibit_rules:
  # Inhibit warnings if critical alert is firing for same service
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'namespace', 'service']

  # Inhibit downstream alerts if upstream is down
  - source_match:
      alertname: 'ServiceDown'
    target_match_re:
      alertname: 'High.*'
    equal: ['namespace']
```

---

## 5. Dashboards

### 5.1 Service Overview Dashboard

```json
{
  "title": "MindWeave Service Overview",
  "uid": "mindweave-overview",
  "tags": ["mindweave", "services", "overview"],
  "timezone": "browser",
  "refresh": "30s",
  "panels": [
    {
      "title": "Request Rate",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 0, "y": 0 },
      "targets": [
        {
          "expr": "sum(rate(http_requests_total{namespace=\"mindweave-services\"}[5m]))",
          "legendFormat": "Requests/sec"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "reqps",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              { "color": "green", "value": null },
              { "color": "yellow", "value": 1000 },
              { "color": "red", "value": 5000 }
            ]
          }
        }
      }
    },
    {
      "title": "Error Rate",
      "type": "gauge",
      "gridPos": { "h": 4, "w": 4, "x": 4, "y": 0 },
      "targets": [
        {
          "expr": "sum(rate(http_requests_total{namespace=\"mindweave-services\",status_code=~\"5..\"}[5m])) / sum(rate(http_requests_total{namespace=\"mindweave-services\"}[5m])) * 100"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "min": 0,
          "max": 100,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              { "color": "green", "value": null },
              { "color": "yellow", "value": 1 },
              { "color": "red", "value": 5 }
            ]
          }
        }
      }
    },
    {
      "title": "P99 Latency",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 8, "y": 0 },
      "targets": [
        {
          "expr": "histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket{namespace=\"mindweave-services\"}[5m])) by (le))"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "s",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              { "color": "green", "value": null },
              { "color": "yellow", "value": 0.5 },
              { "color": "red", "value": 1 }
            ]
          }
        }
      }
    },
    {
      "title": "Active Pods",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 12, "y": 0 },
      "targets": [
        {
          "expr": "sum(kube_pod_status_phase{namespace=\"mindweave-services\",phase=\"Running\"})"
        }
      ]
    },
    {
      "title": "Request Rate by Service",
      "type": "timeseries",
      "gridPos": { "h": 8, "w": 12, "x": 0, "y": 4 },
      "targets": [
        {
          "expr": "sum(rate(http_requests_total{namespace=\"mindweave-services\"}[5m])) by (service)",
          "legendFormat": "{{ service }}"
        }
      ]
    },
    {
      "title": "Error Rate by Service",
      "type": "timeseries",
      "gridPos": { "h": 8, "w": 12, "x": 12, "y": 4 },
      "targets": [
        {
          "expr": "sum(rate(http_requests_total{namespace=\"mindweave-services\",status_code=~\"5..\"}[5m])) by (service)",
          "legendFormat": "{{ service }}"
        }
      ]
    },
    {
      "title": "Latency Percentiles",
      "type": "timeseries",
      "gridPos": { "h": 8, "w": 12, "x": 0, "y": 12 },
      "targets": [
        {
          "expr": "histogram_quantile(0.50, sum(rate(http_request_duration_seconds_bucket{namespace=\"mindweave-services\"}[5m])) by (le))",
          "legendFormat": "p50"
        },
        {
          "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{namespace=\"mindweave-services\"}[5m])) by (le))",
          "legendFormat": "p95"
        },
        {
          "expr": "histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket{namespace=\"mindweave-services\"}[5m])) by (le))",
          "legendFormat": "p99"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "s"
        }
      }
    },
    {
      "title": "CPU Usage by Service",
      "type": "timeseries",
      "gridPos": { "h": 8, "w": 12, "x": 12, "y": 12 },
      "targets": [
        {
          "expr": "sum(rate(container_cpu_usage_seconds_total{namespace=\"mindweave-services\"}[5m])) by (pod)",
          "legendFormat": "{{ pod }}"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percentunit"
        }
      }
    }
  ]
}
```

### 5.2 Business Metrics Dashboard

```json
{
  "title": "MindWeave Business Metrics",
  "uid": "mindweave-business",
  "tags": ["mindweave", "business", "usage"],
  "panels": [
    {
      "title": "Total API Calls (24h)",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 0, "y": 0 },
      "targets": [
        {
          "expr": "sum(increase(mindweave_api_calls_total[24h]))"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "short"
        }
      }
    },
    {
      "title": "Total Tokens (24h)",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 4, "y": 0 },
      "targets": [
        {
          "expr": "sum(increase(mindweave_tokens_processed_total[24h]))"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "short"
        }
      }
    },
    {
      "title": "Total Cost (24h)",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 8, "y": 0 },
      "targets": [
        {
          "expr": "sum(increase(mindweave_cost_cents_total[24h])) / 100"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "currencyUSD"
        }
      }
    },
    {
      "title": "Active Organizations",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 12, "y": 0 },
      "targets": [
        {
          "expr": "count(count by (org_id) (mindweave_api_calls_total))"
        }
      ]
    },
    {
      "title": "API Calls by Model",
      "type": "piechart",
      "gridPos": { "h": 8, "w": 8, "x": 0, "y": 4 },
      "targets": [
        {
          "expr": "sum(increase(mindweave_api_calls_total[24h])) by (model)",
          "legendFormat": "{{ model }}"
        }
      ]
    },
    {
      "title": "Cost by Organization (Top 10)",
      "type": "bargauge",
      "gridPos": { "h": 8, "w": 8, "x": 8, "y": 4 },
      "targets": [
        {
          "expr": "topk(10, sum(increase(mindweave_cost_cents_total[24h])) by (org_id) / 100)",
          "legendFormat": "{{ org_id }}"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "currencyUSD"
        }
      }
    },
    {
      "title": "API Calls Over Time",
      "type": "timeseries",
      "gridPos": { "h": 8, "w": 16, "x": 0, "y": 12 },
      "targets": [
        {
          "expr": "sum(rate(mindweave_api_calls_total[5m])) by (model)",
          "legendFormat": "{{ model }}"
        }
      ]
    },
    {
      "title": "Active MCP Servers",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 16, "y": 4 },
      "targets": [
        {
          "expr": "sum(mindweave_mcp_servers_active)"
        }
      ]
    },
    {
      "title": "MCP Tool Invocations (1h)",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 16, "y": 8 },
      "targets": [
        {
          "expr": "sum(increase(mindweave_mcp_tool_invocations_total[1h]))"
        }
      ]
    },
    {
      "title": "Policy Violations (24h)",
      "type": "stat",
      "gridPos": { "h": 4, "w": 4, "x": 20, "y": 4 },
      "targets": [
        {
          "expr": "sum(increase(mindweave_policy_violations_total[24h]))"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "thresholds": {
            "steps": [
              { "color": "green", "value": null },
              { "color": "yellow", "value": 10 },
              { "color": "red", "value": 100 }
            ]
          }
        }
      }
    }
  ]
}
```

---

## 6. SLO Configuration

### 6.1 SLO Definitions

```yaml
# slo/mindweave-slos.yaml

apiVersion: sloth.slok.dev/v1
kind: PrometheusServiceLevel
metadata:
  name: mindweave-api-gateway
  namespace: mindweave-monitoring
spec:
  service: "api-gateway"
  labels:
    team: platform
    tier: critical
  slos:
    # Availability SLO
    - name: "availability"
      objective: 99.9
      description: "API Gateway availability"
      sli:
        events:
          errorQuery: sum(rate(http_requests_total{service="api-gateway",status_code=~"5.."}[{{.window}}]))
          totalQuery: sum(rate(http_requests_total{service="api-gateway"}[{{.window}}]))
      alerting:
        name: MindWeaveAPIGatewayAvailability
        labels:
          team: platform
        annotations:
          summary: "API Gateway availability SLO breach"
        pageAlert:
          labels:
            severity: critical
        ticketAlert:
          labels:
            severity: warning

    # Latency SLO
    - name: "latency"
      objective: 99.0
      description: "API Gateway latency (p99 < 500ms)"
      sli:
        events:
          errorQuery: |
            sum(rate(http_request_duration_seconds_bucket{service="api-gateway",le="0.5"}[{{.window}}]))
          totalQuery: |
            sum(rate(http_request_duration_seconds_count{service="api-gateway"}[{{.window}}]))
      alerting:
        name: MindWeaveAPIGatewayLatency
        labels:
          team: platform
        annotations:
          summary: "API Gateway latency SLO breach"
---
apiVersion: sloth.slok.dev/v1
kind: PrometheusServiceLevel
metadata:
  name: mindweave-usage-tracker
  namespace: mindweave-monitoring
spec:
  service: "usage-tracker"
  labels:
    team: platform
    tier: critical
  slos:
    # Data ingestion SLO
    - name: "ingestion-availability"
      objective: 99.99
      description: "Usage data ingestion availability"
      sli:
        events:
          errorQuery: sum(rate(usage_events_dropped_total[{{.window}}]))
          totalQuery: sum(rate(usage_events_received_total[{{.window}}]))
      alerting:
        name: MindWeaveUsageTrackerIngestion
        labels:
          team: platform

    # Processing latency SLO
    - name: "processing-latency"
      objective: 99.0
      description: "Usage events processed within 100ms"
      sli:
        events:
          errorQuery: |
            sum(rate(usage_event_processing_duration_seconds_bucket{le="0.1"}[{{.window}}]))
          totalQuery: |
            sum(rate(usage_event_processing_duration_seconds_count[{{.window}}]))
```

### 6.2 Error Budget Policy

```yaml
# slo/error-budget-policy.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: error-budget-policy
  namespace: mindweave-monitoring
data:
  policy.yaml: |
    # Error Budget Policy for MindWeave

    # Budget Calculation
    # 99.9% availability = 43.2 minutes downtime per month
    # 99.99% availability = 4.32 minutes downtime per month

    services:
      api-gateway:
        slo_target: 99.9%
        monthly_budget_minutes: 43.2
        actions:
          budget_remaining_75_percent:
            - normal_development_velocity
            - standard_release_process
          budget_remaining_50_percent:
            - increased_monitoring
            - prioritize_reliability_work
            - reduce_risky_deployments
          budget_remaining_25_percent:
            - freeze_non_critical_changes
            - require_additional_review
            - increase_testing_requirements
          budget_exhausted:
            - freeze_all_non_critical_deployments
            - emergency_reliability_focus
            - incident_response_mode

      usage-tracker:
        slo_target: 99.99%
        monthly_budget_minutes: 4.32
        actions:
          budget_remaining_50_percent:
            - critical_service_handling
            - immediate_escalation
          budget_exhausted:
            - p0_incident_response
            - all_hands_reliability

    # Escalation Matrix
    escalation:
      budget_75_percent:
        notify: ["#platform-alerts"]
        oncall: false
      budget_50_percent:
        notify: ["#platform-alerts", "#engineering-leads"]
        oncall: false
      budget_25_percent:
        notify: ["#platform-alerts", "#engineering-leads", "#exec-team"]
        oncall: true
      budget_exhausted:
        notify: ["all"]
        oncall: true
        page: true
```

---

## 7. DataDog Integration

### 7.1 DataDog Agent Configuration

```yaml
# k8s/monitoring/datadog-agent.yaml

apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
  namespace: mindweave-monitoring
spec:
  global:
    credentials:
      apiSecret:
        secretName: datadog-secret
        keyName: api-key
      appSecret:
        secretName: datadog-secret
        keyName: app-key
    site: datadoghq.com
    tags:
      - "env:production"
      - "team:platform"
      - "service:mindweave"
    clusterName: mindweave-production

  features:
    apm:
      enabled: true
      hostPortConfig:
        enabled: true
        hostPort: 8126
      unixDomainSocketConfig:
        enabled: true
        path: /var/run/datadog/apm.socket

    logCollection:
      enabled: true
      containerCollectAll: true
      containerCollectUsingFiles: true

    liveProcessCollection:
      enabled: true

    liveContainerCollection:
      enabled: true

    npm:
      enabled: true

    usm:
      enabled: true

    cspm:
      enabled: true

    cws:
      enabled: true

    admissionController:
      enabled: true
      mutateUnlabelled: true

  override:
    nodeAgent:
      tolerations:
        - operator: Exists
      env:
        - name: DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL
          value: "true"
        - name: DD_APM_NON_LOCAL_TRAFFIC
          value: "true"
        - name: DD_DOGSTATSD_NON_LOCAL_TRAFFIC
          value: "true"
      volumes:
        - name: logdatadog
          hostPath:
            path: /var/log/datadog
        - name: tmpdir
          emptyDir: {}
      volumeMounts:
        - name: logdatadog
          mountPath: /var/log/datadog
        - name: tmpdir
          mountPath: /tmp

    clusterAgent:
      replicas: 2
      containers:
        cluster-agent:
          resources:
            requests:
              cpu: 200m
              memory: 256Mi
            limits:
              cpu: 500m
              memory: 512Mi
```

### 7.2 DataDog APM Configuration

```typescript
// src/tracing/datadog.ts

import tracer from 'dd-trace';

// Initialize DataDog tracer
tracer.init({
  service: process.env.DD_SERVICE || 'api-gateway',
  env: process.env.DD_ENV || 'production',
  version: process.env.DD_VERSION || '1.0.0',
  logInjection: true,
  runtimeMetrics: true,
  profiling: true,
  appsec: true,
  // Sampling configuration
  sampleRate: 1, // 100% in production for critical services
  // Integrations
  plugins: true,
  // Tags
  tags: {
    'team': 'platform',
    'tier': 'critical',
  },
});

// Custom span tags
tracer.use('http', {
  hooks: {
    request: (span, req, res) => {
      if (req) {
        span?.setTag('http.client_ip', req.headers['x-forwarded-for'] || req.socket.remoteAddress);
        span?.setTag('http.request_id', req.headers['x-request-id']);
      }
    },
  },
});

// PostgreSQL integration
tracer.use('pg', {
  service: 'mindweave-postgres',
  measured: true,
});

// Redis integration
tracer.use('ioredis', {
  service: 'mindweave-redis',
  measured: true,
});

// Kafka integration
tracer.use('kafkajs', {
  service: 'mindweave-kafka',
  measured: true,
});

export default tracer;
```

---

## 8. Runbook Automation

### 8.1 Automated Runbook Trigger

```yaml
# k8s/monitoring/runbook-operator.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: runbook-configs
  namespace: mindweave-monitoring
data:
  high-error-rate.yaml: |
    name: high-error-rate
    description: Automated response to high error rate
    trigger:
      alert: HighErrorRate
      severity: critical
    steps:
      - name: gather-context
        action: kubectl
        command: |
          kubectl get pods -n mindweave-services -l app={{ .Labels.service }} -o wide
          kubectl top pods -n mindweave-services -l app={{ .Labels.service }}
          kubectl logs -n mindweave-services -l app={{ .Labels.service }} --tail=100 --since=5m

      - name: check-dependencies
        action: http
        requests:
          - url: "http://{{ .Labels.service }}.mindweave-services/health/ready"
            method: GET
            timeout: 5s

      - name: scale-up
        action: kubectl
        condition: "{{ .Metrics.error_rate > 0.1 }}"
        command: |
          kubectl scale deployment {{ .Labels.service }} -n mindweave-services --replicas={{ add .Current.replicas 2 }}

      - name: notify
        action: slack
        channel: "#platform-incidents"
        message: |
          :rotating_light: High Error Rate Detected
          Service: {{ .Labels.service }}
          Error Rate: {{ .Metrics.error_rate | percent }}
          Actions Taken:
          - Gathered diagnostic information
          - Scaled up replicas

          Dashboard: {{ .Annotations.dashboard_url }}
          Runbook: {{ .Annotations.runbook_url }}

  pod-restart-loop.yaml: |
    name: pod-restart-loop
    description: Automated response to pod restart loop
    trigger:
      alert: PodRestartLoop
      severity: critical
    steps:
      - name: describe-pod
        action: kubectl
        command: |
          kubectl describe pod {{ .Labels.pod }} -n {{ .Labels.namespace }}

      - name: get-previous-logs
        action: kubectl
        command: |
          kubectl logs {{ .Labels.pod }} -n {{ .Labels.namespace }} --previous --tail=200

      - name: check-resources
        action: kubectl
        command: |
          kubectl top pod {{ .Labels.pod }} -n {{ .Labels.namespace }}

      - name: check-oom
        action: kubectl
        command: |
          kubectl get events -n {{ .Labels.namespace }} --field-selector involvedObject.name={{ .Labels.pod }} --sort-by='.lastTimestamp'

      - name: create-incident
        action: pagerduty
        condition: "{{ .Metrics.restart_count > 10 }}"
        severity: high
        title: "Pod {{ .Labels.pod }} in restart loop"
        details: |
          Pod has restarted {{ .Metrics.restart_count }} times
          Last restart reason: {{ .Events.last_restart_reason }}
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | Overall system design |
| [DEPLOYMENT-STRATEGY.md](./DEPLOYMENT-STRATEGY.md) | Deployment procedures |
| [INCIDENT-RESPONSE.md](./INCIDENT-RESPONSE.md) | Incident handling |
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security controls |
| [DATA-PIPELINE.md](./DATA-PIPELINE.md) | Data processing architecture |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | Platform Engineering | Initial monitoring strategy |

# Feature Specification: Audit Logs

> Complete specification for the Audit Logging feature

---

## Overview

### Feature Summary

| Field | Value |
|-------|-------|
| **Feature Name** | Audit Logs |
| **Priority** | P0 (MVP) |
| **Target Version** | v0.1 (MVP) |
| **Effort Estimate** | 3 weeks |
| **Owner** | Engineering |

### Description

Audit Logs provide comprehensive, immutable logging of all Claude API interactions for compliance, debugging, and security investigation.

### Problem Statement

Enterprises require audit trails for compliance:
- SOC 2 auditors require evidence of AI usage controls
- Security teams need to investigate incidents
- Compliance officers need to demonstrate governance
- No existing solution provides Claude-specific audit trails

### Success Metrics

| Metric | Target |
|--------|--------|
| Log Completeness | 100% of API calls logged |
| Search Performance | <3 seconds for 1 year |
| Audit Evidence | Pass SOC 2 audit |
| User Satisfaction | 4.2/5 rating |

---

## User Experience

### Entry Points

1. **Main Navigation:** "Audit" in left sidebar
2. **User Profile:** "View Activity" link
3. **Team Page:** "Audit Trail" tab
4. **MCP Detail:** "Usage Log" section

### Primary Screen: Audit Log Viewer

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← Audit Logs                                         Export ↓  Help ? │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Filters                                           [Clear All]   │  │
│  │                                                                   │  │
│  │  Date Range: [Dec 1, 2025] to [Dec 28, 2025]     🗓               │  │
│  │                                                                   │  │
│  │  User: [All Users ▼]      Team: [All Teams ▼]                    │  │
│  │                                                                   │  │
│  │  Model: [All Models ▼]    MCP: [All MCPs ▼]                      │  │
│  │                                                                   │  │
│  │  [Apply Filters]                                                  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  Showing 1,847 of 234,521 log entries                                   │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Timestamp          User          Team      Model    Tokens  MCPs│  │
│  │  ─────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  Dec 28, 14:32:18   susan@acme    Product   Sonnet   4,723  2   │  │
│  │  Dec 28, 14:31:45   david@acme    Backend   Opus     12,847  1  │  │
│  │  Dec 28, 14:31:02   maria@acme    Sales     Sonnet   2,156   1  │  │
│  │  Dec 28, 14:30:55   john@acme     Frontend  Haiku    891     0  │  │
│  │  Dec 28, 14:30:12   alice@acme    Backend   Sonnet   5,432   3  │  │
│  │  Dec 28, 14:29:48   emily@acme    ML        Opus     18,234  2  │  │
│  │  Dec 28, 14:29:15   carol@acme    Product   Sonnet   3,654   1  │  │
│  │  Dec 28, 14:28:33   bob@acme      Sales     Haiku    654     0  │  │
│  │  ...                                                              │  │
│  │                                                                   │  │
│  │  [1] [2] [3] [4] [5] ... [185]                    [50 ▼] per page│  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  Click row to view details →                                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Log Entry Detail

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Log Entry Details                                              [Close] │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  BASIC INFORMATION                                                │  │
│  │                                                                   │  │
│  │  Log ID:        log_7f8a9b2c3d4e5f6a                              │  │
│  │  Timestamp:     Dec 28, 2025 14:32:18.234 UTC                     │  │
│  │  User:          susan@acme.com (Susan Chen)                       │  │
│  │  Team:          Product                                           │  │
│  │  IP Address:    192.168.1.45                                      │  │
│  │  Client:        Claude Code v1.2.3                                │  │
│  │                                                                   │  │
│  │  ─────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  API DETAILS                                                      │  │
│  │                                                                   │  │
│  │  Model:         claude-3-5-sonnet-20241022                        │  │
│  │  Input Tokens:  2,847                                             │  │
│  │  Output Tokens: 1,876                                             │  │
│  │  Total Tokens:  4,723                                             │  │
│  │  Est. Cost:     $0.24                                             │  │
│  │  Latency:       1,234 ms                                          │  │
│  │  Status:        Success (200)                                     │  │
│  │                                                                   │  │
│  │  ─────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  MCPs USED                                                        │  │
│  │                                                                   │  │
│  │  • Salesforce CRM Reader (3 invocations)                         │  │
│  │  • Google Docs Writer (1 invocation)                             │  │
│  │                                                                   │  │
│  │  ─────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  ⚠️ Conversation content not logged (privacy policy)             │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Functional Requirements

### FR-1: Log All Claude API Calls

**Requirement:**
Capture every Claude API interaction.

**Details:**

| Field | Description | Required |
|-------|-------------|----------|
| log_id | Unique identifier | Yes |
| timestamp | UTC timestamp with milliseconds | Yes |
| org_id | Organization | Yes |
| user_id | User making request | Yes |
| team_id | User's team | Yes |
| model | Claude model used | Yes |
| input_tokens | Input token count | Yes |
| output_tokens | Output token count | Yes |
| mcps_used | List of MCPs invoked | Yes |
| status_code | API response code | Yes |
| latency_ms | Response time | Yes |
| ip_address | Client IP | Yes |
| user_agent | Client application | Yes |
| conversation_id | Claude conversation ID | Optional |
| cost_estimate | Estimated cost | Calculated |

**Acceptance Criteria:**
- [ ] All API calls logged
- [ ] Logs written within 5 seconds
- [ ] No data loss under load
- [ ] Accurate token counts

---

### FR-2: Log Immutability

**Requirement:**
Audit logs cannot be modified or deleted.

**Details:**
- Write-once storage
- No delete API for logs
- Cryptographic integrity (hash chain)
- Tamper detection

**Acceptance Criteria:**
- [ ] No delete endpoint exists
- [ ] API rejects update requests
- [ ] Hash chain implemented
- [ ] Tamper alerts work

---

### FR-3: Search and Filter

**Requirement:**
Fast search across log entries.

**Details:**
- Search by: user, team, date, model, MCP
- Combined filters
- Full-text search (optional)
- Saved searches

**Acceptance Criteria:**
- [ ] All filters work correctly
- [ ] Search returns in <3 seconds
- [ ] Combined filters work
- [ ] Results are accurate

---

### FR-4: Log Retention

**Requirement:**
Configurable log retention.

**Details:**
- Default: 365 days
- Options: 90, 180, 365, 730 days, Forever
- Compliance hold (prevent deletion)
- Archival to cold storage

**Acceptance Criteria:**
- [ ] Retention configurable
- [ ] Old logs archived/deleted per policy
- [ ] Compliance hold prevents deletion
- [ ] Archival works correctly

---

### FR-5: Export Functionality

**Requirement:**
Export logs for compliance and analysis.

**Details:**
- CSV export
- JSON export
- Excel export
- Date range filter
- Maximum 100k records per export

**Acceptance Criteria:**
- [ ] All formats work
- [ ] Export completes in <60 seconds
- [ ] Exported data matches UI
- [ ] Large exports handled

---

### FR-6: Privacy Controls

**Requirement:**
Protect user privacy while maintaining audit capability.

**Details:**
- Conversation content NOT logged by default
- Optional: log prompts only, or full conversation
- PII masking option
- User consent tracking

**Acceptance Criteria:**
- [ ] Content not logged by default
- [ ] Optional content logging works
- [ ] PII masking works
- [ ] Settings documented

---

### FR-7: Access Control

**Requirement:**
Restrict access to audit logs.

**Details:**
- Org Admin: All logs
- Team Admin: Team logs only
- Compliance Officer: All logs (read-only)
- Member: Own logs only

**Acceptance Criteria:**
- [ ] RBAC enforced
- [ ] Users see only permitted logs
- [ ] Access attempts logged
- [ ] Export restricted by role

---

## Non-Functional Requirements

### NFR-1: Performance

| Metric | Requirement |
|--------|-------------|
| Log write latency | <100ms |
| Search response | <3 seconds |
| Export time | <60 seconds |
| Throughput | 10,000 logs/second |

### NFR-2: Reliability

| Metric | Requirement |
|--------|-------------|
| Log delivery | 99.99% |
| Data durability | 99.999999999% (11 9s) |
| Availability | 99.9% |

### NFR-3: Security

| Requirement | Implementation |
|-------------|----------------|
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.3 |
| Access logging | All access logged |
| Integrity | SHA-256 hash chain |

---

## Data Model

```sql
-- Audit logs table (partitioned by month)
CREATE TABLE audit_logs (
  id UUID PRIMARY KEY,
  org_id UUID NOT NULL,
  user_id UUID NOT NULL,
  team_id UUID,
  timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  model VARCHAR(100) NOT NULL,
  input_tokens INTEGER NOT NULL,
  output_tokens INTEGER NOT NULL,
  total_tokens INTEGER GENERATED ALWAYS AS (input_tokens + output_tokens) STORED,
  mcps_used JSONB DEFAULT '[]',
  status_code INTEGER NOT NULL,
  latency_ms INTEGER,
  ip_address INET,
  user_agent VARCHAR(500),
  conversation_id VARCHAR(100),
  cost_estimate DECIMAL(10,4),
  metadata JSONB DEFAULT '{}',
  hash VARCHAR(64),

  -- Partitioning
  created_month DATE NOT NULL
) PARTITION BY RANGE (created_month);

-- Create monthly partitions
CREATE TABLE audit_logs_2025_12 PARTITION OF audit_logs
  FOR VALUES FROM ('2025-12-01') TO ('2026-01-01');

-- Indexes
CREATE INDEX idx_audit_org_time ON audit_logs(org_id, timestamp DESC);
CREATE INDEX idx_audit_user ON audit_logs(user_id, timestamp DESC);
CREATE INDEX idx_audit_team ON audit_logs(team_id, timestamp DESC);
CREATE INDEX idx_audit_model ON audit_logs(model);
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/audit-logs` | GET | List logs (with filters) |
| `/api/audit-logs/:id` | GET | Get log entry |
| `/api/audit-logs/export` | POST | Export logs |
| `/api/audit-logs/stats` | GET | Aggregate statistics |
| `/api/audit-logs/search` | POST | Advanced search |

---

## Compliance Mapping

### SOC 2 Controls

| Control | Evidence |
|---------|----------|
| CC6.1 (Access) | Log access attempts |
| CC7.2 (Monitoring) | Real-time log capture |
| CC7.3 (Detection) | Anomaly alerts |
| CC7.4 (Response) | Investigation capability |

### GDPR

| Article | Implementation |
|---------|----------------|
| Art. 30 (Records) | Processing activity log |
| Art. 33 (Breach) | Incident investigation |

---

## Related Documents

- [PRD-MVP.md](../PRD-MVP.md) - MVP requirements
- [FEATURE-TOKEN-DASHBOARD.md](./FEATURE-TOKEN-DASHBOARD.md) - Usage dashboard
- [../wireframes/WIREFRAME-AUDIT-LOGS.md](../wireframes/WIREFRAME-AUDIT-LOGS.md)

---

*Last Updated: December 2025*
*Owner: Engineering Lead*

# MindWeave Database Schema Design

## Document Information
| Field | Value |
|-------|-------|
| Document ID | ENG-004 |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Owner | Engineering Team |
| Status | Draft |
| Classification | Internal |

---

## Executive Summary

This document defines MindWeave's database schema, including entity relationships, table structures, indexing strategies, and data partitioning approaches. We use a polyglot persistence strategy with PostgreSQL for transactional data and TimescaleDB for time-series analytics.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     MINDWEAVE DATA ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    TRANSACTIONAL LAYER (PostgreSQL)                  │   │
│  │                                                                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐    │   │
│  │  │   Users    │  │   Orgs     │  │  Projects  │  │   Teams    │    │   │
│  │  │            │  │            │  │            │  │            │    │   │
│  │  │ • Profile  │  │ • Settings │  │ • Config   │  │ • Members  │    │   │
│  │  │ • Auth     │  │ • Billing  │  │ • API Keys │  │ • Roles    │    │   │
│  │  │ • Sessions │  │ • Plans    │  │ • Quotas   │  │ • Invites  │    │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘    │   │
│  │                                                                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐    │   │
│  │  │    MCP     │  │  Policies  │  │   Alerts   │  │   Audit    │    │   │
│  │  │  Registry  │  │            │  │            │  │    Log     │    │   │
│  │  │            │  │ • Rules    │  │ • Rules    │  │            │    │   │
│  │  │ • Servers  │  │ • Scopes   │  │ • History  │  │ • Events   │    │   │
│  │  │ • Tools    │  │ • Actions  │  │ • Channels │  │ • Changes  │    │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                   TIME-SERIES LAYER (TimescaleDB)                    │   │
│  │                                                                      │   │
│  │  ┌─────────────────────────────────────────────────────────────────┐│   │
│  │  │                     USAGE EVENTS                                 ││   │
│  │  │  • API Calls  • Token Counts  • Costs  • Latencies  • Errors   ││   │
│  │  └─────────────────────────────────────────────────────────────────┘│   │
│  │                                                                      │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐ │   │
│  │  │  1-min Aggs     │  │  Hourly Aggs    │  │   Daily Aggs        │ │   │
│  │  │  (7 days)       │  │  (90 days)      │  │   (Forever)         │ │   │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────┘ │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Database Strategy

### 1.1 Polyglot Persistence

| Database | Purpose | Data Types | Retention |
|----------|---------|------------|-----------|
| **PostgreSQL 15** | Transactional data | Users, Orgs, Config | Indefinite |
| **TimescaleDB 2.x** | Time-series analytics | Usage events, Metrics | Tiered |
| **Redis 7.x** | Caching, Sessions | Hot data, Rate limits | Ephemeral |
| **S3** | Object storage | Exports, Backups | Per policy |

### 1.2 Design Principles

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **Normalization** | 3NF for transactional data | Foreign keys, joins |
| **Denormalization** | Time-series for performance | Pre-aggregated views |
| **Soft Deletes** | Preserve history | `deleted_at` timestamp |
| **Auditing** | Track all changes | Trigger-based audit log |
| **Multi-tenancy** | Data isolation | `org_id` on all tables |
| **UUIDs** | Globally unique IDs | `uuid_generate_v4()` |

---

## 2. Core Entity Relationships

### 2.1 Entity Relationship Diagram

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    ENTITY RELATIONSHIP DIAGRAM                              │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐          │
│  │    USER     │    N    │   ORG_      │    N    │   PROJECT   │          │
│  │             │◄────────│   MEMBER    │────────►│             │          │
│  │  id (PK)    │         │             │         │  id (PK)    │          │
│  │  email      │         │  user_id    │         │  org_id (FK)│          │
│  │  name       │         │  org_id     │         │  name       │          │
│  │  avatar_url │         │  role       │         │  settings   │          │
│  └──────┬──────┘         └─────────────┘         └──────┬──────┘          │
│         │                       │                        │                 │
│         │                       │                        │                 │
│         │                 ┌─────▼─────┐                  │                 │
│         │                 │    ORG    │                  │                 │
│         │                 │           │                  │                 │
│         │                 │  id (PK)  │                  │                 │
│         │                 │  name     │                  │                 │
│         │                 │  slug     │                  │                 │
│         │                 │  settings │                  │                 │
│         │                 └─────┬─────┘                  │                 │
│         │                       │                        │                 │
│         │                       │ 1                      │                 │
│         │                       │                        │                 │
│         │                 ┌─────▼─────┐                  │                 │
│         │                 │SUBSCRIPTION                  │                 │
│         │                 │           │                  │                 │
│         │                 │  id (PK)  │                  │                 │
│         │                 │  org_id   │                  │                 │
│         │                 │  plan     │                  │                 │
│         │                 │  status   │                  │                 │
│         │                 └───────────┘                  │                 │
│         │                                                │                 │
│         │         ┌─────────────┐         ┌─────────────┤                 │
│         │         │  MCP_SERVER │    N    │             │                 │
│         └────────►│             │◄────────┘             │                 │
│            owns   │  id (PK)    │    belongs            │                 │
│                   │  project_id │                       │                 │
│                   │  name       │◄──────────────────────┘                 │
│                   │  status     │         project has N                   │
│                   │  manifest   │                                         │
│                   └──────┬──────┘                                         │
│                          │                                                 │
│                          │ 1                                              │
│                          │                                                 │
│                    ┌─────▼─────┐                                          │
│                    │ MCP_TOOL  │                                          │
│                    │           │                                          │
│                    │  id (PK)  │                                          │
│                    │ server_id │                                          │
│                    │  name     │                                          │
│                    │  schema   │                                          │
│                    └───────────┘                                          │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Relationship Summary

| Parent | Child | Relationship | On Delete |
|--------|-------|--------------|-----------|
| User | OrgMember | 1:N | Cascade |
| Organization | OrgMember | 1:N | Cascade |
| Organization | Project | 1:N | Cascade |
| Organization | Subscription | 1:1 | Set Null |
| Project | APIKey | 1:N | Cascade |
| Project | MCPServer | 1:N | Cascade |
| MCPServer | MCPTool | 1:N | Cascade |
| Organization | Policy | 1:N | Cascade |
| Project | Policy | 1:N | Cascade |

---

## 3. Table Definitions

### 3.1 Users Table

```sql
-- Users table: Authentication and profile information
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Authentication
    email VARCHAR(255) NOT NULL UNIQUE,
    email_verified BOOLEAN NOT NULL DEFAULT FALSE,
    password_hash VARCHAR(255),  -- NULL for OAuth-only users

    -- Profile
    name VARCHAR(255) NOT NULL,
    avatar_url VARCHAR(500),
    timezone VARCHAR(50) DEFAULT 'UTC',
    locale VARCHAR(10) DEFAULT 'en-US',

    -- MFA
    mfa_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    mfa_secret VARCHAR(255),
    mfa_backup_codes TEXT[],

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'suspended', 'pending_verification')),
    last_login_at TIMESTAMPTZ,
    last_login_ip INET,

    -- Metadata
    settings JSONB NOT NULL DEFAULT '{}',
    metadata JSONB NOT NULL DEFAULT '{}',

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ
);

-- Indexes
CREATE INDEX idx_users_email ON users(email) WHERE deleted_at IS NULL;
CREATE INDEX idx_users_status ON users(status) WHERE deleted_at IS NULL;
CREATE INDEX idx_users_created_at ON users(created_at);

-- Full-text search
CREATE INDEX idx_users_name_search ON users USING gin(to_tsvector('english', name));
```

### 3.2 Organizations Table

```sql
-- Organizations table: Multi-tenant account structure
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Identity
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) NOT NULL UNIQUE,

    -- Contact
    billing_email VARCHAR(255),
    support_email VARCHAR(255),

    -- Settings
    settings JSONB NOT NULL DEFAULT '{
        "default_model": "claude-3-sonnet",
        "require_mcp_approval": true,
        "audit_retention_days": 90
    }',

    -- Billing
    stripe_customer_id VARCHAR(255),

    -- Security
    sso_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    sso_provider VARCHAR(50),
    sso_config JSONB,
    allowed_email_domains TEXT[],

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'suspended', 'pending')),

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ
);

-- Indexes
CREATE UNIQUE INDEX idx_orgs_slug ON organizations(slug) WHERE deleted_at IS NULL;
CREATE INDEX idx_orgs_status ON organizations(status) WHERE deleted_at IS NULL;
CREATE INDEX idx_orgs_stripe_customer ON organizations(stripe_customer_id);
```

### 3.3 Organization Members Table

```sql
-- Organization members: User-organization relationships
CREATE TABLE org_members (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Relationships
    org_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    -- Role
    role VARCHAR(20) NOT NULL DEFAULT 'member'
        CHECK (role IN ('owner', 'admin', 'member', 'viewer')),

    -- Invitation
    invited_by UUID REFERENCES users(id),
    invited_at TIMESTAMPTZ,
    accepted_at TIMESTAMPTZ,

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'invited', 'suspended')),

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Constraints
    UNIQUE(org_id, user_id)
);

-- Indexes
CREATE INDEX idx_org_members_user ON org_members(user_id);
CREATE INDEX idx_org_members_org ON org_members(org_id);
CREATE INDEX idx_org_members_role ON org_members(org_id, role);
```

### 3.4 Projects Table

```sql
-- Projects table: Resource containers within organizations
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Relationships
    org_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,

    -- Identity
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) NOT NULL,
    description TEXT,

    -- Configuration
    settings JSONB NOT NULL DEFAULT '{
        "allowed_models": ["claude-3-opus", "claude-3-sonnet", "claude-3-haiku"],
        "default_model": "claude-3-sonnet",
        "mcp_auto_approve": false
    }',

    -- Quotas
    quotas JSONB NOT NULL DEFAULT '{
        "max_tokens_per_day": null,
        "max_cost_per_day_usd": null,
        "max_requests_per_minute": 100
    }',

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'paused', 'archived')),

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ,

    -- Constraints
    UNIQUE(org_id, slug)
);

-- Indexes
CREATE INDEX idx_projects_org ON projects(org_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_projects_status ON projects(org_id, status) WHERE deleted_at IS NULL;
```

### 3.5 API Keys Table

```sql
-- API keys table: Project authentication
CREATE TABLE api_keys (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Relationships
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id),

    -- Key
    key_prefix VARCHAR(20) NOT NULL,  -- mw_sk_live_, mw_sk_test_
    key_hash VARCHAR(64) NOT NULL,    -- SHA-256 hash

    -- Metadata
    name VARCHAR(255) NOT NULL,
    description TEXT,

    -- Permissions
    scopes TEXT[] NOT NULL DEFAULT ARRAY['read', 'write'],
    allowed_ips INET[],

    -- Usage
    last_used_at TIMESTAMPTZ,
    last_used_ip INET,
    usage_count BIGINT NOT NULL DEFAULT 0,

    -- Expiration
    expires_at TIMESTAMPTZ,

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'revoked', 'expired')),
    revoked_at TIMESTAMPTZ,
    revoked_by UUID REFERENCES users(id),

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_api_keys_project ON api_keys(project_id) WHERE status = 'active';
CREATE INDEX idx_api_keys_prefix_hash ON api_keys(key_prefix, key_hash);
CREATE INDEX idx_api_keys_last_used ON api_keys(last_used_at);
```

### 3.6 MCP Servers Table

```sql
-- MCP servers table: Registered MCP server configurations
CREATE TABLE mcp_servers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Relationships
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    registered_by UUID NOT NULL REFERENCES users(id),

    -- Identity
    name VARCHAR(255) NOT NULL,
    description TEXT,
    version VARCHAR(50),

    -- Transport configuration
    transport_type VARCHAR(20) NOT NULL
        CHECK (transport_type IN ('stdio', 'sse', 'http')),
    transport_config JSONB NOT NULL,
    -- Example: {"command": "npx", "args": ["-y", "@github/mcp-server"]}

    -- Environment
    environment JSONB NOT NULL DEFAULT '{}',
    -- Example: {"GITHUB_TOKEN": "${secrets.GITHUB_TOKEN}"}

    -- Manifest
    manifest JSONB,
    manifest_url VARCHAR(500),

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'approved', 'rejected', 'deprecated')),

    -- Approval
    approved_by UUID REFERENCES users(id),
    approved_at TIMESTAMPTZ,
    rejection_reason TEXT,

    -- Security scan
    security_scan_status VARCHAR(20) DEFAULT 'pending'
        CHECK (security_scan_status IN ('pending', 'running', 'passed', 'failed')),
    security_scan_results JSONB,
    last_scanned_at TIMESTAMPTZ,

    -- Policy
    policy JSONB NOT NULL DEFAULT '{
        "allowed_roles": ["admin", "developer"],
        "rate_limit_per_minute": 100,
        "requires_approval_per_use": false
    }',

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ,

    -- Constraints
    UNIQUE(project_id, name) WHERE deleted_at IS NULL
);

-- Indexes
CREATE INDEX idx_mcp_servers_project ON mcp_servers(project_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_mcp_servers_status ON mcp_servers(project_id, status) WHERE deleted_at IS NULL;
```

### 3.7 MCP Tools Table

```sql
-- MCP tools table: Tools provided by MCP servers
CREATE TABLE mcp_tools (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Relationships
    server_id UUID NOT NULL REFERENCES mcp_servers(id) ON DELETE CASCADE,

    -- Identity
    name VARCHAR(255) NOT NULL,
    description TEXT,

    -- Schema
    input_schema JSONB NOT NULL,

    -- Risk assessment
    risk_level VARCHAR(20) NOT NULL DEFAULT 'low'
        CHECK (risk_level IN ('low', 'medium', 'high', 'critical')),
    risk_notes TEXT,

    -- Status
    enabled BOOLEAN NOT NULL DEFAULT TRUE,

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Constraints
    UNIQUE(server_id, name)
);

-- Indexes
CREATE INDEX idx_mcp_tools_server ON mcp_tools(server_id);
CREATE INDEX idx_mcp_tools_risk ON mcp_tools(server_id, risk_level);
```

### 3.8 Policies Table

```sql
-- Policies table: Governance rules and quotas
CREATE TABLE policies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Relationships (one of org_id or project_id required)
    org_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id),

    -- Identity
    name VARCHAR(255) NOT NULL,
    description TEXT,

    -- Policy type
    type VARCHAR(20) NOT NULL
        CHECK (type IN ('usage', 'access', 'compliance', 'custom')),

    -- Rules (JSON schema varies by type)
    rules JSONB NOT NULL,
    -- Usage example: {"max_tokens_per_day": 1000000, "action": "soft_limit"}
    -- Access example: {"allowed_models": ["claude-3-sonnet"], "blocked_mcp_tools": ["delete_*"]}

    -- Scope
    applies_to JSONB NOT NULL DEFAULT '{
        "users": ["all"],
        "projects": ["all"],
        "models": ["all"]
    }',

    -- Priority (higher = evaluated first)
    priority INTEGER NOT NULL DEFAULT 100,

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'disabled', 'draft')),

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ,

    -- Constraints
    CHECK (org_id IS NOT NULL OR project_id IS NOT NULL)
);

-- Indexes
CREATE INDEX idx_policies_org ON policies(org_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_policies_project ON policies(project_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_policies_type ON policies(type, status) WHERE deleted_at IS NULL;
CREATE INDEX idx_policies_priority ON policies(priority DESC);
```

### 3.9 Subscriptions Table

```sql
-- Subscriptions table: Billing plans and status
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Relationships
    org_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE UNIQUE,

    -- Plan
    plan VARCHAR(20) NOT NULL DEFAULT 'free'
        CHECK (plan IN ('free', 'team', 'pro', 'enterprise')),

    -- Stripe
    stripe_subscription_id VARCHAR(255),
    stripe_price_id VARCHAR(255),

    -- Billing
    billing_cycle VARCHAR(20) NOT NULL DEFAULT 'monthly'
        CHECK (billing_cycle IN ('monthly', 'yearly')),

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'past_due', 'canceled', 'trialing')),

    -- Dates
    current_period_start TIMESTAMPTZ,
    current_period_end TIMESTAMPTZ,
    trial_end TIMESTAMPTZ,
    canceled_at TIMESTAMPTZ,

    -- Limits (plan-specific)
    limits JSONB NOT NULL DEFAULT '{
        "max_users": 5,
        "max_projects": 3,
        "max_tokens_per_month": 1000000,
        "max_mcp_servers": 10
    }',

    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE UNIQUE INDEX idx_subscriptions_org ON subscriptions(org_id);
CREATE INDEX idx_subscriptions_stripe ON subscriptions(stripe_subscription_id);
CREATE INDEX idx_subscriptions_status ON subscriptions(status);
```

---

## 4. Time-Series Tables (TimescaleDB)

### 4.1 Usage Events Table

```sql
-- Usage events hypertable: Raw API usage data
CREATE TABLE usage_events (
    time TIMESTAMPTZ NOT NULL,

    -- Context
    org_id UUID NOT NULL,
    project_id UUID NOT NULL,
    user_id UUID,
    api_key_id UUID,

    -- Request
    request_id UUID NOT NULL,
    event_type VARCHAR(20) NOT NULL
        CHECK (event_type IN ('api_call', 'mcp_tool', 'streaming')),

    -- Model
    model VARCHAR(50) NOT NULL,

    -- Tokens
    input_tokens INTEGER NOT NULL DEFAULT 0,
    output_tokens INTEGER NOT NULL DEFAULT 0,
    cache_read_tokens INTEGER NOT NULL DEFAULT 0,
    cache_write_tokens INTEGER NOT NULL DEFAULT 0,

    -- Cost (in USD cents for precision)
    cost_cents INTEGER NOT NULL DEFAULT 0,

    -- Performance
    latency_ms INTEGER,
    time_to_first_token_ms INTEGER,

    -- MCP (if applicable)
    mcp_server_id UUID,
    mcp_tool_name VARCHAR(255),

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'success'
        CHECK (status IN ('success', 'error', 'timeout', 'rate_limited')),
    error_code VARCHAR(50),
    error_message TEXT,

    -- Metadata
    metadata JSONB NOT NULL DEFAULT '{}'
);

-- Convert to hypertable
SELECT create_hypertable('usage_events', 'time',
    chunk_time_interval => INTERVAL '1 day');

-- Compression
ALTER TABLE usage_events SET (
    timescaledb.compress,
    timescaledb.compress_segmentby = 'org_id, project_id',
    timescaledb.compress_orderby = 'time DESC'
);

-- Add compression policy (compress after 7 days)
SELECT add_compression_policy('usage_events', INTERVAL '7 days');

-- Retention policy (keep raw data for 30 days)
SELECT add_retention_policy('usage_events', INTERVAL '30 days');

-- Indexes
CREATE INDEX idx_usage_events_org_time ON usage_events(org_id, time DESC);
CREATE INDEX idx_usage_events_project_time ON usage_events(project_id, time DESC);
CREATE INDEX idx_usage_events_user_time ON usage_events(user_id, time DESC)
    WHERE user_id IS NOT NULL;
CREATE INDEX idx_usage_events_model ON usage_events(model, time DESC);
CREATE INDEX idx_usage_events_mcp ON usage_events(mcp_server_id, time DESC)
    WHERE mcp_server_id IS NOT NULL;
```

### 4.2 Continuous Aggregates

```sql
-- Hourly aggregation continuous aggregate
CREATE MATERIALIZED VIEW usage_hourly
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', time) AS bucket,
    org_id,
    project_id,
    model,

    -- Counts
    COUNT(*) AS request_count,
    COUNT(*) FILTER (WHERE status = 'success') AS success_count,
    COUNT(*) FILTER (WHERE status = 'error') AS error_count,

    -- Tokens
    SUM(input_tokens) AS total_input_tokens,
    SUM(output_tokens) AS total_output_tokens,
    SUM(cache_read_tokens) AS total_cache_read_tokens,

    -- Cost
    SUM(cost_cents) AS total_cost_cents,

    -- Latency
    AVG(latency_ms) AS avg_latency_ms,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY latency_ms) AS p50_latency_ms,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY latency_ms) AS p95_latency_ms,
    PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY latency_ms) AS p99_latency_ms,

    -- Unique users
    COUNT(DISTINCT user_id) AS unique_users

FROM usage_events
GROUP BY bucket, org_id, project_id, model
WITH NO DATA;

-- Refresh policy (every hour)
SELECT add_continuous_aggregate_policy('usage_hourly',
    start_offset => INTERVAL '3 hours',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour');

-- Daily aggregation
CREATE MATERIALIZED VIEW usage_daily
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 day', time) AS bucket,
    org_id,
    project_id,
    model,
    user_id,

    COUNT(*) AS request_count,
    SUM(input_tokens) AS total_input_tokens,
    SUM(output_tokens) AS total_output_tokens,
    SUM(cost_cents) AS total_cost_cents,
    AVG(latency_ms) AS avg_latency_ms

FROM usage_events
GROUP BY bucket, org_id, project_id, model, user_id
WITH NO DATA;

SELECT add_continuous_aggregate_policy('usage_daily',
    start_offset => INTERVAL '3 days',
    end_offset => INTERVAL '1 day',
    schedule_interval => INTERVAL '1 day');

-- Monthly aggregation
CREATE MATERIALIZED VIEW usage_monthly
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 month', time) AS bucket,
    org_id,
    project_id,
    model,

    COUNT(*) AS request_count,
    SUM(input_tokens) AS total_input_tokens,
    SUM(output_tokens) AS total_output_tokens,
    SUM(cost_cents) AS total_cost_cents,
    COUNT(DISTINCT user_id) AS unique_users,
    COUNT(DISTINCT DATE(time)) AS active_days

FROM usage_events
GROUP BY bucket, org_id, project_id, model
WITH NO DATA;

SELECT add_continuous_aggregate_policy('usage_monthly',
    start_offset => INTERVAL '3 months',
    end_offset => INTERVAL '1 month',
    schedule_interval => INTERVAL '1 day');
```

### 4.3 MCP Usage Table

```sql
-- MCP tool usage tracking
CREATE TABLE mcp_usage (
    time TIMESTAMPTZ NOT NULL,

    -- Context
    org_id UUID NOT NULL,
    project_id UUID NOT NULL,
    user_id UUID,

    -- MCP
    server_id UUID NOT NULL,
    tool_name VARCHAR(255) NOT NULL,

    -- Request
    request_id UUID NOT NULL,
    parent_request_id UUID,  -- Link to Claude API call

    -- Execution
    latency_ms INTEGER,
    status VARCHAR(20) NOT NULL
        CHECK (status IN ('success', 'error', 'timeout', 'blocked')),
    error_message TEXT,

    -- Input/Output size (bytes)
    input_size INTEGER,
    output_size INTEGER,

    -- Metadata
    metadata JSONB NOT NULL DEFAULT '{}'
);

SELECT create_hypertable('mcp_usage', 'time',
    chunk_time_interval => INTERVAL '1 day');

-- Indexes
CREATE INDEX idx_mcp_usage_server ON mcp_usage(server_id, time DESC);
CREATE INDEX idx_mcp_usage_tool ON mcp_usage(server_id, tool_name, time DESC);
CREATE INDEX idx_mcp_usage_project ON mcp_usage(project_id, time DESC);
```

---

## 5. Audit and Compliance

### 5.1 Audit Log Table

```sql
-- Audit log: Immutable record of all changes
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    time TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Actor
    actor_type VARCHAR(20) NOT NULL
        CHECK (actor_type IN ('user', 'api_key', 'system', 'webhook')),
    actor_id UUID,
    actor_ip INET,
    actor_user_agent TEXT,

    -- Context
    org_id UUID,
    project_id UUID,

    -- Action
    action VARCHAR(50) NOT NULL,
    -- Examples: 'user.login', 'project.create', 'mcp_server.approve', 'policy.update'

    -- Resource
    resource_type VARCHAR(50) NOT NULL,
    resource_id UUID,

    -- Changes
    changes JSONB,
    -- Example: {"name": {"old": "Old Name", "new": "New Name"}}

    -- Request context
    request_id UUID,

    -- Compliance flags
    sensitive BOOLEAN NOT NULL DEFAULT FALSE,
    retention_days INTEGER
);

-- Convert to hypertable for efficient time-based queries
SELECT create_hypertable('audit_logs', 'time',
    chunk_time_interval => INTERVAL '1 month');

-- Indexes
CREATE INDEX idx_audit_logs_org ON audit_logs(org_id, time DESC);
CREATE INDEX idx_audit_logs_actor ON audit_logs(actor_id, time DESC);
CREATE INDEX idx_audit_logs_resource ON audit_logs(resource_type, resource_id, time DESC);
CREATE INDEX idx_audit_logs_action ON audit_logs(action, time DESC);

-- Retention (keep for 1 year by default)
SELECT add_retention_policy('audit_logs', INTERVAL '365 days');
```

### 5.2 Audit Trigger Function

```sql
-- Generic audit trigger function
CREATE OR REPLACE FUNCTION audit_trigger_func()
RETURNS TRIGGER AS $$
DECLARE
    changes_json JSONB;
    old_json JSONB;
    new_json JSONB;
BEGIN
    IF TG_OP = 'DELETE' THEN
        changes_json = jsonb_build_object('deleted', to_jsonb(OLD));
        INSERT INTO audit_logs (
            actor_type, actor_id, org_id, action,
            resource_type, resource_id, changes
        ) VALUES (
            'system',
            current_setting('app.current_user_id', true)::uuid,
            COALESCE(OLD.org_id, current_setting('app.current_org_id', true)::uuid),
            TG_TABLE_NAME || '.delete',
            TG_TABLE_NAME,
            OLD.id,
            changes_json
        );
        RETURN OLD;
    ELSIF TG_OP = 'UPDATE' THEN
        old_json = to_jsonb(OLD);
        new_json = to_jsonb(NEW);

        -- Calculate only changed fields
        SELECT jsonb_object_agg(
            key,
            jsonb_build_object('old', old_json->key, 'new', new_json->key)
        )
        INTO changes_json
        FROM jsonb_each(new_json)
        WHERE new_json->key IS DISTINCT FROM old_json->key
          AND key NOT IN ('updated_at');

        IF changes_json IS NOT NULL THEN
            INSERT INTO audit_logs (
                actor_type, actor_id, org_id, action,
                resource_type, resource_id, changes
            ) VALUES (
                'system',
                current_setting('app.current_user_id', true)::uuid,
                COALESCE(NEW.org_id, current_setting('app.current_org_id', true)::uuid),
                TG_TABLE_NAME || '.update',
                TG_TABLE_NAME,
                NEW.id,
                changes_json
            );
        END IF;
        RETURN NEW;
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO audit_logs (
            actor_type, actor_id, org_id, action,
            resource_type, resource_id, changes
        ) VALUES (
            'system',
            current_setting('app.current_user_id', true)::uuid,
            COALESCE(NEW.org_id, current_setting('app.current_org_id', true)::uuid),
            TG_TABLE_NAME || '.create',
            TG_TABLE_NAME,
            NEW.id,
            jsonb_build_object('created', to_jsonb(NEW))
        );
        RETURN NEW;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Apply to tables
CREATE TRIGGER audit_organizations
    AFTER INSERT OR UPDATE OR DELETE ON organizations
    FOR EACH ROW EXECUTE FUNCTION audit_trigger_func();

CREATE TRIGGER audit_projects
    AFTER INSERT OR UPDATE OR DELETE ON projects
    FOR EACH ROW EXECUTE FUNCTION audit_trigger_func();

CREATE TRIGGER audit_mcp_servers
    AFTER INSERT OR UPDATE OR DELETE ON mcp_servers
    FOR EACH ROW EXECUTE FUNCTION audit_trigger_func();

CREATE TRIGGER audit_policies
    AFTER INSERT OR UPDATE OR DELETE ON policies
    FOR EACH ROW EXECUTE FUNCTION audit_trigger_func();
```

---

## 6. Indexing Strategy

### 6.1 Index Summary

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         INDEXING STRATEGY                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  INDEX TYPES USED:                                                         │
│  ─────────────────                                                         │
│                                                                             │
│  B-Tree (default)                                                          │
│  • Primary keys, foreign keys                                              │
│  • Equality and range queries                                              │
│  • Most common queries                                                     │
│                                                                             │
│  GIN (Generalized Inverted Index)                                         │
│  • JSONB columns                                                           │
│  • Array columns                                                           │
│  • Full-text search                                                        │
│                                                                             │
│  BRIN (Block Range Index)                                                  │
│  • Time-series data                                                        │
│  • Large sequential tables                                                 │
│  • Low maintenance overhead                                                │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  PARTIAL INDEXES:                                                          │
│  ────────────────                                                          │
│                                                                             │
│  WHERE deleted_at IS NULL    -- Soft delete optimization                  │
│  WHERE status = 'active'     -- Active records only                       │
│  WHERE column IS NOT NULL    -- Non-null optimization                     │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  COMPOSITE INDEXES:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│  (org_id, created_at)        -- Org timeline queries                      │
│  (project_id, status)        -- Project filtering                         │
│  (user_id, time DESC)        -- User activity                             │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Query Patterns and Indexes

| Query Pattern | Index | Type |
|--------------|-------|------|
| Get user by email | `idx_users_email` | B-Tree (Unique) |
| List org projects | `idx_projects_org` | B-Tree (Partial) |
| Get MCP server tools | `idx_mcp_tools_server` | B-Tree |
| Search users by name | `idx_users_name_search` | GIN |
| Usage by org/time | `idx_usage_events_org_time` | B-Tree |
| Audit by resource | `idx_audit_logs_resource` | B-Tree |
| JSONB settings query | `idx_*_settings` | GIN |

---

## 7. Data Migration Strategy

### 7.1 Migration Workflow

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      MIGRATION WORKFLOW                                     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                    ┌─────────────────────┐                                 │
│                    │   Migration File    │                                 │
│                    │   (Timestamp_name)  │                                 │
│                    └──────────┬──────────┘                                 │
│                               │                                            │
│               ┌───────────────┼───────────────┐                           │
│               │               │               │                           │
│               ▼               ▼               ▼                           │
│        ┌──────────┐    ┌──────────┐    ┌──────────┐                      │
│        │   Up     │    │  Down    │    │  Test    │                      │
│        │ Function │    │ Function │    │   Data   │                      │
│        └────┬─────┘    └────┬─────┘    └────┬─────┘                      │
│             │               │               │                             │
│             ▼               ▼               ▼                             │
│        Apply schema    Rollback        Validate                          │
│        changes         changes         migration                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  MIGRATION PRINCIPLES:                                                     │
│                                                                             │
│  1. Every migration must be reversible                                    │
│  2. Migrations must be idempotent                                         │
│  3. Schema changes separate from data migrations                          │
│  4. Large data migrations use batching                                    │
│  5. Zero-downtime deployment compatibility                                │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  ZERO-DOWNTIME PATTERNS:                                                   │
│                                                                             │
│  Adding column:                                                            │
│  1. Add nullable column                                                   │
│  2. Deploy code that writes to new column                                 │
│  3. Backfill existing data                                                │
│  4. Add NOT NULL constraint if needed                                     │
│                                                                             │
│  Renaming column:                                                          │
│  1. Add new column                                                        │
│  2. Deploy code that writes to both                                       │
│  3. Backfill new column                                                   │
│  4. Deploy code that reads from new                                       │
│  5. Remove old column                                                     │
│                                                                             │
│  Dropping column:                                                          │
│  1. Deploy code that doesn't read column                                  │
│  2. Deploy code that doesn't write column                                 │
│  3. Drop column                                                           │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Migration Tools

```bash
# Migration commands (using golang-migrate or similar)

# Create new migration
migrate create -ext sql -dir migrations -seq add_mcp_risk_level

# Run migrations
migrate -path migrations -database "$DATABASE_URL" up

# Rollback last migration
migrate -path migrations -database "$DATABASE_URL" down 1

# Check migration status
migrate -path migrations -database "$DATABASE_URL" version
```

---

## 8. Backup and Recovery

### 8.1 Backup Strategy

| Type | Frequency | Retention | Tool |
|------|-----------|-----------|------|
| Full backup | Daily | 30 days | pg_dump |
| Incremental | Hourly | 7 days | WAL archiving |
| Point-in-time | Continuous | 7 days | WAL streaming |
| Cross-region | Daily | 14 days | RDS cross-region |

### 8.2 Recovery Procedures

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      RECOVERY PROCEDURES                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SCENARIO 1: Single Table Recovery                                         │
│  ─────────────────────────────────                                         │
│  1. Restore backup to staging                                              │
│  2. Export affected table                                                  │
│  3. Import to production                                                   │
│  RTO: 30 minutes                                                           │
│                                                                             │
│  SCENARIO 2: Database Corruption                                           │
│  ──────────────────────────────                                            │
│  1. Failover to read replica                                              │
│  2. Promote replica to primary                                            │
│  3. Create new replica                                                    │
│  RTO: 5 minutes                                                            │
│                                                                             │
│  SCENARIO 3: Point-in-Time Recovery                                        │
│  ───────────────────────────────────                                       │
│  1. Stop application writes                                               │
│  2. Create new instance from backup                                       │
│  3. Replay WAL to target time                                             │
│  4. Verify data integrity                                                 │
│  5. Switch DNS/connection string                                          │
│  RTO: 1-4 hours depending on data size                                    │
│                                                                             │
│  SCENARIO 4: Region Failure                                                │
│  ─────────────────────────────                                             │
│  1. DNS failover to secondary region                                      │
│  2. Promote cross-region replica                                          │
│  3. Update application configuration                                      │
│  RTO: 15 minutes                                                           │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. Performance Optimization

### 9.1 Query Optimization Techniques

| Technique | Use Case | Impact |
|-----------|----------|--------|
| Connection pooling | High concurrency | 10x connections |
| Read replicas | Read-heavy workload | 3x read throughput |
| Query caching | Repeated queries | 100x for cached |
| Batch inserts | Bulk operations | 50x insert speed |
| Continuous aggregates | Analytics queries | 1000x for aggregates |
| Partitioning | Large tables | 10x query speed |

### 9.2 Connection Pooling

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      CONNECTION POOLING (PgBouncer)                         │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  APPLICATION SERVERS                                                       │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                                 │
│  │App 1│ │App 2│ │App 3│ │App 4│ │App N│                                 │
│  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘                                 │
│     │       │       │       │       │                                      │
│     └───────┴───────┴───────┴───────┘                                      │
│                     │                                                       │
│                     ▼                                                       │
│     ┌─────────────────────────────────┐                                    │
│     │         PGBOUNCER               │                                    │
│     │                                 │                                    │
│     │  Mode: Transaction pooling      │                                    │
│     │  Max client conn: 10,000        │                                    │
│     │  Default pool size: 20          │                                    │
│     │  Max pool size: 100             │                                    │
│     └────────────────┬────────────────┘                                    │
│                      │                                                      │
│                      ▼                                                      │
│     ┌─────────────────────────────────┐                                    │
│     │         POSTGRESQL              │                                    │
│     │                                 │                                    │
│     │  max_connections: 200           │                                    │
│     │  (Reserved: 10 for admin)       │                                    │
│     └─────────────────────────────────┘                                    │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | System overview |
| [MICROSERVICES-DESIGN.md](./MICROSERVICES-DESIGN.md) | Service architecture |
| [API-SPECIFICATIONS.md](./API-SPECIFICATIONS.md) | API contracts |
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security design |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Engineering | Initial database schema design |

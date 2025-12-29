# Ephemeral PR Environments: The Complete 2025 Guide

> **Purpose**: This guide covers everything you need to deploy full-stack, isolated preview environments on every Pull Request — including databases, Redis, secrets, data seeding, MCP servers, and AI workloads.

---

## Table of Contents

1. [Why Ephemeral Environments?](#why-ephemeral-environments)
2. [Full-Stack Preview Platforms](#full-stack-preview-platforms)
3. [Database Branching & Cloning](#database-branching--cloning)
4. [Data Seeding & Anonymization](#data-seeding--anonymization)
5. [Secrets Management](#secrets-management)
6. [MCP Server Deployment](#mcp-server-deployment)
7. [AI/ML Environment Patterns](#aiml-environment-patterns)
8. [Config & Feature Flags](#config--feature-flags)
9. [Architecture Patterns](#architecture-patterns)
10. [The Recommended Stack](#the-recommended-stack)
11. [Implementation Playbook](#implementation-playbook)

---

## Why Ephemeral Environments?

### The Problem with Shared Staging

Traditional shared staging environments create bottlenecks:

- **Merge conflicts on data**: Multiple PRs testing against the same DB corrupt each other's state
- **Flaky tests**: One team's changes break another team's preview
- **Slow feedback loops**: Waiting for "staging to be free" kills velocity
- **Production drift**: Staging accumulates cruft that doesn't reflect prod

### The Ephemeral Solution

Ephemeral (preview) environments solve this by giving **every PR its own isolated stack**:

```
PR #123 → https://pr-123.preview.unitpay.dev
         ├── Frontend (Next.js)
         ├── API Server
         ├── Database (branched from prod)
         ├── Redis (isolated instance)
         ├── Background Workers (Trigger.dev)
         ├── MCP Servers (for AI features)
         └── Secrets (scoped to this env)
```

### Key Benefits

| Benefit | Impact |
|---------|--------|
| **Parallel development** | Unlimited PRs can test simultaneously |
| **Production-like data** | Branch from prod with anonymized PII |
| **Fast feedback** | Test changes in minutes, not hours |
| **Clean teardown** | PR closes → environment destroyed |
| **Cost efficiency** | Pay only for active previews |

---

## Full-Stack Preview Platforms

### Tier 1: Managed Platforms (Fastest Setup)

#### Vercel
- **Best for**: Frontend/fullstack Next.js, React, static sites
- **Preview deploys**: Automatic on every PR
- **Database**: Pairs with Neon for Postgres branching
- **Limitations**: Backend-only services need additional platform
- **Pricing**: Free tier generous, $20/user/month for teams

```yaml
# vercel.json - automatic preview config
{
  "git": {
    "deploymentEnabled": {
      "main": true,
      "previews": true
    }
  }
}
```

#### Railway
- **Best for**: Full-stack apps (frontend + backend + DB + Redis)
- **Key feature**: Spin up entire stack per PR including databases
- **DX**: Deploy via GitHub, CLI, or API
- **Pricing**: Usage-based, ~$5-20/month for preview envs

```bash
# Railway CLI - create preview environment
railway environment create pr-$PR_NUMBER
railway up --environment pr-$PR_NUMBER
```

#### Render
- **Best for**: Simple full-stack apps
- **Preview envs**: Automatic for all services in a Blueprint
- **Databases**: Managed Postgres with branching (newer feature)
- **Pricing**: Free tier, then usage-based

### Tier 2: Kubernetes-Native Platforms

#### Bunnyshell
- **Best for**: Teams wanting complete isolation without K8s expertise
- **Key features**:
  - Template-driven environment definitions
  - Database snapshots from production (anonymized)
  - Built-in secret management
  - Auto-teardown on PR merge
- **DX**: YAML-based config, excellent UI

```yaml
# bunnyshell.yaml
kind: Environment
name: preview-{{ PR_NUMBER }}
components:
  - name: api
    type: docker
    image: myapp/api:{{ COMMIT_SHA }}
  - name: database
    type: postgres
    snapshot: production  # Clone from prod
    anonymize: true
  - name: redis
    type: redis
lifecycle:
  ttl: 7d  # Auto-delete after 7 days
```

#### Qovery
- **Best for**: Developer velocity + resource optimization
- **Key features**:
  - Auto environment provisioning on code commits
  - Clone environments with one click
  - Cost optimization (scale down inactive envs)
- **Integrates with**: AWS, GCP, Azure, Scaleway

#### Northflank
- **Best for**: Enterprise teams needing secrets + DB cloning
- **Key features**:
  - Secret groups with environment scoping
  - Clone staging data in seconds
  - Spot/preemptible server support (90% cost savings)
  - Working hours auto-pause

#### Okteto
- **Best for**: Microservices teams already on Kubernetes
- **Key features**:
  - Per-branch K8s namespaces
  - Full namespace isolation
  - Requires your own K8s cluster
- **Philosophy**: "Kubernetes, but developer-friendly"

```yaml
# okteto.yaml
deploy:
  - helm upgrade --install api ./charts/api
  - helm upgrade --install worker ./charts/worker
  - kubectl apply -f k8s/preview-ingress.yaml
```

#### Atmosly
- **Best for**: Enterprise K8s with compliance needs
- **Key features**:
  - DB snapshots from prod with anonymization
  - Slack notifications on environment events
  - Per-preview observability

### Tier 3: Open Source / Self-Hosted

#### Uffizzi
- **Best for**: Teams wanting full control + OSS
- **Deployment**: Self-host on K8s or use their SaaS
- **GitHub Actions**: First-class integration
- **Key feature**: Full-stack previews including DBs

```yaml
# .github/workflows/preview.yml
- name: Deploy Preview
  uses: UffizziCloud/preview-action@v2
  with:
    compose-file: docker-compose.preview.yml
    server: https://app.uffizzi.com
```

#### Coolify
- **Best for**: Self-hosted Vercel alternative
- **Runs on**: Any VPS or bare metal
- **Features**: Preview deployments, databases, Redis

### Platform Comparison Matrix

| Platform | DB Branching | Redis | Secrets | K8s Required | Pricing Model |
|----------|-------------|-------|---------|--------------|---------------|
| Vercel | Via Neon | Via Upstash | Built-in | No | Per-seat |
| Railway | Native | Native | Built-in | No | Usage |
| Bunnyshell | Snapshots | Native | Built-in | Optional | Usage |
| Qovery | Native | Native | Built-in | BYOC | Usage |
| Northflank | Clone | Native | Groups | Optional | Usage |
| Okteto | External | External | K8s secrets | Yes | Per-seat |
| Uffizzi | External | Compose | External | Self-host | Free/Usage |

---

## Database Branching & Cloning

### The Database Problem

Preview environments need isolated databases, but:
- Full DB copies are slow and expensive
- Shared DBs cause test pollution
- Production data has PII concerns

### Solution: Copy-on-Write Branching

Modern databases use **copy-on-write** to create instant branches:

```
Production DB (500GB)
    │
    ├── PR-123 Branch (instant, ~0 storage until writes)
    ├── PR-124 Branch (instant, ~0 storage until writes)
    └── PR-125 Branch (instant, ~0 storage until writes)
```

### Neon (Postgres) — The Gold Standard

Neon pioneered database branching for Postgres:

```bash
# Create branch via API
curl -X POST "https://console.neon.tech/api/v2/projects/$PROJECT_ID/branches" \
  -H "Authorization: Bearer $NEON_API_KEY" \
  -d '{
    "branch": {
      "name": "pr-123",
      "parent_id": "br-main-abc123"
    }
  }'
```

**Key Features**:
- Instant branching (< 1 second for any size DB)
- Copy-on-write (pay only for changed data)
- Auto-suspend (scale to zero when idle)
- Point-in-time restore (branch from any moment)

**GitHub Actions Integration**:
```yaml
- name: Create Neon Branch
  uses: neondatabase/create-branch-action@v4
  with:
    project_id: ${{ secrets.NEON_PROJECT_ID }}
    branch_name: pr-${{ github.event.pull_request.number }}
    api_key: ${{ secrets.NEON_API_KEY }}
```

**Vercel Integration** (zero config):
```bash
# In Vercel project settings, connect Neon
# Branches auto-create on preview deploys
```

### PlanetScale (MySQL/Vitess)

```bash
# Create branch
pscale branch create mydb pr-123

# Deploy schema changes
pscale deploy-request create mydb pr-123
```

**Key Features**:
- Git-like branching for MySQL
- Non-blocking schema changes
- Deploy requests for review

### Supabase (Postgres + More)

```bash
# Supabase CLI branching (newer feature)
supabase branches create pr-123
```

**Key Features**:
- Postgres + Auth + Storage + Edge Functions
- Branching for all services
- Row-level security carries over

### Turso (SQLite at the Edge)

```bash
# Create database branch
turso db create myapp-pr-123 --from-db myapp-production
```

**Key Features**:
- LibSQL (SQLite fork)
- Edge-first (replicas worldwide)
- Embedded replicas in your app

### Database Branching Comparison

| Database | Engine | Branch Time | Storage Model | Best For |
|----------|--------|-------------|---------------|----------|
| Neon | Postgres | < 1s | Copy-on-write | General purpose |
| PlanetScale | MySQL (Vitess) | < 1s | Copy-on-write | MySQL shops |
| Supabase | Postgres | ~30s | Full copy | Full-stack apps |
| Turso | SQLite | < 1s | Copy-on-write | Edge/embedded |
| Xata | Postgres | < 1s | Copy-on-write | Serverless + search |

---

## Data Seeding & Anonymization

### The PII Problem

You want production-like data for realistic testing, but:
- Production data contains PII (emails, names, addresses)
- GDPR/HIPAA/SOC2 prohibit using real customer data
- Synthetic data often lacks realistic patterns

### Solution: Anonymize + Seed

```
Production DB
     │
     ▼
┌─────────────────┐
│  Anonymization  │  ← Transform PII while keeping structure
│  Layer          │
└─────────────────┘
     │
     ▼
Preview Branch (Safe to use)
```

### Neosync (Open Source, Recently Acquired)

> **Note**: Neosync was recently acquired. Check current status before adopting.

```yaml
# neosync job config
jobs:
  - name: anonymize-users
    source:
      connection: production-postgres
    destination:
      connection: preview-postgres
    mappings:
      - schema: public
        table: users
        columns:
          - name: email
            transformer: generate_email
          - name: first_name
            transformer: generate_first_name
          - name: ssn
            transformer: null  # Remove entirely
```

**Key Features**:
- PII detection + transformation
- Referential integrity preservation
- Subset large databases
- GDPR/HIPAA compliance helpers

### Snaplet Seed (Data Generation)

> **Note**: Snaplet (the company) ceased operations, but Seed lives on as an open tool.

```typescript
// seed.config.ts
import { defineConfig } from "@snaplet/seed";

export default defineConfig({
  select: ["public.*"],  // Which tables to seed
  introspect: {
    databaseUrl: process.env.DATABASE_URL,
  },
});
```

```typescript
// seed.ts - Generate realistic test data
import { createSeedClient } from "@snaplet/seed";

const seed = await createSeedClient();

// Create users with realistic data
await seed.users((x) => x(100, {
  email: ({ seed }) => `user-${seed}@example.com`,
  created_at: ({ seed }) => new Date(Date.now() - seed * 86400000),
}));

// Create related posts (respects foreign keys)
await seed.posts((x) => x(500));
```

### DIY Anonymization (Postgres)

For simple cases, write your own:

```sql
-- Create anonymized view
CREATE VIEW users_anonymized AS
SELECT 
  id,
  md5(email) || '@example.com' AS email,
  'User ' || id AS first_name,
  'Test' AS last_name,
  created_at,
  updated_at
FROM users;

-- Or update in place on branch
UPDATE users SET
  email = 'user-' || id || '@example.com',
  first_name = 'Test',
  last_name = 'User ' || id,
  phone = NULL,
  ssn = NULL;
```

### Data Seeding Strategies

| Strategy | Pros | Cons | Best For |
|----------|------|------|----------|
| **Anonymized prod copy** | Realistic patterns | Slow for large DBs | E2E testing |
| **Synthetic generation** | Fast, no PII risk | May miss edge cases | Unit/integration tests |
| **Hybrid** | Best of both | Complex setup | Production-like testing |
| **Minimal seed** | Fast, deterministic | Not realistic | CI speed |

---

## Secrets Management

### The Secrets Problem in Preview Envs

Each preview environment needs:
- Different database connection strings
- Scoped API keys (Stripe test mode, etc.)
- Environment-specific feature flags
- Isolated credentials (no cross-env leakage)

### Modern Secrets Management Tools

#### Infisical (Open Source, Recommended)

**Why Infisical**:
- Open source (MIT license)
- Self-hostable or managed cloud
- Modern UI (not Vault-level complexity)
- Dynamic secrets support

```bash
# CLI usage
infisical secrets set DATABASE_URL="postgres://..." --env=pr-123

# In app
infisical run --env=pr-123 -- npm start
```

```yaml
# GitHub Actions
- name: Inject Secrets
  uses: Infisical/secrets-action@v1
  with:
    environment: pr-${{ github.event.pull_request.number }}
```

**Key Features**:
- Secret versioning + rollback
- Secret scanning (prevent leaks)
- Kubernetes operator + CSI driver
- Dynamic secrets (Postgres, MySQL, etc.)

#### Doppler (Managed, Fastest Setup)

**Why Doppler**:
- Branch-based environment management
- Real-time sync across services
- Excellent CI/CD integrations

```bash
# CLI usage
doppler run --config pr-123 -- npm start

# Create environment
doppler configs create pr-123 --project unitpay
```

**Comparison with Infisical**:
| Feature | Infisical | Doppler |
|---------|-----------|---------|
| Self-host | ✅ Yes | ❌ No |
| Open source | ✅ MIT | ❌ Closed |
| Dynamic secrets | ✅ Yes | ⚠️ Beta |
| Pricing | Free tier + paid | Free tier + $3/user |
| DX | Great | Excellent |

#### HashiCorp Vault (Enterprise)

For large organizations with dedicated platform teams:

```hcl
# Dynamic database credentials
path "database/creds/preview-*" {
  capabilities = ["read"]
}
```

```bash
# Get ephemeral database credentials
vault read database/creds/preview-pr-123
# Returns: username=v-token-pr-123-xyz, password=abc123
# Credentials auto-expire after TTL
```

**When to use Vault**:
- You have a platform team
- Need dynamic secrets at scale
- Complex policy requirements
- Multi-cloud with unified secrets

#### External Secrets Operator (Kubernetes)

Bridge any secrets manager to K8s:

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
  namespace: preview-pr-123
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: app-secrets
  data:
    - secretKey: database-url
      remoteRef:
        key: preview/pr-123/database
        property: url
```

### Secrets Strategy for Preview Envs

```
┌─────────────────────────────────────────────────────────────┐
│                    SECRETS HIERARCHY                        │
├─────────────────────────────────────────────────────────────┤
│  Base Secrets (shared across all previews)                  │
│  ├── STRIPE_TEST_KEY (same for all)                         │
│  ├── SENTRY_DSN (same for all)                              │
│  └── ANALYTICS_ID (same for all)                            │
│                                                             │
│  Environment-Specific (generated per preview)               │
│  ├── DATABASE_URL (unique per branch)                       │
│  ├── REDIS_URL (unique per instance)                        │
│  └── JWT_SECRET (unique per env)                            │
│                                                             │
│  Dynamic Secrets (short-lived, auto-rotated)                │
│  ├── DB credentials via Vault/Infisical                     │
│  └── Cloud provider tokens                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## MCP Server Deployment

### What is MCP?

**Model Context Protocol (MCP)** is the emerging standard for LLM tool integration:
- Announced by Anthropic (Nov 2024)
- Adopted by OpenAI, Google DeepMind (2025)
- Standardizes how LLMs interact with external tools

### MCP in Preview Environments

Each preview environment may need its own MCP servers:

```
PR-123 Preview Environment
├── App (Next.js)
├── API Server
├── MCP Servers
│   ├── mcp-database (query this PR's DB)
│   ├── mcp-github (scoped to this branch)
│   └── mcp-tools (custom business logic)
└── Claude/GPT Client
```

### Deploying MCP Servers Per Preview

#### Option 1: Containerized MCP Servers

```dockerfile
# Dockerfile.mcp-server
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3001
CMD ["npx", "mcp-server", "--transport", "http", "--port", "3001"]
```

```yaml
# docker-compose.preview.yml
services:
  mcp-database:
    build:
      context: ./mcp-servers/database
    environment:
      DATABASE_URL: ${DATABASE_URL}
      MCP_AUTH_TOKEN: ${MCP_AUTH_TOKEN}
    ports:
      - "3001:3001"
  
  mcp-tools:
    build:
      context: ./mcp-servers/tools
    environment:
      API_BASE_URL: https://pr-${PR_NUMBER}.preview.app.com
```

#### Option 2: Cloudflare Workers (Edge MCP)

```typescript
// mcp-server.ts (Cloudflare Worker)
import { McpServer } from "@modelcontextprotocol/sdk";

export default {
  async fetch(request: Request, env: Env) {
    const server = new McpServer({
      name: "preview-tools",
      version: "1.0.0",
    });

    server.addTool({
      name: "get_user",
      description: "Fetch user from this preview's database",
      parameters: { userId: { type: "string" } },
      execute: async ({ userId }) => {
        const db = env.DB;  // D1 database binding
        return await db.prepare("SELECT * FROM users WHERE id = ?")
          .bind(userId)
          .first();
      },
    });

    return server.handleRequest(request);
  },
};
```

#### Option 3: Railway/Render Service

```yaml
# railway.toml
[service]
name = "mcp-server"

[deploy]
healthcheck = "/health"

[environments.pr-*]
# Auto-deployed for each PR
DATABASE_URL = "{{Postgres.DATABASE_URL}}"
```

### MCP Server Configuration Per Environment

```typescript
// mcp-config.ts
export const getMcpConfig = (environment: string) => ({
  servers: [
    {
      name: "database",
      transport: "http",
      url: `https://mcp-db.${environment}.preview.unitpay.dev`,
      auth: {
        type: "bearer",
        token: process.env.MCP_AUTH_TOKEN,
      },
    },
    {
      name: "github",
      transport: "http", 
      url: `https://mcp-github.${environment}.preview.unitpay.dev`,
    },
  ],
});
```

### MCP Security Considerations

```yaml
# Per-environment MCP isolation
security:
  # Each preview gets its own MCP auth token
  mcp_auth_token: ${MCP_AUTH_TOKEN_PR_123}
  
  # Scoped permissions per environment
  allowed_tools:
    - read_database
    - query_api
  blocked_tools:
    - delete_production
    - modify_billing
  
  # Rate limiting per preview
  rate_limit:
    requests_per_minute: 100
```

---

## AI/ML Environment Patterns

### Deploying AI Features in Preview Envs

Preview environments need special handling for AI workloads:

| Component | Strategy |
|-----------|----------|
| LLM API calls | Use test/sandbox keys |
| Vector DBs | Branch or fresh instance |
| Model artifacts | Shared across previews |
| GPU inference | Shared service or skip |

### Vector Database Branching

#### Pinecone

```python
# Create namespace per preview
index = pinecone.Index("main-index")
preview_namespace = f"pr-{pr_number}"

# Upsert to preview namespace
index.upsert(vectors=vectors, namespace=preview_namespace)

# Query from preview namespace
results = index.query(vector=query, namespace=preview_namespace)

# Cleanup on PR close
index.delete(delete_all=True, namespace=preview_namespace)
```

#### Qdrant

```python
# Create collection per preview (or use payload filtering)
client.create_collection(
    collection_name=f"embeddings-pr-{pr_number}",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
)
```

### AI API Key Management

```yaml
# Different API keys per environment type
environments:
  production:
    OPENAI_API_KEY: ${OPENAI_PROD_KEY}
    ANTHROPIC_API_KEY: ${ANTHROPIC_PROD_KEY}
  
  preview:
    # Use lower-tier keys for previews
    OPENAI_API_KEY: ${OPENAI_TEST_KEY}
    ANTHROPIC_API_KEY: ${ANTHROPIC_TEST_KEY}
    
    # Rate limit proxies
    AI_PROXY_URL: https://ai-proxy.internal/v1
```

### Modal (Serverless GPU)

```python
# modal_app.py
import modal

app = modal.App("preview-inference")

@app.function(gpu="A10G")
def run_inference(prompt: str, environment: str):
    # Each preview can call this
    model = load_model()
    return model.generate(prompt)
```

---

## Config & Feature Flags

### Environment-Specific Configuration

#### Pulumi ESC (Unified Config)

```yaml
# environments/base.yaml
values:
  app:
    name: unitpay
    log_level: info
  
  integrations:
    stripe:
      publishable_key: ${stripe.test.publishable}
    sentry:
      dsn: ${sentry.dsn}

# environments/preview.yaml
imports:
  - base

values:
  app:
    log_level: debug
    
  database:
    url: ${neon.preview.url}
    
  features:
    new_checkout: true
    beta_dashboard: true
```

```bash
# Inject into any command
pulumi env run preview-pr-123 -- npm start
```

### Feature Flags Per Preview

#### LaunchDarkly

```typescript
// Target specific preview environments
const flags = await ldClient.variation(
  "new-checkout-flow",
  {
    key: userId,
    custom: {
      environment: `pr-${prNumber}`,
      branch: branchName,
    },
  },
  false
);
```

#### ConfigCat

```typescript
// Environment-based targeting
const configCatClient = configcat.getClient(
  process.env.CONFIGCAT_SDK_KEY,
  PollingMode.AutoPoll,
  {
    defaultUser: {
      identifier: userId,
      custom: {
        environment: process.env.PREVIEW_ENV,
      },
    },
  }
);
```

### Environment Variables Strategy

```bash
# Base environment (all previews inherit)
BASE_URL=https://pr-${PR_NUMBER}.preview.unitpay.dev
NODE_ENV=preview
LOG_LEVEL=debug

# Computed at deploy time
DATABASE_URL=postgres://...  # From Neon branch
REDIS_URL=redis://...        # From Upstash
MCP_ENDPOINT=https://mcp.pr-${PR_NUMBER}.preview.unitpay.dev

# Shared across previews (use test keys)
STRIPE_SECRET_KEY=sk_test_...
OPENAI_API_KEY=sk-test-...
```

---

## Architecture Patterns

### Pattern 1: Vercel + Neon (Simplest)

```
┌─────────────────────────────────────────────────────────────┐
│                    VERCEL + NEON STACK                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  GitHub PR #123                                             │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────┐    auto-creates    ┌─────────────┐            │
│  │ Vercel  │ ────────────────── │ Neon Branch │            │
│  │ Preview │                    │  (Postgres) │            │
│  └─────────┘                    └─────────────┘            │
│       │                              │                      │
│       └──────── DATABASE_URL ────────┘                      │
│                                                             │
│  Teardown: Automatic on PR merge/close                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Setup time**: ~30 minutes
**Best for**: Next.js apps, simple full-stack

### Pattern 2: Railway Full-Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    RAILWAY FULL-STACK                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  GitHub PR #123                                             │
│       │                                                     │
│       ▼                                                     │
│  Railway Environment (pr-123)                               │
│  ┌────────────────────────────────────────────┐            │
│  │  ┌─────────┐  ┌──────────┐  ┌───────────┐ │            │
│  │  │ Next.js │  │ Express  │  │ Worker    │ │            │
│  │  │ (web)   │  │ (api)    │  │ (jobs)    │ │            │
│  │  └─────────┘  └──────────┘  └───────────┘ │            │
│  │       │            │             │        │            │
│  │       └────────────┴─────────────┘        │            │
│  │                    │                       │            │
│  │  ┌─────────────────┴───────────────────┐  │            │
│  │  │         Postgres + Redis            │  │            │
│  │  └─────────────────────────────────────┘  │            │
│  └────────────────────────────────────────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Setup time**: ~1 hour
**Best for**: Monorepo with multiple services

### Pattern 3: Kubernetes with Bunnyshell

```
┌─────────────────────────────────────────────────────────────┐
│                 BUNNYSHELL ON KUBERNETES                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  GitHub PR #123 ──▶ Bunnyshell Webhook                      │
│                          │                                  │
│                          ▼                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Kubernetes Namespace: preview-pr-123                   │ │
│  │                                                        │ │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐  │ │
│  │  │ Web Pod │ │ API Pod │ │ Worker  │ │ MCP Server  │  │ │
│  │  └────┬────┘ └────┬────┘ └────┬────┘ └──────┬──────┘  │ │
│  │       │           │           │              │         │ │
│  │  ┌────┴───────────┴───────────┴──────────────┴──────┐  │ │
│  │  │              Secrets (from Infisical)            │  │ │
│  │  └──────────────────────────────────────────────────┘  │ │
│  │                                                        │ │
│  │  ┌──────────────────┐  ┌────────────────────────────┐  │ │
│  │  │ Postgres (clone) │  │ Redis (ephemeral)          │  │ │
│  │  │ from prod        │  │                            │  │ │
│  │  └──────────────────┘  └────────────────────────────┘  │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  Ingress: pr-123.preview.unitpay.dev                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Setup time**: ~4 hours
**Best for**: Complex microservices, enterprise

### Pattern 4: Hybrid (Best of Both)

```
┌─────────────────────────────────────────────────────────────┐
│                      HYBRID PATTERN                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Vercel (Frontend)          Railway (Backend)               │
│  ┌───────────────┐          ┌────────────────────┐         │
│  │ Next.js App   │◀────────▶│ API + Workers      │         │
│  │ pr-123.vercel │          │ pr-123.railway     │         │
│  └───────────────┘          └────────────────────┘         │
│         │                           │                       │
│         │                           │                       │
│         ▼                           ▼                       │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                     Shared Services                    │ │
│  │  ┌──────────┐  ┌──────────┐  ┌────────────────────┐   │ │
│  │  │ Neon     │  │ Upstash  │  │ Trigger.dev        │   │ │
│  │  │ Postgres │  │ Redis    │  │ (background jobs)  │   │ │
│  │  └──────────┘  └──────────┘  └────────────────────┘   │ │
│  │        │             │                │                │ │
│  │        └─────────────┴────────────────┘                │ │
│  │                      │                                 │ │
│  │              ┌───────┴───────┐                         │ │
│  │              │   Infisical   │                         │ │
│  │              │   (secrets)   │                         │ │
│  │              └───────────────┘                         │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Setup time**: ~2 hours
**Best for**: Teams using best-of-breed tools

---

## The Recommended Stack

### For UnitPay OS Specifically

Given your TypeScript monorepo + CLI-based SDLC + AI features:

```
┌─────────────────────────────────────────────────────────────┐
│                 UNITPAY OS PREVIEW STACK                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LAYER              TOOL                 REASON             │
│  ──────────────────────────────────────────────────────────│
│                                                             │
│  Frontend           Vercel               Best Next.js DX    │
│                                                             │
│  Backend            Railway              Full isolation,    │
│                                          simple setup       │
│                                                             │
│  Database           Neon                 Instant branching, │
│                                          Vercel integration │
│                                                             │
│  Cache              Upstash Redis        Serverless, free   │
│                                          tier generous      │
│                                                             │
│  Secrets            Infisical            Open source,       │
│                     (or Doppler)         self-hostable      │
│                                                             │
│  Background Jobs    Trigger.dev          Preview env        │
│                                          support native     │
│                                                             │
│  MCP Servers        Containerized        Full isolation     │
│                     (Railway/Docker)     per preview        │
│                                                             │
│  Config             Pulumi ESC           Unified env vars   │
│                     (or Infisical)       across services    │
│                                                             │
│  Data Seeding       Custom script +      DIY since Snaplet  │
│                     Neon branches        is deprecated      │
│                                                             │
│  Feature Flags      ConfigCat            Simple, free tier  │
│                     (or code-based)                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Cost Estimate (Per Active Preview)

| Service | Est. Monthly Cost |
|---------|-------------------|
| Vercel | $0 (included in team plan) |
| Railway | $2-5/preview |
| Neon | $0 (branches free) |
| Upstash Redis | $0 (free tier) |
| Infisical | $0 (free tier) |
| Trigger.dev | $0 (free tier) |
| **Total** | **~$5/active preview** |

---

## Implementation Playbook

### Phase 1: Foundation (Day 1)

```bash
# 1. Set up Neon project with branching
neon projects create unitpay-preview

# 2. Connect to Vercel
vercel integrations add neon

# 3. Set up Infisical
infisical init
infisical secrets set STRIPE_TEST_KEY="sk_test_..."
```

### Phase 2: GitHub Actions Workflow (Day 2)

```yaml
# .github/workflows/preview.yml
name: Preview Environment

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  deploy-preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      # Create Neon branch
      - name: Create Database Branch
        uses: neondatabase/create-branch-action@v4
        id: neon
        with:
          project_id: ${{ secrets.NEON_PROJECT_ID }}
          branch_name: pr-${{ github.event.pull_request.number }}
          api_key: ${{ secrets.NEON_API_KEY }}
      
      # Seed database (optional)
      - name: Seed Database
        run: |
          npx prisma db seed
        env:
          DATABASE_URL: ${{ steps.neon.outputs.db_url }}
      
      # Create Infisical environment
      - name: Setup Secrets
        uses: Infisical/secrets-action@v1
        with:
          environment: pr-${{ github.event.pull_request.number }}
          domain: https://app.infisical.com
      
      # Deploy to Vercel (auto-configured)
      - name: Deploy Preview
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          github-comment: true
        env:
          DATABASE_URL: ${{ steps.neon.outputs.db_url }}
```

### Phase 3: Cleanup Workflow (Day 2)

```yaml
# .github/workflows/preview-cleanup.yml
name: Cleanup Preview

on:
  pull_request:
    types: [closed]

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      # Delete Neon branch
      - name: Delete Database Branch
        uses: neondatabase/delete-branch-action@v3
        with:
          project_id: ${{ secrets.NEON_PROJECT_ID }}
          branch: pr-${{ github.event.pull_request.number }}
          api_key: ${{ secrets.NEON_API_KEY }}
      
      # Clean up Infisical environment
      - name: Delete Secrets Environment
        run: |
          infisical environments delete pr-${{ github.event.pull_request.number }}
```

### Phase 4: MCP Server Integration (Day 3)

```typescript
// packages/mcp-server/src/index.ts
import { McpServer } from "@modelcontextprotocol/sdk";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

const server = new McpServer({
  name: "unitpay-tools",
  version: "1.0.0",
});

server.addTool({
  name: "get_invoice",
  description: "Fetch invoice by ID from this preview environment",
  parameters: {
    invoice_id: { type: "string", description: "Invoice UUID" },
  },
  execute: async ({ invoice_id }) => {
    const result = await pool.query(
      "SELECT * FROM invoices WHERE id = $1",
      [invoice_id]
    );
    return result.rows[0];
  },
});

server.addTool({
  name: "list_customers",
  description: "List customers with pagination",
  parameters: {
    limit: { type: "number", default: 10 },
    offset: { type: "number", default: 0 },
  },
  execute: async ({ limit, offset }) => {
    const result = await pool.query(
      "SELECT id, email, name FROM customers LIMIT $1 OFFSET $2",
      [limit, offset]
    );
    return result.rows;
  },
});

// Start server
server.listen({ port: 3001, transport: "http" });
```

### Phase 5: Data Anonymization Script (Day 4)

```typescript
// scripts/anonymize-preview.ts
import { Pool } from "pg";
import { faker } from "@faker-js/faker";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

async function anonymize() {
  // Anonymize users
  await pool.query(`
    UPDATE users SET
      email = 'user-' || id || '@preview.unitpay.dev',
      first_name = 'Test',
      last_name = 'User ' || id,
      phone = NULL,
      address = NULL
  `);

  // Anonymize customers
  await pool.query(`
    UPDATE customers SET
      email = 'customer-' || id || '@preview.unitpay.dev',
      company_name = 'Test Company ' || id,
      tax_id = NULL,
      billing_address = '123 Test St'
  `);

  // Clear sensitive logs
  await pool.query(`TRUNCATE audit_logs, payment_logs`);

  console.log("✅ Database anonymized for preview environment");
}

anonymize();
```

---

## Quick Reference

### Environment Variables Template

```bash
# .env.preview.template
# Auto-generated for PR preview environments

# Core
NODE_ENV=preview
PREVIEW_ENV=pr-${PR_NUMBER}
BASE_URL=https://pr-${PR_NUMBER}.preview.unitpay.dev

# Database (from Neon)
DATABASE_URL=${NEON_BRANCH_URL}

# Cache (from Upstash)
REDIS_URL=${UPSTASH_REDIS_URL}

# Auth (test mode)
NEXTAUTH_SECRET=${PREVIEW_AUTH_SECRET}
NEXTAUTH_URL=https://pr-${PR_NUMBER}.preview.unitpay.dev

# Payments (Stripe test mode)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_test_...

# AI (test/sandbox)
OPENAI_API_KEY=sk-test-...
ANTHROPIC_API_KEY=sk-ant-test-...

# MCP
MCP_SERVER_URL=https://mcp.pr-${PR_NUMBER}.preview.unitpay.dev
MCP_AUTH_TOKEN=${PREVIEW_MCP_TOKEN}

# Feature Flags
CONFIGCAT_SDK_KEY=${CONFIGCAT_DEV_KEY}
```

### CLI Commands Cheatsheet

```bash
# Neon
neon branches create --name pr-123
neon branches delete pr-123
neon branches list

# Infisical
infisical secrets --env=pr-123
infisical run --env=pr-123 -- npm start
infisical export --env=pr-123 > .env

# Railway
railway environment create pr-123
railway up --environment pr-123
railway environment delete pr-123

# Vercel
vercel --confirm  # Deploy preview
vercel env pull .env.local

# Trigger.dev
npx trigger.dev dev --env=pr-123
```

---

## Resources

### Official Docs
- [Neon Branching](https://neon.tech/docs/introduction/branching)
- [Vercel Preview Deployments](https://vercel.com/docs/deployments/preview-deployments)
- [Railway Environments](https://docs.railway.app/develop/environments)
- [Bunnyshell Documentation](https://documentation.bunnyshell.com/)
- [Infisical Docs](https://infisical.com/docs)
- [MCP Specification](https://modelcontextprotocol.io/)

### Tutorials
- [Neon + Vercel Integration](https://neon.tech/docs/guides/vercel)
- [Preview Environments with GitHub Actions](https://docs.github.com/en/actions/deployment/about-deployments/deploying-with-github-actions)
- [Trigger.dev Environment Isolation](https://trigger.dev/docs/documentation/concepts/environments)

---

*Last updated: December 2025*
*For UnitPay OS internal use*

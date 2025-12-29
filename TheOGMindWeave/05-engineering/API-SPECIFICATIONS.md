# MindWeave API Specifications

## Document Information
| Field | Value |
|-------|-------|
| Document ID | ENG-003 |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Owner | Engineering Team |
| Status | Draft |
| Classification | Internal |

---

## Executive Summary

This document defines MindWeave's API specifications, including REST endpoints, GraphQL schema, authentication mechanisms, and SDK design. Our APIs follow OpenAPI 3.0 standards with a focus on developer experience and enterprise integration requirements.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MINDWEAVE API ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      EXTERNAL CLIENTS                                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │   │
│  │  │   Web App   │  │    CLI      │  │    SDKs    │  │ Integrations│ │   │
│  │  │  (React)    │  │  (Node.js)  │  │(TS/Py/Go)  │  │  (Zapier)  │ │   │
│  │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └─────┬──────┘ │   │
│  └─────────┼────────────────┼────────────────┼───────────────┼────────┘   │
│            │                │                │               │             │
│            └────────────────┴────────────────┴───────────────┘             │
│                                    │                                        │
│                          ┌─────────▼─────────┐                             │
│                          │  api.mindweave.ai │                             │
│                          │                   │                             │
│                          │  • REST API (v1)  │                             │
│                          │  • GraphQL        │                             │
│                          │  • WebSocket      │                             │
│                          └─────────┬─────────┘                             │
│                                    │                                        │
│  ┌─────────────────────────────────▼───────────────────────────────────┐   │
│  │                         API GATEWAY                                  │   │
│  │  ┌─────────────────────────────────────────────────────────────────┐│   │
│  │  │  Rate Limiting │ Authentication │ Request Validation │ Routing  ││   │
│  │  └─────────────────────────────────────────────────────────────────┘│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. API Design Principles

### 1.1 Core Principles

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **RESTful** | Resource-oriented design | Proper HTTP methods, status codes |
| **Versioned** | Backward compatibility | URL versioning (v1, v2) |
| **Consistent** | Predictable patterns | Standardized naming, responses |
| **Documented** | Self-documenting | OpenAPI 3.0, interactive docs |
| **Secure** | Defense in depth | OAuth 2.0, API keys, rate limiting |
| **Performant** | Fast response times | Caching, pagination, compression |

### 1.2 URL Structure

```
┌────────────────────────────────────────────────────────────────────────────┐
│                          URL STRUCTURE                                      │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BASE URL: https://api.mindweave.ai/v1                                     │
│                                                                             │
│  PATTERN: /{resource}/{id}/{sub-resource}/{sub-id}                         │
│                                                                             │
│  EXAMPLES:                                                                 │
│  ─────────                                                                 │
│  GET    /organizations                     List orgs                       │
│  POST   /organizations                     Create org                      │
│  GET    /organizations/:org_id             Get org                         │
│  PATCH  /organizations/:org_id             Update org                      │
│  DELETE /organizations/:org_id             Delete org                      │
│                                                                             │
│  GET    /organizations/:org_id/projects    List org projects               │
│  POST   /organizations/:org_id/projects    Create project                  │
│                                                                             │
│  GET    /projects/:project_id/usage        Get project usage               │
│  GET    /projects/:project_id/mcp-servers  List MCP servers               │
│                                                                             │
│  QUERY PARAMETERS:                                                         │
│  ─────────────────                                                         │
│  ?page=1&per_page=20             Pagination                               │
│  ?sort=created_at&order=desc     Sorting                                  │
│  ?filter[status]=active          Filtering                                │
│  ?include=owner,members          Relationships                            │
│  ?fields=id,name,status          Sparse fieldsets                         │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Authentication & Authorization

### 2.1 Authentication Methods

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      AUTHENTICATION METHODS                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  METHOD 1: API KEY (Server-to-Server)                                      │
│  ──────────────────────────────────────                                    │
│                                                                             │
│  Authorization: Bearer mw_sk_live_abc123...                                │
│                                                                             │
│  Key Types:                                                                │
│  • mw_sk_live_  - Production secret key                                   │
│  • mw_sk_test_  - Test/sandbox key                                        │
│  • mw_pk_live_  - Public key (client-side)                                │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  METHOD 2: OAUTH 2.0 (User Authentication)                                 │
│  ──────────────────────────────────────────                                │
│                                                                             │
│  Flow: Authorization Code with PKCE                                        │
│                                                                             │
│  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐                  │
│  │  User  │────►│  App   │────►│ Auth   │────►│  API   │                  │
│  │        │     │        │     │ Server │     │        │                  │
│  └────────┘     └────────┘     └────────┘     └────────┘                  │
│       │              │              │              │                       │
│       │  1. Login    │              │              │                       │
│       │─────────────►│              │              │                       │
│       │              │  2. Auth URL │              │                       │
│       │              │─────────────►│              │                       │
│       │  3. Consent  │              │              │                       │
│       │◄─────────────│              │              │                       │
│       │              │  4. Code     │              │                       │
│       │              │◄─────────────│              │                       │
│       │              │  5. Exchange │              │                       │
│       │              │─────────────►│              │                       │
│       │              │  6. Tokens   │              │                       │
│       │              │◄─────────────│              │                       │
│       │              │  7. API Call │              │                       │
│       │              │──────────────────────────►│                       │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  METHOD 3: SSO/SAML (Enterprise)                                           │
│  ────────────────────────────────                                          │
│                                                                             │
│  • SAML 2.0 for enterprise IdP integration                                │
│  • Support for Okta, Azure AD, Google Workspace                           │
│  • SCIM provisioning for user sync                                        │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Authorization (RBAC)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      ROLE-BASED ACCESS CONTROL                              │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ROLES & PERMISSIONS:                                                      │
│  ─────────────────────                                                     │
│                                                                             │
│  Role         │ Scope        │ Permissions                                │
│  ─────────────┼──────────────┼────────────────────────────────────────    │
│  Owner        │ Organization │ Full access, delete org, manage billing   │
│  Admin        │ Organization │ Manage members, settings, all projects    │
│  Member       │ Organization │ Access assigned projects, read org data   │
│  Viewer       │ Organization │ Read-only access to assigned resources    │
│  ─────────────┼──────────────┼────────────────────────────────────────    │
│  Project Lead │ Project      │ Manage project settings, members          │
│  Developer    │ Project      │ Full access to project data               │
│  Analyst      │ Project      │ Read analytics, cannot modify config      │
│                                                                             │
│  PERMISSION MATRIX:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│                      Owner  Admin  Member  Viewer  Lead   Dev   Analyst   │
│  ───────────────────────────────────────────────────────────────────────  │
│  org:delete           ✓      ─      ─       ─      ─      ─      ─       │
│  org:manage_billing   ✓      ─      ─       ─      ─      ─      ─       │
│  org:manage_members   ✓      ✓      ─       ─      ─      ─      ─       │
│  org:manage_settings  ✓      ✓      ─       ─      ─      ─      ─       │
│  org:read             ✓      ✓      ✓       ✓      ─      ─      ─       │
│  project:create       ✓      ✓      ✓       ─      ─      ─      ─       │
│  project:delete       ✓      ✓      ─       ─      ✓      ─      ─       │
│  project:manage       ✓      ✓      ─       ─      ✓      ─      ─       │
│  project:read         ✓      ✓      ✓       ✓      ✓      ✓      ✓       │
│  usage:read           ✓      ✓      ✓       ✓      ✓      ✓      ✓       │
│  mcp:manage           ✓      ✓      ─       ─      ✓      ✓      ─       │
│  mcp:read             ✓      ✓      ✓       ✓      ✓      ✓      ✓       │
│  policies:manage      ✓      ✓      ─       ─      ✓      ─      ─       │
│  export:create        ✓      ✓      ✓       ─      ✓      ✓      ✓       │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. REST API Endpoints

### 3.1 Organizations API

```yaml
# OpenAPI 3.0 Specification (excerpt)
openapi: 3.0.3
info:
  title: MindWeave API
  version: 1.0.0
  description: Enterprise AI Governance Platform API

paths:
  /v1/organizations:
    get:
      summary: List organizations
      operationId: listOrganizations
      tags: [Organizations]
      security:
        - BearerAuth: []
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/PerPageParam'
      responses:
        '200':
          description: List of organizations
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Organization'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'
        '401':
          $ref: '#/components/responses/Unauthorized'

    post:
      summary: Create organization
      operationId: createOrganization
      tags: [Organizations]
      security:
        - BearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [name]
              properties:
                name:
                  type: string
                  minLength: 1
                  maxLength: 100
                  example: "Acme Corp"
                slug:
                  type: string
                  pattern: ^[a-z0-9-]+$
                  example: "acme-corp"
                settings:
                  $ref: '#/components/schemas/OrganizationSettings'
      responses:
        '201':
          description: Organization created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Organization'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'

  /v1/organizations/{org_id}:
    parameters:
      - name: org_id
        in: path
        required: true
        schema:
          type: string
          format: uuid

    get:
      summary: Get organization
      operationId: getOrganization
      tags: [Organizations]
      responses:
        '200':
          description: Organization details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Organization'
        '404':
          $ref: '#/components/responses/NotFound'

    patch:
      summary: Update organization
      operationId: updateOrganization
      tags: [Organizations]
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrganizationUpdate'
      responses:
        '200':
          description: Organization updated
        '404':
          $ref: '#/components/responses/NotFound'

    delete:
      summary: Delete organization
      operationId: deleteOrganization
      tags: [Organizations]
      responses:
        '204':
          description: Organization deleted
        '404':
          $ref: '#/components/responses/NotFound'
```

### 3.2 Usage Analytics API

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       USAGE ANALYTICS API                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  GET /v1/organizations/{org_id}/usage                                      │
│  ─────────────────────────────────────                                     │
│                                                                             │
│  Query Parameters:                                                         │
│  • start_date (required): ISO8601 date                                     │
│  • end_date (required): ISO8601 date                                       │
│  • granularity: hour | day | week | month (default: day)                  │
│  • group_by: model | user | project | mcp_server                          │
│  • metrics: tokens,cost,requests,latency (comma-separated)                │
│                                                                             │
│  Response:                                                                 │
│  {                                                                         │
│    "data": {                                                               │
│      "summary": {                                                          │
│        "total_tokens": 15420000,                                          │
│        "input_tokens": 10280000,                                          │
│        "output_tokens": 5140000,                                          │
│        "total_cost_usd": 462.60,                                          │
│        "total_requests": 8420,                                            │
│        "avg_latency_ms": 1234                                             │
│      },                                                                    │
│      "timeseries": [                                                       │
│        {                                                                   │
│          "timestamp": "2024-01-15T00:00:00Z",                             │
│          "tokens": 512000,                                                │
│          "cost_usd": 15.36,                                               │
│          "requests": 280                                                  │
│        },                                                                  │
│        ...                                                                 │
│      ],                                                                    │
│      "breakdown": {                                                        │
│        "by_model": [                                                       │
│          {"model": "claude-3-opus", "tokens": 5000000, "cost": 150.0},   │
│          {"model": "claude-3-sonnet", "tokens": 10000000, "cost": 150.0} │
│        ],                                                                  │
│        "by_user": [...],                                                   │
│        "by_project": [...]                                                 │
│      }                                                                     │
│    },                                                                      │
│    "meta": {                                                               │
│      "start_date": "2024-01-01T00:00:00Z",                                │
│      "end_date": "2024-01-31T23:59:59Z",                                  │
│      "granularity": "day"                                                 │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  GET /v1/organizations/{org_id}/usage/forecast                             │
│  ──────────────────────────────────────────────                            │
│                                                                             │
│  Query Parameters:                                                         │
│  • horizon: 7 | 14 | 30 | 90 (days, default: 30)                          │
│  • confidence: 0.80 | 0.90 | 0.95 (default: 0.90)                         │
│                                                                             │
│  Response:                                                                 │
│  {                                                                         │
│    "forecast": {                                                           │
│      "projected_cost_usd": 1850.00,                                       │
│      "projected_tokens": 61500000,                                        │
│      "confidence_interval": {                                             │
│        "lower": 1650.00,                                                  │
│        "upper": 2100.00                                                   │
│      },                                                                    │
│      "daily_projections": [...]                                           │
│    },                                                                      │
│    "budget_status": {                                                      │
│      "budget_usd": 2000.00,                                               │
│      "projected_spend_pct": 92.5,                                         │
│      "days_until_exceeded": null,                                         │
│      "recommendation": "On track to stay within budget"                   │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 MCP Registry API

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         MCP REGISTRY API                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LIST MCP SERVERS                                                          │
│  ─────────────────                                                         │
│  GET /v1/projects/{project_id}/mcp-servers                                 │
│                                                                             │
│  Query Parameters:                                                         │
│  • status: all | approved | pending | rejected                            │
│  • search: text search on name/description                                │
│  • sort: name | created_at | usage                                        │
│                                                                             │
│  Response:                                                                 │
│  {                                                                         │
│    "data": [                                                               │
│      {                                                                     │
│        "id": "mcp_123abc",                                                │
│        "name": "github-mcp-server",                                       │
│        "description": "GitHub integration for issue management",          │
│        "version": "1.2.0",                                                │
│        "status": "approved",                                              │
│        "transport": "stdio",                                              │
│        "tools_count": 12,                                                 │
│        "resources_count": 5,                                              │
│        "created_at": "2024-01-10T08:00:00Z",                             │
│        "approved_at": "2024-01-10T09:30:00Z",                            │
│        "approved_by": "user_456def",                                      │
│        "usage": {                                                         │
│          "total_calls": 15420,                                           │
│          "last_used": "2024-01-15T14:30:00Z"                             │
│        },                                                                  │
│        "policy": {                                                        │
│          "allowed_roles": ["admin", "developer"],                        │
│          "rate_limit": 100,                                              │
│          "requires_approval": false                                      │
│        }                                                                   │
│      }                                                                     │
│    ]                                                                       │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  REGISTER MCP SERVER                                                       │
│  ─────────────────────                                                     │
│  POST /v1/projects/{project_id}/mcp-servers                                │
│                                                                             │
│  Request Body:                                                             │
│  {                                                                         │
│    "name": "slack-mcp-server",                                            │
│    "description": "Slack workspace integration",                          │
│    "manifest_url": "https://example.com/mcp-manifest.json",               │
│    "transport": {                                                          │
│      "type": "stdio",                                                     │
│      "command": "npx",                                                    │
│      "args": ["-y", "@slack/mcp-server"]                                 │
│    },                                                                      │
│    "environment": {                                                        │
│      "SLACK_TOKEN": "${secrets.SLACK_TOKEN}"                              │
│    },                                                                      │
│    "policy": {                                                             │
│      "allowed_roles": ["admin"],                                          │
│      "requires_approval": true                                            │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  Response: 201 Created                                                     │
│  {                                                                         │
│    "id": "mcp_789ghi",                                                    │
│    "status": "pending",                                                   │
│    "security_scan": {                                                      │
│      "status": "in_progress",                                             │
│      "started_at": "2024-01-15T10:00:00Z"                                │
│    },                                                                      │
│    "approval_required": true,                                             │
│    "approval_url": "https://app.mindweave.ai/approvals/mcp_789ghi"       │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  GET MCP SERVER TOOLS                                                      │
│  ──────────────────────                                                    │
│  GET /v1/mcp-servers/{server_id}/tools                                     │
│                                                                             │
│  Response:                                                                 │
│  {                                                                         │
│    "data": [                                                               │
│      {                                                                     │
│        "name": "create_issue",                                            │
│        "description": "Create a new GitHub issue",                        │
│        "risk_level": "low",                                               │
│        "input_schema": {                                                   │
│          "type": "object",                                                │
│          "properties": {                                                   │
│            "title": {"type": "string"},                                   │
│            "body": {"type": "string"},                                    │
│            "labels": {"type": "array", "items": {"type": "string"}}     │
│          },                                                               │
│          "required": ["title"]                                            │
│        },                                                                  │
│        "usage_stats": {                                                    │
│          "total_calls": 542,                                             │
│          "success_rate": 98.5,                                           │
│          "avg_latency_ms": 850                                           │
│        }                                                                   │
│      }                                                                     │
│    ]                                                                       │
│  }                                                                         │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 3.4 Governance Policies API

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       GOVERNANCE POLICIES API                               │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LIST POLICIES                                                             │
│  ─────────────                                                             │
│  GET /v1/organizations/{org_id}/policies                                   │
│                                                                             │
│  Response:                                                                 │
│  {                                                                         │
│    "data": [                                                               │
│      {                                                                     │
│        "id": "pol_123",                                                   │
│        "name": "Daily Token Limit",                                       │
│        "type": "usage",                                                   │
│        "scope": "organization",                                           │
│        "status": "active",                                                │
│        "rules": {                                                          │
│          "max_tokens_per_day": 1000000,                                   │
│          "max_cost_per_day_usd": 100.00,                                  │
│          "action": "soft_limit"                                           │
│        },                                                                  │
│        "applies_to": {                                                     │
│          "users": ["all"],                                                │
│          "projects": ["all"],                                             │
│          "models": ["claude-3-opus"]                                      │
│        },                                                                  │
│        "notifications": {                                                  │
│          "at_80_percent": true,                                           │
│          "at_100_percent": true,                                          │
│          "channels": ["email", "slack"]                                   │
│        }                                                                   │
│      },                                                                    │
│      {                                                                     │
│        "id": "pol_456",                                                   │
│        "name": "MCP Tool Restrictions",                                   │
│        "type": "access",                                                  │
│        "scope": "project",                                                │
│        "status": "active",                                                │
│        "rules": {                                                          │
│          "mcp_servers": {                                                 │
│            "github-mcp": {                                                │
│              "allowed_tools": ["read_file", "list_issues"],              │
│              "blocked_tools": ["delete_repo", "admin_*"]                 │
│            }                                                              │
│          }                                                                 │
│        }                                                                   │
│      }                                                                     │
│    ]                                                                       │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  CREATE POLICY                                                             │
│  ─────────────                                                             │
│  POST /v1/organizations/{org_id}/policies                                  │
│                                                                             │
│  Request Body:                                                             │
│  {                                                                         │
│    "name": "Production Project Limits",                                   │
│    "type": "usage",                                                       │
│    "rules": {                                                              │
│      "max_tokens_per_hour": 500000,                                       │
│      "max_concurrent_requests": 50,                                       │
│      "allowed_models": ["claude-3-sonnet", "claude-3-haiku"],            │
│      "action": "hard_limit"                                               │
│    },                                                                      │
│    "applies_to": {                                                         │
│      "projects": ["proj_production"]                                      │
│    },                                                                      │
│    "notifications": {                                                      │
│      "at_80_percent": true,                                               │
│      "channels": ["slack:engineering-alerts"]                             │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  EVALUATE POLICY (Internal)                                                │
│  ──────────────────────────                                                │
│  POST /v1/governance/evaluate                                              │
│                                                                             │
│  Request:                                                                  │
│  {                                                                         │
│    "context": {                                                            │
│      "org_id": "org_123",                                                 │
│      "project_id": "proj_456",                                            │
│      "user_id": "user_789",                                               │
│      "action": "api_call",                                                │
│      "resource": {                                                         │
│        "model": "claude-3-opus",                                          │
│        "estimated_tokens": 5000                                           │
│      }                                                                     │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  Response:                                                                 │
│  {                                                                         │
│    "allowed": true,                                                       │
│    "policies_evaluated": ["pol_123", "pol_456"],                          │
│    "warnings": [                                                           │
│      {"policy": "pol_123", "message": "85% of daily limit reached"}      │
│    ],                                                                      │
│    "quotas": {                                                             │
│      "tokens_remaining": 150000,                                          │
│      "cost_remaining_usd": 15.00                                          │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. GraphQL API

### 4.1 Schema Overview

```graphql
# MindWeave GraphQL Schema

type Query {
  # Organizations
  organization(id: ID!): Organization
  organizations(first: Int, after: String): OrganizationConnection!

  # Projects
  project(id: ID!): Project
  projects(orgId: ID!, first: Int, after: String): ProjectConnection!

  # Usage Analytics
  usage(
    orgId: ID!
    startDate: DateTime!
    endDate: DateTime!
    granularity: Granularity = DAY
    groupBy: [GroupBy!]
  ): UsageData!

  # MCP Registry
  mcpServers(projectId: ID!, status: MCPStatus): [MCPServer!]!
  mcpServer(id: ID!): MCPServer

  # Current User
  me: User!
}

type Mutation {
  # Organizations
  createOrganization(input: CreateOrganizationInput!): Organization!
  updateOrganization(id: ID!, input: UpdateOrganizationInput!): Organization!
  deleteOrganization(id: ID!): Boolean!

  # Projects
  createProject(input: CreateProjectInput!): Project!
  updateProject(id: ID!, input: UpdateProjectInput!): Project!

  # MCP Registry
  registerMCPServer(input: RegisterMCPServerInput!): MCPServer!
  approveMCPServer(id: ID!): MCPServer!
  rejectMCPServer(id: ID!, reason: String): MCPServer!

  # Policies
  createPolicy(input: CreatePolicyInput!): Policy!
  updatePolicy(id: ID!, input: UpdatePolicyInput!): Policy!
  deletePolicy(id: ID!): Boolean!
}

type Subscription {
  # Real-time usage updates
  usageUpdated(projectId: ID!): UsageEvent!

  # Alert notifications
  alertTriggered(orgId: ID!): Alert!

  # MCP server status changes
  mcpServerStatusChanged(projectId: ID!): MCPServer!
}

# Types
type Organization {
  id: ID!
  name: String!
  slug: String!
  createdAt: DateTime!
  updatedAt: DateTime!

  # Relationships
  owner: User!
  members(first: Int, after: String): MemberConnection!
  projects(first: Int, after: String): ProjectConnection!
  subscription: Subscription

  # Computed
  usage(startDate: DateTime!, endDate: DateTime!): UsageSummary!
  memberCount: Int!
  projectCount: Int!
}

type Project {
  id: ID!
  name: String!
  slug: String!
  status: ProjectStatus!
  createdAt: DateTime!

  # Relationships
  organization: Organization!
  apiKeys: [APIKey!]!
  mcpServers: [MCPServer!]!
  policies: [Policy!]!

  # Usage
  usage(startDate: DateTime!, endDate: DateTime!): UsageSummary!
  realtimeUsage: RealtimeUsage!
}

type MCPServer {
  id: ID!
  name: String!
  description: String
  version: String!
  status: MCPStatus!
  transport: MCPTransport!

  # Tools and resources
  tools: [MCPTool!]!
  resources: [MCPResource!]!

  # Security
  securityScan: SecurityScan
  approvedBy: User
  approvedAt: DateTime

  # Usage
  usageStats: MCPUsageStats!
}

type UsageData {
  summary: UsageSummary!
  timeseries: [UsageDataPoint!]!
  breakdown: UsageBreakdown!
}

type UsageSummary {
  totalTokens: Int!
  inputTokens: Int!
  outputTokens: Int!
  totalCostUsd: Float!
  totalRequests: Int!
  avgLatencyMs: Float!
}

# Enums
enum Granularity {
  HOUR
  DAY
  WEEK
  MONTH
}

enum GroupBy {
  MODEL
  USER
  PROJECT
  MCP_SERVER
}

enum MCPStatus {
  PENDING
  APPROVED
  REJECTED
  DEPRECATED
}
```

### 4.2 GraphQL Query Examples

```graphql
# Dashboard Query - Get all data in one request
query DashboardData($orgId: ID!, $startDate: DateTime!, $endDate: DateTime!) {
  organization(id: $orgId) {
    name
    memberCount
    projectCount

    usage(startDate: $startDate, endDate: $endDate) {
      totalTokens
      totalCostUsd
      totalRequests
    }

    projects(first: 5) {
      edges {
        node {
          id
          name
          realtimeUsage {
            tokensToday
            costToday
          }
          mcpServers {
            id
            name
            status
          }
        }
      }
    }
  }
}

# MCP Server Detail Query
query MCPServerDetail($serverId: ID!) {
  mcpServer(id: $serverId) {
    id
    name
    description
    version
    status

    tools {
      name
      description
      riskLevel
      usageStats {
        totalCalls
        successRate
        avgLatencyMs
      }
    }

    securityScan {
      status
      findings {
        severity
        message
      }
      completedAt
    }

    approvedBy {
      name
      email
    }
    approvedAt
  }
}

# Real-time Usage Subscription
subscription UsageUpdates($projectId: ID!) {
  usageUpdated(projectId: $projectId) {
    timestamp
    tokenCount
    costUsd
    model
    user {
      name
    }
  }
}
```

---

## 5. WebSocket API

### 5.1 Real-time Events

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        WEBSOCKET API                                        │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CONNECTION:                                                               │
│  wss://api.mindweave.ai/v1/ws                                             │
│                                                                             │
│  Authentication: ?token=<jwt_token>                                        │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  SUBSCRIBE TO CHANNELS:                                                    │
│  ─────────────────────                                                     │
│                                                                             │
│  // Subscribe to organization events                                       │
│  {                                                                         │
│    "type": "subscribe",                                                   │
│    "channel": "org:org_123:usage"                                         │
│  }                                                                         │
│                                                                             │
│  // Subscribe to project events                                            │
│  {                                                                         │
│    "type": "subscribe",                                                   │
│    "channel": "project:proj_456:events"                                   │
│  }                                                                         │
│                                                                             │
│  // Subscribe to alerts                                                    │
│  {                                                                         │
│    "type": "subscribe",                                                   │
│    "channel": "org:org_123:alerts"                                        │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  EVENT TYPES:                                                              │
│  ────────────                                                              │
│                                                                             │
│  // Usage update event                                                     │
│  {                                                                         │
│    "type": "usage.update",                                                │
│    "channel": "project:proj_456:events",                                  │
│    "timestamp": "2024-01-15T10:30:00Z",                                   │
│    "data": {                                                               │
│      "tokens": 1500,                                                      │
│      "cost_usd": 0.045,                                                   │
│      "model": "claude-3-opus",                                            │
│      "user_id": "user_789",                                               │
│      "cumulative": {                                                       │
│        "tokens_today": 150000,                                            │
│        "cost_today_usd": 4.50                                             │
│      }                                                                     │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  // Alert triggered event                                                  │
│  {                                                                         │
│    "type": "alert.triggered",                                             │
│    "channel": "org:org_123:alerts",                                       │
│    "timestamp": "2024-01-15T10:30:00Z",                                   │
│    "data": {                                                               │
│      "alert_id": "alert_abc",                                             │
│      "severity": "warning",                                               │
│      "title": "Usage threshold reached",                                  │
│      "message": "Project 'Production' has reached 80% of daily limit",   │
│      "project_id": "proj_456"                                             │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  // MCP server status change                                               │
│  {                                                                         │
│    "type": "mcp.status_changed",                                          │
│    "channel": "project:proj_456:events",                                  │
│    "timestamp": "2024-01-15T10:30:00Z",                                   │
│    "data": {                                                               │
│      "server_id": "mcp_123",                                              │
│      "server_name": "github-mcp-server",                                  │
│      "old_status": "pending",                                             │
│      "new_status": "approved",                                            │
│      "approved_by": "user_789"                                            │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  HEARTBEAT:                                                                │
│  ──────────                                                                │
│  Server sends ping every 30 seconds                                       │
│  Client must respond with pong within 10 seconds                          │
│                                                                             │
│  // Ping from server                                                       │
│  { "type": "ping", "timestamp": "2024-01-15T10:30:00Z" }                  │
│                                                                             │
│  // Pong from client                                                       │
│  { "type": "pong" }                                                       │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. SDK Design

### 6.1 TypeScript/JavaScript SDK

```typescript
// MindWeave TypeScript SDK

import { MindWeave } from '@mindweave/sdk';

// Initialize client
const mindweave = new MindWeave({
  apiKey: 'mw_sk_live_...',
  baseUrl: 'https://api.mindweave.ai/v1', // optional
});

// Organizations
const org = await mindweave.organizations.get('org_123');
const orgs = await mindweave.organizations.list({ page: 1, perPage: 20 });

// Usage Analytics
const usage = await mindweave.usage.get({
  orgId: 'org_123',
  startDate: '2024-01-01',
  endDate: '2024-01-31',
  granularity: 'day',
  groupBy: ['model', 'user'],
});

// MCP Registry
const servers = await mindweave.mcp.list({
  projectId: 'proj_456',
  status: 'approved',
});

const newServer = await mindweave.mcp.register({
  projectId: 'proj_456',
  name: 'slack-mcp-server',
  transport: {
    type: 'stdio',
    command: 'npx',
    args: ['-y', '@slack/mcp-server'],
  },
});

// Policies
const policy = await mindweave.policies.create({
  orgId: 'org_123',
  name: 'Daily Limit',
  type: 'usage',
  rules: {
    maxTokensPerDay: 1000000,
    action: 'soft_limit',
  },
});

// Real-time subscriptions
const subscription = mindweave.subscribe({
  channels: ['org:org_123:usage', 'org:org_123:alerts'],
  onMessage: (event) => {
    console.log('Event:', event.type, event.data);
  },
  onError: (error) => {
    console.error('Error:', error);
  },
});

// Cleanup
subscription.unsubscribe();
```

### 6.2 Python SDK

```python
# MindWeave Python SDK

from mindweave import MindWeave
from mindweave.types import Granularity, GroupBy

# Initialize client
client = MindWeave(api_key="mw_sk_live_...")

# Organizations
org = client.organizations.get("org_123")
orgs = client.organizations.list(page=1, per_page=20)

# Usage Analytics
usage = client.usage.get(
    org_id="org_123",
    start_date="2024-01-01",
    end_date="2024-01-31",
    granularity=Granularity.DAY,
    group_by=[GroupBy.MODEL, GroupBy.USER],
)

print(f"Total cost: ${usage.summary.total_cost_usd:.2f}")
print(f"Total tokens: {usage.summary.total_tokens:,}")

# MCP Registry
servers = client.mcp.list(
    project_id="proj_456",
    status="approved",
)

for server in servers:
    print(f"{server.name}: {len(server.tools)} tools")

# Async support
import asyncio
from mindweave import AsyncMindWeave

async def main():
    async with AsyncMindWeave(api_key="mw_sk_live_...") as client:
        usage = await client.usage.get(
            org_id="org_123",
            start_date="2024-01-01",
            end_date="2024-01-31",
        )
        print(usage.summary.total_cost_usd)

asyncio.run(main())
```

### 6.3 Go SDK

```go
// MindWeave Go SDK

package main

import (
    "context"
    "fmt"
    "github.com/mindweave/mindweave-go"
)

func main() {
    // Initialize client
    client := mindweave.NewClient("mw_sk_live_...")

    ctx := context.Background()

    // Get organization
    org, err := client.Organizations.Get(ctx, "org_123")
    if err != nil {
        panic(err)
    }
    fmt.Printf("Organization: %s\n", org.Name)

    // Get usage analytics
    usage, err := client.Usage.Get(ctx, &mindweave.UsageParams{
        OrgID:       "org_123",
        StartDate:   "2024-01-01",
        EndDate:     "2024-01-31",
        Granularity: mindweave.GranularityDay,
        GroupBy:     []mindweave.GroupBy{mindweave.GroupByModel},
    })
    if err != nil {
        panic(err)
    }
    fmt.Printf("Total cost: $%.2f\n", usage.Summary.TotalCostUSD)

    // List MCP servers
    servers, err := client.MCP.List(ctx, &mindweave.MCPListParams{
        ProjectID: "proj_456",
        Status:    mindweave.MCPStatusApproved,
    })
    if err != nil {
        panic(err)
    }
    for _, server := range servers {
        fmt.Printf("Server: %s (%d tools)\n", server.Name, len(server.Tools))
    }
}
```

---

## 7. Error Handling

### 7.1 Error Response Format

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        ERROR RESPONSE FORMAT                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STANDARD ERROR RESPONSE:                                                  │
│  {                                                                         │
│    "error": {                                                              │
│      "code": "validation_error",                                          │
│      "message": "Invalid request parameters",                             │
│      "details": [                                                          │
│        {                                                                   │
│          "field": "email",                                                │
│          "message": "Must be a valid email address",                      │
│          "code": "invalid_format"                                         │
│        }                                                                   │
│      ],                                                                    │
│      "request_id": "req_abc123",                                          │
│      "documentation_url": "https://docs.mindweave.ai/errors/validation"  │
│    }                                                                       │
│  }                                                                         │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  ERROR CODES:                                                              │
│  ────────────                                                              │
│                                                                             │
│  HTTP  Code                    Description                                 │
│  ────  ────                    ───────────                                 │
│  400   validation_error        Request validation failed                   │
│  400   invalid_request         Malformed request body                     │
│  401   unauthorized            Missing or invalid authentication          │
│  401   token_expired           JWT token has expired                       │
│  403   forbidden               Insufficient permissions                    │
│  403   quota_exceeded          Usage quota exceeded                        │
│  404   not_found               Resource not found                          │
│  409   conflict                Resource conflict (duplicate)               │
│  422   unprocessable_entity    Semantic validation failed                 │
│  429   rate_limited            Too many requests                           │
│  500   internal_error          Server error                                │
│  503   service_unavailable     Service temporarily unavailable            │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  RATE LIMIT HEADERS:                                                       │
│  ───────────────────                                                       │
│                                                                             │
│  X-RateLimit-Limit: 1000          # Requests per window                   │
│  X-RateLimit-Remaining: 985       # Remaining in window                   │
│  X-RateLimit-Reset: 1705312800    # Window reset timestamp                │
│  Retry-After: 60                  # Seconds until retry (on 429)          │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 HTTP Status Code Usage

| Status Code | Usage |
|-------------|-------|
| 200 OK | Successful GET, PATCH |
| 201 Created | Successful POST creating resource |
| 204 No Content | Successful DELETE |
| 400 Bad Request | Malformed request, validation error |
| 401 Unauthorized | Missing or invalid authentication |
| 403 Forbidden | Valid auth but insufficient permissions |
| 404 Not Found | Resource doesn't exist |
| 409 Conflict | Duplicate resource, concurrent modification |
| 422 Unprocessable | Semantic validation error |
| 429 Too Many Requests | Rate limit exceeded |
| 500 Internal Error | Server error |
| 503 Service Unavailable | Maintenance, overload |

---

## 8. Rate Limiting

### 8.1 Rate Limit Tiers

| Tier | Requests/min | Burst | Applies To |
|------|-------------|-------|------------|
| Free | 60 | 10 | Free tier accounts |
| Team | 600 | 100 | Team tier accounts |
| Pro | 2,000 | 500 | Pro tier accounts |
| Enterprise | 10,000 | 2,000 | Enterprise accounts |

### 8.2 Rate Limit Strategy

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      RATE LIMITING STRATEGY                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ALGORITHM: Token Bucket with Sliding Window                               │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │   Request                                                           │   │
│  │      │                                                               │   │
│  │      ▼                                                               │   │
│  │  ┌──────────────────┐                                               │   │
│  │  │  Check Bucket    │                                               │   │
│  │  └────────┬─────────┘                                               │   │
│  │           │                                                          │   │
│  │     ┌─────┴─────┐                                                   │   │
│  │     │           │                                                   │   │
│  │     ▼           ▼                                                   │   │
│  │  Tokens      No Tokens                                              │   │
│  │  Available   Available                                              │   │
│  │     │           │                                                   │   │
│  │     ▼           ▼                                                   │   │
│  │  Process    Return 429                                              │   │
│  │  Request    + Retry-After                                           │   │
│  │     │                                                                │   │
│  │     ▼                                                               │   │
│  │  Consume Token                                                      │   │
│  │  Update Headers                                                     │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  SCOPES:                                                                   │
│  • Per API Key                                                             │
│  • Per User (within org)                                                  │
│  • Per Endpoint (separate limits for heavy endpoints)                     │
│                                                                             │
│  SPECIAL LIMITS:                                                           │
│  • Analytics export: 10/hour                                              │
│  • Bulk operations: 100/hour                                              │
│  • MCP registration: 20/hour                                              │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. API Versioning

### 9.1 Versioning Strategy

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       API VERSIONING STRATEGY                               │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  APPROACH: URL Path Versioning                                             │
│  ───────────────────────────────                                           │
│                                                                             │
│  Current:  https://api.mindweave.ai/v1/...                                │
│  Future:   https://api.mindweave.ai/v2/...                                │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  VERSION LIFECYCLE:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│     Active        Deprecated      Sunset         Removed                   │
│        │              │             │               │                      │
│        │  +12 months  │  +6 months  │               │                      │
│        │─────────────►│────────────►│──────────────►│                      │
│        │              │             │               │                      │
│                                                                             │
│  Active: Full support, all features                                       │
│  Deprecated: Security fixes only, migration warnings                      │
│  Sunset: Read-only, heavy migration warnings                              │
│  Removed: 404 with migration information                                  │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  DEPRECATION HEADERS:                                                      │
│  ────────────────────                                                      │
│                                                                             │
│  Deprecation: Sun, 15 Jan 2025 00:00:00 GMT                               │
│  Sunset: Sun, 15 Jul 2025 00:00:00 GMT                                    │
│  Link: <https://docs.mindweave.ai/migration/v1-v2>; rel="successor"       │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  BREAKING CHANGES (require new version):                                   │
│  • Removing endpoints                                                      │
│  • Removing required fields                                               │
│  • Changing response structure                                            │
│  • Changing authentication                                                │
│                                                                             │
│  NON-BREAKING CHANGES (same version):                                      │
│  • Adding new endpoints                                                   │
│  • Adding optional fields                                                 │
│  • Adding new values to enums                                             │
│  • Relaxing validation                                                    │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 10. API Documentation

### 10.1 Documentation Strategy

| Format | Purpose | Tool |
|--------|---------|------|
| OpenAPI 3.0 | Machine-readable spec | Swagger/Redocly |
| Interactive Docs | Try-it-out experience | Redocly |
| SDK Docs | Language-specific guides | TypeDoc/Sphinx |
| Tutorials | Getting started | Docusaurus |
| Changelog | Version history | GitHub Releases |

### 10.2 Documentation Structure

```
docs.mindweave.ai/
├── Getting Started/
│   ├── Quick Start
│   ├── Authentication
│   └── Making Your First Request
├── API Reference/
│   ├── Organizations
│   ├── Projects
│   ├── Usage Analytics
│   ├── MCP Registry
│   ├── Policies
│   └── Webhooks
├── SDKs/
│   ├── TypeScript/JavaScript
│   ├── Python
│   └── Go
├── Guides/
│   ├── Cost Management
│   ├── MCP Governance
│   ├── Policy Configuration
│   └── Real-time Analytics
├── Webhooks/
│   ├── Event Types
│   └── Verification
└── Changelog/
    └── API Versions
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | System design |
| [MICROSERVICES-DESIGN.md](./MICROSERVICES-DESIGN.md) | Service architecture |
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security design |
| [DATABASE-SCHEMA.md](./DATABASE-SCHEMA.md) | Data models |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Engineering | Initial API specifications |

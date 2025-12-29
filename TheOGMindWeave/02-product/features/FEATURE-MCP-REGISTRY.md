# Feature Specification: MCP Registry

> Complete specification for the Global MCP Registry feature

---

## Overview

### Feature Summary

| Field | Value |
|-------|-------|
| **Feature Name** | MCP Registry |
| **Priority** | P0 (MVP) |
| **Target Version** | v0.1 (MVP) |
| **Effort Estimate** | 4 weeks |
| **Owner** | Engineering |

### Description

The MCP Registry is a centralized inventory of all Model Context Protocol integrations across the organization. It enables discovery, prevents duplicate development, and provides visibility into the organization's AI integration landscape.

### Problem Statement

Enterprises building with Claude and MCP face critical challenges:
- Teams build duplicate MCPs without knowing others exist
- No central inventory of AI integrations
- No way to discover reusable components
- Security has no visibility into what systems AI can access

### Success Metrics

| Metric | Target |
|--------|--------|
| MCP Discovery Rate | 80% of teams check before building |
| Duplicate Prevention | 50% reduction in duplicate MCPs |
| Registry Completeness | 95% of MCPs registered |
| User Satisfaction | 4.3/5 star rating |

---

## User Experience

### Entry Points

1. **Main Navigation:** "MCPs" in left sidebar
2. **Search Bar:** Global search includes MCPs
3. **Team Page:** "MCPs" tab on team detail
4. **Quick Add:** "Register MCP" button in header

### Primary Screen: MCP Registry

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← MCP Registry                    + Register MCP    🔍 Search MCPs    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Organization MCPs: 147 total                                     │  │
│  │                                                                   │  │
│  │  Filter: [All Categories ▼] [All Teams ▼] [All Status ▼]        │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  By Category                                                      │  │
│  │                                                                   │  │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │  │
│  │  │    CRM      │ │  FINANCE    │ │    CODE     │ │    DATA     │ │  │
│  │  │             │ │             │ │             │ │             │ │  │
│  │  │   23 MCPs   │ │   18 MCPs   │ │   34 MCPs   │ │   28 MCPs   │ │  │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ │  │
│  │                                                                   │  │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │  │
│  │  │    COMMS    │ │   CUSTOM    │ │   OTHER     │                 │  │
│  │  │             │ │             │ │             │                 │  │
│  │  │   19 MCPs   │ │   25 MCPs   │ │   0 MCPs    │                 │  │
│  │  └─────────────┘ └─────────────┘ └─────────────┘                 │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Most Used MCPs                                        View All → │  │
│  │                                                                   │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │ 🔷 Salesforce CRM Reader                     34 teams      │  │  │
│  │  │    Read and query Salesforce objects                       │  │  │
│  │  │    Owner: Sales Ops  │  Status: ✅ Approved                │  │  │
│  │  └────────────────────────────────────────────────────────────┘  │  │
│  │                                                                   │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │ 🔷 GitHub PR Analyzer                        28 teams      │  │  │
│  │  │    Analyze pull requests and code changes                  │  │  │
│  │  │    Owner: Platform  │  Status: ✅ Approved                 │  │  │
│  │  └────────────────────────────────────────────────────────────┘  │  │
│  │                                                                   │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │ 🔷 Slack Message Poster                      22 teams      │  │  │
│  │  │    Post messages to Slack channels                         │  │  │
│  │  │    Owner: IT  │  Status: ✅ Approved                       │  │  │
│  │  └────────────────────────────────────────────────────────────┘  │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Recently Added                                        View All → │  │
│  │                                                                   │  │
│  │  🆕 Linear Issue Creator (Backend Team) - 2 hours ago            │  │
│  │  🆕 Stripe Payment Lookup (Finance) - 1 day ago                  │  │
│  │  🆕 Notion Page Updater (Product) - 3 days ago                   │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### MCP Detail Page

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← Back to Registry                                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                                                                   │  │
│  │  🔷 Salesforce CRM Reader                                        │  │
│  │                                                                   │  │
│  │  Status: ✅ Approved    Category: CRM    Version: 2.1.0          │  │
│  │                                                                   │  │
│  │  ────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  DESCRIPTION                                                      │  │
│  │  Read and query Salesforce CRM objects including Accounts,       │  │
│  │  Contacts, Opportunities, and custom objects. Supports SOQL      │  │
│  │  queries and record lookups by ID.                               │  │
│  │                                                                   │  │
│  │  ────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  CAPABILITIES                                                     │  │
│  │  • Query objects with SOQL                                       │  │
│  │  • Lookup record by ID                                           │  │
│  │  • List recent records                                           │  │
│  │  • Search across objects                                         │  │
│  │                                                                   │  │
│  │  DATA ACCESS                                                      │  │
│  │  ⚠️ Customer Data: Accounts, Contacts, Opportunities             │  │
│  │  ⚠️ PII: Contact email, phone, address                           │  │
│  │                                                                   │  │
│  │  ────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  OWNERSHIP                                                        │  │
│  │  Owner: Sales Operations Team                                    │  │
│  │  Created: Oct 15, 2024                                           │  │
│  │  Last Updated: Dec 10, 2024                                      │  │
│  │  Security Reviewed: Dec 1, 2024                                  │  │
│  │                                                                   │  │
│  │  ────────────────────────────────────────────────────────────── │  │
│  │                                                                   │  │
│  │  USAGE STATISTICS                                                 │  │
│  │                                                                   │  │
│  │  Teams Using: 34        Users: 127       Monthly Invocations: 8.2K│
│  │                                                                   │  │
│  │  Usage Trend (30 days):                                          │  │
│  │  ▁▂▃▄▅▆▇█▇▆▅▆▇█████▇▆▅▆▇███                                     │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  [Request Access]  [Report Issue]  [Contact Owner]                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Functional Requirements

### FR-1: MCP Discovery (Auto-Detection)

**Requirement:**
Automatically discover MCPs from Claude API usage logs.

**Details:**
- Parse Claude API calls for MCP invocations
- Extract MCP name, capabilities, resources
- Create registry entry if new MCP detected
- Link to team based on user who invoked
- Run detection hourly

**Acceptance Criteria:**
- [ ] New MCPs detected within 1 hour of first use
- [ ] MCP metadata accurately extracted
- [ ] No duplicate entries created
- [ ] Detection works for all MCP types

---

### FR-2: Manual MCP Registration

**Requirement:**
Allow users to manually register MCPs.

**Details:**
- Registration form with: name, description, category, capabilities
- Owner assignment (defaults to creator)
- Team assignment
- Status: Draft → Pending → Approved/Rejected
- Version number

**Acceptance Criteria:**
- [ ] Form validates required fields
- [ ] MCP appears in registry after save
- [ ] Owner receives confirmation
- [ ] Admins notified for approval

---

### FR-3: MCP Search

**Requirement:**
Enable searching across all registered MCPs.

**Details:**
- Full-text search on name, description, capabilities
- Filter by: category, team, status, data type
- Sort by: name, usage, date created
- Search results in <500ms

**Acceptance Criteria:**
- [ ] Search returns relevant results
- [ ] Filters work correctly
- [ ] Empty results show helpful message
- [ ] Results are paginated

---

### FR-4: MCP Categories

**Requirement:**
Organize MCPs into categories.

**Details:**
- Pre-defined categories: CRM, Finance, Code, Data, Communication, Custom
- Admin can add custom categories
- MCPs can be in multiple categories
- Category icons for visual distinction

**Acceptance Criteria:**
- [ ] All categories displayed
- [ ] Category counts accurate
- [ ] Filter by category works
- [ ] Custom categories supported

---

### FR-5: MCP Metadata

**Requirement:**
Capture comprehensive metadata for each MCP.

**Details:**

| Field | Type | Required |
|-------|------|----------|
| Name | String | Yes |
| Description | Text | Yes |
| Category | Enum[] | Yes |
| Owner | User | Yes |
| Team | Team | Yes |
| Status | Enum | Yes |
| Version | String | No |
| Capabilities | Text[] | No |
| Data Access | Text[] | No |
| Dependencies | MCP[] | No |
| Documentation URL | URL | No |

**Acceptance Criteria:**
- [ ] All fields stored correctly
- [ ] Required fields enforced
- [ ] Edit functionality works
- [ ] Change history tracked

---

### FR-6: MCP Usage Statistics

**Requirement:**
Track and display usage statistics per MCP.

**Details:**
- Total invocations (all time, last 30 days)
- Unique users
- Teams using
- Trend chart (invocations over time)

**Acceptance Criteria:**
- [ ] Stats update within 15 minutes
- [ ] Accurate counts
- [ ] Trend chart renders correctly
- [ ] Performance OK with high-usage MCPs

---

### FR-7: MCP Status Workflow

**Requirement:**
Implement status workflow for MCP lifecycle.

**Details:**
- Statuses: Draft, Pending Review, Approved, Deprecated, Rejected
- Transitions require authorization
- Comments on status changes
- Notification on status change

**Acceptance Criteria:**
- [ ] Status changes logged
- [ ] Only authorized users can approve
- [ ] Deprecated MCPs hidden by default
- [ ] History preserved

---

### FR-8: MCP Access Control

**Requirement:**
Control which teams can access which MCPs.

**Details:**
- Visibility: Private, Team, Specific Teams, Org-wide
- Private: Only owner can see/use
- Team: Owner's team can see/use
- Specific Teams: Listed teams can see/use
- Org-wide: Everyone can see/use

**Acceptance Criteria:**
- [ ] Access control enforced
- [ ] Users only see permitted MCPs
- [ ] Admins can override
- [ ] Request access workflow

---

## Non-Functional Requirements

### NFR-1: Performance

| Metric | Requirement |
|--------|-------------|
| Page load time | <2 seconds |
| Search response | <500ms |
| Registry capacity | 10,000+ MCPs |
| Auto-detection | Hourly |

### NFR-2: Scalability

| Metric | Requirement |
|--------|-------------|
| MCPs per org | 10,000+ |
| Concurrent searches | 100+ |
| API rate limit | 1000 req/min |

---

## Data Model

```sql
-- MCPs table
CREATE TABLE mcps (
  id UUID PRIMARY KEY,
  org_id UUID REFERENCES orgs(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  categories VARCHAR(100)[] DEFAULT '{}',
  owner_id UUID REFERENCES users(id),
  team_id UUID REFERENCES teams(id),
  status VARCHAR(50) DEFAULT 'draft',
  version VARCHAR(50),
  capabilities TEXT[],
  data_access TEXT[],
  documentation_url VARCHAR(500),
  visibility VARCHAR(50) DEFAULT 'team',
  allowed_teams UUID[],
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  -- Search optimization
  search_vector TSVECTOR
);

-- Full-text search index
CREATE INDEX idx_mcp_search ON mcps USING GIN(search_vector);

-- MCP usage stats (aggregated daily)
CREATE TABLE mcp_usage_stats (
  id UUID PRIMARY KEY,
  mcp_id UUID REFERENCES mcps(id),
  date DATE,
  invocations INTEGER DEFAULT 0,
  unique_users INTEGER DEFAULT 0,
  teams_using INTEGER DEFAULT 0
);
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/mcps` | GET | List MCPs (with filters) |
| `/api/mcps` | POST | Register new MCP |
| `/api/mcps/:id` | GET | Get MCP details |
| `/api/mcps/:id` | PUT | Update MCP |
| `/api/mcps/:id` | DELETE | Archive MCP |
| `/api/mcps/:id/stats` | GET | Get usage stats |
| `/api/mcps/:id/access` | POST | Request access |
| `/api/mcps/search` | GET | Search MCPs |
| `/api/mcps/categories` | GET | List categories |

---

## Future Enhancements (Post-MVP)

1. **Duplicate Detection:** AI-powered detection of similar MCPs
2. **MCP Versioning:** Track version history, rollback
3. **MCP Dependencies:** Map dependencies between MCPs
4. **MCP Templates:** Start from pre-built templates
5. **Marketplace Integration:** Publish to public marketplace

---

## Related Documents

- [PRD-MVP.md](../PRD-MVP.md) - MVP requirements
- [FEATURE-HIVEMIND.md](./FEATURE-HIVEMIND.md) - Duplicate detection (v1.0)
- [../wireframes/WIREFRAME-MCP-REGISTRY.md](../wireframes/WIREFRAME-MCP-REGISTRY.md) - Wireframes

---

*Last Updated: December 2025*
*Owner: Engineering Lead*

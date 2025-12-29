# MindWeave MVP Product Requirements Document

> Formal PRD for Minimum Viable Product

---

## Document Information

| Field | Value |
|-------|-------|
| **Product** | MindWeave |
| **Version** | MVP (v0.1) |
| **Author** | The OG (CEO) |
| **Status** | Draft |
| **Target Date** | Q1 2025 |
| **Last Updated** | December 2025 |

---

## Executive Summary

### Vision

MindWeave MVP enables enterprises to gain visibility and basic control over their Claude deployments, validating product-market fit with 10 design partners.

### Mission

Ship the minimum feature set that proves enterprises will pay for Claude governance, generating $2M ARR within 6 months of launch.

### Success Metrics

| Metric | Target |
|--------|--------|
| Design Partners | 10 |
| Paying Customers (Month 6) | 25 |
| ARR (Month 6) | $2M |
| NPS | 40+ |
| Feature Usage | 70%+ weekly active |

---

## Problem Statement

### The Problem

Enterprises deploying Claude at scale (50-5000 employees) lack visibility into:
1. **Who** is using Claude and how much
2. **What** integrations (MCPs) exist across the organization
3. **How much** they're spending and who to attribute costs to
4. **Whether** usage complies with security and governance requirements

### Evidence

- 100% of customer interviews cited lack of visibility as top pain point
- 75% have discovered duplicate MCP builds across teams
- 88% cannot attribute Claude costs to specific teams
- 63% have compliance concerns about AI usage

### Impact

- Wasted spend on duplicate development
- Compliance risk from ungoverned AI usage
- Inability to demonstrate AI ROI
- Security vulnerabilities from untracked integrations

---

## Target Users

### Primary Persona: VP/Director of Engineering

**Profile:**
- Manages 50-500 engineers
- Responsible for developer productivity
- Reports to CTO on AI adoption
- Budget owner for developer tools

**Goals:**
- Understand Claude adoption across team
- Justify AI tool investment to leadership
- Prevent duplicate work across teams
- Enable developers while maintaining control

**Pain Points:**
- No visibility into who uses Claude
- Can't track costs by team
- Discovers duplicate MCPs accidentally
- Struggles to report on AI usage

---

### Secondary Persona: CISO/Security Leader

**Profile:**
- Responsible for security and compliance
- Reports to CEO/Board on risk
- Approves new technology purchases
- Manages audits and compliance

**Goals:**
- Ensure Claude usage is auditable
- Prevent unauthorized data access
- Maintain compliance with regulations
- Demonstrate governance to auditors

**Pain Points:**
- No audit trail for AI usage
- Can't control who accesses what via Claude
- Compliance requirements unclear
- Board asking about AI governance

---

### Tertiary Persona: Engineering Manager

**Profile:**
- Manages 5-15 engineers
- Hands-on with team's tools
- Advocates for productivity tools
- Evaluates and champions new tech

**Goals:**
- Enable team to use Claude effectively
- Track team's Claude usage
- Share best practices
- Justify tool budget

**Pain Points:**
- Team building MCPs others already built
- Can't see how other teams use Claude
- No way to share learnings
- Usage reporting is manual

---

## MVP Scope

### In Scope

| Feature | Priority | Rationale |
|---------|----------|-----------|
| Token Usage Dashboard | P0 | #1 pain point from research |
| Team/User Management | P0 | Foundation for all features |
| MCP Registry | P0 | Core differentiator |
| Basic Audit Logs | P0 | Compliance requirement |
| SSO Integration | P0 | Enterprise table stakes |

### Out of Scope (Post-MVP)

| Feature | Version | Rationale |
|---------|---------|-----------|
| Hivemind Discovery | v1.0 | Complex, needs data |
| DORA Metrics | v1.0 | Nice-to-have |
| Skill Tracking | v1.0 | Needs ML |
| Multi-Model Support | v2.0 | Focus on Claude |
| MCP Marketplace | v3.0 | Network effects later |

---

## Feature Specifications

### Feature 1: Token Usage Dashboard

#### Overview

Real-time visibility into Claude token consumption across organization, broken down by team, user, and time period.

#### User Stories

| ID | Story | Priority |
|----|-------|----------|
| TU-1 | As a VP Eng, I want to see total token usage this month so I can track spend | P0 |
| TU-2 | As a VP Eng, I want to see usage by team so I can allocate costs | P0 |
| TU-3 | As an Eng Manager, I want to see my team's usage vs. others so I can benchmark | P1 |
| TU-4 | As a Finance user, I want to export usage data so I can do chargebacks | P1 |
| TU-5 | As a VP Eng, I want to set budget alerts so I can prevent overages | P2 |

#### Requirements

**Functional:**
- FR-TU-1: Display total tokens (input + output) for selectable time period
- FR-TU-2: Calculate and display estimated cost based on Claude pricing
- FR-TU-3: Break down usage by team hierarchy (org → team → user)
- FR-TU-4: Show usage trends (daily, weekly, monthly charts)
- FR-TU-5: Allow filtering by model (Haiku, Sonnet, Opus)
- FR-TU-6: Export data as CSV/Excel

**Non-Functional:**
- NFR-TU-1: Dashboard loads in <2 seconds
- NFR-TU-2: Data updates within 15 minutes of API usage
- NFR-TU-3: Supports 10,000+ users without performance degradation

#### Acceptance Criteria

```gherkin
Feature: Token Usage Dashboard

Scenario: View organization token usage
  Given I am logged in as an org admin
  When I navigate to the Token Usage dashboard
  Then I see total tokens consumed this month
  And I see estimated cost in USD
  And I see a chart of daily usage

Scenario: View team breakdown
  Given I am viewing the Token Usage dashboard
  When I click "By Team" tab
  Then I see a table of teams ranked by token usage
  And each row shows team name, tokens, cost, % of total

Scenario: Export usage data
  Given I am viewing usage data
  When I click "Export CSV"
  Then a CSV file downloads with usage by user and day
```

---

### Feature 2: Team/User Management

#### Overview

Administrative functionality to create organizational structure, manage users, and assign roles.

#### User Stories

| ID | Story | Priority |
|----|-------|----------|
| TM-1 | As an admin, I want to create teams so I can organize users | P0 |
| TM-2 | As an admin, I want to add users from SSO so they can access MindWeave | P0 |
| TM-3 | As an admin, I want to assign users to teams so usage is attributed | P0 |
| TM-4 | As an admin, I want to set user roles so permissions are appropriate | P1 |
| TM-5 | As an admin, I want to create team hierarchies so we match org structure | P2 |

#### Requirements

**Functional:**
- FR-TM-1: Create, read, update, delete teams
- FR-TM-2: Support nested team hierarchies (up to 5 levels)
- FR-TM-3: Sync users from Okta/Azure AD
- FR-TM-4: Assign users to one or more teams
- FR-TM-5: Define roles: Org Admin, Team Admin, Member, Viewer
- FR-TM-6: Bulk user import via CSV

**Non-Functional:**
- NFR-TM-1: User sync completes within 5 minutes
- NFR-TM-2: Support 10,000+ users per organization
- NFR-TM-3: Changes reflected across system within 1 minute

#### Acceptance Criteria

```gherkin
Feature: Team Management

Scenario: Create a new team
  Given I am an org admin
  When I click "Create Team" and enter "Backend Engineering"
  Then a new team is created
  And I can assign users to it

Scenario: SSO user sync
  Given Okta is configured
  When users are added/removed in Okta
  Then MindWeave reflects changes within 5 minutes

Scenario: Assign user to team
  Given I am a team admin
  When I add a user to my team
  Then their Claude usage is attributed to this team
```

---

### Feature 3: MCP Registry

#### Overview

Centralized inventory of all Model Context Protocol integrations across the organization, with metadata and ownership.

#### User Stories

| ID | Story | Priority |
|----|-------|----------|
| MR-1 | As a VP Eng, I want to see all MCPs in our org so I know what exists | P0 |
| MR-2 | As a developer, I want to discover MCPs before building so I avoid duplication | P0 |
| MR-3 | As an admin, I want to see who built each MCP so I know ownership | P0 |
| MR-4 | As a developer, I want to see MCP usage stats so I know what's popular | P1 |
| MR-5 | As an admin, I want to flag MCPs as approved/pending/deprecated | P2 |

#### Requirements

**Functional:**
- FR-MR-1: Auto-discover MCPs from Claude API logs
- FR-MR-2: Display MCP list with: name, description, creator, team, created date
- FR-MR-3: Show usage stats per MCP (invocations, users, tokens)
- FR-MR-4: Search and filter MCPs by name, team, category
- FR-MR-5: Allow manual MCP registration for local MCPs
- FR-MR-6: Status workflow: Draft → Pending Review → Approved → Deprecated

**Non-Functional:**
- NFR-MR-1: MCP discovery runs hourly
- NFR-MR-2: Registry search returns results in <500ms
- NFR-MR-3: Support 10,000+ MCPs per organization

#### Acceptance Criteria

```gherkin
Feature: MCP Registry

Scenario: View all MCPs
  Given I am logged in
  When I navigate to MCP Registry
  Then I see a list of all MCPs in my organization
  And I see name, team, creator, and usage for each

Scenario: Search for MCP
  Given I am in the MCP Registry
  When I search for "Salesforce"
  Then I see all MCPs with Salesforce in name or description

Scenario: View MCP details
  Given I am viewing an MCP
  When I click on it
  Then I see full description, creator, creation date
  And I see usage charts (invocations over time)
  And I see which teams use this MCP
```

---

### Feature 4: Basic Audit Logs

#### Overview

Comprehensive logging of all Claude interactions for compliance, debugging, and security.

#### User Stories

| ID | Story | Priority |
|----|-------|----------|
| AL-1 | As a CISO, I want to see all Claude usage so I can audit for compliance | P0 |
| AL-2 | As an admin, I want to search logs by user so I can investigate issues | P0 |
| AL-3 | As a compliance officer, I want to export logs so I can provide to auditors | P0 |
| AL-4 | As a CISO, I want to see which MCPs were used so I understand data access | P1 |
| AL-5 | As an admin, I want log retention controls so we meet policy requirements | P2 |

#### Requirements

**Functional:**
- FR-AL-1: Log every Claude API call with: timestamp, user, team, model, tokens, MCPs
- FR-AL-2: Search logs by user, team, date range, model, MCP
- FR-AL-3: Export logs as CSV with date range filter
- FR-AL-4: Display log entries in sortable, filterable table
- FR-AL-5: Configurable retention period (30/60/90/365 days)
- FR-AL-6: Do NOT log conversation content in MVP (privacy concerns)

**Non-Functional:**
- NFR-AL-1: Logs written within 5 seconds of API call
- NFR-AL-2: Log search returns results in <3 seconds for 100M logs
- NFR-AL-3: Log storage is encrypted at rest (AES-256)
- NFR-AL-4: Logs cannot be deleted by users (immutable)

#### Acceptance Criteria

```gherkin
Feature: Audit Logs

Scenario: View recent audit logs
  Given I am an admin or compliance officer
  When I navigate to Audit Logs
  Then I see a table of recent Claude usage
  And each row shows timestamp, user, team, model, tokens, MCPs

Scenario: Search audit logs
  Given I am viewing Audit Logs
  When I filter by user "susan@acme.com" and date range "Dec 1-15"
  Then I see only Susan's usage in that period

Scenario: Export for compliance
  Given I have filtered audit logs
  When I click "Export CSV"
  Then a file downloads with all matching log entries
```

---

### Feature 5: SSO Integration

#### Overview

Single Sign-On integration with enterprise identity providers for secure, managed access.

#### User Stories

| ID | Story | Priority |
|----|-------|----------|
| SSO-1 | As an admin, I want to configure Okta so users login via SSO | P0 |
| SSO-2 | As a user, I want to login with my work credentials so I don't need a new password | P0 |
| SSO-3 | As an admin, I want to configure Azure AD so users login via SSO | P0 |
| SSO-4 | As an admin, I want JIT provisioning so new users are created on first login | P1 |
| SSO-5 | As an admin, I want SCIM so user lifecycle is automated | P2 |

#### Requirements

**Functional:**
- FR-SSO-1: Support SAML 2.0 SSO with Okta
- FR-SSO-2: Support SAML 2.0 SSO with Azure AD
- FR-SSO-3: Just-in-time user provisioning on first login
- FR-SSO-4: Map SSO groups to MindWeave teams
- FR-SSO-5: Support SSO logout (SLO)
- FR-SSO-6: SCIM 2.0 for user provisioning/deprovisioning

**Non-Functional:**
- NFR-SSO-1: SSO login completes in <3 seconds
- NFR-SSO-2: Support 10,000+ concurrent SSO sessions
- NFR-SSO-3: Session timeout configurable (default 8 hours)

#### Acceptance Criteria

```gherkin
Feature: SSO Integration

Scenario: Okta SSO login
  Given Okta is configured
  When a user navigates to MindWeave and clicks "Login with Okta"
  Then they are redirected to Okta
  And after authentication, they are logged into MindWeave

Scenario: JIT provisioning
  Given a user exists in Okta but not in MindWeave
  When they SSO login for the first time
  Then a MindWeave account is created automatically
  And they are assigned to a default team

Scenario: SSO logout
  Given a user is logged in via SSO
  When they click logout
  Then they are logged out of MindWeave
  And redirected to IdP logout (if configured)
```

---

## Technical Requirements

### Architecture Overview

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           MINDWEAVE MVP ARCHITECTURE                      │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────────────────────┐│
│  │   React     │────│   Node.js   │────│        PostgreSQL            ││
│  │   Frontend  │     │   API       │     │        + Redis               ││
│  └─────────────┘     └─────────────┘     └─────────────────────────────┘│
│         │                  │                         │                   │
│         │                  │                         │                   │
│  ┌──────┴──────────────────┴─────────────────────────┴─────────────────┐│
│  │                        AWS INFRASTRUCTURE                            ││
│  │  • ECS/Fargate (containers)                                          ││
│  │  • RDS PostgreSQL (database)                                         ││
│  │  • ElastiCache Redis (sessions, cache)                               ││
│  │  • S3 (log storage, exports)                                         ││
│  │  • CloudWatch (monitoring)                                           ││
│  │  • Route 53 (DNS)                                                    ││
│  │  • ACM (SSL certificates)                                            ││
│  └─────────────────────────────────────────────────────────────────────┘│
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │                        EXTERNAL INTEGRATIONS                         │ │
│  │  • Claude API (via Anthropic)                                        │ │
│  │  • Okta (SSO)                                                        │ │
│  │  • Azure AD (SSO)                                                    │ │
│  │  • Stripe (billing) - post-MVP                                       │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

### Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Frontend | React + TypeScript | Industry standard, hiring pool |
| UI Framework | Tailwind + Shadcn | Fast development, beautiful UX |
| API | Node.js + Express | JavaScript everywhere, fast iteration |
| Database | PostgreSQL | Reliable, scalable, JSON support |
| Cache | Redis | Sessions, real-time updates |
| Cloud | AWS | Market leader, enterprise trust |
| Auth | Passport.js + SAML | Proven SSO library |

### Performance Requirements

| Metric | Requirement |
|--------|-------------|
| Page load time | <2 seconds |
| API response time | <500ms (p95) |
| Concurrent users | 1,000+ |
| Data freshness | <15 minutes |
| Uptime | 99.9% |

### Security Requirements

| Requirement | Implementation |
|-------------|----------------|
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.3 |
| Authentication | SSO + MFA |
| Authorization | RBAC |
| Audit logging | Immutable logs |
| Vulnerability scanning | Weekly |

---

## Success Criteria

### MVP Launch Criteria (Q1 2025)

| Criterion | Measure | Target |
|-----------|---------|--------|
| Features Complete | All P0 features shipped | 100% |
| Quality | Critical bugs | 0 |
| Performance | Page load | <2s |
| Security | Vulnerabilities | 0 critical/high |
| Design Partners | Active usage | 10 |

### 6-Month Success Criteria

| Metric | Target | Stretch |
|--------|--------|---------|
| Paying Customers | 25 | 40 |
| ARR | $2M | $3M |
| NPS | 40 | 50 |
| Logo Churn | <5% | <3% |
| Feature Adoption | 70% | 80% |

---

## Dependencies

### External Dependencies

| Dependency | Owner | Risk | Mitigation |
|------------|-------|------|------------|
| Claude API access | Anthropic | Low | Existing relationship |
| Okta integration | Engineering | Low | Well-documented |
| Azure AD integration | Engineering | Low | Well-documented |
| AWS infrastructure | DevOps | Low | Standard stack |

### Internal Dependencies

| Dependency | Owner | Status |
|------------|-------|--------|
| Founding engineer hired | CEO | In progress |
| Design partner agreements | CEO | 2 signed |
| Seed funding | CEO | Fundraising |

---

## Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Engineering delays | Medium | High | Prioritize ruthlessly, cut scope |
| Design partner churn | Low | Medium | Oversubscribe, active engagement |
| Claude API changes | Low | High | Abstract API layer, monitor closely |
| Competitor launches | Medium | Medium | Move fast, ship unique features |

---

## Timeline

```
MVP Development Timeline

Week 1-2      Week 3-4      Week 5-6      Week 7-8
────────────────────────────────────────────────────
│ Foundation  │ Core Data   │ Dashboard   │ Polish  │
│             │             │             │         │
│ • Auth/SSO  │ • Team CRUD │ • Token UI  │ • Test  │
│ • DB schema │ • MCP sync  │ • MCP UI    │ • Docs  │
│ • API setup │ • Audit log │ • Audit UI  │ • Pilot │
└─────────────┴─────────────┴─────────────┴─────────┘
                                                    ▼
                                              MVP LAUNCH
```

---

## Appendix

### Glossary

| Term | Definition |
|------|------------|
| MCP | Model Context Protocol - Anthropic's standard for AI tool integrations |
| Token | Unit of text processed by Claude (roughly 4 characters) |
| Org | Top-level customer organization in MindWeave |
| Team | Group of users within an organization |
| RBAC | Role-Based Access Control |
| SSO | Single Sign-On |
| JIT | Just-In-Time provisioning |

### References

- [PRODUCT-ROADMAP.md](./PRODUCT-ROADMAP.md)
- [PRIORITY-MATRIX.md](./PRIORITY-MATRIX.md)
- [../01-research/CUSTOMER-INTERVIEWS.md](../01-research/CUSTOMER-INTERVIEWS.md)

---

*Document Owner: The OG (CEO)*
*Approval Required: VP Product, CTO*
*Version: 1.0 Draft*

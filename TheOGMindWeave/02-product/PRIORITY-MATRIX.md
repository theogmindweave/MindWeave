# MindWeave Priority Matrix

> What to build, in what order, and why

---

## The 80/20 Rule Applied

**80% of value comes from 20% of features.**

Our job: Identify the 20% that matters most.

---

## Priority Framework

We use **ICE Scoring**:
- **I**mpact (1-10): How much value does this create?
- **C**onfidence (1-10): How sure are we this works?
- **E**ase (1-10): How easy is it to build?

**ICE Score = (Impact + Confidence + Ease) / 3**

---

## TIER 1: Must Have (MVP)

*These ship in v0.1 or we don't launch*

| Feature | Impact | Confidence | Ease | ICE | Why Critical |
|---------|--------|------------|------|-----|--------------|
| **Token Usage Dashboard** | 10 | 10 | 8 | 9.3 | #1 pain point - "where's my money going?" |
| **Team/User Management** | 9 | 10 | 7 | 8.7 | Foundation for everything else |
| **MCP Registry** | 9 | 9 | 6 | 8.0 | Core differentiator - see all MCPs |
| **Basic Audit Logs** | 8 | 10 | 8 | 8.7 | Compliance table stakes |
| **SSO (Okta/Azure)** | 8 | 10 | 6 | 8.0 | Enterprise requirement |

### MVP Scope Summary
- See token usage by team/user
- Create teams, assign users
- View all MCPs in organization
- Basic audit trail
- Login via Okta/Azure AD

**Build Time Estimate:** 6-8 weeks
**First Value:** "I can finally see what we're spending on Claude"

---

## TIER 2: Should Have (v1.0)

*Ship within 3 months of MVP*

| Feature | Impact | Confidence | Ease | ICE | Why Important |
|---------|--------|------------|------|-----|---------------|
| **Team-Based MCP Access** | 9 | 9 | 5 | 7.7 | Security - Finance can't see Sales MCPs |
| **DORA Metrics** | 8 | 8 | 5 | 7.0 | Engineering leaders love this |
| **Nightly Processing** | 9 | 7 | 4 | 6.7 | Core to APIR - but complex |
| **Skill Suggestions** | 9 | 6 | 4 | 6.3 | Differentiator - but needs data first |
| **Cost Alerts** | 7 | 10 | 8 | 8.3 | "Alert me when team exceeds budget" |

### v1.0 Scope Summary
- Per-team MCP permissions
- DORA metrics dashboard
- Nightly analysis jobs (basic)
- Simple skill suggestions
- Budget alerts

**Build Time Estimate:** 8-12 weeks after MVP

---

## TIER 3: Nice to Have (v1.5)

*Ship within 6 months*

| Feature | Impact | Confidence | Ease | ICE | Notes |
|---------|--------|------------|------|-----|-------|
| **Hivemind Discovery** | 10 | 5 | 3 | 6.0 | Huge differentiator but hard |
| **Manager Approval Flow** | 7 | 8 | 5 | 6.7 | Important for enterprise |
| **SOC 2 Dashboard** | 8 | 9 | 4 | 7.0 | Compliance reporting |
| **API Access** | 6 | 10 | 6 | 7.3 | Developers want this |
| **Slack Integration** | 6 | 9 | 7 | 7.3 | Notifications |

---

## TIER 4: Future (v2.0+)

*Backlog for later*

| Feature | Impact | Notes |
|---------|--------|-------|
| Multi-model Support (GPT-4, Gemini) | 8 | Reduces Claude dependency |
| Skill Marketplace | 9 | Network effects - big opportunity |
| Custom Dashboards | 6 | Enterprise customization |
| On-Prem Deployment | 7 | Premier tier feature |
| Mobile App | 4 | Low priority for enterprise |

---

## The 80/20 Analysis

### The 20% That Delivers 80% Value

1. **Token Usage Visibility** (30% of value)
   - Simple dashboard showing spend
   - Team breakdown
   - Trend over time

2. **MCP Registry** (25% of value)
   - See all MCPs in one place
   - Know who built what
   - Avoid duplicates

3. **Team-Based Access Control** (15% of value)
   - Security/compliance
   - Per-team permissions

4. **Basic Analytics** (10% of value)
   - Usage patterns
   - Top users
   - Active MCPs

**Total: 80% of customer value from 4 features**

### What to SKIP (for now)

| Feature | Why Skip |
|---------|----------|
| Complex ML/AI features | Need data first, high complexity |
| Multi-cloud support | Focus on Claude only for MVP |
| Custom branding | Enterprise fluff |
| Advanced reporting | Start simple |
| Webhooks | API access is enough |

---

## Decision: MVP Feature Set

### IN (Build This)
- Token usage dashboard
- Team/user management
- MCP registry (read-only)
- Audit logs (basic)
- SSO authentication

### OUT (Not MVP)
- DORA metrics
- Skill suggestions
- Hivemind discovery
- Manager approvals
- Marketplace

---

## Build Sequence

```
Week 1-2: Foundation
├── Auth (SSO)
├── Database schema
└── Basic API

Week 3-4: Core Data
├── User/Team CRUD
├── MCP import/sync
└── Audit logging

Week 5-6: Dashboard
├── Token usage UI
├── Team overview
└── MCP registry

Week 7-8: Polish
├── Testing
├── Documentation
└── Pilot onboarding
```

---

## Validation Checkpoints

| Milestone | Success Criteria | When |
|-----------|-----------------|------|
| Week 2 | Can login via SSO | Week 2 |
| Week 4 | Can see token usage | Week 4 |
| Week 6 | Can browse MCPs | Week 6 |
| Week 8 | First pilot customer happy | Week 8 |

---

## Key Decisions Made

1. **Claude-only for MVP** - No multi-model
2. **No AI features in MVP** - Build data foundation first
3. **SSO required** - Enterprise table stakes
4. **Read-only MCP registry** - No MCP management in MVP
5. **Simple audit** - Full compliance later

---

*APIR: This priority matrix will evolve as we learn.*

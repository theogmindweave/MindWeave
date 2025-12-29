# User Stories: Developer

> 10 user stories for the Developer persona

---

## Persona Overview

### Senior Developer / Tech Lead

**Profile:**
- Senior software engineer or tech lead
- Daily Claude user for coding assistance
- Builds MCPs for team productivity
- Technically sophisticated, values efficiency
- Advocates for useful tools

**Goals:**
- Use Claude effectively without friction
- Find and reuse existing MCPs
- Share useful integrations with team
- Avoid bureaucratic governance overhead

**Frustrations:**
- Builds MCPs others already built
- Can't find what's available
- Governance feels like policing
- No visibility into own usage

---

## User Stories

### Story 1: Discover Existing MCPs Before Building

**Story:**
> As a Developer, I want to search for existing MCPs before building new ones so that I don't waste time duplicating work.

**Acceptance Criteria:**
- [ ] Search bar prominently displayed
- [ ] Search by name, description, keywords
- [ ] See usage stats (how popular is this MCP?)
- [ ] See owner and contact info
- [ ] Quick preview of MCP capabilities

**Priority:** P0

**Story Points:** 3

**Dependencies:** MCP Registry

---

### Story 2: View My Personal Usage Stats

**Story:**
> As a Developer, I want to see my own Claude usage statistics so that I understand my AI consumption.

**Acceptance Criteria:**
- [ ] Personal dashboard shows my tokens used
- [ ] Breakdown by model (Haiku, Sonnet, Opus)
- [ ] Breakdown by MCP used
- [ ] Trend over time (week, month)
- [ ] Compare to team average (optional)

**Priority:** P1

**Story Points:** 2

**Dependencies:** Usage tracking, personal dashboard

---

### Story 3: Quick Access to Approved MCPs

**Story:**
> As a Developer, I want quick access to MCPs I'm allowed to use so that I can integrate them into my workflow.

**Acceptance Criteria:**
- [ ] "My MCPs" section on dashboard
- [ ] Shows MCPs I have access to
- [ ] One-click to view MCP details
- [ ] Recently used MCPs highlighted
- [ ] Favorite/bookmark MCPs for quick access

**Priority:** P1

**Story Points:** 2

**Dependencies:** MCP Registry, access control

---

### Story 4: Request Access to Restricted MCP

**Story:**
> As a Developer, I want to request access to MCPs my team doesn't have so that I can use tools built by other teams.

**Acceptance Criteria:**
- [ ] "Request Access" button on restricted MCPs
- [ ] Form to explain why access needed
- [ ] Notification sent to MCP owner/admin
- [ ] Status tracking (pending, approved, denied)
- [ ] Email notification when resolved

**Priority:** P2

**Story Points:** 3

**Dependencies:** MCP access control, workflow

---

### Story 5: Share MCP with My Team

**Story:**
> As a Developer, I want to share an MCP I built with my team so that they can benefit from my work.

**Acceptance Criteria:**
- [ ] Register MCP with name, description, instructions
- [ ] Set visibility to team only (initially)
- [ ] Team members can see and use immediately
- [ ] Edit MCP metadata as needed
- [ ] View usage of my shared MCP

**Priority:** P1

**Story Points:** 2

**Dependencies:** MCP Registry, team management

---

### Story 6: Propose MCP for Org-Wide Use

**Story:**
> As a Developer, I want to propose my MCP for org-wide use so that all teams can benefit.

**Acceptance Criteria:**
- [ ] "Propose for Org" action on my MCP
- [ ] Describe business value and use cases
- [ ] Workflow routes to security/admin for review
- [ ] Track approval status
- [ ] Promoted to org-wide if approved

**Priority:** P2

**Story Points:** 2

**Dependencies:** MCP Registry, approval workflow

---

### Story 7: View MCP Documentation

**Story:**
> As a Developer, I want to see documentation for an MCP so that I know how to use it correctly.

**Acceptance Criteria:**
- [ ] MCP detail page has documentation section
- [ ] Shows: purpose, inputs, outputs, examples
- [ ] Includes setup instructions if needed
- [ ] Contact info for MCP owner
- [ ] Version history if updated

**Priority:** P1

**Story Points:** 2

**Dependencies:** MCP Registry

---

### Story 8: Report Issue with MCP

**Story:**
> As a Developer, I want to report issues with an MCP so that problems get fixed.

**Acceptance Criteria:**
- [ ] "Report Issue" button on MCP detail
- [ ] Describe the issue
- [ ] Notification to MCP owner
- [ ] Issue tracked with status
- [ ] Resolution notification

**Priority:** P2

**Story Points:** 2

**Dependencies:** MCP Registry, issue tracking

---

### Story 9: See What's Popular

**Story:**
> As a Developer, I want to see the most popular MCPs so that I can discover useful tools.

**Acceptance Criteria:**
- [ ] "Trending" or "Popular" section on MCP Registry
- [ ] Ranked by usage (invocations, users)
- [ ] Filter by category (CRM, code, data, etc.)
- [ ] See popularity trend (rising, stable)
- [ ] Recommendations based on my team's profile

**Priority:** P2

**Story Points:** 2

**Dependencies:** MCP usage analytics

---

### Story 10: Authenticate via SSO

**Story:**
> As a Developer, I want to login with my work SSO so that I don't need another password.

**Acceptance Criteria:**
- [ ] "Login with Okta" or "Login with Azure AD" button
- [ ] Redirects to company SSO
- [ ] Returns to MindWeave authenticated
- [ ] No separate MindWeave password needed
- [ ] Session persists for workday (8 hours)

**Priority:** P0

**Story Points:** 3

**Dependencies:** SSO integration

---

## Story Map

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        DEVELOPER STORY MAP                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  DISCOVERY               SHARING                 ACCOUNT                 │
│  ─────────               ───────                 ───────                 │
│  │                       │                       │                       │
│  ├─ S1: Search MCPs      ├─ S5: Share w/ Team    ├─ S2: My Usage        │
│  │                       │                       │                       │
│  ├─ S3: My MCPs          ├─ S6: Propose Org      ├─ S10: SSO Login      │
│  │                       │                       │                       │
│  ├─ S7: View Docs        ├─ S4: Request Access   │                       │
│  │                       │                       │                       │
│  ├─ S9: Popular MCPs     ├─ S8: Report Issue     │                       │
│  │                       │                       │                       │
│                                                                          │
│  MVP: S1, S10            v1.0: S2, S3, S5, S7    v1.5: S4, S6, S8, S9   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Prioritization

| Story | Priority | Sprint | Rationale |
|-------|----------|--------|-----------|
| S1: Search MCPs | P0 | MVP | Core discovery |
| S10: SSO Login | P0 | MVP | Access requirement |
| S2: My Usage | P1 | v1.0 | Personal value |
| S3: My MCPs | P1 | v1.0 | Quick access |
| S5: Share w/ Team | P1 | v1.0 | Enable sharing |
| S7: View Docs | P1 | v1.0 | Usability |
| S4: Request Access | P2 | v1.5 | Workflow feature |
| S6: Propose Org | P2 | v1.5 | Governance |
| S8: Report Issue | P2 | v1.5 | Maintenance |
| S9: Popular MCPs | P2 | v1.5 | Discovery |

---

## Developer Experience Principles

### 1. Minimal Friction
- Don't require extra steps for basic Claude usage
- Governance should be invisible when not needed
- One-click access to commonly used features

### 2. Self-Service
- Developers can find what they need without asking
- Documentation is readily available
- Issues can be reported and tracked

### 3. Value Over Policing
- Show developers value (save time, find MCPs)
- Don't position as surveillance
- Enable productivity, don't hinder it

---

## Related Documents

- [PRD-MVP.md](./PRD-MVP.md) - MVP requirements
- [USER-STORIES-ENGINEERING-MANAGER.md](./USER-STORIES-ENGINEERING-MANAGER.md) - Manager stories
- [USER-STORIES-CISO.md](./USER-STORIES-CISO.md) - Security stories

---

*Last Updated: December 2025*
*Owner: VP Product (TBH)*

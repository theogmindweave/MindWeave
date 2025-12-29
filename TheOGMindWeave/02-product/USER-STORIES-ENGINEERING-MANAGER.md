# User Stories: Engineering Manager

> 10 user stories for the Engineering Manager persona

---

## Persona Overview

### Engineering Manager

**Profile:**
- Manages 8-15 engineers on a product team
- Hands-on technical background
- Responsible for team productivity and output
- Reports to VP/Director of Engineering
- Champions new tools and processes

**Goals:**
- Maximize team productivity with AI tools
- Track and justify AI tool investment
- Share best practices within and across teams
- Identify skill gaps and training needs

**Frustrations:**
- No visibility into how team uses Claude
- Discovers duplicate work after it's built
- Can't benchmark team against others
- Manual processes to track AI usage

---

## User Stories

### Story 1: View Team Token Usage

**Story:**
> As an Engineering Manager, I want to see my team's Claude token usage so that I can understand our AI consumption and budget.

**Acceptance Criteria:**
- [ ] Dashboard shows my team's total tokens (input + output) for current month
- [ ] Dashboard shows estimated cost in USD
- [ ] I can select different time periods (week, month, quarter)
- [ ] I can see usage trend over time (chart)
- [ ] Data refreshes at least every 15 minutes

**Priority:** P0

**Story Points:** 3

**Dependencies:** Token tracking infrastructure

---

### Story 2: Compare Team Usage to Organization

**Story:**
> As an Engineering Manager, I want to compare my team's Claude usage to other teams so that I can benchmark our AI adoption.

**Acceptance Criteria:**
- [ ] Leaderboard shows all teams ranked by token usage
- [ ] My team is highlighted in the list
- [ ] I can see percentage of total org usage
- [ ] I can filter by time period
- [ ] Comparison includes tokens and estimated cost

**Priority:** P1

**Story Points:** 2

**Dependencies:** Team management, org-wide data access

---

### Story 3: View Individual Developer Usage

**Story:**
> As an Engineering Manager, I want to see token usage by individual developer so that I can identify power users and encourage adoption.

**Acceptance Criteria:**
- [ ] Table shows each team member's usage
- [ ] Sortable by tokens, cost, number of sessions
- [ ] Can see usage trend per developer
- [ ] Can click through to user details
- [ ] Respects privacy settings (configurable org-wide)

**Priority:** P1

**Story Points:** 2

**Dependencies:** User-level usage tracking

---

### Story 4: Discover Existing MCPs

**Story:**
> As an Engineering Manager, I want to search for existing MCPs before my team builds new ones so that we don't duplicate work.

**Acceptance Criteria:**
- [ ] Search box in MCP Registry
- [ ] Search by name, description, category
- [ ] Results show MCP name, team owner, usage stats
- [ ] Can filter by status (approved, pending, deprecated)
- [ ] Can see which teams are using each MCP

**Priority:** P0

**Story Points:** 3

**Dependencies:** MCP Registry

---

### Story 5: Register Team's MCPs

**Story:**
> As an Engineering Manager, I want to register MCPs my team builds so that others can discover and reuse them.

**Acceptance Criteria:**
- [ ] Form to register new MCP with: name, description, category
- [ ] Assign owner (defaults to me)
- [ ] Set visibility (team only, org-wide)
- [ ] MCP appears in registry after submission
- [ ] Can edit MCP metadata after creation

**Priority:** P1

**Story Points:** 2

**Dependencies:** MCP Registry, Team management

---

### Story 6: View Team's MCP Portfolio

**Story:**
> As an Engineering Manager, I want to see all MCPs my team owns so that I can manage our integration portfolio.

**Acceptance Criteria:**
- [ ] Filtered view showing only my team's MCPs
- [ ] Shows each MCP's status, usage, last updated
- [ ] Can identify unused or deprecated MCPs
- [ ] Can see which other teams use our MCPs
- [ ] Export list for team review

**Priority:** P1

**Story Points:** 2

**Dependencies:** MCP Registry, Team filtering

---

### Story 7: Set Team Token Budget

**Story:**
> As an Engineering Manager, I want to set a monthly token budget for my team so that I can control costs.

**Acceptance Criteria:**
- [ ] Input field for monthly budget (in tokens or USD)
- [ ] Dashboard shows current usage vs. budget
- [ ] Progress bar visualization (80%, 100% thresholds)
- [ ] Email notification when 80% consumed
- [ ] Option for hard cap or soft warning

**Priority:** P2

**Story Points:** 3

**Dependencies:** Token tracking, notification system

---

### Story 8: Review Team Audit Logs

**Story:**
> As an Engineering Manager, I want to review my team's Claude activity logs so that I can investigate issues or unusual usage.

**Acceptance Criteria:**
- [ ] Audit log filtered to my team only
- [ ] Shows timestamp, user, model, tokens, MCPs used
- [ ] Search by user, date range, MCP
- [ ] Export filtered logs for analysis
- [ ] Does NOT show conversation content (privacy)

**Priority:** P1

**Story Points:** 2

**Dependencies:** Audit logging, Team filtering

---

### Story 9: Identify AI Champions

**Story:**
> As an Engineering Manager, I want to identify which team members are most effective with Claude so that I can leverage their expertise.

**Acceptance Criteria:**
- [ ] Report showing top users by sessions, tokens, MCPs used
- [ ] Identify users with consistent, growing usage
- [ ] See which MCPs each user commonly invokes
- [ ] Highlight users with high output ratio (output/input tokens)
- [ ] Exportable for recognition or training planning

**Priority:** P2

**Story Points:** 3

**Dependencies:** Usage analytics, user-level tracking

---

### Story 10: Onboard New Team Member

**Story:**
> As an Engineering Manager, I want to add new engineers to my team so that their usage is tracked correctly.

**Acceptance Criteria:**
- [ ] Add user to team (via search or SSO sync)
- [ ] New user inherits team permissions
- [ ] New user sees team's MCP inventory
- [ ] Their usage is attributed to our team immediately
- [ ] Can remove users who leave the team

**Priority:** P0

**Story Points:** 2

**Dependencies:** Team management, SSO integration

---

## Story Map

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ENGINEERING MANAGER STORY MAP                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  VISIBILITY              DISCOVERY              MANAGEMENT               │
│  ─────────               ─────────              ──────────               │
│  │                       │                      │                        │
│  ├─ S1: Team Usage       ├─ S4: Search MCPs     ├─ S5: Register MCPs    │
│  │                       │                      │                        │
│  ├─ S2: Compare Teams    ├─ S6: Team MCPs       ├─ S7: Set Budget       │
│  │                       │                      │                        │
│  ├─ S3: Developer Usage  │                      ├─ S10: Onboard User    │
│  │                       │                      │                        │
│  ├─ S8: Audit Logs       │                      │                        │
│  │                       │                      │                        │
│  └─ S9: AI Champions     │                      │                        │
│                                                                          │
│  MVP: S1, S4, S10        v1.0: S2, S3, S5, S6, S8     v1.5: S7, S9     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Prioritization

| Story | Priority | Sprint | Rationale |
|-------|----------|--------|-----------|
| S1: Team Usage | P0 | MVP | Core value proposition |
| S4: Search MCPs | P0 | MVP | Discovery is key differentiator |
| S10: Onboard User | P0 | MVP | Foundation for team management |
| S2: Compare Teams | P1 | v1.0 | Benchmarking adds value |
| S3: Developer Usage | P1 | v1.0 | Manager need |
| S5: Register MCPs | P1 | v1.0 | Enable sharing |
| S6: Team MCPs | P1 | v1.0 | Portfolio management |
| S8: Audit Logs | P1 | v1.0 | Compliance need |
| S7: Set Budget | P2 | v1.5 | Cost control |
| S9: AI Champions | P2 | v1.5 | Advanced analytics |

---

## Related Documents

- [PRD-MVP.md](./PRD-MVP.md) - MVP requirements
- [USER-STORIES-CISO.md](./USER-STORIES-CISO.md) - CISO stories
- [USER-STORIES-DEVELOPER.md](./USER-STORIES-DEVELOPER.md) - Developer stories

---

*Last Updated: December 2025*
*Owner: VP Product (TBH)*

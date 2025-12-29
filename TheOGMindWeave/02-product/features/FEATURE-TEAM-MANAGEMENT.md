# Feature Specification: Team Management

> Complete specification for the Team Management feature

---

## Overview

### Feature Summary

| Field | Value |
|-------|-------|
| **Feature Name** | Team Management |
| **Priority** | P0 (MVP) |
| **Target Version** | v0.1 (MVP) |
| **Effort Estimate** | 3 weeks |
| **Owner** | Engineering |

### Description

Team Management provides the administrative functionality to create organizational structure, manage users, assign roles, and establish the foundation for team-based governance.

### Problem Statement

Enterprise Claude deployments lack organizational structure:
- No way to group users into teams
- Can't attribute usage to organizational units
- Can't set permissions at team level
- No alignment with existing org structure

### Success Metrics

| Metric | Target |
|--------|--------|
| Team Coverage | 100% of users assigned to teams |
| Admin Satisfaction | 4.5/5 rating |
| Setup Time | <30 minutes for 500 users |
| SSO Sync | 95% accuracy with IdP |

---

## User Experience

### Entry Points

1. **Main Navigation:** "Teams" in left sidebar (admin only)
2. **Settings:** "Organization" → "Teams"
3. **User Profile:** View/change team assignment

### Primary Screen: Teams List

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← Team Management                                    + Create Team     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Organization: Acme Corp                    Total Users: 487      │  │
│  │  Teams: 12            Unassigned Users: 3                        │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  🔍 Search teams...                      Sort: [Name ▼]  [Structure ▼] │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                                                                   │  │
│  │  ▼ Engineering                                    87 members     │  │
│  │    │                                                              │  │
│  │    ├── Backend Team                               34 members     │  │
│  │    │   Admin: John Smith                                         │  │
│  │    │   MCPs: 12  │  Monthly Tokens: 523M                        │  │
│  │    │                                                              │  │
│  │    ├── Frontend Team                              28 members     │  │
│  │    │   Admin: Sarah Lee                                          │  │
│  │    │   MCPs: 8   │  Monthly Tokens: 187M                        │  │
│  │    │                                                              │  │
│  │    └── ML Team                                    25 members     │  │
│  │        Admin: David Chen                                         │  │
│  │        MCPs: 23  │  Monthly Tokens: 312M                        │  │
│  │                                                                   │  │
│  │  ▼ Product                                        23 members     │  │
│  │    Admin: Emily Brown                                            │  │
│  │    MCPs: 5   │  Monthly Tokens: 187M                            │  │
│  │                                                                   │  │
│  │  ▼ Sales                                          45 members     │  │
│  │    Admin: Mike Wilson                                            │  │
│  │    MCPs: 7   │  Monthly Tokens: 94M                             │  │
│  │                                                                   │  │
│  │  ▶ Marketing                                      18 members     │  │
│  │  ▶ Finance                                        12 members     │  │
│  │  ▶ Customer Success                               22 members     │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ⚠️ 3 users not assigned to any team  [View & Assign]                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Team Detail Screen

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← Back to Teams                                       ⚙ Edit Team     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Backend Team                                                     │  │
│  │  Part of: Engineering                                             │  │
│  │                                                                   │  │
│  │  Admin: John Smith (john@acme.com)                               │  │
│  │  Created: Oct 15, 2024                                           │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  [Members]  [MCPs]  [Usage]  [Settings]                                 │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Members (34)                              + Add Member           │  │
│  │                                                                   │  │
│  │  🔍 Search members...                                             │  │
│  │                                                                   │  │
│  │  Name              Email                   Role        Joined     │  │
│  │  ─────────────────────────────────────────────────────────────   │  │
│  │  John Smith        john@acme.com           Admin       Oct 15     │  │
│  │  Alice Wang        alice@acme.com          Member      Oct 16     │  │
│  │  Bob Johnson       bob@acme.com            Member      Oct 17     │  │
│  │  Carol Davis       carol@acme.com          Member      Oct 18     │  │
│  │  ...                                                              │  │
│  │                                                                   │  │
│  │  [1] [2] [3] [4] ... [7]                                         │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Functional Requirements

### FR-1: Create Team

**Requirement:**
Allow admins to create new teams.

**Details:**
- Form with: team name, description, parent team (optional)
- Assign team admin
- Set initial members
- Configure team settings

**Acceptance Criteria:**
- [ ] Team created successfully
- [ ] Team appears in hierarchy
- [ ] Admin receives notification
- [ ] Validation on duplicate names

---

### FR-2: Team Hierarchy

**Requirement:**
Support nested team structure up to 5 levels.

**Details:**
- Root teams have no parent
- Child teams inherit from parent
- Usage aggregates up hierarchy
- MCPs can be scoped to hierarchy

**Acceptance Criteria:**
- [ ] Create nested teams
- [ ] Display hierarchy visually
- [ ] Aggregate stats correctly
- [ ] Prevent circular references

---

### FR-3: Add/Remove Team Members

**Requirement:**
Allow team admins to manage team membership.

**Details:**
- Add users by email or from SSO directory
- Remove users from team
- Bulk add/remove
- Users can be in multiple teams

**Acceptance Criteria:**
- [ ] Add single user works
- [ ] Remove user works
- [ ] Bulk operations work
- [ ] Multi-team membership works

---

### FR-4: Team Roles

**Requirement:**
Define roles within teams.

**Details:**
- Org Admin: Full org access
- Team Admin: Full team access
- Member: Standard access
- Viewer: Read-only access

| Permission | Org Admin | Team Admin | Member | Viewer |
|------------|-----------|------------|--------|--------|
| View all teams | ✅ | ❌ | ❌ | ❌ |
| Create teams | ✅ | ❌ | ❌ | ❌ |
| Edit own team | ✅ | ✅ | ❌ | ❌ |
| Add team members | ✅ | ✅ | ❌ | ❌ |
| View team MCPs | ✅ | ✅ | ✅ | ✅ |
| Register MCPs | ✅ | ✅ | ✅ | ❌ |
| View team usage | ✅ | ✅ | ✅ | ✅ |
| Export data | ✅ | ✅ | ❌ | ❌ |

**Acceptance Criteria:**
- [ ] Roles enforced correctly
- [ ] UI reflects permissions
- [ ] Role changes take effect immediately
- [ ] Audit log captures role changes

---

### FR-5: SSO User Sync

**Requirement:**
Sync users from Okta/Azure AD.

**Details:**
- SCIM 2.0 provisioning
- Just-in-time (JIT) provisioning
- Map IdP groups to MindWeave teams
- Sync runs on schedule + real-time

**Acceptance Criteria:**
- [ ] New users created on first login (JIT)
- [ ] SCIM creates/deactivates users
- [ ] Group mapping works
- [ ] Sync errors logged and alerted

---

### FR-6: Team Settings

**Requirement:**
Configure team-specific settings.

**Details:**
- Token budget (optional)
- Default MCP access level
- Notification preferences
- Team description and metadata

**Acceptance Criteria:**
- [ ] Settings save correctly
- [ ] Settings applied to team
- [ ] Inherited from parent (configurable)
- [ ] Override at child level

---

### FR-7: Unassigned Users Management

**Requirement:**
Handle users not assigned to any team.

**Details:**
- Display list of unassigned users
- Quick assign to teams
- Default team option
- Alert when new unassigned users

**Acceptance Criteria:**
- [ ] Unassigned users visible
- [ ] Easy assignment workflow
- [ ] Default team configurable
- [ ] Alerts sent to admins

---

## Data Model

```sql
-- Teams table
CREATE TABLE teams (
  id UUID PRIMARY KEY,
  org_id UUID REFERENCES orgs(id),
  parent_team_id UUID REFERENCES teams(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  token_budget_monthly BIGINT,
  settings JSONB DEFAULT '{}',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  UNIQUE(org_id, name)
);

-- Team memberships
CREATE TABLE team_memberships (
  id UUID PRIMARY KEY,
  team_id UUID REFERENCES teams(id),
  user_id UUID REFERENCES users(id),
  role VARCHAR(50) DEFAULT 'member',
  joined_at TIMESTAMP DEFAULT NOW(),

  UNIQUE(team_id, user_id)
);

-- Create indexes
CREATE INDEX idx_team_org ON teams(org_id);
CREATE INDEX idx_team_parent ON teams(parent_team_id);
CREATE INDEX idx_membership_user ON team_memberships(user_id);
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/teams` | GET | List all teams |
| `/api/teams` | POST | Create team |
| `/api/teams/:id` | GET | Get team details |
| `/api/teams/:id` | PUT | Update team |
| `/api/teams/:id` | DELETE | Archive team |
| `/api/teams/:id/members` | GET | List members |
| `/api/teams/:id/members` | POST | Add member(s) |
| `/api/teams/:id/members/:userId` | DELETE | Remove member |
| `/api/users/unassigned` | GET | List unassigned users |

---

## Related Documents

- [PRD-MVP.md](../PRD-MVP.md) - MVP requirements
- [FEATURE-SSO-AUTH.md](./FEATURE-SSO-AUTH.md) - SSO integration
- [../wireframes/WIREFRAME-TEAM-MANAGEMENT.md](../wireframes/WIREFRAME-TEAM-MANAGEMENT.md)

---

*Last Updated: December 2025*
*Owner: Engineering Lead*

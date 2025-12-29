# Feature Specification: Token Usage Dashboard

> Complete specification for the Token Usage Dashboard feature

---

## Overview

### Feature Summary

| Field | Value |
|-------|-------|
| **Feature Name** | Token Usage Dashboard |
| **Priority** | P0 (MVP) |
| **Target Version** | v0.1 (MVP) |
| **Effort Estimate** | 3 weeks |
| **Owner** | Engineering |

### Description

The Token Usage Dashboard provides real-time visibility into Claude token consumption across the organization. It enables leaders to understand spend, track trends, and allocate costs to teams.

### Problem Statement

Enterprises deploying Claude have no visibility into:
- Total token consumption
- Cost attribution by team
- Usage trends over time
- Model utilization (Haiku vs. Sonnet vs. Opus)

This leads to budget surprises, inability to demonstrate ROI, and lack of cost accountability.

### Success Metrics

| Metric | Target |
|--------|--------|
| Feature Adoption | 90% of admins use weekly |
| Time to Value | <5 minutes to first insight |
| User Satisfaction | 4.5/5 star rating |
| Export Usage | 30% of users export monthly |

---

## User Experience

### Entry Points

1. **Main Navigation:** "Usage" in left sidebar
2. **Dashboard Card:** Summary widget on home dashboard
3. **Quick Link:** "View Usage" from team page

### Primary Screen: Usage Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← Usage Dashboard                                    Export ↓  Filter ⚙│
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  This Month: December 2025                                        │  │
│  │                                                                   │  │
│  │  Total Tokens          Cost              Trend                    │  │
│  │  ████████████████      ██████████        ████████████            │  │
│  │  847.3M               $42,365            +23% vs Nov             │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Daily Usage Trend                                                │  │
│  │                                                                   │  │
│  │      ▲                                         ┌──┐               │  │
│  │      │                            ┌──┐    ┌──┐ │  │               │  │
│  │  40M │                    ┌──┐    │  │    │  │ │  │ ┌──┐          │  │
│  │      │          ┌──┐ ┌──┐ │  │    │  │    │  │ │  │ │  │          │  │
│  │  20M │     ┌──┐ │  │ │  │ │  │┌──┐│  │┌──┐│  │ │  │ │  │          │  │
│  │      │ ┌──┐│  │ │  │ │  │ │  ││  ││  ││  ││  │ │  │ │  │          │  │
│  │   0M └─────────────────────────────────────────────────────────   │  │
│  │        1   5    10   15   20   25   28                            │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌────────────────────────────┐  ┌────────────────────────────────────┐│
│  │  By Team                   │  │  By Model                          ││
│  │                            │  │                                    ││
│  │  Engineering    523M  62%  │  │  Sonnet       612M  72%           ││
│  │  █████████████████████████ │  │  ████████████████████████████████ ││
│  │                            │  │                                    ││
│  │  Product        187M  22%  │  │  Haiku        178M  21%           ││
│  │  ████████████              │  │  ████████████                     ││
│  │                            │  │                                    ││
│  │  Sales           94M  11%  │  │  Opus          57M   7%           ││
│  │  ██████                    │  │  ████                             ││
│  │                            │  │                                    ││
│  │  Marketing       43M   5%  │  │                                    ││
│  │  ███                       │  │                                    ││
│  │                            │  │                                    ││
│  │  View All Teams →          │  │                                    ││
│  └────────────────────────────┘  └────────────────────────────────────┘│
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Top Users This Month                                             │  │
│  │                                                                   │  │
│  │  #   User              Team         Tokens      Cost              │  │
│  │  ─────────────────────────────────────────────────────────────   │  │
│  │  1   Susan Chen        Product      47.2M       $2,360            │  │
│  │  2   David Park        Backend      39.1M       $1,955            │  │
│  │  3   Maria Lopez       Sales        31.8M       $1,590            │  │
│  │  4   James Wilson      Frontend     28.4M       $1,420            │  │
│  │  5   Emily Brown       ML Team      24.7M       $1,235            │  │
│  │                                                                   │  │
│  │  View All Users →                                                 │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Filters

| Filter | Options |
|--------|---------|
| **Time Period** | Today, This Week, This Month, This Quarter, Custom Range |
| **Team** | All Teams, Specific Team(s) |
| **Model** | All Models, Haiku, Sonnet, Opus |
| **User** | All Users, Specific User(s) |

### Export Options

| Format | Contents |
|--------|----------|
| **CSV** | Raw data by day, user, team, model |
| **Excel** | Formatted with charts |
| **PDF** | Executive summary report |

---

## Functional Requirements

### FR-1: Display Total Token Usage

**Requirement:**
Display total tokens consumed for selected time period.

**Details:**
- Sum of input tokens + output tokens
- Calculated from audit log data
- Updates within 15 minutes of usage
- Handles millions of tokens without overflow

**Acceptance Criteria:**
- [ ] Total displays correctly for all time periods
- [ ] Handles 0 usage gracefully
- [ ] Matches audit log totals exactly

---

### FR-2: Calculate and Display Cost

**Requirement:**
Display estimated cost in USD based on Claude pricing.

**Details:**
- Uses current Claude API pricing:
  - Haiku: $0.25 / $1.25 per MTok (input/output)
  - Sonnet: $3 / $15 per MTok
  - Opus: $15 / $75 per MTok
- Separate input/output token costs
- Admin can override pricing if negotiated rates differ

**Acceptance Criteria:**
- [ ] Cost calculations are accurate to 2 decimal places
- [ ] Pricing is configurable in admin settings
- [ ] Cost breakdown by model available

---

### FR-3: Team Usage Breakdown

**Requirement:**
Display token usage broken down by team.

**Details:**
- Bar chart or table showing each team's usage
- Percentage of total
- Sortable by tokens or cost
- Click-through to team detail

**Acceptance Criteria:**
- [ ] All teams with usage displayed
- [ ] Sorted by usage descending by default
- [ ] Teams with 0 usage shown (optional toggle)

---

### FR-4: User Usage Breakdown

**Requirement:**
Display top users by token consumption.

**Details:**
- Top 10 users by default, expandable
- Shows: name, team, tokens, cost
- Links to user profile
- Respects privacy settings (can be disabled)

**Acceptance Criteria:**
- [ ] Top users displayed correctly
- [ ] Privacy toggle in settings
- [ ] Team managers only see their team (RBAC)

---

### FR-5: Usage Trend Chart

**Requirement:**
Display usage over time in a chart.

**Details:**
- Line or bar chart
- Granularity: daily (for month), weekly (for quarter), monthly (for year)
- Comparison to previous period (optional overlay)
- Tooltip with details on hover

**Acceptance Criteria:**
- [ ] Chart renders in <2 seconds
- [ ] All data points accurate
- [ ] Responsive design (mobile-friendly)

---

### FR-6: Model Usage Breakdown

**Requirement:**
Display usage by Claude model.

**Details:**
- Pie chart or bar chart
- Shows: Haiku, Sonnet, Opus
- Percentage and absolute tokens
- Cost per model

**Acceptance Criteria:**
- [ ] All models displayed
- [ ] Accurate breakdown
- [ ] Cost calculated per model

---

### FR-7: Export Functionality

**Requirement:**
Allow users to export usage data.

**Details:**
- CSV: raw data, filterable
- Excel: formatted with summary
- PDF: executive report format
- Email option for scheduled reports

**Acceptance Criteria:**
- [ ] Export completes in <30 seconds for 1 year of data
- [ ] Exported data matches dashboard
- [ ] Secure (no unauthorized export)

---

### FR-8: Time Period Selection

**Requirement:**
Allow selection of various time periods.

**Details:**
- Presets: Today, This Week, This Month, This Quarter, This Year
- Custom date range picker
- Compare to previous period option
- Timezone handling (user's local time)

**Acceptance Criteria:**
- [ ] All presets work correctly
- [ ] Custom range works with date picker
- [ ] Timezone displays correctly

---

## Non-Functional Requirements

### NFR-1: Performance

| Metric | Requirement |
|--------|-------------|
| Page load time | <2 seconds |
| Data refresh | <15 minutes lag |
| Chart render | <1 second |
| Export time | <30 seconds |

### NFR-2: Scalability

| Metric | Requirement |
|--------|-------------|
| Users per org | 10,000+ |
| Tokens per month | 10B+ |
| Teams per org | 500+ |
| Concurrent users | 100+ |

### NFR-3: Security

| Requirement | Implementation |
|-------------|----------------|
| Data access | RBAC enforced |
| Export audit | Logged in audit trail |
| Encryption | TLS in transit, AES at rest |

---

## Technical Design

### Data Model

```sql
-- Usage aggregation table (materialized view)
CREATE TABLE usage_aggregates (
  id UUID PRIMARY KEY,
  org_id UUID REFERENCES orgs(id),
  team_id UUID REFERENCES teams(id),
  user_id UUID REFERENCES users(id),
  model VARCHAR(50),
  date DATE,
  input_tokens BIGINT,
  output_tokens BIGINT,
  total_tokens BIGINT,
  estimated_cost DECIMAL(12,4),
  created_at TIMESTAMP
);

-- Index for fast queries
CREATE INDEX idx_usage_org_date ON usage_aggregates(org_id, date);
CREATE INDEX idx_usage_team_date ON usage_aggregates(team_id, date);
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/usage/summary` | GET | Total usage for period |
| `/api/usage/by-team` | GET | Usage by team |
| `/api/usage/by-user` | GET | Usage by user |
| `/api/usage/by-model` | GET | Usage by model |
| `/api/usage/trend` | GET | Time series data |
| `/api/usage/export` | POST | Generate export |

### Aggregation Pipeline

```
Claude API ──► Audit Log ──► Aggregation Job ──► Usage Table ──► Dashboard
                              (runs hourly)
```

---

## Edge Cases

| Scenario | Behavior |
|----------|----------|
| No usage data | Show "No usage data" message with onboarding |
| Deleted user | Show "Deleted User" in reports, retain data |
| Deleted team | Archive usage, show in historical views |
| Timezone change | Use user's current timezone for display |
| Pricing change | Apply new pricing to future data only |

---

## Dependencies

| Dependency | Type | Status |
|------------|------|--------|
| Audit log infrastructure | Internal | In progress |
| Team management | Internal | Planned |
| User authentication | Internal | Planned |
| Claude pricing API | External | Research needed |

---

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Aggregation performance | Medium | High | Pre-compute, caching |
| Pricing accuracy | Low | Medium | Regular pricing updates |
| Data volume | Medium | Medium | Archival strategy |

---

## Future Enhancements (Post-MVP)

1. **Budget Alerts:** Notify when usage exceeds threshold
2. **Forecasting:** Predict month-end usage
3. **Anomaly Detection:** Flag unusual usage patterns
4. **Chargeback Reports:** Finance-ready cost allocation
5. **Custom Dashboards:** Drag-and-drop widgets

---

## Related Documents

- [PRD-MVP.md](../PRD-MVP.md) - MVP requirements
- [FEATURE-AUDIT-LOGS.md](./FEATURE-AUDIT-LOGS.md) - Audit logs (data source)
- [../wireframes/WIREFRAME-TOKEN-USAGE.md](../wireframes/WIREFRAME-TOKEN-USAGE.md) - Wireframes

---

*Last Updated: December 2025*
*Owner: Engineering Lead*

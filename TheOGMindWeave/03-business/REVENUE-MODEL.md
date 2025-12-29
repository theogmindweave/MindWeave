# MindWeave Revenue Model

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Revenue Model Architecture |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Author | MindWeave Business Team |
| Status | Strategic |
| Classification | Confidential |

---

## 1. Revenue Model Overview

### 1.1 Model Type

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        HYBRID SAAS REVENUE MODEL                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│    ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐    │
│    │   RECURRING  │    │  USAGE-BASED │    │      SERVICES        │    │
│    │  SUBSCRIPTION│    │   COMPONENT  │    │    (PROFESSIONAL)    │    │
│    └──────┬───────┘    └──────┬───────┘    └──────────┬───────────┘    │
│           │                   │                       │                 │
│           v                   v                       v                 │
│    ┌────────────────────────────────────────────────────────────────┐  │
│    │                    TOTAL REVENUE                                │  │
│    │   Subscription (85%) + Usage Overages (10%) + Services (5%)    │  │
│    └────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Revenue Stream Composition

| Stream | Year 1 | Year 2 | Year 3 | Description |
|--------|--------|--------|--------|-------------|
| Subscription | 90% | 85% | 82% | Recurring monthly/annual fees |
| Usage Overages | 5% | 10% | 12% | Per-seat, per-token overages |
| Professional Services | 5% | 5% | 6% | Implementation, training |

---

## 2. Subscription Revenue

### 2.1 Tier Revenue Breakdown

```
┌─────────────────────────────────────────────────────────────────────┐
│                  SUBSCRIPTION TIER REVENUE MIX                       │
│                                                                      │
│   Year 1                    Year 2                   Year 3          │
│   ┌─────────────────────┐   ┌─────────────────────┐  ┌────────────┐  │
│   │                     │   │                     │  │            │  │
│   │    Team: 60%        │   │    Team: 45%        │  │ Team: 30%  │  │
│   │    ($6K ARR avg)    │   │    ($6K ARR avg)    │  │            │  │
│   │                     │   │                     │  │ Pro: 35%   │  │
│   │    Pro: 30%         │   │    Pro: 40%         │  │            │  │
│   │    ($24K ARR avg)   │   │    ($24K ARR avg)   │  │ Ent: 35%   │  │
│   │                     │   │                     │  │            │  │
│   │    Enterprise: 10%  │   │    Enterprise: 15%  │  │            │  │
│   │    ($60K ARR avg)   │   │    ($60K ARR avg)   │  │            │  │
│   └─────────────────────┘   └─────────────────────┘  └────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Average Revenue Per Account (ARPA)

| Tier | Monthly | Annual | Notes |
|------|---------|--------|-------|
| Team | $500 | $5,400 (10% discount) | 10 seats included |
| Pro | $2,000 | $21,600 (10% discount) | 50 seats included |
| Enterprise | $5,000+ | $54,000+ | Custom, 100+ seats |

### 2.3 Blended ARPA Trajectory

| Period | Blended ARPA | Growth Driver |
|--------|--------------|---------------|
| Q1 Y1 | $8,000 | Early adopters (Pro-heavy) |
| Q4 Y1 | $12,000 | Enterprise traction |
| Q4 Y2 | $18,000 | Enterprise expansion |
| Q4 Y3 | $28,000 | Large enterprise deals |

---

## 3. Usage-Based Revenue

### 3.1 Usage Pricing Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        USAGE-BASED PRICING                              │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                    INCLUDED IN SUBSCRIPTION                      │   │
│   │                                                                  │   │
│   │   Team:       10 seats, 1M tokens/mo, 10 MCP servers             │   │
│   │   Pro:        50 seats, 10M tokens/mo, 50 MCP servers            │   │
│   │   Enterprise: 100+ seats, 100M+ tokens, unlimited MCP            │   │
│   │                                                                  │   │
│   └──────────────────────────┬──────────────────────────────────────┘   │
│                              │                                          │
│                              v                                          │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                      OVERAGE PRICING                             │   │
│   │                                                                  │   │
│   │   Additional Seats:      $25/seat/month                          │   │
│   │   Additional Tokens:     $2 per 100K tokens                      │   │
│   │   Additional MCP:        $10/server/month                        │   │
│   │   API Calls:             $0.10 per 1,000 calls (after 100K)      │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Overage Revenue Projections

| Metric | Y1 | Y2 | Y3 |
|--------|----|----|-----|
| % Accounts with Overages | 15% | 25% | 35% |
| Avg Overage per Account | $150/mo | $300/mo | $500/mo |
| Total Overage Revenue | $54K | $270K | $1.05M |

### 3.3 Usage Growth Drivers

| Driver | Description | Revenue Impact |
|--------|-------------|----------------|
| Team Growth | Customers hire more developers | +20% seat overages |
| AI Adoption | More AI usage = more tokens | +30% token overages |
| MCP Expansion | New tool integrations | +15% MCP overages |
| API Integrations | Custom dashboard builds | +10% API overages |

---

## 4. Professional Services Revenue

### 4.1 Service Offerings

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROFESSIONAL SERVICES CATALOG                        │
│                                                                         │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐    │
│   │  IMPLEMENTATION │  │    TRAINING     │  │   CUSTOM DEV        │    │
│   ├─────────────────┤  ├─────────────────┤  ├─────────────────────┤    │
│   │                 │  │                 │  │                     │    │
│   │ Standard: $5K   │  │ Basic: $2K      │  │ MCP Custom: $10K+   │    │
│   │ Premium: $15K   │  │ Advanced: $5K   │  │ Integration: $15K+  │    │
│   │ Enterprise: $50K│  │ Enterprise: $10K│  │ Dedicated: $25K+    │    │
│   │                 │  │                 │  │                     │    │
│   │ Avg Engagement: │  │ Avg Engagement: │  │ Avg Engagement:     │    │
│   │ $12K            │  │ $4K             │  │ $18K                │    │
│   │                 │  │                 │  │                     │    │
│   └─────────────────┘  └─────────────────┘  └─────────────────────┘    │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                    SUPPORT PACKAGES                              │   │
│   │                                                                  │   │
│   │   Standard:    Included in subscription                          │   │
│   │   Premium:     $500/month - 4hr response, dedicated CSM          │   │
│   │   Enterprise:  $2,000/month - 1hr response, TAM                  │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Services Revenue Mix

| Service Type | Y1 % | Y2 % | Y3 % |
|--------------|------|------|------|
| Implementation | 60% | 50% | 40% |
| Training | 25% | 25% | 25% |
| Custom Development | 10% | 15% | 20% |
| Premium Support | 5% | 10% | 15% |

### 4.3 Services Attach Rate

| Tier | Implementation | Training | Support Upgrade |
|------|----------------|----------|-----------------|
| Team | 5% | 10% | 2% |
| Pro | 30% | 40% | 15% |
| Enterprise | 80% | 60% | 50% |

---

## 5. Revenue Recognition

### 5.1 Recognition Policies

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     REVENUE RECOGNITION (ASC 606)                       │
│                                                                         │
│   SUBSCRIPTION REVENUE                                                  │
│   ├── Monthly subscriptions: Recognized monthly as service delivered    │
│   ├── Annual subscriptions: Recognized ratably over 12 months           │
│   └── Multi-year deals: Recognized ratably over contract term           │
│                                                                         │
│   USAGE REVENUE                                                         │
│   ├── Overage fees: Recognized in month of usage                        │
│   └── Pre-purchased credits: Recognized as consumed                     │
│                                                                         │
│   PROFESSIONAL SERVICES                                                 │
│   ├── Time & materials: Recognized as services performed                │
│   ├── Fixed-fee projects: Recognized on % completion                    │
│   └── Training: Recognized upon delivery                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Deferred Revenue

| Category | Typical Deferral Period | Y1 Balance |
|----------|------------------------|------------|
| Annual Subscriptions | 6 months avg | $180K |
| Multi-year Deals | 18 months avg | $90K |
| Pre-purchased Credits | 3 months avg | $15K |
| **Total Deferred** | - | **$285K** |

---

## 6. Revenue Expansion

### 6.1 Expansion Revenue Sources

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      NET REVENUE RETENTION DRIVERS                       │
│                                                                         │
│    ┌──────────────────────────────────────────────────────────────┐     │
│    │                     EXPANSION MOTIONS                         │     │
│    ├──────────────────────────────────────────────────────────────┤     │
│    │                                                               │     │
│    │   1. SEAT EXPANSION                                           │     │
│    │      └─> Developer team growth adds seats                     │     │
│    │      └─> Typical: +20% seats/year in growing companies        │     │
│    │                                                               │     │
│    │   2. TIER UPGRADES                                            │     │
│    │      └─> Team → Pro: Need SSO, audit logs                     │     │
│    │      └─> Pro → Enterprise: Need custom integrations           │     │
│    │                                                               │     │
│    │   3. USAGE GROWTH                                             │     │
│    │      └─> More AI adoption = more token usage                  │     │
│    │      └─> More MCP servers deployed                            │     │
│    │                                                               │     │
│    │   4. CROSS-SELL                                               │     │
│    │      └─> Premium support packages                             │     │
│    │      └─> Professional services                                │     │
│    │                                                               │     │
│    └──────────────────────────────────────────────────────────────┘     │
│                                                                         │
│    Target NRR: 115% (Y1) → 125% (Y2) → 130% (Y3)                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Expansion Revenue Metrics

| Metric | Y1 | Y2 | Y3 |
|--------|----|----|-----|
| Gross Revenue Retention | 90% | 92% | 94% |
| Expansion Revenue Rate | 25% | 33% | 36% |
| Net Revenue Retention | 115% | 125% | 130% |
| Expansion ARR | $90K | $375K | $1.2M |

### 6.3 Upgrade Funnel

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        TIER UPGRADE FUNNEL                              │
│                                                                         │
│   TEAM TIER CUSTOMERS (100 accounts)                                    │
│   │                                                                     │
│   ├─> 70% Remain Team (grow seats)                                      │
│   │                                                                     │
│   ├─> 25% Upgrade to Pro (within 18 months)                             │
│   │   └─> Triggers: >15 seats, SSO requirement, audit needs             │
│   │                                                                     │
│   └─> 5% Churn                                                          │
│                                                                         │
│   PRO TIER CUSTOMERS (50 accounts)                                      │
│   │                                                                     │
│   ├─> 75% Remain Pro (grow seats/usage)                                 │
│   │                                                                     │
│   ├─> 20% Upgrade to Enterprise (within 24 months)                      │
│   │   └─> Triggers: >75 seats, custom SLA, dedicated support            │
│   │                                                                     │
│   └─> 5% Churn                                                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Revenue Seasonality

### 7.1 Quarterly Patterns

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      QUARTERLY REVENUE PATTERNS                          │
│                                                                         │
│   Revenue Index (Q1 = 100)                                              │
│                                                                         │
│   130 ┤                                              ████               │
│   120 ┤                         ████                 ████               │
│   110 ┤             ████        ████        ████     ████               │
│   100 ┤   ████      ████        ████        ████     ████               │
│    90 ┤   ████      ████        ████        ████     ████               │
│       └─────────────────────────────────────────────────────            │
│           Q1        Q2          Q3          Q4                          │
│                                                                         │
│   Q1: Budget cycle start - new deals close                              │
│   Q2: Slight uptick - Q1 implementations complete                       │
│   Q3: Summer slowdown (offset by expansion)                             │
│   Q4: Year-end budget flush - enterprise deals                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Enterprise Sales Cycle

| Phase | Duration | Activities |
|-------|----------|------------|
| Discovery | 2-4 weeks | Demo, requirements |
| Evaluation | 4-6 weeks | POC, security review |
| Procurement | 4-8 weeks | Legal, finance |
| **Total Cycle** | **10-18 weeks** | - |

---

## 8. Revenue by Customer Segment

### 8.1 Segment Distribution

| Segment | Y1 ARR | Y2 ARR | Y3 ARR | % of Total (Y3) |
|---------|--------|--------|--------|-----------------|
| Enterprise Tech | $360K | $1.2M | $3.6M | 40% |
| Financial Services | $90K | $450K | $1.8M | 20% |
| Healthcare | $45K | $225K | $900K | 10% |
| AI-First Startups | $180K | $450K | $900K | 10% |
| Professional Services | $45K | $180K | $720K | 8% |
| Other | $80K | $295K | $1.08M | 12% |

### 8.2 Segment Characteristics

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SEGMENT REVENUE CHARACTERISTICS                       │
│                                                                         │
│   ENTERPRISE TECH (40% of revenue)                                      │
│   ├── Avg Deal Size: $45K ARR                                           │
│   ├── Sales Cycle: 12 weeks                                             │
│   ├── NRR: 130%                                                         │
│   └── CAC: $15K                                                         │
│                                                                         │
│   FINANCIAL SERVICES (20% of revenue)                                   │
│   ├── Avg Deal Size: $60K ARR                                           │
│   ├── Sales Cycle: 20 weeks                                             │
│   ├── NRR: 120%                                                         │
│   └── CAC: $25K                                                         │
│                                                                         │
│   AI-FIRST STARTUPS (10% of revenue)                                    │
│   ├── Avg Deal Size: $12K ARR                                           │
│   ├── Sales Cycle: 4 weeks                                              │
│   ├── NRR: 150%                                                         │
│   └── CAC: $3K                                                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 9. Revenue Forecasting Model

### 9.1 Bottom-Up Methodology

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    REVENUE FORECASTING METHODOLOGY                       │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ 1. PIPELINE ANALYSIS                                             │   │
│   │    New ARR = Qualified Pipeline × Win Rate × Avg Deal Size       │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                              ↓                                          │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ 2. EXPANSION CALCULATION                                         │   │
│   │    Expansion ARR = Beginning ARR × (NRR - GRR)                   │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                              ↓                                          │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ 3. CHURN DEDUCTION                                               │   │
│   │    Churned ARR = Beginning ARR × (1 - GRR)                       │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                              ↓                                          │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ 4. TOTAL ARR                                                     │   │
│   │    Ending ARR = Beginning + New + Expansion - Churn              │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 9.2 Key Forecast Assumptions

| Assumption | Conservative | Base | Aggressive |
|------------|--------------|------|------------|
| New Logo Win Rate | 15% | 20% | 25% |
| Average Deal Size | $15K | $18K | $22K |
| Net Revenue Retention | 110% | 120% | 130% |
| Gross Revenue Retention | 88% | 92% | 95% |
| Sales Cycle (days) | 120 | 90 | 60 |

### 9.3 Three-Year Revenue Scenarios

| Scenario | Y1 ARR | Y2 ARR | Y3 ARR |
|----------|--------|--------|--------|
| Conservative | $600K | $1.8M | $4.5M |
| Base | $800K | $3.0M | $9.0M |
| Aggressive | $1.2M | $5.0M | $15.0M |

---

## 10. Related Documents

| Document | Relationship |
|----------|--------------|
| [PRICING-STRATEGY.md](./PRICING-STRATEGY.md) | Detailed pricing tiers |
| [UNIT-ECONOMICS.md](./UNIT-ECONOMICS.md) | LTV/CAC analysis |
| [FINANCIAL-PROJECTIONS.md](./FINANCIAL-PROJECTIONS.md) | Full P&L forecast |
| [BUSINESS-MODEL-CANVAS.md](./BUSINESS-MODEL-CANVAS.md) | Business model overview |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Business Team | Initial revenue model |

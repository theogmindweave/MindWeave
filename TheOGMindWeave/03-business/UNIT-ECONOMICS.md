# MindWeave Unit Economics

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Unit Economics Analysis |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Author | MindWeave Business Team |
| Status | Strategic |
| Classification | Confidential |

---

## 1. Executive Summary

### 1.1 Key Metrics Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      UNIT ECONOMICS DASHBOARD                            │
│                                                                         │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐     │
│   │   LTV : CAC      │  │   CAC PAYBACK    │  │   GROSS MARGIN   │     │
│   │                  │  │                  │  │                  │     │
│   │      4.2x        │  │   11 months      │  │      78%         │     │
│   │   (Target: >3x)  │  │  (Target: <18)   │  │  (Target: >70%)  │     │
│   └──────────────────┘  └──────────────────┘  └──────────────────┘     │
│                                                                         │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐     │
│   │      ARPA        │  │    LIFETIME      │  │    BLENDED CAC   │     │
│   │                  │  │                  │  │                  │     │
│   │   $1,200/mo      │  │   36 months      │  │     $10,000      │     │
│   │    ($14.4K ARR)  │  │   (3 years)      │  │                  │     │
│   └──────────────────┘  └──────────────────┘  └──────────────────┘     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Customer Acquisition Cost (CAC)

### 2.1 CAC Components

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          CAC BREAKDOWN                                   │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ SALES COSTS (55% of CAC)                                         │   │
│   │ ├── Sales rep salary (commission-weighted)      $3,500            │   │
│   │ ├── Sales engineering/demo support              $1,200            │   │
│   │ ├── Sales tools (CRM, prospecting)              $400              │   │
│   │ └── Travel & entertainment                      $400              │   │
│   │                                         Subtotal: $5,500          │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ MARKETING COSTS (45% of CAC)                                     │   │
│   │ ├── Paid acquisition (Google, LinkedIn)         $2,000            │   │
│   │ ├── Content marketing (amortized)               $800              │   │
│   │ ├── Events & conferences                        $700              │   │
│   │ └── Marketing tools & automation                $500              │   │
│   │                                         Subtotal: $4,000          │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ ONBOARDING COSTS (Included in CAC)                               │   │
│   │ ├── Implementation support                      $400              │   │
│   │ └── Training & documentation                    $100              │   │
│   │                                         Subtotal: $500            │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│                               TOTAL CAC: $10,000                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.2 CAC by Customer Tier

| Tier | Fully-Loaded CAC | Sales Motion | Cycle Length |
|------|------------------|--------------|--------------|
| Team | $3,000 | Product-led + light touch | 2-4 weeks |
| Pro | $12,000 | Inside sales | 6-10 weeks |
| Enterprise | $35,000 | Field sales | 12-20 weeks |
| **Blended** | **$10,000** | Mixed | 8 weeks avg |

### 2.3 CAC Efficiency Trends

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        CAC TREND (MONTHLY)                               │
│                                                                         │
│   CAC ($)                                                               │
│   15,000 ┤ ████                                                         │
│   14,000 ┤ ████ ████                                                    │
│   13,000 ┤ ████ ████ ████                                               │
│   12,000 ┤ ████ ████ ████ ████                                          │
│   11,000 ┤ ████ ████ ████ ████ ████                                     │
│   10,000 ┤ ████ ████ ████ ████ ████ ████                                │
│    9,000 ┤ ████ ████ ████ ████ ████ ████ ████                           │
│    8,000 ┤ ████ ████ ████ ████ ████ ████ ████ ████ ████                 │
│          └───────────────────────────────────────────────               │
│            M1   M3   M5   M7   M9   M11  M13  M15  M18                   │
│                                                                         │
│   Target: CAC declining 30% by Month 18 through:                        │
│   • Improved funnel conversion (15% → 25%)                              │
│   • Better content/SEO reducing paid spend                              │
│   • Faster sales cycles with refined process                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Customer Lifetime Value (LTV)

### 3.1 LTV Calculation

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        LTV CALCULATION                                   │
│                                                                         │
│   Formula: LTV = ARPA × Gross Margin × Customer Lifetime                │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                                                                  │   │
│   │   ARPA (Average Revenue Per Account)                             │   │
│   │   └── Monthly: $1,200                                            │   │
│   │   └── Annual: $14,400                                            │   │
│   │                                                                  │   │
│   │   GROSS MARGIN                                                   │   │
│   │   └── 78% (after infrastructure & support costs)                 │   │
│   │                                                                  │   │
│   │   CUSTOMER LIFETIME                                              │   │
│   │   └── 1 / Monthly Churn Rate = 1 / 2.8% = 36 months              │   │
│   │                                                                  │   │
│   │   ─────────────────────────────────────────────────────────────  │   │
│   │                                                                  │   │
│   │   LTV = $1,200 × 0.78 × 36 = $33,696                             │   │
│   │                                                                  │   │
│   │   Simplified: LTV ≈ $42,000 (with expansion revenue)             │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 LTV by Customer Tier

| Tier | Monthly ARPA | Lifetime (mo) | Gross Margin | LTV |
|------|--------------|---------------|--------------|-----|
| Team | $500 | 30 | 80% | $12,000 |
| Pro | $2,000 | 36 | 78% | $56,160 |
| Enterprise | $8,000 | 48 | 75% | $288,000 |
| **Blended** | **$1,200** | **36** | **78%** | **$42,000** |

### 3.3 LTV with Net Revenue Retention

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   LTV ADJUSTMENT FOR NRR                                 │
│                                                                         │
│   Base LTV (no expansion):     $33,696                                  │
│                                                                         │
│   With 120% NRR:                                                        │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                                                                  │   │
│   │   Year 1: $14,400 × 0.78 =                        $11,232        │   │
│   │   Year 2: $14,400 × 1.20 × 0.78 =                 $13,478        │   │
│   │   Year 3: $14,400 × 1.20 × 1.20 × 0.78 =          $16,174        │   │
│   │                                                                  │   │
│   │   3-Year LTV (with expansion):                    $40,884        │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   Adjusted LTV: ~$42,000 (rounding for Year 4+ residual value)          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. LTV:CAC Ratio Analysis

### 4.1 Overall LTV:CAC

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        LTV:CAC RATIO                                     │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                                                                  │   │
│   │         LTV        $42,000                                       │   │
│   │   ─────────────  = ─────────  =  4.2x                            │   │
│   │         CAC        $10,000                                       │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   Industry Benchmarks:                                                  │
│   ├── Poor: < 1x (losing money on every customer)                       │
│   ├── Minimum Viable: 1-3x (need improvement)                           │
│   ├── Good: 3-5x (healthy SaaS business)                                │
│   └── Excellent: > 5x (very efficient acquisition)                      │
│                                                                         │
│   MindWeave Status: GOOD ✓                                              │
│   Target Y2: 5.0x (through CAC reduction and LTV expansion)             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 LTV:CAC by Tier

| Tier | LTV | CAC | LTV:CAC | Health |
|------|-----|-----|---------|--------|
| Team | $12,000 | $3,000 | 4.0x | Good |
| Pro | $56,160 | $12,000 | 4.7x | Good |
| Enterprise | $288,000 | $35,000 | 8.2x | Excellent |

### 4.3 LTV:CAC Improvement Plan

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    LTV:CAC IMPROVEMENT ROADMAP                           │
│                                                                         │
│   Current: 4.2x                                                         │
│                                                                         │
│   CAC REDUCTION INITIATIVES                    Impact on Ratio          │
│   ├── Product-led growth motions               +0.3x                    │
│   ├── Content marketing / SEO investment       +0.2x                    │
│   ├── Referral program                         +0.2x                    │
│   └── Sales process optimization               +0.1x                    │
│                                                                         │
│   LTV EXPANSION INITIATIVES                                             │
│   ├── Improved onboarding (reduce churn)       +0.3x                    │
│   ├── Usage expansion features                 +0.2x                    │
│   ├── Premium support upsells                  +0.1x                    │
│   └── Cross-sell additional products           +0.2x                    │
│                                                                         │
│   Target Y2: 5.8x   Target Y3: 6.5x                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 5. CAC Payback Period

### 5.1 Payback Calculation

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      CAC PAYBACK PERIOD                                  │
│                                                                         │
│   Formula: CAC Payback = CAC / (ARPA × Gross Margin)                    │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                                                                  │   │
│   │           $10,000                                                │   │
│   │   ─────────────────────────  =  10.7 months ≈ 11 months          │   │
│   │     $1,200 × 0.78                                                │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   Industry Benchmarks:                                                  │
│   ├── SMB SaaS: 6-12 months (Good)                                      │
│   ├── Mid-Market SaaS: 12-18 months (Good)                              │
│   └── Enterprise SaaS: 18-24 months (Acceptable)                        │
│                                                                         │
│   MindWeave (Blended): 11 months = GOOD ✓                               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Payback by Tier

| Tier | ARPA | CAC | Gross Margin | Payback |
|------|------|-----|--------------|---------|
| Team | $500 | $3,000 | 80% | 7.5 months |
| Pro | $2,000 | $12,000 | 78% | 7.7 months |
| Enterprise | $8,000 | $35,000 | 75% | 5.8 months |

### 5.3 Payback Visualization

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CUMULATIVE MARGIN vs CAC                              │
│                                                                         │
│   $15,000 ┤                                            ┌───────────────  │
│           │                                       ────┘                  │
│   $10,000 ┤                              ────────┘                       │
│           │                     ────────┘ ← CAC Recovery Point (Mo 11)   │
│    $5,000 ┤            ────────┘                                         │
│           │    ────────┘                                                 │
│        $0 ┼────┘                                                         │
│           │                                                              │
│   -$5,000 │                                                              │
│           │                                                              │
│  -$10,000 ┤ ● CAC Investment ($10,000)                                   │
│           └─────────────────────────────────────────────────────────     │
│             0    3    6    9    12   15   18   Months                    │
│                                                                         │
│   ─── Cumulative Gross Margin                                           │
│   ─── CAC Recovery Point                                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Gross Margin Analysis

### 6.1 Gross Margin Breakdown

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      GROSS MARGIN STRUCTURE                              │
│                                                                         │
│   REVENUE                                              100%              │
│   │                                                                     │
│   └── COST OF GOODS SOLD (COGS)                        22%              │
│       │                                                                 │
│       ├── Cloud Infrastructure (AWS/GCP)               10%              │
│       │   ├── Compute                    5%                             │
│       │   ├── Storage                    2%                             │
│       │   ├── Network/CDN                2%                             │
│       │   └── Third-party services       1%                             │
│       │                                                                 │
│       ├── Customer Success (variable)                   8%              │
│       │   ├── Support tickets            4%                             │
│       │   ├── Onboarding assist          2%                             │
│       │   └── Technical support          2%                             │
│       │                                                                 │
│       └── Payment Processing                            4%              │
│           ├── Stripe fees                3%                             │
│           └── Billing operations         1%                             │
│                                                                         │
│   ═══════════════════════════════════════════════════════════════════   │
│                                                                         │
│   GROSS MARGIN                                         78%              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Gross Margin by Tier

| Tier | Revenue | Infrastructure | Support | Payment | Gross Margin |
|------|---------|----------------|---------|---------|--------------|
| Team | $500 | $40 (8%) | $50 (10%) | $10 (2%) | 80% |
| Pro | $2,000 | $200 (10%) | $160 (8%) | $80 (4%) | 78% |
| Enterprise | $8,000 | $1,000 (12.5%) | $600 (7.5%) | $400 (5%) | 75% |

### 6.3 Gross Margin Improvement Opportunities

```
┌─────────────────────────────────────────────────────────────────────────┐
│                 GROSS MARGIN IMPROVEMENT LEVERS                          │
│                                                                         │
│   Current: 78%   Target Y2: 80%   Target Y3: 82%                        │
│                                                                         │
│   INFRASTRUCTURE OPTIMIZATION                                           │
│   ├── Reserved instance commitments            -1% COGS                 │
│   ├── Multi-tier storage (hot/warm/cold)       -0.5% COGS               │
│   └── Edge caching improvements                -0.3% COGS               │
│                                                                         │
│   SUPPORT EFFICIENCY                                                    │
│   ├── Self-service knowledge base              -0.5% COGS               │
│   ├── AI-assisted support triage               -0.3% COGS               │
│   └── Improved documentation                   -0.2% COGS               │
│                                                                         │
│   PAYMENT OPTIMIZATION                                                  │
│   ├── Volume discount negotiations             -0.3% COGS               │
│   └── Annual payment incentives                -0.2% COGS               │
│                                                                         │
│   Total Potential Improvement: +3.3% Gross Margin                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Churn Economics

### 7.1 Churn Impact Analysis

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        CHURN ECONOMICS                                   │
│                                                                         │
│   Monthly Churn Rate: 2.8%                                              │
│   Annual Churn Rate: 1 - (1 - 0.028)^12 = 29%                           │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ COST OF CHURN                                                    │   │
│   │                                                                  │   │
│   │ Per Churned Customer:                                            │   │
│   │ ├── Lost remaining LTV:        ~$28,000                          │   │
│   │ ├── Wasted CAC (if early):     ~$10,000                          │   │
│   │ └── Reputation/referral loss:  ~$2,000 (estimated)               │   │
│   │                                                                  │   │
│   │ Total Cost: ~$40,000 per churned customer                        │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   With 100 customers and 29% annual churn:                              │
│   • 29 churned customers × $40,000 = $1.16M annual churn cost           │
│   • 1% churn reduction = $160K saved annually                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Churn by Cohort

| Tenure | Monthly Churn | Annual Churn | Notes |
|--------|---------------|--------------|-------|
| 0-3 months | 5.0% | 46% | Critical onboarding period |
| 3-6 months | 3.5% | 34% | Value realization phase |
| 6-12 months | 2.0% | 22% | Established users |
| 12+ months | 1.2% | 14% | Sticky customers |

### 7.3 Churn Reduction Investment

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CHURN REDUCTION ROI                                   │
│                                                                         │
│   INVESTMENT: $150K annually in retention programs                      │
│                                                                         │
│   PROGRAMS:                                                             │
│   ├── Proactive health scoring          $40K                            │
│   ├── Enhanced onboarding               $35K                            │
│   ├── Quarterly business reviews        $25K                            │
│   ├── Automated engagement campaigns    $25K                            │
│   └── At-risk intervention team         $25K                            │
│                                                                         │
│   EXPECTED OUTCOME:                                                     │
│   • Reduce churn from 29% → 20% annually                                │
│   • Save 9 customers per 100                                            │
│   • Value: 9 × $40,000 = $360K saved                                    │
│                                                                         │
│   ROI: ($360K - $150K) / $150K = 140%                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Cohort Analysis

### 8.1 Revenue Cohort Performance

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     COHORT REVENUE RETENTION                             │
│                                                                         │
│   % of Starting Revenue                                                 │
│                                                                         │
│   130% ┤                                   ████                         │
│   120% ┤                          ████     ████ ← Strong cohorts        │
│   110% ┤                 ████     ████     ████                         │
│   100% ┤ ████ ═══════════════════════════════════════════════           │
│    90% ┤ ████     ████                                                  │
│    80% ┤ ████     ████                                                  │
│    70% ┤ ████     ████ ← Early churn                                    │
│        └────────────────────────────────────────────────────            │
│          M1      M6      M12     M18     M24                            │
│                                                                         │
│   Key Insight: Customers surviving Month 6 show strong expansion        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Cohort Metrics by Quarter

| Cohort | Initial ARR | 6-mo ARR | 12-mo ARR | 12-mo NRR |
|--------|-------------|----------|-----------|-----------|
| Q1 2024 | $180K | $160K | $195K | 108% |
| Q2 2024 | $240K | $220K | $275K | 115% |
| Q3 2024 | $320K | $305K | $384K | 120% |
| Q4 2024 | $480K | $468K | - | Tracking |

---

## 9. Unit Economics by Channel

### 9.1 Channel Economics

| Channel | CAC | LTV | LTV:CAC | Payback | Volume % |
|---------|-----|-----|---------|---------|----------|
| Organic/SEO | $2,500 | $38,000 | 15.2x | 3 mo | 15% |
| Content/Inbound | $6,000 | $40,000 | 6.7x | 6 mo | 25% |
| Paid Acquisition | $15,000 | $35,000 | 2.3x | 16 mo | 20% |
| Outbound Sales | $18,000 | $55,000 | 3.1x | 12 mo | 25% |
| Referrals | $3,500 | $48,000 | 13.7x | 4 mo | 10% |
| Partners | $8,000 | $42,000 | 5.3x | 9 mo | 5% |

### 9.2 Channel Optimization Strategy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CHANNEL MIX OPTIMIZATION                              │
│                                                                         │
│   Current Mix            Target Mix (Y2)         Impact                 │
│                                                                         │
│   Organic: 15%    →      Organic: 25%            CAC -$1,200            │
│   Content: 25%    →      Content: 30%            CAC -$400              │
│   Paid: 20%       →      Paid: 10%               CAC -$1,000            │
│   Outbound: 25%   →      Outbound: 15%           CAC -$400              │
│   Referral: 10%   →      Referral: 15%           CAC -$600              │
│   Partner: 5%     →      Partner: 5%             CAC $0                 │
│                                                                         │
│   Net CAC Reduction: -$3,600 (36% improvement)                          │
│   Blended CAC Target: $6,400                                            │
│   New LTV:CAC: 6.6x                                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 10. Unit Economics Targets

### 10.1 Three-Year Trajectory

| Metric | Current | Y1 Target | Y2 Target | Y3 Target |
|--------|---------|-----------|-----------|-----------|
| Blended CAC | $10,000 | $9,000 | $7,500 | $6,500 |
| Blended LTV | $42,000 | $45,000 | $52,000 | $60,000 |
| LTV:CAC | 4.2x | 5.0x | 6.9x | 9.2x |
| Payback (mo) | 11 | 10 | 8 | 6 |
| Gross Margin | 78% | 79% | 81% | 83% |
| Monthly Churn | 2.8% | 2.3% | 1.8% | 1.5% |

### 10.2 World-Class Benchmarks

```
┌─────────────────────────────────────────────────────────────────────────┐
│               MINDWEAVE vs WORLD-CLASS SAAS BENCHMARKS                   │
│                                                                         │
│                        MindWeave    Top Quartile   Gap                  │
│   ─────────────────────────────────────────────────────────────────     │
│   LTV:CAC               4.2x          5.0x        -0.8x                 │
│   CAC Payback           11 mo         10 mo       -1 mo                 │
│   Gross Margin          78%           82%         -4%                   │
│   Net Revenue Retention 120%          125%        -5%                   │
│   Logo Retention        71%           85%         -14%                  │
│   ─────────────────────────────────────────────────────────────────     │
│                                                                         │
│   Priority Gap: Logo Retention (biggest room for improvement)           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 11. Related Documents

| Document | Relationship |
|----------|--------------|
| [REVENUE-MODEL.md](./REVENUE-MODEL.md) | Revenue streams detail |
| [PRICING-STRATEGY.md](./PRICING-STRATEGY.md) | Pricing tiers |
| [FINANCIAL-PROJECTIONS.md](./FINANCIAL-PROJECTIONS.md) | Full P&L |
| [BURN-RATE.md](./BURN-RATE.md) | Cost structure |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Business Team | Initial unit economics analysis |

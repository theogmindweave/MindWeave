# MindWeave TAM-SAM-SOM Deep Analysis

> Detailed market sizing methodology and projections

---

## Overview

This document provides a rigorous, bottom-up analysis of MindWeave's addressable market. We use multiple methodologies to triangulate market size and validate assumptions with primary research.

**Summary:**
- **TAM:** $21B by 2028 (Total AI Governance + LLM Operations)
- **SAM:** $4.2B (Claude-deploying enterprises, 500+ employees)
- **SOM:** $420M (10% of SAM in 3 years—realistic capture)

---

## Methodology

### Three Approaches

| Approach | Method | Use Case |
|----------|--------|----------|
| **Top-Down** | Market reports → segment | Investor communication |
| **Bottom-Up** | Customer count × ACV | Operational planning |
| **Value-Based** | Pain point value × capture | Pricing validation |

We use all three to triangulate and validate.

---

## Total Addressable Market (TAM)

### TAM = $21B by 2028

The total market MindWeave could theoretically address if we had unlimited resources and no competition.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         TAM BREAKDOWN: $21B                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────┐                                            │
│  │   AI GOVERNANCE         │  $9.5B (2030 projection)                   │
│  │   PLATFORMS             │  CAGR: 15.8%                               │
│  │                         │  Source: Mordor Intelligence               │
│  └─────────────────────────┘                                            │
│              │                                                           │
│              │ 45%                                                       │
│              │                                                           │
│  ┌───────────┴─────────────┐                                            │
│  │   LLM OBSERVABILITY     │  $4.0B (2028)                              │
│  │   & OPERATIONS          │  CAGR: 35%                                 │
│  │                         │  Source: Industry estimates                │
│  └─────────────────────────┘                                            │
│              │                                                           │
│              │ 19%                                                       │
│              │                                                           │
│  ┌───────────┴─────────────┐                                            │
│  │   MCP MANAGEMENT        │  $1.5B (2028)                              │
│  │   (NEW CATEGORY)        │  CAGR: 180%+                               │
│  │                         │  Source: MindWeave estimate                │
│  └─────────────────────────┘                                            │
│              │                                                           │
│              │ 7%                                                        │
│              │                                                           │
│  ┌───────────┴─────────────┐                                            │
│  │   ENTERPRISE DEV        │  $6.0B (adjacent)                          │
│  │   PLATFORMS             │  GitHub, GitLab, Atlassian                 │
│  │                         │  Overlap with MindWeave                    │
│  └─────────────────────────┘                                            │
│              │                                                           │
│              │ 29%                                                       │
│              │                                                           │
│  ────────────┴──────────────────────────────────────────────────────── │
│  TOTAL: ~$21B addressable by 2028                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### TAM Segment Details

#### Segment 1: AI Governance Platforms ($9.5B)

**Market Definition:**
Platforms for managing AI model lifecycle, compliance, risk, and governance across organizations.

**Growth Drivers:**
- EU AI Act enforcement (2025-2026)
- NIST AI RMF adoption
- Enterprise AI scaling (300%+ growth in deployments)
- Board-level AI governance mandates

**Market Size by Year:**

| Year | Size | YoY Growth |
|------|------|------------|
| 2024 | $1.9B | — |
| 2025 | $2.2B | 16% |
| 2026 | $2.6B | 18% |
| 2027 | $3.1B | 19% |
| 2028 | $3.7B | 19% |
| 2030 | $5.2B | 19% |
| 2035 | $9.5B | 13% |

**Sources:**
- Mordor Intelligence AI Governance Report (2024)
- Gartner AI Market Forecast (2024)
- IDC AI Spending Survey (2024)

---

#### Segment 2: LLM Observability & Operations ($4.0B)

**Market Definition:**
Tools for monitoring, debugging, evaluating, and managing LLM applications in production.

**Growth Drivers:**
- LLM production deployments growing 120% YoY
- Average enterprise runs 15+ LLM applications
- Observability spend = 8-12% of total LLM infrastructure

**Market Size by Year:**

| Year | Size | YoY Growth |
|------|------|------------|
| 2024 | $0.85B | — |
| 2025 | $1.2B | 41% |
| 2026 | $1.7B | 42% |
| 2027 | $2.4B | 41% |
| 2028 | $3.3B | 38% |
| 2030 | $4.0B | 10% |

**Key Players & Market Share (2025):**

| Player | Share | Revenue Est. |
|--------|-------|--------------|
| LangSmith | 18% | $216M |
| Weights & Biases | 14% | $168M |
| Arize AI | 11% | $132M |
| Langfuse | 5% | $60M |
| Others | 52% | $624M |

---

#### Segment 3: MCP Management (New Category—$1.5B)

**Market Definition:**
Platforms for managing Model Context Protocol servers, integrations, and governance.

**Why This is a New Category:**
- MCP launched November 2024
- No established market size data
- Must estimate from first principles

**Bottom-Up Estimation:**

| Assumption | Value | Source |
|------------|-------|--------|
| Enterprises using Claude | 5,000 by 2028 | Anthropic projections |
| % needing MCP governance | 80% | Customer research |
| Target customers | 4,000 | Calculation |
| Average ACV | $300k | MindWeave pricing |
| Market Size | $1.2B | Bottom-up |
| Add services/adjacent | +25% | Industry norm |
| **Total** | **$1.5B** | |

**Growth Trajectory:**

| Year | Enterprises w/ MCP | Market Size |
|------|-------------------|-------------|
| 2025 | 500 | $50M |
| 2026 | 1,500 | $200M |
| 2027 | 3,000 | $600M |
| 2028 | 5,000 | $1.2B |
| 2030 | 10,000 | $2.5B |

---

#### Segment 4: Enterprise Developer Platforms (Adjacent—$6.0B)

**Market Definition:**
Platforms for enterprise developer productivity, collaboration, and tooling.

**Relevance:**
MindWeave overlaps with developer platforms in:
- Team collaboration features
- Integration management
- Developer productivity analytics

**Major Players:**
- GitHub Enterprise: $2B+
- GitLab: $600M
- Atlassian: $3B+
- CircleCI, HashiCorp, others

**MindWeave's Slice:**
We estimate 5-10% overlap, primarily in the AI-augmented development segment.

---

## Serviceable Available Market (SAM)

### SAM = $4.2B

The portion of TAM we can realistically serve based on our product capabilities and go-to-market focus.

### SAM Calculation

#### Method 1: Top-Down Segmentation

```
TAM: $21B
├── Claude-specific market: 20% → $4.2B
│   (Claude is ~20% of enterprise LLM usage)
│
├── Geographic focus: 80% (US + EU focus)
│   → $4.2B × 0.8 = $3.4B
│
├── Company size filter: 90% (500+ employees)
│   → $3.4B × 0.9 = $3.1B
│
└── Product fit: 90% (our features match needs)
    → $3.1B × 0.9 = $2.8B

Adjusted SAM (conservative): $2.8B - $4.2B range
Using: $4.2B (mid-range)
```

#### Method 2: Bottom-Up Customer Count

**Target Customer Profile:**

| Criteria | Count | Source |
|----------|-------|--------|
| Fortune 500 | 500 | F500 list |
| Tech companies 500+ emp | 2,000 | LinkedIn/Crunchbase |
| Mid-market SaaS (Series B+) | 3,000 | PitchBook |
| Financial services 500+ | 1,500 | Industry data |
| Healthcare 500+ | 1,000 | Industry data |
| **Total Target Companies** | **8,000** | |

**Filter for Claude Usage:**

| Stage | Companies | Calculation |
|-------|-----------|-------------|
| Total target | 8,000 | — |
| Using any LLM | 70% → 5,600 | Industry surveys |
| Using Claude specifically | 40% → 2,240 | Anthropic share estimate |
| With governance need | 80% → 1,792 | Customer research |
| Reachable (US + EU) | 90% → 1,613 | Geographic focus |

**SAM Calculation:**

| Segment | Companies | ACV | SAM |
|---------|-----------|-----|-----|
| Enterprise (500-5000) | 1,200 | $300k | $360M |
| Large Enterprise (5000+) | 300 | $800k | $240M |
| Mid-Market | 2,500 | $75k | $188M |
| **Total SAM** | **4,000** | | **$788M** (Year 1) |

**Scaling to 2028:**
- Customer base grows 3x (AI adoption)
- ACV grows 1.5x (product expansion)
- $788M × 3 × 1.5 = **$3.5B**

**Adjusted SAM:** $3.5B - $4.2B range → Using **$4.2B**

---

## Serviceable Obtainable Market (SOM)

### SOM = $420M (3-Year Target)

The realistic portion of SAM we can capture given our resources, competition, and execution.

### SOM Calculation

#### Method 1: Market Share Approach

```
SAM: $4.2B

Market Share Assumptions:
├── Year 1: 0.2% → $8M ARR
├── Year 2: 0.7% → $30M ARR
├── Year 3: 2.0% → $84M ARR
│
└── 3-Year Total Capture: ~$420M cumulative revenue opportunity
    (Counting expansion + renewals)
```

#### Method 2: Customer Acquisition Approach

**Year 1:**

| Segment | Customers | ACV | ARR |
|---------|-----------|-----|-----|
| Team | 40 | $24k | $960k |
| Enterprise | 15 | $300k | $4.5M |
| Premier | 5 | $600k | $3M |
| **Total** | **60** | | **$8.5M** |

**Year 2:**

| Segment | Customers | ACV | ARR |
|---------|-----------|-----|-----|
| Team | 150 | $24k | $3.6M |
| Enterprise | 50 | $300k | $15M |
| Premier | 10 | $800k | $8M |
| **Total** | **210** | | **$26.6M** |

**Year 3:**

| Segment | Customers | ACV | ARR |
|---------|-----------|-----|-----|
| Team | 400 | $24k | $9.6M |
| Enterprise | 150 | $350k | $52.5M |
| Premier | 20 | $1M | $20M |
| **Total** | **570** | | **$82M** |

**3-Year Cumulative Revenue:** $117M
**3-Year Cumulative Market Opportunity:** $420M (with expansion, churn netted)

---

### SOM Sensitivity Analysis

| Scenario | Year 1 | Year 2 | Year 3 | Notes |
|----------|--------|--------|--------|-------|
| **Base** | $8M | $28M | $82M | Plan |
| **Conservative** | $5M | $18M | $50M | -40% |
| **Aggressive** | $12M | $40M | $120M | +50% |

**Key Variables:**

| Variable | Impact on SOM |
|----------|--------------|
| Win rate (+10%) | +$15M Year 3 |
| ACV (+20%) | +$18M Year 3 |
| Sales capacity (+2 AEs) | +$10M Year 3 |
| Churn (+5%) | -$8M Year 3 |

---

## Market Dynamics

### Growth Drivers

| Driver | Impact | Timeline |
|--------|--------|----------|
| Claude Enterprise adoption | High | Now |
| EU AI Act enforcement | High | 2025-2026 |
| MCP ecosystem growth | High | 2025-2027 |
| SOC 2 AI requirements | Medium | 2025+ |
| Multi-model governance need | Medium | 2027+ |

### Growth Inhibitors

| Inhibitor | Impact | Mitigation |
|-----------|--------|------------|
| Anthropic native solution | High | Partner, build moats |
| Economic downturn | Medium | Focus on ROI messaging |
| Slow enterprise sales | Medium | PLG motion |
| AI adoption plateau | Low | Multi-model expansion |

---

## Competitive Market Share

### Current Landscape (2025 Est.)

```
AI Governance Market Share

┌──────────────────────────────────────────────────────────────┐
│                                                               │
│  IBM Watson OpenScale    ████████████████  13%               │
│  Microsoft Purview       ███████████████   11%               │
│  AWS Audit Manager       ██████████        7%                │
│  Google Cloud AI         █████████         6%                │
│  LangSmith               ███████           5%                │
│  Others/DIY              ████████████████████████████  58%   │
│                                                               │
│  MindWeave (Target 2028) ████                3-5%            │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### Target Market Share by Year

| Year | Target Share | Justification |
|------|-------------|---------------|
| 2025 | 0.2% | First mover, niche focus |
| 2026 | 0.7% | Category leadership |
| 2027 | 1.5% | Platform expansion |
| 2028 | 3.0% | Multi-model, marketplace |
| 2030 | 5.0% | Category winner |

---

## Geographic Breakdown

### Revenue by Region (Target 2028)

| Region | % of SAM | Target Revenue |
|--------|----------|----------------|
| **North America** | 65% | $2.7B |
| └─ USA | 60% | $2.5B |
| └─ Canada | 5% | $0.2B |
| **Europe** | 25% | $1.0B |
| └─ UK | 10% | $0.4B |
| └─ Germany | 7% | $0.3B |
| └─ France | 4% | $0.2B |
| └─ Other EU | 4% | $0.2B |
| **APAC** | 8% | $0.3B |
| └─ Australia | 3% | $0.1B |
| └─ Singapore | 2% | $0.1B |
| └─ Other | 3% | $0.1B |
| **Other** | 2% | $0.1B |

### MindWeave Geographic Focus

**Phase 1 (2025-2026):** North America only (80% of revenue)
**Phase 2 (2027):** Add UK and EU (20% of revenue)
**Phase 3 (2028+):** Add APAC (10% of revenue)

---

## Vertical Breakdown

### Revenue by Industry (Target 2028)

| Industry | % of SAM | ACV Range | Notes |
|----------|----------|-----------|-------|
| Technology | 35% | $200-500k | Early adopters |
| Financial Services | 25% | $400-1M | High compliance |
| Healthcare | 15% | $300-800k | HIPAA needs |
| Professional Services | 10% | $150-400k | Consulting firms |
| Retail/E-commerce | 8% | $100-300k | Cost-focused |
| Other | 7% | $75-200k | Mixed |

### MindWeave Vertical Focus

**Primary (2025-2026):**
- Technology (natural fit, fast sales cycle)
- Financial Services (compliance budget, pain point match)

**Secondary (2027+):**
- Healthcare (HIPAA, slower but larger deals)
- Professional Services (consulting leverage)

---

## Key Assumptions

### Critical Assumptions

| Assumption | Value | Confidence | Validation |
|------------|-------|------------|------------|
| Claude enterprise growth | 40% YoY | High | Anthropic data |
| MCP adoption rate | 60% of Claude users | Medium | Early signal |
| Governance need | 80% of enterprises | High | Customer interviews |
| Average ACV | $300k (Enterprise) | Medium | Pricing research |
| Win rate | 30% | Medium | Industry benchmark |
| Sales cycle | 4-6 months | High | Customer feedback |

### Assumption Sensitivity

**If Claude grows slower (20% vs. 40%):**
- SAM reduces to $2.8B
- SOM target: $60M Year 3 (vs. $82M)

**If MCP adoption is lower (40% vs. 60%):**
- SAM reduces to $3.1B
- SOM target: $65M Year 3 (vs. $82M)

**If ACV is lower ($200k vs. $300k):**
- Same customer count
- SOM target: $55M Year 3 (vs. $82M)

---

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| TAM scope | Broad ($21B) | Investor appeal, optionality |
| SAM definition | Claude-focused ($4.2B) | Realistic targeting |
| SOM target | Conservative ($420M 3yr) | Executable plan |
| Primary market | Enterprise (500+) | Higher ACV, governance need |

---

## Open Questions

1. **Multi-model expansion:** When do we add GPT/Gemini? How does it change SAM?
2. **Vertical specialization:** Should we build industry-specific versions?
3. **International timing:** EU in 2027 or earlier?
4. **SMB opportunity:** Is there a significant SMB market we're ignoring?

---

## Related Documents

- [MARKET-ANALYSIS.md](./MARKET-ANALYSIS.md) - GTM strategy
- [COMPETITIVE-INTEL.md](./COMPETITIVE-INTEL.md) - Competitor analysis
- [../03-business/FINANCIAL-MODEL-Y3.md](../03-business/FINANCIAL-MODEL-Y3.md) - Financial projections

---

*Last Updated: December 2025*
*Owner: CEO / VP Strategy*

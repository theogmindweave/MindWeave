# MindWeave ICP & Buyer Personas

## Document Information

| Field | Value |
|-------|-------|
| Document Title | Ideal Customer Profile & Buyer Personas |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Author | MindWeave GTM Team |
| Status | Active |
| Classification | Internal |

---

## 1. Ideal Customer Profile (ICP)

### 1.1 ICP Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    IDEAL CUSTOMER PROFILE                                │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                    FIRMOGRAPHICS                                 │   │
│   │                                                                  │   │
│   │   Company Size:      50-5,000 employees                          │   │
│   │   Revenue:           $10M - $500M                                │   │
│   │   Engineering Team:  20-500 developers                           │   │
│   │   Funding Stage:     Series A+ or profitable                     │   │
│   │   Geography:         North America, Europe (English-speaking)    │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                    TECHNOGRAPHICS                                │   │
│   │                                                                  │   │
│   │   AI Stack:          Claude API active usage                     │   │
│   │   Claude Users:      10+ developers using Claude                 │   │
│   │   MCP Adoption:      Exploring or using MCP tools                │   │
│   │   Cloud Provider:    AWS, GCP, or Azure                          │   │
│   │   Dev Tools:         Modern toolchain (Git, CI/CD)               │   │
│   │   Auth:              SSO (Okta, Azure AD, etc.)                   │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                    BEHAVIORAL                                    │   │
│   │                                                                  │   │
│   │   Pain Level:        Experiencing governance challenges          │   │
│   │   AI Maturity:       Early majority to late majority             │   │
│   │   Decision Speed:    2-8 week buying cycle                       │   │
│   │   Budget:            Has budget for developer tools              │   │
│   │   Innovation:        Open to new solutions                       │   │
│   │                                                                  │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 ICP Scoring Matrix

| Factor | Weight | Criteria | Score |
|--------|--------|----------|-------|
| Claude Usage | 30% | 10+ users = 10, 5-10 = 5, <5 = 0 | 0-10 |
| Company Size | 20% | 100-1000 = 10, 50-100 = 7, >1000 = 5 | 0-10 |
| Industry Fit | 15% | Tech = 10, Regulated = 8, Other = 5 | 0-10 |
| Budget Signal | 15% | Funded/profitable = 10, Pre-rev = 3 | 0-10 |
| Growth Stage | 10% | Scaling AI = 10, Early = 5, Mature = 7 | 0-10 |
| Geographic | 10% | US = 10, EU = 8, Other = 5 | 0-10 |

**ICP Score Thresholds:**
- 80-100: Tier 1 (Ideal) - Prioritize
- 60-79: Tier 2 (Good Fit) - Pursue
- 40-59: Tier 3 (Potential) - Nurture
- <40: Not ICP - Deprioritize

### 1.3 Target Industries

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TARGET INDUSTRY SEGMENTS                              │
│                                                                         │
│   TIER 1: PRIMARY (70% of focus)                                        │
│   ─────────────────────────────────────────────────────────────────     │
│                                                                         │
│   Technology / SaaS                                                     │
│   • Why: Early Claude adopters, developer-centric                       │
│   • Company examples: Developer tools, B2B SaaS, AI startups            │
│   • Budget: High willingness to pay for productivity                    │
│   • Decision: CTO/VP Engineering led                                    │
│                                                                         │
│   AI-First Startups                                                     │
│   • Why: Core Claude users, scaling rapidly                             │
│   • Company examples: AI applications, ML platforms                     │
│   • Budget: VC-funded, growth-focused                                   │
│   • Decision: Fast, founder-driven                                      │
│                                                                         │
│   TIER 2: SECONDARY (20% of focus)                                      │
│   ─────────────────────────────────────────────────────────────────     │
│                                                                         │
│   Financial Services                                                    │
│   • Why: Strong compliance needs, large budgets                         │
│   • Company examples: Fintech, banks, insurance                         │
│   • Budget: Large but careful procurement                               │
│   • Decision: CISO/CTO + procurement                                    │
│                                                                         │
│   Healthcare / Life Sciences                                            │
│   • Why: HIPAA, FDA compliance drivers                                  │
│   • Company examples: Healthtech, pharma, biotech                       │
│   • Budget: Compliance-justified spending                               │
│   • Decision: Security + compliance led                                 │
│                                                                         │
│   TIER 3: OPPORTUNISTIC (10% of focus)                                  │
│   ─────────────────────────────────────────────────────────────────     │
│                                                                         │
│   Professional Services                                                 │
│   • Why: Consulting firms using AI for clients                          │
│                                                                         │
│   Education / Research                                                  │
│   • Why: Academic AI research, learning institutions                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Buyer Personas

### 2.1 Primary Persona: The Engineering Manager

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PERSONA: THE ENGINEERING MANAGER                      │
│                    "Emily, Engineering Manager"                          │
│                                                                         │
│   DEMOGRAPHICS                                                          │
│   ─────────────────────────────────────────────────────────────────     │
│   Title:        Engineering Manager / Tech Lead                         │
│   Age:          28-38                                                   │
│   Experience:   5-10 years in engineering                               │
│   Team Size:    5-15 direct reports                                     │
│   Reports To:   VP Engineering or CTO                                   │
│                                                                         │
│   GOALS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • Ship features faster with AI assistance                             │
│   • Keep team productive and happy                                      │
│   • Control costs within budget                                         │
│   • Look good to leadership                                             │
│                                                                         │
│   PAINS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • "I have no idea what my team is building with Claude"               │
│   • "Our AI costs are unpredictable and hard to justify"                │
│   • "Different developers use different tools - it's chaos"             │
│   • "I can't answer leadership questions about AI ROI"                  │
│                                                                         │
│   BUYING BEHAVIOR                                                       │
│   ─────────────────────────────────────────────────────────────────     │
│   Role:         Champion / Initiator                                    │
│   Budget:       Can approve <$5K, needs approval above                  │
│   Research:     Technical blogs, Twitter, peer recommendations          │
│   Decision:     Wants to try before buying                              │
│   Timeline:     Can move fast if sees clear value                       │
│                                                                         │
│   MESSAGING                                                             │
│   ─────────────────────────────────────────────────────────────────     │
│   Hook:         "See what your team is building with Claude"            │
│   Value Prop:   "Complete visibility in 5 minutes"                      │
│   Proof:        Usage dashboards, cost savings examples                 │
│   CTA:          "Start free trial"                                      │
│                                                                         │
│   CHANNELS                                                              │
│   ─────────────────────────────────────────────────────────────────     │
│   • Twitter / X (engineering community)                                 │
│   • Hacker News                                                         │
│   • Technical blogs (dev.to, Medium)                                    │
│   • Engineering podcasts                                                │
│   • Peer recommendations                                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Economic Buyer: VP Engineering / CTO

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PERSONA: VP ENGINEERING / CTO                         │
│                    "David, VP of Engineering"                            │
│                                                                         │
│   DEMOGRAPHICS                                                          │
│   ─────────────────────────────────────────────────────────────────     │
│   Title:        VP Engineering / CTO / Director of Engineering          │
│   Age:          35-50                                                   │
│   Experience:   12-20 years, management track                           │
│   Team Size:    30-200 engineers                                        │
│   Reports To:   CEO / COO                                               │
│                                                                         │
│   GOALS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • Scale engineering output efficiently                                │
│   • Manage costs while enabling innovation                              │
│   • Reduce risk and ensure compliance                                   │
│   • Build organizational capabilities                                   │
│                                                                         │
│   PAINS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • "AI adoption is growing but governance isn't"                       │
│   • "I can't justify AI spend to the board without data"                │
│   • "Shadow AI usage creates security and compliance risk"              │
│   • "We need to standardize without killing innovation"                 │
│                                                                         │
│   BUYING BEHAVIOR                                                       │
│   ─────────────────────────────────────────────────────────────────     │
│   Role:         Economic Buyer / Final Decision Maker                   │
│   Budget:       Can approve $25K-100K+                                  │
│   Research:     Peer networks, analyst reports, board pressure          │
│   Decision:     Needs business case, champion validation                │
│   Timeline:     Quarterly budget cycles                                 │
│                                                                         │
│   MESSAGING                                                             │
│   ─────────────────────────────────────────────────────────────────     │
│   Hook:         "Govern AI at scale without slowing innovation"         │
│   Value Prop:   "Single control plane for enterprise Claude"            │
│   Proof:        Enterprise customers, compliance certifications         │
│   CTA:          "Schedule executive briefing"                           │
│                                                                         │
│   CHANNELS                                                              │
│   ─────────────────────────────────────────────────────────────────     │
│   • LinkedIn                                                            │
│   • Industry conferences                                                │
│   • Peer networks (CTO forums)                                          │
│   • Executive briefings                                                 │
│   • Analyst recommendations                                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Security Stakeholder: CISO

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PERSONA: CISO / SECURITY LEAD                         │
│                    "Sarah, Chief Information Security Officer"           │
│                                                                         │
│   DEMOGRAPHICS                                                          │
│   ─────────────────────────────────────────────────────────────────     │
│   Title:        CISO / VP Security / Security Director                  │
│   Age:          38-55                                                   │
│   Experience:   15+ years in security                                   │
│   Team Size:    5-30 security team                                      │
│   Reports To:   CEO / CIO                                               │
│                                                                         │
│   GOALS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • Protect the organization from AI-related risks                      │
│   • Ensure regulatory compliance                                        │
│   • Enable business with appropriate controls                           │
│   • Maintain visibility into all AI systems                             │
│                                                                         │
│   PAINS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • "I don't know where AI is being used or what data it sees"          │
│   • "We have no audit trail for AI activities"                          │
│   • "EU AI Act is coming and we're not ready"                           │
│   • "Shadow AI is my worst nightmare"                                   │
│                                                                         │
│   BUYING BEHAVIOR                                                       │
│   ─────────────────────────────────────────────────────────────────     │
│   Role:         Blocker or Influencer                                   │
│   Budget:       Controls security budget                                │
│   Research:     Security vendor evaluations, compliance requirements    │
│   Decision:     Veto power, security questionnaire required             │
│   Timeline:     Tied to compliance deadlines                            │
│                                                                         │
│   MESSAGING                                                             │
│   ─────────────────────────────────────────────────────────────────     │
│   Hook:         "Complete audit trail for every AI interaction"         │
│   Value Prop:   "Enterprise-grade AI governance and compliance"         │
│   Proof:        SOC 2, security architecture, audit capabilities        │
│   CTA:          "Request security review"                               │
│                                                                         │
│   CHANNELS                                                              │
│   ─────────────────────────────────────────────────────────────────     │
│   • Security conferences (RSA, Black Hat)                               │
│   • CISO networks and forums                                            │
│   • Compliance webinars                                                 │
│   • Analyst reports (Gartner, Forrester)                                │
│   • Peer recommendations                                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.4 Finance Stakeholder: CFO

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PERSONA: CFO / FINANCE LEADER                         │
│                    "Michael, Chief Financial Officer"                    │
│                                                                         │
│   DEMOGRAPHICS                                                          │
│   ─────────────────────────────────────────────────────────────────     │
│   Title:        CFO / VP Finance / Controller                           │
│   Age:          40-55                                                   │
│   Experience:   15+ years in finance                                    │
│   Reports To:   CEO / Board                                             │
│                                                                         │
│   GOALS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • Control and predict costs                                           │
│   • Enable growth with responsible spending                             │
│   • Attribute costs to business units                                   │
│   • Report accurate financials                                          │
│                                                                         │
│   PAINS                                                                 │
│   ─────────────────────────────────────────────────────────────────     │
│   • "AI costs are the fastest growing line item"                        │
│   • "I can't attribute AI spend to departments"                         │
│   • "We had 3 surprise bills last quarter"                              │
│   • "I need predictability for board reporting"                         │
│                                                                         │
│   BUYING BEHAVIOR                                                       │
│   ─────────────────────────────────────────────────────────────────     │
│   Role:         Influencer / Budget Gatekeeper                          │
│   Budget:       Approves all significant purchases                      │
│   Research:     ROI analysis, cost comparisons                          │
│   Decision:     Needs clear ROI and payback                             │
│   Timeline:     Budget cycles, fiscal year planning                     │
│                                                                         │
│   MESSAGING                                                             │
│   ─────────────────────────────────────────────────────────────────     │
│   Hook:         "Predict and control AI costs"                          │
│   Value Prop:   "35% average reduction in Claude spend"                 │
│   Proof:        ROI calculator, customer savings data                   │
│   CTA:          "See ROI analysis"                                      │
│                                                                         │
│   CHANNELS                                                              │
│   ─────────────────────────────────────────────────────────────────     │
│   • CFO networks                                                        │
│   • Finance publications                                                │
│   • ROI-focused content                                                 │
│   • Executive briefings                                                 │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Buying Committee Map

### 3.1 Typical Buying Committee

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    BUYING COMMITTEE STRUCTURE                            │
│                                                                         │
│                         ┌───────────────┐                               │
│                         │     CEO       │                               │
│                         │  (Exec Sponsor│                               │
│                         │   - large deals)                              │
│                         └───────┬───────┘                               │
│                                 │                                       │
│         ┌───────────────────────┼───────────────────────┐               │
│         │                       │                       │               │
│         v                       v                       v               │
│   ┌───────────┐          ┌───────────┐          ┌───────────┐          │
│   │   CTO/    │          │   CISO    │          │   CFO     │          │
│   │ VP Eng    │          │           │          │           │          │
│   │(Economic  │          │(Technical │          │ (Budget   │          │
│   │ Buyer)    │          │ Validator)│          │ Approver) │          │
│   └─────┬─────┘          └─────┬─────┘          └───────────┘          │
│         │                      │                                        │
│         │                      │                                        │
│         v                      v                                        │
│   ┌───────────┐          ┌───────────┐                                  │
│   │   Eng     │          │  Security │                                  │
│   │ Manager   │          │  Engineer │                                  │
│   │(Champion) │          │(Technical │                                  │
│   │           │          │ Evaluator)│                                  │
│   └───────────┘          └───────────┘                                  │
│                                                                         │
│   DEAL SIZE DYNAMICS                                                    │
│   ─────────────────────────────────────────────────────────────────     │
│   Team (<$10K):    Champion + Manager approval                          │
│   Pro ($10-50K):   + CTO/VP Eng approval                                │
│   Enterprise (>$50K): + CISO review + CFO/CEO visibility                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Multi-Threading Strategy

| Persona | Role | Engagement Strategy |
|---------|------|---------------------|
| Eng Manager | Champion | Build excitement, enable internal selling |
| CTO/VP Eng | Economic Buyer | ROI presentation, executive briefing |
| CISO | Validator | Security review, compliance discussion |
| CFO | Budget Approver | ROI analysis, cost savings data |
| Developers | End Users | Trial adoption, product feedback |

---

## 4. Anti-Personas (Who NOT to Sell To)

### 4.1 Poor Fit Signals

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ANTI-PERSONAS: WHO TO AVOID                           │
│                                                                         │
│   RED FLAGS                                                             │
│   ─────────────────────────────────────────────────────────────────     │
│                                                                         │
│   "THE NON-ADOPTER"                                                     │
│   • Not using Claude or considering it                                  │
│   • "We use ChatGPT/OpenAI exclusively"                                 │
│   • No plans to expand AI usage                                         │
│   → Why avoid: No product fit                                           │
│                                                                         │
│   "THE TINY TEAM"                                                       │
│   • <5 developers total                                                 │
│   • Solo founder or very early stage                                    │
│   • No budget for tools                                                 │
│   → Why avoid: Economics don't work                                     │
│                                                                         │
│   "THE DIY BUILDER"                                                     │
│   • "We'll build this ourselves"                                        │
│   • Large platform team with bandwidth                                  │
│   • NIH (Not Invented Here) culture                                     │
│   → Why avoid: Long sales cycle, likely to churn                        │
│                                                                         │
│   "THE PRICE SHOPPER"                                                   │
│   • Only focused on lowest cost                                         │
│   • No appreciation for value                                           │
│   • Excessive negotiation                                               │
│   → Why avoid: Poor LTV, support-heavy                                  │
│                                                                         │
│   "THE ENTERPRISE BUREAUCRACY"                                          │
│   • 18+ month procurement cycles                                        │
│   • Requires excessive customization                                    │
│   • RFP-only purchasing                                                 │
│   → Why avoid: Too early for complex enterprise                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Disqualification Questions

| Question | Disqualify If |
|----------|---------------|
| "Are you using Claude today?" | No, and no plans |
| "How many developers use Claude?" | <5 and not growing |
| "Do you have budget for this?" | "Looking for free" |
| "What's your decision timeline?" | >6 months |
| "Who else would be involved?" | "I can't decide" |

---

## 5. Persona Content Map

### 5.1 Content by Persona & Stage

| Persona | Awareness | Consideration | Decision |
|---------|-----------|---------------|----------|
| Eng Manager | Blog: "Claude Cost Optimization" | Guide: "Getting Started" | Trial experience |
| CTO/VP | Blog: "AI Governance at Scale" | Webinar: "Enterprise AI" | ROI calculator |
| CISO | Blog: "AI Compliance Guide" | Security whitepaper | Security review |
| CFO | Blog: "AI Cost Attribution" | ROI guide | Business case template |

---

## 6. Related Documents

| Document | Relationship |
|----------|--------------|
| [GTM-STRATEGY.md](./GTM-STRATEGY.md) | Overall GTM |
| [SALES-PLAYBOOK.md](./SALES-PLAYBOOK.md) | Persona selling |
| [MARKETING-PLAN.md](./MARKETING-PLAN.md) | Persona targeting |
| [USER-STORIES-*.md](../02-product/) | Product personas |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | GTM Team | Initial persona documentation |

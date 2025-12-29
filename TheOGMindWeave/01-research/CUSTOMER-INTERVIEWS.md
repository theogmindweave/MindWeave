# MindWeave Customer Interviews

> Discovery research with target customers

---

## Overview

This document contains templates, methodologies, and synthesized findings from customer discovery interviews. These interviews inform product priorities, pricing, messaging, and go-to-market strategy.

Our goal: Validate problem-solution fit before building, and ensure we're solving real problems for real customers.

---

## Interview Methodology

### Interview Types

| Type | Purpose | Duration | Frequency |
|------|---------|----------|-----------|
| **Discovery** | Understand problems, workflow, pain points | 45-60 min | Pre-product |
| **Validation** | Test solution concepts, pricing, features | 30-45 min | Post-prototype |
| **Feedback** | Evaluate product, gather improvements | 30 min | Ongoing |
| **Win/Loss** | Understand why they chose us (or didn't) | 20-30 min | Post-sales |

### Target Personas

| Persona | Title | Pain Points | Decision Authority |
|---------|-------|-------------|-------------------|
| **Engineering Leader** | VP/Director Engineering | Visibility, efficiency, tool sprawl | High (budget owner) |
| **Security/Compliance** | CISO, Compliance Manager | Audit trails, access control, regulations | High (veto power) |
| **Developer** | Sr. Engineer, Tech Lead | Productivity, friction, governance overhead | Medium (influence) |
| **IT/Platform** | Platform Engineer, IT Manager | Integration, management, scale | Medium |

---

## Discovery Interview Template

### Opening (5 minutes)

**Introduction Script:**
"Thank you for taking the time to speak with us. We're researching how companies manage AI tools like Claude and their integrations. There are no right or wrong answers—we're genuinely curious about your experience.

This conversation is confidential and will only be used to inform our product direction. Is it okay if I take notes? Would you prefer we not record?"

**Background Questions:**
1. What's your role and what does your day-to-day look like?
2. How long have you been using AI tools in your work?
3. How many people on your team use Claude or other AI assistants?

---

### Current State (15 minutes)

**AI Usage Questions:**
1. Walk me through how Claude is deployed in your organization today.
2. How did you decide to adopt Claude? Who was involved in that decision?
3. What's the scale of usage? (users, tokens/month, use cases)

**Governance Questions:**
4. How do you currently track who's using Claude and for what?
5. What visibility do you have into token usage and costs?
6. Are there any controls or policies around Claude usage?

**MCP/Integration Questions:**
7. Do you use MCPs (Model Context Protocol) or Claude's tool use features?
8. How many integrations have been built? Who built them?
9. How do teams share or discover integrations others have built?

---

### Pain Points (15 minutes)

**Problem Discovery:**
1. What's the biggest challenge you face with Claude at your organization?
2. Tell me about a time when lack of visibility into AI usage caused a problem.
3. Have you ever had duplicate work—different teams building the same thing?
4. What concerns does your security or compliance team have about Claude?

**Quantifying Pain:**
5. How much time does your team spend on AI governance/management tasks?
6. What's the cost impact of these problems? (time, money, risk)
7. If you had to put a dollar figure on the value of solving this, what would it be?

**Alternative Solutions:**
8. How are you solving these problems today?
9. What tools or processes have you tried?
10. What's working? What's not?

---

### Solution Exploration (10 minutes)

**Concept Testing:**
"Imagine a platform that [description of MindWeave]..."

1. How valuable would that be to you?
2. What features would be most important?
3. What would you be willing to pay for this?
4. Who else would need to be involved in a purchasing decision?

**Objection Discovery:**
5. What would prevent you from buying a solution like this?
6. What would you need to see before committing?
7. How long would evaluation typically take?

---

### Closing (5 minutes)

**Next Steps:**
1. Would you be interested in being a design partner for early product access?
2. Can I follow up with more specific questions as we build?
3. Is there anyone else on your team we should speak with?
4. Any questions for us?

**Thank You:**
"Thank you so much for your time. This is incredibly valuable. We'll keep you updated on our progress."

---

## Validation Interview Template

### Feature Validation (30 minutes)

**Setup:**
- Show prototype/mockups/demos
- Explain we're testing concepts, not selling
- Encourage honest feedback

**Questions per Feature:**

1. **Token Dashboard:**
   - "Here's how we visualize token usage across teams..."
   - How useful is this? What's missing?
   - Would this solve a real problem for you?

2. **MCP Registry:**
   - "This shows all Claude integrations across your organization..."
   - How valuable is seeing this inventory?
   - What metadata would you want to see?

3. **Team-Based Permissions:**
   - "This lets you control which teams can access which MCPs..."
   - How important is this granularity?
   - What permission model would you need?

4. **Hivemind Discovery:**
   - "This AI identifies duplicate integrations and suggests collaboration..."
   - Would you trust AI-generated suggestions?
   - How often would you act on these insights?

**Pricing Validation:**

"If this product existed today, what would you expect to pay?"

| Package | Our Target | Customer Response |
|---------|------------|-------------------|
| Team (10 seats) | $2,000/mo | _________________ |
| Enterprise (50 seats) | $25,000/mo | _________________ |
| Premier (custom) | $80,000/mo | _________________ |

---

## Interview Findings Summary

### Customer Interview Log

| # | Date | Company | Title | Industry | Key Insights |
|---|------|---------|-------|----------|--------------|
| 1 | Dec 2024 | TechCorp (F500) | VP Engineering | SaaS | No visibility into 200+ Claude users |
| 2 | Dec 2024 | FinanceInc | CISO | Finance | SOC 2 auditors asking about AI |
| 3 | Dec 2024 | HealthPlus | Dir. Compliance | Healthcare | HIPAA concerns blocking adoption |
| 4 | Dec 2024 | StartupX | CTO | Series B | 15 duplicate MCPs across 5 teams |
| 5 | Dec 2024 | BigRetail | IT Director | Retail | Cost overruns, no attribution |
| 6 | Dec 2024 | MediaCo | Eng Manager | Media | Team jealousy over AI access |
| 7 | Dec 2024 | ConsultCo | Partner | Consulting | Client-facing AI governance needed |
| 8 | Dec 2024 | MfgGlobal | Plant Ops Dir | Manufacturing | Shadow AI concerns |

---

## Synthesized Findings

### Top Pain Points (Ranked by Frequency)

| Rank | Pain Point | Mentioned By | Severity |
|------|------------|--------------|----------|
| 1 | **No visibility into AI usage** | 8/8 (100%) | Critical |
| 2 | **Can't track costs by team** | 7/8 (88%) | High |
| 3 | **Duplicate MCP/integration work** | 6/8 (75%) | High |
| 4 | **Compliance/audit concerns** | 6/8 (75%) | Critical |
| 5 | **No access controls** | 5/8 (63%) | Medium |
| 6 | **Don't know who's good at AI** | 4/8 (50%) | Medium |

---

### Customer Quotes

#### On Visibility
> "We have 347 people with Claude access. I have no idea what any of them are doing with it. That keeps me up at night."
> — VP Engineering, F500 SaaS Company

> "Our CFO asked me how much we spent on Claude last quarter. I had to say 'I don't know' and that was embarrassing."
> — CTO, Series C Startup

#### On Duplicate Work
> "I found out last week that three different teams built Salesforce integrations for Claude. Three! Nobody talked to each other."
> — Director of Engineering, Tech Company

> "We're a 5,000-person company. I guarantee there are dozens of duplicate MCPs. But I have no way to find them."
> — Platform Engineer, Enterprise

#### On Compliance
> "Our SOC 2 auditor asked about AI controls. We had nothing. Now it's a finding we have to remediate."
> — CISO, FinTech

> "HIPAA requires audit trails for any system touching patient data. Claude has zero audit capability at the org level."
> — Compliance Director, Healthcare

#### On Access Control
> "Finance can see Sales data through Claude. Sales can see HR data. It's a security nightmare waiting to happen."
> — Security Architect, F500

---

### Willingness to Pay

| Segment | Expected Price | Notes |
|---------|---------------|-------|
| Mid-Market (100-500 emp) | $200-300/seat/mo | Price sensitive, value-focused |
| Enterprise (500-5000) | $400-600/seat/mo | Will pay for compliance features |
| Large Enterprise (5000+) | $800-1000/seat/mo | Custom deals, on-prem options |

**Key Finding:** Compliance-driven buyers (CISO, Compliance) are less price sensitive than IT-driven buyers.

---

### Feature Priority (Customer Ranked)

| Feature | % Very Important | % Nice to Have | % Not Needed |
|---------|-----------------|----------------|--------------|
| Token Usage Dashboard | 100% | 0% | 0% |
| Cost Attribution by Team | 88% | 12% | 0% |
| MCP Registry | 75% | 25% | 0% |
| Audit Logs | 75% | 25% | 0% |
| SSO Integration | 63% | 25% | 12% |
| Team-Based Permissions | 50% | 50% | 0% |
| Duplicate Detection | 50% | 38% | 12% |
| Skill Tracking | 25% | 50% | 25% |

**Interpretation:** Visibility and cost features are table stakes. Advanced features (Hivemind) are differentiators, not requirements.

---

### Buying Process Insights

**Decision Makers:**
- Primary: CTO or VP Engineering (60%)
- Secondary: CISO or VP Security (30%)
- Influencer: Engineering Managers (10%)

**Evaluation Timeline:**
- SMB: 2-4 weeks
- Mid-Market: 4-8 weeks
- Enterprise: 3-6 months

**Common Objections:**
1. "We're building this internally" (30%)
2. "Need to see ROI before committing" (25%)
3. "Security review will take time" (20%)
4. "This isn't a priority right now" (15%)
5. "Anthropic might build this" (10%)

---

### Competitive Intel from Interviews

| Competitor Mentioned | Times | Context |
|---------------------|-------|---------|
| "Building internally" | 6/8 | Most common alternative |
| IBM Watson | 2/8 | "Too complex, too expensive" |
| LangSmith | 2/8 | "Good for debugging, not governance" |
| Datadog | 1/8 | "Wish AI tools had Datadog-like visibility" |
| AWS Audit Manager | 1/8 | "Only covers AWS usage" |

---

## Design Partner Program

### Criteria for Design Partners

| Criteria | Requirement |
|----------|-------------|
| Claude Usage | 100k+ tokens/month |
| Team Size | 50+ developers |
| Decision Maker | VP+ level sponsor |
| Engagement | Weekly 30-min calls |
| Feedback | Honest, actionable |
| Reference | Willing to be quoted (eventually) |

### Design Partner Benefits

- Free access during development (6-12 months)
- Direct input on product roadmap
- Priority support and custom features
- 50% discount on launch pricing (Year 1)
- Recognition as founding customer

### Current Design Partner Pipeline

| Company | Industry | Size | Status | Notes |
|---------|----------|------|--------|-------|
| TechCorp | SaaS | F500 | LOI Signed | 200+ Claude users |
| FinanceInc | Finance | 2000 | Verbal | CISO champion |
| StartupX | B2B SaaS | 300 | Interested | CTO intro needed |
| HealthPlus | Healthcare | 800 | Evaluating | HIPAA concerns |
| MediaCo | Media | 1500 | LOI Signed | Fast timeline |

**Target:** 10 design partners by MVP launch

---

## Interview Tracking

### Monthly Targets

| Month | Discovery | Validation | Total |
|-------|-----------|------------|-------|
| Jan 2025 | 10 | 0 | 10 |
| Feb 2025 | 8 | 5 | 13 |
| Mar 2025 | 5 | 10 | 15 |
| Apr 2025 | 3 | 12 | 15 |

### Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Interviews Completed | 50 (pre-launch) | 8 |
| Design Partners | 10 | 2 (LOI) |
| Win Rate (Verbal → LOI) | 60% | 40% |
| Persona Coverage | All 4 | 3/4 |

---

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Interview before building | Always | Avoid building wrong thing |
| Design partners | Free access | Reduce friction, get feedback |
| Target personas | 4 focus areas | Coverage without dilution |
| Interview frequency | 10+/month | Statistical significance |

---

## Open Questions

1. **Persona balance:** Are we talking to enough CISOs vs. engineers?
2. **Vertical focus:** Should we focus on specific industries?
3. **International:** When to start interviewing non-US customers?
4. **Competitor customers:** How to reach IBM/LangSmith users?

---

## Related Documents

- [../02-product/PRD-MVP.md](../02-product/PRD-MVP.md) - MVP product requirements
- [COMPETITIVE-INTEL.md](./COMPETITIVE-INTEL.md) - Competitor analysis
- [../04-gtm/ICP-PERSONAS.md](../04-gtm/ICP-PERSONAS.md) - Buyer personas

---

*Last Updated: December 2025*
*Owner: VP Product (TBH) / CEO*

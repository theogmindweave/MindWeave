# ITERATION 15: CHURN PREVENTION & CUSTOMER RETENTION PLAYBOOK

**Date:** December 29, 2025
**Focus:** Zero-churn operating system with predictive intervention and expansion mechanics
**Target:** 85%+ annual retention (vs 75% baseline) → unlock Series A funding acceleration

---

## SECTION 1: CHURN MATHEMATICS & WHY IT MATTERS

### The NRR Impact of Retention

**Scenario A: 75% Retention (Typical)**
```
Starting cohort: 100 customers at $150K ACV = $15M ARR
Year 2 base revenue: 75 customers × $150K = $11.25M
Expansion: 20 customers upgrade ($50K each) = $1M
Year 2 Total: $12.25M
NRR: ($12.25M / $15M) = 82% (NEGATIVE - losing revenue)
```

**Scenario B: 85% Retention (Best-in-Class)**
```
Starting cohort: 100 customers at $150K ACV = $15M ARR
Year 2 base revenue: 85 customers × $150K = $12.75M
Expansion: 25 customers upgrade ($50K each) = $1.25M
Year 2 Total: $14M
NRR: ($14M / $15M) = 93% (CLOSER TO 115%)
```

**Scenario C: 90% Retention (Top 10%)**
```
Starting cohort: 100 customers at $150K ACV = $15M ARR
Year 2 base revenue: 90 customers × $150K = $13.5M
Expansion: 30 customers upgrade ($50K each) = $1.5M
Year 2 Total: $15M
NRR: ($15M / $15M) = 100% (FOUNDATION for 120%+ total)
```

**Key Insight:** Every 1% increase in retention = +$150K ARR in Year 2 (with $15M starting base). A 90% retention customer base is 5x easier to scale to $100M+ than 75% base.

### Churn Tiers by Impact

**Churn Rate by Customer Size:**
- Startup tier ($500-$2K/mo): 20-30% annual churn (healthy, expected)
- Mid-market ($5K-$20K/mo): 10-15% annual churn (good)
- Enterprise ($50K+/mo): 5-10% annual churn (excellent)

**Why: Larger customers have more integration, switching cost is higher, budget is locked in.**

---

## SECTION 2: THE CHURN PREDICTION MODEL

### 8 Churn Risk Signals (Track Weekly)

**Signal #1: Usage Drop (Early Warning)**
- **Metric:** Weekly active users trend
- **Trigger:** 50% drop in WAU from previous week
- **Risk Level:** LOW-MEDIUM (many causes)
- **Action:** Diagnostic email "We noticed less activity. Everything OK?"
- **Conversion:** 60% respond, 30% reveal actual issue

**Signal #2: Feature Abandonment**
- **Metric:** Core features unused for 2+ weeks
- **Trigger:** Audit dashboard not accessed in 14 days
- **Risk Level:** MEDIUM (customer not getting value)
- **Action:** 1:1 CSM call to understand why
- **Conversion:** 70% of calls reveal fixable issue

**Signal #3: Support Escalation Pattern**
- **Metric:** Multiple support tickets with same theme
- **Trigger:** 3+ tickets in 2 weeks about same problem
- **Risk Level:** MEDIUM (product issue, not customer issue)
- **Action:** Escalate to product, create fix, notify customer personally
- **Conversion:** 80% satisfied after fix + personal attention

**Signal #4: Expansion Conversation Avoided**
- **Metric:** CSM tries to schedule expansion call, customer declines 2x
- **Trigger:** "Not interested in expansion" stated directly
- **Risk Level:** MEDIUM-HIGH (customer seeing limited value)
- **Action:** Discovery call "Help me understand—what would make this worth expanding?"
- **Conversion:** 50% of calls identify new feature/integration needed

**Signal #5: Budget Conversation Initiated**
- **Metric:** Customer asks about downsizing contract
- **Trigger:** "Can we reduce our seats/usage?" question
- **Risk Level:** HIGH (financial pressure or reduced need)
- **Action:** Immediate CFO/CRO involvement, understand budget situation, offer alternative
- **Conversion:** 40-50% can be saved with package restructuring

**Signal #6: Stakeholder Change**
- **Metric:** New person on customer calls replaces old champion
- **Trigger:** Email introduces replacement, new person unfamiliar with MindWeave
- **Risk Level:** MEDIUM (relationship risk, not product risk)
- **Action:** Immediate onboarding call with new stakeholder
- **Conversion:** 70% become advocates if onboarded right

**Signal #7: Peer Company Churn**
- **Metric:** Competitor announces win in customer's industry
- **Trigger:** Salesforce or Crunchbase alert shows competitor deal in same vertical
- **Risk Level:** MEDIUM (FOMO/competitive pressure)
- **Action:** Proactive call "Saw [competitor] in your space. Want to discuss strategy?"
- **Conversion:** 60% reaffirm commitment, 20% upgrade

**Signal #8: NPS Decline**
- **Metric:** NPS drops >10 points QoQ
- **Trigger:** Customer went from NPS 8 to NPS 5 in quarterly survey
- **Risk Level:** HIGH (strong churn signal)
- **Action:** 1:1 conversation "Your feedback shifted. What happened?"
- **Conversion:** 70% of conversations reveal specific issue + fixable

### Churn Prediction Score Calculation

```
Churn Risk Score (0-100, 100=highest risk):

Usage Drop (50% WAU decrease): +30 points
Feature Abandonment (core features unused): +25 points
Support Escalation (3+ tickets, same theme): +20 points
Expansion Avoided (customer declines 2x): +20 points
Budget Reduction Request: +35 points
Stakeholder Change (no relationship): +15 points
Peer Competitor Win (in same industry): +15 points
NPS Decline (>10 points drop): +25 points

Score Interpretation:
0-20: Low risk (stable customer)
21-40: Medium risk (monitor closely)
41-70: High risk (intervention needed)
71+: Critical risk (CEO involvement required)
```

**Weekly Process:**
- Calculate score for every customer
- Flag 71+ for immediate intervention
- Flag 41-70 for CSM action within 48 hours
- Monitor 21-40 for trends

---

## SECTION 3: INTERVENTION PLAYBOOKS (By Risk Level)

### LOW RISK INTERVENTION (Score 0-20)
**Action:** Automated email (template)
```
Subject: "MindWeave tip: [Feature] can save you 10 hours/month"

Hi [Name],

I noticed you're not using our [Feature] yet. Many customers in
your industry are using it to [specific outcome] and saving
[specific hours] per month.

Quick thought—might be worth exploring. Happy to walk through
in 15 minutes if helpful.

[CSM Name]
```
**Expected outcome:** 20% reply rate, 10% feature adoption

### MEDIUM RISK INTERVENTION (Score 21-40)
**Action:** Scheduled 1:1 call (not optional)

**CSM Call Script (30 minutes):**
```
Min 0-2: Small talk, relationship
Min 2-5: Observation: "We noticed a bit less activity last week"
Min 5-15: Listen (80%): "Help me understand what's going on?"
         - Is it a product issue?
         - Is it organizational change (budget, team)?
         - Is it competitive pressure?
         - Is it just less urgent than other priorities?
Min 15-25: Problem-solving
         - If product issue: "Here's how we solve this. Can I show you?"
         - If budget: "Let's talk options. Maybe we restructure?"
         - If competitive: "Let's discuss positioning. What are they claiming?"
         - If priority shift: "What if we focus on your top use case first?"
Min 25-30: Commitment
         - If solved: "Let's follow up next week. I'll set up time?"
         - If unsure: "I'll investigate this internally. Let me come back Friday?"
         - If churn risk: Go to HIGH RISK protocol
```
**Expected outcome:** 70% call completion, 50% issue resolution, 20% upgrade

### HIGH RISK INTERVENTION (Score 41-70)
**Action:** CSM + Manager + Executive involvement

**Escalation Protocol:**
1. **Day 0:** CSM sends problem summary to VP Customer Success
2. **Day 1:** VP schedules immediate call with customer (executive air cover)
3. **Call (60 minutes):**
   - Minutes 0-5: Executive intro + credibility ("I'm [VP], handle our most important relationships")
   - Minutes 5-30: Deep listen (customer feels heard by authority)
   - Minutes 30-45: Executive problem-solving (what can we do to fix this?)
   - Minutes 45-60: Commitment + ownership ("I'm personally going to own this. Here's my number.")
4. **Day 3:** Executive sends summary, specific action plan
5. **Week 1:** Follow-up call with positive news (usually execution on promised actions)

**Expected outcome:** 65% save rate (vs 40% without executive intervention)

### CRITICAL RISK INTERVENTION (Score 71+)
**Action:** CEO + Sales + Customer Success response

**CEO Intervention Protocol:**
1. **Day 0:** CEO reviewed case, reaches out personally
   ```
   Call script: "Hi [Name], I'm [CEO]. I saw we haven't delivered
   what you needed. I want to personally understand what happened
   and fix it. Can we talk tomorrow?"
   ```

2. **CEO Call (90 minutes):**
   - Listen 70%, talk 30%
   - Understand core issue (not the surface complaint)
   - Offer 2-3 concrete solutions
   - If budget: offer discount for renewal + future commitment
   - If product: offer custom feature + CEO check-in timeline

3. **Post-Call:**
   - Email same-day with summary + action plan
   - CEO personally owns follow-up
   - Custom Slack channel for real-time updates
   - Weekly CEO check-in until resolved

4. **Expected Outcome:** 80% save rate (CEO involvement is powerful)

---

## SECTION 4: SAVE PLAYBOOK (If Customer Says "We're Leaving")

### The 48-Hour Save Protocol

**Hour 0 (When Customer Says They're Leaving):**
- Do NOT panic or argue
- Say: "I understand. Help me understand what we missed."
- Record exact reason
- Thank them for feedback
- Ask: "If we fixed [specific issue], would you stay?"

**Hour 1:**
- Escalate immediately to VP Customer Success + VP Product
- Create action plan
- Identify: Can we fix this? How long? What will it cost?

**Hour 4:**
- VP Customer Success calls customer back
- Propose specific fix + timeline
- Frame: "We don't want you to leave. Let's work through this."

**Hour 12:**
- If fixable: Executive (VP/CEO) commits to specific action with timeline
- If not fixable: Offer discount/alternative

**Hour 24:**
- Team has begun work on fix (if needed)
- Send customer progress update
- Reinforce: "We're solving this"

**Hour 48:**
- Follow-up call
- Show progress (even partial)
- Reinforce commitment
- Get customer to commit: "If we fix this, would you stay?"

### Common Save Scenarios

**Scenario #1: "Your product doesn't do [feature] we need"**

Save script:
> "That's fair. Here's what I'm hearing: you need [feature] to solve
> [outcome]. We can build this. It would take [timeline] and cost
> [amount]. Here's what I propose: we build it under a [duration]
> pilot program. If it works, you stay. If not, we part ways. Fair?"

Expected save rate: 70% (customers want solutions, not to leave)

**Scenario #2: "You're too expensive"**

Save script:
> "I get it. Let's look at this differently. You're paying $150K/year
> for [core feature]. What if we restructured: you keep core for $100K/year,
> and add [premium feature] for $25K/year when you're ready? Gives you
> time to prove ROI to your CFO."

Expected save rate: 60% (packaging changes save deals)

**Scenario #3: "We're going with [competitor]"**

Save script:
> "Fair. Help me understand why. [Listen] OK, here's my honest take:
> they're great at [their strength]. We're better at [our strength].
> Instead of leaving, what if we do a quick 2-week side-by-side test?
> Let's see which actually delivers better on [your priority]?"

Expected save rate: 40% (some decisions already made, but 40% can be swayed)

**Scenario #4: "Our company is downsizing/budget cut"**

Save script:
> "I understand. This isn't about us—it's about your situation.
> Here's what I propose: we pause your contract for 3 months (save
> you $37.5K), you keep access, and when things improve, you re-activate
> with 20% discount locked in. Sound fair?"

Expected save rate: 75% (pausing > losing them)

**Scenario #5: "Our new CFO doesn't believe in the ROI"**

Save script:
> "New CFO = new perspective. Fair question. Let me prove it. Can
> we do a 15-minute call where I show your CFO the 3 ways we've saved
> your team money? [Do call, show impact]. CFO now understands ROI →
> problem solved."

Expected save rate: 80% (CFO usually convinced by data)

---

## SECTION 5: EXPANSION MECHANICS (Prevent Churn by Upgrading)

### Expansion Calendar (Quarterly Conversations)

**Quarter 1 (Months 1-3): Onboarding**
- Focus: Get customer to "first value"
- Expansion ask: NONE (too early)
- Goal: NPS 30+, regular usage

**Quarter 2 (Months 4-6): Value Realization**
- Focus: Customer expanding internally
- Expansion trigger: Usage growing, team interest emerging
- Expansion ask: "Your team is using this heavily. Ready to add team seats?"
- Expected upgrade: 15-20% of customers

**Quarter 3 (Months 7-9): Expansion Window**
- Focus: Second department adopts, new use case emerges
- Expansion trigger: Marketing team wants access, new stakeholder interested
- Expansion ask: "Your success is clear. Expand to [team] with Pro tier?"
- Expected upgrade: 20-25% of customers

**Quarter 4 (Months 10-12): Enterprise Expansion**
- Focus: Enterprise-wide adoption signals
- Expansion trigger: Company growth, Series funding, compliance upgrade
- Expansion ask: "You're scaling. Enterprise tier unlocks [features]."
- Expected upgrade: 15-20% of customers

**Combined annual expansion: 50-65% of customers expand or move tiers**

### Expansion Conversation Framework (30 minutes)

**Minutes 0-5: Relationship**
- "How's the team? What's new with you?"
- Build rapport

**Minutes 5-10: Success Recap**
- "I was reviewing your impact. You've: [specific metrics]"
- Customer hears: "We've been tracking your success"
- Psychological trigger: achievement recognition

**Minutes 10-15: Growth Observation**
- "I'm noticing [team name] is interested in this. Are they?"
- Customer usually: "Yeah, they want access"
- You: "Perfect. Let me show you how to do that."

**Minutes 15-25: Solution Presentation**
- Show Pro tier with specific features they need
- Price: "It's $300K/year total ($250K current + $50K for team)"
- Frame: "You're paying us $250K. You're saving $400K with governance. Adding $50K for team access = 8x ROI."
- Psychological trigger: Loss aversion (don't lose out on savings)

**Minutes 25-30: Commitment**
- "Let's try it for Q1. If the team adopts, it's theirs."
- Usually: "Makes sense, let's do it."
- Close: "Great. I'll send you the paperwork."

**Expected close rate: 70%** (expansion conversations are 4x easier than new customer sales)

---

## SECTION 6: NPS & SATISFACTION TRACKING

### Quarterly NPS Survey (4-Question Framework)

**Q1: Core NPS (0-10 scale)**
> "How likely are you to recommend MindWeave to a colleague?"

**Q2: Likelihood to Expand (Yes/No)**
> "In the next 12 months, are you planning to expand your use of MindWeave?"

**Q3: Churn Risk (Yes/No)**
> "Are you considering switching to an alternative solution?"

**Q4: Open Feedback**
> "What's one thing we should improve?"

### NPS Segmentation

**Promoters (NPS 9-10):**
- Action: Ask for referral ("Know anyone in healthcare governance?")
- Feature: Make them advocates (case study, testimonial)
- Expansion: They're your best expansion candidates

**Passives (NPS 7-8):**
- Action: "What would make you a 9?" (identify missing feature/support)
- Feature: Quick fix often converts them to promoters
- Expansion: Conditional (fix issue first, then expand)

**Detractors (NPS 0-6):**
- Action: Immediate 1:1 to understand issue
- Feature: This is your churn risk pool
- Expansion: NEVER ask detractors to expand (they'll leave)
- Recovery: Fix issue, re-survey after 30 days

### Quarterly Review Agenda (VP Customer Success)

**Review Template:**
```
NPS Trend: [Q1] → [Q2] → [Q3] → [Q4]
Promoters: [%] (target 50%+)
Passives: [%] (target 30-40%)
Detractors: [%] (target 10%-)

Promoter Insights: [Top 3 reasons they love us]
Detractor Insights: [Top 3 reasons they're unhappy]
Action Items: [What to fix]
```

---

## SECTION 7: ZERO-CHURN OPERATING SYSTEM (Weekly Cadence)

### Monday CSM Team Standup (30 minutes)
- Review all customers with score 41+
- Assign escalation owners
- Plan week's interventions
- Track save rate from last week

### Weekly Metrics Dashboard
```
Metric                          Target    Actual   Status
Active Customers               100       98       ✓
Customers with Score 0-20      70%       72%      ✓
Customers with Score 21-40     20%       20%      ✓
Customers with Score 41+       10%       8%       ✓
Churn Rate (Monthly)           1.5%      1.2%     ✓
Expansion Rate                 3%        3.5%     ✓
NPS Average                    47        48       ✓
```

### Friday Expansion Review (1 hour, VP Sales + CS)
- Review expansion opportunities identified
- Close any qualified expansion conversations
- Celebrate wins
- Plan next week's expansion asks

### Monthly CEO Business Review
- Cohort retention by month (Month 1, 2, 3+)
- Churn causes analysis (product, budget, competitive)
- Save rate by intervention type
- NPS by segment
- Expansion rate trends
- Revenue impact of retention improvements

---

## SECTION 8: CUSTOMER HEALTH SCORE

### 5-Factor Health Score (0-100)

**Factor #1: Engagement (40% weight)**
- Weekly active users: 25 points
- Feature adoption: 10 points
- Support tickets (positive): 5 points
- Score: Active customers = 40/40, Declining = 20/40, Inactive = 5/40

**Factor #2: Value Realization (30% weight)**
- Achieved stated ROI: 30 points (or partial credit)
- Expansion conversation positive: 10 points
- NPS 8+: 20 points
- Score: High value = 30/30, Some value = 20/30, No value = 5/30

**Factor #3: Budget (20% weight)**
- Budget approved for renewal: 15 points
- Budget for expansion: 5 points
- Score: Locked budget = 20/20, Uncertain = 10/20, At risk = 2/20

**Factor #4: Relationship (5% weight)**
- Multi-stakeholder engagement: 4 points
- Executive sponsor in place: 1 point
- Score: Strong = 5/5, Weak = 2/5, At risk = 0/5

**Factor #5: Competitive (5% weight)**
- No competitive threat: 5 points
- Aware of alternatives: 2 points
- In active evaluation: 0 points

**Health Score Interpretation:**
- 80-100: Green (Healthy, expand)
- 50-79: Yellow (At risk, monitor + support)
- 0-49: Red (Critical, intervention needed)

### Automated Health Scoring
- Calculate weekly for each customer
- Trend analysis (improving vs declining)
- Forecasting: Red score → probable churn in 4-12 weeks
- Alert: Yellow→Red transition triggers immediate intervention

---

## SECTION 9: CHURN PREVENTION ROI

### The Math: Retention Investment Payoff

**Scenario: Invest $200K/year in retention infrastructure**
- 1 VP Customer Success: $150K
- 2 CSM hires: $200K (2x $100K)
- Tools/systems: $50K
- **Total: $400K/year investment**

**Expected outcome:** Retention improves from 75% → 85%

**Impact on $15M ARR starting base:**
- 75% retention Year 2: $11.25M base
- 85% retention Year 2: $12.75M base
- **Difference: $1.5M additional ARR** (via retention)

**ROI Calculation:**
- Investment: $400K
- Incremental revenue: $1.5M
- Additional gross profit (at 77% margin): $1.155M
- **Year 1 ROI: 288%** (1.155M / 400K)

**Years 2+:** Compounding benefit
- Year 2: $2M+ additional revenue (compounding from Year 1)
- Year 3: $3M+ additional revenue

**5-Year cumulative impact:**
- Investment: $2M (5 years x $400K)
- Additional revenue: $8-10M
- **Lifetime ROI: 400%+**

**Key insight:** Retention infrastructure is the highest ROI investment a SaaS company can make.

---

## SECTION 10: EXECUTION CHECKLIST

### This Month
- [ ] Build churn prediction model
- [ ] Audit all customers for churn risk
- [ ] Flag 20-30 high-risk customers
- [ ] Create intervention playbooks
- [ ] Assign CSM owners

### Next Month
- [ ] Launch weekly risk scoring
- [ ] Execute interventions for 41+ score customers
- [ ] Track save rates
- [ ] Survey NPS quarterly
- [ ] Create health score dashboard

### Quarterly
- [ ] Review cohort retention
- [ ] Identify churn causes
- [ ] Iterate on intervention playbooks
- [ ] Plan expansion calendar
- [ ] CEO business review

---

**RESULT:** 85%+ annual retention, enabling 115%+ NRR, enabling Series A at better valuation and Series B at higher round size.


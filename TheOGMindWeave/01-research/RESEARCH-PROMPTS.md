# Research Prompts for MindWeave

> Copy-paste these into Perplexity Pro or Claude Opus 4.5
> After getting responses, paste results here for processing

---

## CATEGORY 1: Market & Competition

### Prompt 1.1: Enterprise AI Governance Market (Perplexity)
```
Research the enterprise AI governance market in 2025:

1. What is the total addressable market (TAM) for AI governance platforms?
2. Who are the top 10 competitors in this space? Include:
   - Company name
   - Funding raised
   - Key features
   - Pricing model
   - Target customers
3. What are the key trends driving this market?
4. What regulatory frameworks are pushing enterprises toward AI governance?
   - EU AI Act
   - NIST AI RMF
   - State-level regulations
5. What pain points do enterprises have with current AI governance solutions?

Provide specific numbers, statistics, and sources where possible.
```

### Prompt 1.2: Claude Enterprise Adoption (Perplexity)
```
Research Anthropic Claude's enterprise adoption in 2025:

1. Which major companies have publicly announced Claude Enterprise deployments?
   - Company name
   - Use case
   - Scale (employees, usage)
2. What is Claude Enterprise's pricing?
3. What features does Claude Enterprise offer vs. standard?
4. What are the main use cases for Claude in enterprises?
5. How does Claude Code fit into enterprise workflows?
6. What MCP (Model Context Protocol) integrations are available?
7. What governance features does Anthropic provide natively?

Include recent news, case studies, and announcements.
```

### Prompt 1.3: MCP Protocol Landscape (Perplexity)
```
Research the Model Context Protocol (MCP) ecosystem in 2025:

1. What is MCP and when was it launched?
2. What companies are building MCP tools/platforms?
3. What are the most popular MCP servers available?
4. How are enterprises managing MCP deployments?
5. What security concerns exist with MCP?
6. What governance/management tools exist for MCP?
7. How does MCP compare to other integration approaches?

Focus on enterprise use cases and management challenges.
```

---

## CATEGORY 2: Technical Deep Dives

### Prompt 2.1: Engineering Intelligence Platforms (Claude Opus)
```
You are a technical analyst researching engineering intelligence platforms.

Analyze these platforms in depth:
1. Workweave.dev - What exactly do they do? Features? Pricing?
2. Middleware (open source) - Architecture, features, limitations
3. Apache DevLake - How does it work? What metrics does it track?
4. LinearB - Features, pricing, enterprise adoption
5. Jellyfish - What makes them different?

For each platform, provide:
- Core value proposition
- Key features
- Technical architecture (if known)
- Pricing model
- Strengths and weaknesses
- What MindWeave can learn from them

Be comprehensive and technical.
```

### Prompt 2.2: AI Usage Tracking Systems (Claude Opus)
```
Research how enterprises track AI tool usage and ROI:

1. How do companies currently measure AI tool adoption?
2. What metrics matter for AI usage tracking?
   - Token usage
   - Cost allocation
   - Productivity impact
   - Quality improvements
3. How does Workweave.dev track "% AI" in PRs?
4. What technical approaches exist for measuring AI contribution to code?
5. How can you attribute time savings to AI tools?
6. What dashboards/reports do engineering leaders want?

Provide technical implementation details where possible.
```

### Prompt 2.3: DORA Metrics Implementation (Claude Opus)
```
Deep dive into DORA metrics for engineering teams:

1. What are the 4 DORA metrics exactly?
   - Deployment Frequency
   - Lead Time for Changes
   - Mean Time to Restore
   - Change Failure Rate
2. How do you calculate each metric accurately?
3. What data sources are needed?
4. How do you integrate with GitHub/GitLab for this data?
5. What are "Elite", "High", "Medium", "Low" thresholds?
6. How do leading platforms implement DORA tracking?
7. What's the correlation between DORA and business outcomes?

Provide implementation details and best practices.
```

---

## CATEGORY 3: Enterprise Requirements

### Prompt 3.1: Enterprise Compliance for AI (Perplexity)
```
Research enterprise compliance requirements for AI tools in 2025:

1. What compliance certifications do AI platforms need?
   - SOC 2 Type I vs Type II
   - HIPAA for healthcare
   - GDPR for EU
   - FedRAMP for government
2. What audit requirements exist for AI usage?
3. How do enterprises handle data privacy with AI tools?
4. What access control models are required?
5. What logging/audit trail requirements exist?
6. How do companies handle AI tool approval workflows?

Focus on practical requirements for a B2B SaaS platform.
```

### Prompt 3.2: Enterprise AI Procurement (Perplexity)
```
Research how enterprises buy AI governance tools:

1. Who are the typical buyers? (CTO, CISO, VP Eng, etc.)
2. What is the typical sales cycle length?
3. What security reviews are required?
4. What POC/pilot requirements exist?
5. What contract terms are standard?
6. What integrations are table-stakes for enterprise?
7. What price ranges are acceptable?

Include insights from recent enterprise software deals.
```

---

## CATEGORY 4: Startup Strategy

### Prompt 4.1: B2B SaaS GTM Strategies (Claude Opus)
```
You are a startup advisor. Recommend GTM strategies for MindWeave:

Context:
- MindWeave is an enterprise AI governance platform
- Target: 500+ employee companies using Claude Code
- Price point: $200-$1000/seat/month
- Differentiators: Team-based governance, APIR learning, Hivemind discovery

Questions:
1. What GTM motion should we use? (PLG, sales-led, hybrid)
2. How should we structure the sales team?
3. What marketing channels work best for enterprise AI tools?
4. How do we get first 10 customers?
5. How do we build credibility quickly?
6. What partnerships should we pursue?
7. What content strategy works?

Be specific and actionable.
```

### Prompt 4.2: Startup Funding Landscape (Perplexity)
```
Research the funding landscape for AI infrastructure startups in 2025:

1. What recent funding rounds have happened in AI governance/tooling?
2. What valuations are AI startups getting at Seed, Series A, B?
3. Which VCs are most active in this space?
4. What metrics do investors look for?
5. What ARR milestones unlock each funding round?
6. What's the typical dilution at each stage?
7. Are there relevant accelerators or grants?

Include specific recent deals and investor names.
```

---

## CATEGORY 5: Technical Architecture

### Prompt 5.1: LLM Observability Architecture (Claude Opus)
```
Design the technical architecture for an LLM observability platform:

1. How do you capture LLM interactions without impacting performance?
2. What data should be logged for each interaction?
3. How do you store and query large volumes of LLM logs?
4. How do you calculate costs in real-time?
5. How do you detect anomalies in LLM usage?
6. How do you integrate with Claude API specifically?
7. What's the best tech stack for this?

Provide architectural diagrams (text-based) and technology choices.
```

### Prompt 5.2: Skill/Pattern Detection System (Claude Opus)
```
Design a system that detects patterns in developer work and generates skill suggestions:

Context: MindWeave's "Intelligent Mind" runs nightly to:
- Analyze all code/PRs from the day
- Identify patterns and inefficiencies
- Generate skill suggestions for developers
- Learn from accept/reject feedback

Questions:
1. What data do we need to collect?
2. How do we identify "patterns" in code/PRs?
3. How do we generate actionable skill suggestions?
4. How do we implement the feedback loop?
5. What ML/AI approaches work best?
6. How do we handle multi-tenant data?
7. How do we scale this for 500+ developer orgs?

Be technically detailed.
```

---

## CATEGORY 6: Open Source Research

### Prompt 6.1: Open Source Alternatives Analysis (Claude Opus)
```
Analyze these open-source projects for what MindWeave can learn:

1. github.com/middlewarehq/middleware
   - What features do they have?
   - How is it architected?
   - What's their data model?
   - What can we copy/learn?

2. github.com/qodo-ai/pr-agent
   - How do they do AI PR review?
   - How do they track AI impact?
   - What's their plugin architecture?

3. github.com/langfuse/langfuse
   - How do they do LLM observability?
   - What's their tracing approach?
   - How do they handle multi-tenant?

4. github.com/apache/incubator-devlake
   - What data sources do they support?
   - How do they calculate DORA?
   - What's their plugin system?

For each: features, architecture, what to learn, what to avoid.
```

---

## HOW TO USE THESE PROMPTS

1. **Copy a prompt** from above
2. **Paste into Perplexity Pro** (for market research, current data)
3. **Or paste into Claude Opus 4.5** (for technical analysis, strategy)
4. **Copy the response**
5. **Paste below in the RESPONSES section**
6. **Tag with date and source**

---

## RESPONSES (Paste Results Here)

### Response Log

| Date | Prompt | Source | Status |
|------|--------|--------|--------|
| - | - | - | Awaiting responses |

---

### [DATE] - [PROMPT NAME] - [SOURCE]

```
Paste response here
```

**Key Takeaways:**
-
-
-

**Action Items:**
-
-
-

---

*Add more response sections as needed*

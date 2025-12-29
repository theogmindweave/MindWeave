# Open Source Repositories for MindWeave

> Learn from these. Don't reinvent the wheel.

---

## CLONED REPOSITORIES

*Located in `/open-source/` directory*

### 1. Middleware (DORA Metrics)
```
Repo: github.com/middlewarehq/middleware
Stars: 1,500+
License: Apache 2.0
```

**What It Does:**
- PR analytics and DORA metrics
- Team performance tracking
- Engineering productivity insights

**What to Learn:**
- [ ] Data model for PR tracking
- [ ] DORA calculation logic
- [ ] Dashboard design patterns
- [ ] GitHub integration approach

**Key Files to Study:**
- `backend/analytics/` - Metrics calculation
- `web/src/components/` - Dashboard UI
- `docker-compose.yml` - Deployment setup

---

### 2. PR-Agent by Qodo
```
Repo: github.com/qodo-ai/pr-agent
Stars: 9,500+
License: Apache 2.0
```

**What It Does:**
- AI-powered PR review
- AI usage % tracking
- Code suggestions
- Impact evaluation

**What to Learn:**
- [ ] How they track AI contribution %
- [ ] PR analysis architecture
- [ ] LLM integration patterns
- [ ] Suggestion generation logic

**Key Files to Study:**
- `pr_agent/tools/` - Core analysis tools
- `pr_agent/ai_handler.py` - LLM integration
- `docs/` - Feature documentation

---

### 3. Langfuse (LLM Observability)
```
Repo: github.com/langfuse/langfuse
Stars: 20,000+
License: MIT
```

**What It Does:**
- LLM tracing and observability
- Cost tracking
- Prompt management
- Analytics

**What to Learn:**
- [ ] Multi-tenant architecture
- [ ] Trace/span data model
- [ ] Cost calculation approach
- [ ] Dashboard patterns

**Key Files to Study:**
- `packages/shared/` - Core data models
- `web/src/` - Frontend
- `worker/` - Background processing

---

### 4. Apache DevLake
```
Repo: github.com/apache/incubator-devlake
Stars: 3,000+
License: Apache 2.0
```

**What It Does:**
- Engineering analytics
- 15+ data source integrations
- DORA metrics
- Custom dashboards

**What to Learn:**
- [ ] Plugin architecture for integrations
- [ ] Data pipeline design
- [ ] Metric definitions
- [ ] Enterprise patterns

**Key Files to Study:**
- `backend/plugins/` - Integration plugins
- `backend/models/` - Data models
- `config-ui/` - Configuration UI

---

### 5. Anthropic Cookbook
```
Repo: github.com/anthropics/anthropic-cookbook
Stars: 3,000+
License: MIT
```

**What It Does:**
- Claude API patterns
- Best practices
- Use case examples

**What to Learn:**
- [ ] Claude API integration patterns
- [ ] Prompt engineering
- [ ] Error handling
- [ ] Rate limiting

**Key Notebooks:**
- `misc/prompt_caching.ipynb`
- `skills/citations/` - Citation examples
- `tool_use/` - Tool use patterns

---

### 6. MCP Servers (Official)
```
Repo: github.com/modelcontextprotocol/servers
Stars: 5,000+
License: MIT
```

**What It Does:**
- Official MCP server implementations
- Reference implementations
- Integration examples

**What to Learn:**
- [ ] MCP protocol structure
- [ ] Server implementation patterns
- [ ] Available integrations
- [ ] Security patterns

**Key Directories:**
- `src/` - Server implementations
- Each server folder has README

---

### 7. MCP Specification
```
Repo: github.com/modelcontextprotocol/specification
Stars: 2,000+
License: MIT
```

**What It Does:**
- Official MCP protocol spec
- Schema definitions
- Protocol documentation

**What to Learn:**
- [ ] Protocol structure
- [ ] Schema definitions
- [ ] Capabilities
- [ ] Best practices

---

### 8. DORA Four Keys
```
Repo: github.com/dora-team/fourkeys
Stars: 2,200+
License: Apache 2.0
```

**What It Does:**
- Official Google DORA implementation
- Metric calculations
- GCP deployment

**What to Learn:**
- [ ] Official DORA definitions
- [ ] Calculation methods
- [ ] Data sources needed
- [ ] Dashboard design

**Note:** Archived Jan 2024 but still valuable reference

---

## TO CLONE (Not Yet Cloned)

### High Priority

| Repo | Why Important | Action |
|------|---------------|--------|
| `github.com/langchain-ai/langsmith-sdk` | LLM tracing patterns | Clone |
| `github.com/PostHog/posthog` | Product analytics | Study |
| `github.com/supabase/supabase` | Auth/DB patterns | Study |
| `github.com/cal-com/cal.com` | Enterprise SaaS patterns | Study |

### Medium Priority

| Repo | Why Important |
|------|---------------|
| `github.com/Infisical/infisical` | Secrets management |
| `github.com/boxyhq/jackson` | SSO implementation |
| `github.com/triggerdotdev/trigger.dev` | Background jobs |

---

## STUDY PLAN

### Week 1: Core Analytics
1. [ ] Study Middleware data model
2. [ ] Understand DORA calculations
3. [ ] Review Langfuse architecture

### Week 2: AI Integration
1. [ ] Study PR-Agent LLM integration
2. [ ] Review Anthropic cookbook patterns
3. [ ] Understand MCP protocol

### Week 3: Enterprise Patterns
1. [ ] Study multi-tenant patterns
2. [ ] Review SSO implementations
3. [ ] Understand audit logging

---

## KEY LEARNINGS (Document Here)

### From Middleware
```
Learning: [Document as you study]
```

### From PR-Agent
```
Learning: [Document as you study]
```

### From Langfuse
```
Learning: [Document as you study]
```

---

## CLONE COMMANDS

```bash
# Already cloned - in /open-source/
cd open-source/

# Additional repos to clone
git clone --depth 1 https://github.com/PostHog/posthog.git
git clone --depth 1 https://github.com/supabase/supabase.git
git clone --depth 1 https://github.com/boxyhq/jackson.git
```

---

*APIR: Learn from others, adapt to our needs, prune what doesn't fit.*

# How We Turn Your Github, Linear, and Cursor Data Into Actionable Data - Remote

> Weave combines LLMs and domain-specific machine learning to understand engineering work. We understand how much work was done by AI vs. humans. How much AI is helping your team ship faster, if it's having an impact on code quality and code reviews.

- ##### 1. - - ##### #### - - 1. ##### 1. ##### #### ##### - - ##### - ##### - ##### #### ##### ##### ### $4.2M seed round led by Moonfire, Burst Capital & Y Combinator

$4.2M seed round led by Moonfire, Burst Capital & Y Combinator

Building the Deep Research Agent: Turning Engineering Data Into Intelligence

What is the deep research agent?

Our agent, Wooly AI, analyzes all of your engineering metrics and data to answer any question about your team's productivity. It reasons across code output, review patterns, AI usage, quality metrics, and team dynamics to surface insights that would take hours of manual analysis to uncover, if you could uncover them at all.

**The core difference:**Traditional analytics are reactive. They show what you've configured them to show. It’s exploratory. It understands your question, identifies which metrics matter, gathers relevant data from multiple sources, and synthesizes an answer that's contextual to your specific team.

The data aggregation advantage

Weave consolidates metrics from across your project management tools, version control systems, and productivity platforms. Most engineering teams have their data fragmented across 5-10 different tools. When you ask "how can I ship faster?", answering that question requires pulling together code output from GitHub, project context from Jira or Linear and AI usage data from Cursor, Claude Code and more.

DRA operates on this unified data layer. The agent sees your entire engineering system holistically, which means it can discover insights that span multiple tools, insights that are literally impossible to find when your data lives in silos.

This data aggregation is our moat. The agentic architecture is sophisticated, but the real value is having comprehensive, integrated data to reason over.

**Current state:**Wooly AI is deployed as a research and reporting agent, excelling at deep analytical questions and comprehensive performance reports.

**Who it's for:**Engineering leaders and team leads making data-driven decisions about velocity, quality, and team health.

What Wooly AI does best

1. Anomaly Detection: "What's Wrong Right Now?"

Instead of manually scanning dashboards for red flags, ask DRA to analyze everything and surface what's actually unusual:

A PR that took 28 days to merge when your team average is 4 days
- An engineer whose output suddenly dropped 70% from their baseline
- A team's review cycle time that spiked 3x in the last week
- A repository that went from 50 commits/week to 12 with no explanation

DRA finds these patterns across any time range: last week, last month, last quarter and explains what changed.

2. Performance Analysis: "How Do I Ship Faster?"

This question requires a systematic analysis of your entire system. DRA doesn't just look at velocity in isolation; it finds the bottlenecks:

**Example analysis:**"Your org's average review wait time increased from 8 hours to 38 hours over the last month. DRA identifies that 60% of cross-team reviews now route through your Platform team, they're doing 4.2x more reviews than any other team. The bottleneck isn't code quality or review thoroughness; it's that Platform became a single point of dependency after the org restructure. Recommended action: Distribute architecture review responsibility across senior engineers in each team."

The agent examines:

**Code output patterns**across repositories, teams, and authors
- **Review dynamics**: Who's reviewing what? Where are the queues forming?
- **Quality vs. velocity trade-offs**: Reverted PRs, bug introduction rates, technical debt accumulation
- **AI adoption impact**: Teams using AI-assisted coding showing 30% higher output, should other teams adopt similar tools?

3. Multi-Dimensional Correlation Analysis

Real insights live at the intersections:

Did velocity drop because of increased review burden, or because the team added two junior engineers who need more mentoring?
- Is your highest-performing team actually introducing more bugs per line of code than slower teams?
- Are teams with high AI adoption also showing improved code quality, or are they trading quality for speed?
- Did your switch from feature branches to trunk-based development actually improve cycle time, or did it just shift where the delays happen?

DRA can analyze these questions across:

**Code output**: repository, team, and author levels
- **Review patterns**: cycle times, quality signals, bottleneck identification
- **AI metrics**: Usage correlation with output and quality
- **Quality indicators**: Reverted PRs, bug patterns, technical debt
- **Time-series trends**: Week over week, month over month, quarter over quarter

Beyond Simple Lookups

DRA isn't optimized for simple fact retrieval. "What was the last PR John pushed?" is better answered by looking at GitHub directly. DRA excels at synthesis, questions requiring multiple data sources, trend identification, and contextualized recommendations.

How It Works: Built for Intelligence

Why This Problem Needs Agents

Engineering management operates on incomplete, unstructured information spread across multiple systems. Should this task be assigned to Alice or Bob? Which bugs should be prioritized? Is this new review process helping or hurting? These decisions require:

**Context awareness**across multiple data sources
1. **Pattern recognition**that humans might miss
1. **Reasoning**about causality, not just correlation
1. **Synthesis**of insights into actionable recommendations

Traditional rule-based systems can't handle this complexity. Dashboards can show you the data but can't reason about it. This is precisely where agentic AI excels: taking messy, multi-dimensional data and extracting signal from noise.

The Multi-Node Agentic Workflow

Wooly AI is an orchestrated workflow where different stages operate with different contexts and constraints.

**Context-Aware Phases:**

**Understanding**: Classify the query (simple vs. deep research)
1. **Context Gathering**: Collect relevant user/team metadata
1. **Research**: Gather data from multiple sources
1. **Analysis**: Identify patterns and correlations
1. **Reporting**: Synthesize findings into actionable insights

Each phase receives only the context relevant to that stage. This is critical. By hiding irrelevant information, we keep the agent focused and reduce hallucination risk.

**Intelligent Query Routing:**Not all questions need the same computational effort. DRA automatically classifies queries:

**Simple queries**(e.g., "Show me commits from the mobile team last week") → Single-agent, streamlined workflow
- **Deep research queries**(e.g., "Why did velocity drop and what should we do about it?") → Parallel research system

Auto-classification achieves 90%+ accuracy. Users can also manually toggle modes.

**Parallel Research Agents:**For complex queries, DRA deploys up to six parallel research agents. Here's a real example:

**Query:**"Why did velocity drop 30% last month?"

**DRA spawns 6 agents:**

**Agent 1**: Analyze code output trends across all teams (finds Mobile team output dropped 60%)
- **Agent 2**: Examine review cycle time patterns (identifies 2x longer review waits)
- **Agent 3**: Investigate deployment frequency changes (no significant change)
- **Agent 4**: Check for infrastructure or tooling changes
- **Agent 5**: Correlate with team composition changes (discovers 2 senior engineers on PTO)
- **Agent 6**: Examine external dependencies and blockers (identifies API dependency delays)

Each agent iterates independently: high-level analysis → detailed drill-down → refinement. Results synthesize into: "Velocity drop primarily driven by Mobile team (60% decrease). Root causes: CI/CD migration created 4-day deployment delays, compounded by two senior engineers on PTO during critical sprint. Platform team velocity actually increased 15%. Recommendation: Prioritize Mobile CI/CD stabilization; consider cross-team pairing to reduce PTO impact."

This parallel approach delivers both speed and depth. Sequential exploration would be slow; multiple agents exploring different angles simultaneously gets comprehensive answers fast.

Infrastructure and Design Choices

**Tech stack:**Python for the agent service and MCP server (fast iteration, rich ecosystem for agentic workflows), integrating with our Go backend. FastAPI handles the agent service orchestration.

**Architecture:**

The Model Context Protocol (MCP) provides a clean abstraction for data access. Our Go backend remains the source of truth for all metrics, handling authentication and retrieval.

**Internal-only by design:**Both the agent and MCP server require authentication. Only verified users within our platform can query DRA. This gives us security and control as we iterate rapidly. Many companies are building public MCP servers; we may get there, but our focus now is nailing the authenticated use case. The agent is only acting on company data. The only data that is used beyond your team's connections are the percentiles and benchmarks for all our metrics. These are only used for comparison purposes, not direct data querying.

**Read-only operations:**DRA currently only reads data, it doesn't modify, create, or delete anything. This is a deliberate constraint as we build trust and understand the right interaction patterns. Write operations unlock massive value but introduce risk. We're moving carefully.

The Roadmap: From Analysis to Action

We're building toward DRA as the central nervous system for engineering operations. Here's the trajectory:

**Near-term (Next 3-6 months):**

**Anomaly detection system integration**: Continuous monitoring that proactively alerts you to unusual patterns before you have to ask
- **Enhanced pattern recognition**: Early warning signs of burnout, predictors of quality issues, indicators of process breakdown
- **Expanded metric coverage**: Deeper integration with more tools and richer signal extraction

**Medium-term (6-12 months):**

**Write capabilities**: Creating tickets, assigning tasks, updating project state
- **Automated project management**: Setting up projects with learned patterns from your previous work
- **Intelligent bug discovery**: Analyzing PRs for common error patterns and automatically creating remediation tickets

**The vision:**

Imagine this workflow: "Create a new project for the mobile team's Q2 initiative, using the same structure as the backend refactor project. Set up initial tasks and assign them based on who has capacity and relevant expertise."

DRA executes:

Reads your previous project configurations, extracts patterns
1. Analyzes current team capacity, skills, and workload distribution
1. Creates project structure in your PM tool
1. Generates and assigns initial tasks to appropriate team members
1. Configures workflows, integrations, and tracking dashboards
1. Sets up automated status reporting

This automation reclaims hours each week spent on project administration, ticket grooming, and process coordination. The logical extension: DRA becomes your engineering operations partner, continuously optimizing processes, identifying opportunities, and executing routine management tasks while you focus on strategy and people.

Try It and Shape It

We're early, DRA is powerful today at research and analysis, but most of what we just described is ahead of us. We're sharing this because we believe in building with community feedback.

**We want to hear about:**

**The question you wish you could ask your engineering data:**What insight would change how you make decisions?
- **The pattern that signals trouble in your org:**What subtle indicator always means something's wrong (that no tool catches)?
- **The management task you'd gladly hand to an agent tomorrow:**What's tedious enough that you'd trust automation?
- **The workflow DRA should enable:**What integration or capability would transform your team?

The engineering data landscape is vast, and the possibilities for agentic intelligence are genuinely exciting. We have strong hypotheses, but we know we're missing things. Your feedback shapes where this goes.

Share your ideas, your use cases, your wild what-if scenarios. This technology is powerful, and we're still discovering all the ways it can help teams ship better software faster.

**Try the Deep Research Agent:**www.workweave.dev/agent

Article written by

Samir Amin

Make AI Engineering Simple

Effortless charts, clear scope, easy code review, and team analysis

Book a demo

Book a demo

Book a demo

Book a demo

Book a demo

Book a demo
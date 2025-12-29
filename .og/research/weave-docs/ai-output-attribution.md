# AI output attribution

> Understanding how Weave attributes output between humans and AI tools

# AI output attribution

Weave uses sophisticated methods to accurately attribute code contributions between human developers and AI coding assistants. This attribution helps teams understand the impact of AI tools on their development process while ensuring human contributions are properly recognized.

## Overview

When developers use AI coding tools like Cursor, GitHub Copilot, or Windsurf, Weave automatically tracks and attributes the code contributions. The system ensures that:

* Human developers receive full credit for driving the work
* AI contributions are accurately measured
* Attribution adapts based on available data quality
* Teams get clear visibility into AI tool effectiveness

## Attribution strategies

Weave employs multiple attribution strategies, automatically selecting the most accurate method based on available data:

### 1. Detailed API data (most accurate)

<div className="bg-primary/5 p-4 rounded-lg mb-4">
  <strong>Used with:</strong> Cursor Enterprise
</div>

When AI tools provide detailed API data about their contributions, Weave uses this as the primary source of truth. This includes:

* **Cursor's AI Code Tracking API**: Available with Cursor Team/Business plans, this API provides exact line-by-line attribution for every commit

**How it works:**

1. The AI tool reports exactly how many lines it generated or modified and which commits were
   involved in the modification
2. Weave attributes those specific lines to the AI tool
3. Remaining lines are attributed to human developers
4. Multiple AI tools can be tracked simultaneously

**Example calculation:**

```
Commit with 100 lines changed:
- Cursor API reports 70 lines AI-generated
- Attribution: 70% AI, 30% human
- Human still receives full output credit for driving the work
```

### 2. Co-authorship metadata

<div className="bg-primary/5 p-4 rounded-lg mb-4">
  <strong>Used with:</strong> Any AI tool that appears as a Git co-author
</div>

Many AI tools are configured to appear as co-authors in Git commits. When this metadata is available, Weave applies intelligent attribution rules:

**Default split:**

* When an AI tool is listed as a co-author, attribute 65% to AI and 35% to the developer
* The developer retains full output credit
* This reflects the significant contribution AI tools make to code generation

**Multiple contributors example:**

```
Commit authored by: Alice
Co-authored by: Bob, Cursor, Copilot

Attribution breakdown:
1. First, split between unique humans: Alice 50%, Bob 50%
2. Then apply AI attribution (35% human / 65% AI):
   - Alice's 50% → 17.5% solo + 16.25% Cursor + 16.25% Copilot
   - Bob's 50% → 17.5% solo + 16.25% Cursor + 16.25% Copilot
```

### 3. Daily coding patterns

<div className="bg-primary/5 p-4 rounded-lg mb-4">
  <strong>Used with:</strong> All AI tools when direct attribution isn't
  available
</div>

For AI tools without API data or co-authorship information, Weave analyzes daily coding patterns to estimate AI contribution:

**The analysis considers:**

* Lines of code written during AI tool usage periods
* Comparison with the developer's typical output patterns
* Time of day and coding velocity changes

**Weighted attribution formula:**

```
AI percentage = (AI LOC) / ((AI LOC) + (Human LOC × 0.6667))
```

The 0.6667 multiplier (equivalent to 2:3 ratio) gives appropriate weight to human contributions, recognizing that human-written code often requires more thought and decision-making per line.

### 4. Priority resolution

When multiple data sources are available for the same contribution, Weave uses a priority system to avoid double-counting:

1. **API data** (highest priority) - Most accurate, real-time data
2. **Co-authorship metadata** - Git-level attribution
3. **Activity telemetry** - Tool usage patterns
4. **Daily coding patterns** (lowest priority) - Pattern-based estimates

This ensures the most accurate data source is always used.

## Special cases

### Claude Code attribution

Claude Code (including Claude.ai usage) has special handling due to multiple possible data sources:

```
Priority order:
1. API activity records (most current)
2. Git telemetry data
3. CSV usage exports (least current)
```

### Multiple AI tools

When multiple AI tools contribute to the same code:

* Each tool's contribution is tracked independently
* Contributions are never double-counted
* The human developer receives credit for orchestrating all AI tools

### No AI detection

When no AI assistance is detected in a commit:

* Multiple human authors receive equal attribution
* Each co-author gets an equal share of the output value
* No AI attribution is applied

## Output credit vs. AI attribution

It's important to understand the distinction:

* **Output Credit**: The human developer always receives full credit for output when using AI tools, as they are driving the work
* **AI Attribution**: Tracks what percentage of the actual code was AI-generated

This dual tracking ensures:

* Developers aren't penalized for using AI tools efficiently
* Teams can measure AI tool adoption and effectiveness
* Individual productivity metrics remain fair

## Configuration

Organizations can configure AI attribution through:

1. **Tool Integration**: Connect AI tools that provide API data for most accurate attribution
2. **Git Configuration**: Ensure AI tools are properly configured as co-authors

## Best practices

To ensure accurate AI attribution:

1. **Use enterprise AI tools** when possible for API-level accuracy
2. **Configure Git co-authorship** for AI tools in your workflow
3. **Review attribution data** regularly to understand AI impact
4. **Communicate the approach** to your team - using AI is encouraged, not penalized


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
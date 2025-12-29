# AI efficiency index

> A composite score measuring how effectively your team uses AI coding tools

## How it works

The AI efficiency index is a composite metric that combines four AI-related metrics into a single 0-100 score. It helps you understand how effectively your team is leveraging AI tools by balancing output, adoption, cost, and code quality.

A higher score indicates better overall AI tool usage - high output and adoption, reasonable costs, and low code churn.

## Calculation

The AI efficiency index uses **percentile-based normalization** to combine metrics with different scales. Each component is converted to a percentile rank (0-100) based on global benchmarks, then combined with equal weighting.

**Formula:**

```
AI efficiency index = (AI output percentile x 0.25) +
                      (AI usage percentile x 0.25) +
                      (AI cost percentile x 0.25) +
                      (code turnover percentile x 0.25)
```

### Component metrics

| Component           | Weight | Description                                    | Direction        |
| ------------------- | ------ | ---------------------------------------------- | ---------------- |
| AI output volume    | 25%    | Total code output from AI-assisted PRs         | Higher is better |
| AI usage percentage | 25%    | Percentage of total output that is AI-assisted | Higher is better |
| AI cost per user    | 25%    | Monthly spending on AI tools per user          | Lower is better  |
| Code turnover rate  | 25%    | Percentage of code reworked within 90 days     | Lower is better  |

### Percentile normalization

Since these metrics have different scales (percentages, dollars, lines of code), we convert each to a percentile rank before combining them:

1. Your value is compared against global benchmark data from all organizations
2. A percentile rank (0-100) indicates where you fall in that distribution
3. For "lower is better" metrics (cost and turnover), the percentile is inverted so that higher always means better

**Example:** If your AI cost is in the 20th percentile (low cost = good), it becomes the 80th percentile rank in the efficiency calculation.

## Technical details

<AccordionGroup>
  <Accordion icon="calculator" title="How are components calculated?">
    **AI output volume**

    * Source: Lines of code in merged PRs that had AI tool involvement
    * Normalized per day for fair comparison across time periods

    **AI usage percentage**

    * Formula: AI Code Output / Total Code Output
    * Displayed as 0-100%

    **AI cost per user**

    * Source: Aggregated spending from connected AI tools (Claude Code, Cursor, GitHub Copilot, etc.)
    * Normalized per month

    **Code turnover rate**

    * Measures how much code is changed or deleted within 90 days of being merged
    * See [code turnover](/metrics/code-turnover) for details
  </Accordion>

  <Accordion icon="circle-question" title="What if a component is missing?">
    All four component metrics must be present to calculate the efficiency index. If any component is missing for a given time period, that data point is skipped.

    This ensures the score is always based on complete data rather than partial calculations.
  </Accordion>

  <Accordion icon="chart-line" title="What data sources are used?">
    The AI efficiency index pulls data from:

    * GitHub, GitLab, and Bitbucket for code output and turnover
    * Connected AI tools for usage and cost data (Claude Code, Cursor, GitHub Copilot, Windsurf, etc.)
  </Accordion>
</AccordionGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
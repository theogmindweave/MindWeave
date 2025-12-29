# Review efficiency index

> A composite score measuring the effectiveness of your code review process

## How it works

The review efficiency index is a composite metric that combines three code review metrics into a single 0-100 score. It helps you understand how effective your team's code review process is by measuring resolution rates, review quality, and turnaround time.

A higher score indicates a more effective review process - comments are being resolved, reviews are high quality, and turnaround is fast.

## Calculation

The review efficiency index uses **percentile-based normalization** to combine metrics with different scales. Each component is converted to a percentile rank (0-100) based on global benchmarks, then combined with equal weighting.

**Formula:**

```
review efficiency index = (comment resolution percentile / 3) +
                          (review quality percentile / 3) +
                          (review turnaround percentile / 3)
```

### Component metrics

| Component               | Weight | Description                                                | Direction        |
| ----------------------- | ------ | ---------------------------------------------------------- | ---------------- |
| Comment resolution rate | 33%    | Percentage of suggestion comments resolved by code changes | Higher is better |
| Code review quality     | 33%    | Quality score of code reviews (0-100 scale)                | Higher is better |
| Code review turnaround  | 33%    | Median time from review request to completion              | Lower is better  |

### Percentile normalization

Since these metrics have different scales (percentages, scores, time), we convert each to a percentile rank before combining them:

1. Your value is compared against global benchmark data from all organizations
2. A percentile rank (0-100) indicates where you fall in that distribution
3. For "lower is better" metrics (turnaround time), the percentile is inverted so that higher always means better

**Example:** If your review turnaround is in the 10th percentile (very fast = good), it becomes the 90th percentile rank in the efficiency calculation.

## Technical details

<AccordionGroup>
  <Accordion icon="calculator" title="How are components calculated?">
    **Comment resolution rate**

    * Measures the percentage of suggestion/nitpick comments that are resolved by code changes
    * Formula: `Resolved Comments / Total Suggestion Comments`

    **Code review quality**

    * Uses a sigmoid transformation to scale raw review ratings to 0-100
    * Formula: `100 / (1 + e^(-(rating - 800) / 250))`
    * A rating of 800 maps to approximately 50
    * See [review quality](/metrics/review-quality) for more details

    **Code review turnaround**

    * Measures the median time between when a review is requested and when it's completed
    * See [review turnaround](/metrics/review-turnaround) for more details
  </Accordion>

  <Accordion icon="circle-question" title="What if a component is missing?">
    All three component metrics must be present to calculate the efficiency index. If any component is missing for a given time period, that data point is skipped.

    This ensures the score is always based on complete data rather than partial calculations.
  </Accordion>

  <Accordion icon="chart-line" title="What data sources are used?">
    The review efficiency index pulls data from:

    * GitHub
    * GitLab
    * Bitbucket
  </Accordion>
</AccordionGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
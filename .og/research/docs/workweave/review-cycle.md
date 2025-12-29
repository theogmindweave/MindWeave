# Review cycles

> Number of review rounds per PR before merge

## How it works

Review cycle measures the average number of review rounds a PR goes through before being merged. This metric is tracked from the PR author's perspective.

A **review round** is a group of consecutive reviews (from any reviewer) uninterrupted by a code update from the PR author. Each time the author pushes new code in response to feedback, a new round begins.

For example:

```
PR Created → Review A → Review B → Code Update → Review C → Approval → Merge
            └──── Round 1 ────┘                └──── Round 2 ─────┘
```

This PR has 2 review rounds.

## What it indicates

* **1 round** is ideal—the PR was approved on the first review
* **Higher values** may indicate PRs that need more rework, unclear requirements, or opportunities to improve code quality before review

## Common causes of high review cycles

* Large or complex PRs that require multiple rounds of feedback
* Unclear requirements leading to revisions
* Code quality issues that need to be addressed

<Note>
  The following are excluded from this metric: - Self-reviews (where the PR
  author reviews their own PR) - Reviews that occur after the PR is merged -
  Reviews from AI tools (e.g., Copilot, CodeRabbit)
</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
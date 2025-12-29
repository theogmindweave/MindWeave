# Ignored PRs

> Weave automatically excludes ignored PRs from metrics

## How it works

Weave uses an AI agent to determine which PRs should not be included in metrics. We consider a PR
ignored, and exclude it from metrics, if it is **not the result of human/AI effort**.

These PRs typically fall into one of three buckets:

* PRs that move code from one branch to another (for example: moving the latest `main` branch to
  `production`)
* PRs that bump versions (for example: Dependabot-style PRs)
* PRs that run linters or other codemod tools (for example: adding a new lint rule and running it on
  the entire codebase)

## Improving detection

The ignored PR detection is smart but it's not perfect. To improve its accuracy, you can manually
mark a PR as ignored or not by flipping its ignored toggle. Over time, Weave will learn from your overrides and improve its categorization accuracy.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
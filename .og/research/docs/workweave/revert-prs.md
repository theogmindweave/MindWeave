# Reverted PRs

> Count of PRs that revert previous changes

## How it works

Counts pull requests that undo previous changes. Weave detects reverts by analyzing PR titles and descriptions for revert patterns (e.g., `Revert "..."` titles or GitHub's auto-generated `Reverts owner/repo#123` text).

## Interpretation

Reverts can indicate bugs that slipped through review, production incidents, or intentional rollbacks (delayed feature launches, A/B test results, changed requirements).

A steady pattern of reverts may warrant investigation into code review practices or testing coverage. Use alongside [bugs introduced](/metrics/bugs-introduced) and [code turnover](/metrics/code-turnover) for context.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
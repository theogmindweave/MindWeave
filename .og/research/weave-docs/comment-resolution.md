# Comment resolution

> Track whether PR review comments were resolved by code changes

## How it works

Tracks whether review feedback results in code changes. Weave analyzes comments left during review and checks if subsequent commits address them.

### Calculation method

Weave uses AI analysis to determine if a comment was resolved:

1. **Comment selection** — Only analyzes comments from merged PRs. Focuses on "suggestion" comments (proposed improvements), excluding questions and praise that don't require code changes.

2. **Commit analysis** — For each comment, examines all commits made after the comment was created but before the PR was merged. Analyzes the commit's file changes, diff content, and code modifications.

3. **Resolution detection** — Uses AI to determine if a commit directly and completely addresses the specific feedback in the comment. The commit must:

   * Address the exact concern raised in the comment
   * Modify the specific file and lines referenced
   * Fully resolve all points mentioned (not partial fixes)

4. **Confidence levels** — Each resolution is assigned a confidence level (very high, high, medium, low) based on how clearly the commit addresses the comment.

5. **Context consideration** — Incorporates thread replies and broader PR conversation context to better understand if feedback was acknowledged or addressed.

## Comment intents

Comments are categorized by intent to focus analysis on actionable feedback:

* **Suggestion** — Proposed improvements (expected to result in changes)
* **Question** — Clarification requests (may or may not result in changes)
* **Praise** — Positive feedback (no changes expected)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
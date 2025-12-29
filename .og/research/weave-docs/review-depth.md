# Review depth

> Weave's proprietary algorithm for categorizing the depth of review a PR received

## How it works

Weave uses an AI agent to categorize PRs based on the depth of the review they received before being
merged. There are three categories: **full**, **rubber stamp**, and **none**.

The algorithm is fairly straightforward:

1. Was there any review on the PR at all? If not, it's categorized as **none**
2. Was the PR complex enough to warrant a nontrivial review? If not, it's categorized as a **full** review.
   * For example, if a PR just fixes a typo, then any review will be categorized as a full review
     (even if there are no comments at all).
3. Did the reviewer(s) meaningfully review the PR and provide any meaningful feedback on the PR? If
   so, it's categorized as a **full** review. Otherwise, it's categorized as a **rubber stamp** review.

<Note>Self-reviews (where the PR author reviews their own PR) are excluded from this metric.</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
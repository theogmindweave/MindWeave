# Bugs introduced

> Track which commits and engineers introduced bugs that were later fixed

## Overview

The **bugs introduced** metric identifies commits that introduced bugs which were later fixed in bug-fix PRs. Unlike [bug ratio](/metrics/bug-ratio), which measures the proportion of output spent on fixes, bugs introduced traces bugs back to their source—helping you understand where bugs originate and who introduced them.

This enables powerful insights like:

* Which code changes are most likely to introduce bugs
* Patterns in when and how bugs get introduced
* Attribution of bug introductions to individuals or teams
* Correlation between AI-assisted code and bug introduction rates

## How it works

When a bug-fix PR is merged, Weave's Bug Finder traces the bug back to its source:

1. **Analyze the fix** — Parse the PR to understand what bug was fixed and which code sections changed
2. **Extract traceable lines** — Identify deleted/modified lines (not additions) that can be traced back
3. **Rank sections** — Use AI to rank which sections most likely contained the bug (based on logic complexity, error-prone patterns, etc.)
4. **Git blame** — Trace each section's history back up to 5 commits to find candidate source commits
5. **Score candidates** — AI evaluates each candidate's code changes to assess if it introduced the bug
6. **Final ranking** — Assign each candidate a confidence level based on the evidence

## Metric filtering

Only high-quality bug attributions are included in the metric. A bug introduction is counted when
the confidence level is **medium, high, or very high**. Low confidence bug attributions are not
tracked but not shown.

## Time attribution

Bugs are attributed to the time when the **buggy code was originally written**, not when the bug was detected or fixed. This gives you an accurate picture of when bugs are being introduced, even if they're discovered much later.

## Confidence levels

| Level         | Description                                                                        |
| ------------- | ---------------------------------------------------------------------------------- |
| **Very High** | 99%+ certain. The code changes directly introduce the exact problematic logic.     |
| **High**      | Strong evidence with clear overlap in logic and behavior.                          |
| **Medium**    | Plausible connection—the code touches related areas but the link isn't definitive. |
| **Low**       | Weak or speculative connection. Not included in the metric.                        |

## Relationship to bug ratio

| Metric                          | Measures                                | Attribution                          |
| ------------------------------- | --------------------------------------- | ------------------------------------ |
| [Bug ratio](/metrics/bug-ratio) | Proportion of output spent on bug fixes | To the person who fixed the bug      |
| Bugs introduced                 | Number of bugs traced to their source   | To the person who introduced the bug |

Both metrics are valuable: Bug ratio helps you understand how much effort goes into fixing bugs, while bugs introduced helps you understand where bugs come from.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
# Code turnover

> Weave's proprietary algorithm for measuring how much code is reworked after it's merged

## How it works

Code turnover quantifies the amount of code that is reworked or removed after it's merged.

To calculate it, Weave will:

1. Note all the lines changed in the PR (ignoring meaningless lines like whitespace, brackets, etc.)
2. For every subsequent PR, note any cases where a line from the initial PR is changed or deleted.
   * Special case: if a line is *moved* in a later PR, that change is ignored; so if that line is
     later deleted, it will count as code turnover for the original PR.
3. Calculate the ratio of changed lines to total lines.

For example, if a PR has 100 lines changed, and 20 lines are changed or deleted in a later PR, the
code turnover is 20/100 = 20%.

We only count code turnover within 90 days of the initial PR.

## Is code turnover bad?

Not necessarily! It depends on the situation.

For example, if a team is working on an experimental feature and releasing it behind a feature flag,
it is normal and even expected to significantly rework that code before shipping it to all users. In
that case, a higher code turnover is expected.

Code turnover is most interesting as a relative metric. For example, if a single team has
significantly higher turnover than other teams, that team might need to improve their code review
process or test coverage.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
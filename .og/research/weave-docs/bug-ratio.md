# Bug ratio

> The proportion of code output spent on fixing bugs

## How it works

Bug ratio measures what percentage of your team's code output is spent on fixing bugs versus building features or doing other maintenance work.

To calculate it, Weave will:

1. Measure the total code output for the time period
2. Identify which PRs are categorized as "bug" fixes using Weave's [PR type categorization](/analysis/type-categorization)
3. Measure the code output from bug-fix PRs
4. Calculate the ratio: bug output / total output

## What is a bug PR?

A PR is categorized as a "bug" if it fixes something that is broken or not working as intended. This includes:

* Fixing customer-reported issues
* Addressing security vulnerabilities
* Correcting calculation errors
* Fixing UI elements that aren't displaying correctly
* Mitigating crashes or failing requests

Weave uses an AI agent to automatically categorize PRs, but you can manually override the categorization if needed. See [PR type categorization](/analysis/type-categorization) for more details.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
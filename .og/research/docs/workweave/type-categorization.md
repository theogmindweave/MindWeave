# PR type categorization

> Weave's proprietary algorithm for categorizing PRs

## How it works

Weave uses an AI agent to categorize every PR into one of the following types:

### Feature

A feature PR introduces new functionality or innovation.

<Accordion icon="sparkles" title="Examples">
  * Adding a new user dashboard
  * Implementing a new search algorithm
  * Creating a new API endpoint
  * Adding a new report type
</Accordion>

### Bug

A "bug" PR fixes something that is broken or not working as intended.

<Accordion icon="bug" title="Examples">
  * Fixing a login issue reported by users
  * Addressing a security vulnerability
  * Correcting a calculation error
  * Fixing a UI element that's not displaying correctly
</Accordion>

### KTLO (Keeping The Lights On)

KTLO PRs represent maintenance work that keeps the system running but doesn't introduce new
functionality. Anything that's not a feature or a bug is categorized as KTLO.

<Accordion icon="wrench" title="Examples">
  * Refactoring a module for better maintainability
  * Improving database query performance
  * Updating documentation
  * Adding new tests
  * Moving code between repositories
  * Deploying to new environments
  * Making debugging tools more accessible
</Accordion>

## Improving categorization

The PR type categorization is smart but it's not perfect. To improve its accuracy, you can manually
override the categorization. To do so, click on the PR type and select the correct category:

<img style={{ maxHeight: "400px", margin: "0 auto" }} noZoom src="https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/pr-type-categorization-edit.png?fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=80e9878ce30924e6b8192cdd11c30530" alt="Edit PR type categorization" data-og-width="488" width="488" data-og-height="499" height="499" data-path="images/pr-type-categorization-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/pr-type-categorization-edit.png?w=280&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=d880d391be1ade39683afa3a4637dde6 280w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/pr-type-categorization-edit.png?w=560&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=da1fec8f44e983d7e8b8c3cf579ec76f 560w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/pr-type-categorization-edit.png?w=840&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=deb79ad6954d9e9bbf335d42bc16ad3b 840w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/pr-type-categorization-edit.png?w=1100&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=420fac44c7ad7670161799b66ceb532e 1100w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/pr-type-categorization-edit.png?w=1650&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=c7380be00822c26eaf95605c2c0ceaba 1650w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/pr-type-categorization-edit.png?w=2500&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=d3fd4753470ccc5b7cde40e974427b64 2500w" />

Over time, Weave will learn from your overrides and improve its categorization accuracy.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
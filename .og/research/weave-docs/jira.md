# Jira

> Connect Jira to track task completion and delivery metrics

Connect Jira to sync your issues, epics, and project data for task-based metrics.

## What's synced

* Issues and their status
* Epics and story points
* Sprint data
* Project structure
* Assignees and reporters

## Connecting Jira

<Steps>
  <Step title="Start connection">
    Go to **Data** and click **Connect** on Jira
  </Step>

  <Step title="Authorize Weave">
    Sign in to Jira and authorize the Weave app
  </Step>

  <Step title="Select projects">
    Choose which projects to sync
  </Step>
</Steps>

## Metrics enabled

Once connected, you can track:

* **Task delivery** — How many tasks are completed over time
* **Task lead time** — Time from creation to completion
* **Points delivered** — Story points completed
* **Bug tasks** — Bug-related issues

## Linking tasks to PRs

Weave automatically links PRs to Jira issues when:

* The PR title or branch name contains the issue key (e.g., `PROJ-123`)
* The PR description mentions the issue key

This enables end-to-end tracking from task creation to code delivery.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
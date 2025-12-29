# Archived members

> Remove users from active tracking while preserving their historical data

## What is archiving?

Archiving is a way to remove team members from your active roster while preserving their historical contributions in your metrics. When someone leaves your organization or no longer needs to be tracked, archiving them keeps your data accurate without losing history.

## Archive vs remove

Weave offers two options for handling departed team members:

| Action      | Historical data           | Billing     | Use case                           |
| ----------- | ------------------------- | ----------- | ---------------------------------- |
| **Archive** | Preserved in metrics      | Not charged | Team member left, contractor ended |
| **Remove**  | Excluded from all metrics | Not charged | Added by mistake, test account     |

<Tip>
  Archive is the recommended action for most departing team members. Only use
  **Remove** when you want to completely erase someone's contributions from your
  metrics history.
</Tip>

## How archived data works

When you archive a member, Weave calculates an "activity period" for that user—from their start date to their archive date. This determines how their data appears in metrics and reports.

### Data that counts

Archived users' contributions **are included** in metrics for time periods **before** they were archived:

* Pull requests they authored
* Code they committed
* Reviews they performed
* Tasks they completed
* AI tool usage

For example, if you archive a user on March 15, their contributions from January through March 14 will still appear in any reports covering those dates.

### Data that doesn't count

Archived users' data is **excluded** from:

* Current member counts and team rosters
* Billable seat calculations
* Metrics for time periods **after** their archive date
* Active user lists in drill-down views for current data

## Managing archived members

### Archiving a member

<Steps>
  <Step title="Go to members">Navigate to **Members** in the sidebar</Step>

  <Step title="Find the member">
    Search or scroll to find the team member you want to archive
  </Step>

  <Step title="Open the menu">
    Click the **⋯** (more options) button on their row
  </Step>

  <Step title="Archive">
    Click **Archive** to move them to the archived state
  </Step>
</Steps>

### Viewing archived members

Archived members appear in a separate **Archived** section on the Members page. Each archived member shows the date they were archived.

### Unarchiving a member

If someone returns to your organization or was archived by mistake:

<Steps>
  <Step title="Find the archived member">
    Go to **Members** and scroll to the **Archived** section
  </Step>

  <Step title="Open the menu">
    Click the **⋯** (more options) button on their row
  </Step>

  <Step title="Unarchive">
    Click **Unarchive** to restore them to active status
  </Step>
</Steps>

When unarchived, the member:

* Returns to the active members list
* Counts toward your billable seats again
* Has their activity period updated to include the new active period

## Related

* [User roles](/features/user-roles) — understanding admin permissions
* [Suggested members](/team-management/suggested-members) — inviting new team members


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
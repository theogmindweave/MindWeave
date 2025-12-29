# User roles

> Understanding access levels in Weave

Weave has four user roles, each with different levels of access to data and settings.

## Role overview

| Role          | Description                                            |
| ------------- | ------------------------------------------------------ |
| **Admin**     | Full access to all settings, data, and team management |
| **Manager**   | View all metrics and reports across the organization   |
| **Team lead** | View data for themselves and teams they belong to      |
| **Member**    | View only their own individual metrics and data        |

## Admin

Admins have complete access to Weave.

<Accordion icon="shield-check" title="Admin capabilities">
  * View all reports and metrics
  * Access organization settings
  * Manage integrations and data sources
  * Invite and manage team members
  * Assign roles to other users
  * Create and manage teams
  * Configure SSO
  * Create custom slash commands
  * Access API keys
</Accordion>

## Manager

Managers can see all organization data but cannot change settings.

<Accordion icon="chart-bar" title="Manager capabilities">
  * View all reports and metrics for all team members
  * Access individual reports for any member
  * View team reports for all teams
  * Use Wooly AI to analyze any data
  * Export data
</Accordion>

## Team lead

Team leads have access scoped to their teams.

<Accordion icon="users" title="Team lead capabilities">
  * View their own individual metrics
  * View team reports for teams they belong to
  * View individual reports for members of their teams
  * Access includes child teams in the hierarchy
</Accordion>

## Member

Members have the most restricted access.

<Accordion icon="user" title="Member capabilities">
  * View their own individual report
  * See their personal metrics and contributions
  * Access may be further restricted by organization settings
</Accordion>

## Page access by role

| Page                  | Admin | Manager |   Team lead  |   Member  |
| --------------------- | :---: | :-----: | :----------: | :-------: |
| Overview report       |   ✓   |    ✓    |       ✓      |     -     |
| Team report           |   ✓   |    ✓    |   Own teams  |     -     |
| Individual report     |   ✓   |    ✓    | Team members | Self only |
| Standup report        |   ✓   |    ✓    |   Own teams  |     -     |
| AI reports            |   ✓   |    ✓    |       ✓      |     -     |
| Quality report        |   ✓   |    ✓    |       ✓      |     -     |
| Process report        |   ✓   |    ✓    |       ✓      |     -     |
| Organization settings |   ✓   |    -    |       -      |     -     |
| Data sources          |   ✓   |    -    |       -      |     -     |
| Members page          |   ✓   |    -    |       -      |     -     |
| Wooly AI              |   ✓   |    ✓    |       ✓      |     -     |

## Changing roles

Only Admins can change user roles.

<Steps>
  <Step title="Go to members">Navigate to **Members** in the sidebar</Step>
  <Step title="Find the user">Search or scroll to find the team member</Step>

  <Step title="Change role">
    Click the role dropdown and select the new role
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
# Suggested members

> Manage your team members and link their multiple identities

## What are suggested members?

Suggested members are individuals who have contributed code (via pull requests) to your connected repositories but are not yet set up as users in Weave.

When you connect a data source like GitHub, GitLab, or Bitbucket, Weave analyzes the history of your repositories to identify all contributors. Anyone who has authored a PR is flagged as a potential team member.

## How it works

Weave continuously scans your connected repositories for new activity. When it finds a PR author who doesn't match an existing Weave user or a known repository connection, they appear in the **Suggested members** list on the [Members page](https://app.workweave.ai/members).

This ensures that you don't miss tracking work from new hires or contributors you might have forgotten to invite.

### Provider specifics

While the general concept is the same, the exact source of suggested members varies slightly by provider:

* **GitHub**: Weave scans the **collaborators** and **organization members** associated with your connected repositories. Any member who has authored a pull request but isn't in Weave will be suggested.
* **GitLab**: Weave scans the **project members** and **group members** of your connected projects. Any member who has authored a merge request but isn't in Weave will be suggested.
* **Bitbucket**: Weave scans your **workspace users** (Cloud) or **project users** (Data Center). Additionally, Weave automatically detects **commit authors** in pull requests and adds them to the suggestion list, even if they are not explicitly listed as workspace members.

> **Note on domains**: If your Weave organization has a configured email domain (e.g., `@acme.com`), Weave will filter suggestions to only include users with matching email addresses (or users with no public email). This helps avoid suggesting external open-source contributors.

## Managing suggestions

For each suggested member, you can take the following actions:

### Invite

If the suggestion represents a valid team member:

1. Click **Invite**.
2. Verify their name and email address.
3. Assign them a role (member or admin) and add them to teams.
4. Click **Send Invite**. This will create their account and send them an email invitation.

### Dismiss

If the suggestion is not relevant (e.g., a bot, a former employee, or an open-source contributor outside your org):

1. Click **Dismiss**.
2. The suggestion will be moved to the "Dismissed" tab and will not appear in the main list. You can restore them later if needed.

## Linking multiple identities

A unique and powerful feature of Weave's member management is the ability to link multiple identities to a single user.

Developers often have different usernames or emails across different platforms (e.g., `@jdoe` on GitHub and `@john.doe` on Bitbucket). Weave allows you to consolidate these into a single profile.

When inviting a suggested member, Weave automatically attempts to find matching identities from other connected platforms based on email or username. You can also manually select multiple connections (e.g., a GitHub user and a GitLab user) to be merged into the new Weave user account.

This ensures that your metrics (like code output and review quality) accurately reflect the total work of an individual, regardless of which platform they used.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
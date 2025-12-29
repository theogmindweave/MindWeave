# SCIM

> Automate user provisioning with SCIM directory sync

SCIM (System for Cross-domain Identity Management) allows for automated user provisioning from your identity provider to Weave.

## Overview

With SCIM enabled:

* User accounts are automatically created when added to your directory
* User accounts are archived when removed from your directory
* User profile changes (name, email) sync automatically
* Directory groups sync as Weave teams
* User roles are assigned based on group membership

## Setting up SCIM

SCIM is configured by the Weave team. Contact [support@workweave.ai](mailto:support@workweave.ai) to set up SCIM for your organization.

You'll need to provide:

* Your identity provider type (Okta, Azure AD, OneLogin, etc.)
* Your organization's WorkOS directory ID

Once configured, you'll receive:

* A SCIM base connector URL
* A Bearer token for authentication
* Instructions for your specific identity provider

## Role provisioning

Weave assigns roles based on group membership using convention-based group names. Create these groups in your identity provider and assign users to set their Weave role:

| IdP Group Name      | Weave Role |
| ------------------- | ---------- |
| `weave-admins`      | Admin      |
| `weave-managers`    | Manager    |
| `weave-team-leads`  | Team Lead  |
| (no matching group) | Member     |

<Note>
  These role groups do not create teams in Weave. They only control role assignment.
</Note>

### Setting up role groups

<Steps>
  <Step title="Create groups in your IdP">
    Create groups named exactly `weave-admins`, `weave-managers`, and/or `weave-team-leads` in your identity provider
  </Step>

  <Step title="Assign users">
    Add users to the appropriate group based on their desired Weave role
  </Step>

  <Step title="Push groups via SCIM">
    Configure your IdP to push these groups to Weave via SCIM
  </Step>
</Steps>

Users can only have one role. If a user belongs to multiple role groups, the highest-privilege role is assigned (Admin > Manager > Team Lead > Member).

## Group to team sync

All directory groups (except the role groups above) automatically sync as Weave teams:

* When a group is created, a corresponding team is created in Weave
* When users are added/removed from a group, team membership updates automatically
* When a group is renamed, the team name updates
* When a group is deleted, the team is unlinked (not deleted) from SCIM

Teams created via SCIM have their membership managed entirely through your identity provider.

## User sync

Weave keeps the following user properties in sync:

| Property      | Source                        |
| ------------- | ----------------------------- |
| Email         | Primary email from directory  |
| Name          | First name + last name        |
| Active status | User state (active/suspended) |

When a user is marked inactive or deleted in your directory, their Weave account is archived (not deleted) to preserve historical data.

## Managing SCIM

Once SCIM is configured, you can manage it from **Settings > Directory Sync**:

* **Enable/Disable**: Toggle SCIM sync on or off
* **Trigger Sync**: Manually trigger a full sync
* **View Status**: See when the last sync occurred

## Disabling SCIM

When SCIM is disabled:

* SCIM requests from your identity provider are rejected
* Teams linked to groups are unlinked
* Users remain in their current state (not archived)
* Manual user and team management is re-enabled

If you re-enable SCIM later, you may need to trigger a full sync from your identity provider to reconcile any changes made while SCIM was disabled.

## Supported identity providers

SCIM should work with most SCIM 2.0 compatible identity providers. We have tested with:

* Okta
* Azure AD (Entra ID)
* OneLogin
* Google Workspace

Contact support if you need help configuring a specific provider.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
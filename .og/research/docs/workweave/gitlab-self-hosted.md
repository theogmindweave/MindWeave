# GitLab (self-hosted)

> How to connect your self-hosted GitLab instance to Weave

## Setup

To set up a self-hosted GitLab instance, you need to create an application in GitLab. This allows
you and your organization members to authenticate using your GitLab instance, and allows Weave to
access your instance's API on your behalf.

1. Go to the [data sources page](https://app.workweave.ai/data)
2. On the GitLab card, click **Connect self-hosted** button
3. Follow the instructions to create an application in GitLab
4. Select the repositories you want to connect to Weave
5. Go to the [members page](https://app.workweave.ai/members) and ensure everyone from your GitLab
   instance is added as a Weave user.

## Limitations

You can connect to multiple self-hosted GitLab instances, or to both self-hosted and cloud GitLab.
However, each user in Weave can only be connected to a single GitLab user.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
# Goal lines

> Set custom performance targets for your team with goal lines on charts

## What are goal lines?

Goal lines are reference lines that you can add to charts to visualize performance targets. They help teams understand how current performance compares to desired goals, making it easy to track progress toward objectives.

Goal lines can be set at three different levels:

* **Individual**: Set specific targets for individual team members on their personal charts
* **Team**: Set shared targets for entire teams on team-level charts
* **Organization**: Set company-wide targets visible on organization charts

## How to configure goal lines

### Setting a goal line

1. Navigate to any supported chart (see [Supported charts](#supported-charts) below)
2. Click the settings icon in the top right corner of the chart
3. In the "Goal Line" section, enter your target value
4. The goal line will immediately appear on the chart as a reference line

You can set goal lines in two ways:

* **By value**: Enter a specific numeric target (e.g., "50 LOC/day")
* **By percentile**: Enter a percentile rank to automatically set the goal to match that benchmark (e.g., "90th percentile")

### Updating or removing a goal line

To update an existing goal line, simply enter a new value in the chart settings. To remove a goal line, clear the value field.

### Visibility settings

By default, goal lines are only visible to managers and admins. Organization admins can configure visibility:

1. Click the settings icon in the top navigation bar
2. Navigate to **Dashboard Settings > Annotations**
3. Toggle the "Show goal lines to individual users" setting

When enabled, all team members can see goal lines on their charts. When disabled, only managers and admins see them.

## Default settings

Goal lines have conservative defaults to give you full control:

| Setting                 | Default Value | Description                                                       |
| ----------------------- | ------------- | ----------------------------------------------------------------- |
| **Display goal lines**  | `false`       | Goal lines are hidden by default until you enable them            |
| **Show to individuals** | `false`       | Only managers/admins can see goal lines by default                |
| **Initial goal lines**  | None          | No goal lines are set automatically - you configure them manually |

These defaults ensure that goal lines are only shown when you're ready to use them, and that you can set targets privately before sharing them with your team.

## Supported charts

Goal lines are available on the following output charts:

### Individual charts

* **Code output** - Lines of code produced per engineer
* **Pull requests** - Number of pull requests created per engineer

### Team charts

* **Total output** - Total lines of code produced by the team
* **Output per engineer** - Average lines of code per team member

### Organization charts

* **Total output** - Organization-wide code output
* **Output per engineer** - Average lines of code across the entire organization

### Standup charts

* **Total output** - Total lines of code for standup context
* **Output per engineer** - Average output per engineer in standup

## How goal lines work with time granularity

Goal lines automatically adjust based on the time granularity you're viewing:

* If you set a goal of "50 LOC/day" and switch to weekly view, it will display as "350 LOC/week"
* Goal values are stored as daily rates and converted for display
* This ensures consistent targets regardless of how you view the data

## Permissions

Goal lines respect your organization's permission structure:

* **Managers and admins**: Can always see and set goal lines
* **Individual team members**: Can see goal lines only if the "Show to individuals" setting is
  enabled


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
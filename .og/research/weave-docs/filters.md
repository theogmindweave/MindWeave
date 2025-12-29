# Filters and granularity

> Filter your data by date, team, user, and more

Filters let you focus on specific subsets of your data across all Weave reports.

## Filter types

| Filter     | Description                   | Shortcut |
| ---------- | ----------------------------- | -------- |
| Date       | Filter by time range          | `D`      |
| User       | Filter by team member         | `U`      |
| Team       | Filter by team                | `T`      |
| Repository | Filter by repository          | `R`      |
| Project    | Filter by Jira/Linear project | `P`      |
| AI tool    | Filter by AI coding assistant | `A`      |

## How to add filters

There are several ways to add filters:

1. **Click the filter bar** at the top of any report
2. **Press `F`** to open the add filter menu
3. **Use shortcuts** like `D` for date, `T` for team, etc.
4. **Use the command menu** (`⌘K`) and search for filters

## Time granularity

Control how data is grouped over time:

| Granularity | Best for                            |
| ----------- | ----------------------------------- |
| Day         | Short time ranges, daily standups   |
| Week        | Most reports (default)              |
| Month       | Quarterly reviews, long-term trends |
| Quarter     | Annual planning                     |
| Year        | Multi-year comparisons              |

Press `G` to change granularity, or click the granularity pill in the filter bar.

## Default date ranges

Different reports have different default date ranges:

| Report              | Default range |
| ------------------- | ------------- |
| Most reports        | Last 3 months |
| Standup             | Current week  |
| R\&D Capitalization | Year to date  |

## Combining filters

You can apply multiple filters at once. For example:

* Date: Last 30 days + Team: Backend + Repository: API

Filters are combined with AND logic—data must match all active filters.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
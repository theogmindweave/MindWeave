# Benchmarks

> Industry benchmarks to compare your team's performance against similar organizations

## What are benchmarks?

Benchmarks allow you to compare your team's performance against industry standards. Weave calculates benchmarks from real data across thousands of engineering organizations, segmented by organization size to ensure fair comparisons.

## How to configure benchmarks

In the top right corner of any page, click the settings icon to configure your benchmarks.

<img style={{ maxHeight: "400px", margin: "0 auto" }} src="https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/benchmark-options.png?fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=fcad3b0031f42728b16797bddd118dc4" alt="Benchmarks settings" data-og-width="303" width="303" data-og-height="261" height="261" data-path="images/benchmark-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/benchmark-options.png?w=280&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=c17d0ef1b3bf44f79feeaeaf7a67a068 280w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/benchmark-options.png?w=560&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=8ec8c6495bc84eca154ed7d45736cb44 560w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/benchmark-options.png?w=840&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=f9bb0fc12105a8fbf9211eea1827aed8 840w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/benchmark-options.png?w=1100&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=b703e26b07ac9e15946704efa5937f6a 1100w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/benchmark-options.png?w=1650&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=38d6faec68b581caded20d7dbba5f204 1650w, https://mintcdn.com/weave-50313446/CXI5lD0k_us8oXPb/images/benchmark-options.png?w=2500&fit=max&auto=format&n=CXI5lD0k_us8oXPb&q=85&s=421a6f5088f8a8a829bf6d35d191b088 2500w" />

## Organization size buckets

Benchmarks are calculated separately for different organization sizes, since team dynamics and performance characteristics vary significantly between small startups and large enterprises.

| Bucket                | Description              |
| --------------------- | ------------------------ |
| **1-5 engineers**     | Small teams and startups |
| **6-10 engineers**    | Growing startups         |
| **11-20 engineers**   | Mid-size teams           |
| **21-50 engineers**   | Established companies    |
| **51-100 engineers**  | Large teams              |
| **101-200 engineers** | Enterprise teams         |
| **201+ engineers**    | Large enterprises        |

Your organization is automatically placed in the appropriate bucket based on the number of engineers with at least one team membership.

## Benchmark types

### Percentile benchmarks

Percentile benchmarks show how your metrics compare to the broader industry:

* **Median (50th percentile)**: The middle value - half of organizations perform better, half perform worse
* **Top 10% (90th percentile)**: High-performing organizations - only 10% of organizations perform better

These appear as reference lines on time-series charts.

**Percentile rank** is a score from 0-100 showing where your performance ranks. For example, a rank of 85 means you're performing better than 85% of similar organizations. Higher percentile ranks always indicate better performance - for metrics where lower values are better (like code review turnaround), the rank is automatically inverted.

### Organizational benchmarks

These benchmarks compare your performance to other reference points:

* **Company average**: Your organization's overall average performance
* **Team average**: Your team's average performance (when available)

Note: on an [individual report page](/reports/individual), that individual's contributions will be excluded from the team average if they are on the team.

## Supported metrics

Benchmarks are available for the following metrics:

* **Code output per engineer** - How much code each engineer produces
* **PRs per engineer** - Number of pull requests per engineer
* **Code review quality** - Quality scores of code reviews
* **Code review turnaround** - Time to complete code reviews
* **Code LOC turnover** - Rate of code change and refactoring

## How benchmarks are calculated

### Data collection

* **Time period**: 180 days of historical data
* **Data sources**: Real metrics from engineering organizations using Weave
* **Filtering**: Only includes non-generated (human-written) code and PRs

### Scaling by context

Benchmark values are automatically scaled based on how you're viewing the data:

* **Individual/Account view**: Shows per-person benchmarks
* **Team view**: Scales benchmarks by average team size
* **Organization view**: Scales benchmarks by total organization size

For metrics that accumulate over time, values are normalized to per-day rates to ensure fair comparisons regardless of the time period analyzed.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
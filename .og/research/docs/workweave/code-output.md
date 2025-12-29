# Code output

> Weave's proprietary algorithm for quantifying engineering productivity

## How it works

The output score for a PR is the answer to the question: <strong>"how long
would this PR take an expert engineer to complete?"</strong>

The result is a standard unit to quantify output. It's consistent and comparable across individuals,
teams, languages, and organizations.

Unlike flawed metrics like lines of code or number of PRs, our algorithm analyzes source code
changes. It understands the meaning and impact of every change.

| Metric        |                    Understands code?                   |                 Measures productivity?                 | Correlation with effort<sup>1</sup> |
| ------------- | :----------------------------------------------------: | :----------------------------------------------------: | :---------------------------------: |
| # of PRs      |   <Icon icon="x" color="#ef4444" iconType="solid" />   |   <Icon icon="x" color="#ef4444" iconType="solid" />   |                  -                  |
| DORA          |   <Icon icon="x" color="#ef4444" iconType="solid" />   |   <Icon icon="x" color="#ef4444" iconType="solid" />   |                  -                  |
| Lines of code |   <Icon icon="x" color="#ef4444" iconType="solid" />   |   <Icon icon="x" color="#ef4444" iconType="solid" />   |                 0.34                |
| Weave         | <Icon icon="check" color="#157f3c" iconType="solid" /> | <Icon icon="check" color="#157f3c" iconType="solid" /> |        <strong>0.94</strong>        |

## Examples

What does that look like in practice? Here are some example PRs from open source teams:

<CardGroup cols={1}>
  <Card title="PostHog/posthog#25056" icon="github" href="https://github.com/PostHog/posthog/pull/25056">
    Adds backend, frontend, and tests for a new feature

    62 commits across 2 weeks

    <br />

    Output: <strong>15.3</strong>
  </Card>

  <Card title="microsoft/vscode#222315" icon="github" href="https://github.com/microsoft/vscode/pull/222315">
    Refactors code to use a new service and adds new tests

    6 commits across 3 days

    <br />

    Output: <strong>8.4</strong>
  </Card>

  <Card title="facebook/react#27977" icon="github" href="https://github.com/facebook/react/pull/27977">
    Small change with extensive, high effort tests

    Approximately 1 day of work for expert engineer

    <br />

    Output: <strong>5.8</strong>
  </Card>
</CardGroup>

## Technical details

<AccordionGroup>
  <Accordion icon="circle-help" title="How does it work?">
    Weave's code output algorithm combines the world knowledge of an LLM with
    static analysis and a custom ML model.
  </Accordion>

  <Accordion icon="braces" title="How was the model trained?">
    It was trained on a large proprietary data set of PRs, hand labelled by the
    expert engineers that wrote them.
  </Accordion>
</AccordionGroup>

***

<p className="text-sm">
  <sup>1</sup> Source: Weave research, 2024
</p>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
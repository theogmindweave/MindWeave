# AI code percentage

> How much of your code is written by AI?

## How it works

AI code % measures the proportion of code churn (additions and deletions) that is attributed to AI assistants. This metric helps you understand the impact of AI on your team's development process.

It answers the question: <strong>"What percentage of our codebase changes are coming from AI?"</strong>

A high AI code % can indicate strong adoption of AI tools, which could lead to increased productivity. However, it's important to correlate this metric with other quality and output metrics to ensure that AI-generated code is meeting your standards.

## Calculation

The AI code % is calculated as the total lines of code added or deleted by an AI assistant, divided by the total lines of code added or deleted overall, expressed as a percentage. This includes a scaling factor to account for the fact that not all AI-generated code makes it into the final codebase.

**Formula:**
AI code % = AI LOC / (AI LOC + merged LOC × 2/3)

Where:

* **AI LOC** = lines of code written by AI assistants
* **Merged LOC** = lines of code in merged pull requests
* **2/3** = Scaling factor to account for AI code retention

## Technical details

<AccordionGroup>
  <Accordion icon="circle-help" title="What are the assumptions?">
    The calculation of AI code % is based on the following assumptions:

    * **We can't track AI code to merged PRs:** We don't (yet!) have the ability to track code from the editor to a merged PR. Because of that, we have to make an assumption about how much code written by an AI ends up in a merged PR.

    * **60% of AI-written code is kept:** We assume that 60% of the code written by an AI ends up in a merged PR.

    * **Metric is based on churn:** It considers both added and deleted lines of code, not just the net new code. This captures the total activity, including refactoring.
  </Accordion>

  <Accordion icon="braces" title="What counts as AI code?">
    Code is attributed to AI if it originates from a connected AI assistant,
    such as Cursor or Claude Code.
  </Accordion>
</AccordionGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
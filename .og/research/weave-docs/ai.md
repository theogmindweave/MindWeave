# AI

> See how your team is using AI in their engineering work.

## How it works

Weave ties your usage data from [Cursor](https://www.cursor.com/),
[Sourcegraph](https://sourcegraph.com/), [Augment Code](https://augmentcode.com/), and/or [GitHub Copilot](https://copilot.github.com/) to
outputs, so you can see:

* How much is being written by AI code generation tools
* [% of code written by AI](/metrics/ai-code-percentage) code generation tools over time
* The correlation between engineering velocity & AI code generation tool usage.

## Provider-specific notes

<AccordionGroup>
  <Accordion title="GitHub Copilot">
    To get stats from GitHub Copilot, you need to explicitly enable API access.
    To do so, follow the instructions
    [here](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#enabling-copilot-features-in-your-organization)
    and enable "Copilot Metrics API access".

    The Copilot stats do not break numbers down by user, so there is no way to see individual-level usage.

    Also, Copilot does not report the number of lines removed. And it does not report the number of lines affected by accepting chat suggestions, so we estimate each accepted chat suggestion to have added 10 lines of code.
  </Accordion>

  <Accordion title="Sourcegraph">
    Sourcegraph does not split out the number of lines added/removed, so we can
    only count additions.

    Also, Sourcegraph reports characters accepted, not lines, so we approximate by assuming 50 characters per line (based on an
    analysis of thousands of randomly sampled lines of code).
  </Accordion>
</AccordionGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
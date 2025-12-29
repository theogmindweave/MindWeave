# Review quality

> Weave's proprietary algorithm for quantifying code review quality

## How it works

The review quality for a PR is evaluated by an LLM based on three criteria:

### Depth

Did the reviewer clearly go deep and understand the reviewed code at more than just a surface level? Are they giving suggestions on things like architecture or design, not just surface level code style? Are they exhibiting technical leadership?

### Quality of communication

Is the reviewer communicating well with the PR author? Are they being clear about what they're suggesting, and why? Are they being helpful?

### Practicality

Is the reviewer being practical when suggesting changes? Are they allowing the PR to move forward if it's an improvement, even if it's not perfect; or are they being too much of a stickler for things that don't matter as much?

## What it doesn't do (yet)

The review quality metric does not actually review the entire PR. So it doesn't catch errors of
omission. For example, if the PR has a bug and the reviewer misses it, the review quality will not
be affected.

For a tool that can catch errors of omission like this automatically, we recommend [Greptile](https://www.greptile.com/).

<Note>Self-reviews (where the PR author reviews their own PR) are excluded from this metric.</Note>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
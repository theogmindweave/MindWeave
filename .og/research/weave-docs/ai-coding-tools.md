# AI coding tools

> Connect your AI coding assistants to track adoption and impact

Weave integrates with AI coding tools to help you understand how your team uses AI and measure its impact on productivity.

## Supported tools

### Direct integrations

These tools can be connected directly to Weave:

| Tool        | Connection type | What's tracked                             |
| ----------- | --------------- | ------------------------------------------ |
| Cursor      | API key         | IDE usage, code generation, agent activity |
| Windsurf    | API key         | IDE usage, code generation                 |
| Claude Code | API key         | Code generation metrics                    |
| Amazon Q    | S3 integration  | Usage metrics                              |
| Firebender  | API key         | Usage metrics                              |
| Gemini CLI  | API key         | Usage metrics                              |
| Augment     | CSV upload      | Usage metrics                              |
| Sourcegraph | CSV upload      | Usage metrics                              |
| Codex       | API key         | Usage metrics                              |

### Auto-detected tools

These tools are automatically detected from commit metadata:

* GitHub Copilot
* CodeRabbit
* Devin
* Graphite
* Greptile
* Jules
* Junie

## Connecting Cursor

<Steps>
  <Step title="Get your API key">
    Contact your Cursor administrator to get your organization's API key
  </Step>

  <Step title="Add to Weave">
    Go to **Data** → **Cursor** → **Configure** and paste your API key
  </Step>

  <Step title="Wait for sync">
    Weave will begin syncing your Cursor data. This may take a few minutes.
  </Step>
</Steps>

## Connecting Windsurf

<Steps>
  <Step title="Get your API key">Get your API key from Windsurf settings</Step>

  <Step title="Add to Weave">
    Go to **Data** → **Windsurf** → **Configure** and paste your API key
  </Step>
</Steps>

## Connecting Claude Code

<Steps>
  <Step title="Get your API key">
    Get your API key from your Claude Code account
  </Step>

  <Step title="Add to Weave">
    Go to **Data** → **Claude Code** → **Configure** and paste your API key
  </Step>
</Steps>

## Foreground vs background AI

Weave categorizes AI tools into two groups:

**Foreground AI** — Tools that engineers interact with directly:

* Cursor
* Windsurf
* Claude Code
* Copilot
* Firebender
* Gemini CLI
* Augment
* Sourcegraph
* Amazon Q
* Codex
* Junie

**Background AI** — Tools that work automatically in the background:

* CodeRabbit
* Cubic
* Cursor Agent
* Cursor Bugbot
* Devin
* GitHub
* Graphite
* Greptile
* Jules
* Junie Bot
* Wispbit

This distinction helps you understand both active AI usage and passive AI assistance.

## What you can measure

Once connected, you can track:

* **AI code percentage** — What portion of code is AI-generated
* **AI LOC** — Lines of code written with AI assistance
* **AI tool costs** — Spending on AI tools (with subscription tracking)
* **AI efficiency index** — Correlation between AI usage and output
* **AI adoption trends** — How AI usage changes over time


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt
# A way to measure and optimize AI code editors, agents and review tools - Remote

> Weave combines LLMs and domain-specific machine learning to understand engineering work. We understand how much work was done by AI vs. humans. How much AI is helping your team ship faster, if it's having an impact on code quality and code reviews.

### ### ### ### ## ## ## $4.2M seed round led by Moonfire, Burst Capital & Y Combinator

$4.2M seed round led by Moonfire, Burst Capital & Y Combinator

I’m Andrew, the co-founder and CTO at Weave, a software engineering intelligence platform that tells you how well you are using AI and how to use it better. We are used by individual engineers looking to self-improve and engineering leaders trying to optimize AI adoption.

**The problem that got us started**

We originally launched Weave as an engineering productivity measurement tool. After our first ShowHN (here), we faced some well-intentioned push-back but still managed to get our first 50 or so customers in the following months. Teams loved having an alternative to traditional shitty metrics (lines of code, number of PRs, DORA), but we kept getting called "big brother" and never felt as much of a pull as we hoped.

So in June I began reflecting on my chats with tons of CTOs over the past year and realized there's real stress and urgency around getting the most out of AI tools. I chat with dozens of AI-pilled engineers weekly, and while nobody knows exactly what's "best," some teams have clearly figured out how to produce significantly more output.

This made me realize we could build on top of our existing models to answer a different question: how can you and your team measure and maximize output with AI?

To solve this we built 2 suites of products which we are excited to show today! The first is around optimizing your AI setup, the second is around optimizing your AI usage.

**How to optimize your AI setup with Weave**

We need to make sure we are covering the basics in setup so I chatted with the most forward thinking CTOs and we landed on a comprehensive AI adoption checklist. The purpose being: if you complete everything on this list, your remaining AI improvements should come from building better intuition around what tasks to use AI for and actually executing on them. Lmk if you think we missed anything!

Now that we have our AI tools set up, we need to start optimizing them, so we built a Cursor rules linter.

AI coding tools like Cursor and Windsurf work by passing context to models to get them to generate code. If that context isn't high quality, your results suffer. The best way to optimize this is through rules files that get parsed before every request and fed to the LLM. But most teams have terrible rules files that actually hurt their AI coding workflow. Our AI Rules Linter automatically analyzes your GitHub repository and pulls in all your rules files. It checks them against industry-standard heuristics and suggests changes for optimal performance.

Once you finish these two steps, we know there’s nothing on the setup side that’s causing you to move slowly with AI. But there may be still be problems in how you are using it!

**Now to figure out what’s working and what to tweak**

**How do you measure your current performance**

You can't optimize what you don't measure. Our foundational output models provide a metric (Weave Score) that tracks engineering team productivity. This lets you judge the actual impact of your AI tool decisions. Below is our own data at Weave. We've been adopting tools like Windsurf, Claude Code, Cursor, Greptile, and Devin over the past few months. You can clearly see our output trending upward as we've gotten better with these tools.

**How do we know what AI is actually writing**

Since AI tools show up as co-authors and committers in git commits when they generate code directly, we built detection logic to identify these AI contributions across all your repositories. We integrate with all the most popular AI tools: Cursor, Windsor, Devin, Greptile, and more. Don’t even get me start on the Claude Code. They don’t have an API, just a buried configuration option to export OpenTelemetry metadata. On the bright side, I got to learn how to setup an OpenTelemetry collector to receive all the events and send them over to our backend, so we can how people are actually using Claude Code:

Now knowing what’s written by AI we can begin to answer:

**What should be written with AI?**

Building intuition around what AI should do takes months, even for the most forward-thinking engineers I know. We built a model that suggests which PRs could have been written with AI. This helps every developer build intuition on where AI should be used and where it shouldn't. We see lots of teams wasting time on tasks that AI isn't designed for yet.

(Also, sneak peak, we’re going to be building this further upstream to check your tickets ahead of time to see what should be built)

**But what’s the ROI?**

The final step ties everything back to dollars. Weave Score is useful, but CFOs really care about*money*. Since we know what's being created with AI, we can take user-submitted wage data and calculate the financial impact. This gives you a single number representing how much money your organization is saving by adopting AI tools.

If you’re interested in measuring and optimizing your AI usage checkwww.workweave.devand lmk your thoughts!

Article written by

Andrew Churchill

Make AI Engineering Simple

Effortless charts, clear scope, easy code review, and team analysis

Book a demo

Book a demo

Book a demo

Book a demo

Book a demo

Book a demo
# The Problem with Using DORA Metrics To Measure Your Engineering Productivity - Remote

> Weave combines LLMs and domain-specific machine learning to understand engineering work. We understand how much work was done by AI vs. humans. How much AI is helping your team ship faster, if it's having an impact on code quality and code reviews.

## ## ### ### ### ### ## - ## $4.2M seed round led by Moonfire, Burst Capital & Y Combinator

$4.2M seed round led by Moonfire, Burst Capital & Y Combinator

DORA became popular because it appears scientific. 4 metrics. Clean acronym. Google's blessing.

But measuring DevOps process ≠ measuring team productivity!

I’ve spoken with dozens of CTOs who are unknowingly using DORA as a proxy for productivity. They didn’t realize they were measuring the wrong thing.

This article breaks down DORA metrics, highlights where they miss the mark, and offers a better way to approach engineering productivity measurement.

What Are DORA Metrics?

First, quick history lesson if you don’t know what DORA is (if you do skip to the next section). DORA metrics first appeared in the2014 State of DevOps Report. Some of the co-authors of that report would go on tofound DORA(DevOps Research and Assessment) in 2016. They continued to publish these reports annually, and in 2018Google acquired DORA. Since then, they have continued to release the State of DevOps Reportannually.

When people refer to DORA metrics, they are referring to the following set of 4 numbers:

**Deployment Frequency**: How often you deploy code
- **Lead Time for Changes**: Time from commit to production
- **Change Failure Rate**: Percentage of deployments causing failures
- **Time to Recovery**: How quickly you restore service after incidents

The researchers behind DORA used these numbers to attempt to quantify the DevOps processes across hundreds of companies in one standard way. Now, with years of research and Google’s backing, these metrics have become the gold standard for DevOps measurement.

DORA metrics very neatly distill down DevOps*process*into just a few numbers. But crucially, these metrics were never meant to measure*productivity*.

What DORA Metrics Don’t Capture

Deployment Frequency

High deployment frequency feels productive. But whether a single feature was deployed all at once or across several smaller incremental releases, it’s still the same amount of work. I've seen teams game this metric by breaking meaningful updates into dozens of micro-deployments. While it’s great to ship faster, it doesn’t actually mean you’re getting more done.

**What it misses**: how much value is actually delivered in each deployment

Lead Time

Faster lead times are generally good. But similar to deployment frequency, you can cut lead time in half without actually delivering any more value just by splitting work into smaller chunks.

**What it misses**: what the team is accomplishing across all the work it delivers

Change Failure Rate

Change failure rates are a reasonable proxy for software quality, and it’s worth tracking. It’s a useful guardrail metric when trying to optimize for speed.

Time to Recovery

This metric makes it clear what DORA metrics are for: DevOps teams charged with managing production infrastructure. TTR has little to no relevance for product-focused teams, and it certainly doesn’t reflect how productive a team is.

A Better Solution

We built Weave to solve these problems with DORA metrics. Instead of asking "How fast can we deploy?" Weave asks "How much are we getting done?"

We provide:

**Objective output measurements:**By combining LLMs with our own custom ML models, we objectively quantify every PR and tell you how long it would take an expert engineer to complete it.

**AI insights:**We’ll show you exactly the impact AI tools are having on your process and productivity.

**Individual reports:**We built a page for ICs specifically so they can improve themselves. It’s like Whoop for software engineers.

**Code review quality:**It’s easy to see how fast reviews are submitted. It’s hard to know how good they are. Weave solves this using AI to scan every review and quantify its depth, pragmatism, and quality, so you know where to focus.

**Code Review Turnover:**Is the code your team is shipping built to last, or are you running in place? Find out by quantifying how much of your code is being rewritten.

**Cross-Team Visibility & Comparison**: We give insight into how different teams are performing so you can easily compare.

Conclusion

DORA metrics aren't wrong (we have them in our platform) but they are incomplete. They measure the mechanics of software delivery while ignoring the contents.

The question isn't whether you can deploy code quickly. It's whether deploying that code quickly creates value for your business and customers.

Are you measuring what matters?

**Written By:**Andrew Churchill CTO, Co-founder

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
# I spent 3 years as a founding engineer making a huge mistake in my code review process - Remote

> Weave combines LLMs and domain-specific machine learning to understand engineering work. We understand how much work was done by AI vs. humans. How much AI is helping your team ship faster, if it's having an impact on code quality and code reviews.

## ## ## ## ## $4.2M seed round led by Moonfire, Burst Capital & Y Combinator

$4.2M seed round led by Moonfire, Burst Capital & Y Combinator

I spent my previous 3 years as a founding engineer unknowingly creating a massive productivity drain on my team. The culprit wasn't technical debt, unclear requirements, or inadequate tooling. It was something much simpler: I was only doing code reviews once per day.

The Problem I Didn't See

Here's how my review process worked: I'd block out time each morning to go through all pending pull requests. Clean, efficient, organized. If someone submitted a PR at 10:01 AM and I'd already finished my review session at 10 AM, they'd wait until the next day.

This seemed reasonable. Code review is important, but so is deep focus time. Context switching is expensive. Better to batch the work, right?

Wrong.

What I didn't realize was that this created a cascade of slowdowns that compounded across the entire team. Let me walk through what actually happened when reviews took multiple days versus multiple hours.

Good vs. Bad

When an engineer submits a PR and has to wait a full day for feedback, they can't just sit idle. They start working on something else. Now they have two contexts in their head.

The next day, they address review feedback (context switch #1), then go back to the new task (context switch #2). They submit that second PR, wait another day, and start a third task (context switch #3).

By the time they're juggling three or four partially-complete features, each context switch becomes expensive. They're spending significant mental energy just remembering what they were doing and why.

Worse, when feedback finally arrives on a PR that's two days old, the engineer has to reload the entire context of that feature. What problem were they solving? What tradeoffs did they make? Why did they structure the code that way? All of that has to be reconstructed from scratch.

The Data Behind Fast Reviews

I initially dismissed this as a "nice to have" optimization until I discoveredGoogle's researchon code review velocity. They found something counterintuitive: most complaints about code review processes - even seemingly unrelated ones like "reviewers are too nitpicky" or "the standards are too strict" - actually disappear when reviews simply happen faster.

It turns out that review speed affects how people perceive the entire process. A nitpicky review that comes back in two hours feels like helpful feedback. The same review that comes back in two days feels obstructionist.

How to Fix It

The solution isn't complex, but it does require changing your mental model of how code review fits into your day.

Instead of batching reviews into dedicated time blocks, treat review requests as interrupts that take priority over non-urgent work. When you finish a focused coding session—whether that's 30 minutes or 3 hours—check for pending reviews before starting the next task.

This doesn't mean constantly context switching. You still get your deep work time. But you eliminate the artificial delays that force your teammates to juggle multiple incomplete tasks.

Why This Matters More Now

As teams get more distributed and async work becomes the norm, it's tempting to optimize for individual productivity over team velocity. But code review is fundamentally a collaborative process. Optimizing it in isolation creates systemic problems that are much more expensive than the individual cost of occasional context switching.

This is becoming critical in the age of AI-assisted development. AI can generate syntactically correct code that solves the immediate problem while missing broader context about system design, performance implications, or team conventions.

When AI-generated code sits in slow review queues, you get the worst of both worlds: the speed benefits of AI are negated by review bottlenecks, while the quality benefits of human oversight are delayed until the code's context has faded from the author's memory. Fast reviews become essential not just for velocity, but for maintaining code quality in an AI-accelerated development environment.

The fastest individual contributor on a slow-reviewing team will be less productive than a slightly slower individual contributor on a team with tight review cycles. The team dynamics dominate individual optimization.

The fix is simple, but the impact is profound: treat code review as a shared responsibility that takes priority over individual task completion. Your future self—and your teammates—will thank you.

*Credit to my former coworker**Tom McIntyre**, who helped me see that my "efficient" review process was actually the team's biggest bottleneck. Sometimes the most impactful changes are the simplest ones!*

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
# Cursor Analytics: Tracking AI Coding Tool Usage for Engineering Teams - Remote

> Weave combines LLMs and domain-specific machine learning to understand engineering work. We understand how much work was done by AI vs. humans. How much AI is helping your team ship faster, if it's having an impact on code quality and code reviews.

## - ## - ## - ## ## ## $4.2M seed round led by Moonfire, Burst Capital & Y Combinator

$4.2M seed round led by Moonfire, Burst Capital & Y Combinator

Introduction

AI-powered coding tools have rapidly become part of the modern developer’s workflow. In fact, a recent GitHub survey found that over 90% of developers are already using AI coding tools in some capacity [1]. With such widespread adoption, the question for engineering leaders has shifted from*“Should our team use AI assistants?”*to*“How do we measure their impact and value?”*This is where Cursor Analytics comes into play. In this blog, we’ll explore why tracking Cursor usage matters, what metrics are available, and how to leverage those insights. We’ll also discuss the challenge of multiple AI tools in use and how a unified platform can help address fragmented analytics. The goal is to equip CTOs and VPs of Engineering with a comprehensive understanding of Cursor Analytics and how it can drive data-informed decisions in the era of AI-assisted coding.

Why engineering leaders care about AI tool usage

AI coding assistants promise increased developer productivity and faster delivery – but leaders need data to verify these benefits. With most developers jumping on AI tools (84% of developers globally use or plan to use them in their development process [2], simply providing tools like Cursor or GitHub Copilot isn’t enough; engineering managers want to ensure these tools are actually being utilized and adding value. Key questions arise:*Are engineers actively using the AI tool? Is it saving them time? How much code is the AI contributing, and with what quality?*Answering these questions is crucial for evaluating ROI on AI tool investments and guiding strategy.

By tracking usage metrics, leaders can move beyond anecdotal feedback and gut feel. Data from AI tool usage analytics provides visibility into adoption rates, developer engagement, and potential productivity gains. For example, if a team has paid for Cursor’s business licenses, the VP of Engineering will want to see metrics like how often developers invoke Cursor’s AI suggestions and how frequently those suggestions are accepted. High utilization and acceptance might correlate with efficiency gains, whereas low usage or many rejected suggestions could indicate problems – perhaps developers need training, or the AI’s outputs need improvement. In short,*you can’t manage what you don’t measure*. This is why Cursor Analytics is so valuable: it gives engineering leaders a window into how AI is actually used day-to-day, enabling data-driven decisions on tooling and process.

What is Cursors analytics dashboard?

**Cursor**is an AI-enhanced IDE (integrated development environment) that enables “vibe coding” – developers can write code with AI assistance through real-time suggestions, chat-based prompts, and automated code actions. It’s like having an AI pair programmer built into your coding workflow. Cursor’s popularity has surged since its 2023 launch, attracting thousands of developers with promises of faster development cycles. But beyond the coding features, Cursor offers something especially relevant to engineering leaders:**an Analytics Dashboard for teams**.

**Cursor Analytics**is a built-in feature for team admins to monitor how the tool is being used across their organization. The dashboard provides both aggregate and per-user metrics over time [3]. Here’s what you can find in Cursor’s analytics:

**Total Team Usage:**An overview of**aggregate usage stats**for the entire team (e.g. total AI prompts or “tabs” used, and total AI requests made). This gives a high-level sense of how heavily Cursor is being utilized across all developers.
- **Per-User Averages:**Metrics**per active user**, including how many AI suggestion tabs a typical user accepts and how many lines of code are generated with Cursor on average [3]. For instance, you might see that, on average, a developer on your team accepts a certain number of AI-suggested code lines per day.
- **Active User Counts:**Cursor tracks**weekly and monthly active users**in your team [3]. This is similar to DAU/MAU (Daily/Monthly Active Users) in product analytics – it shows how many team members are actually engaging with the AI tool within a given period. A rising trend in active users over weeks or months signals growing adoption, whereas a decline might indicate dropping engagement or potential issues.

Not only can you view these metrics on the dashboard, but team admins can also export detailed analytics reports. Each report includes fine-grained data on user activity and feature usage. For example, Cursor logs how many AI-generated lines of code were suggested to a user versus how many were accepted into the codebase. It tracks events like an engineer applying an AI fix or rejecting a suggestion. By capturing actions such as “Chat Total Accepts” (count of suggestions accepted) and lines of AI code added or deleted, Cursor’s analytics can quantify the tool’s impact on code output. In essence, the Cursor Analytics dashboard turns the nebulous concept of “AI assistant usage” into concrete numbers and charts.

Key metrics in Cursor analytics (and how to use them)

For CTOs and engineering VPs, certain metrics in Cursor Analytics stand out as especially informative. Understanding these key indicators – and how to interpret them – will help you measure the effectiveness of AI assistance on your team. Below are some of the most important metrics and what they tell you:

**Active Users (Engagement):**This metric shows how many developers are actively using Cursor over a given time frame (weekly or monthly active users). A high number of active users (relative to total team size) means the tool has been adopted broadly. Tracking active user trends helps you gauge adoption momentum. For example, if 90% of your engineers used Cursor at least once this month, it’s clearly become a fixture in their workflow. If that percentage is low, you may need to investigate if there are access issues, lack of awareness, or reluctance among the team.
- **AI Suggestions Shown vs. Accepted (Acceptance Rate):**Cursor can report how many AI suggestions were presented to a developer and how many of those were accepted/applied. This essentially measures the acceptance rate of AI-generated code. A higher acceptance rate and a large number of AI-suggested lines accepted indicates that developers find Cursor’s recommendations helpful and are incorporating them into the codebase [4]. A low acceptance rate might mean the suggestions often miss the mark or developers don’t trust them – an opportunity to improve the AI models or provide better training to developers on how to use the tool effectively. Monitoring**lines of code accepted from AI**is particularly insightful; it quantifies how much of your code is written by the AI. For instance, if Cursor suggested 100 lines and 30 of those lines were accepted and merged into the repository, that’s a 30% acceptance rate. Over time, you can track this percentage to see if AI contributions are increasing as the models improve or as developers become more comfortable.
- **Usage Frequency (Activity per User):**Beyond just who is using Cursor, you’ll want to see**how they are using it**. Cursor Analytics provides averages per user for things like “tabs accepted” (the number of suggestion pop-ups a user accepted) and AI requests made. This helps normalize usage: instead of just raw totals (which could be skewed by team size), you can see on average how often each engineer is invoking the AI. If, for example, each active developer uses Cursor to assist with 10 coding tasks per day on average, that shows a high integration into daily work. Usage frequency can be correlated with productivity metrics – if higher Cursor usage frequency aligns with faster completion of tasks or fewer errors, that’s a positive sign.
- **Feature Usage Breakdown:**Cursor’s analytics may also break down different features – such as use of the chat-based assistant, automated code review (BugBot), background agents, etc. For leaders, this breakdown reveals which AI capabilities are most utilized by the team. If you find that the team heavily uses Cursor for code generation via chat but not so much for automated code fixes, it might guide you to promote certain features more (or understand why some features aren’t used). It can also highlight workflow patterns; e.g., maybe developers predominantly use Cursor for refactoring tasks versus initial code writing.

Using these metrics, engineering leaders can build a comprehensive picture of AI tool engagement. Crucially, don’t view these numbers in isolation, they should be examined in context with your existing engineering KPIs. For example, if Cursor’s analytics show a high volume of accepted suggestions and an upward trend in active users, you might also look at your team’s cycle time or code review turnaround metrics for improvement. Ideally, increased AI assistant usage correlates with faster delivery or improved code quality (perhaps reflected in fewer review corrections needed). On the other hand, if Cursor usage is high but you don’t see improvements in output, it might prompt a deeper look: are developers over-relying on it for trivial code, or is it generating solutions that require rework?

**Tip for CTOs:**Track these metrics over time (month-to-month) rather than just snapshots. Trends can be more telling than absolute numbers. A rising trend in weekly active users and suggestion acceptance over a quarter, for instance, would suggest growing trust and integration of Cursor into the team’s processes – a sign that your investment in AI tooling is paying off.

Benefits of Using Cursor Analytics for Decision-Making

Collecting data is only half the battle; the real value comes from translating these insights into action. Here are several ways**Cursor Analytics can inform engineering leadership decisions and strategies**:

**Evaluate ROI of AI Tools:**By having concrete usage and acceptance data, you can determine if Cursor (and its associated costs) is delivering enough value. For example, if only a handful of developers use the tool regularly, you might reconsider the number of licenses or provide enablement to increase adoption. Conversely, strong usage stats combined with faster development times could justify further investment in AI tools or related training.
- **Identify Training and Enablement Needs:**Analytics might reveal uneven adoption – perhaps some teams or individuals hardly use Cursor while others use it extensively. If so, you can investigate why. It could be that certain projects aren’t suited for AI assistance, or it could be a lack of knowledge. You might organize workshops or pair programming sessions to share how top users integrate Cursor into their workflow. Additionally, metrics like low suggestion acceptance rates could indicate that developers need guidance on crafting better prompts or understanding Cursor’s capabilities.
- **Improve AI and Development Workflows:**The data may highlight bottlenecks or opportunities in your workflow. For instance, if the analytics show that many AI suggestions are rejected, engineering leaders might feedback this to the tool vendor or adjust how the team uses the AI (maybe the AI works better for certain languages or tasks). If certain features (like automated code review) are under utilized, you could dig into why – maybe developers find them less useful or there’s overlap with another tool. Armed with data, you can refine your internal best practices for AI usage (e.g., when to trust the AI vs. when to double-check manually).
- **Benchmark and Goal-Setting:**Over time, Cursor’s metrics can serve as a benchmark for your organization’s AI-assisted development. You could set goals such as “Increase the percentage of code contributed by AI from 15% to 30% next quarter” or “Have 100% of the team active on Cursor each month.” Of course, these goals should align with quality and productivity outcomes. The analytics will tell you if you’re trending toward those targets. If you also use industry benchmarks (for example, knowing that top-performing teams accept X lines of AI code per week on average), you can gauge where you stand and aim higher.

From a cultural perspective, sharing some of these insights with the engineering team can also be beneficial. Developers are often curious how much time the AI is actually saving or which teams leverage it most. By transparently discussing metrics (without making it a surveillance tool or pressuring individuals), you can foster a data-informed culture where the team collectively learns and improves how they work with AI.

What if I use a combination of AI coding tools?

**S**ome developers might use GitHub Copilot in their IDE, Devin for agentic AI and others rely on a code assistant like Sourcegraph for search and refactoring. Some may even use code review tools like Greptile. This mix of tools can create a fragmented analytics picture, with usage data siloed in different places (each platform might offer its own stats, or some have none at all). In such cases, using a centralized platform like**Weave**(www.workweave.dev) can help consolidate insights and provide unified visibility across all these tools. Weave is designed to aggregate data from multiple AI development tools, giving engineering leadership a single pane of glass to see how AI is influencing coding across the organization. This neutral, unified view ensures you’re not missing the forest for the trees, you can track total AI-driven code contributions, compare adoption rates between tools, and identify organization-wide trends and best practices. By complementing Cursor’s in-depth analytics with a broader cross-tool analytics platform, CTOs and VPs of Engineering can obtain a holistic understanding of their team’s AI usage, enabling smarter decisions and truly maximizing the productivity benefits of these emerging coding assistants.

Article written by

Brennan Lupyrypa

Make AI Engineering Simple

Effortless charts, clear scope, easy code review, and team analysis

Book a demo

Book a demo

Book a demo

Book a demo

Book a demo

Book a demo
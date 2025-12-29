# Why Lines of Code Are A Bad Measure of Developer Productivity - Remote

> Weave combines LLMs and domain-specific machine learning to understand engineering work. We understand how much work was done by AI vs. humans. How much AI is helping your team ship faster, if it's having an impact on code quality and code reviews.

- ## ## ## ## - ### - ### ### ## 1. ## $4.2M seed round led by Moonfire, Burst Capital & Y Combinator

$4.2M seed round led by Moonfire, Burst Capital & Y Combinator

Ever felt that nagging feeling that counting the lines of code you write is a bit like judging a chef by the number of pots they use? It seems logical on the surface: more code, more work done, right? But as any seasoned developer knows, this is a massive oversimplification.

For years, managers have tried to quantify developer productivity using metrics like Lines of Code (LOC). But this approach is outdated and, frankly, misleading. Software development is a creative, problem-solving discipline, not an assembly line.

Let's dig into why LOC is such a poor metric and explore what we should be focusing on instead.

What Are Lines of Code (LOC)?

Lines of Code (LOC) is a software metric used to measure the size of a program by counting the number of lines in its source code. It’s a straightforward way to put a number on a codebase, but the devil is in the details.

There are two main ways to count LOC:

**Physical LOC**: This is a literal count of every single line in a file. It includes executable code, comments, and even blank lines. It's simple to calculate but also simple-minded.
1. **Logical LOC (or SLOC - Source Lines of Code)**: This method tries to be a bit smarter by counting only the lines that contain actual programming statements or instructions. It typically excludes comments and blank lines, aiming to measure the functional size of the code[2].

While logical LOC is a slight improvement, both methods fail to capture the full picture of a developer's contribution.

The Problem with Counting Lines

At first glance, LOC seems like a tangible output. But relying on it to measure productivity is riddled with problems. A high LOC count doesn't mean more value, and in many cases, it can mean the opposite.

Here’s why it’s a flawed metric.

Language Differences are Huge

Different programming languages have different levels of verbosity. A task that requires 50 lines of C++ might be accomplished in just 10 lines of Python.

Consider these two simple examples that do the same thing: print "Hello, World!" ten times.

**Java (more verbose):**

publicclassHelloWorld{publicstaticvoidmain(String[]args){for(inti=0;i<10;i++){System.out.println("Hello, World!");}}}**Python (more concise):**

for_inrange(10):print("Hello, World!")Is the Java developer more "productive" because they wrote more lines? Of course not. They just used a different tool for the job. This variability makes LOC a useless metric for comparing work across different languages or even different programming paradigms[1].

Quality Over Quantity, Always

Great developers often write*less*code, not more. They find elegant, efficient solutions to complex problems. A shorter, well-crafted piece of code is easier to read, maintain, and debug than a long, convoluted one.

Think about it:

**Deleting code is work.**Refactoring often involves removing redundant lines, which improves the codebase but results in a*negative*LOC count. Should a developer be penalized for making the code better?
- **Solving a problem without code is ideal.**The best solution is sometimes a configuration change or realizing the feature isn't needed at all. That’s pure value with zero lines written.
- **Complex code is a liability.**More code means a larger surface area for bugs and higher maintenance costs. Measuring LOC incentivizes writing bloated, complex code, which is the exact opposite of what you want[5].

The Danger of Goodhart's Law

This brings us to a critical concept in metrics:**Goodhart's Law**. It states:**"When a measure becomes a target, it ceases to be a good measure."**[7]

If you tell developers that their productivity will be judged by the number of lines they write, they will write more lines. It’s human nature. This can lead to all sorts of bad behavior[4]:

Unnecessary comments and blank lines.
- Overly complicated solutions where simple ones would suffice.
- Copy-pasting code instead of creating reusable functions.
- Avoiding crucial refactoring work that would reduce the line count.

Focusing on LOC as a target actively encourages engineers to write worse code, leading to technical debt and long-term problems[6].

So, What's a Better Way to Measure Productivity?

If LOC is out, what should we focus on? Instead of measuring*inputs*, we should focus on*outputs*and enabling developers to do their best work.

Modern tools likeWeaveare combining LLMs, ML and RL to accurately measure engineering work by understanding the code and providing a relative unit of measure by answering the question "how long would this PR take an expert engineer to complete."

Stop Counting, Start Enabling

As we move past November 2025, it's clear that the industry needs to retire outdated metrics like lines of code. It's a low-signal metric that often correlates negatively with what we actually value: quality, maintainability, and real-world impact[3].

True productivity isn't about the volume of code written. It's about solving problems for users, building robust and scalable systems, and continuously improving the health of the codebase. By focusing on the developer experience and using intelligent tools to gain real insights, we can finally move beyond counting lines and start measuring what truly counts.

Ready to see what your work*really*looks like, beyond the line count?Get Started with WorkWeaveand get a holistic analysis of your engineering activity.

Meta Description

Learn why lines of code is a poor metric for developer productivity and discover better, outcome-focused ways to measure true engineering impact.

Citations

[1]https://gitclear.com/count_lines_of_code_at_your_own_peril
- [2]https://multitudes.com/blog/lines-of-code
- [3]https://linkedin.com/posts/rmurphey_are-we-measuring-ais-impact-in-software-activity-7322997648477544448-uzqZ
- [4]https://linkedin.com/pulse/goodharts-law-software-engineering-josh-gray-04ure
- [5]https://christianheilmann.com/2024/02/06/lines-of-code-how-to-not-measure-code-quality-and-developer-efficiency
- [6]https://agilecoffee.com/toolkit/goodharts-law

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
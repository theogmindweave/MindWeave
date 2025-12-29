# What to Put in My Teams Cursor Rules File - Remote

> Weave combines LLMs and domain-specific machine learning to understand engineering work. We understand how much work was done by AI vs. humans. How much AI is helping your team ship faster, if it's having an impact on code quality and code reviews.

- ## ## ### ### ## ### ### - ### - ### ## - ### ### 1. - **Dependencies and Versions:**Explicitly specify important libraries, frameworks, and SDK versions[2]. This prevents the AI from using outdated syntax or features from incorrect versions.

Example:`Use React 18.x syntax. Do not use class components. For state management, prefer Zustand over Redux.`
1. **Unique Requirements:**Detail any specific configurations, architectural decisions, or constraints unique to the project, such as custom build steps, internationalization (i18n) patterns, or accessibility (a11y) requirements[2].

Code Examples and Edge Cases

Concrete examples are often more effective than abstract descriptions[2].

Include examples for common patterns in your codebase—API calls, component structure, error handling, state management. Concrete examples work much better than abstract descriptions.

Things like:

// Example: Error Handling for API calls// Always use try-catch blocks for asynchronous operations that might fail.// Log errors using the 'logger.error()' utility.// For user-facing errors, provide a clear message and a reference ID.asyncfunctionfetchUserProfile(userId:string):Promise<UserProfile |null>{try{constresponse=awaitapiClient.get(`/users/${userId}`);returnresponse.data;}catch(error){logger.error(`Failed to fetch profile for user${userId}:`,error);// Display a user-friendly error message via notification serviceshowNotification('Error fetching profile. Please try again later.','error');returnnull;}}Rationale Behind Patterns

Briefly explain why certain patterns are preferred. This helps the AI make intelligent decisions when adapting examples to new contexts.

"Use our internal data-fetcher library for API calls because it automatically handles retries, caching, and authentication tokens"
- "Prefer Zustand over Redux because it requires less boilerplate and integrates better with our component structure"
- "Use Tailwind classes instead of CSS modules to maintain consistency with our design system"

Best Practices for Crafting Effective Rules

How you write and manage your rules file also impacts its effectiveness.

Keep it Concise and Focused

Create multiple small, specific files rather than one massive file. This prevents polluting the context window with irrelevant information and keeps rules targeted to specific languages or modules.

Cursor offers four modes for including rules:

**Auto-attached based on file type**(best choice)
- **Agent-requested when relevant**(second best)
- **Include on request**(worst—nobody remembers to request it)
- **Always include**(bad unless genuinely universal)

Keep things language or folder-specific. Your React rules shouldn't interfere when writing Python scripts.

Be Specific and Provide Concrete Examples

Vague instructions like "write clean code" are unhelpful. Instead, define what "clean code" means in your context with specific criteria and examples[1].
- The more concrete and illustrative your examples, the better the AI can understand and adhere to your desired patterns[1].

Update Rules Based on Feedback

**The most important habit:**Update your rules every time the AI does something wrong. The key indicator of ineffective rules is repetitive feedback—if you keep saying "nope, don't do it that way" or "you forgot about this," that's a symptom of inadequate rules.

Use Cursor's "generate cursor rules" feature whenever you give feedback during a chat. The generated rules aren't perfect—remove about 80% of the random stuff—but it's a solid first draft. If you don't want to say something again, turn it into a rule.

Centralize Your Guidelines

Make your Cursor rules the single source of truth that both humans and AI learn from. Don't maintain separate code quality documents—consolidate everything into these files so there's no confusion about standards.

Boosting Developer Productivity with Cursor Rules

The Impact of Well-Defined Rules

This isn't about marginal improvements—it's transformational. AI can be 5x better when you invest upfront in giving it the right guidance. This is a one-time cost that gets compounding returns.

With effective rules, you spend less time on repetitive corrections and can focus on actual task-specific work. You need less effort crafting perfect prompts because the AI already understands your codebase conventions.

Without good rules, you're re-onboarding the AI every single conversation. With them, you pay once and benefit continuously across your entire team.

Measuring and Optimizing Productivity

While Cursor Rules directly refine AI assistance, understanding their full impact on team efficiency and identifying areas for further improvement benefits from broader analytics. Developer productivity tools that offer insights into engineering work can help track team output, reveal hidden strengths and weaknesses, monitor time investments, and debug project delivery bottlenecks for engineering teams of all sizes. By integrating such analytics, teams can better quantify the productivity gains from well-configured AI assistants guided by robust rules files and pinpoint other opportunities to optimize their development processes and AI integration strategies.

Maximize Your AI Coding Assistant

Investing the effort to create and maintain a comprehensive rules file is a crucial step in leveraging AI coding assistants to their full potential. By providing clear, specific, and context-aware guidance, you empower the AI to be a more effective partner, generating code that is not only functional but also high-quality, consistent, and aligned with your project's unique needs. This ultimately translates to saved time, improved codebases, and a more productive development experience for the entire team.

Citations

[1]https://docs.cursor.com/context/rules
- [2]https://github.com/PatrickJS/awesome-cursorrules
- [3]https://www.lullabot.com/articles/supercharge-your-ai-coding-cursor-rules-and-memory-banks

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
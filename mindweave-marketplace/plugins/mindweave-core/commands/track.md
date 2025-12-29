---
description: "Track a significant AI-assisted accomplishment"
argument-hint: "[achievement description]"
---

# Track Achievement

Log a significant accomplishment from this Claude Code session to MindWeave.

## What to Track

Track items that demonstrate AI-assisted value:
- Features implemented
- Bugs fixed
- Refactoring completed
- Documentation created
- Tests written
- Performance improvements
- Security fixes

## Instructions

1. Parse the achievement description from $ARGUMENTS
2. Analyze the current session context for:
   - Files modified
   - Complexity of changes
   - Time investment (estimated)
   - Category of work

3. Format as a structured entry:
   ```yaml
   timestamp: [ISO timestamp]
   achievement: [description]
   category: [feature|bugfix|refactor|docs|tests|perf|security]
   files_touched: [count]
   estimated_value: [low|medium|high]
   ```

4. Append to `.mindweave/achievements.log` (create if needed)
5. Provide a summary confirmation

This data feeds into the APIR Productivity score.

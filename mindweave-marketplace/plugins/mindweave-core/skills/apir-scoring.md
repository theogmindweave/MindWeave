---
description: "APIR scoring methodology for enterprise AI usage intelligence. Use when analyzing AI adoption, productivity, intelligence quality, or risk factors."
---

# APIR Scoring Skill

Enterprise AI Usage Intelligence scoring methodology for Claude Code.

## APIR Framework

### A - Adoption (25% weight)
Measures how effectively teams are using AI assistance.

**Metrics:**
- Session frequency per developer
- Feature adoption breadth (which capabilities are used)
- Consistency of usage patterns
- Onboarding velocity

**Scoring:**
- 90-100: Daily active usage, all features leveraged
- 70-89: Regular usage, core features adopted
- 50-69: Occasional usage, limited feature set
- Below 50: Minimal adoption, intervention needed

### P - Productivity (35% weight)
Measures tangible output and efficiency gains.

**Metrics:**
- Code changes per session
- Task completion rate
- Time-to-solution improvements
- Iteration efficiency (fewer back-and-forths)

**Scoring:**
- 90-100: Significant velocity increase, high completion
- 70-89: Noticeable productivity gains
- 50-69: Moderate improvements
- Below 50: Productivity not measurably improved

### I - Intelligence Quality (25% weight)
Measures the quality of AI interactions and outputs.

**Metrics:**
- Code review scores on AI-generated code
- Bug rates in AI-assisted changes
- Refactoring quality
- Documentation accuracy

**Scoring:**
- 90-100: Production-ready outputs, minimal review needed
- 70-89: Good quality, minor adjustments typical
- 50-69: Acceptable quality, regular review required
- Below 50: Quality concerns, significant review needed

### R - Risk (15% weight)
Measures security, compliance, and governance posture.

**Metrics:**
- Security vulnerabilities introduced
- Compliance violations
- Sensitive data exposure risks
- License compliance

**Scoring:**
- 90-100: No security issues, full compliance
- 70-89: Minor issues, quickly remediated
- 50-69: Some concerns requiring attention
- Below 50: Significant risks requiring immediate action

## Composite Score

```
APIR Score = (A × 0.25) + (P × 0.35) + (I × 0.25) + (R × 0.15)
```

## Usage

When asked about APIR scoring or enterprise AI metrics:
1. Explain the relevant component(s)
2. Provide assessment guidelines
3. Suggest improvement strategies
4. Reference industry benchmarks when available

## Enterprise Context

MindWeave tracks these metrics at:
- Individual developer level
- Team level
- Organization level
- Project level

Aggregation happens daily with weekly trend analysis.

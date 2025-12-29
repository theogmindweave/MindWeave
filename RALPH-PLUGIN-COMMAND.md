# /ralph Plugin Command Specification

This file defines the `/ralph` command for running 2-iteration Ralph loops in Claude Code plugins.

---

## COMMAND: `/ralph`

### Purpose
Execute a rapid 2-iteration Ralph loop upgrade cycle for MindWeave strategic documentation (Research+Product, GTM+Engineering).

### Syntax
```bash
/ralph [iteration] [phase]
```

### Parameters

| Parameter | Type | Required | Options | Description |
|-----------|------|----------|---------|-------------|
| `iteration` | string | No | `1`, `2` | Run Iteration 1 (Phases 1-3) or Iteration 2 (Phases 4-6). Default: `1` |
| `phase` | number | No | `1-6` | Run specific phase. Default: next incomplete phase |

### Examples

```bash
# Start Iteration 1, Phase 1 (Research Synthesis)
/ralph 1 1

# Continue with Iteration 1, Phase 2 (Competitive Positioning)
/ralph 1 2

# Start Iteration 2, Phase 4 (Product Roadmap)
/ralph 2 4

# Auto-detect next incomplete phase
/ralph
```

---

## WHAT THE COMMAND DOES

### Execution Flow

```
/ralph → Load Context → Identify Phase → Execute Tasks → Generate Deliverables → Council Review → Git Commit → Complete
```

---

## 2-ITERATION STRUCTURE

### Iteration 1: Research → Product Prep (Phases 1-3)

```bash
/ralph 1          # Phase 1: Research Synthesis
/ralph 1 2        # Phase 2: Competitive Positioning
/ralph 1 3        # Phase 3: Customer Validation
```

### Iteration 2: GTM → Engineering (Phases 4-6)

```bash
/ralph 2          # Phase 4: Product Roadmap
/ralph 2 5        # Phase 5: GTM Strategy
/ralph 2 6        # Phase 6: Engineering Roadmap
```

---

## QUICK REFERENCE: PHASES 1-6

| Phase | Title | Days | Key Deliverables |
|-------|-------|------|------------------|
| 1 | Research Synthesis | 1-3 | SYNTHESIS.md, RESEARCH-GAPS.md |
| 2 | Competitive Positioning | 4-6 | COMPETITIVE-STRATEGY.md, MARKET-TIMING.md |
| 3 | Customer Validation | 7-10 | CUSTOMER-VALIDATION.md, SALES-SCENARIOS.md |
| 4 | Product Roadmap | 11-14 | PRD-MVP.md, PRODUCT-ROADMAP.md |
| 5 | GTM Strategy | 15-17 | GTM-STRATEGY.md, CONTENT-CALENDAR.md |
| 6 | Engineering Roadmap | 18-20 | ENGINEERING-ROADMAP.md, API-SPECS.md |

---

## PLUGIN MANIFEST ENTRY

```yaml
name: ralph
type: command
description: "Execute a Ralph loop iteration phase for MindWeave strategic upgrade"
category: "Strategic Planning"
version: "1.0"
iteration_count: 2
phases_per_iteration: 3
primary_file: "RALPH-LOOP-CONSOLIDATED.md"
config_files:
  - "@ralph-loop.local.md"
  - "RALPH-LOOP-MASTER-PROMPT.md"
  - "RALPH-LOOP-EXECUTION-CHECKLIST.md"
arguments:
  - name: iteration
    type: string
    description: "Iteration 1 or 2"
    default: "1"
    values: ["1", "2"]
  - name: phase
    type: number
    description: "Phase number (1-6 for 2-iteration mode)"
    default: "auto"
```

---

## WHAT YOU NEED TO GIVE IN PLUGIN

```
1. PRIMARY EXECUTION FILE: RALPH-LOOP-CONSOLIDATED.md
   └─ Contains all task definitions, deliverables, success criteria

2. REFERENCE FILES:
   ├─ @ralph-loop.local.md (Council framework)
   ├─ RALPH-LOOP-MASTER-PROMPT.md (Daily task details)
   └─ RALPH-LOOP-EXECUTION-CHECKLIST.md (Phase tracking)

3. COMMAND PARAMETERS:
   ├─ iteration: "1" or "2"
   └─ phase: auto-detect or manual selection (1-6)

4. EXECUTION MODE:
   └─ 2 Iterations × 3 Phases = 6 total phases
```

---

**Last Updated:** Dec 29, 2025
**Version:** 1.0
**Status:** Ready for Plugin Implementation

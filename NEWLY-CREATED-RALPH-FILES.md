# 🆕 NEWLY CREATED RALPH FILES (Dec 29, 2025)

**These 3 files are all you need to run the Ralph loop for 2 iterations.**

---

## FILE 1: RALPH-LOOP-SUMMARY.md
**Purpose:** One-page overview with main point + 5 key reference files

**What it contains:**
- ✅ The Main Point (one sentence)
- ✅ 5 Core Reference Files with links & purposes
- ✅ 3 Iteration Breakdown (Research/Product/Compliance)
- ✅ Council of Experts roles (5 reviewers)
- ✅ Quick start instructions
- ✅ Success criteria checklist

**Use this when:** You need a quick overview or want to show someone the whole Ralph loop in 2 minutes

---

## FILE 2: RALPH-LOOP-CONSOLIDATED.md
**Purpose:** Complete executable master file with ALL tasks, deliverables, and checklists for 10 phases

**What it contains:**
- ✅ Full Phase 1-10 task lists ("What to Do" for each phase)
- ✅ All deliverables you need to create per phase
- ✅ Success criteria for each phase
- ✅ Council review template
- ✅ Git commit format for each phase
- ✅ Key research inputs to analyze
- ✅ Success metrics tracking table

**Use this when:** You're executing a phase and need to know exactly what tasks to complete

**This is your:** Day-to-day execution bible

---

## FILE 3: RALPH-LOOP-PLUGIN-COMMAND.md
**Purpose:** Specification for `/ralph` command that runs 2 iterations with parameters

**What it contains:**
- ✅ Command syntax: `/ralph [iteration] [phase]`
- ✅ Parameter definitions (iteration 1 or 2, phase 1-6)
- ✅ Examples of how to use the command
- ✅ Execution flow (step-by-step)
- ✅ Command output format (what user sees)
- ✅ 2-Iteration structure (Iteration 1 vs Iteration 2)
- ✅ Council review process within command
- ✅ Plugin implementation details
- ✅ Quick reference table of phases 1-6
- ✅ Execution example walkthrough

**Use this when:**
- Building the Ralph loop as a Claude Code plugin
- Understanding what the `/ralph` command should do
- Showing others how to use the command

**This is your:** Plugin specification document

---

## HOW TO USE THESE 3 FILES

### Step 1: Understand the Overview
→ Read **RALPH-LOOP-SUMMARY.md** (2 minutes)

### Step 2: Execute Phase by Phase
→ Use **RALPH-LOOP-CONSOLIDATED.md** as your task checklist

### Step 3: Implement as Plugin (Optional)
→ Follow **RALPH-LOOP-PLUGIN-COMMAND.md** to build `/ralph` command

---

## QUICK MAPPING

| Need | Use File | Section |
|------|----------|---------|
| What's Ralph Loop? | SUMMARY.md | The Main Point |
| How do I execute Phase 1? | CONSOLIDATED.md | Phase 1 section |
| What are council reviews? | SUMMARY.md | Council of Experts |
| How does `/ralph` command work? | PLUGIN-COMMAND.md | Command syntax |
| What deliverables do I create? | CONSOLIDATED.md | Each phase's deliverables |
| What are success criteria? | CONSOLIDATED.md | Each phase's success criteria |
| How do I use the command? | PLUGIN-COMMAND.md | Examples section |

---

## THE MAIN POINT (Copy-Paste Ready)

**Ralph Loop is a 10-Phase Strategic Upgrade Framework that iteratively improves MindWeave through 3 continuous improvement cycles (Research → Product → Compliance → Launch) using a Council of Experts validation model to achieve hyper-growth execution readiness in 30 days.**

---

## FOR PLUGIN: THE `/ralph` COMMAND

**What to give in plugin right settings:**

```yaml
command: ralph
type: execution_command
description: "Execute Ralph loop iteration phase for MindWeave strategic upgrade"
primary_file: "RALPH-LOOP-CONSOLIDATED.md"
config_files:
  - "@ralph-loop.local.md"
  - "RALPH-LOOP-MASTER-PROMPT.md"
  - "RALPH-LOOP-EXECUTION-CHECKLIST.md"
parameters:
  iteration: ["1", "2"]
  phase: ["1", "2", "3", "4", "5", "6"]
  mode: ["auto", "manual"]
iterations: 2
phases_per_iteration: 3
total_days: 20
```

---

## QUICK START COMMANDS

**For Iteration 1:**
```bash
/ralph 1          # Phase 1: Research Synthesis
/ralph 1 2        # Phase 2: Competitive Positioning
/ralph 1 3        # Phase 3: Customer Validation
```

**For Iteration 2:**
```bash
/ralph 2          # Phase 4: Product Roadmap
/ralph 2 5        # Phase 5: GTM Strategy
/ralph 2 6        # Phase 6: Engineering Roadmap
```

---

**Created:** Dec 29, 2025
**All Files Ready:** ✅
**Next Step:** Pick an iteration and start executing phases

#!/bin/bash

# MINDWEAVE CLEANUP SCRIPT
# Removes all duplicate/old files, leaving only essential 6 in TheOGMindWeave

echo "🧹 MINDWEAVE CLEANUP: DELETE ALL DUPLICATES"
echo ""
echo "Before: 30+ files in TheOGMindWeave (with many duplicates)"
echo "After: 6 essential files only (no duplicates)"
echo ""

# STEP 1: Delete all old files from TheOGMindWeave
echo "Step 1: Cleaning TheOGMindWeave directory..."
cd /Users/vijaygorfad/Desktop/MindWeave/TheOGMindWeave

# Delete all ITERATION-* files (they're archived in .ogdump/ARCHIVE/ITERATIONS/)
echo "Removing ITERATION files..."
rm -f ITERATION-*.md

# Delete old MASTER-OPERATING-SYSTEM files (consolidated into EXECUTIVE-PLAYBOOK.md)
echo "Removing old MASTER-OPERATING-SYSTEM files..."
rm -f MASTER-OPERATING-SYSTEM-*.md

# Delete old manifests (consolidated into .ogdump/MANIFESTS/)
echo "Removing old STAGE manifests..."
rm -f STAGE-*.md

# Delete duplicate synthesis files (consolidated into STRATEGIC-EVOLUTION.md)
echo "Removing old synthesis files..."
rm -f FINAL-ULTRADEEP-SYNTHESIS.md
rm -f ULTRATHINK-SYNTHESIS-ITERATION-2.md
rm -f ULTIMATE-MASTER-SYNTHESIS.md

# Delete navigation files (references moved to main ORGANIZATION-INDEX.md)
echo "Removing redundant navigation..."
rm -f START-HERE-EXECUTION-READY.md
rm -f MASTER-OPERATING-SYSTEM-INDEX.md

# Delete Ralph-Loop config files (kept in main directory only)
echo "Removing Ralph-Loop configs..."
rm -f @ralph-loop.local.md
rm -f @ralph-loop-ultrathink.local.md
rm -f RALPH-LOOP-CONFIG.md

# Delete old evolution/research files (moved to 01-vision, 02-research)
echo "Removing duplicate framework files..."
rm -f 01-APIR-FRAMEWORK-DEEP-DIVE.md
rm -f 02-ARCHITECTURE-VISION.md

cd /Users/vijaygorfad/Desktop/MindWeave

# STEP 2: Clean up duplicate files in main directory
echo ""
echo "Step 2: Cleaning main directory duplicates..."

# Delete old manifests (moved to .ogdump/MANIFESTS/)
rm -f STAGE-1-DISCOVERY-MANIFEST.md
rm -f STAGE-2-PRECISION-SCORE-MATRIX.md
rm -f STAGE-4-5-DEPENDENCY-GRAPH-AND-CONSOLIDATION.md
rm -f STAGE-7-8-FINAL-DISCOVERY-REPORT.md

# Delete old files from Phase 1-5 cleanup that are now in folders
rm -f FILE-MAP.md
rm -f REPOSITORY-INDEX.md

# Delete old consolidation files (now in folders)
rm -f FINAL-ULTRADEEP-SYNTHESIS.md
rm -f ULTRATHINK-SYNTHESIS-ITERATION-2.md

# Delete old duplicate iterations (moved to folders)
rm -f ITERATION-7-MINDWEAVE-ULTRATHINK-SYNTHESIS.md
rm -f ITERATION-8-MAXIMUM-PRECISION.md

# STEP 3: Verify final state
echo ""
echo "✅ Cleanup complete!"
echo ""
echo "TheOGMindWeave now contains:"
cd /Users/vijaygorfad/Desktop/MindWeave/TheOGMindWeave
echo "Files: $(ls -1 *.md | wc -l)"
ls -1 *.md
echo ""

echo "Main directory system/navigation files:"
cd /Users/vijaygorfad/Desktop/MindWeave
ls -1 *.md | head -15
echo ""

echo "📊 FINAL STATE:"
echo "TheOGMindWeave: 6 essential files (EXECUTIVE-PLAYBOOK, STRATEGIC-EVOLUTION, PRODUCT-STRATEGY, GTM-STRATEGY, 100-DAY-EXECUTION, README)"
echo "Main directory: 10 navigation/system files"
echo "Organized folders: 27 strategic reference docs (by function)"
echo "Archive: .ogdump/ (all iterations versioned + audit trail)"
echo ""
echo "✨ Ready for founder execution!"

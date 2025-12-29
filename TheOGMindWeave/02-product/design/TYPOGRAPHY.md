# MindWeave Typography

## Document Information
| Field | Value |
|-------|-------|
| Document ID | DS-004 |
| Version | 1.0.0 |
| Last Updated | 2024-12-29 |
| Owner | Product Design |
| Status | Active |

## Overview

The MindWeave typography system establishes a clear visual hierarchy and ensures optimal readability across all platform interfaces. Built on the Inter font family for UI elements and JetBrains Mono for code, this system supports information-dense enterprise interfaces while maintaining accessibility standards.

---

## 1. Font Families

### 1.1 Primary Font: Inter

```
┌─────────────────────────────────────────────────────────────────────┐
│                       INTER FONT FAMILY                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Inter is a typeface carefully crafted for computer screens.       │
│   Features include:                                                 │
│   • Tall x-height for improved readability at small sizes           │
│   • Variable font support for smooth weight transitions             │
│   • OpenType features for tabular numbers and ligatures             │
│                                                                     │
│   Weights Used:                                                     │
│                                                                     │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │                                                               │ │
│   │   Regular (400)                                               │ │
│   │   The quick brown fox jumps over the lazy dog                 │ │
│   │   Use for: Body text, descriptions, labels                    │ │
│   │                                                               │ │
│   │   Medium (500)                                                │ │
│   │   The quick brown fox jumps over the lazy dog                 │ │
│   │   Use for: Emphasis, form labels, buttons                     │ │
│   │                                                               │ │
│   │   Semibold (600)                                              │ │
│   │   The quick brown fox jumps over the lazy dog                 │ │
│   │   Use for: Headings, table headers, important text            │ │
│   │                                                               │ │
│   │   Bold (700)                                                  │ │
│   │   The quick brown fox jumps over the lazy dog                 │ │
│   │   Use for: Page titles, primary headings only                 │ │
│   │                                                               │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   CSS Implementation:                                               │
│   font-family: 'Inter', -apple-system, BlinkMacSystemFont,          │
│                'Segoe UI', Roboto, sans-serif;                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Monospace Font: JetBrains Mono

```
┌─────────────────────────────────────────────────────────────────────┐
│                    JETBRAINS MONO FONT                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   JetBrains Mono is designed for developers with increased height   │
│   for improved readability of code.                                 │
│                                                                     │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │                                                               │ │
│   │   Regular (400)                                               │ │
│   │   const apiKey = "sk-123abc";                                 │ │
│   │   function processTokens() { ... }                            │ │
│   │                                                               │ │
│   │   Use for:                                                    │ │
│   │   • Code snippets and examples                                │ │
│   │   • API keys and identifiers                                  │ │
│   │   • JSON/config displays                                      │ │
│   │   • Error messages with technical details                     │ │
│   │   • Terminal output                                           │ │
│   │                                                               │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   CSS Implementation:                                               │
│   font-family: 'JetBrains Mono', 'Fira Code', 'Consolas',           │
│                'Monaco', monospace;                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Type Scale

### 2.1 Size Scale

```
┌─────────────────────────────────────────────────────────────────────┐
│                       TYPE SIZE SCALE                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Based on a 1.25 ratio (Major Third) scale                         │
│                                                                     │
│   Size Token   │ Pixels │ REM    │ Use Case                         │
│   ─────────────┼────────┼────────┼────────────────────────────────  │
│   text-xs      │ 11px   │ 0.6875 │ Fine print, timestamps            │
│   text-sm      │ 12px   │ 0.75   │ Captions, helper text             │
│   text-base    │ 14px   │ 0.875  │ Body text, most UI (DEFAULT)      │
│   text-lg      │ 16px   │ 1.0    │ Emphasized body, lead text        │
│   text-xl      │ 18px   │ 1.125  │ H4, card titles                   │
│   text-2xl     │ 20px   │ 1.25   │ H3, section headers               │
│   text-3xl     │ 24px   │ 1.5    │ H2, major sections                │
│   text-4xl     │ 30px   │ 1.875  │ H1, page titles                   │
│   text-5xl     │ 36px   │ 2.25   │ Display, hero text                │
│   text-6xl     │ 48px   │ 3.0    │ Marketing, landing pages          │
│                                                                     │
│   Visual Scale:                                                     │
│                                                                     │
│   xs (11px)   Fine print text                                       │
│   sm (12px)   Caption text example                                  │
│   base (14px) Standard body text for the application                │
│   lg (16px)   Slightly larger emphasized text                       │
│   xl (18px)   Card Title Example                                    │
│   2xl (20px)  Section Header                                        │
│   3xl (24px)  Major Section                                         │
│   4xl (30px)  Page Title                                            │
│   5xl (36px)  Display Heading                                       │
│   6xl (48px)  Hero Text                                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Line Height

```
┌─────────────────────────────────────────────────────────────────────┐
│                       LINE HEIGHT SCALE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Token        │ Value  │ Use Case                                  │
│   ─────────────┼────────┼───────────────────────────────────────── │
│   leading-none │ 1.0    │ Single-line text, buttons                 │
│   leading-tight│ 1.25   │ Headings, short labels                    │
│   leading-snug │ 1.375  │ Subheadings, card titles                  │
│   leading-base │ 1.5    │ Body text (DEFAULT)                       │
│   leading-relaxed │ 1.625 │ Long-form content                       │
│   leading-loose│ 2.0    │ Very spaced text (rare)                   │
│                                                                     │
│   Default Pairings:                                                 │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │ Font Size  │ Line Height │ Computed │ Example                 │ │
│   ├──────────────────────────────────────────────────────────────┤ │
│   │ 14px       │ 1.5         │ 21px     │ Body text               │ │
│   │ 12px       │ 1.5         │ 18px     │ Captions                │ │
│   │ 16px       │ 1.5         │ 24px     │ Lead text               │ │
│   │ 20px       │ 1.375       │ 27.5px   │ H3 headings             │ │
│   │ 24px       │ 1.25        │ 30px     │ H2 headings             │ │
│   │ 30px       │ 1.25        │ 37.5px   │ H1 headings             │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Heading Styles

### 3.1 Heading Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│                       HEADING HIERARCHY                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   H1 - Page Title                                                   │
│   ═══════════════                                                   │
│   Size: 30px | Weight: Semibold (600) | Line Height: 1.25           │
│   Color: Slate 900 | Letter Spacing: -0.025em                       │
│   Use: Primary page title, one per page                             │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ Token Usage Dashboard                                        │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   H2 - Section Header                                               │
│   ═══════════════════                                               │
│   Size: 24px | Weight: Semibold (600) | Line Height: 1.25           │
│   Color: Slate 900 | Letter Spacing: -0.02em                        │
│   Use: Major content sections                                       │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ Usage by Team                                                │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   H3 - Subsection Header                                            │
│   ══════════════════════                                            │
│   Size: 20px | Weight: Semibold (600) | Line Height: 1.375          │
│   Color: Slate 800 | Letter Spacing: -0.01em                        │
│   Use: Subsections within major sections                            │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ Backend Team                                                 │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   H4 - Card/Component Title                                         │
│   ═════════════════════════                                         │
│   Size: 16px | Weight: Semibold (600) | Line Height: 1.5            │
│   Color: Slate 900 | Letter Spacing: 0                              │
│   Use: Card headers, modal titles, small sections                   │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ Monthly Summary                                              │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   H5 - Label/Caption Header                                         │
│   ═════════════════════════                                         │
│   Size: 14px | Weight: Medium (500) | Line Height: 1.5              │
│   Color: Slate 700 | Letter Spacing: 0                              │
│   Use: Form section labels, small headers                           │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   H6 - Overline                                                     │
│   ═════════════                                                     │
│   Size: 12px | Weight: Medium (500) | Line Height: 1.5              │
│   Color: Slate 500 | Letter Spacing: 0.05em | Transform: Uppercase  │
│   Use: Category labels, meta information                            │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ ANALYTICS                                                    │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Heading CSS

```css
/* Heading Styles */
.h1, h1 {
  font-size: 1.875rem;    /* 30px */
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -0.025em;
  color: var(--color-text-primary);
}

.h2, h2 {
  font-size: 1.5rem;      /* 24px */
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -0.02em;
  color: var(--color-text-primary);
}

.h3, h3 {
  font-size: 1.25rem;     /* 20px */
  font-weight: 600;
  line-height: 1.375;
  letter-spacing: -0.01em;
  color: var(--color-text-secondary);
}

.h4, h4 {
  font-size: 1rem;        /* 16px */
  font-weight: 600;
  line-height: 1.5;
  color: var(--color-text-primary);
}

.h5, h5 {
  font-size: 0.875rem;    /* 14px */
  font-weight: 500;
  line-height: 1.5;
  color: var(--color-text-secondary);
}

.h6, h6 {
  font-size: 0.75rem;     /* 12px */
  font-weight: 500;
  line-height: 1.5;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--color-text-tertiary);
}
```

---

## 4. Body Text Styles

### 4.1 Body Text Variants

```
┌─────────────────────────────────────────────────────────────────────┐
│                       BODY TEXT VARIANTS                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Body Default                                                      │
│   ────────────                                                      │
│   Size: 14px | Weight: Regular (400) | Line Height: 1.5             │
│   Color: Slate 700                                                  │
│                                                                     │
│   Use: Standard paragraph text throughout the application           │
│                                                                     │
│   Example:                                                          │
│   This is the primary body text style used for most content         │
│   throughout the application. It provides optimal readability       │
│   for information-dense interfaces.                                 │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Body Large                                                        │
│   ──────────                                                        │
│   Size: 16px | Weight: Regular (400) | Line Height: 1.5             │
│   Color: Slate 700                                                  │
│                                                                     │
│   Use: Lead paragraphs, important descriptions, empty states        │
│                                                                     │
│   Example:                                                          │
│   Monitor and analyze your organization's Claude API usage          │
│   with real-time insights and cost tracking.                        │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Body Small                                                        │
│   ──────────                                                        │
│   Size: 12px | Weight: Regular (400) | Line Height: 1.5             │
│   Color: Slate 500                                                  │
│                                                                     │
│   Use: Captions, helper text, timestamps, secondary info            │
│                                                                     │
│   Example:                                                          │
│   Last updated 5 minutes ago                                        │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Body XS                                                           │
│   ───────                                                           │
│   Size: 11px | Weight: Regular (400) | Line Height: 1.5             │
│   Color: Slate 400                                                  │
│                                                                     │
│   Use: Fine print, legal text, dense data tables                    │
│                                                                     │
│   Example:                                                          │
│   All times shown in UTC                                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Text Emphasis Styles

```
┌─────────────────────────────────────────────────────────────────────┐
│                       TEXT EMPHASIS                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Strong / Bold                                                     │
│   ─────────────                                                     │
│   Weight: Semibold (600)                                            │
│   Use sparingly to emphasize key terms                              │
│                                                                     │
│   Example: The API key will expire in **7 days**.                   │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Italic / Emphasis                                                 │
│   ─────────────────                                                 │
│   Style: Italic                                                     │
│   Use for titles, terms, or subtle emphasis                         │
│                                                                     │
│   Example: See the *Getting Started* guide for details.             │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Link                                                              │
│   ────                                                              │
│   Color: Indigo 600 | Decoration: None (hover: underline)           │
│   Cursor: pointer                                                   │
│                                                                     │
│   Example: View documentation →                                     │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Muted                                                             │
│   ─────                                                             │
│   Color: Slate 500                                                  │
│   Use for secondary or less important text                          │
│                                                                     │
│   Example: Optional field                                           │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Code Inline                                                       │
│   ───────────                                                       │
│   Font: JetBrains Mono | Size: 0.875em | Background: Slate 100      │
│   Padding: 2px 6px | Border Radius: 4px                             │
│                                                                     │
│   Example: Use the `processTokens()` function.                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. UI Text Styles

### 5.1 Labels & Form Text

```
┌─────────────────────────────────────────────────────────────────────┐
│                       UI TEXT STYLES                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Form Label                                                        │
│   ──────────                                                        │
│   Size: 14px | Weight: Medium (500) | Line Height: 1.5              │
│   Color: Slate 700                                                  │
│   Margin Bottom: 6px                                                │
│                                                                     │
│   Example:                                                          │
│   Email Address *                                                   │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ user@example.com                                             │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Helper Text                                                       │
│   ───────────                                                       │
│   Size: 12px | Weight: Regular (400) | Line Height: 1.5             │
│   Color: Slate 500                                                  │
│   Margin Top: 4px                                                   │
│                                                                     │
│   Example:                                                          │
│   Enter your work email address                                     │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Error Text                                                        │
│   ──────────                                                        │
│   Size: 12px | Weight: Regular (400) | Line Height: 1.5             │
│   Color: Red 600 (#DC2626)                                          │
│   Margin Top: 4px                                                   │
│                                                                     │
│   Example:                                                          │
│   ⚠ This field is required                                          │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Placeholder Text                                                  │
│   ────────────────                                                  │
│   Size: 14px | Weight: Regular (400)                                │
│   Color: Slate 400                                                  │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ Enter your email...                                          │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Button Text

```
┌─────────────────────────────────────────────────────────────────────┐
│                       BUTTON TEXT STYLES                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Size    │ Font Size │ Weight │ Letter Spacing │ Transform         │
│   ────────┼───────────┼────────┼────────────────┼──────────────────│
│   xs      │ 12px      │ 500    │ 0              │ none              │
│   sm      │ 13px      │ 500    │ 0              │ none              │
│   md      │ 14px      │ 500    │ 0              │ none              │
│   lg      │ 15px      │ 500    │ 0              │ none              │
│   xl      │ 16px      │ 500    │ 0              │ none              │
│                                                                     │
│   Visual Examples:                                                  │
│                                                                     │
│   ┌──────────┐  ┌─────────────┐  ┌────────────────┐                │
│   │  Save    │  │    Save     │  │     Save       │                │
│   └──────────┘  └─────────────┘  └────────────────┘                │
│      sm             md                  lg                          │
│                                                                     │
│   Button Label Guidelines:                                          │
│   • Use action verbs: "Save", "Create", "Delete"                    │
│   • Keep labels concise: 1-3 words maximum                          │
│   • Be specific: "Save Changes" > "Save"                            │
│   • Use sentence case: "Create team" not "Create Team"              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.3 Navigation Text

```
┌─────────────────────────────────────────────────────────────────────┐
│                       NAVIGATION TEXT                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Sidebar Navigation Item                                           │
│   ───────────────────────                                           │
│   Size: 14px | Weight: Medium (500) | Line Height: 1.5              │
│   Default Color: Slate 600                                          │
│   Hover Color: Slate 900                                            │
│   Active Color: Indigo 600                                          │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────┐                                          │
│   │  □ Dashboard        │  ◄── Default                              │
│   │  ■ Analytics        │  ◄── Active                               │
│   │  □ MCP Registry     │                                          │
│   └─────────────────────┘                                          │
│                                                                     │
│   Tab Navigation                                                    │
│   ──────────────                                                    │
│   Size: 14px | Weight: Medium (500) | Line Height: 1.5              │
│   Default Color: Slate 500                                          │
│   Active Color: Slate 900                                           │
│   Active Indicator: Indigo 600 (2px underline)                      │
│                                                                     │
│   Example:                                                          │
│   ┌───────────────────────────────────────────────────┐            │
│   │   Overview      Usage      Access      Settings   │            │
│   │   ─────────                                       │            │
│   └───────────────────────────────────────────────────┘            │
│                                                                     │
│   Breadcrumb                                                        │
│   ──────────                                                        │
│   Size: 14px | Weight: Regular (400)                                │
│   Link Color: Slate 500 | Hover: Indigo 600                         │
│   Current Color: Slate 900 | Separator: Slate 400                   │
│                                                                     │
│   Example:                                                          │
│   Home / Teams / Backend / Members                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6. Data Display Typography

### 6.1 Table Typography

```
┌─────────────────────────────────────────────────────────────────────┐
│                       TABLE TYPOGRAPHY                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Table Header                                                      │
│   ────────────                                                      │
│   Size: 12px | Weight: Semibold (600) | Line Height: 1.5            │
│   Color: Slate 600 | Letter Spacing: 0.02em                         │
│   Text Transform: Uppercase                                         │
│                                                                     │
│   Table Cell - Default                                              │
│   ────────────────────                                              │
│   Size: 14px | Weight: Regular (400) | Line Height: 1.5             │
│   Color: Slate 700                                                  │
│                                                                     │
│   Table Cell - Numeric                                              │
│   ────────────────────                                              │
│   Font Feature: Tabular Numbers (tnum)                              │
│   Align: Right                                                      │
│                                                                     │
│   Example:                                                          │
│   ┌────────────┬──────────────┬───────────┬───────────┐            │
│   │ NAME       │ TEAM         │ TOKENS    │ COST      │            │
│   ├────────────┼──────────────┼───────────┼───────────┤            │
│   │ John Smith │ Backend      │  124,567  │   $12.45  │            │
│   │ Jane Doe   │ Frontend     │   89,234  │    $8.92  │            │
│   │ Bob Wilson │ ML           │  456,789  │   $45.67  │            │
│   └────────────┴──────────────┴───────────┴───────────┘            │
│                                                                     │
│   Note: Numbers use tabular figures for alignment                   │
│   font-variant-numeric: tabular-nums;                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 Metric Display Typography

```
┌─────────────────────────────────────────────────────────────────────┐
│                       METRIC TYPOGRAPHY                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Large Metric Value                                                │
│   ──────────────────                                                │
│   Size: 36px | Weight: Semibold (600) | Line Height: 1.2            │
│   Color: Slate 900 | Font Feature: Tabular Numbers                  │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────┐                                      │
│   │  2.4M                   │                                      │
│   │  Total Tokens           │                                      │
│   └─────────────────────────┘                                      │
│                                                                     │
│   Medium Metric Value                                               │
│   ───────────────────                                               │
│   Size: 24px | Weight: Semibold (600) | Line Height: 1.2            │
│   Color: Slate 900                                                  │
│                                                                     │
│   Small Metric Value                                                │
│   ──────────────────                                                │
│   Size: 18px | Weight: Semibold (600) | Line Height: 1.2            │
│   Color: Slate 900                                                  │
│                                                                     │
│   Metric Label                                                      │
│   ────────────                                                      │
│   Size: 12px | Weight: Medium (500) | Line Height: 1.5              │
│   Color: Slate 500                                                  │
│                                                                     │
│   Trend Indicator                                                   │
│   ───────────────                                                   │
│   Size: 12px | Weight: Medium (500)                                 │
│   Positive: Green 600 (#16A34A) with ↑                              │
│   Negative: Red 600 (#DC2626) with ↓                                │
│   Neutral: Slate 500 with →                                         │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────┐                                      │
│   │  $12,450        ↑ 12%   │                                      │
│   │  Monthly Cost   vs Nov  │                                      │
│   └─────────────────────────┘                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. Code & Technical Typography

### 7.1 Code Blocks

```
┌─────────────────────────────────────────────────────────────────────┐
│                       CODE TYPOGRAPHY                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Inline Code                                                       │
│   ───────────                                                       │
│   Font: JetBrains Mono | Size: 0.875em (relative)                   │
│   Background: Slate 100 | Padding: 2px 6px                          │
│   Border Radius: 4px | Color: Slate 800                             │
│                                                                     │
│   Example: Use the `getTeamMembers()` function.                     │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Code Block                                                        │
│   ──────────                                                        │
│   Font: JetBrains Mono | Size: 13px | Line Height: 1.6              │
│   Background: Slate 900 (dark) | Padding: 16px                      │
│   Border Radius: 8px | Color: Slate 100                             │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ const response = await claude.messages.create({              │   │
│   │   model: "claude-3-opus-20240229",                           │   │
│   │   max_tokens: 1024,                                          │   │
│   │   messages: [{ role: "user", content: "Hello" }]             │   │
│   │ });                                                          │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   Syntax Highlighting Colors (Dark Theme):                          │
│   • Keywords: #FF79C6 (Pink)                                        │
│   • Strings: #F1FA8C (Yellow)                                       │
│   • Numbers: #BD93F9 (Purple)                                       │
│   • Comments: #6272A4 (Muted Blue)                                  │
│   • Functions: #50FA7B (Green)                                      │
│   • Variables: #F8F8F2 (White)                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 API & Technical Text

```
┌─────────────────────────────────────────────────────────────────────┐
│                       TECHNICAL TEXT                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   API Key Display                                                   │
│   ───────────────                                                   │
│   Font: JetBrains Mono | Size: 14px                                 │
│   Background: Slate 100 | Padding: 8px 12px                         │
│   Border: 1px solid Slate 200 | Border Radius: 6px                  │
│   Character Spacing: 0.05em (for readability)                       │
│                                                                     │
│   Example:                                                          │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ sk-ant-api03-1234567890abcdef...                     [Copy] │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   Error Code Display                                                │
│   ──────────────────                                                │
│   Font: JetBrains Mono | Size: 12px                                 │
│   Color: Red 700 | Background: Red 50                               │
│                                                                     │
│   Example:                                                          │
│   Error: ERR_RATE_LIMIT_EXCEEDED                                    │
│                                                                     │
│   JSON Display                                                      │
│   ────────────                                                      │
│   Font: JetBrains Mono | Size: 13px | Line Height: 1.5              │
│   Indentation: 2 spaces                                             │
│                                                                     │
│   Example:                                                          │
│   {                                                                 │
│     "id": "msg_01XFDUDYJgAACzvnptvVoYEL",                          │
│     "type": "message",                                              │
│     "role": "assistant",                                            │
│     "content": [...]                                                │
│   }                                                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8. Responsive Typography

### 8.1 Responsive Scale

```
┌─────────────────────────────────────────────────────────────────────┐
│                    RESPONSIVE TYPOGRAPHY                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Breakpoint Adjustments:                                           │
│                                                                     │
│   Element    │ Mobile (<640) │ Tablet (640-1024) │ Desktop (>1024) │
│   ───────────┼───────────────┼───────────────────┼────────────────  │
│   H1         │ 24px          │ 28px              │ 30px             │
│   H2         │ 20px          │ 22px              │ 24px             │
│   H3         │ 18px          │ 19px              │ 20px             │
│   H4         │ 16px          │ 16px              │ 16px             │
│   Body       │ 14px          │ 14px              │ 14px             │
│   Caption    │ 12px          │ 12px              │ 12px             │
│   Metric (L) │ 28px          │ 32px              │ 36px             │
│                                                                     │
│   Implementation:                                                   │
│   Use CSS clamp() for fluid typography                              │
│                                                                     │
│   h1 {                                                              │
│     font-size: clamp(1.5rem, 1.25rem + 1vw, 1.875rem);             │
│   }                                                                 │
│                                                                     │
│   h2 {                                                              │
│     font-size: clamp(1.25rem, 1.1rem + 0.75vw, 1.5rem);            │
│   }                                                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 9. Accessibility

### 9.1 Text Accessibility Guidelines

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TEXT ACCESSIBILITY                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Minimum Sizes:                                                    │
│   • Body text: 14px minimum (16px preferred)                        │
│   • Interactive elements: 14px minimum                              │
│   • Small text: 12px (use sparingly, non-essential only)            │
│   • Never use text smaller than 11px                                │
│                                                                     │
│   Line Length:                                                      │
│   • Optimal: 50-75 characters per line                              │
│   • Maximum: 80 characters per line                                 │
│   • Use max-width on text containers                                │
│                                                                     │
│   Spacing:                                                          │
│   • Paragraph spacing: 1em (equal to font size)                     │
│   • Section spacing: 1.5-2em                                        │
│                                                                     │
│   Do NOT:                                                           │
│   ✗ Use justified text alignment                                    │
│   ✗ Use all caps for more than a few words                          │
│   ✗ Use italic for long passages                                    │
│   ✗ Rely on color alone to convey meaning                           │
│                                                                     │
│   Text Resizing:                                                    │
│   • Support 200% text zoom without horizontal scroll                │
│   • Use relative units (rem, em) not pixels                         │
│   • Test with browser zoom at 200%                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 10. CSS Variables

```css
:root {
  /* Font Families */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;

  /* Font Sizes */
  --text-xs: 0.6875rem;    /* 11px */
  --text-sm: 0.75rem;      /* 12px */
  --text-base: 0.875rem;   /* 14px */
  --text-lg: 1rem;         /* 16px */
  --text-xl: 1.125rem;     /* 18px */
  --text-2xl: 1.25rem;     /* 20px */
  --text-3xl: 1.5rem;      /* 24px */
  --text-4xl: 1.875rem;    /* 30px */
  --text-5xl: 2.25rem;     /* 36px */
  --text-6xl: 3rem;        /* 48px */

  /* Font Weights */
  --font-regular: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;

  /* Letter Spacing */
  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
}
```

---

## Related Documents

- [DESIGN-SYSTEM.md](./DESIGN-SYSTEM.md) - Design system overview
- [COLOR-PALETTE.md](./COLOR-PALETTE.md) - Color specifications
- [ACCESSIBILITY.md](./ACCESSIBILITY.md) - Accessibility guidelines
- [RESPONSIVE-DESIGN.md](./RESPONSIVE-DESIGN.md) - Responsive guidelines

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-12-29 | Product Design | Initial typography system |

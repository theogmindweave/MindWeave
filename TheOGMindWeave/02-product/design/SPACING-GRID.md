# MindWeave Spacing & Grid System

## Document Information
| Field | Value |
|-------|-------|
| Document ID | DS-006 |
| Version | 1.0.0 |
| Last Updated | 2024-12-29 |
| Owner | Product Design |
| Status | Active |

## Overview

The MindWeave spacing and grid system establishes consistent visual rhythm across all interfaces. Built on a base unit of 4px, this system ensures components align precisely, creating a professional and organized appearance that enterprise customers expect.

---

## 1. Spacing Scale

### 1.1 Base Unit

```
┌─────────────────────────────────────────────────────────────────────┐
│                       BASE UNIT: 4px                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   All spacing values are multiples of 4px                           │
│                                                                     │
│   Why 4px?                                                          │
│   • Divides evenly into common screen densities                     │
│   • Creates consistent visual rhythm                                │
│   • Allows for precise alignment                                    │
│   • Compatible with 8px grid systems (2× base)                      │
│                                                                     │
│   Visual Reference:                                                 │
│   ┌─┐                                                              │
│   │ │  4px = 1 base unit                                           │
│   └─┘                                                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Spacing Scale

```
┌─────────────────────────────────────────────────────────────────────┐
│                       SPACING SCALE                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Token      │ Value  │ Use Case                                    │
│   ───────────┼────────┼──────────────────────────────────────────  │
│   space-0    │ 0px    │ No spacing                                  │
│   space-0.5  │ 2px    │ Hairline gaps                               │
│   space-1    │ 4px    │ Tight spacing, icon gaps                    │
│   space-2    │ 8px    │ Related elements, button padding            │
│   space-3    │ 12px   │ Form field spacing                          │
│   space-4    │ 16px   │ Standard component padding                  │
│   space-5    │ 20px   │ Comfortable spacing                         │
│   space-6    │ 24px   │ Section padding                             │
│   space-8    │ 32px   │ Large gaps, card padding                    │
│   space-10   │ 40px   │ Section gaps                                │
│   space-12   │ 48px   │ Large section gaps                          │
│   space-16   │ 64px   │ Page section separation                     │
│   space-20   │ 80px   │ Major section breaks                        │
│   space-24   │ 96px   │ Hero spacing                                │
│                                                                     │
│   Visual Scale:                                                     │
│                                                                     │
│   0.5 ├┤     2px                                                   │
│   1   ├──┤    4px                                                  │
│   2   ├────┤   8px                                                 │
│   3   ├──────┤  12px                                               │
│   4   ├────────┤  16px                                             │
│   6   ├────────────┤  24px                                         │
│   8   ├────────────────┤  32px                                     │
│   12  ├────────────────────────┤  48px                             │
│   16  ├────────────────────────────────┤  64px                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.3 Common Spacing Applications

| Context | Spacing Token | Value | Example |
|---------|---------------|-------|---------|
| Icon gap | space-1 | 4px | Icon to label |
| Button padding X | space-4 | 16px | Button horizontal |
| Button padding Y | space-2 | 8px | Button vertical |
| Form field gap | space-3 | 12px | Between label and input |
| Form group gap | space-6 | 24px | Between form groups |
| Card padding | space-6 | 24px | Card inner padding |
| Card gap | space-4 | 16px | Between cards |
| Section gap | space-12 | 48px | Between sections |
| Page padding | space-8 | 32px | Page margins |
| Table cell padding | space-3 | 12px | Cell inner padding |
| Modal padding | space-6 | 24px | Modal content padding |
| List item gap | space-2 | 8px | Between list items |

---

## 2. Grid System

### 2.1 Page Grid

```
┌─────────────────────────────────────────────────────────────────────┐
│                       12-COLUMN GRID                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Desktop Layout (> 1024px):                                        │
│                                                                     │
│   │◄────────────────────── 1440px max ──────────────────────►│     │
│   │◄─48px─►│◄─────────── content area ──────────►│◄─48px─►│        │
│             │                                     │                 │
│   ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐                           │
│   │1 │2 │3 │4 │5 │6 │7 │8 │9 │10│11│12│  12 columns                │
│   └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘                           │
│     │◄──24px gutter──►│                                            │
│                                                                     │
│   Column Width: (container - (gutters × 11)) / 12                   │
│   Example at 1344px content: (1344 - 264) / 12 = 90px               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Breakpoints

```
┌─────────────────────────────────────────────────────────────────────┐
│                       BREAKPOINTS                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Name     │ Min Width │ Columns │ Gutter │ Margin │ Max Width     │
│   ─────────┼───────────┼─────────┼────────┼────────┼──────────────│
│   xs       │ 0px       │ 4       │ 16px   │ 16px   │ 100%          │
│   sm       │ 640px     │ 8       │ 20px   │ 24px   │ 100%          │
│   md       │ 768px     │ 12      │ 24px   │ 32px   │ 100%          │
│   lg       │ 1024px    │ 12      │ 24px   │ 32px   │ 100%          │
│   xl       │ 1280px    │ 12      │ 32px   │ 48px   │ 1200px        │
│   2xl      │ 1536px    │ 12      │ 32px   │ 64px   │ 1440px        │
│                                                                     │
│   Visual Representation:                                            │
│                                                                     │
│   xs (Mobile):        sm (Tablet):         lg (Desktop):            │
│   ┌────────┐         ┌──────────────┐     ┌──────────────────────┐ │
│   │████████│         │██████████████│     │██████████████████████│ │
│   │4 cols  │         │8 cols        │     │12 cols               │ │
│   │16px gut│         │20px gutter   │     │24px gutter           │ │
│   └────────┘         └──────────────┘     └──────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.3 Column Spanning

```
┌─────────────────────────────────────────────────────────────────────┐
│                       COLUMN SPANS                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Full Width (12 columns):                                          │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │                          100%                                 │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   Two Thirds + One Third (8 + 4):                                   │
│   ┌──────────────────────────────────────────┐┌──────────────────┐ │
│   │                 66.67%                    ││     33.33%       │ │
│   └──────────────────────────────────────────┘└──────────────────┘ │
│                                                                     │
│   Half + Half (6 + 6):                                              │
│   ┌──────────────────────────────┐┌──────────────────────────────┐ │
│   │            50%               ││            50%               │ │
│   └──────────────────────────────┘└──────────────────────────────┘ │
│                                                                     │
│   Thirds (4 + 4 + 4):                                               │
│   ┌──────────────────┐┌──────────────────┐┌──────────────────┐     │
│   │      33.33%      ││      33.33%      ││      33.33%      │     │
│   └──────────────────┘└──────────────────┘└──────────────────┘     │
│                                                                     │
│   Quarters (3 + 3 + 3 + 3):                                         │
│   ┌────────────┐┌────────────┐┌────────────┐┌────────────┐         │
│   │    25%     ││    25%     ││    25%     ││    25%     │         │
│   └────────────┘└────────────┘└────────────┘└────────────┘         │
│                                                                     │
│   Sixths (2 + 2 + 2 + 2 + 2 + 2):                                   │
│   ┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐                 │
│   │16.67%││16.67%││16.67%││16.67%││16.67%││16.67%│                 │
│   └──────┘└──────┘└──────┘└──────┘└──────┘└──────┘                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Layout Patterns

### 3.1 App Shell Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                       APP SHELL LAYOUT                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │ Header                                            64px      │   │
│   ├──────────┬──────────────────────────────────────────────────┤   │
│   │          │                                                  │   │
│   │          │  Page Header Area                                │   │
│   │          │  ┌────────────────────────────────────────────┐  │   │
│   │          │  │ Title + Breadcrumb                 Actions │  │   │
│   │ Sidebar  │  └────────────────────────────────────────────┘  │   │
│   │          │                                                  │   │
│   │ 240px    │  Content Area (scrollable)                       │   │
│   │          │  ┌────────────────────────────────────────────┐  │   │
│   │          │  │                                            │  │   │
│   │          │  │                                            │  │   │
│   │          │  │           Main Content                     │  │   │
│   │          │  │                                            │  │   │
│   │          │  │                                            │  │   │
│   │          │  └────────────────────────────────────────────┘  │   │
│   │          │                                                  │   │
│   └──────────┴──────────────────────────────────────────────────┘   │
│                                                                     │
│   Measurements:                                                     │
│   • Header height: 64px                                             │
│   • Sidebar width: 240px (expanded), 64px (collapsed)               │
│   • Content padding: 32px                                           │
│   • Page header padding: 24px 32px                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Dashboard Grid

```
┌─────────────────────────────────────────────────────────────────────┐
│                       DASHBOARD LAYOUT                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Metric Cards (4-column grid):                                     │
│   gap: 16px (space-4)                                               │
│                                                                     │
│   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐  │
│   │  Metric 1   │ │  Metric 2   │ │  Metric 3   │ │  Metric 4   │  │
│   │  2.4M       │ │  $12,450    │ │  47 MCPs    │ │  245ms      │  │
│   └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘  │
│   │◄─────────────────── 24px gap ──────────────────►│              │
│                                                                     │
│   ─────────────────────────────────────────────────────── 48px ─   │
│                                                                     │
│   Charts (2-column grid):                                           │
│   gap: 24px (space-6)                                               │
│                                                                     │
│   ┌──────────────────────────┐ ┌──────────────────────────┐        │
│   │                          │ │                          │        │
│   │     Usage Over Time      │ │     Usage by Team        │        │
│   │     (Line Chart)         │ │     (Bar Chart)          │        │
│   │                          │ │                          │        │
│   └──────────────────────────┘ └──────────────────────────┘        │
│                                                                     │
│   Full Width Table:                                                 │
│   margin-top: 48px (space-12)                                       │
│                                                                     │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │  Recent Activity Table                                        │ │
│   │  ─────────────────────────────────────────────────────────   │ │
│   │  Row 1                                                        │ │
│   │  Row 2                                                        │ │
│   │  Row 3                                                        │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.3 Form Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                       FORM LAYOUT                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Single Column Form (max-width: 480px):                            │
│                                                                     │
│   ┌────────────────────────────────────────────────────────────┐   │
│   │                                                             │   │
│   │  Organization Name *                           ◄─ Label     │   │
│   │  ┌───────────────────────────────────────────────────────┐ │   │
│   │  │ Acme Corp                                             │ │   │
│   │  └───────────────────────────────────────────────────────┘ │   │
│   │  Enter your company's legal name              ◄─ Helper    │   │
│   │                                                             │   │
│   │  │◄─────────── 24px gap (space-6) ───────────►│            │   │
│   │                                                             │   │
│   │  Admin Email *                                              │   │
│   │  ┌───────────────────────────────────────────────────────┐ │   │
│   │  │ admin@acme.com                                        │ │   │
│   │  └───────────────────────────────────────────────────────┘ │   │
│   │                                                             │   │
│   │  │◄─────────── 24px gap (space-6) ───────────►│            │   │
│   │                                                             │   │
│   │  Team Size                                                  │   │
│   │  ┌───────────────────────────────────────────────────────┐ │   │
│   │  │ Select team size ▼                                    │ │   │
│   │  └───────────────────────────────────────────────────────┘ │   │
│   │                                                             │   │
│   │  │◄─────────── 32px gap (space-8) ───────────►│ (section)  │   │
│   │                                                             │   │
│   │                               [Cancel]  [Save]              │   │
│   │                                     │◄─12px─►│              │   │
│   │                                                             │   │
│   └────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   Spacing Rules:                                                    │
│   • Label to input: 6px (space-1.5)                                 │
│   • Input to helper: 4px (space-1)                                  │
│   • Between fields: 24px (space-6)                                  │
│   • Between sections: 32px (space-8)                                │
│   • Button gap: 12px (space-3)                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.4 Two-Column Form

```
┌─────────────────────────────────────────────────────────────────────┐
│                       TWO-COLUMN FORM                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Desktop (> 768px):                                                │
│   gap: 24px horizontal, 24px vertical                               │
│                                                                     │
│   ┌─────────────────────────────┐ ┌─────────────────────────────┐  │
│   │ First Name *                │ │ Last Name *                 │  │
│   │ ┌─────────────────────────┐ │ │ ┌─────────────────────────┐ │  │
│   │ │ John                    │ │ │ │ Smith                   │ │  │
│   │ └─────────────────────────┘ │ │ └─────────────────────────┘ │  │
│   └─────────────────────────────┘ └─────────────────────────────┘  │
│   │◄──────────── 24px gap ────────────►│                           │
│                                                                     │
│   ┌─────────────────────────────┐ ┌─────────────────────────────┐  │
│   │ Email *                     │ │ Phone                       │  │
│   │ ┌─────────────────────────┐ │ │ ┌─────────────────────────┐ │  │
│   │ │ john@example.com        │ │ │ │ +1 555 123 4567         │ │  │
│   │ └─────────────────────────┘ │ │ └─────────────────────────┘ │  │
│   └─────────────────────────────┘ └─────────────────────────────┘  │
│                                                                     │
│   Full-width field:                                                 │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ Address                                                      │  │
│   │ ┌─────────────────────────────────────────────────────────┐ │  │
│   │ │ 123 Main Street                                         │ │  │
│   │ └─────────────────────────────────────────────────────────┘ │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   Mobile (< 768px): Stack to single column                          │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ First Name *                                                 │  │
│   │ ┌─────────────────────────────────────────────────────────┐ │  │
│   │ │ John                                                    │ │  │
│   │ └─────────────────────────────────────────────────────────┘ │  │
│   │ Last Name *                                                  │  │
│   │ ┌─────────────────────────────────────────────────────────┐ │  │
│   │ │ Smith                                                   │ │  │
│   │ └─────────────────────────────────────────────────────────┘ │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Component Spacing

### 4.1 Card Spacing

```
┌─────────────────────────────────────────────────────────────────────┐
│                       CARD SPACING                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Standard Card:                                                    │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │◄─24px─►                                           ◄─24px─►│   │
│   │                                                             │   │
│   │        Card Title                                           │   │
│   │                              ◄── 16px below title           │   │
│   │        Card content goes here with standard                 │   │
│   │        padding around all sides.                            │   │
│   │                                                             │   │
│   │◄─24px─►                                           ◄─24px─►│   │
│   └─────────────────────────────────────────────────────────────┘   │
│   padding: 24px (space-6) all sides                                 │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Compact Card:                                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │◄16px►                                               ◄16px►│   │
│   │      Compact content                                        │   │
│   │◄16px►                                               ◄16px►│   │
│   └─────────────────────────────────────────────────────────────┘   │
│   padding: 16px (space-4) all sides                                 │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Card with Header:                                                 │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │◄16px► Card Header                      Actions    ◄16px►│   │
│   ├─────────────────────────────────────────────────────────────┤   │
│   │◄24px►                                               ◄24px►│   │
│   │                                                             │   │
│   │       Card body content                                     │   │
│   │                                                             │   │
│   │◄24px►                                               ◄24px►│   │
│   └─────────────────────────────────────────────────────────────┘   │
│   Header padding: 16px 24px                                         │
│   Body padding: 24px                                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Button Spacing

```
┌─────────────────────────────────────────────────────────────────────┐
│                       BUTTON SPACING                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Button Internal Padding:                                          │
│                                                                     │
│   Size   │ Padding X │ Padding Y │ Height │ Icon Gap               │
│   ───────┼───────────┼───────────┼────────┼────────────────────────│
│   xs     │ 8px       │ 4px       │ 24px   │ 4px                    │
│   sm     │ 12px      │ 6px       │ 32px   │ 6px                    │
│   md     │ 16px      │ 8px       │ 40px   │ 8px                    │
│   lg     │ 24px      │ 12px      │ 48px   │ 8px                    │
│   xl     │ 32px      │ 14px      │ 56px   │ 10px                   │
│                                                                     │
│   Visual:                                                           │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │◄16px►  + Add Team  ◄16px►│  md button                       │ │
│   │        │◄8px►│                                                │ │
│   │        icon gap                                               │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   Button Groups:                                                    │
│   gap: 12px (space-3) between buttons                               │
│                                                                     │
│   ┌────────────┐ ┌────────────┐                                    │
│   │  Cancel    │ │   Save     │                                    │
│   └────────────┘ └────────────┘                                    │
│                │◄─12px─►│                                          │
│                                                                     │
│   Stacked Buttons (mobile):                                         │
│   gap: 8px (space-2) between buttons                                │
│                                                                     │
│   ┌────────────────────────────────┐                               │
│   │            Save                │                               │
│   └────────────────────────────────┘                               │
│                │◄─8px─►│                                           │
│   ┌────────────────────────────────┐                               │
│   │           Cancel               │                               │
│   └────────────────────────────────┘                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.3 Table Spacing

```
┌─────────────────────────────────────────────────────────────────────┐
│                       TABLE SPACING                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Standard Table:                                                   │
│                                                                     │
│   ┌────────────────────────────────────────────────────────────┐   │
│   │◄16px► NAME             TEAM       TOKENS    COST   ◄16px►│   │
│   ├────────────────────────────────────────────────────────────┤   │
│   │◄16px► John Smith       Backend    124,567   $12.45 ◄16px►│   │  Row height: 48px
│   ├────────────────────────────────────────────────────────────┤   │
│   │◄16px► Jane Doe         Frontend   89,234    $8.92  ◄16px►│   │
│   ├────────────────────────────────────────────────────────────┤   │
│   │◄16px► Bob Wilson       ML         456,789   $45.67 ◄16px►│   │
│   └────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   Cell Padding: 12px 16px (space-3 space-4)                         │
│   Row Height: 48px                                                  │
│   Header Height: 48px                                               │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Compact Table:                                                    │
│                                                                     │
│   Cell Padding: 8px 12px (space-2 space-3)                          │
│   Row Height: 40px                                                  │
│   Header Height: 40px                                               │
│                                                                     │
│   ───────────────────────────────────────────────────────────────   │
│                                                                     │
│   Relaxed Table:                                                    │
│                                                                     │
│   Cell Padding: 16px 20px (space-4 space-5)                         │
│   Row Height: 64px                                                  │
│   Header Height: 56px                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Content Width

### 5.1 Max Width Constraints

```
┌─────────────────────────────────────────────────────────────────────┐
│                       MAX WIDTH CONSTRAINTS                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Token       │ Width  │ Use Case                                   │
│   ────────────┼────────┼────────────────────────────────────────── │
│   max-w-xs    │ 320px  │ Small modals, tooltips                     │
│   max-w-sm    │ 384px  │ Small forms, sidebars                      │
│   max-w-md    │ 448px  │ Single-column forms                        │
│   max-w-lg    │ 512px  │ Modals (default)                           │
│   max-w-xl    │ 576px  │ Wide forms                                 │
│   max-w-2xl   │ 672px  │ Content areas                              │
│   max-w-3xl   │ 768px  │ Large modals                               │
│   max-w-4xl   │ 896px  │ Wide content                               │
│   max-w-5xl   │ 1024px │ Very wide content                          │
│   max-w-6xl   │ 1152px │ Dashboard content                          │
│   max-w-7xl   │ 1280px │ Full width content                         │
│                                                                     │
│   Visual Scale:                                                     │
│                                                                     │
│   xs  ├──────────────────┤  320px                                  │
│   sm  ├────────────────────────┤  384px                            │
│   md  ├──────────────────────────────┤  448px                      │
│   lg  ├────────────────────────────────────┤  512px                │
│   xl  ├──────────────────────────────────────────┤  576px          │
│   2xl ├────────────────────────────────────────────────┤  672px    │
│   3xl ├──────────────────────────────────────────────────────┤  768│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Reading Width

```
┌─────────────────────────────────────────────────────────────────────┐
│                       READING WIDTH                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   For optimal readability, text blocks should have:                 │
│                                                                     │
│   • Optimal: 60-75 characters per line                              │
│   • Maximum: 80 characters per line                                 │
│   • At 14px body text: ~640px max-width                             │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                                                              │   │
│   │  This is an example of text content that has been           │   │
│   │  constrained to an optimal reading width for better          │   │
│   │  comprehension. Notice how the eyes don't have to travel     │   │
│   │  too far to reach the next line.                             │   │
│   │                                                              │   │
│   │  max-width: 65ch (approximately 640px at 14px)               │   │
│   │                                                              │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   Use Cases:                                                        │
│   • Long-form content                                               │
│   • Documentation                                                   │
│   • Help text                                                       │
│   • Error messages                                                  │
│   • Empty states                                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6. CSS Implementation

### 6.1 Spacing CSS Variables

```css
:root {
  /* Base spacing scale */
  --space-0: 0px;
  --space-0-5: 2px;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;

  /* Layout widths */
  --sidebar-width: 240px;
  --sidebar-collapsed: 64px;
  --header-height: 64px;
  --content-max-width: 1440px;

  /* Grid settings */
  --grid-columns: 12;
  --grid-gutter: 24px;
  --grid-margin: 32px;
}

/* Responsive grid margins */
@media (max-width: 768px) {
  :root {
    --grid-columns: 4;
    --grid-gutter: 16px;
    --grid-margin: 16px;
  }
}

@media (min-width: 768px) and (max-width: 1024px) {
  :root {
    --grid-columns: 8;
    --grid-gutter: 20px;
    --grid-margin: 24px;
  }
}
```

### 6.2 Utility Classes

```css
/* Padding utilities */
.p-0 { padding: 0; }
.p-1 { padding: 4px; }
.p-2 { padding: 8px; }
.p-3 { padding: 12px; }
.p-4 { padding: 16px; }
.p-6 { padding: 24px; }
.p-8 { padding: 32px; }

/* Margin utilities */
.m-0 { margin: 0; }
.m-1 { margin: 4px; }
.m-2 { margin: 8px; }
.m-3 { margin: 12px; }
.m-4 { margin: 16px; }
.m-6 { margin: 24px; }
.m-8 { margin: 32px; }

/* Gap utilities */
.gap-1 { gap: 4px; }
.gap-2 { gap: 8px; }
.gap-3 { gap: 12px; }
.gap-4 { gap: 16px; }
.gap-6 { gap: 24px; }
.gap-8 { gap: 32px; }

/* Max width utilities */
.max-w-xs { max-width: 320px; }
.max-w-sm { max-width: 384px; }
.max-w-md { max-width: 448px; }
.max-w-lg { max-width: 512px; }
.max-w-xl { max-width: 576px; }
.max-w-2xl { max-width: 672px; }
.max-w-3xl { max-width: 768px; }
.max-w-prose { max-width: 65ch; }
```

---

## Related Documents

- [DESIGN-SYSTEM.md](./DESIGN-SYSTEM.md) - Design system overview
- [RESPONSIVE-DESIGN.md](./RESPONSIVE-DESIGN.md) - Responsive guidelines
- [COMPONENT-LIBRARY.md](./COMPONENT-LIBRARY.md) - Component specifications

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-12-29 | Product Design | Initial spacing and grid system |

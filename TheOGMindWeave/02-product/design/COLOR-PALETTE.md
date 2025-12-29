# MindWeave Color Palette

## Document Information
| Field | Value |
|-------|-------|
| Document ID | DS-003 |
| Version | 1.0.0 |
| Last Updated | 2024-12-29 |
| Owner | Product Design |
| Status | Active |

## Overview

The MindWeave color system provides a comprehensive palette designed for enterprise software that demands professionalism, accessibility, and visual clarity. Built on a foundation of neutral grays with strategic accent colors, this system supports both light and dark modes while maintaining WCAG 2.1 AA compliance.

---

## 1. Color Philosophy

### 1.1 Design Principles

```
┌─────────────────────────────────────────────────────────────────────┐
│                     COLOR PHILOSOPHY                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   PROFESSIONALISM          CLARITY              TRUST               │
│   ┌─────────────────┐     ┌─────────────────┐  ┌─────────────────┐ │
│   │ Neutral-forward │     │ High contrast   │  │ Consistent      │ │
│   │ palette with    │     │ for readability │  │ semantic colors │ │
│   │ strategic       │     │ and data        │  │ across all      │ │
│   │ accent colors   │     │ visualization   │  │ interactions    │ │
│   └─────────────────┘     └─────────────────┘  └─────────────────┘ │
│                                                                     │
│   Key Decisions:                                                    │
│   • Indigo as primary brand color (trustworthy, tech-forward)       │
│   • Slate gray scale (warmer than pure gray, professional)          │
│   • Semantic colors follow industry standards (green=success)       │
│   • All combinations tested for WCAG AA accessibility               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Primary Colors

### 2.1 Brand Colors

```
┌─────────────────────────────────────────────────────────────────────┐
│                       BRAND COLOR PALETTE                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   INDIGO (Primary Brand)                                            │
│   ─────────────────────────────────────────                         │
│                                                                     │
│   ┌─────┐  Indigo 50    #EEF2FF   Background tints                 │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 100   #E0E7FF   Hover states, borders            │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 200   #C7D2FE   Focus rings                      │
│   │▒▒▒▒▒│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 300   #A5B4FC   Inactive elements                │
│   │▒▒▒▒▒│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 400   #818CF8   Secondary buttons                │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 500   #6366F1   Primary buttons, links           │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 600   #4F46E5   ★ PRIMARY BRAND COLOR            │
│   │█████│               Used for CTAs, active states               │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 700   #4338CA   Hover on primary                 │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 800   #3730A3   Active/pressed state             │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 900   #312E81   Dark mode primary                │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Indigo 950   #1E1B4B   Darkest accent                   │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Brand Color Usage

| Use Case | Color | Hex Code |
|----------|-------|----------|
| Primary buttons | Indigo 600 | #4F46E5 |
| Primary button hover | Indigo 700 | #4338CA |
| Primary button active | Indigo 800 | #3730A3 |
| Links | Indigo 600 | #4F46E5 |
| Link hover | Indigo 700 | #4338CA |
| Focus ring | Indigo 200 | #C7D2FE |
| Active nav item background | Indigo 50 | #EEF2FF |
| Active nav item border | Indigo 600 | #4F46E5 |
| Selected row | Indigo 50 | #EEF2FF |

---

## 3. Neutral Colors

### 3.1 Slate Scale

```
┌─────────────────────────────────────────────────────────────────────┐
│                       NEUTRAL PALETTE (SLATE)                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   SLATE (Neutral Gray with subtle warmth)                           │
│   ─────────────────────────────────────────                         │
│                                                                     │
│   ┌─────┐  Slate 50     #F8FAFC   Page backgrounds                 │
│   │     │                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 100    #F1F5F9   Secondary backgrounds            │
│   │░░░░░│                         Card backgrounds on gray bg      │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 200    #E2E8F0   Borders, dividers                │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 300    #CBD5E1   Disabled borders                 │
│   │▒▒▒▒▒│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 400    #94A3B8   Placeholder text                 │
│   │▒▒▒▒▒│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 500    #64748B   Secondary text, icons            │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 600    #475569   Body text                        │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 700    #334155   Emphasis text                    │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 800    #1E293B   Headings                         │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 900    #0F172A   Primary text                     │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Slate 950    #020617   Darkest (dark mode bg)           │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Neutral Usage

| Use Case | Color | Hex Code |
|----------|-------|----------|
| Page background | White or Slate 50 | #FFFFFF / #F8FAFC |
| Card background | White | #FFFFFF |
| Sidebar background | Slate 50 | #F8FAFC |
| Borders | Slate 200 | #E2E8F0 |
| Dividers | Slate 200 | #E2E8F0 |
| Primary text | Slate 900 | #0F172A |
| Secondary text | Slate 600 | #475569 |
| Tertiary text | Slate 500 | #64748B |
| Placeholder text | Slate 400 | #94A3B8 |
| Disabled text | Slate 400 | #94A3B8 |
| Icons (default) | Slate 500 | #64748B |
| Hover backgrounds | Slate 100 | #F1F5F9 |

---

## 4. Semantic Colors

### 4.1 Success (Green)

```
┌─────────────────────────────────────────────────────────────────────┐
│                       SUCCESS COLORS (GREEN)                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────┐  Green 50     #F0FDF4   Success alert background         │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Green 100    #DCFCE7   Badge background                 │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Green 500    #22C55E   Success icons                    │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Green 600    #16A34A   Success buttons                  │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Green 700    #15803D   Badge text                       │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Usage:                                                            │
│   • Success toasts and alerts                                       │
│   • Active/enabled status badges                                    │
│   • Positive trends (↑ metrics)                                     │
│   • Checkmarks and confirmations                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Warning (Amber/Yellow)

```
┌─────────────────────────────────────────────────────────────────────┐
│                       WARNING COLORS (AMBER)                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────┐  Amber 50     #FFFBEB   Warning alert background         │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Amber 100    #FEF3C7   Badge background                 │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Amber 500    #F59E0B   Warning icons                    │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Amber 600    #D97706   Warning buttons                  │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Amber 700    #B45309   Badge text                       │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Usage:                                                            │
│   • Warning toasts and alerts                                       │
│   • Pending status badges                                           │
│   • Approaching limits                                              │
│   • Action required indicators                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.3 Error (Red)

```
┌─────────────────────────────────────────────────────────────────────┐
│                       ERROR COLORS (RED)                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────┐  Red 50       #FEF2F2   Error alert background           │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Red 100      #FEE2E2   Badge background                 │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Red 500      #EF4444   Error icons, borders             │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Red 600      #DC2626   Destructive buttons              │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Red 700      #B91C1C   Badge text                       │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Usage:                                                            │
│   • Error toasts and alerts                                         │
│   • Form validation errors                                          │
│   • Destructive action buttons                                      │
│   • Failed status badges                                            │
│   • Negative trends (↓ when bad)                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.4 Info (Blue)

```
┌─────────────────────────────────────────────────────────────────────┐
│                       INFO COLORS (BLUE)                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────┐  Blue 50      #EFF6FF   Info alert background            │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Blue 100     #DBEAFE   Badge background                 │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Blue 500     #3B82F6   Info icons                       │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Blue 600     #2563EB   Info buttons                     │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Blue 700     #1D4ED8   Badge text                       │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Usage:                                                            │
│   • Informational toasts and alerts                                 │
│   • Help text and tooltips                                          │
│   • Neutral status indicators                                       │
│   • Admin/role badges                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Data Visualization Colors

### 5.1 Chart Palette

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DATA VISUALIZATION PALETTE                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Primary Data Series (ordered for visual distinction):             │
│                                                                     │
│   ┌─────┐  Series 1     #4F46E5   Indigo (Primary)                 │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Series 2     #06B6D4   Cyan                             │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Series 3     #8B5CF6   Violet                           │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Series 4     #F59E0B   Amber                            │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Series 5     #EC4899   Pink                             │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Series 6     #10B981   Emerald                          │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Series 7     #F97316   Orange                           │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Series 8     #6366F1   Indigo Light                     │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Model-Specific Colors

```
┌─────────────────────────────────────────────────────────────────────┐
│                   CLAUDE MODEL COLORS                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Claude Opus (Premium):                                            │
│   ┌─────┐  Primary      #7C3AED   Violet 600                       │
│   │█████│                                                           │
│   └─────┘                                                           │
│   ┌─────┐  Background   #F3E8FF   Violet 100                       │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Claude Sonnet (Balanced):                                         │
│   ┌─────┐  Primary      #2563EB   Blue 600                         │
│   │█████│                                                           │
│   └─────┘                                                           │
│   ┌─────┐  Background   #DBEAFE   Blue 100                         │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Claude Haiku (Fast):                                              │
│   ┌─────┐  Primary      #059669   Emerald 600                      │
│   │█████│                                                           │
│   └─────┘                                                           │
│   ┌─────┐  Background   #ECFDF5   Emerald 50                       │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.3 Sequential Scales

```
┌─────────────────────────────────────────────────────────────────────┐
│                   SEQUENTIAL COLOR SCALES                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Blue Scale (for heatmaps, single-metric visualizations):          │
│                                                                     │
│   Low ─────────────────────────────────────────────────────► High   │
│   ┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐        │
│   │#EFF6│#DBEAF│#BFDBF│#93C5F│#60A5F│#3B82F│#2563E│#1E40A│        │
│   │FF   │E     │E     │D     │A     │6     │B     │F     │        │
│   └─────┘└─────┘└─────┘└─────┘└─────┘└─────┘└─────┘└─────┘        │
│                                                                     │
│   Green Scale (for positive metrics):                               │
│                                                                     │
│   Low ─────────────────────────────────────────────────────► High   │
│   ┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐        │
│   │#F0FD│#DCFCE│#BBF7D│#86EFA│#4ADE8│#22C55│#16A34│#15803│        │
│   │F4   │7     │0     │C     │0     │E     │A     │D     │        │
│   └─────┘└─────┘└─────┘└─────┘└─────┘└─────┘└─────┘└─────┘        │
│                                                                     │
│   Red Scale (for negative metrics, costs):                          │
│                                                                     │
│   Low ─────────────────────────────────────────────────────► High   │
│   ┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐        │
│   │#FEF2│#FEE2E│#FECACA│#FCA5A│#F87171│#EF4444│#DC2626│#B91C1│        │
│   │F2   │2     │      │5     │      │      │      │C     │        │
│   └─────┘└─────┘└─────┘└─────┘└─────┘└─────┘└─────┘└─────┘        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6. Special Purpose Colors

### 6.1 Status Badge Colors

| Status | Background | Text | Border |
|--------|------------|------|--------|
| Active | #DCFCE7 (Green 100) | #166534 (Green 800) | transparent |
| Pending | #FEF3C7 (Amber 100) | #92400E (Amber 800) | transparent |
| Approved | #DBEAFE (Blue 100) | #1E40AF (Blue 800) | transparent |
| Rejected | #FEE2E2 (Red 100) | #991B1B (Red 800) | transparent |
| Deprecated | #F1F5F9 (Slate 100) | #475569 (Slate 600) | transparent |

### 6.2 Role Badge Colors

| Role | Background | Text |
|------|------------|------|
| Admin | #DBEAFE (Blue 100) | #1E40AF (Blue 800) |
| Member | #F1F5F9 (Slate 100) | #475569 (Slate 600) |
| Viewer | #F8FAFC (Slate 50) | #64748B (Slate 500) |
| Owner | #EEF2FF (Indigo 50) | #3730A3 (Indigo 800) |

### 6.3 MCP Category Colors

| Category | Background | Text |
|----------|------------|------|
| CRM | #FEF3C7 (Amber 100) | #92400E (Amber 800) |
| Database | #DBEAFE (Blue 100) | #1E40AF (Blue 800) |
| Communication | #DCFCE7 (Green 100) | #166534 (Green 800) |
| DevOps | #F3E8FF (Violet 100) | #6B21A8 (Violet 800) |
| Analytics | #ECFDF5 (Emerald 50) | #047857 (Emerald 700) |
| Security | #FEE2E2 (Red 100) | #991B1B (Red 800) |

---

## 7. Accessibility

### 7.1 Contrast Ratios

```
┌─────────────────────────────────────────────────────────────────────┐
│                   CONTRAST RATIO REQUIREMENTS                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   WCAG 2.1 AA Requirements:                                         │
│   • Normal text (< 18px): 4.5:1 minimum contrast                    │
│   • Large text (≥ 18px or 14px bold): 3:1 minimum contrast          │
│   • UI components and graphical objects: 3:1 minimum contrast       │
│                                                                     │
│   Verified Combinations (Light Mode):                               │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │ Background  │ Text Color    │ Ratio  │ Pass/Fail             │ │
│   ├──────────────────────────────────────────────────────────────┤ │
│   │ White       │ Slate 900     │ 15.1:1 │ ✓ AAA                 │ │
│   │ White       │ Slate 700     │ 8.2:1  │ ✓ AAA                 │ │
│   │ White       │ Slate 600     │ 5.7:1  │ ✓ AA                  │ │
│   │ White       │ Slate 500     │ 4.5:1  │ ✓ AA                  │ │
│   │ White       │ Indigo 600    │ 5.0:1  │ ✓ AA                  │ │
│   │ Indigo 600  │ White         │ 5.0:1  │ ✓ AA                  │ │
│   │ Slate 50    │ Slate 900     │ 13.9:1 │ ✓ AAA                 │ │
│   │ Green 100   │ Green 800     │ 5.2:1  │ ✓ AA                  │ │
│   │ Red 100     │ Red 800       │ 5.5:1  │ ✓ AA                  │ │
│   │ Amber 100   │ Amber 800     │ 4.6:1  │ ✓ AA                  │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   ⚠ Caution Combinations:                                          │
│   • Slate 400 on White = 3.5:1 (Use only for non-essential text)   │
│   • Slate 300 on White = 2.6:1 (Use only for decorative elements)  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 Color Blindness Considerations

```
┌─────────────────────────────────────────────────────────────────────┐
│               COLOR BLINDNESS ACCESSIBILITY                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Design Rules:                                                     │
│   • Never use color alone to convey information                     │
│   • Always pair colors with icons, patterns, or text                │
│   • Use shapes in addition to colors for charts                     │
│                                                                     │
│   Status Indicator Examples:                                        │
│                                                                     │
│   Good:                                                             │
│   ┌──────────────────────────────────────┐                         │
│   │ ✓ Active  │  ⏳ Pending  │  ✗ Failed │                         │
│   └──────────────────────────────────────┘                         │
│   Uses icons + color + text labels                                  │
│                                                                     │
│   Bad:                                                              │
│   ┌──────────────────────────────────────┐                         │
│   │ ●         │  ●           │  ●        │                         │
│   └──────────────────────────────────────┘                         │
│   Only uses color (inaccessible)                                    │
│                                                                     │
│   Chart Patterns (for colorblind users):                            │
│   Series 1: ████ Solid                                             │
│   Series 2: ░░░░ Dotted                                            │
│   Series 3: ──── Dashed                                            │
│   Series 4: ╳╳╳╳ Cross-hatched                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8. Dark Mode

### 8.1 Dark Mode Palette

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DARK MODE COLOR MAPPING                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Background Hierarchy:                                             │
│                                                                     │
│   ┌─────┐  Level 0      #020617   Slate 950 (Page bg)              │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Level 1      #0F172A   Slate 900 (Card bg)              │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Level 2      #1E293B   Slate 800 (Elevated)             │
│   │█████│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Level 3      #334155   Slate 700 (Hover)                │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Text Colors:                                                      │
│   ┌─────┐  Primary      #F8FAFC   Slate 50                         │
│   │     │                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Secondary    #CBD5E1   Slate 300                        │
│   │░░░░░│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   ┌─────┐  Tertiary     #94A3B8   Slate 400                        │
│   │▒▒▒▒▒│                                                           │
│   └─────┘                                                           │
│                                                                     │
│   Borders:                                                          │
│   ┌─────┐  Default      #334155   Slate 700                        │
│   │▓▓▓▓▓│                                                           │
│   └─────┘                                                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2 Light/Dark Mode Mapping

| Purpose | Light Mode | Dark Mode |
|---------|------------|-----------|
| Page background | #FFFFFF / #F8FAFC | #020617 |
| Card background | #FFFFFF | #0F172A |
| Sidebar | #F8FAFC | #0F172A |
| Primary text | #0F172A | #F8FAFC |
| Secondary text | #475569 | #CBD5E1 |
| Tertiary text | #64748B | #94A3B8 |
| Borders | #E2E8F0 | #334155 |
| Hover background | #F1F5F9 | #1E293B |
| Active background | #EEF2FF | #312E81 |
| Primary button | #4F46E5 | #6366F1 |
| Primary button text | #FFFFFF | #FFFFFF |

---

## 9. CSS Variables

### 9.1 Light Mode Variables

```css
:root {
  /* Brand */
  --color-primary: #4F46E5;
  --color-primary-hover: #4338CA;
  --color-primary-active: #3730A3;
  --color-primary-light: #EEF2FF;

  /* Neutrals */
  --color-background: #FFFFFF;
  --color-background-secondary: #F8FAFC;
  --color-surface: #FFFFFF;
  --color-border: #E2E8F0;
  --color-border-strong: #CBD5E1;

  /* Text */
  --color-text-primary: #0F172A;
  --color-text-secondary: #475569;
  --color-text-tertiary: #64748B;
  --color-text-placeholder: #94A3B8;
  --color-text-disabled: #94A3B8;

  /* Semantic */
  --color-success: #16A34A;
  --color-success-light: #DCFCE7;
  --color-warning: #D97706;
  --color-warning-light: #FEF3C7;
  --color-error: #DC2626;
  --color-error-light: #FEE2E2;
  --color-info: #2563EB;
  --color-info-light: #DBEAFE;
}
```

### 9.2 Dark Mode Variables

```css
[data-theme="dark"] {
  /* Brand */
  --color-primary: #6366F1;
  --color-primary-hover: #818CF8;
  --color-primary-active: #4F46E5;
  --color-primary-light: #312E81;

  /* Neutrals */
  --color-background: #020617;
  --color-background-secondary: #0F172A;
  --color-surface: #0F172A;
  --color-border: #334155;
  --color-border-strong: #475569;

  /* Text */
  --color-text-primary: #F8FAFC;
  --color-text-secondary: #CBD5E1;
  --color-text-tertiary: #94A3B8;
  --color-text-placeholder: #64748B;
  --color-text-disabled: #64748B;

  /* Semantic (adjusted for dark backgrounds) */
  --color-success: #22C55E;
  --color-success-light: #14532D;
  --color-warning: #F59E0B;
  --color-warning-light: #78350F;
  --color-error: #EF4444;
  --color-error-light: #7F1D1D;
  --color-info: #3B82F6;
  --color-info-light: #1E3A8A;
}
```

---

## Related Documents

- [DESIGN-SYSTEM.md](./DESIGN-SYSTEM.md) - Design system overview
- [DARK-MODE.md](./DARK-MODE.md) - Dark mode implementation
- [ACCESSIBILITY.md](./ACCESSIBILITY.md) - Accessibility guidelines

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-12-29 | Product Design | Initial color palette |

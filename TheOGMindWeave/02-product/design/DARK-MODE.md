# MindWeave Dark Mode

## Document Information
| Field | Value |
|-------|-------|
| Document ID | DS-009 |
| Version | 1.0.0 |
| Last Updated | 2024-12-29 |
| Owner | Product Design |
| Status | Active |

## Overview

Dark mode provides an alternative color scheme that reduces eye strain in low-light environments, conserves battery on OLED displays, and offers user preference choice. This document defines the dark mode color system, implementation patterns, and transition behaviors for the MindWeave platform.

---

## 1. Dark Mode Strategy

### 1.1 Design Approach

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DARK MODE PHILOSOPHY                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Principles:                                                       │
│                                                                     │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│   │  NOT INVERTED   │  │  ELEVATED       │  │  REDUCED        │    │
│   │                 │  │  SURFACES       │  │  CONTRAST       │    │
│   │  Dark mode is   │  │                 │  │                 │    │
│   │  a redesign,    │  │  Higher Z-index │  │  Softer whites, │    │
│   │  not a simple   │  │  = lighter      │  │  not pure #FFF  │    │
│   │  color invert   │  │  background     │  │  to reduce      │    │
│   │                 │  │                 │  │  eye strain     │    │
│   └─────────────────┘  └─────────────────┘  └─────────────────┘    │
│                                                                     │
│   Key Differences from Light Mode:                                  │
│   • Surfaces get lighter as they elevate (opposite of light mode)   │
│   • Shadows are less visible; use surface color for elevation       │
│   • Pure white (#FFF) is avoided; use Slate 50 for text            │
│   • Primary colors are slightly lighter for contrast                │
│   • Borders are more prominent for element separation               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Theme Detection

```
┌─────────────────────────────────────────────────────────────────────┐
│                   THEME DETECTION                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Theme Options:                                                    │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ Appearance                                                   │  │
│   │                                                              │  │
│   │ ○ Light                                                      │  │
│   │ ○ Dark                                                       │  │
│   │ ● System (follow OS setting)  ◄── Default                   │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   Detection Priority:                                               │
│   1. User preference (stored in localStorage)                       │
│   2. System preference (prefers-color-scheme media query)           │
│   3. Default to light mode                                          │
│                                                                     │
│   Implementation:                                                   │
│   const getTheme = () => {                                          │
│     const stored = localStorage.getItem('theme');                   │
│     if (stored && stored !== 'system') return stored;               │
│                                                                     │
│     return window.matchMedia('(prefers-color-scheme: dark)')        │
│       .matches ? 'dark' : 'light';                                  │
│   };                                                                │
│                                                                     │
│   // Listen for system changes                                      │
│   window.matchMedia('(prefers-color-scheme: dark)')                 │
│     .addEventListener('change', (e) => {                            │
│       if (localStorage.getItem('theme') === 'system') {             │
│         applyTheme(e.matches ? 'dark' : 'light');                   │
│       }                                                             │
│     });                                                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Dark Mode Color Palette

### 2.1 Background Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DARK BACKGROUND LEVELS                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Higher elevation = Lighter background                             │
│                                                                     │
│   Level 0 - Page Background                                         │
│   ┌─────┐  #020617  Slate 950                                      │
│   │█████│  Darkest level, main page background                      │
│   └─────┘                                                           │
│                                                                     │
│   Level 1 - Surface (Cards, Sidebar)                                │
│   ┌─────┐  #0F172A  Slate 900                                      │
│   │█████│  Primary surfaces like cards, navigation                  │
│   └─────┘                                                           │
│                                                                     │
│   Level 2 - Elevated Surface (Modals, Dropdowns)                    │
│   ┌─────┐  #1E293B  Slate 800                                      │
│   │█████│  Modals, popovers, elevated cards                         │
│   └─────┘                                                           │
│                                                                     │
│   Level 3 - Hover State                                             │
│   ┌─────┐  #334155  Slate 700                                      │
│   │▓▓▓▓▓│  Hover backgrounds, active states                         │
│   └─────┘                                                           │
│                                                                     │
│   Level 4 - Selected/Active                                         │
│   ┌─────┐  #475569  Slate 600                                      │
│   │▓▓▓▓▓│  Selected rows, pressed states                            │
│   └─────┘                                                           │
│                                                                     │
│   Visual Comparison:                                                │
│                                                                     │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │ Page Background (Level 0)                                     │ │
│   │ ┌──────────────────────────────────────────────────────────┐ │ │
│   │ │ Card (Level 1)                                           │ │ │
│   │ │ ┌──────────────────────────────────────────────────────┐ │ │ │
│   │ │ │ Modal (Level 2)                                      │ │ │ │
│   │ │ │ ┌──────────────────────────────────────────────────┐ │ │ │ │
│   │ │ │ │ Dropdown (Level 2)                               │ │ │ │ │
│   │ │ │ └──────────────────────────────────────────────────┘ │ │ │ │
│   │ │ └──────────────────────────────────────────────────────┘ │ │ │
│   │ └──────────────────────────────────────────────────────────┘ │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Text Colors

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DARK MODE TEXT COLORS                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Primary Text                                                      │
│   ┌─────┐  #F8FAFC  Slate 50                                       │
│   │     │  Main headings, primary content                           │
│   └─────┘  Contrast on Slate 900: 14.8:1 ✓                         │
│                                                                     │
│   Secondary Text                                                    │
│   ┌─────┐  #CBD5E1  Slate 300                                      │
│   │░░░░░│  Body text, descriptions                                  │
│   └─────┘  Contrast on Slate 900: 8.3:1 ✓                          │
│                                                                     │
│   Tertiary Text                                                     │
│   ┌─────┐  #94A3B8  Slate 400                                      │
│   │▒▒▒▒▒│  Labels, captions, timestamps                             │
│   └─────┘  Contrast on Slate 900: 5.1:1 ✓                          │
│                                                                     │
│   Disabled Text                                                     │
│   ┌─────┐  #64748B  Slate 500                                      │
│   │▓▓▓▓▓│  Disabled states, placeholders                            │
│   └─────┘  Contrast on Slate 900: 3.3:1 (large text only)          │
│                                                                     │
│   Link Text                                                         │
│   ┌─────┐  #818CF8  Indigo 400                                     │
│   │▒▒▒▒▒│  Clickable links                                          │
│   └─────┘  Lighter than light mode for visibility                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.3 Border Colors

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DARK MODE BORDERS                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Default Border                                                    │
│   ┌─────┐  #334155  Slate 700                                      │
│   │▓▓▓▓▓│  Card borders, input borders, dividers                    │
│   └─────┘                                                           │
│                                                                     │
│   Subtle Border                                                     │
│   ┌─────┐  #1E293B  Slate 800                                      │
│   │█████│  Very subtle separation lines                             │
│   └─────┘                                                           │
│                                                                     │
│   Strong Border                                                     │
│   ┌─────┐  #475569  Slate 600                                      │
│   │▓▓▓▓▓│  Emphasized borders, focus states                         │
│   └─────┘                                                           │
│                                                                     │
│   Focus Ring                                                        │
│   ┌─────┐  #6366F1  Indigo 500                                     │
│   │▓▓▓▓▓│  Keyboard focus indicator                                 │
│   └─────┘                                                           │
│                                                                     │
│   Note: Borders are more important in dark mode for separation      │
│   since shadows are less visible against dark backgrounds.          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.4 Semantic Colors (Adjusted)

```
┌─────────────────────────────────────────────────────────────────────┐
│                   SEMANTIC COLORS - DARK MODE                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Success                                                           │
│   ┌─────┐  Primary: #22C55E (Green 500)                            │
│   │▓▓▓▓▓│  Background: #14532D (Green 900 @ 20% opacity)            │
│   └─────┘  Text: #4ADE80 (Green 400)                               │
│                                                                     │
│   Warning                                                           │
│   ┌─────┐  Primary: #F59E0B (Amber 500)                            │
│   │▓▓▓▓▓│  Background: #78350F (Amber 900 @ 20% opacity)            │
│   └─────┘  Text: #FBBF24 (Amber 400)                               │
│                                                                     │
│   Error                                                             │
│   ┌─────┐  Primary: #EF4444 (Red 500)                              │
│   │▓▓▓▓▓│  Background: #7F1D1D (Red 900 @ 20% opacity)              │
│   └─────┘  Text: #F87171 (Red 400)                                 │
│                                                                     │
│   Info                                                              │
│   ┌─────┐  Primary: #3B82F6 (Blue 500)                             │
│   │▓▓▓▓▓│  Background: #1E3A8A (Blue 900 @ 20% opacity)             │
│   └─────┘  Text: #60A5FA (Blue 400)                                │
│                                                                     │
│   Alert Examples:                                                   │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ ✓  Changes saved successfully                                │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   Dark green background, lighter green text                         │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ ✕  Failed to save changes                                    │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   Dark red background, lighter red text                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.5 Brand Colors (Adjusted)

```
┌─────────────────────────────────────────────────────────────────────┐
│                   BRAND COLORS - DARK MODE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Primary Button                                                    │
│   ┌─────┐  Background: #6366F1 (Indigo 500)                        │
│   │▓▓▓▓▓│  Lighter than light mode for visibility                   │
│   └─────┘  Text: #FFFFFF                                           │
│                                                                     │
│   Primary Button Hover                                              │
│   ┌─────┐  Background: #818CF8 (Indigo 400)                        │
│   │▒▒▒▒▒│  Even lighter on hover                                    │
│   └─────┘                                                           │
│                                                                     │
│   Active Navigation                                                 │
│   ┌─────┐  Background: #312E81 (Indigo 900)                        │
│   │█████│  Dark indigo for selected nav items                       │
│   └─────┘  Text: #A5B4FC (Indigo 300)                              │
│                                                                     │
│   Link Color                                                        │
│   ┌─────┐  #818CF8 (Indigo 400)                                    │
│   │▒▒▒▒▒│  Lighter than light mode (#4F46E5)                        │
│   └─────┘                                                           │
│                                                                     │
│   Focus Ring                                                        │
│   ┌─────┐  #6366F1 (Indigo 500)                                    │
│   │▓▓▓▓▓│  Visible against dark backgrounds                         │
│   └─────┘                                                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Light/Dark Mapping

### 3.1 Complete Color Mapping

| Purpose | Light Mode | Dark Mode |
|---------|------------|-----------|
| **Backgrounds** | | |
| Page background | #FFFFFF | #020617 (Slate 950) |
| Surface (cards) | #FFFFFF | #0F172A (Slate 900) |
| Elevated surface | #FFFFFF + shadow | #1E293B (Slate 800) |
| Sidebar | #F8FAFC (Slate 50) | #0F172A (Slate 900) |
| Input background | #FFFFFF | #0F172A (Slate 900) |
| Hover background | #F1F5F9 (Slate 100) | #1E293B (Slate 800) |
| Selected/Active | #EEF2FF (Indigo 50) | #312E81 (Indigo 900) |
| **Text** | | |
| Primary | #0F172A (Slate 900) | #F8FAFC (Slate 50) |
| Secondary | #475569 (Slate 600) | #CBD5E1 (Slate 300) |
| Tertiary | #64748B (Slate 500) | #94A3B8 (Slate 400) |
| Placeholder | #94A3B8 (Slate 400) | #64748B (Slate 500) |
| Disabled | #94A3B8 (Slate 400) | #475569 (Slate 600) |
| **Borders** | | |
| Default | #E2E8F0 (Slate 200) | #334155 (Slate 700) |
| Strong | #CBD5E1 (Slate 300) | #475569 (Slate 600) |
| **Interactive** | | |
| Primary button | #4F46E5 (Indigo 600) | #6366F1 (Indigo 500) |
| Primary hover | #4338CA (Indigo 700) | #818CF8 (Indigo 400) |
| Link | #4F46E5 (Indigo 600) | #818CF8 (Indigo 400) |
| Focus ring | #C7D2FE (Indigo 200) | #6366F1 (Indigo 500) |

### 3.2 Shadows in Dark Mode

```
┌─────────────────────────────────────────────────────────────────────┐
│                   SHADOWS IN DARK MODE                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Light Mode Shadows:                                               │
│   • Shadows are visible against light backgrounds                   │
│   • Used for elevation and depth                                    │
│                                                                     │
│   shadow-sm: 0 1px 2px rgba(0,0,0,0.05)                             │
│   shadow-md: 0 4px 6px rgba(0,0,0,0.1)                              │
│   shadow-lg: 0 10px 15px rgba(0,0,0,0.1)                            │
│                                                                     │
│   Dark Mode Approach:                                               │
│   • Shadows are nearly invisible on dark backgrounds                │
│   • Use SURFACE COLOR for elevation instead                         │
│   • Add subtle border for definition                                │
│                                                                     │
│   Level 0 (Page):     #020617                                       │
│   Level 1 (Card):     #0F172A + 1px border #334155                 │
│   Level 2 (Modal):    #1E293B + 1px border #475569                 │
│   Level 3 (Dropdown): #334155 + 1px border #475569                 │
│                                                                     │
│   Optional: Very subtle shadow for dramatic elevation               │
│   shadow-dark: 0 8px 32px rgba(0,0,0,0.5)                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Component Adaptations

### 4.1 Buttons

```
┌─────────────────────────────────────────────────────────────────────┐
│                   BUTTON DARK MODE                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Primary Button:                                                   │
│   Light                          Dark                               │
│   ┌────────────────┐            ┌────────────────┐                 │
│   │   Action       │            │   Action       │                 │
│   └────────────────┘            └────────────────┘                 │
│   bg: Indigo 600                bg: Indigo 500                     │
│   text: White                   text: White                        │
│                                                                     │
│   Secondary Button:                                                 │
│   Light                          Dark                               │
│   ┌────────────────┐            ┌────────────────┐                 │
│   │   Action       │            │   Action       │                 │
│   └────────────────┘            └────────────────┘                 │
│   bg: Slate 100                 bg: Slate 800                      │
│   text: Slate 700               text: Slate 200                    │
│                                                                     │
│   Outline Button:                                                   │
│   Light                          Dark                               │
│   ┌────────────────┐            ┌────────────────┐                 │
│   │   Action       │            │   Action       │                 │
│   └────────────────┘            └────────────────┘                 │
│   border: Slate 200             border: Slate 600                  │
│   text: Slate 700               text: Slate 200                    │
│                                                                     │
│   Ghost Button:                                                     │
│   Light                          Dark                               │
│   ┌────────────────┐            ┌────────────────┐                 │
│   │   Action       │            │   Action       │                 │
│   └────────────────┘            └────────────────┘                 │
│   bg: transparent               bg: transparent                    │
│   text: Indigo 600              text: Indigo 400                   │
│   hover: Slate 100              hover: Slate 800                   │
│                                                                     │
│   Destructive Button:                                               │
│   Light                          Dark                               │
│   ┌────────────────┐            ┌────────────────┐                 │
│   │   Delete       │            │   Delete       │                 │
│   └────────────────┘            └────────────────┘                 │
│   bg: Red 600                   bg: Red 600                        │
│   text: White                   text: White                        │
│   (No change needed)                                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Form Inputs

```
┌─────────────────────────────────────────────────────────────────────┐
│                   INPUT DARK MODE                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Default Input:                                                    │
│   Light                                                             │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ Input value                                                  │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   bg: White, border: Slate 200, text: Slate 900                    │
│                                                                     │
│   Dark                                                              │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ Input value                                                  │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   bg: Slate 900, border: Slate 700, text: Slate 50                 │
│                                                                     │
│   Focus State (Dark):                                               │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ Input value                                                  │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   border: Indigo 500, ring: Indigo 500/20%                         │
│                                                                     │
│   Error State (Dark):                                               │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ Invalid value                                                │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   ⚠ Error message                                                   │
│   border: Red 500, error text: Red 400                             │
│                                                                     │
│   Disabled Input (Dark):                                            │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ Disabled value                                               │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   bg: Slate 800, text: Slate 500, opacity: 0.7                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.3 Cards & Surfaces

```
┌─────────────────────────────────────────────────────────────────────┐
│                   CARDS DARK MODE                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Light Mode Card:                                                  │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                                                              │  │
│   │  Card content with shadow                                    │  │
│   │                                                              │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   bg: White, shadow: md, border: none                              │
│                                                                     │
│   Dark Mode Card:                                                   │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                                                              │  │
│   │  Card content with border                                    │  │
│   │                                                              │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   bg: Slate 900, shadow: none, border: 1px Slate 700               │
│                                                                     │
│   Hover State:                                                      │
│   Light: shadow increases                                           │
│   Dark: border color lightens to Slate 600                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.4 Navigation

```
┌─────────────────────────────────────────────────────────────────────┐
│                   NAVIGATION DARK MODE                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Light Mode Sidebar:                                               │
│   ┌─────────────────────────┐                                      │
│   │  ◇ MindWeave            │                                      │
│   ├─────────────────────────┤  bg: Slate 50                        │
│   │  ■ Dashboard            │  active bg: Indigo 50                │
│   │  □ Analytics            │  active text: Indigo 600             │
│   │  □ MCP Registry         │  text: Slate 600                     │
│   └─────────────────────────┘                                      │
│                                                                     │
│   Dark Mode Sidebar:                                                │
│   ┌─────────────────────────┐                                      │
│   │  ◇ MindWeave            │                                      │
│   ├─────────────────────────┤  bg: Slate 900                       │
│   │  ■ Dashboard            │  active bg: Indigo 900               │
│   │  □ Analytics            │  active text: Indigo 300             │
│   │  □ MCP Registry         │  text: Slate 400                     │
│   └─────────────────────────┘                                      │
│                                                                     │
│   Header Bar:                                                       │
│   Light: bg White, border-bottom Slate 200                          │
│   Dark: bg Slate 900, border-bottom Slate 700                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Implementation

### 5.1 CSS Variables

```css
/* Light theme (default) */
:root {
  --color-bg-page: #ffffff;
  --color-bg-surface: #ffffff;
  --color-bg-elevated: #ffffff;
  --color-bg-hover: #f1f5f9;
  --color-bg-selected: #eef2ff;

  --color-text-primary: #0f172a;
  --color-text-secondary: #475569;
  --color-text-tertiary: #64748b;
  --color-text-placeholder: #94a3b8;

  --color-border-default: #e2e8f0;
  --color-border-strong: #cbd5e1;

  --color-primary: #4f46e5;
  --color-primary-hover: #4338ca;
  --color-link: #4f46e5;
  --color-focus-ring: #c7d2fe;

  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
}

/* Dark theme */
[data-theme="dark"] {
  --color-bg-page: #020617;
  --color-bg-surface: #0f172a;
  --color-bg-elevated: #1e293b;
  --color-bg-hover: #1e293b;
  --color-bg-selected: #312e81;

  --color-text-primary: #f8fafc;
  --color-text-secondary: #cbd5e1;
  --color-text-tertiary: #94a3b8;
  --color-text-placeholder: #64748b;

  --color-border-default: #334155;
  --color-border-strong: #475569;

  --color-primary: #6366f1;
  --color-primary-hover: #818cf8;
  --color-link: #818cf8;
  --color-focus-ring: #6366f1;

  --shadow-sm: none;
  --shadow-md: none;
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.5);
}
```

### 5.2 Theme Toggle Component

```typescript
interface ThemeToggleProps {
  theme: 'light' | 'dark' | 'system';
  onChange: (theme: 'light' | 'dark' | 'system') => void;
}

const ThemeToggle = ({ theme, onChange }: ThemeToggleProps) => {
  return (
    <select value={theme} onChange={(e) => onChange(e.target.value)}>
      <option value="light">Light</option>
      <option value="dark">Dark</option>
      <option value="system">System</option>
    </select>
  );
};

// Apply theme to document
const applyTheme = (theme: 'light' | 'dark') => {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
};
```

### 5.3 Transition Animation

```css
/* Smooth theme transition */
:root {
  --theme-transition: 200ms ease;
}

* {
  transition:
    background-color var(--theme-transition),
    border-color var(--theme-transition),
    color var(--theme-transition);
}

/* Disable transitions during theme change to prevent flash */
.theme-changing * {
  transition: none !important;
}
```

---

## 6. Dark Mode Checklist

### 6.1 Implementation Checklist

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DARK MODE CHECKLIST                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Colors:                                                           │
│   □ All backgrounds use appropriate dark palette                    │
│   □ Text colors maintain contrast requirements                      │
│   □ Links are visible against dark backgrounds                      │
│   □ Semantic colors (success, error) adjusted                       │
│   □ Primary brand colors adjusted for visibility                    │
│   □ Border colors visible against dark backgrounds                  │
│                                                                     │
│   Components:                                                       │
│   □ Buttons use dark mode variants                                  │
│   □ Form inputs have dark styling                                   │
│   □ Cards use borders instead of shadows                            │
│   □ Modals use elevated surface color                               │
│   □ Dropdowns and popovers styled                                   │
│   □ Tables have visible borders                                     │
│   □ Charts use appropriate colors                                   │
│                                                                     │
│   Assets:                                                           │
│   □ Logo has dark mode variant                                      │
│   □ Icons visible on dark backgrounds                               │
│   □ Images don't appear too bright                                  │
│   □ Illustrations have dark variants                                │
│                                                                     │
│   Accessibility:                                                    │
│   □ Focus indicators visible                                        │
│   □ Contrast ratios meet AA (4.5:1 for text)                        │
│   □ Status indicators use shape + color                             │
│                                                                     │
│   System:                                                           │
│   □ Theme preference saved                                          │
│   □ System preference detected                                      │
│   □ Transitions are smooth                                          │
│   □ No flash on page load                                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Related Documents

- [COLOR-PALETTE.md](./COLOR-PALETTE.md) - Complete color specifications
- [DESIGN-SYSTEM.md](./DESIGN-SYSTEM.md) - Design system overview
- [ACCESSIBILITY.md](./ACCESSIBILITY.md) - Accessibility guidelines

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-12-29 | Product Design | Initial dark mode specification |

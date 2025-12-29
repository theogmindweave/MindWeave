# MindWeave Accessibility Guidelines

## Document Information
| Field | Value |
|-------|-------|
| Document ID | DS-008 |
| Version | 1.0.0 |
| Last Updated | 2024-12-29 |
| Owner | Product Design |
| Status | Active |

## Overview

MindWeave is committed to providing an accessible experience for all users. This document outlines the accessibility standards, guidelines, and implementation requirements to ensure WCAG 2.1 Level AA compliance across all platform interfaces.

---

## 1. Accessibility Standards

### 1.1 Compliance Target

```
┌─────────────────────────────────────────────────────────────────────┐
│                   WCAG 2.1 COMPLIANCE                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Target Level: AA (with AAA enhancements where practical)          │
│                                                                     │
│   POUR Principles:                                                  │
│                                                                     │
│   ┌─────────────────┐  ┌─────────────────┐                        │
│   │  PERCEIVABLE    │  │   OPERABLE      │                        │
│   │                 │  │                 │                        │
│   │  Information    │  │  All functions  │                        │
│   │  and UI must    │  │  available via  │                        │
│   │  be presentable │  │  keyboard and   │                        │
│   │  to all senses  │  │  other inputs   │                        │
│   └─────────────────┘  └─────────────────┘                        │
│                                                                     │
│   ┌─────────────────┐  ┌─────────────────┐                        │
│   │ UNDERSTANDABLE  │  │    ROBUST       │                        │
│   │                 │  │                 │                        │
│   │  Content and    │  │  Compatible     │                        │
│   │  operation must │  │  with current   │                        │
│   │  be clear and   │  │  and future     │                        │
│   │  predictable    │  │  technologies   │                        │
│   └─────────────────┘  └─────────────────┘                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Key Requirements

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 1.1.1 Non-text Content | A | All images have alt text |
| 1.3.1 Info and Relationships | A | Semantic HTML structure |
| 1.4.1 Use of Color | A | Color not sole indicator |
| 1.4.3 Contrast (Minimum) | AA | 4.5:1 for text |
| 1.4.11 Non-text Contrast | AA | 3:1 for UI components |
| 2.1.1 Keyboard | A | All functionality keyboard accessible |
| 2.4.3 Focus Order | A | Logical focus sequence |
| 2.4.7 Focus Visible | AA | Visible focus indicator |
| 4.1.2 Name, Role, Value | A | ARIA labels for custom components |

---

## 2. Color & Contrast

### 2.1 Contrast Requirements

```
┌─────────────────────────────────────────────────────────────────────┐
│                   CONTRAST REQUIREMENTS                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Text Contrast:                                                    │
│                                                                     │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │ Size              │ Weight    │ Minimum Ratio │ Level        │ │
│   ├──────────────────────────────────────────────────────────────┤ │
│   │ Normal (< 18px)   │ Regular   │ 4.5:1         │ AA           │ │
│   │ Normal (< 18px)   │ Bold      │ 4.5:1         │ AA           │ │
│   │ Large (≥ 18px)    │ Regular   │ 3:1           │ AA           │ │
│   │ Large (≥ 14px)    │ Bold      │ 3:1           │ AA           │ │
│   │ Any size          │ Any       │ 7:1           │ AAA          │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   Verified Color Combinations:                                      │
│                                                                     │
│   ✓ Slate 900 on White: 15.1:1 (exceeds AAA)                       │
│   ✓ Slate 700 on White: 8.2:1 (exceeds AAA)                        │
│   ✓ Slate 600 on White: 5.7:1 (passes AA)                          │
│   ✓ Indigo 600 on White: 5.0:1 (passes AA)                         │
│   ✓ White on Indigo 600: 5.0:1 (passes AA)                         │
│   ⚠ Slate 400 on White: 3.5:1 (fails for small text)               │
│                                                                     │
│   UI Component Contrast (3:1 minimum):                              │
│                                                                     │
│   ✓ Button borders                                                  │
│   ✓ Input field borders                                             │
│   ✓ Focus indicators                                                │
│   ✓ Icon buttons                                                    │
│   ✓ Chart elements                                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Color Independence

```
┌─────────────────────────────────────────────────────────────────────┐
│                   COLOR INDEPENDENCE                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Never use color as the only means of conveying information.       │
│                                                                     │
│   ✗ BAD: Status indicated by color only                            │
│   ┌───────────────────────────────────────────────────────────────┐│
│   │ ●  john@example.com                                           ││
│   │ ●  jane@example.com                                           ││
│   │ ●  bob@example.com                                            ││
│   └───────────────────────────────────────────────────────────────┘│
│   (Green/Red circles meaningless to colorblind users)              │
│                                                                     │
│   ✓ GOOD: Color + icon + text label                                │
│   ┌───────────────────────────────────────────────────────────────┐│
│   │ ✓ Active   john@example.com                                   ││
│   │ ✓ Active   jane@example.com                                   ││
│   │ ⏳ Pending bob@example.com                                     ││
│   └───────────────────────────────────────────────────────────────┘│
│   (Icon shape + label + color provides redundant information)       │
│                                                                     │
│   Status Indicators Must Have:                                      │
│   • Distinct icon shape                                             │
│   • Text label (visible or sr-only)                                 │
│   • Color as enhancement, not sole indicator                        │
│                                                                     │
│   Charts Must Have:                                                 │
│   • Patterns in addition to colors                                  │
│   • Text labels or legends                                          │
│   • Tooltips with values                                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Keyboard Navigation

### 3.1 Focus Management

```
┌─────────────────────────────────────────────────────────────────────┐
│                   FOCUS MANAGEMENT                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Focus Ring Style:                                                 │
│   ┌─────────────────────────────┐                                  │
│   │  ┌───────────────────────┐  │ ◄── 2px ring                     │
│   │  │                       │  │     Indigo 200 (#C7D2FE)         │
│   │  │      Component        │  │     offset: 2px                  │
│   │  │                       │  │                                  │
│   │  └───────────────────────┘  │                                  │
│   └─────────────────────────────┘                                  │
│                                                                     │
│   Focus Visibility Rules:                                           │
│   • ALWAYS visible when element is focused                          │
│   • Use :focus-visible for keyboard-only focus                      │
│   • Never use outline: none without replacement                     │
│   • Sufficient contrast against all backgrounds                     │
│                                                                     │
│   CSS Implementation:                                               │
│   .focusable:focus-visible {                                        │
│     outline: none;                                                  │
│     box-shadow: 0 0 0 2px white, 0 0 0 4px #C7D2FE;                │
│   }                                                                 │
│                                                                     │
│   Focus Order:                                                      │
│   • Follow visual/logical order (left→right, top→bottom)           │
│   • Tab through interactive elements sequentially                   │
│   • Skip non-interactive elements                                   │
│   • Respect DOM order; avoid tabindex > 0                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Keyboard Patterns

```
┌─────────────────────────────────────────────────────────────────────┐
│                   KEYBOARD PATTERNS                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   General Navigation:                                               │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │ Key         │ Action                                         │ │
│   ├──────────────────────────────────────────────────────────────┤ │
│   │ Tab         │ Move to next focusable element                 │ │
│   │ Shift+Tab   │ Move to previous focusable element             │ │
│   │ Enter       │ Activate button/link                           │ │
│   │ Space       │ Activate button, toggle checkbox               │ │
│   │ Escape      │ Close modal, cancel action                     │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   Component-Specific Patterns:                                      │
│                                                                     │
│   Dropdown/Select:                                                  │
│   • Enter/Space: Open dropdown                                      │
│   • Arrow Down/Up: Navigate options                                 │
│   • Enter: Select focused option                                    │
│   • Escape: Close without selection                                 │
│   • Type letter: Jump to matching option                            │
│                                                                     │
│   Tabs:                                                             │
│   • Arrow Left/Right: Navigate between tabs                         │
│   • Enter/Space: Activate tab (if manual activation)                │
│   • Tab: Move into tab panel content                                │
│   • Home/End: Jump to first/last tab                                │
│                                                                     │
│   Table:                                                            │
│   • Arrow keys: Navigate cells                                      │
│   • Enter: Open row detail                                          │
│   • Space: Toggle row selection                                     │
│                                                                     │
│   Modal:                                                            │
│   • Tab: Cycle through modal elements (trapped)                     │
│   • Escape: Close modal                                             │
│   • Focus moves to modal on open                                    │
│   • Focus returns to trigger on close                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.3 Skip Links

```
┌─────────────────────────────────────────────────────────────────────┐
│                   SKIP LINKS                                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Provide skip links to bypass repeated content:                    │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ [Skip to main content]  ◄── Visible on focus only           │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │ Header                                                       │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │ Navigation                                                   │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │                                                              │  │
│   │ Main Content  ◄── Skip link target (#main-content)          │  │
│   │                                                              │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   Implementation:                                                   │
│                                                                     │
│   <a href="#main-content" class="skip-link">                        │
│     Skip to main content                                            │
│   </a>                                                              │
│                                                                     │
│   .skip-link {                                                      │
│     position: absolute;                                             │
│     left: -9999px;                                                  │
│   }                                                                 │
│   .skip-link:focus {                                                │
│     position: fixed;                                                │
│     top: 8px;                                                       │
│     left: 8px;                                                      │
│     z-index: 100;                                                   │
│     background: white;                                              │
│     padding: 8px 16px;                                              │
│   }                                                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Screen Reader Support

### 4.1 Semantic HTML

```
┌─────────────────────────────────────────────────────────────────────┐
│                   SEMANTIC STRUCTURE                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Use semantic HTML elements:                                       │
│                                                                     │
│   ✓ GOOD                         ✗ BAD                             │
│   ─────────                      ─────────                          │
│   <header>                       <div class="header">               │
│   <nav>                          <div class="nav">                  │
│   <main>                         <div class="main">                 │
│   <article>                      <div class="article">              │
│   <section>                      <div class="section">              │
│   <aside>                        <div class="sidebar">              │
│   <footer>                       <div class="footer">               │
│   <h1>-<h6>                      <div class="heading">              │
│   <button>                       <div onclick="">                   │
│   <a href="">                    <span onclick="">                  │
│   <ul><li>                       <div class="list">                 │
│   <table>                        <div class="table">                │
│                                                                     │
│   Landmark Regions:                                                 │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ <header role="banner">                                       │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │ <nav role="navigation" aria-label="Main navigation">        │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │ <main role="main">                                           │  │
│   │   <section aria-labelledby="section-heading">                │  │
│   │     <h2 id="section-heading">Section Title</h2>              │  │
│   │   </section>                                                 │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 ARIA Patterns

```
┌─────────────────────────────────────────────────────────────────────┐
│                   ARIA IMPLEMENTATION                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Rule 1: Use semantic HTML first                                   │
│   Rule 2: Don't change native semantics                             │
│   Rule 3: All interactive elements must be keyboard accessible      │
│   Rule 4: Don't use role="presentation" on focusable elements       │
│   Rule 5: All interactive elements must have accessible names       │
│                                                                     │
│   Common ARIA Patterns:                                             │
│                                                                     │
│   Icon Button:                                                      │
│   <button aria-label="Delete item">                                 │
│     <TrashIcon aria-hidden="true" />                                │
│   </button>                                                         │
│                                                                     │
│   Expandable Section:                                               │
│   <button aria-expanded="false" aria-controls="panel-1">            │
│     Section Title                                                   │
│   </button>                                                         │
│   <div id="panel-1" hidden>Panel content</div>                      │
│                                                                     │
│   Modal Dialog:                                                     │
│   <div role="dialog" aria-modal="true" aria-labelledby="modal-title">│
│     <h2 id="modal-title">Modal Title</h2>                          │
│     ...                                                             │
│   </div>                                                            │
│                                                                     │
│   Live Region:                                                      │
│   <div aria-live="polite" aria-atomic="true">                       │
│     {statusMessage}  <!-- Announced when content changes -->        │
│   </div>                                                            │
│                                                                     │
│   Loading State:                                                    │
│   <button aria-busy="true" aria-disabled="true">                    │
│     <Spinner aria-hidden="true" /> Saving...                        │
│   </button>                                                         │
│                                                                     │
│   Tab Panel:                                                        │
│   <div role="tablist" aria-label="Team settings">                   │
│     <button role="tab" aria-selected="true" aria-controls="tab-1">  │
│       General                                                       │
│     </button>                                                       │
│     <button role="tab" aria-selected="false" aria-controls="tab-2"> │
│       Members                                                       │
│     </button>                                                       │
│   </div>                                                            │
│   <div role="tabpanel" id="tab-1">...</div>                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.3 Accessible Names

```
┌─────────────────────────────────────────────────────────────────────┐
│                   ACCESSIBLE NAMES                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Every interactive element needs an accessible name:               │
│                                                                     │
│   Method 1: Visible Label                                           │
│   <button>Save Changes</button>                                     │
│   ✓ Name: "Save Changes" (from content)                            │
│                                                                     │
│   Method 2: aria-label                                              │
│   <button aria-label="Close dialog">                                │
│     <XIcon />                                                       │
│   </button>                                                         │
│   ✓ Name: "Close dialog"                                           │
│                                                                     │
│   Method 3: aria-labelledby                                         │
│   <h2 id="section-title">Team Members</h2>                          │
│   <table aria-labelledby="section-title">...</table>                │
│   ✓ Name: "Team Members"                                           │
│                                                                     │
│   Method 4: Associated Label                                        │
│   <label for="email">Email Address</label>                          │
│   <input id="email" type="email" />                                 │
│   ✓ Name: "Email Address"                                          │
│                                                                     │
│   Priority Order:                                                   │
│   1. aria-labelledby                                                │
│   2. aria-label                                                     │
│   3. <label> element                                                │
│   4. title attribute                                                │
│   5. Content (for buttons, links)                                   │
│                                                                     │
│   Screen Reader Only Text:                                          │
│   .sr-only {                                                        │
│     position: absolute;                                             │
│     width: 1px;                                                     │
│     height: 1px;                                                    │
│     padding: 0;                                                     │
│     margin: -1px;                                                   │
│     overflow: hidden;                                               │
│     clip: rect(0, 0, 0, 0);                                         │
│     border: 0;                                                      │
│   }                                                                 │
│                                                                     │
│   <span class="sr-only">Status:</span>                              │
│   <span aria-hidden="true">●</span> Active                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 5. Forms & Inputs

### 5.1 Form Accessibility

```
┌─────────────────────────────────────────────────────────────────────┐
│                   ACCESSIBLE FORMS                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Complete Form Field:                                              │
│                                                                     │
│   <div class="form-field">                                          │
│     <label for="email">                                             │
│       Email Address                                                 │
│       <span class="required" aria-hidden="true">*</span>            │
│     </label>                                                        │
│     <input                                                          │
│       id="email"                                                    │
│       type="email"                                                  │
│       aria-required="true"                                          │
│       aria-describedby="email-help email-error"                     │
│       aria-invalid="false"                                          │
│     />                                                              │
│     <p id="email-help" class="helper-text">                         │
│       Enter your work email address                                 │
│     </p>                                                            │
│     <p id="email-error" class="error-text" role="alert" hidden>     │
│       Please enter a valid email address                            │
│     </p>                                                            │
│   </div>                                                            │
│                                                                     │
│   Error State:                                                      │
│   • Set aria-invalid="true" on input                                │
│   • Show error message (role="alert")                               │
│   • Move focus to first error on submit                             │
│   • Announce: "Error: Please enter a valid email address"           │
│                                                                     │
│   Required Fields:                                                  │
│   • Use aria-required="true"                                        │
│   • Visual indicator (asterisk)                                     │
│   • Legend explains: "* Required field"                             │
│                                                                     │
│   Fieldset for Groups:                                              │
│   <fieldset>                                                        │
│     <legend>Notification Preferences</legend>                       │
│     <label><input type="checkbox" /> Email</label>                  │
│     <label><input type="checkbox" /> SMS</label>                    │
│   </fieldset>                                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Error Handling

```
┌─────────────────────────────────────────────────────────────────────┐
│                   ERROR HANDLING                                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Form Submission Errors:                                           │
│                                                                     │
│   1. Show error summary at top of form:                             │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │ ⚠ Please fix the following errors:                          │  │
│   │                                                              │  │
│   │ • Email address is required                                  │  │
│   │ • Password must be at least 8 characters                     │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   role="alert" + focus moves here                                   │
│                                                                     │
│   2. Move focus to error summary or first error field               │
│                                                                     │
│   3. Inline errors remain visible:                                  │
│   Email Address *                                                   │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                                                              │  │
│   └─────────────────────────────────────────────────────────────┘  │
│   ⚠ Email address is required                                       │
│                                                                     │
│   Live Validation:                                                  │
│   • Validate on blur (not on every keystroke)                       │
│   • Clear errors as user fixes them                                 │
│   • Use aria-live="polite" for non-critical updates                 │
│   • Use role="alert" for form submission errors                     │
│                                                                     │
│   Success Feedback:                                                 │
│   • Announce: "Form submitted successfully"                         │
│   • Use aria-live="polite"                                          │
│   • Redirect or update UI appropriately                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6. Dynamic Content

### 6.1 Live Regions

```
┌─────────────────────────────────────────────────────────────────────┐
│                   LIVE REGIONS                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   aria-live values:                                                 │
│                                                                     │
│   "off"      │ No announcements (default)                           │
│   "polite"   │ Announce when user is idle                           │
│   "assertive"│ Interrupt and announce immediately                   │
│                                                                     │
│   Use Cases:                                                        │
│                                                                     │
│   Toast Notifications (polite):                                     │
│   <div aria-live="polite" aria-atomic="true">                       │
│     {toastMessage}                                                  │
│   </div>                                                            │
│                                                                     │
│   Error Alerts (assertive):                                         │
│   <div role="alert">                                                │
│     Session expired. Please log in again.                           │
│   </div>                                                            │
│   (role="alert" implies aria-live="assertive")                      │
│                                                                     │
│   Loading Status (polite):                                          │
│   <div aria-live="polite">                                          │
│     {isLoading ? "Loading data..." : "Data loaded"}                 │
│   </div>                                                            │
│                                                                     │
│   Search Results (polite):                                          │
│   <div aria-live="polite">                                          │
│     {results.length} results found for "{query}"                    │
│   </div>                                                            │
│                                                                     │
│   Best Practices:                                                   │
│   • Use sparingly to avoid announcement fatigue                     │
│   • Prefer "polite" over "assertive"                                │
│   • Keep messages concise                                           │
│   • Test with actual screen readers                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 Focus Management

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DYNAMIC FOCUS MANAGEMENT                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   When content changes dynamically, manage focus appropriately:     │
│                                                                     │
│   Modal Opens:                                                      │
│   1. Save reference to trigger element                              │
│   2. Move focus to modal (first focusable or title)                 │
│   3. Trap focus within modal                                        │
│   4. On close, return focus to trigger                              │
│                                                                     │
│   Modal Closes:                                                     │
│   const triggerRef = useRef();                                      │
│   const openModal = () => {                                         │
│     triggerRef.current = document.activeElement;                    │
│     setIsOpen(true);                                                │
│   };                                                                │
│   const closeModal = () => {                                        │
│     setIsOpen(false);                                               │
│     triggerRef.current?.focus();                                    │
│   };                                                                │
│                                                                     │
│   Item Deleted:                                                     │
│   • Move focus to next item in list                                 │
│   • If last item, move to previous item                             │
│   • If list empty, move to list container or add button             │
│                                                                     │
│   Page Navigation:                                                  │
│   • Move focus to main content area                                 │
│   • Or to page title/h1                                             │
│   • Announce page change via live region                            │
│                                                                     │
│   Infinite Scroll:                                                  │
│   • Announce "Loading more items..."                                │
│   • Keep focus position stable                                      │
│   • Announce "5 more items loaded"                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. Touch & Mobile

### 7.1 Touch Target Size

```
┌─────────────────────────────────────────────────────────────────────┐
│                   TOUCH TARGETS                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Minimum Touch Target: 44 × 44 pixels (WCAG 2.1 AAA)               │
│   Recommended: 48 × 48 pixels                                       │
│                                                                     │
│   Visual vs Touch Target:                                           │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │                                                               │ │
│   │           ┌────────┐                                          │ │
│   │           │  Icon  │  ◄── Visual: 24px                        │ │
│   │           │  24px  │                                          │ │
│   │           └────────┘                                          │ │
│   │                                                               │ │
│   │  ┌────────────────────┐                                       │ │
│   │  │                    │  ◄── Touch target: 48px               │ │
│   │  │    Touch Area      │                                       │ │
│   │  │       48px         │                                       │ │
│   │  │                    │                                       │ │
│   │  └────────────────────┘                                       │ │
│   │                                                               │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│   Implementation:                                                   │
│   .icon-button {                                                    │
│     min-width: 48px;                                                │
│     min-height: 48px;                                               │
│     display: flex;                                                  │
│     align-items: center;                                            │
│     justify-content: center;                                        │
│   }                                                                 │
│                                                                     │
│   Spacing Between Targets:                                          │
│   • Minimum 8px between touch targets                               │
│   • Prevents accidental taps                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 Mobile Considerations

```
┌─────────────────────────────────────────────────────────────────────┐
│                   MOBILE ACCESSIBILITY                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Orientation:                                                      │
│   • Support both portrait and landscape                             │
│   • Don't lock orientation unless essential                         │
│   • Content reflows appropriately                                   │
│                                                                     │
│   Gestures:                                                         │
│   • Provide alternatives to complex gestures                        │
│   • Swipe actions need button alternatives                          │
│   • Pinch-to-zoom: Don't disable user zoom                          │
│                                                                     │
│   <meta name="viewport"                                             │
│     content="width=device-width, initial-scale=1,                   │
│              maximum-scale=5">  <!-- Allow zoom up to 500% -->      │
│                                                                     │
│   Screen Reader Support:                                            │
│   • VoiceOver (iOS) compatible                                      │
│   • TalkBack (Android) compatible                                   │
│   • Test with actual devices                                        │
│                                                                     │
│   Touch Gestures vs Alternatives:                                   │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │ Gesture            │ Alternative                             │ │
│   ├──────────────────────────────────────────────────────────────┤ │
│   │ Swipe to delete    │ Delete button in menu                   │ │
│   │ Pull to refresh    │ Refresh button                          │ │
│   │ Long press         │ Menu button                             │ │
│   │ Pinch zoom         │ Zoom controls (+/-)                     │ │
│   │ Double tap         │ Single tap + button                     │ │
│   └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8. Testing Guidelines

### 8.1 Manual Testing Checklist

```
┌─────────────────────────────────────────────────────────────────────┐
│                   ACCESSIBILITY CHECKLIST                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Keyboard Testing:                                                 │
│   □ All interactive elements reachable via Tab                      │
│   □ Focus order is logical (left→right, top→bottom)                │
│   □ Focus indicator clearly visible                                 │
│   □ Modals trap focus                                               │
│   □ Escape closes modals/dropdowns                                  │
│   □ Skip link works                                                 │
│                                                                     │
│   Screen Reader Testing:                                            │
│   □ Page title is descriptive                                       │
│   □ Headings form logical hierarchy                                 │
│   □ Images have appropriate alt text                                │
│   □ Form labels are announced                                       │
│   □ Errors are announced                                            │
│   □ Dynamic content is announced                                    │
│   □ Buttons/links have accessible names                             │
│                                                                     │
│   Visual Testing:                                                   │
│   □ Works at 200% zoom                                              │
│   □ Color contrast passes                                           │
│   □ No reliance on color alone                                      │
│   □ Text resizes without breaking layout                            │
│                                                                     │
│   Motion Testing:                                                   │
│   □ Respects prefers-reduced-motion                                 │
│   □ Animations can be paused                                        │
│   □ No content flashes more than 3 times/sec                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2 Tools & Resources

| Tool | Purpose |
|------|---------|
| axe DevTools | Automated accessibility testing |
| WAVE | Visual accessibility evaluation |
| Lighthouse | Accessibility audit in Chrome |
| NVDA | Free screen reader (Windows) |
| VoiceOver | Built-in screen reader (macOS/iOS) |
| TalkBack | Built-in screen reader (Android) |
| Color Contrast Analyzer | Check contrast ratios |
| Keyboard Navigation | Tab through entire page |

---

## Related Documents

- [DESIGN-SYSTEM.md](./DESIGN-SYSTEM.md) - Design system overview
- [COLOR-PALETTE.md](./COLOR-PALETTE.md) - Color specifications
- [COMPONENT-LIBRARY.md](./COMPONENT-LIBRARY.md) - Component specifications

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-12-29 | Product Design | Initial accessibility guidelines |

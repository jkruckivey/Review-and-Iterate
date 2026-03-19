# Ivey Online Widget Style Guide

**Created:** 2026-03-10
**Status:** Draft — based on audit of all 6 courses
**Purpose:** Define a single widget design standard for all Ivey Online courses on Uplimit

---

## Current State: Three Design Systems

An audit of widgets across all 6 courses found three independently-developed design systems. This guide proposes a unified standard based on the strongest elements of each.

### System 1: "Geist Neutral" (Analytics/Excel, Sports Marketing W3+)
- Font: Geist (Google Fonts)
- Neutral gray scale `#fafafa` to `#171717`
- Sage green accent `#6b9085`
- Dark buttons `#171717`
- Success `#22c55e` / Error `#ef4444`
- CSS custom properties throughout
- Strong accessibility (ARIA live, sr-only, keyboard nav)

### System 2: "Ivey Brand" (Accounting)
- Font: System stack (Segoe UI, Roboto, etc.)
- Ivey green `#005951`, bright green `#A4B544`, purple `#5B2C6F`, turquoise `#0093A9`
- Gradient buttons (green-to-turquoise)
- Success `#A4B544` (lime) / Error `#5B2C6F` (purple)
- Best accessibility: `prefers-reduced-motion`, skip links, extensive ARIA
- Issue: purple-for-incorrect breaks red/green convention

### System 3: "Teal Pastels" (AI Prototyping, AI Transformation partial)
- Font: Segoe UI / Tahoma / Verdana
- Dark teal `#034638`, pastels `#c0d1cd`, `#bfe5e7`, `#d5cae0`
- Cream backgrounds `#faf9f5`
- Success `#2d6a4f` / Error `#8b2020`
- Step-based interaction patterns
- Moderate accessibility

### Outliers
- **Financial Analysis:** Inter font, hybrid Ivey palette (`#c0d1cd`, `#d5cae0`, `#bfe5e7`), status colors `#48825d`/`#c45a5a`, weakest accessibility
- **Sports Marketing W1:** Nashville Predators brand colors (`#ffb81c` gold, `#041e42` navy) — case-specific, may be intentional
- **AI Transformation:** Uses 3 different fonts across its own widgets (Geist W2, System W3, Inter W5)

---

## Proposed Standard

Based on the audit, the recommendation is to converge on a system that takes the **Geist Neutral foundation** (cleanest, most consistent) and incorporates the **best accessibility practices from Accounting** and the **pastel accent palette** that appears across multiple systems.

### Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Primary | `Geist` via Google Fonts | 400 (body), 500 (labels), 600 (headings), 700 (emphasis) | Base: `1rem` (16px) |
| Fallback | `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | | |
| Monospace (code/formulas) | `Consolas, 'Courier New', monospace` | 400 | `0.9rem` |
| Excel simulation | `Calibri, sans-serif` | — | Context-dependent |

**Rationale:** Geist is already used in 3 of 6 courses and is the Uplimit platform's preferred font. System fonts are acceptable as fallback but should not be the primary choice.

### Color Palette

#### Neutral Scale (from Geist Neutral system — already shared across courses)
```
--color-neutral-50:  #fafafa
--color-neutral-100: #f5f5f5
--color-neutral-200: #e5e5e5
--color-neutral-300: #d4d4d4
--color-neutral-400: #a3a3a3
--color-neutral-500: #737373
--color-neutral-600: #525252
--color-neutral-700: #404040
--color-neutral-800: #262626
--color-neutral-900: #171717
```

#### Accent Colors (shared across multiple systems already)
```
--color-accent:       #6b9085  (sage green — primary interactive)
--color-accent-light: #c0d1cd  (light sage — backgrounds, secondary)
--color-green:        #c0d1cd  (same as accent-light)
--color-purple:       #d5cae0  (muted purple — categories, highlights)
--color-turquoise:    #bfe5e7  (light cyan — insights, callouts)
--color-sand:         #f0ede0  (warm beige — scenario boxes)
```

#### Semantic Colors
```
--color-success:      #22c55e  (correct answers, positive states)
--color-success-light:#dcfce7  (correct answer backgrounds)
--color-error:        #ef4444  (incorrect answers, negative states)
--color-error-light:  #fee2e2  (incorrect answer backgrounds)
--color-warning:      #f59e0b  (hints, cautions)
--color-warning-light:#fef3c7  (warning backgrounds)
```

**Important:** Correct = green, Incorrect = red. Never use purple for error states. This aligns with universal UX convention and all courses except Accounting already follow it.

### Buttons

#### Primary Button
```css
.btn-primary {
    background: var(--color-neutral-800);   /* #262626 */
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    font-family: 'Geist', -apple-system, sans-serif;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s ease;
}
.btn-primary:hover {
    background: var(--color-neutral-700);   /* #404040 */
}
.btn-primary:focus-visible {
    outline: 2px solid var(--color-neutral-900);
    outline-offset: 2px;
}
.btn-primary:disabled {
    background: var(--color-neutral-400);
    opacity: 0.6;
    cursor: not-allowed;
}
```

#### Secondary Button
```css
.btn-secondary {
    background: var(--color-neutral-100);
    color: var(--color-neutral-800);
    border: 1px solid var(--color-neutral-300);
    /* Same padding, radius, font as primary */
}
.btn-secondary:hover {
    background: var(--color-neutral-200);
}
```

#### Preset/Scenario Button
```css
.btn-preset {
    background: white;
    color: var(--color-neutral-700);
    border: 1px solid var(--color-neutral-300);
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-size: 0.875rem;
    font-weight: 500;
}
.btn-preset:hover {
    background: var(--color-neutral-100);
    border-color: var(--color-neutral-400);
}
.btn-preset.active {
    background: var(--color-accent-light);
    border-color: var(--color-accent);
    color: var(--color-neutral-800);
}
```

**No gradient buttons.** Solid colors are cleaner and more consistent. The Accounting gradient style should be migrated.

### Layout

| Property | Value |
|----------|-------|
| Container max-width | `800px` (standard), `900px` (calculators/simulators), `1200px` (dashboards) |
| Container margin | `0 auto` |
| Body padding | `24px` |
| Card padding | `24px` |
| Card border-radius | `8px` (standard), `12px` (large cards) |
| Card border | `1px solid var(--color-neutral-200)` |
| Card shadow | `0 1px 3px rgba(0, 0, 0, 0.08)` |
| Grid gap | `1rem` (tight), `1.5rem` (standard), `2rem` (spacious) |
| Primary breakpoint | `768px` |

### Feedback States

#### Correct Answer
```css
.feedback-correct {
    background: var(--color-success-light);   /* #dcfce7 */
    border: 1px solid var(--color-success);   /* #22c55e */
    color: var(--color-neutral-900);
    padding: 12px 16px;
    border-radius: 8px;
}
```

#### Incorrect Answer
```css
.feedback-incorrect {
    background: var(--color-error-light);     /* #fee2e2 */
    border: 1px solid var(--color-error);     /* #ef4444 */
    color: var(--color-neutral-900);
    padding: 12px 16px;
    border-radius: 8px;
}
```

#### Hint / Warning
```css
.feedback-hint {
    background: var(--color-warning-light);   /* #fef3c7 */
    border: 1px solid var(--color-warning);   /* #f59e0b */
    color: var(--color-neutral-900);
    padding: 12px 16px;
    border-radius: 8px;
}
```

### Accessibility Requirements (WCAG 2.2 AA)

All widgets must include:

#### Required
- `aria-live="polite"` region for dynamic feedback announcements
- `role` attributes on interactive elements (`button`, `radiogroup`, `grid`, etc.)
- `aria-label` or `aria-labelledby` on all interactive elements
- `aria-expanded` on collapsible sections
- Keyboard navigation: Tab, Enter, Space, Arrow keys as appropriate
- Focus outlines: `2px solid var(--color-neutral-900)` with `outline-offset: 2px`
- `.sr-only` class for screen-reader-only content:
  ```css
  .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      border: 0;
  }
  ```

#### Required (from Accounting — best practice)
- `@media (prefers-reduced-motion: reduce)` — disable transitions and animations
- Color is never the sole indicator of state — always pair with text and/or icons

#### Recommended
- Skip link for complex widgets
- `@media (prefers-contrast: high)` support
- Print stylesheet where relevant

### Code Structure

| Aspect | Standard |
|--------|----------|
| Framework | Vanilla JavaScript (no React, Vue, etc.) |
| Styling | Inline `<style>` block with CSS custom properties |
| External dependencies | Chart.js via CDN when needed; nothing else |
| Data | Embedded in JavaScript arrays/objects |
| Event handling | `addEventListener()` preferred over inline `onclick` |
| State management | Simple object or DOM queries (no framework state) |
| Mobile | Responsive, primary breakpoint at `768px` |

---

## Course-by-Course Gap Analysis

What each course needs to conform to this standard:

### Fundamentals of Analytics and Excel
**Gap: Small** — closest to the standard already
- Add `prefers-reduced-motion` media query
- Verify all widgets have consistent `2px` focus outlines (some use `3px`)

### Business of Sports Marketing
**Gap: Small to Medium**
- W1 Nashville quiz uses entirely different color system (Predators brand) — may be intentional for case context, but should be documented as an exception
- W3+ already uses Geist Neutral system
- Add `prefers-reduced-motion`
- Standardize focus outline width (2px vs 3px inconsistency)

### Fundamentals of Financial Analysis
**Gap: Medium**
- Change font from Inter to Geist
- Replace status colors (`#48825d`/`#c45a5a`) with standard success/error
- Add ARIA live regions (currently missing)
- Add keyboard navigation to flipcard widgets (currently click-only)
- Add `.sr-only` class
- Add `prefers-reduced-motion`

### Fundamentals of Accounting
**Gap: Medium**
- Change font from system stack to Geist
- Replace gradient buttons with solid dark buttons
- Replace purple-for-incorrect with red (`#ef4444` / `#fee2e2`)
- Replace Ivey brand greens (`#005951`) with neutral palette
- Already has strong accessibility — preserve `prefers-reduced-motion`, skip links, extensive ARIA

### Igniting AI Transformation
**Gap: Medium to Large**
- Unify font: currently uses Geist (W2), system (W3), Inter (W5) — standardize to Geist
- W3 widgets use `#034638` teal system — migrate to neutral palette with sage accent
- W5 stakeholder map uses Inter and blue focus color (`#2563eb`) — align with standard
- Accessibility is generally good but inconsistent across weeks

### AI Prototyping for Business Innovation
**Gap: Large**
- Only 6 widgets total, but 4 different font stacks across them
- W1 learning outcomes widget already close (uses Geist + sage)
- W3-W5 widgets use Segoe UI + teal pastels — full migration needed
- Replace `#034638` primary with neutral-800/900 + sage accent
- Standardize button styles (currently varies per widget)
- Strengthen accessibility: add ARIA live regions, sr-only class consistently

---

## Implementation Priority

| Priority | Action | Effort |
|----------|--------|--------|
| 1 | Fix Accounting purple-for-incorrect | Low — color swap |
| 2 | Add `prefers-reduced-motion` to Analytics, Sports Mktg, Financial Analysis, AI Prototyping | Low — CSS addition |
| 3 | Add keyboard nav + ARIA to Financial Analysis flipcards | Medium |
| 4 | Standardize fonts to Geist across all courses | Medium — find-and-replace in CSS |
| 5 | Align color palettes to unified standard | Medium-High — per-widget review |
| 6 | Standardize button styles | Medium — per-widget update |
| 7 | Full accessibility pass on AI Prototyping widgets | Medium |
| 8 | Unify AI Transformation widgets (3 different systems in one course) | High |

---

## Exceptions

Some design deviations may be intentional and should be documented rather than "fixed":

- **Excel simulation widgets** (Analytics course) legitimately use Calibri font and Excel-brand green `#217346` to simulate the Excel UI. This is a pedagogical choice, not a branding inconsistency.
- **Case-specific branding** (Sports Marketing Nashville quiz) uses Predators team colors. If this is a deliberate design decision to immerse students in the case, document it as an exception.
- **Chart.js** integration may impose its own styling. Chart colors should still draw from the standard palette where possible.

# Fundamentals of Strategy — Storyboard Reconciliation
**Date:** 2026-03-13
**Sources compared:**
1. **Live platform** — Uplimit GraphQL API extraction (session `session_cmkwq0y4300tr1e7d0ze148b7`)
2. **Widget inventory** — `WIDGET-INVENTORY.md` (last updated 2025-12-30, lists 46 widgets)
3. **Widget files on disk** — `widgets/` folder (53 .html files + index.html)
4. **Storyboard audit** — `STORYBOARD-AUDIT-SUMMARY.md` (2025-01-19, modules 0-2 only)

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Widgets on live platform | **20** |
| Widgets in inventory doc | **46** |
| Widget files on disk | **53** (excl. index.html) |
| Widgets on disk but NOT live | **33** |
| Widgets live but NOT on disk | **0** |
| Widget inventory doc discrepancies | **8** |

**The headline:** Only **20 of 53 built widgets** (38%) are actually live on the platform. 33 widgets were built and exist as files but were never uploaded — or were removed. The widget inventory document lists 46 but is also out of date (counts don't match the 53 on disk or the 20 live).

---

## Three-Way Widget Comparison

### Widgets LIVE on Platform (20)

| # | Filename | On Disk? | In Inventory? | Module (Platform) | Section (Platform) |
|---|----------|----------|---------------|--------------------|--------------------|
| 1 | `learning-outcomes-map.html` | YES | YES (M0) | Welcome | Course Overview |
| 2 | `strategy-concept-map.html` | YES | YES (M0) | Welcome | Course Overview |
| 3 | `learning-outcomes-module-1.html` | YES | YES (M1) | Intro to Goal Setting | From Framework to Application |
| 4 | `learning-outcomes-module-2.html` | YES | YES (M2) | Intro to Value Proposition | Overview and Learning Outcomes |
| 5 | `position-metrics.html` | YES | YES (M2) | Intro to Value Proposition | Productivity Frontier Overview |
| 6 | `mid-market-squeeze.html` | YES | YES (M2) | Position Risks and Tradeoffs | Risk Return Overview |
| 7 | `position-risk-return-calculator.html` | YES | YES (M2) | Practice and Application | Position Risk-Return Calculator |
| 8 | `learning-outcomes-module-3.html` | YES | YES (M3) | Intro to Customer Connection | Overview and Learning Outcomes |
| 9 | `learning-outcomes-module-4.html` | YES | YES (M4) | Intro to Competitive Differentiation | Overview and Learning Outcomes |
| 10 | `differentiation-analyzer.html` | YES | YES (M4) | Practice & Application | Differentiation Analyzer |
| 11 | `learning-outcomes-module-5.html` | YES | YES (M5) | Introduction to Value Chain | Overview and Learning Outcomes |
| 12 | `learning-outcomes-module-6.html` | YES | YES (M6) | Introduction to Create Value | Overview and Learning Outcomes |
| 13 | `value-creation-analyzer.html` | YES | YES (M6) | Practice and Application | Value Creation Analyzer |
| 14 | `learning-outcomes-module-7.html` | YES | YES (M7) | Introduction to Capture Value | Overview and Learning Outcomes |
| 15 | `revenue-margin-explorer.html` | NO | NO | Pricing and Margins | How Margins Build Value |
| 16 | `learning-outcomes-module-8.html` | YES | NO* | Intro to Persistence and Change | Overview and Learning Outcomes |
| 17 | `learning-outcomes-module-9.html` | YES | NO* | Overview and Learning Outcomes | Overview and Learning Outcomes |
| 18 | `learning-outcomes-module-10.html` | YES | NO* | Intro to the Ends of Strategy | Overview and Learning Outcomes |
| 19 | `strategy-integration-explorer.html` | NO | NO | Final Steps | Strategy Integration Explorer |
| 20 | `strategy-final-assessment.html` | NO | NO | Final Steps | Final Course Quiz |

**\*** The inventory uses different filenames for M8/M9: `learning-outcomes-persistence-change.html` and `learning-outcomes-wrap-up.html` — but the platform has `learning-outcomes-module-8.html` and `learning-outcomes-module-9.html`. The inventory also doesn't list a Module 10 learning outcomes widget at all.

**Key finding:** 3 widgets are live on the platform (`revenue-margin-explorer.html`, `strategy-integration-explorer.html`, `strategy-final-assessment.html`) that do NOT exist in the local `widgets/` folder. These were likely built and uploaded directly to the platform without being saved to the source repository.

---

### Widgets on Disk but NOT Live (33)

These widget files exist in the `widgets/` folder but are not embedded on the live platform:

#### Module 0 (1 widget not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `course-roadmap.html` | YES | Listed in M0 inventory but not on platform |

#### Module 1 (9 widgets not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `five-forces-analyzer.html` | YES | Interactive Five Forces tool — built but not deployed |
| `five-forces-identifier.html` | YES | Practice tool — built but not deployed |
| `industry-performance-explorer.html` | YES | Data visualization — built but not deployed |
| `industry-structure-deep-dive.html` | YES | Detailed analysis — built but not deployed |
| `goal-reality-check.html` | YES | Goal plausibility tool — built but not deployed |
| `rivalry-dimensions.html` | YES | Rivalry explorer — built but not deployed |
| `substitutes-framework.html` | YES | Substitutes analysis — built but not deployed |
| `knowledge-check-industry-performance.html` | YES | Quiz — built but not deployed |
| `knowledge-check-five-forces-identification.html` | YES | Quiz — built but not deployed |

#### Module 2 (7 widgets not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `productivity-frontier.html` | YES | Interactive frontier — built but not deployed |
| `industry-position-plotter.html` | YES | Position plotting tool — built but not deployed |
| `strategic-position-matcher.html` | YES | Matching exercise — built but not deployed |
| `real-company-position-analyzer.html` | YES | Real company analysis — built but not deployed |
| `knowledge-check-frontier-concept.html` | YES | Quiz — built but not deployed |
| `knowledge-check-three-positions.html` | YES | Quiz — built but not deployed |
| `part-3-knowledge-check.html` | YES | Comprehensive assessment — built but not deployed |

#### Module 3 (4 widgets not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `jobs-to-be-done.html` | YES | JTBD explorer — built but not deployed |
| `jobs-discovery-workshop.html` | YES | Workshop — built but not deployed |
| `jtbd-research-workshop.html` | YES | Research methods — built but not deployed |
| `knowledge-check-customer-connection.html` | YES | Quiz — built but not deployed |

#### Module 4 (2 widgets not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `performance-dimensions-explorer.html` | YES | 4 dimensions explorer — built but not deployed |
| `strategic-positioning-integrator.html` | YES | Integration tool — built but not deployed |

#### Module 5 (1 widget not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `value-chain-analyzer.html` | YES | Make vs. buy tool — built but not deployed |

#### Module 7 (1 widget not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `profitability-driver-analyzer.html` | YES | Revenue vs. cost — built but not deployed |

#### Module 8 (1 widget not live)
| Filename | In Inventory? | Notes |
|----------|---------------|-------|
| `strategic-decision-analyzer.html` | YES | Drift vs. adaptation — built but not deployed |

#### Not in inventory at all (7 widgets on disk, not live, not inventoried)
| Filename | Notes |
|----------|-------|
| `complete-framework-summary.html` | Variant of complete-framework-analyzer? |
| `correlation-vs-causation-detective.html` | Listed in M3 inventory but also exists as section name on platform (text-only?) |
| `part-2-knowledge-check.html` | M1 comprehensive assessment |
| `revenue-vs-cost-distribution.html` | M7 visualization |
| `roa-decomposition-chart.html` | Financial analysis chart |
| `southwest-airlines-timeline.html` | M10 case study visual |
| `value-creation-matrix.html` | M6 matrix tool |
| `vertical-structure-diagram.html` | M5 value chain visual |
| `wrigley-weis-comic.html` | M7 case illustration |

*Note: `correlation-vs-causation-detective.html` IS in the M3 inventory. Corrected count: 8 not in inventory.*

---

## Widget Inventory Document Issues

The `WIDGET-INVENTORY.md` (dated 2025-12-30) has these problems:

1. **Count mismatch**: Header says 46 widgets, summary table totals 45, actual disk has 53 files (excl. index)
2. **Missing module 10**: No entry for Module 10 (Ends of Strategy) — but `learning-outcomes-module-10.html` exists on disk AND is live
3. **Wrong filenames for M8**: Lists `learning-outcomes-persistence-change.html` — platform uses `learning-outcomes-module-8.html`
4. **Wrong filenames for M9**: Lists `learning-outcomes-wrap-up.html` — platform uses `learning-outcomes-module-9.html`; lists `complete-framework-analyzer.html` as M9 — platform doesn't have this live
5. **Module numbering mismatch**: Inventory uses M0-M9 (10 modules); platform has 11 weeks with "Persistence and Change" (M8) and "Limits: Change" (M9) as separate weeks, plus "The Ends of Strategy" (M10) and "Course Wrap-Up" (M11)
6. **Several on-disk widgets not listed**: `complete-framework-summary.html`, `revenue-vs-cost-distribution.html`, `roa-decomposition-chart.html`, `southwest-airlines-timeline.html`, `value-creation-matrix.html`, `vertical-structure-diagram.html`, `wrigley-weis-comic.html`
7. **Three live widgets not on disk**: `revenue-margin-explorer.html`, `strategy-integration-explorer.html`, `strategy-final-assessment.html` are on the platform but not in the local widgets folder

---

## Module Numbering: Storyboard vs Platform

The storyboard uses a 0-10 module numbering, but the platform organizes content into 12 "weeks." Here's the mapping:

| Storyboard Module | Platform Week | Notes |
|--------------------|---------------|-------|
| Module 0: Introduction | Introduction | Match |
| Module 1: Goal Setting | Goal Setting Through Industry Analysis | Match |
| Module 2: Industry Position | Value Proposition: Industry Position | Match |
| Module 3: Customer Connection | Customer Connection | Match |
| Module 4: Competitive Differentiation | Competitive Differentiation | Match |
| Module 5: Value Chain | Implementation: Value Chain | Match (added "Implementation:" prefix) |
| Module 6: Create Value | Implementation: Create Value | Match (added "Implementation:" prefix) |
| Module 7: Capture Value | Implementation: Capture Value | Match (added "Implementation:" prefix) |
| Module 8: Persistence | Persistence and Change | Match |
| Module 9: Change | Limits: Change | Different name |
| Module 10: Ends of Strategy | The Ends of Strategy | Match |
| (not in storyboard) | Course Wrap-Up | Platform-only week |

---

## Platform Issues Found

1. **"Key Takeways" typo** — Misspelled in 9 of 11 weeks (should be "Key Takeaways"). Only Week 10 ("Key Takeaways") and Week 12 (no key takeaways section) are correct.

2. **Caption download casing** — Inconsistent capitalization: "Download Captions" vs "Download captions" across sections.

3. **Module/Section name duplication** — Week 10 has a module named "Overview and Learning Outcomes" containing a section also named "Overview and Learning Outcomes."

4. **Extra whitespace in section names** — Leading/trailing spaces in several section names (e.g., " Canary Medical Value Chain Decisions ").

5. **Missing `course-roadmap.html` widget** — Listed in inventory, exists on disk, but not embedded on the live platform. The Course Overview section uses `learning-outcomes-map.html` and `strategy-concept-map.html` but no roadmap.

---

## Storyboard Audit Gap

The `STORYBOARD-AUDIT-SUMMARY.md` was written 2025-01-19 and only covers Modules 0, 1, and 2. It identifies substantial text-heaviness issues and recommends 50-60 hours of visual enhancement work. **Modules 3-10 have never been formally audited.** Given that modules 3-10 have significantly fewer widgets deployed (most not uploaded), the same text-heaviness pattern likely persists or worsens.

---

## Recommendations

### Immediate Actions (High Priority)

1. **Upload missing widgets** — 33 widgets are built and sitting on disk. Determine which should go live and deploy them. Prioritize:
   - All knowledge checks (7 quizzes)
   - Interactive analyzers for M1 (Five Forces tools) and M2 (Frontier tools)
   - M3 JTBD widgets

2. **Recover 3 platform-only widgets** — `revenue-margin-explorer.html`, `strategy-integration-explorer.html`, and `strategy-final-assessment.html` exist on the platform but not in source. Download and save to `widgets/` folder.

3. **Fix "Key Takeways" typo** — 9 occurrences across the live platform.

4. **Fix whitespace in section names** — Clean up leading/trailing spaces.

### Documentation Updates (Medium Priority)

5. **Update WIDGET-INVENTORY.md** — Correct counts, add Module 10, fix M8/M9 filenames, add 8 unlisted widgets.

6. **Complete storyboard audit** — Modules 3-10 have never been audited. Extend the audit from `STORYBOARD-AUDIT-SUMMARY.md` to cover the full course.

7. **Reconcile module numbering** — Document the storyboard M0-M10 ↔ platform Week 1-12 mapping so future updates don't create confusion.

### Source Control (Lower Priority)

8. **Standardize widget filenames** — Decide whether M8/M9 learning outcomes should be `learning-outcomes-module-{n}.html` (platform convention) or `learning-outcomes-{topic}.html` (inventory convention). Apply consistently.

9. **Add module folder structure** — The inventory references per-module widget folders (`modules/module-{n}/widgets/`) but all widgets are actually in one flat `widgets/` directory.

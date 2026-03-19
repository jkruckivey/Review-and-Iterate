# Ivey Online Course Review & Iteration Process

**Created:** 2026-03-10
**Status:** Phase 1 — Post-Mortems in Progress

---

## Purpose

These courses launched in a crunch. This process exists to:
1. Deep-dive each course as a post-mortem — reviewing every deliverable
2. Surface consistency issues and quality gaps across courses
3. Codify findings into standards and a style guide
4. Embed the review process into future course development so these problems don't repeat

---

## Course Inventory

Six courses on the Uplimit platform. Three self-paced (SP), three cohort (CB).

### Self-Paced Courses

| Course | Code | Files | Primary Format | Storyboard Style | Organization |
|--------|------|-------|----------------|------------------|--------------|
| Fundamentals of Analytics and Excel | IO-SP-Jan7 | 460 | Markdown | `.md` per module (M0-M8) | Clean |
| Fundamentals of Financial Analysis | IO-SP-Jan7 | 735 | DOCX | `.docx` monolithic | Moderate — graphics duplication |
| Fundamentals of Accounting | IO-SP-Jan7 | 323 | HTML + PDF pairs | `.docx` monolithic | Duplicated — central + per-module |

### Cohort Courses

| Course | Code | Files | Primary Format | Storyboard Style | Organization |
|--------|------|-------|----------------|------------------|--------------|
| Igniting AI Transformation | IO-CB-Apr1 | 907 | HTML → Markdown | Mixed across weeks | Messy — format transitions, scattered Week 3 |
| Business of Sports Marketing | IO-CB-Jan27 | 455 | Markdown | `.md` per module (8-module pattern) | Mostly clean — Week 1 bloat, temp files |
| AI Prototyping for Business Innovation | IO-CB-Jan27 | 676 | DOCX | `.docx` scattered | Fragmented — 3 content buckets |

### Cross-Course Observations

- No standard folder structure across courses
- Courses built with Claude Code tooling (Analytics, Sports Marketing) are more consistently structured
- Courses with heavier SME/external contributor involvement tend to be messier
- Self-paced courses trend toward monolithic storyboard docs; cohort courses have per-module files
- Version control is the universal problem — old files, duplicates, "which is current?" confusion everywhere
- Deprecated content never gets cleaned up

---

## Review Categories

Each course post-mortem covers all of these areas. The review is holistic — consistency can only be assessed by looking at everything together.

### 1. Course Videos
- HeyGen avatar quality (appearance, delivery, glitches)
- Graphics/slides in videos (accuracy, branding, legibility, formatting)
- Script alignment (does the video match the script?)
- Captions/subtitles (present, accurate, synced)
- Pacing and audio levels

### 2. Course Copy & Tone
- Consistent voice across modules and weeks
- Appropriate for target audience
- Cohort vs. self-paced tone (collaborative vs. independent language)
- No placeholder text or rough draft language
- Grammar, punctuation, formatting consistency

### 3. Storyboard Currency
- Do storyboards reflect what's actually live on Uplimit?
- Were changes made on-platform that never got back-ported to source files?
- Could someone rebuild the course from the storyboard alone?

### 4. Widgets & Interactive Elements
- Functional (no broken interactions)
- Accessible (WCAG 2.2 AA)
- Consistent design language across the course
- Answer keys exist for all widgets (remediation item — Analytics/Excel has one, others need them)

### 5. Assessments & Knowledge Checks
- Correct answers verified
- Clear rubrics where applicable
- Fair difficulty and appropriate alignment to learning outcomes
- Answer keys complete

### 6. Cases & Data Files
- Accurate and complete data
- Files downloadable and usable
- Instructions clear

### 7. Graphics & Images
- Branded consistently
- Legible at display size
- Current (no outdated content)

### 8. Platform Configuration
- Everything uploaded and wired up correctly on Uplimit
- No broken links or missing assets
- Correct sequencing

### 9. File Organization
- Folder structure navigable
- Naming conventions followed
- No orphaned files, duplicates, or stale drafts
- Clear what's current vs. archived

---

## Review Progress

### Video Review — In Progress

Tracked in: `Video_Reviews.xlsx` (currently in Downloads — to be moved here)

**49 issues logged across 4 courses:**

| Avatar | Course | Issues Logged |
|--------|--------|---------------|
| Nadine | Fundamentals of Accounting | 5 |
| Mehmet | Fundamentals of Analytics and Excel | 4 |
| Fillipe-Steven | Fundamentals of Financial Analysis | 26 |
| Matt | Business of Sports Marketing | 10 |

**Not yet reviewed:** Igniting AI Transformation, AI Prototyping for Business Innovation

### Widget Design Audit — Complete (2026-03-10)

Sampled 2-3 widgets per course (all 6 for AI Prototyping). Full findings in [Widget-Style-Guide.md](Widget-Style-Guide.md). Key finding: **three different design systems** are in use across courses, with no unified standard.

### All Other Categories — Not Yet Started

---

## Recurring Patterns (from video review + folder audits + widget audit)

These are the consistency issues already surfaced. They will feed into a style guide.

### Video / Script Patterns

**Module references in scripts (brittle)**
Scripts contain language like "in the next module," "past 4 modules," "in this section." These break if content is reordered. Found in Financial Analysis (items 12-14, 23, 27, 31, 35) and Sports Marketing (item 49).

**Slide text formatting inconsistencies**
- Ampersand vs. "plus" vs. "and" — no standard (Analytics item 7, Financial Analysis items 28, 21)
- Bullet punctuation — some with periods, some without, within the same video (Accounting item 2, Financial Analysis items 16, 20)
- Capitalization rules unclear (Accounting item 1, Sports Marketing item 43)
- Quoting/bracketing conventions differ across avatars (Financial Analysis items 10, 11)

**Avatar / delivery issues**
- Glitches and hard transitions (Financial Analysis items 15, 22; Sports Marketing item 36)
- Pacing problems — pauses needed, delivery too fast at end of videos (Analytics item 9, Sports Marketing items 37, 46)
- Odd avatar behavior (Financial Analysis item 32)
- Audio level inconsistencies (Sports Marketing item 38)

**Content clarity on slides**
- Too much content on screen (Financial Analysis item 24)
- Slide order not matching narration order (Financial Analysis item 19)
- Missing explanations — students must infer what should be stated (Financial Analysis item 18)

**Production artifacts**
- VEO watermark left in video (Sports Marketing item 48)
- Missing animations for referenced graphics (Analytics item 8)

### Widget Design Patterns

**Three separate design systems in use (see [Widget-Style-Guide.md](Widget-Style-Guide.md) for full details)**

| System | Courses | Font | Primary Color |
|--------|---------|------|---------------|
| "Geist Neutral" | Analytics/Excel, Sports Marketing (W3+) | Geist | `#171717` / `#6b9085` sage |
| "Ivey Brand" | Accounting | System fonts | `#005951` green / `#5B2C6F` purple |
| "Teal Pastels" | AI Prototyping, AI Transformation (partial) | Segoe UI | `#034638` teal / pastels |

Financial Analysis uses Inter font with a fourth hybrid palette. AI Transformation uses three different fonts across its own widgets.

**Specific issues:**
- Accounting uses purple (`#5B2C6F`) for incorrect answers instead of red — different mental model from all other courses
- 5 different primary fonts across 6 courses
- At least 4 different button style patterns
- 4 different correct/incorrect color pairings
- Accessibility quality varies widely: Accounting and AI Transformation strongest, Financial Analysis weakest (no ARIA live regions, no keyboard nav on flipcards)

### Structural / Organizational Patterns

**No standard folder structure**
Every course organized differently. Analytics uses `M{n}-Topic.md`; Sports Marketing uses `module-{n}-description.md`; Financial Analysis and Accounting use DOCX with no module-level file separation.

**Version control gaps**
- Multiple versions of same file with no clear "current" indicator (Accounting: 4 versions of one activity)
- Updated files alongside originals (Financial Analysis: `06_quiz.html` and `06updated_quiz.html`)
- "OLD" and "Not in Live Course" files never removed

**Duplicate storage**
- Accounting stores everything in both a central folder AND per-module folders
- Financial Analysis has same graphics in Screen Exports, Final Asset Exports, and Final Reference Slides
- AI Transformation has Week 1/2 content nested inside the Week 3 folder

**Contributor-specific organization**
- Accounting: top-level folders named after developers (Majid, Yuvika)
- AI Transformation: Mehmet edits folder, Yuvika & Majid widgets folder
- No shared convention for how contributors organize their work

---

## Process (Evolving)

### Phase 1: Post-Mortems (Current)
- Review each course across all categories
- Document findings in consistent format
- Create missing deliverables as they're identified (answer keys, updated storyboards)
- Reconcile source files with what's live on platform

### Phase 2: Standards Definition
- Based on post-mortem patterns, define:
  - Standard folder structure template
  - Naming conventions
  - Required deliverables per course type (SP vs. CB)
  - Style guide (slide formatting, script language, tone)
  - Quality gates for each development stage

### Phase 3: Process Integration
- Embed standards into course development workflow
- Define review checkpoints at key milestones (not just post-launch)
- Maintain this space as living documentation

---

## Remediation Items (Identified So Far)

| Item | Courses Affected | Priority |
|------|-----------------|----------|
| Create widget answer keys | All except Analytics/Excel | High |
| Reconcile storyboards with live platform content | All (assumed) | High |
| Resolve 49 open video issues | Accounting, Analytics, Financial Analysis, Sports Marketing | High |
| Review videos for AI Transformation and AI Prototyping | Those 2 courses | Next |
| Clean up deprecated/duplicate files | All courses | Medium |
| Standardize folder structure | Future courses (retrofit TBD) | Phase 2 |
| Create style guide from consistency findings | Cross-course | Phase 2 |
| Unify widget design system (font, colors, buttons, feedback) | All courses | Phase 2 |
| Fix Accounting purple-for-incorrect feedback colors | Accounting | High |
| Add keyboard nav to Financial Analysis flipcards | Financial Analysis | Medium |
| Add ARIA live regions to Financial Analysis widgets | Financial Analysis | Medium |
| Add `prefers-reduced-motion` support to Analytics, Sports Mktg, Fin. Analysis, AI Prototyping | Those 4 courses | Medium |

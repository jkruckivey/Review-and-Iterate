# Pre-Build Review (QA 1) Checklist

**Purpose:** This is the most critical quality gate in the new development pipeline. It happens *before* any HeyGen videos are rendered, and *before* anyone touches the Uplimit platform. Fixing a mistake here takes 10 seconds; fixing it in the Platform QA stage takes hours.

**Usage:** Create this as a master checklist on each Microsoft Planner card. Do not move the card to the "Development" bucket until these items are verified by a peer reviewer.

---

### 1. Video Scripting & Narration
- [ ] **No Brittle Sequencing:** The script does NOT say things like "in the next module," "past 4 modules," or "in Week 3." It only references "this week" or past topics (to allow courses to be reordered without breaking).
- [ ] **Grammar & Tone Continuity:** Narration uses consistent phrasing (e.g., choosing either "vs." or "versus", "and" or "&" consistently).
- [ ] **Number Formatting:** All numbers under 10 are spelled out in the script.
- [ ] **Pacing Marks:** The script includes intentional pauses or transition breaks, especially toward the end of a video.

### 2. Slide Concept & Design
- [ ] **Single Concept Adherence:** Does each slide communicate exactly one idea? If a slide has 6 bullets covering 3 topics, force the author to split it.
- [ ] **No Narration Duplication:** Ensure the proposed slide text does not simply duplicate the spoken script verbatim.
- [ ] **Animations Indicated:** The storyboard explicitly indicates progressive reveal timings for bullets that map natively to the audio track.
- [ ] **Purposeful Meaning:** Any requested B-roll, 4K AI images, or technical graphics are *directly referenced or explained* in the accompanying narration. No purely decorative visuals.

### 3. Interactive Widgets & Assessments
- [ ] **Answer Keys Verified:** Every single interactive widget, quiz, or knowledge check has a verified, complete answer key drafted alongside it.
- [ ] **Design Language Adherence:** Instructions for the widget strictly adhere to the unified style guide (e.g., confirming the correct standard colors are used for "Incorrect" feedback, removing legacy patterns like purple-for-incorrect).
- [ ] **Data File Accuracy:** Any case files or datasets referenced in the module are fully complete, attached to the card, and tested for accuracy.

### 4. File Hygiene & Organization
- [ ] **Single Source of Truth:** Confirm the reviewed storyboard is the definitive, solitary version. No `_OLD`, `v2_temp`, or duplicate files exist in the source folder for this module.
- [ ] **No Placeholders:** All conversational placeholder text (e.g., "[Reviewer, is this right?]" or "[Insert image here]") has been fully resolved and deleted.

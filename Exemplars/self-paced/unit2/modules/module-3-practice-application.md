## MODULE 3: Practice and Application

**Version:** 1.0.0 | **Last Updated:** March 19, 2026

**Purpose:** Build competency through guided practice. Students apply Five Forces framework to real industries using interactive widgets, watch Canary Medical CEO interview on industry forces, and complete guided reflection demonstrating independent analysis capability.

**Unit Learning Outcomes Supported:**
- ALO 2: Analyze any industry using Porter's Five Forces framework
- ALO 3: Identify the strongest competitive force(s) in a given industry
- ALO 4: Set realistic profitability goals based on industry analysis

**Uplimit Module Position:** Third module in Unit 2 (Goal Setting)

---

## Element Table

| Order | Element | Content/Purpose | Time | Implementation Notes |
|-------|---------|-----------------|------|---------------------|
| 1 | **▬ Text** | Widget intro: Five Forces Identifier | 2 min | Embedded markdown below |
| 2 | **⚙ Widget** | Five Forces Identifier (8 scenarios) | 8 min | `five-forces-identifier.html` |
| 3 | **▬ Text** | Widget intro: Five Forces Analyzer | 2 min | Embedded markdown below |
| 4 | **⚙ Widget** | Five Forces Analyzer (slider-based) | 8 min | `five-forces-analyzer.html` |
| 5 | **▶ Video Interview** | Canary Medical CEO on industry forces | 5 min | Bill Hunter interview clip |
| 6 | **▬ Text** | Canary Medical context (~150 words) | 1 min | Embedded markdown below |
| 7 | **▬ Text** | Guided reflection prompt (~100 words) | 2 min | Embedded markdown below |
| 8 | **📝 Guided Reflection** | "Analyze Five Forces for industry of choice" | 20 min | Student written response, AI coach feedback |

**Module Totals:**
- **Total Time:** 70–90 minutes
- **Required Elements:** 8
- **Interactive Time:** 16 minutes (two widgets)
- **Writing/Reflection Time:** 20 minutes
- **Video/Watching Time:** 6 minutes
- **Reading Time:** 5 minutes

---

## Element 1: Text — Widget Introduction: Five Forces Identifier

**Copy this markdown directly into Uplimit platform:**

```markdown
# Practice: Recognize Five Forces in Real Scenarios

You've learned the Five Forces framework. Now let's practice recognizing each force in realistic business situations.

In the interactive activity below, you'll encounter 8 different business scenarios. Your task: **Identify which of the five forces is MOST relevant** to each scenario.

## What You'll Discover

- How to recognize each force in real-world contexts
- That forces appear in combination (but one is usually strongest)
- How forces manifest differently across industries (airline rivalry looks different from tech rivalry)
- That the same situation can have multiple relevant forces, but one dominates

## How the Identifier Works

1. **Read scenario** (2-3 sentences describing a business situation)
2. **Select which force** you think is most relevant (5 force options)
3. **Get instant feedback** explaining why your choice was right/wrong
4. **Learn from mistakes** with detailed explanations (don't get discouraged if you miss some!)
5. **Track your score** (8/8 = "Perfect!"; 6-7/8 = "Great!"; 5-6/8 = "Good, keep learning")

## Why This Matters

Identifying forces quickly is your first step toward industry analysis. Once you can recognize forces, you'll be ready to rate them (which you'll do in the next activity).

Take your time. You can try scenarios multiple times. There's no penalty for learning—just growth.

Let's begin!
```

---

## Element 2: Interactive Widget — Five Forces Identifier

### ⚙ Five Forces Identifier Widget

**Purpose:** Practice recognizing forces in realistic scenarios; build automaticity in force identification

**Status:** ✅ Built and tested

**File:** `five-forces-identifier.html`
**Location:** `/widgets/`
**Time:** 8 minutes

### How It Works

Students encounter 8 business scenarios (randomized order). For each:

1. **Read scenario** (e.g., "Netflix is losing subscribers to Disney+, Apple TV+, and HBO Max...")
2. **Select force category** (Rivalry / New Entrants / Substitutes / Suppliers / Customers)
3. **Submit answer**
4. **Receive instant feedback:**
   - ✅ **If correct:** "Correct! This is a [FORCE] situation because..." (explain why)
   - ❌ **If incorrect:** "Not quite—you might be thinking of [OTHER FORCE], but the key issue here is [CORRECT FORCE] because..." (gentle correction with explanation)

### Scenarios (8 total)

1. **Amazon Cloud vs. Microsoft Azure** (New Entrants—economies of scale)
2. **Netflix vs. Disney+** (Substitutes—competing for entertainment)
3. **Airlines: Intense Price Competition** (Rivalry—evenly matched, price-based)
4. **EV Makers Dependent on Battery Suppliers** (Suppliers—critical input, limited suppliers)
5. **Hotel Chains Losing to Airbnb** (Substitutes—alternative accommodation)
6. **Walmart's Dominance Over Small Suppliers** (Customers—Walmart extracts value)
7. **Pharmaceutical Patent Expiration** (New Entrants—barriers drop when patent expires)
8. **App Developers Dependent on Apple App Store** (Customers—Apple controls distribution)

**Scoring System:**
- 8/8: "Perfect! You can identify forces with clarity."
- 6-7/8: "Great! You're recognizing most forces. Review the ones you missed."
- 5-6/8: "Good progress! Keep practicing—force identification is a learnable skill."
- <5/8: "Keep trying! Forces can be tricky. Review explanations and try again."

**Learning Outcomes:**
- Recognize five forces in diverse scenarios
- Distinguish between forces (e.g., rivalry vs. substitutes can look similar)
- Connect business situations to strategic frameworks
- Build confidence in analysis

**Technical:** HTML form with radio buttons, JavaScript scoring, instant feedback with ARIA live regions for accessibility

**Accessibility:** ✅ Keyboard nav, ARIA labels, high contrast, focus indicators, screen reader support

---

## Element 3: Text — Widget Introduction: Five Forces Analyzer

**Copy this markdown directly into Uplimit platform:**

```markdown
# Analyze: Rate Each Force and See Industry Attractiveness

You've practiced recognizing individual forces. Now it's time to analyze a complete industry by rating all FIVE forces simultaneously.

In the interactive tool below, you'll analyze an industry by:
1. **Selecting an industry** (or entering your own)
2. **Rating each of the five forces** on a 1-5 scale
3. **Watching a real-time dashboard** show overall industry attractiveness
4. **Answering diagnostic questions** for each force to guide your ratings
5. **Comparing your analysis** to other industries

## What You'll Discover

- That industry attractiveness is the result of MULTIPLE forces (not just one)
- How to synthesize five separate ratings into an overall assessment
- Diagnostic questions that guide rigorous analysis
- That the same industry can have different attractiveness depending on how forces are rated (your judgment matters)

## How the Analyzer Works

1. **Select industry preset** (Airlines, Pharmaceuticals, Software, Retail, etc.) OR enter custom industry
2. **For each force, answer diagnostic questions:**
   - Rivalry: "How many competitors? Are they evenly matched?"
   - New Entrants: "What barriers exist? Capital? Talent? Switching costs?"
   - Substitutes: "Are there viable alternatives?"
   - Suppliers: "How dependent are you on suppliers? How many exist?"
   - Customers: "How concentrated are customers? Can they switch easily?"
3. **Rate force on 1-5 scale** (1=weak force helping profitability, 5=strong force hurting profitability)
4. **See real-time results:**
   - Overall attractiveness score (average of five ratings)
   - Force comparison bar chart
   - Insights panel ("Strongest force: Rivalry (5); Suppliers have moderate power (3)")
5. **Compare to other industries** ("How does your airline analysis compare to pharmaceuticals?")

## Why This Approach?

The diagnostic questions do the heavy lifting. They help you think through each force systematically instead of guessing. By the time you rate on the 1-5 scale, you've already analyzed deeply. The scale becomes your synthesis, not your starting point.

Let's analyze your chosen industry.
```

---

## Element 4: Interactive Widget — Five Forces Analyzer

### ⚙ Five Forces Analyzer Widget

**Purpose:** Synthesize five separate force assessments into overall industry attractiveness; practice diagnostic thinking

**Status:** ✅ Built and tested

**File:** `five-forces-analyzer.html`
**Location:** `/widgets/`
**Time:** 8 minutes

### How It Works

1. **Select Industry:** Dropdown presets (Airlines, Pharmaceuticals, Software, Retail, Media, Medical Devices) OR "Custom"

2. **For Each Force, Answer Diagnostic Questions:**

   **Rivalry:**
   - How many significant competitors? (Solo? 2-3? 4+ evenly matched?)
   - Are competitors evenly matched in size/strength? (Yes / Somewhat / No)
   - Is competition primarily price-based? (Yes / Somewhat / No)
   - Are there high exit barriers? (Yes / Somewhat / No)

   **New Entrants:**
   - Capital requirements for entry? (Low / Moderate / High)
   - Switching costs for customers? (Low / Moderate / High)
   - Network effects or brand loyalty? (Strong / Moderate / Weak)
   - Access to distribution? (Easy / Moderate / Difficult)

   **Substitutes:**
   - Do viable substitutes exist? (None / Few / Many)
   - Are substitutes improving/becoming cheaper? (Rapidly / Moderately / Slowly)
   - What % of customers might switch? (<20% / 20-50% / >50%)

   **Suppliers:**
   - How concentrated are suppliers? (Many / Few / Single source)
   - Financial significance of supplier costs? (Low / Moderate / High)
   - Strategic significance (critical to competitive advantage)? (No / Somewhat / Yes)

   **Customers:**
   - How concentrated are customers? (Fragmented / Moderate / Highly concentrated)
   - Can customers switch suppliers easily? (Difficult / Moderate / Easy)
   - What % of revenue from largest customer? (<10% / 10-25% / >25%)
   - Can customers integrate backward? (Impossible / Difficult / Possible)

3. **Rate Each Force (1-5 Scale):**
   - Slider for each force (after questions answered)
   - Default: Based on diagnostic answers (student can adjust)
   - 1 = Force is weak (benefits profitability)
   - 5 = Force is strong (hurts profitability)

4. **See Real-Time Dashboard:**
   - **Overall Attractiveness Score** (average of 5 ratings, 1-5 scale)
   - **Bar chart** showing force comparisons (which is strongest?)
   - **Insights panel:** "This industry has strong rivalry (4.5) and high barriers (1.5), creating moderate attractiveness (2.8/5)"
   - **Benchmark comparison:** "Compared to pharmaceuticals (1.8/5), this industry is less attractive"

5. **Export Analysis:** Button to export findings as PDF (optional)

### Example Output (Airlines):

```
Industry: Airlines
Overall Attractiveness: 4.2/5 (Low attractiveness)

Force Ratings:
- Rivalry: 5.0 (Very strong—evenly matched competitors, price-based competition)
- New Entrants: 4.0 (Strong barriers: capital, airport slots, brand)
- Substitutes: 3.0 (Moderate: video conferencing substitutes for business travel)
- Suppliers: 3.5 (Moderate: concentrated suppliers, fuel costs important)
- Customers: 4.5 (Strong: customers have high switching power, price-sensitive)

Key Insights:
"Airlines face very strong competitive pressures across most forces. Only barriers to entry provide some protection. Expected profitability: Low (2-8% ROA)."
```

### Example Output (Pharmaceuticals):

```
Industry: Pharmaceuticals
Overall Attractiveness: 1.8/5 (High attractiveness)

Force Ratings:
- Rivalry: 1.5 (Weak: patents protect differentiation, limited direct competition)
- New Entrants: 1.0 (Weak: very high barriers [R&D, FDA approval, capital])
- Substitutes: 1.5 (Weak: limited alternatives for disease-specific drugs)
- Suppliers: 2.0 (Weak: multiple suppliers, low switching costs)
- Customers: 1.5 (Weak: medical need drives prescription, not price negotiation)

Key Insights:
"Pharmaceuticals face weak competitive pressures across all forces. Barriers are exceptional. Expected profitability: High (15-20% ROA)."
```

**Learning Outcomes:**
- Understand that attractiveness is multi-dimensional (not just one force)
- Synthesize multiple ratings into overall assessment
- Compare industries systematically
- Apply diagnostic questions rigorously
- Recognize industry patterns (pharma always scores low/attractive; airlines always score high/unattractive)

**Technical:** HTML form with 5 slider groups + diagnostic questions, Chart.js for visualization, real-time calculation, localStorage for saving student's analysis

**Accessibility:** ✅ Keyboard nav (Tab through questions, Arrow keys on sliders, Enter to submit), ARIA labels on all sliders and questions, high contrast chart, focus indicators, screen reader support

---

## Element 5: Video Interview — Canary Medical CEO on Industry Forces

### ▶ Video Interview: Bill Hunter (Canary Medical CEO)

**File Details:**
- **Source:** Interview clip extracted from longer Bill Hunter conversation (Nov 2025)
- **Duration:** ~5 minutes
- **Format:** MP4 H.264, 1920x1080
- **Caption File:** VTT format (extracted from interview transcript)
- **Title on Platform:** "Canary Medical: Understanding Industry Forces—Interview with CEO Bill Hunter"

**Interview Clip Content:**

The clip focuses on how Canary Medical's strategy was shaped by industry forces:

**Key Segments:**

1. **"What makes medical device industry attractive?"** (1 min)
   - Bill discusses high barriers to entry (regulatory, capital, clinical evidence)
   - How Stryker, Smith & Nephew, J&J dominate through scale
   - Why competition is limited compared to software

2. **"Who are your real competitors?"** (1 min)
   - Acknowledges direct competitors (other implant companies)
   - Discusses substitutes (alternative treatments, conservative management)
   - Explains why Canary's differentiation (data from implant) matters

3. **"What about suppliers?"** (1 min)
   - Discusses dependence on manufacturing partners
   - How supply chain constraints affect startups
   - Why vertical integration would be expensive

4. **"Who holds the power: customers, hospitals, doctors, or insurers?"** (1.5 min)
   - Discusses complexity of healthcare buying (multiple decision-makers)
   - Doctors drive medical decisions; hospitals/insurers drive economics
   - How Canary navigates multiple customer layers

5. **"Bottom line: Is medical devices an attractive industry?"** (0.5 min)
   - Bill: "High barriers protect profitability. But innovation is expensive. Not attractive if you're a follower. Attractive if you're a leader with breakthrough technology."

**Production Notes:**
- Interview clip is candid, not scripted
- Bill speaks authentically about strategic thinking
- Shows real strategic reasoning (not textbook answers)
- Connects abstract Five Forces framework to real company decisions

**Platform Integration:**
- Embed via iFrame with player controls
- Include transcript below video
- Include reflection prompt after video

**Accessibility:**
- ✅ VTT caption file
- ✅ Transcript available
- ✅ Video player with play/pause, CC toggle, speed control

---

## Element 6: Text — Canary Medical Context

**Copy this markdown directly into Uplimit platform:**

```markdown
# Canary Medical: Medical Device Industry Analysis

Throughout this course, you're following **Canary Medical**, a Vancouver-based medical device company, as they navigate real strategic decisions. Their story brings these frameworks to life.

## The Company

Canary Medical develops smart dental implants—artificial tooth roots that integrate digital monitoring to warn patients and dentists about implant failures before they become emergencies. The company was founded in 2009 and remains a private startup competing in the medical device industry against giants like Stryker, Smith & Nephew, and Johnson & Johnson.

## Industry Context

The medical device industry includes products ranging from simple (bandages, syringes) to complex (imaging equipment, surgical robots, implants). Canary Medical competes specifically in the **orthopedic implants** segment—a multi-billion-dollar market dominated by large, established competitors.

## Canary's Challenge

As a startup in a highly consolidated market, Canary must answer: "How can we compete against companies 100x our size?"

Their answer: **Focus on a specific application (dental implants), develop breakthrough technology (digital monitoring), and emphasize innovation over cost leadership.**

Watch the CEO interview above to hear Bill Hunter explain how industry forces shaped this strategy.

---

**Key Questions to Consider:**
- Which Five Forces are strongest in medical devices? Which are weakest?
- How does Canary's strategy respond to industry forces?
- Would you invest in Canary Medical given the industry structure?
```

---

## Element 7: Text — Guided Reflection Prompt

**Copy this markdown directly into Uplimit platform:**

```markdown
# Reflection: Apply Five Forces to Your Industry

Now it's your turn. You've practiced identifying forces and rating them. You've seen how Canary Medical navigates industry forces strategically.

## Your Task

**Select an industry you find interesting** (your workplace, a company you admire, an emerging technology, etc.). **Analyze that industry using Five Forces.**

## What to Include

Your reflection should address:

1. **Industry selection:** Which industry are you analyzing? Why did you choose it?

2. **Five Forces Analysis:**
   - **Rivalry:** Rate intensity (1-5). Why?
   - **New Entrants:** Rate barrier strength (1-5). Why?
   - **Substitutes:** Rate threat (1-5). Why?
   - **Suppliers:** Rate bargaining power (1-5). Why?
   - **Customers:** Rate bargaining power (1-5). Why?

3. **Overall Assessment:** Based on your five ratings, is this industry attractive (low score) or unattractive (high score)? What does profitability look like?

4. **Strategic Implication:** If you were a company in this industry, what would you do to improve profitability given the forces you identified?

## Format

- **Length:** 300-500 words (write naturally; don't force word count)
- **Structure:** Address the four points above in any order that feels natural
- **Examples:** Use specific companies or scenarios to illustrate your points
- **Tone:** Analytical but accessible (explain jargon; don't assume reader knows strategy)

## Criteria

Your reflection will be assessed on:
- ✅ **Identified all five forces** (not just one or two)
- ✅ **Justified your ratings** (didn't just assign numbers; explained why)
- ✅ **Synthesized into overall assessment** (connected five forces to profitability outlook)
- ✅ **Showed strategic thinking** (proposed realistic responses to forces)

## How Feedback Works

You'll submit your reflection, and an AI coach will:
1. **Check comprehension** — Did you identify all five forces? Did you understand them correctly?
2. **Provide feedback** — Strengths ("You really understood supplier power in this industry") and growth areas ("Consider how substitutes might emerge...")
3. **Ask follow-up questions** — Push your thinking deeper ("Given that rivalry is very high, would you enter this industry?")

Your instructor may also read and comment on your reflection.

## Why This Matters

This reflection demonstrates your ability to **independently analyze an industry**—a core skill for strategic decision-making. In later modules, you'll use this analysis to make positioning choices. In Unit 10 (capstone project), you'll apply this skill to a real company or industry.

Take your time. Think deeply. Use examples. Let your curiosity guide the analysis.

**Ready? Let's analyze.**
```

---

## Element 8: Guided Reflection Assessment

### 📝 Guided Reflection: "Analyze Five Forces for Industry of Choice"

**Assessment Type:** Formative (low-stakes, designed to help you learn and demonstrate competency)

**Submission Format:**
- Written response (300-500 words)
- Free-response text box in platform
- Submit once; can revise based on AI coach feedback

**Submission Process:**
1. Read reflection prompt (Element 7)
2. Select industry (in your head or write it down)
3. Analyze using Five Forces framework
4. Write reflection addressing four points:
   - Industry selection & rationale
   - Five Forces ratings (with justifications)
   - Overall attractiveness assessment
   - Strategic implications
5. Submit response

**AI Coach Feedback:**

After submission, AI coach provides structured feedback:

```
COMPREHENSION CHECK:
✅ "You correctly identified all five forces: rivalry (strong), barriers (high), substitutes (moderate), suppliers (low), customers (moderate)."

ANALYTICAL DEPTH:
✅ "You provided specific examples to justify your ratings—this shows deep thinking."
⚠️ "Your assessment of supplier power could be stronger. You mentioned one supplier relationship, but what about the broader supplier landscape?"

SYNTHESIS:
✅ "You correctly concluded that despite strong rivalry, high barriers and low supplier power make this industry moderately attractive."

STRATEGIC THINKING:
✅ "Your recommendation to 'differentiate and build switching costs' is sound strategy given the forces you identified."

GROWTH AREA:
"Consider how technology might change barriers to entry over the next 5 years. What would that mean for your industry analysis?"

NEXT STEP:
"In Module 4, you'll deepen this analysis by positioning within your industry. Your Five Forces understanding will inform your positioning strategy."

Score: 8/10 (Excellent understanding; minor growth opportunity)
```

**Rubric (Optional, for instructor):**

| Criterion | Excellent (4) | Good (3) | Developing (2) | Beginning (1) |
|---|---|---|---|---|
| **Identified all five forces** | All five forces identified with specific examples | Four forces clearly identified | Three forces mentioned | Fewer than three forces |
| **Justified ratings** | Clear, specific justifications; connects to industry structure | Decent justification for most forces | Some justification; mostly surface-level | Minimal or vague justification |
| **Synthesized into overall assessment** | Clear overall attractiveness conclusion; connected to profitability | Attempted synthesis; mostly coherent | Some synthesis; loosely connected | No clear synthesis or conclusion |
| **Strategic thinking** | Realistic strategic response; considers force dynamics | Reasonable strategy suggested | Generic strategy without specific connection | No strategy or irrelevant suggestions |

**Time to Complete:** 20-25 minutes

**Timing in Module:** After students complete both widgets and watch interview (after ~18 minutes), reflection gives them time to synthesize learning through writing

**Learning Purpose:**
- Demonstrate independent application of Five Forces framework
- Synthesize multiple forces into coherent industry analysis
- Connect framework to strategic decision-making
- Prepare for Unit 3 (positioning within industry)

**Accessibility:**
- ✅ Large text input box (easy to see cursor)
- ✅ Character counter (shows word count progress)
- ✅ Auto-save (prevents data loss)
- ✅ Screen reader compatible (ARIA labels on input, instructions clear)
- ✅ Keyboard operable (Tab to input, type, Submit button accessible)

---

## Module Production Checklist

Before launching Module 3, verify:

- [ ] **Widgets:**
  - [ ] Five Forces Identifier widget tested (8 scenarios, feedback accurate)
  - [ ] Five Forces Analyzer widget tested (sliders work, dashboard calculates correctly)
  - [ ] Both widgets responsive on mobile (6"), tablet (10"), desktop (24")
  - [ ] Both widgets keyboard navigable and screen reader compatible

- [ ] **Video:**
  - [ ] Bill Hunter interview clip extracted and edited (~5 min)
  - [ ] VTT caption file created and tested
  - [ ] Transcript provided below video player

- [ ] **Text & Assessment:**
  - [ ] All markdown text (Elements 1, 3, 6, 7) imported and formatted
  - [ ] Guided reflection prompt clear and actionable
  - [ ] AI coach feedback system configured and tested
  - [ ] Rubric created (for optional instructor grading)

- [ ] **Accessibility:**
  - [ ] Full WCAG 2.2 AA compliance
  - [ ] Video captions synced with audio
  - [ ] High contrast on all elements (4.5:1 minimum)
  - [ ] Keyboard navigation comprehensive
  - [ ] Focus indicators visible on all interactive elements

- [ ] **QA/Testing:**
  - [ ] Submitted reflection triggers AI coach feedback
  - [ ] Feedback appears within 5-10 seconds
  - [ ] Student can revise and resubmit

- [ ] **SME Review:**
  - [ ] Michael Raynor reviews Canary Medical context for accuracy
  - [ ] Validates AI coach rubric and feedback prompts

---

**Last Updated:** March 19, 2026
**Version:** 1.0.0 (Self-Paced Exemplar)
**Status:** Ready for production

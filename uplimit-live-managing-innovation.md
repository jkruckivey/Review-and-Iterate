# Managing Innovation — Live Uplimit Widgets (Extracted 2026-03-20)

Source: Uplimit GraphQL API via Apollo cache, session `session_cmfvbcany05ok197f0lmf12no`
Course slug: `ivey-business-school-managing-innovation`
Course ID: `course_cmfrbb4bb00t7199n8ju7dh7s`
Widget host: `https://uplimit.com/ugc-assets/course/course_cmfrbb4bb00t7199n8ju7dh7s/assets/{token}/`

## Widgets on Platform (31 HTML widgets)

| # | Module | Section | Platform Filename | Source |
|---|--------|---------|-------------------|--------|
| 1 | Getting Started | Course Overview | `io-cb-mi-gs-weekly-recap-lighter-colors.html` | CDN only |
| 2 | Week 1: Self-Assessment | Self-Assessment | `io-cb-mi-w1-pre-assessment-v2-lighter-colors.html` | CDN only |
| 3 | Module 1: How the Innovation Process is Different | Accidental Innovation | `io-cb-mi-w1-accidental-innovation-flip-cards-lighter-colors.html` | CDN only (5.4MB, embedded images) |
| 4 | Module 1: How the Innovation Process is Different | The Innovation Tension | `3m-sixsigma-timeline.html` | W1/M1/3m-sixsigma-timeline(1).html |
| 5 | Module 1: How the Innovation Process is Different | The Innovation Tension | `process-vs-innovation.html` | W1/M1/process-vs-innovation.html |
| 6 | Module 2: Innovation's Hard Problems | The Shape of Iteration | `shape-of-innovation2.html` | W1/M2/shape-of-innovation(2).html |
| 7 | Module 2: Innovation's Hard Problems | Human Barriers to Innovating | `io-cb-mi-w1-the-xerox-parc-story-v2-lighter-colors.html` | CDN only |
| 8 | Module 4: Synthesis and Application | Week 1 Reflection | `io-cb-mi-w1-m1-podcast-player.html` | CDN only (33MB, embedded audio) |
| 9 | Week 2: Self-Assessment | Self-Assessment | `io-cb-mi-w2-m1-pre-assessment-lighter-colors.html` | CDN only |
| 10 | Module 2: User and Open Innovation | User Centric Innovation | `io-cb-mi-w2-m1-user-centric-innovation-approaches-follow-up-activity-lighter-colors.html` | CDN only |
| 11 | Module 2: User and Open Innovation | Where Innovation Really Comes From | `user-innovation-chart.html` | W2/M2/user-innovation-chart.html |
| 12 | Module 2: User and Open Innovation | Challenges in Managing Crowdsourcing | `io-cb-mi-w2-m1-challenges-in-managing-crowdsourcing-business-model-follow-up-activity-lighter-colors.html` | CDN only |
| 13 | Week 3: Self-Assessment | Self-Assessment | `io-cb-mi-w3-pre-assessment-lighter-colors.html` | CDN only |
| 14 | Module 1: Why Innovations Spread | Putting the Strategy to Work | `scurve-placement-activity.html` | W3/M1/scurve-placement-activity.html |
| 15 | Module 2: Dominant Designs | When One Design Wins | `standards-battle-infographic.html` | W3/M2/standards-battle-infographic.html |
| 16 | Module 2: Dominant Designs | Factors That Determine a Dominant Design | `what-determines-winner2.html` | W3/M2/what-determines-winner(2).html |
| 17 | Module 2: Dominant Designs | After the Battle: How Industries Transform | `creative-ferment-consolidation.html` | W3/M2/creative-ferment-consolidation.html |
| 18 | Module 2: Dominant Designs | When the Market Decides | `bn-aftermath-timeline.html` | W3/M2/bn-aftermath-timeline.html |
| 19 | Module 3: Ambidexterity | Too Busy to Innovate | `ambidexterity-types1.html` | W3/M3/ambidexterity-types(1).html |
| 20 | Module 3: Ambidexterity | The Debate | `etypes-options.html` | W3/M3/etypes-options.html |
| 21 | Module 3: Ambidexterity | Holding the Line | `jordan-timeline.html` | W3/M3/jordan-timeline.html |
| 22 | Module 4: Synthesis and Application | Week 3 Reflection | `io-cb-mi-w3-podcast-player.html` | CDN only (2.7MB, embedded audio) |
| 23 | Module 1: The Value of Creative Products | The $500 Trash Bin | `vipp-discussion-widget.html` | W4/vipp-discussion-widget.html |
| 24 | Module 2: The Dynamics of Creative Markets | A Rising Tide That Sinks Most Boats | `pareto-distribution.html` | W4/pareto-distribution.html |
| 25 | Module 2: The Dynamics of Creative Markets | A Rising Tide That Sinks Most Boats | `costs-vs-uncertainty1.html` | W4/costs-vs-uncertainty(1).html |
| 26 | Module 2: The Dynamics of Creative Markets | Same Genre, Very Different Fates | `three-films-chart.html` | W4/three-films-chart.html |
| 27 | Module 2: The Dynamics of Creative Markets | The Folly of Category Comparisons | `investor-pitches1.html` | CDN only |
| 28 | Module 2: The Dynamics of Creative Markets | What Then Can We Do? | `blair-witch-comparison.html` | CDN only |
| 29 | Module 2: The Dynamics of Creative Markets | What Then Can We Do? | `portfolio-strategy.html` | CDN only |
| 30 | Module 3: Making and Selling Special Things | Coherence in The Sixth Sense | `patterns-trajectories-closure.html` | CDN only |
| 31 | Module 3: Making and Selling Special Things | How to Manage the Making of Special Things | `coherence-scenario.html` | CDN only |

## Notes

- CDN asset URLs use token-prefixed paths: `assets/{timestamp-token}/{filename}.html`
- Pre-assessment and follow-up activity widgets use React + Tailwind CSS + Babel (large files, 165–230KB)
- Podcast players embed base64 audio content (W1: 33MB, W3: 2.7MB)
- Flip cards widget embeds base64 images (5.4MB)
- Local source files are in `Courses Accepted for Development/IO-CB-Feb18-Managing-Innovation/Course Assests_Cases, HTML Graphics and Widgets, etc/`
- No long-path prefix needed (paths are within 260 char limit)
- `sync-managing-innovation-widgets.py` handles copying locally-available files with correct platform filenames

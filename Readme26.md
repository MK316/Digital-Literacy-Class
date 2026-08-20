# Digital Literacy and English Education
### A Course for Pre-Service EFL/ESL Teachers (1st–2nd Year) | Full Semester (15–16 Weeks)
### v2 — Revised for Python / HTML / Streamlit Focus, 24 Students

---

## Course Description

This course builds pre-service EFL/ESL teachers' practical digital literacy through hands-on creation: computational thinking, basic Python programming, basic HTML, and deploying interactive applications with Streamlit. Students apply each new skill directly to language-teaching contexts (vocabulary tools, text tools, simple learning-material webpages), culminating in a **deployed Streamlit application** as their final project.

This version assumes **no prior pedagogical training** — theoretical frameworks (TPACK/SAMR/DigComp comparisons, multiliteracies theory in depth) are trimmed to brief framing rather than standalone units, since building technical fluency is the priority. A few short readings from standard digital-literacy-in-language-education journals are retained to give students a shared vocabulary and a sense of the field, not as a theory-heavy strand.

## Course Goals

By the end of this course, students will be able to:

1. Apply computational thinking (decomposition, pattern recognition, abstraction, algorithms) to simple programming tasks.
2. Write basic Python scripts (variables, control flow, functions, string/text processing) applied to language-teaching materials.
3. Build a basic static webpage using HTML (and light CSS).
4. Turn a Python script into an interactive, deployed web application using Streamlit.
5. Critically evaluate digital and AI tools for language teaching, and reason about equity/access issues in ed-tech.
6. Independently debug and troubleshoot their own code — a practical, lightweight form of metacognitive monitoring.

## Class Size Note (24 students)

- Final project is done in **pairs** (12 project teams) — keeps live demo time to one class session and halves grading load without lowering technical ambition.
- Weekly labs are individual (auto-checkable / quick to grade: "does it run, does it produce X output").

## Lightweight Reflective Practice (trimmed from a full metacognitive framework)

Rather than a heavy reflective-journal apparatus, each lab includes a **2–3 sentence Debug Log**: *what broke, how you found it, what fixed it.* This is a natural fit for coding (not an add-on) and still builds the habit of monitoring one's own understanding — just without extra grading burden.

---

## Weekly Schedule (Trimmed & Rearranged)

| Week | Topic | What Students Do | Cut/Condensed From v1 |
|---|---|---|---|
| 1 | Course Intro & What "Digital Literacy" Means | Brief framing (practical, not theory-heavy); preview the final Streamlit app target so students see the destination early | Framework deep-dive (TPACK/SAMR/DigComp comparison) cut to one slide |
| 2 | Computational Thinking + Python Setup | Decomposition/pattern/abstraction/algorithm basics; set up Python (Google Colab recommended — no local install issues) | — |
| 3 | Python Basics I | Variables, data types, input/output → build a simple vocabulary flashcard script | — |
| 4 | Python Basics II | Conditionals & loops → build a simple self-grading quiz script | — |
| 5 | Python & Text | Strings, lists, reading files → build a word-frequency counter / text simplifier for reading materials | Combines old "digital reading" + "digital writing tools" weeks into one applied lab |
| 6 | Functions & Code Organization | Refactor Weeks 3–5 scripts into reusable functions — sets up for Streamlit later | — |
| 7 | HTML Basics | Structure, tags → build a simple class materials webpage | — |
| 8 | HTML + Light CSS | Styling, simple forms/embeds | — |
| 9 | Intro to Streamlit | Convert a Python script into a running Streamlit app; first deploy | Old "LMS/classroom management" week cut entirely |
| 10 | Streamlit Components | Input widgets, layout, session state → build an interactive language-learning tool | Old "digital assessment tools (Kahoot/Quizizz)" week cut — Streamlit subsumes this |
| 11 | Polishing & Deploying | UI cleanup, peer testing, deployment via Streamlit Community Cloud | Old MALL and multimedia/storytelling weeks cut — can be offered as optional extensions, not core weeks |
| 12 | AI Tools in English Education | Critical/ethical use of AI writing tools & chatbots; prompt literacy; tie to assigned reading | — |
| 13 | Information & Media Literacy | Evaluating online sources, misinformation — condensed to one week | Old "digital citizenship" week merged in |
| 14 | Digital Equity & Access | Short unit on the digital divide in language-learning contexts (ties to Warschauer reading) | Condensed from a full week to close with project work starting |
| 15 | Project Studio Time | Build/debug time in class, peer testing in pairs | — |
| 16 | Final Presentations | Live demo of deployed Streamlit apps + 1-paragraph reflection per team | — |

**What got fully cut, not just trimmed:** deep multiliteracies theory, framework comparison (TPACK/SAMR/DigComp side-by-side), CMC/telecollaboration as a standalone week, MALL as a standalone week, digital storytelling/multimedia production as a standalone week, LMS/classroom-management tools, and dedicated digital-assessment-tool exploration (Kahoot/Quizizz). These can live as an optional "further exploration" handout rather than class time, if you want to preserve them for interested students.

---

## Assessment Plan (Trimmed)

| Component | Weight | Description |
|---|---|---|
| Weekly Labs + Debug Logs (Weeks 2–11) | 30% | Completion-based: does the script/page run and do what's asked, plus 2–3 sentence debug log |
| Reading Responses (x2) | 10% | Short (half-page) responses to 2 assigned readings from the list below |
| Midterm Check | 15% | Small individual Python script + simple HTML page, done in class — checks fundamentals before the Streamlit unit |
| Final Project: Deployed Streamlit App (pairs) | 35% | A working, deployed language-learning tool (e.g., vocabulary quiz, text simplifier, flashcard app) |
| Final Presentation + Reflection | 10% | 5-minute live demo + one-paragraph team reflection on what they'd improve |

---

## Reading List (Manageable, Standard Journals, with DOIs)

Kept deliberately short — enough to give a shared vocabulary in the field, not a literature-review course. All are from established, widely-cited journals in digital literacy / language education / computing education.

1. New London Group. (1996). A pedagogy of multiliteracies: Designing social futures. *Harvard Educational Review, 66*(1), 60–92. https://doi.org/10.17763/haer.66.1.17370n67v22j160u
   *(Week 1 — foundational framing of "literacy" beyond print, kept brief but worth knowing as the field's origin point.)*

2. Wing, J. M. (2006). Computational thinking. *Communications of the ACM, 49*(3), 33–35. https://doi.org/10.1145/1118178.1118215
   *(Week 2 — short, canonical, sets up the whole Python unit.)*

3. Coiro, J., & Dobler, E. (2007). Exploring the online reading comprehension strategies used by sixth-grade skilled readers to search for and locate information on the Internet. *Reading Research Quarterly, 42*(2), 214–257. https://doi.org/10.1598/RRQ.42.2.2
   *(Week 5 — pairs with the text-processing Python lab.)*

4. Warschauer, M. (2002). Reconceptualizing the digital divide. *First Monday, 7*(7). https://doi.org/10.5210/fm.v7i7.967
   *(Week 14 — open access, short, grounds the equity discussion.)*

5. Godwin-Jones, R. (2022). Partnering with AI: Intelligent writing assistance and instructed language learning. *Language Learning & Technology, 26*(2), 5–24. https://doi.org/10.64152/10125/73474
   *(Week 12 — open access, directly relevant to AI writing tools.)*

6. Koç, F. Ş., & Savaş, P. (2025). The use of artificially intelligent chatbots in English language learning: A systematic meta-synthesis study of articles published between 2010 and 2024. *ReCALL, 37*(1), 4–21. https://doi.org/10.1017/S0958344024000168
   *(Week 12 — recent, well-known CALL journal, gives a research-based overview of chatbot use in ELT.)*

**Suggested reading response pairing (pick 2 of the 6):** #2 (before the Python unit), #5 or #6 (before the AI week), #4 (before the equity week) — these three moments are where a short reading adds the most without slowing down the technical pace.

---

## Notes for Adaptation

- **Python environment**: Google Colab is recommended over local installs to avoid setup issues across 24 students' varied laptops — no install troubleshooting eats into lab time.
- **Streamlit deployment**: Streamlit Community Cloud is free and connects directly to GitHub — worth a short "GitHub basics" pass in Week 9 if students haven't used version control before (10–15 minutes is usually enough for this course's purposes).
- **Pair assignment for final project**: consider pairing by rough skill level (not all-strong or all-weak pairs) so debugging labor is shared reasonably.
- **If you want to preserve any of the cut content** (MALL, digital storytelling, CMC, assessment tools), the cleanest way is a single "digital tools showcase" week where students briefly explore one tool of their choice and share a 2-minute finding with the class — keeps breadth without a dedicated deep-dive week.

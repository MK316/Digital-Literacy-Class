# Mini-project guidelines

* Group meeting: 10/22 (3 hrs)
* Location: 1층 미래교육센터 및 강의실 (e.g., 334)

❤️ Note: Group leader should upload a photo at the start and the end of your meeting, specifying locations, participants, and your activities. [Padlet]()

# To do

## 1. Read & Share (30 mins)

+ [Webb 2007: Vocabulary learning](https://github.com/MK316/Digital-Literacy-Class/blob/main/pages/Webb2007.md)
+ [Nakata et al. 2021](https://github.com/MK316/Digital-Literacy-Class/blob/main/pages/Nakata2021.md)

## 2. 2022년 교육과정 기본어휘 (20 mins)
+ Check the word list: what it is, how it is organized, how levels are marked, what kind of information is included in the list.
+ You don't need to work with this list yet. Just check out and get familiarize yourself with the list.
+ Choose 10 words to use for your mini-app that can help learners study and practice the words.

## 3. Design your vocabulary application (with the 10 chosen words as sample) (130 mins)

> Goal: Build a **first draft** of a vocabulary web app (`index.html`) using generative AI, with your 10 words as sample data.
> You will connect the data to the full 3,000-word list later. For now, focus on **what learners do** and **why it helps them learn**.

### 💦 Step 1. Discuss: Who, what, and how? (25 mins)

Answer these questions as a group. Write your answers down; you will use them in Step 4.

---
#### 참고: Korean school levels and U.S. grade equivalents (K–12)

Korean grade levels correspond directly to U.S. grade numbers. School divisions differ, however: in the U.S., middle school usually covers Grades 6–8 and high school Grades 9–12, so Korean middle school 3rd year (Grade 9) is the first year of U.S. high school (freshman).

| Korean school | Korean grade | U.S. grade (K–12) | Typical age |
|---|---|---|---|
| Elementary school (초등학교) | 1–6 | Grades 1–6 | 6–12 |
| Middle school (중학교) | 1–3 | Grades 7–9 | 12–15 |
| High school (고등학교) | 1–3 | Grades 10–12 | 15–18 |
---

+ **Learners**: Who will use the app? (e.g., K6, K9, K12, adult beginners, etc.)

+ **Goal**: What should learners be able to do after using the app?
  + Recognize the meaning? Spell the word? Use it in a sentence? Know its word family?
+ **Learning activities**: How will learners meet and practice the words? Connect your ideas to the readings:
  + How many times, and in what kinds of contexts, will learners encounter each word? (Webb 2007)
  + Will learners **retrieve** the word (recall it from memory), not just see it again? When and how often? (Nakata et al. 2021)
+ **Use of the list information**: How will your app use the Level, Word-family, and Variation information?

### 💦 Step 2. Decide and share your features (15 mins)

+ Choose **3–4 core features** only. Keep it small enough to build today.
+ Examples:
  + Flashcards (word → meaning, meaning → word)
  + Multiple-choice or fill-in-the-blank quiz
  + Spelling practice with feedback
  + Word-family matching (e.g., *act* → *actual, interact*)
  + Example sentences with the target word highlighted
  + Score, progress bar, or "review again" list for missed words
+ For each feature, write one sentence: **"This feature helps learners ___ because ___."**
+ ✅ Post your feature list on [Padlet]() before moving on.

### 💦 Step 3. Prepare your 10-word sample data (15 mins)

Make a table of your 10 words. Include the information from the list plus anything your features need.

| Word | Word-family | Variation | Level | Meaning (Korean) | Example sentence |
|---|---|---|---|---|---|
| act | actual, interact | NA | Elementary (*) | 행동하다 | They acted quickly to help. |
| ... | | | | | |

+ Use **NA** for empty cells, as in the word list.
+ Write the meanings and example sentences **yourselves**, or check carefully if AI writes them. AI can make mistakes.

### 💦 Step 4. Write your prompt and generate the app (30 mins)

Copy the template below, fill in the blanks with your answers from Steps 1–3, and give it to a generative AI tool (e.g., ChatGPT, Claude, Gemini).

> Create a vocabulary learning web app as a **single `index.html` file** (HTML, CSS, and JavaScript all in one file, no external server or database).
>
> **Learners**: [who]
> **Learning goal**: [what learners should be able to do]
> **Features**:
> 1. [feature 1 and how it works]
> 2. [feature 2 and how it works]
> 3. [feature 3 and how it works]
>
> **Word data**: Use the 10 words below. Store them in a JavaScript array at the top of the code so we can easily replace it with more words later.
> [paste your table from Step 3]
>
> **Design**: [e.g., simple and colorful, large buttons, mobile-friendly, Korean instructions]

+ Save the result as `index.html` and open it in a web browser (Chrome recommended).
+ Tip: Keep the word data in **one place** in the code. This will make it easy to connect the full 3,000-word list later.

### 💦 Step 5. Test and improve (30 mins)

Take turns using the app **as a learner**. Check:

+ [ ] Do all features work? (Click every button.)
+ [ ] Are all 10 words, meanings, and sentences correct?
+ [ ] Does the app give clear feedback when the answer is right or wrong?
+ [ ] Do learners **retrieve** words, and meet each word **more than once**?
+ [ ] Is it easy to use on a phone?

When something is wrong or missing, ask the AI to fix **one thing at a time**, for example:
> "The quiz shows the same word twice in a row. Please shuffle the questions so each word appears once per round. Give me the full updated index.html."

Save each working version (e.g., `index_v1.html`, `index_v2.html`) so you can go back if something breaks.

### 💦 Step 6. Upload your draft to Padlet (15 mins)

Post the following in **one Padlet post** per group:

1. Group name and members
2. `index_G1.html` file (your latest version, group number G1)
3. 1–2 screenshots of your app
4. Feature list (from Step 2), with one sentence on how each feature supports learning
5. The final prompt you used
6. Next steps: one thing you would add or change in the next version

❤️ Don't forget: Group leader uploads the **end-of-meeting photo** on Padlet.

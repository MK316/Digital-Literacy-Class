# 💦 Group Activity 2: Upgrade and Deploy Your Vocabulary App

**Due by 10:00 PM, November 11, 2026**

---

## 📌 Goal

In the previous activity, your group created a vocabulary app using about **10–20 sample words**.

This time, you will:

1. update your previous app,
2. connect the **full curriculum vocabulary CSV file**,
3. convert or connect it to a **single-page Streamlit app**,
4. deploy the app,
5. submit the final Streamlit link.

이번 활동의 핵심은 **샘플 앱을 실제 데이터와 연결하고 온라인에 배포하는 과정**을 경험하는 것입니다.

---

# ⏰ Before You Start

- Meet with your group for **at least 2 hours**.
- You may choose any meeting time before the deadline.
- Final check time: **10:00 PM, November 11**

### Today’s workflow

```text
1. Open your previous project
2. Create README2.md
3. Prepare the CSV file (교육과정 기초어휘 3,000개: 링크는 아래에 있음.)
4. Update the app
5. Build app.py
6. Deploy on Streamlit
7. Test the deployed app
8. Submit the Streamlit link
```

Follow the steps in this order.

---

# Step 1. Open Your Previous Group Project

Start from the vocabulary app your group created before.

Do not start from scratch unless necessary.

As a group, quickly check:

- Which features should stay?
- Which features need improvement?
- Is the app still appropriate for your target learners?
- Does the app still match your learning goal?

기존 앱에서 잘 작동했던 부분은 그대로 유지하고, 필요한 부분만 수정하세요.

---

# Step 2. Create `README2.md` First

Before changing the app, create a new file:

```text
README2.md
```

Do **not** delete the original `README.md`.

이번에는 `README2.md`를 처음부터 만들어 두고, 활동을 진행하면서 조금씩 채우면 됩니다.

Use this structure:

```markdown
# Group Vocabulary App — Streamlit Version

## 1. Group Information
- Group:
- Members:
- Project link: (e.g., [https://github.com/mk316](https://github.com/mk316))

## 2. Target Learners
Who is this app designed for?

## 3. Learning Goal
What should learners practice or learn?

## 4. What We Updated
Write what you changed from the first version.

## 5. Main Features
List the main 3–4 features.

## 6. Vocabulary Data
Explain how the app uses the CSV file.

## 7. What We Learned Through This Group Activity
Write 2–4 sentences.

## 8. Streamlit App
[Open our Streamlit app](YOUR_STREAMLIT_URL)
```

At this point, fill in only what you already know.

You can complete Sections 4–8 later.

---

# Step 3. Prepare the Vocabulary CSV File

Your previous app used about **10–20 sample words**.

Now, connect the app to the **full curriculum vocabulary dataset**.

### Resources

💾 [Vocabulary file](https://github.com/MK316/Digital-Literacy-Class/blob/main/assets/English_Basicvoca.pdf)

📌 [How to get a CSV file from an XLSX file 엑셀통합문서](https://github.com/MK316/Digital-Literacy-Class/blob/main/projects/csvfiles.md)

### Important

The final app should use a CSV file such as:

```text
vocabulary.csv
```

Because your data may contain both English and Korean, save the file as:

```text
CSV UTF-8
```
Your app may:

- randomly select words,
- select words by level,
- make a practice set,
- generate a quiz,
- filter vocabulary for a specific learner group.

The important point is that the app now uses the **full CSV dataset**.

---

# Step 4. Update Your App

Now revise your previous vocabulary app.

Keep the useful features from the first version.

For example:

- flashcards
- quiz
- spelling practice
- example sentences
- word-family practice
- score or review list

기능을 너무 많이 추가하려고 하지 마세요.

이번 활동에서는 **기존 학습 목표를 유지하면서 전체 CSV 데이터를 연결하는 것**이 더 중요합니다.

As you update the app, also update:

```text
README2.md
→ 4. What We Updated
→ 5. Main Features
→ 6. Vocabulary Data
```

---

# Step 5. Create the Streamlit Version

For this assignment, build only a **single-page Streamlit app**.

Multipage apps will be covered later.

Your project may look like this:

```text
G1_miniproject/
│
├── app.py
├── vocabulary.csv
├── requirements.txt
├── README.md
└── README2.md
```

### Important

`app.py` is the main Streamlit file.

You do **not** need a `pages` folder for this activity.

Your previous app was mainly HTML/CSS/JavaScript.

You may:

- rebuild the main features using Streamlit,
- reuse useful HTML content,
- simplify some features,
- improve the mobile interface.

기존 HTML 앱을 완전히 똑같이 복제할 필요는 없습니다.

---

# Step 6. Deploy the App

Deploy `app.py` using Streamlit Community Cloud.

Before deployment, make sure the repository contains all necessary files.

For example:

```text
app.py
vocabulary.csv
requirements.txt
README2.md
```

개인 컴퓨터에만 있는 파일은 Streamlit Cloud에서 사용할 수 없습니다.

Your final URL will look similar to:

```text
https://your-app-name.streamlit.app
```

When deployment is complete, add the URL to:

```text
README2.md
→ 8. Streamlit App
```

---

# Step 7. Test the Deployed App

Every group member should test the **actual Streamlit link**.

Check:

- [ ] Does the CSV file load correctly?
- [ ] Does the app use the full dataset?
- [ ] Do the main features work?
- [ ] Are answers and feedback correct?
- [ ] Does the app still work after refreshing?
- [ ] Can another group member open the link?
- [ ] Does it work reasonably well on a smartphone?

특히 한 사람의 컴퓨터에서만 작동하는지 확인하지 말고, **다른 조원의 기기에서 실제 배포 링크를 열어 보세요.**

If something fails, fix one problem at a time.

Example:

```text
My Streamlit app reads vocabulary.csv,
but the quiz repeats the same word too often.

Please revise app.py so that each round
uses 10 different words.

Give me the complete updated app.py.
```

---

# Step 8. Finish `README2.md`

Before submission, complete all sections in `README2.md`.

Especially check:

- What did you update?
- How does the app use the CSV data?
- What are the main features?
- What did your group learn?
- Is the final Streamlit URL included?

Keep the file short and clear.

---

# Step 9. Submit the Final Link

Submit **one Streamlit URL per group** to the Google Sheet.

### 🔗 Google Sheet

**[Google Sheet link](https://docs.google.com/spreadsheets/d/1knnx8Om_gb21AjS6Aa6lGv_dyU-sNAGOMHCcX6vupiQ/edit?usp=sharing)**

Before submitting, confirm:

- the app is public,
- the link works,
- `README2.md` is complete,
- the CSV file is in the repository,
- the deployed version is the final version.

---

# ✅ Final Checklist

Before **10:00 PM on November 11**:

- [ ] We worked together for at least 2 hours.
- [ ] We started from our previous vocabulary app.
- [ ] We created `README2.md` early and updated it during the activity.
- [ ] We connected the full vocabulary CSV dataset.
- [ ] We created a single-page Streamlit app.
- [ ] Our `app.py` works.
- [ ] Our `requirements.txt` is ready.
- [ ] Every group member tested the deployed app.
- [ ] The Streamlit URL works.
- [ ] We submitted the final link.

---

## 🌱 Project Flow

```text
Previous HTML prototype
        ↓
Create README2.md
        ↓
Prepare full CSV data
        ↓
Update the app
        ↓
Build app.py
        ↓
Deploy to Streamlit
        ↓
Test
        ↓
Submit
```

이번 활동은 새로운 앱을 처음부터 만드는 것이 아니라, **기존 프로토타입을 실제 데이터와 연결하고 배포 가능한 형태로 발전시키는 과정**입니다.

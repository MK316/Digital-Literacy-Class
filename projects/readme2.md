# 💦 Group Activity 2 (Due by 10PM, Nov. 11)

Upgrade and Deploy Your Vocabulary App

## 📌 Goal

In the previous group activity, your team designed a simple vocabulary-learning app using about **10–20 sample words** from the 2022 National Curriculum Basic English Vocabulary List.

This time, your goal is to **upgrade your group app using the full vocabulary dataset** and deploy it as a **single-page Streamlit app**.

이전에는 10–20개의 샘플 단어로 앱의 기능과 디자인을 먼저 확인했다면, 이번에는 **교육과정 기초어휘 전체 CSV 파일을 연결하여 앱을 확장**하는 것이 핵심입니다.

> **Final product:** One working Streamlit app with a shareable URL.

---

## ⏰ Schedule & Deadline

- Work with your group for **at least 2 hours**.
- You do **not** need to meet during a fixed class period.
- Group members may choose a convenient time to meet and work together.
- Complete the project by:

### **Wednesday, November 11, 2026**

I will check the submitted apps at:

### **10:00 PM on November 11**

조별로 편한 시간을 정해서 만나면 됩니다.  
단, 최소 2시간 이상 함께 작업하고, **11월 11일 오후 10시 이전까지 최종 링크가 정상적으로 열리도록** 준비하세요.

---

# 1. Start from Your Previous Group App

Use the vocabulary app your group created during the previous activity.

Your previous version used approximately **10–20 sample words** to test your ideas and features.

이번 활동에서는 처음부터 새로운 앱을 만들기보다, **기존에 만든 앱을 바탕으로 확장하는 것**을 권장합니다.

First, discuss:

- Which features should remain?
- Which features need improvement?
- Does the app still match your original learner group?
- Does the app still support the learning goal you selected?
- Is the interface easy to use?

기존 앱에서 잘 작동했던 기능은 그대로 유지하고, 필요한 부분만 수정하세요.

---

# 2. Replace the Sample Vocabulary with the Full CSV Dataset

In the previous version, your vocabulary was written directly inside the HTML file.

Now, use the **full curriculum vocabulary dataset provided as a CSV file**.

### 가장 중요한 변화

이전:

```text
10–20 sample words
```

이번:

```text
Full curriculum vocabulary CSV file
```
💾 [Vocabulary file](https://github.com/MK316/Digital-Literacy-Class/blob/main/assets/English_Basicvoca.pdf)

Your app should now read vocabulary data from the CSV file rather than depend only on the original sample words.

### Check that your app can:

- load the CSV file correctly
- access vocabulary entries
- use the information needed for your learning activities
- select or display words appropriately
- continue to work with a much larger dataset

전체 3,000개 단어를 한 화면에 모두 보여줄 필요는 없습니다.

For example, your app may:

- randomly select words
- select words by level
- create a practice set
- allow users to choose a level
- generate a quiz from selected words

중요한 것은 **앱이 전체 CSV 데이터와 연결되어 있고, 필요한 단어를 그 안에서 선택해서 사용하는 구조**가 되는 것입니다.

---

# 3. Convert the Project into a Streamlit App

Before this group activity, you will learn how to deploy a simple Streamlit application.

For this assignment, use only a **single-page Streamlit app**.

### 이번 과제에서는 멀티페이지 앱을 만들지 않습니다.

Multipage Streamlit apps will be covered **after this group activity**.

A simple project structure may look like this:

```text
G1_miniproject/
│
├── app.py
├── vocabulary.csv
├── requirements.txt
├── README.md
└── README2.md
```

Your filenames may be slightly different depending on your project.

### Important

`app.py` should be the main file that Streamlit runs.

`pages` 폴더는 이번에는 만들지 않아도 됩니다.

---

# 4. Connect or Rebuild Your HTML App in Streamlit

Your previous project was mainly created as an HTML/CSS/JavaScript application.

Now you need to make the final version accessible through **Streamlit**.

You may:

- recreate the main functions with Streamlit widgets
- simplify some features if needed
- display useful HTML content inside Streamlit
- improve the interface for mobile use

기존 HTML 앱의 기능을 모두 똑같이 복제하려고 할 필요는 없습니다.

**학습 목표와 핵심 기능이 유지되는 것**이 더 중요합니다.

For example:

```text
Old HTML app
    ↓
Keep the useful features
    ↓
Connect CSV data
    ↓
Build app.py
    ↓
Deploy with Streamlit
```

---

# 5. Test the Updated App

Every group member should test the app.

Check the following:

- [ ] Does the CSV file load correctly?
- [ ] Does the app work with the full vocabulary dataset?
- [ ] Do all buttons and activities work?
- [ ] Are vocabulary items displayed correctly?
- [ ] Are answers and feedback correct?
- [ ] Does the app work after refreshing the page?
- [ ] Is the interface understandable for your target learners?
- [ ] Can the app be used reasonably well on a smartphone?
- [ ] Does the Streamlit link open on another person's device?

### 테스트할 때 중요한 점

한 사람의 컴퓨터에서만 되는 것으로 끝내지 마세요.

다른 조원이 실제 Streamlit 링크를 열어서 테스트해 보세요.

특히:

- CSV가 GitHub에 제대로 올라가 있는지
- 개인 컴퓨터의 파일 경로를 사용하고 있지 않은지
- 새로고침 후에도 작동하는지

확인하세요.

If something does not work, fix **one problem at a time**.

For example:

```text
My Streamlit app reads vocabulary.csv, but the quiz repeats
the same word too often.

Please revise the code so that 10 different words are selected
for each quiz round.

Give me the complete updated app.py file.
```

AI에게 한 번에 여러 문제를 고쳐 달라고 하기보다, **한 문제씩 구체적으로 요청하는 것이 더 효과적**입니다.

---

# 6. Create `README2.md`

Create a new file in your group repository:

```text
README2.md
```

Do **not** delete your original `README.md`.

원래의 `README.md`는 첫 번째 프로젝트의 설계 과정과 활동 내용을 기록한 파일입니다.

이번에는 업데이트된 Streamlit 앱을 간단히 소개하는 **새로운 `README2.md`**를 작성하세요.

Your `README2.md` should include at least the following sections:

```markdown
# Group Vocabulary App — Streamlit Version

## 1. Group Information
- Group:
- Members:

## 2. Target Learners
Who is this app designed for?

## 3. Learning Goal
What should learners practice or learn through the app?

## 4. What We Updated
Briefly explain how this version is different from the first HTML version.

Examples:
- Connected the full vocabulary CSV dataset
- Added random word selection
- Revised the quiz
- Improved mobile layout
- Converted the app to Streamlit

## 5. Main Features
Briefly describe the main 3–4 features.

## 6. Vocabulary Data
Explain how the app uses the curriculum vocabulary CSV file.

## 7. What We Learned
Write 2–4 sentences about what your group learned while converting and deploying the app.

## 8. Streamlit App
[Open our Streamlit app](YOUR_STREAMLIT_URL)
```

### README2.md 작성 시 주의

길게 작성할 필요는 없습니다.

각 항목을 **간단하고 깔끔하게** 정리하세요.

특히 다음 세 가지는 반드시 포함하세요.

- 무엇이 업데이트되었는가
- CSV 데이터를 어떻게 사용했는가
- 최종 Streamlit 링크

---

# 7. Deploy the App

Deploy your `app.py` from your group's GitHub repository using Streamlit Community Cloud.

Before submission:

1. Open the deployed app.
2. Refresh the page.
3. Test the main activities.
4. Ask another member to open the link.
5. Test the app on a smartphone if possible.

Your final URL will look similar to:

```text
https://your-app-name.streamlit.app
```

### 꼭 확인할 것

Streamlit Cloud에서 배포할 때는 GitHub 저장소 안에 필요한 파일이 모두 있어야 합니다.

예:

```text
app.py
vocabulary.csv
requirements.txt
README2.md
```

개인 컴퓨터에만 있는 파일은 Streamlit Cloud에서 사용할 수 없습니다.

---

# 8. Submit Your Final Link

When your group is finished, submit the **Streamlit app URL** to the Google Sheet below.

### 🔗 Google Sheet

**[Google Sheet link](https://docs.google.com/spreadsheets/d/1knnx8Om_gb21AjS6Aa6lGv_dyU-sNAGOMHCcX6vupiQ/edit?usp=sharing)**

Only **one final link per group** is necessary.

조별로 최종 링크 하나만 제출하면 됩니다.

Before submitting, make sure that:

- the Streamlit app is public and accessible
- the correct version has been deployed
- `README2.md` is available in the group GitHub repository
- the CSV file needed by the app is available in the repository
- the app works without requiring files from an individual member's computer

---

# ✅ Final Checklist

Before November 11, check:

- [ ] We worked together for at least 2 hours.
- [ ] We used our previous vocabulary app as the starting point.
- [ ] We connected the full curriculum vocabulary CSV dataset.
- [ ] We created a **single-page** Streamlit app.
- [ ] Our `app.py` works correctly.
- [ ] Our `requirements.txt` includes the necessary libraries.
- [ ] We created `README2.md`.
- [ ] Every group member tested the app.
- [ ] The Streamlit URL works.
- [ ] We submitted the URL to the Google Sheet.

---

# 🌱 From Prototype to Application

Your first project was a **prototype**.

이번 프로젝트는 그 프로토타입을 실제로 확장하고 배포하는 단계입니다.

```text
Sample vocabulary
      ↓
HTML prototype
      ↓
Full CSV vocabulary data
      ↓
Streamlit application
      ↓
Online deployment
```

The goal is not simply to make a larger app.

이번 활동의 핵심은 작은 아이디어를 **데이터와 연결하고, 수정하고, 테스트하고, 온라인에 배포하는 전체 과정**을 경험하는 것입니다.

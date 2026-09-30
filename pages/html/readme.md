# 💻 Hands-on Activity: My First HTML App

### Creating and Modifying an English Vocabulary Quiz

**Learning Goal:** In this activity, you will create a simple English vocabulary quiz using HTML, CSS, and JavaScript. You do not need any previous programming experience.

Our goal is not to become programmers. Instead, we will learn how to understand, modify, and test a simple learning app. We will also explore how AI can help us modify the app based on our instructional decisions.

By the end of this activity, you should be able to:
- Identify the basic roles of HTML, CSS, and JavaScript.
- Modify an existing HTML file.
- Make simple decisions about the design of an English learning app.
- Use AI to modify the app and test whether the changes work as intended.

---

## STEP 1. Create Your First HTML App

First, we will create a simple English vocabulary quiz. You will use three components:

| Component | Main Function | Question |
|---|---|---|
| HTML | Content and structure | What do learners see? |
| CSS | Appearance and design | How does the app look? |
| JavaScript | Interaction and behavior | What happens when learners respond? |

### Task 1: Create an index.html file

1. Open your GitHub repository.
2. Create a new file named `index.html`.
3. Copy the following code and paste it into your file.
4. Commit the changes.

**Sample Code**

```html
<!DOCTYPE html>
<html>

<head>
    <title>My First English Learning App</title>

    <!-- CSS: Change how the app looks -->
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin: 50px;
        }

        button {
            font-size: 20px;
            padding: 12px;
            margin: 5px;
            background-color: lightblue;
        }
    </style>
</head>

<body>

    <!-- HTML: Change what learners see -->

    <h1>Vocabulary Quiz</h1>

    <p>What does "take part in" mean?</p>

    <button onclick="checkAnswer('participate')">
        Participate in
    </button>

    <button onclick="checkAnswer('avoid')">
        Avoid
    </button>

    <button onclick="checkAnswer('watch')">
        Watch
    </button>

    <h3 id="feedback"></h3>


    <!-- JavaScript: Change what happens -->

    <script>

        function checkAnswer(answer) {

            if (answer === "participate") {
                document.getElementById("feedback").innerText =
                    "Correct! Well done!";
            }

            else {
                document.getElementById("feedback").innerText =
                    "Incorrect. The answer is Participate in.";
            }

        }

    </script>

</body>
</html>
```

### Task 2: Run your app

Open your `index.html` file in a web browser. You can download the file from GitHub and open it locally or use GitHub Pages if it is configured for your repository.

Check the following:

- Does the title appear correctly?
- Can you see the three answer buttons?
- What happens when you click the correct answer?
- What happens when you click an incorrect answer?

**Remember:** Whenever you modify the code, save your changes and refresh the browser to see the results.

---

## STEP 2. Modify HTML: Change What Learners See

HTML determines the content and structure of your app.

In this step, we will modify the quiz to make it more appropriate for our target learners.

### Task 3: Change the quiz content

Find the following HTML code:

```html
<h1>Vocabulary Quiz</h1>

<p>What does "take part in" mean?</p>
```

Change the quiz title to:

**Phrasal Verb Challenge**

Then, replace the question with another English expression you would like to teach.

You can also modify the answer buttons.

**Important:** If you change the correct answer, remember that the JavaScript code must also recognize your new answer. We will practice modifying JavaScript later.

### Discussion

Before moving on, consider the following questions:

1. Who are your target learners?
2. Is the vocabulary appropriate for their proficiency level?
3. Are the instructions clear enough for your learners?

Changing the content should reflect your instructional decisions rather than simply your personal preferences.

---

## STEP 3. Modify CSS: Change How the App Looks

CSS controls the visual appearance of your app.

In our current code, the buttons are light blue.

### Task 4: Change the button design

Find this CSS code:

```css
button {
    font-size: 20px;
    padding: 12px;
    margin: 5px;
    background-color: lightblue;
}
```

Try the following modifications:

1. Change `font-size` from `20px` to `26px`.
2. Change `background-color` from `lightblue` to `lightgreen`.
3. Increase the `padding` from `12px` to `18px`.

Save your changes and refresh the browser.

### Discussion

Compare your original design with the modified version.

- Which version is easier to use?
- Would larger buttons benefit your target learners?
- Does changing the button color contribute to learning?

**Remember:** A design change is useful when it improves the learning experience.

---

## STEP 4. Modify JavaScript: Change What Happens

JavaScript controls the behavior of your app.

For example, it determines what happens when learners click an answer button.

### Task 5: Modify the feedback

Find the following JavaScript code:

```javascript
if (answer === "participate") {
    document.getElementById("feedback").innerText =
        "Correct! Well done!";
}

else {
    document.getElementById("feedback").innerText =
        "Incorrect. The answer is Participate in.";
}
```

Currently, the app immediately reveals the correct answer when learners make a mistake.

First, make a simple change.

Replace:

```javascript
"Incorrect. The answer is Participate in.";
```

with:

```javascript
"Not quite! Think carefully and try again.";
```

Save your changes and test the app.

### Discussion

What changed?

The app now provides encouraging feedback instead of immediately revealing the answer.

However, the actual learning process has not changed very much.

We have changed the wording of the feedback, but we have not yet implemented a different feedback strategy.

---

## STEP 5. Use AI to Change the Learning Logic

Now we will make a more meaningful modification.

Imagine that you are designing this app for students who need additional opportunities to practice vocabulary.

You decide that the app should work as follows:

| Learner Response | App Behavior |
|---|---|
| Correct answer | Display positive feedback |
| First incorrect answer | Provide a contextual hint |
| Second incorrect answer | Reveal the correct answer and provide an explanation |

This is an instructional decision because it changes how learners receive feedback and how many opportunities they have to respond.

### Task 6: Ask AI to modify your code

Copy your entire `index.html` code and provide it to ChatGPT with the following prompt:

**AI Prompt**

> Modify the feedback logic in this HTML app.
>
> When learners choose an incorrect answer for the first time, provide a short contextual hint without revealing the correct answer.
>
> Allow learners to try again.
>
> If they choose an incorrect answer a second time, show the correct answer with a brief explanation.
>
> Keep the rest of the app unchanged.
>
> Provide the complete revised index.html code.

Replace your existing code with the revised code provided by AI.

Save the file and run your app again.

### Task 7: Inspect the AI-generated code

Before testing the app, examine the new JavaScript code.

Look for the following elements:

- `attempts`: A variable that counts how many times learners have attempted the question.
- `if`: A condition that determines what happens when a learner responds.
- `else`: A condition that handles alternative responses.
- `feedback`: The message displayed to learners.

You do not need to understand every line of code.

Instead, identify the parts that implement your instructional decision.

---

## STEP 6. Test and Debug Your App

AI-generated code does not necessarily work correctly.

As teachers designing learning applications, we must examine whether the app functions as intended.

### Task 8: Test your app

Test the following situations.

| Test | Expected Result |
|---|---|
| Select the correct answer | Positive feedback appears |
| Select an incorrect answer once | A contextual hint appears |
| Select an incorrect answer twice | The correct answer and explanation appear |

If something does not work, inspect your code.

First, check whether you saved the file and refreshed the browser.

Next, examine the code you recently modified.

If you cannot identify the problem, ask ChatGPT for assistance.

**Debugging Prompt**

> My HTML app stopped working after I modified the feedback function.
>
> Identify the likely error, explain it in simple language for a beginner, and make only the smallest necessary correction.
>
> Do not rewrite the rest of the app.

Make one change at a time and test your app after each modification.

---

## STEP 7. Pair Testing

Now exchange your app with another student.

Use your partner's app as if you were an English learner.

Do not examine the code at first. Focus on your experience as a learner.

Discuss the following questions:

1. Did the app function correctly?
2. Were the instructions and feedback easy to understand?
3. Did the hint help you figure out the correct answer?
4. What additional modification would improve the learning experience?

Based on the feedback you receive, identify one improvement you would like to make.

---

## Final Reflection

Before finishing today's activity, reflect on the following questions:

1. What is the difference between modifying HTML, CSS, and JavaScript?
2. How is changing the wording of feedback different from changing the feedback logic?
3. What did you learn about using AI to modify an educational application?

### Today's Key Message

**Decide → Modify → Test → Debug → Improve**

You do not need to memorize every HTML or JavaScript command.

What matters is your ability to make instructional decisions, communicate those decisions to AI, inspect the resulting code, and test whether your app actually supports learning.

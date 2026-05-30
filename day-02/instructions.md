# Day 2 — Build Something Useful

**Duration:** 60 min · **Theme:** You don't want a generic AI. You want one that solves your actual problem.

---

## Today's goal

Write a 2-sentence spec for your project. Build v1 — one real feature that solves an actual problem you have.

---

## The one idea you need

Generic prompts get generic results. Specific prompts get useful results.

The difference between a tool you'd actually use and one you'd close after 10 seconds is almost always the prompt. Today you learn to write prompts that work.

---

## Key concept: the prompt structure

Every good AI prompt has four parts:

| Part | What it does | Example |
|---|---|---|
| **Role** | Tells the AI who it is | "You are a high school study tutor" |
| **Context** | Tells it what situation it's in | "The student is 15, studying for AP US History" |
| **Constraint** | Sets limits on the output | "Use simple language, max 150 words" |
| **Format** | Tells it how to respond | "Return 5 multiple-choice questions with answers" |

You don't need all four every time. But the more specific you are, the more useful the output.

**Before:**
> "You are a helpful assistant."

**After:**
> "You are a high school study tutor who specializes in making complex topics simple. The student is 15 and preparing for a US History AP exam. Use simple language, no jargon, maximum 150 words. Return a 5-question multiple-choice quiz with answers labeled (A) through (D)."

Same model. Completely different output.

---

## Step 1 — Write your 2-sentence spec

Before you write a single line of code, write this:

> **[Tool name]** helps **[who]** do **[what]** by **[how]**. The input is **[what the user gives it]** and the output is **[what comes back]**.

**Example:**
*Study Buddy helps high-schoolers break down complex topics by turning any paragraph into a 5-question quiz. The input is a chunk of text and the output is 5 multiple-choice questions with answers.*

Post your spec in Discord. Wait for a green light before building. If it says "helps people do things better" — it's too vague. Try again.

> ✅ Green light: your spec names a specific person, a specific input, and a specific output.

---

## Step 2 — Build your v1

You'll keep building in `main.py` — the file you started with on Day 1. This is your capstone now. It grows with you for the rest of camp; you don't start a new project each day.

Tell Replit Agent what you're building:

> "I'm building [your tool name]. [Paste your 2-sentence spec.] Rework my main.py and templates/index.html into this tool, with a text input and a submit button. The AI should respond using this system prompt: [paste your role/context/constraint/format prompt]."

Let Agent build it. Click **Run** when it's done.

---

## Step 3 — Iterate the prompt

Your first result probably isn't great. That's expected and normal.

Look at the output and ask:
- Is it the right length?
- Is it the right tone?
- Is it missing something obvious?

Then fix one thing at a time. Tell Agent: *"The output is too long — add a constraint to keep it under 100 words"* or *"It sounds too formal — change the tone to casual and friendly."*

Do at least 2 iterations. The prompt that makes you think "oh this is actually useful" is the one you keep.

---

## Step 4 — Share it

Deploy your v1 and post the link in Discord.

> ✅ Ship proof: live URL in `#day-2-ships` + one sentence describing what your tool does.

---

## Checkpoint

Before you leave today:
- [ ] 2-sentence spec written and approved
- [ ] v1 of your project running with a real prompt
- [ ] At least 2 prompt iterations done
- [ ] Live URL deployed and posted
- [ ] (Bonus) First GitHub push from Day 1 if you haven't done it yet

---

## Homework

Use your tool **3 times** before Day 3. Write down one thing that's annoying about the output. Come ready to say one specific thing you want to fix.

Not "it's bad." Something like: "It always uses bullet points when I want a paragraph" or "The tone is too formal."

---

## You now know

- How to write a 2-sentence spec so you actually know what you're building
- The role/context/constraint/format prompt structure
- Why specific prompts beat generic ones every time
- That prompts almost never work on the first try — and how to iterate

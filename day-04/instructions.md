# Day 4 — Add Intelligence + Midpoint Demo

**Duration:** 60 min build + 60 min optional office hours · **Theme:** Make your tool feel like it's actually thinking.

---

## Today's goal

Add one chained step to your project — so the output of one AI call becomes the input of the next. Give a 60-second live demo of where your project is right now.

---

## The one idea you need

Right now your tool does one thing: input → AI → output. That's good. But the smartest tools do more: they take that output and pass it through another step.

**Chaining** is when the output of one prompt becomes the input of the next. It's how you go from "summarize this" to "summarize this, then turn the summary into a quiz, then score the quiz."

---

## Three chaining patterns (pick one for today)

### Pattern 1 — Refine
Use prompt 1 to generate a draft, then prompt 2 to improve it.

```
Prompt 1: "Draft a 3-sentence summary of this article."
Prompt 2: "Rewrite this summary for a 14-year-old. Remove any jargon."
```

Best for: any tool that produces text that could be cleaner, simpler, or reformatted.

### Pattern 2 — Extract, then act
Use prompt 1 to pull structured info out of messy input, then act on it.

```
Prompt 1: "Extract the key facts from this as a JSON list."
Prompt 2: "For each fact, rate how important it is for a student (1–5) and explain why."
```

Best for: tools that process long input, notes, articles, or anything messy.

### Pattern 3 — Route
Use prompt 1 to classify the input, then pick a different prompt based on the result.

```
Prompt 1: "Is this question about math, history, or science? Reply with one word."
→ if "math": use the math-tutor system prompt
→ if "history": use the history-tutor system prompt
```

Best for: tools that handle more than one type of input.

---

## Build steps

**Step 1 — Pick your pattern**

Look at your project. Which pattern adds the most value?

- If your output could be cleaner or more tailored → **Refine**
- If you're processing long or messy input → **Extract, then act**
- If your tool handles different kinds of questions → **Route**

Post your choice in Discord: *"I'm adding [pattern] because ___."*

**Step 2 — Add the chain**

Tell Replit Agent:

> "I want to add a chained step to my project in main.py. Here's my plan:
> - Step 1: [your existing prompt]
> - Step 2: [new prompt that takes step 1's output as input]
>
> Wire it up so step 1 runs first, then step 2 takes that result and processes it. Show both results to the user, or just the final result — your call on what makes more sense."

Test it. Does the second step actually add value? If not, change the step 2 prompt until it does.

**Step 3 — (Optional) Add basic memory**

If you want your tool to remember context between messages, tell Agent:

> "Add a conversation history list to my app. Each time the user sends a message, append it to the history and pass the full history to the AI. This way the AI remembers what we talked about earlier in the session."

This is how ChatGPT keeps context. It's a list of messages that grows as you chat.

> ⚠️ This stores memory only for the current session — when the page refreshes, it resets. That's fine for now.

---

## Midpoint demo (every student, 60 seconds)

At minute 50, every student shares their screen for 60 seconds:

1. Show your tool running with a real input
2. Show the chained output
3. Say one sentence: "Next week I'm going to add ___"

This isn't a presentation. It's a checkpoint. You get one piece of feedback from the group.

> ✅ Ship proof: midpoint demo completed. Screenshot or recording posted in `#lesson-4`.

---

## Optional office hours (60 min after the main session)

Stay if you want:
- Debug your chaining logic
- Lock in your week 2 direction (what are you building toward for Demo Day?)
- Add persistent memory using Replit Database (saves between sessions — this is the bonus move)

---

## Checkpoint

Before you leave today:
- [ ] One chained step added and working
- [ ] 60-second midpoint demo done
- [ ] Clear direction for what you're building in week 2
- [ ] (Bonus) Conversation memory added

---

## Homework

Think about one repetitive thing you do — or wish you could automate. Write it down:

> "Every [time period], I [action]. If a bot could do this for me, I'd use it every [time period]."

Example: "Every Sunday night, I figure out my homework for the week. If a bot could lay it out for me based on my syllabi, I'd use it every Sunday."

Come to Day 5 ready to build something like that.

---

## You now know

- Three ways to chain prompts to make your tool feel smarter
- How to maintain message history so your tool remembers context within a session
- How to give a 60-second product demo that shows what your tool does (not how it works)
- What "agents" do differently — and what's coming on Day 5

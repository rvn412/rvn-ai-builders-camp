# AI Builders Camp — Starter Template

Welcome to camp. This is your starting point. In two weeks, you'll turn it into a real, deployed AI app that lives at your own link — something you can put on a résumé or a college app.

**Instructor:** Samidha Visai · **Ages:** 13–17 · **Format:** 8 sessions over 2 weeks

---

## Start here (Day 1, ~5 minutes)

1. **Click the green `Run` button** at the top. A simple app called **Explain Anything** opens in the preview window. That's your starter app working.
2. **Connect AI.** Open the **Agent** panel (top right) and type:
   > "Please set up Replit AI so my app can make AI calls."

   This connects your app to AI using your **Replit credits** — no OpenAI account, no API key, no copying secret codes. You do this once.
3. **Click `Run` again** and type something into the app. You should get an AI answer back.
4. **Open `main.py`** and change the `SYSTEM_PROMPT` line to make it yours.

That's it — you're a builder now. Follow `day-01/instructions.md` for the rest.

---

## How this template is organized

```
main.py              ← YOUR APP. The Run button runs this. You grow it all camp.
templates/index.html ← what your app looks like (the web page)
static/style.css     ← your app's colors and styling (you'll make this yours on Day 3)
ai_helper.py         ← your shortcut to AI. Just import ask_ai and use it.

day-01/ ... day-07/  ← one folder per session. Open instructions.md and follow along.
day-05/agent-starter.py ← a working AI agent you'll customize on Day 5

examples/            ← three finished mini-apps to read for ideas
```

You build ONE app across all of camp — it lives in `main.py` and gets better every day. The `day-XX` folders are your lesson guides.

---

## Using AI in your code

Anywhere in your Python code, you can do this:

```python
from ai_helper import ask_ai

answer = ask_ai("Write a haiku about pizza")
print(answer)
```

Want to change the AI's personality? Pass a `system_prompt`:

```python
answer = ask_ai(
    "Tell me about the moon",
    system_prompt="You are a pirate who loves astronomy."
)
```

---

## The 8 days

| Day | You build |
|---|---|
| 1 | Your first AI tool, deployed to a live link |
| 2 | A tool that solves a real problem (with a proper prompt) |
| 3 | A design pass — your app gets a real identity |
| 4 | A smarter, multi-step version + midpoint demo |
| 5 | A working AI agent that uses tools |
| 6 | A pitch, a polished README, and your first users |
| 7 | Final polish + your 60-second demo |
| 8 | Demo Day 🎉 |

---

## Stuck? Three things to try

1. **Ask the Agent.** It can see your code. Describe what's wrong in plain English.
2. **Read the error message.** It usually says which file and line broke.
3. **Post in Discord.** Someone's probably hit the same thing.

You've got this. Let's build.

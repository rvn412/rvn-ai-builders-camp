# Day 5 — Agents + Automation

**Duration:** 60 min · **Theme:** Stop doing it by hand.

---

## Today's goal

Build a working agent from a starter harness — a multi-step program that takes actions, not just answers. Connect it to a trigger: a Run button, a scheduled job, or a bot command.

---

## The one idea you need

Everything you've built so far works like this:
```
user sends input → AI responds → done
```

An agent works like this:
```
trigger → AI thinks → AI asks for a tool → you run the tool → AI sees result → AI thinks again → repeat until done
```

The key difference: **the AI can take multiple steps and use tools.** It's not just answering — it's acting.

The simple shape of every agent:
```
trigger  +  steps  +  tools  +  memory
```

---

## Key vocabulary

| Word | What it means |
|---|---|
| **Agent** | A program that uses an AI + loop + tools to take multiple steps toward a goal |
| **Tool** | A function the AI can ask your code to run — like `get_weather()` or `save_note(text)` |
| **Tool calling** | When the AI says "run this tool with these inputs," you run it, and send the result back |
| **Trigger** | What starts the agent — a button click, a schedule, a bot command, or a message |

---

## The starter agent

Your camp workspace has a starter harness in `day-05/agent-starter.py`. It comes with two tools already wired up:

- `get_time()` — returns the current date and time
- `save_note(text)` — saves a note to a local file

The agent loop is already written. You don't need to build the loop from scratch — you just need to customize the tools.

**Open `day-05/agent-starter.py` and run it.** Watch what happens in the console. You'll see:
1. The trigger fires
2. The AI decides what tools to use
3. Your code runs the tool
4. The AI sees the result and takes the next step

Label each part as you watch it.

---

## Build steps

**Step 1 — Run the starter and understand it**

Click **Run** with `day-05/agent-starter.py` as the entry point. Read the console output. Find where each of these things happens:
- The AI decides to use a tool
- Your code actually runs the tool
- The result goes back to the AI

Ask Agent to explain any part you don't understand: *"What does this line in the tool-calling loop do?"*

**Step 2 — Customize one tool (core path)**

Replace or modify one of the starter tools. Pick something useful:
- `summarize_today(notes)` — takes some text and summarizes it
- `generate_brief(topic)` — generates a short briefing on a topic
- `append_to_log(entry)` — adds a timestamped entry to a log file

Tell Replit Agent:

> "I want to add a tool called [tool name] to my agent in day-05/agent-starter.py. The tool should [what it does]. Wire it up so the AI can decide to use it, and show me the result in the console."

Run it. Does the AI actually use your tool? Does the output make sense?

> ✅ Core path done: an agent that takes multiple steps and produces a real output.

**Step 3 — Pick a trigger (choose your path)**

| Trigger | What it does | Best for |
|---|---|---|
| **Run button** | Agent runs when you click Run | Everyone — do this first |
| **Scheduled run** | Agent runs automatically on a schedule (Replit Deployments) | Morning brief, daily reminders |
| **Discord/Telegram bot** | Agent responds to a command in your chat app | Bot builders |

**Scheduled run (bonus path):**
Tell Agent: *"I want this agent to run automatically every morning at 7am using Replit's scheduled deployments. How do I set that up?"*

**Discord bot (bonus path):**
You'll need a bot token from the Discord Developer Portal. Ask Agent: *"Walk me through creating a Discord bot and connecting it to this agent so it responds to a slash command."* Store the token in Replit Secrets, never in code.

---

## Share

At minute 50, 3–4 students share their screen and show their agent doing one real thing live.

> ✅ Ship proof: agent running with real output posted in `#day-5-ships`. Video or screenshot.

---

## Checkpoint

Before you leave today:
- [ ] Starter agent runs and you understand the loop
- [ ] At least one custom tool added
- [ ] Agent produces a real output (not just "Hello, I am an AI")
- [ ] (Bonus) Connected to a scheduled run or bot command

---

## Rescue path

If bot permissions or scheduled deployment gets complicated, that's fine. Ship a **Run-button agent** that saves to a log file. That still proves you understand the agent pattern. The trigger is the least important part — the loop is everything.

---

## Homework

Run your agent one more time on your own and write down:

> "The tool I'd most want it to have that it doesn't have yet is ___."

Come to Day 6 ready to pitch it. You might build it on Day 7.

---

## You now know

- What an agent is: LLM + loop + tools + memory
- How tool calling works: you give the model tools, it decides when to use them, you run them and send results back
- The difference between answering (what you've done Days 1–4) and acting (what agents do)
- How to connect an agent to a trigger path

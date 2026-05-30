# Day 1 — Your First AI Tool

**Duration:** 60 min · **Theme:** By the end of today, something you built is running live on the internet.

---

## Today's goal

Build a working AI tool in Replit. Type something in, get an AI response back. Deploy it. Share the link.

That's the whole win. Tiny? Fine. Ugly? Fine. **Yours? Required.**

---

## The one idea you need

Every AI tool ever built has the same shape:

```
input  →  AI model  →  output
```

A chatbot: message → model → reply.
A quiz generator: notes → model → questions.
A trip planner: "I have $500 and 3 days" → model → itinerary.

Everything we build for the next 7 days is a remix of this pattern. Keep it in your head.

---

## Key vocabulary

| Word | What it means |
|---|---|
| **LLM** | A program trained on billions of text examples until it learned to predict helpful responses to prompts |
| **API** | A door you knock on with a request — it opens and hands something back |
| **Frontend** | The part of an app users see and interact with |
| **Backend** | The part that runs on a server, handles logic, talks to APIs |
| **Deployed URL** | A live link anyone can open — your app running in the cloud |

---

## What we're building

**"Explain Anything"** — a tool where you type a topic and get a 1-sentence explanation back. Simple, works, yours to customize.

---

## Build steps

**Step 1 — Confirm your starter runs**

Open your camp workspace in Replit. Click **Run**. You should see a welcome screen. If you don't, stop and ask for help before doing anything else.

> ✅ Green light: the starter runs before you touch anything.

**Step 2 — Connect AI (one time, ~30 seconds)**

Click the **Agent** button (top right) and type:

> "Please set up Replit AI so my app can make AI calls."

This connects your app to AI using your Replit credits — no account, no API key. You only do this once.

**Step 3 — Look at your app**

Your starter already includes a working tool called **Explain Anything**. Open `main.py` in the file panel and read it — it's short and commented. This is the app the Run button runs.

**Step 4 — Test it**

Type something into your app. Try: "black holes," "the stock market," "why people get nervous."

> ✅ Tiny change: you changed one input and saw a different output.

**Step 5 — Deploy it**

Click **Deploy** (top right of Replit) → choose **Static** or **Autoscale** → click **Deploy**. You'll get a live URL like `explain-anything.yourusername.repl.app`.

> ✅ Ship proof: post your live URL in `#day-1-ships` in Discord.

---

## Make it yours

Change the system prompt to something you'd actually use. Open `main.py` and find the line that says `SYSTEM_PROMPT`. Replace it with something more interesting:

Ideas to try:
- `"You explain things like a sports announcer calling the play-by-play."`
- `"You explain things like a grumpy history teacher who secretly loves the topic."`
- `"You explain things in exactly 3 bullet points, each under 10 words."`
- Your own idea — what explanation style would you actually use?

Ask Agent if you're not sure how to change it: *"How do I change the SYSTEM_PROMPT in main.py to make the explanation more casual?"*

---

## Checkpoint

Before you leave today, you should have:
- [ ] A working AI tool that responds to input
- [ ] A live deployed URL
- [ ] That URL posted in `#day-1-ships`
- [ ] (Bonus) GitHub first commit if your account is ready

---

## Homework

Brainstorm **3 problems you'd actually want an AI tool to solve** — for you, your family, a hobby, your friend group. Real problems. Not "cure cancer." More like:

- "I always forget when practice is"
- "Picking a movie on Friday nights is a war crime"
- "I need to write an email to my teacher and I don't know how to start"

Post your 3 ideas in Discord tonight. We use them on Day 2.

---

## You now know

- What an LLM is and how it generates responses
- What an API is and how Replit connects to AI models for you
- The universal shape of every AI tool: input → model → output
- How to deploy a live app from Replit

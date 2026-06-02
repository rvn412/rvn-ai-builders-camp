# AI Builders Camp — Starter Template

Welcome to camp. This is your starting point. In two weeks, you'll turn it into a real, deployed AI app that lives at your own link — something you can put on a résumé or a college app.

**Instructor:** Samidha Visai · **Ages:** 13–17 · **Format:** 8 sessions over 2 weeks

---

## Day 1 Setup (~15 minutes total)

Do these steps **in order**. Each one takes 2–3 minutes.

---

### Step 1 — Fork this repo to your own GitHub (2 min)

You need your own copy of this project so your work is saved under your name.

1. Make sure you're signed in to **GitHub** at [github.com](https://github.com)
2. Click **Fork** (top right of this page)
3. In the **Repository name** box, name it after yourself so your instructor can tell projects apart — for example `maya-ai-builders-camp` or `jordan-ai-camp`
4. Click **Create fork**
5. You now have your own copy at `github.com/YOUR-USERNAME/maya-ai-builders-camp`

> **Don't have a GitHub account?** Sign up free at [github.com/signup](https://github.com/signup) — use your real name, this will be your coding portfolio.

---

### Step 2 — Create your Replit account & upgrade to Core (3 min)

AI calls cost credits, and Replit Core gives you the credits you need — so set this up before you import.

1. Go to [replit.com](https://replit.com) and sign in (or sign up free)
2. Replit often offers **Core when you sign up** — if you see that prompt, just upgrade right there
3. Otherwise, click your **profile photo** → **Upgrade to Core**
4. Follow the steps — you'll need a parent's help if you're under 18 (it's the only paid step, ~$20/month, cancel anytime)

> **Already on Core?** Skip ahead to the import.

---

### Step 3 — Import your fork into Replit (2 min)

1. In Replit, click **+ Create Repl** → **Import from GitHub**
2. Paste **your fork's** URL: `https://github.com/YOUR-USERNAME/maya-ai-builders-camp`
3. Click **Import from GitHub** — Replit will set everything up

> ✅ Your Replit is now linked to **your own** GitHub repo. When you push, it goes to your repo — not the original template.

---

### Step 4 — Set up AI (3 min)

This connects your app to a real AI model using your Replit credits. You do this once.

1. Click the **Agent** button (top right of Replit, looks like a sparkle or chat icon)
2. Type exactly this:
   > `Please set up Replit AI so my app can make AI calls.`
3. The Agent will show you an **OpenAI integration** to approve — click **Approve** (not Dismiss!)
4. ⚠️ **Replit may ask you to verify your phone number** — this is a one-time check and required. A parent's phone is fine; Replit only texts once.
5. Wait for Agent to finish — it will say the app is ready

> If you accidentally click **Dismiss** on the integration popup, just type the same message again and approve it the second time.

---

### Step 5 — Run your app and test AI (2 min)

1. Click the green **Run** button at the top
2. The **Explain Anything** app opens in the preview window (right side)
3. Type a topic like `black holes` and click **Explain it →**
4. You should get a real AI answer — not an error message

> ❌ **Still seeing "AI isn't connected yet"?** Go back to Step 4 and ask the Agent again. The error message in the app tells you exactly what to paste if the keys didn't save the first time.

---

### Step 6 — Save your work to GitHub (2 min)

The easiest, most reliable way to back up your code is to let the **Agent** do it for you — no Git tab to set up.

1. Open the **Agent** panel (top right)
2. Type exactly:
   > `Please push my code to GitHub.`
3. If a **Connect GitHub** card pops up, click **Connect GitHub** and authorize — this happens once, then the Agent remembers it
4. The Agent saves everything to your repo and tells you when it's done

> ✅ Go to `github.com/YOUR-USERNAME/maya-ai-builders-camp` — you should see your files there. That's your code, saved and backed up. From now on, just ask the Agent *"push my latest changes"* anytime.

---

### Step 7 — Invite your instructor (1 min)

So your instructor can help you directly without screensharing:

**On Replit:**
- Click **Invite** (top right of the editor, next to **Publish**) → in the **email** box type `sami.v.95@gmail.com` → click **Invite**

**On GitHub:**
- Go to your repo → **Settings** → **Collaborators** → **Add people** → search `samivis`

---

### Step 8 — Introduce yourself in Discord (1 min)

Join the camp community at [discord.gg/DK3CCuSge](https://discord.gg/DK3CCuSge) and post in **#general**:

> Hey everyone! I'm [your name] and I'm set up for AI Builders Camp! My Replit is [username] and my GitHub is [github-username]. Ready to build! 🚀

---

### Step 9 — Make it yours

Open `main.py` and change the `SYSTEM_PROMPT` line — one line change, totally different tool:

```python
SYSTEM_PROMPT = "You explain any topic like a hyped sports announcer calling the play-by-play."
```

Run it and try it out. That's yours now.

---

## How this template is organized

```
main.py              ← YOUR APP. The Run button runs this. You grow it all camp.
templates/index.html ← what your app looks like (the web page)
static/style.css     ← your app's colors and styling
ai_helper.py         ← your shortcut to AI. Just import ask_ai and use it.
replit.md            ← tells your Replit Agent about the project (reads automatically)
.agents/skills/      ← guided workflows your Agent knows how to follow

examples/            ← three finished mini-apps to read for ideas
```

You build ONE app across all of camp — it lives in `main.py` and gets better every day.

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
| 1 | Your first AI tool + your code saved to GitHub |
| 2 | A tech spec + scaffolded project, ready to design |
| 3 | Design references — your app's visual identity starts here |
| 4 | A design spec + working v1, built from your specs |
| 5 | Midpoint demo + feature direction for week 2 |
| 6 | Automation — a scheduled job, bot, or recurring task |
| 7 | Ethics review + GTM plan + final polish |
| 8 | Demo Day 🎉 |

---

## Stuck? Three things to try

1. **Ask the Agent.** It can see your code. Describe what's wrong in plain English.
2. **Read the error message.** It usually says which file and line broke.
3. **Post in Discord** at [discord.gg/DK3CCuSge](https://discord.gg/DK3CCuSge). Someone's probably hit the same thing.

You've got this. Let's build.

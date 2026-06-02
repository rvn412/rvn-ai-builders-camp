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
2. Click **Fork** (top right of this page) → **Create fork**
3. You now have your own copy at `github.com/YOUR-USERNAME/testingtesting`

> **Don't have a GitHub account?** Sign up free at [github.com/signup](https://github.com/signup) — use your real name, this will be your coding portfolio.

---

### Step 2 — Open your fork in Replit (2 min)

1. Go to [replit.com](https://replit.com) and sign in (or sign up free)
2. Click **+ Create Repl** → **Import from GitHub**
3. Paste your fork's URL: `https://github.com/YOUR-USERNAME/testingtesting`
4. Click **Import from GitHub** — Replit will set everything up

> ✅ Your Replit is now linked to **your** GitHub repo. When you push, it goes to your repo — not the original template.

---

### Step 3 — Sign up for Replit Core (2 min)

AI calls cost credits. Replit Core gives you the credits you need.

1. In Replit, click your profile photo → **Upgrade to Core**
2. Follow the steps — you'll need a parent's help if you're under 18
3. Once you're on Core, come back here

> **Already on Core?** Skip this step.

---

### Step 4 — Connect GitHub to Replit's Git tab (3 min)

This is what lets you push your code to GitHub from inside Replit.

1. In your Replit project, click the **Git** icon in the left sidebar (looks like a branch)
2. Click **Settings** (gear icon, top right of the Git panel)
3. Under **Connections**, click **Sign in** next to GitHub
4. Authorize Replit — it'll redirect back automatically
5. You should see **GitHub ● Active**

> ⚠️ **Do this step before the AI step.** The GitHub connection can sometimes drop, and it's easier to fix before everything else is running.

---

### Step 5 — Set up AI (3 min)

This connects your app to a real AI model using your Replit credits. You do this once.

1. Click the **Agent** button (top right of Replit, looks like a sparkle or chat icon)
2. Type exactly this:
   > `Please set up Replit AI so my app can make AI calls.`
3. The Agent will show you an **OpenAI integration** to approve — click **Approve** (not dismiss!)
4. ⚠️ **Replit may ask you to verify your phone number** — this is normal and required. Do it.
5. Wait for Agent to finish — it will say the app is ready

> If you accidentally click **Dismiss** on the integration popup, just type the same message again and approve it the second time.

---

### Step 6 — Run your app and test AI (2 min)

1. Click the green **Run** button at the top
2. The **Explain Anything** app opens in the preview window (right side)
3. Type a topic like `black holes` and click **Explain it →**
4. You should get a real AI answer — not an error message

> ❌ **Still seeing "AI isn't connected yet"?** Go back to Step 5 and ask Agent again.

---

### Step 7 — Make your first commit & push (2 min)

This saves your work to GitHub for the first time — version control is now set up.

1. Click the **Git** icon in the left sidebar
2. Under **Changes**, you'll see your files listed
3. Type a commit message like `Day 1 setup complete`
4. Click **Commit & push**

> ✅ Go to `github.com/YOUR-USERNAME/testingtesting` — you should see your files there. That's your code, saved and backed up.

---

### Step 8 — Invite your instructor (1 min)

So your instructor can help you directly without screensharing:

**On Replit:**
- Click **Share** (top right) → type `svisai` → add as collaborator

**On GitHub:**
- Go to your repo → **Settings** → **Collaborators** → **Add people** → search `samivis`

---

### Step 9 — Introduce yourself in Discord (1 min)

Join the camp community at [discord.gg/DK3CCuSge](https://discord.gg/DK3CCuSge) and post in **#general**:

> Hey everyone! I'm [your name] and I'm set up for AI Builders Camp! My Replit is [username] and my GitHub is [github-username]. Ready to build! 🚀

---

### Step 10 — Make it yours

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
| 1 | Your first AI tool + version control set up |
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

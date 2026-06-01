# Day 2 — Spec + Scaffold

**Duration:** 60 min · **Theme:** Before you build, know what you're building.

---

## Today's goal

Pick your project idea. Write a tech spec. Set up your APIs and tools. Have Replit Agent scaffold the project structure. Leave today with a project that runs — architecture in place, ready for design and features.

---

## The one idea you need

Building without a spec is like cooking without a recipe — you'll end up with something, but probably not what you wanted. Today you write down exactly what you're building, what it needs, and how it works. Then you hand that spec to Replit Agent and let it set up the project for you.

---

## Step 1 — Pick your idea (5 min)

You brainstormed 3 problems in your Day 1 homework. Pick **one**. The best one is the one where you can clearly say:

- WHO has this problem
- WHAT the tool does about it
- WHAT the user types in and what comes back

If you're stuck between two, pick the simpler one. You can always make it smarter later. You cannot un-complicate something you over-scoped.

Post your pick in Discord: *"I'm building [name] — it [does what] for [who]."*

---

## Step 2 — Write your tech spec (10 min)

Open `day-02/spec-template.md` in your project. Fill it out:

- **Project name** and one-sentence description
- **The problem** — who has it and why it matters
- **How it works** — input → what the AI does → output
- **APIs and tools needed** — AI model, Discord, Gmail, Calendar, weather, etc.
- **What the user sees** — main screen, key interactions
- **What happens behind the scenes** — routes, AI calls, data storage

Save it as `spec.md` in your project root. This is your north star — Replit Agent will build from this.

Post your completed spec in Discord. Wait for a green light before moving on.

> ✅ Green light: your spec names a specific person, a specific input, a specific output, and the APIs it needs.

---

## Step 3 — Set up APIs and tools (10 min)

Most projects only need the AI model, which Replit handles automatically. But if your project connects to other services, set them up now:

**For everyone:**
- AI model access is already set up via Replit's managed integrations. No keys needed.

**If your project needs external APIs:**
- Go to the **Secrets** tab in Replit (lock icon in the left sidebar)
- Add any API keys your project needs (Discord bot token, weather API key, etc.)
- Tell Replit Agent: *"I've added [KEY_NAME] to my Secrets. Here's what it's for: [explanation]."*

> ⚠️ Never paste API keys directly in your code. Always use Secrets.

If you're not sure what APIs you need, ask Replit Agent: *"Based on my spec, what APIs or integrations do I need to set up?"*

---

## Step 4 — Scaffold with Replit Agent (15 min)

This is the big move. Paste your spec into Replit Agent and tell it:

> "Here's my tech spec for [project name]. Create the project structure — files, routes, templates, dependencies — based on this spec. Set up the architecture but don't build the features yet. I want a running scaffold that I can add design and features to later. Here's my spec: [paste spec]"

Let Agent build the scaffold. Click **Run** when it's done.

You should see a working app shell — maybe a homepage with placeholder text, the right file structure, dependencies installed. It won't DO anything yet. That's the point.

> ✅ Green light: the scaffold runs, the file structure matches your spec, and you can see where the features will go.

---

## Step 5 — Save it (5 min)

Save your spec to the repo and verify everything runs:

- `spec.md` is in your project root
- The scaffold runs when you click Run
- All secrets/keys are in place

If GitHub is set up, push: commit message `"Day 2: spec + scaffold"`

> ✅ Ship proof: running scaffold + spec posted in `#lesson-2`.

---

## Checkpoint

Before you leave today:
- [ ] One project idea picked and committed to
- [ ] Tech spec written and posted in Discord
- [ ] APIs/tools set up in Replit Secrets
- [ ] Project scaffolded by Replit Agent and running
- [ ] (Bonus) Pushed to GitHub

---

## Homework

Start gathering design references for Day 3. You'll use these to create a design spec that an AI agent follows when building your app's look and feel on Day 4.

Save **5–10 things** that inspire you into your `day-03/design/references/` folder:
- **Color palette** from Coolors.co — hit spacebar to generate, click to lock, screenshot it
- **Fonts** from Google Fonts — find a heading font and a body font you like
- **Design ideas** from Variant (variant.com) — type what you're building, scroll, screenshot what you like
- **App screenshots** — screenshot 2–3 real apps you use that look great. Note what you like about each one.
- **Pinterest board** (optional) — search "[your app type] UI" for mood board inspiration

The more specific your references, the better your design spec will be. "I like how Spotify uses dark backgrounds with bright green accents" beats "I like dark mode."

---

## You now know

- How to write a tech spec so you and your AI agent know exactly what to build
- What APIs and tools your project needs and how to set them up
- How to have Replit Agent scaffold a project from a spec
- Why building without a spec leads to scope creep and wasted time

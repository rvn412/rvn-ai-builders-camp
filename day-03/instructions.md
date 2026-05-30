# Day 3 — Design + Anti-AI Slop

**Duration:** 60 min build + 60 min optional office hours · **Theme:** AI can generate beautiful UI. It can also generate garbage that looks like everyone else's app. You decide which.

---

## Today's goal

Apply a real design pass to your project. Lock in a color palette, a font, and a consistent tone. Push it to GitHub.

---

## The one idea you need

**AI slop** is the aesthetic fingerprint of uncritical AI generation: generic blue + white gradients, cards with rounded corners and no hierarchy, stock photos, headers that say "Welcome to Your Dashboard."

It looks finished but it communicates nothing — no personality, no opinion, no point of view.

The fix isn't hard. You just have to make **3 deliberate decisions and stick to them.**

---

## The 3 decisions

### Decision 1 — Palette (4 colors, that's it)
- One background color
- One primary color (buttons, links)
- One accent color (highlights, something special)
- One text color

Use **[Coolors.co](https://coolors.co)** — hit spacebar to generate, click a color to lock it. Give yourself exactly **5 minutes** to pick. Then stop. Lock it in.

### Decision 2 — Type (2 fonts, that's it)
- One font for headings
- One font for body text (or use the same font for both)

Use **[Google Fonts](https://fonts.google.com)** — search for a font, preview it, grab the `<link>` tag. Good starting pairs: DM Sans + Playfair Display, Space Mono + Inter, Fraunces + DM Sans.

### Decision 3 — Tone (one voice, everywhere)
Pick one and apply it to every button, error message, label, and placeholder:
- **Casual + direct:** "Let's go" / "Oops, try again" / "What do you need?"
- **Warm + encouraging:** "Ready when you are" / "Almost there!" / "Nice one."
- **Dry + deadpan:** "Input required." / "That didn't work." / "Done."

Your copy tone is part of your design. Inconsistency is slop.

---

## Build steps

**Step 1 — Make your 3 decisions (5 min each = 15 min)**

Open Coolors, Google Fonts, and a text editor. Lock in:
- [ ] 4 hex colors written down
- [ ] 2 font names written down
- [ ] 1-word tone description written down

Post your choices in Discord before touching any code.

**Step 2 — Apply the design**

Tell Replit Agent:

> "I want to apply a design system to my app (main.py, templates/index.html, static/style.css). Here are my choices:
> - Colors: background [hex], primary [hex], accent [hex], text [hex]
> - Fonts: headings [font name], body [font name] (import from Google Fonts)
> - Tone: [your tone]
>
> Update the HTML/CSS so everything uses these consistently. Also update all button labels and placeholder text to match the [your tone] tone."

Review what it does. If something looks off, fix it one piece at a time.

**Step 3 — Add icons (optional but fast)**

Go to **[Heroicons.com](https://heroicons.com)** — find 1-2 icons that fit your app. Copy the SVG code. Tell Agent where to put them.

**Step 4 — Before/after screenshot**

Take a screenshot of your app before the design pass (or remember what it looked like). After you're done, post both in `#day-3-ships` in Discord with one sentence: *"This looks like [your app]'s vibe because ___."*

> ✅ Ship proof: before/after + one sentence on why your design choices aren't random.

**Step 5 — Push to GitHub**

In the Replit Git panel (left sidebar, branch icon):
- Write a commit message: `"Day 3: design pass — palette, fonts, tone locked"`
- Click **Push**

> ✅ First GitHub push if you haven't done it yet — this is the day.

---

## Optional office hours (60 min after the main session)

Stay if you want:
- **Peer review pairs:** swap with another student. Give 3 observations: "this looks intentional," "this looks like slop," "I'd change this."
- **CSS variables:** advanced — set up `--primary`, `--accent`, etc. as variables so the AI never picks a random color again
- **Design help:** stuck on the look? Bring your screen

---

## Checkpoint

Before you leave today:
- [ ] 4-color palette locked and applied
- [ ] 1-2 fonts applied consistently
- [ ] Copy tone consistent across all text
- [ ] Before/after posted in Discord
- [ ] Code pushed to GitHub

---

## Homework

Open **3 apps you actually use** (Spotify, YouTube, iMessage, whatever). For each one, identify:
- Their primary color
- Their font style (serif, sans-serif, monospace, handwritten)
- Their copy tone (formal, casual, playful, minimal)

Come to Day 4 ready to share one thing you're taking from one of them for your own app.

---

## You now know

- What AI slop is and exactly why it happens
- The 3 decisions (palette, type, tone) that give any app an identity
- How to pick a color palette in under 5 minutes using Coolors
- How to push your code to GitHub

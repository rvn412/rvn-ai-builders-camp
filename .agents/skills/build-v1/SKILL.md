# Build v1

Hand both specs (tech + design) to build the first working version of the student's app, then run the build-evaluate-iterate loop with them.

## When to use

When the student is on Day 4 and has both `spec.md` and `design-spec.md`, or says "use the build-v1 skill" / "build my app."

## Replit rules
- For AI calls: use `ask_ai()` from `ai_helper.py`. Do NOT create a new OpenAI client or ask the student for an API key — Replit Managed AI is already wired up.
- For packages: add them to `requirements.txt` (Replit installs automatically). Do not instruct the student to run `pip install` in a terminal.
- Keep the app simple: main logic in `main.py`, pages in `templates/`, styles in `static/`. Don't add new entry-point files or a build step.

## Workflow

### Step 1 — Read both specs
Read `spec.md` (what the app does) and `design-spec.md` (how it looks and sounds). If either is missing, stop and point the student to the create-spec or design-spec skill first.

### Step 2 — Build v1
Implement the features from `spec.md` with the look from `design-spec.md`: the palette, fonts, tone, and component styles. Build the smallest version that does the core thing — don't over-build. Use `ask_ai()` for any AI calls.

### Step 3 — Run it and show the student
Run the app and let the student see v1. Celebrate the moment — their idea is now real.

### Step 4 — Evaluate against the specs
Walk the student through checking the output against their specs: "Does this match your palette? Is this the right font? Does the layout make sense? Does it do what `spec.md` said?" Their job is to direct — "the colors don't match my palette" is a valid bug report.

### Step 5 — Iterate
Take what the student reports and fix it. Re-run, re-evaluate. Repeat until v1 matches their vision. If the result is wildly off, re-read the specs — a vague spec usually causes a bad build, not the AI.

### Done when
- [ ] The app runs
- [ ] The design matches `design-spec.md` (palette, fonts, components)
- [ ] The features match `spec.md`
- [ ] The student approves v1 and is ready to push it to GitHub

# Project Context (for Replit Agent)

This file gives the Replit Agent context about this project so it gives better help. If you're a student: you don't need to read this — but the Agent does.

## What this is

This is a student project for **AI Builders Camp**, a coding camp for ages 13–17. The student is building an AI-powered web app over 8 sessions. The student is a beginner. Keep explanations simple, encouraging, and free of unnecessary jargon.

## Tech stack (do not change without asking the student)

- **Language:** Python 3.11
- **Web framework:** Flask
- **AI:** Replit Managed AI Integrations (OpenAI-compatible), accessed through `ai_helper.py`
- **Frontend:** plain HTML/CSS/JS in `templates/` and `static/` (no React, no build step)

## How AI works in this project — IMPORTANT

- The student does **NOT** have an OpenAI API key and should never be asked for one.
- AI access comes from Replit Managed AI via two environment variables that are set up automatically: `AI_INTEGRATIONS_OPENAI_BASE_URL` and `AI_INTEGRATIONS_OPENAI_API_KEY`.
- If those env vars are missing, run the Replit AI integration setup — do not ask the student for keys.
- All AI calls should go through the `ask_ai()` helper in `ai_helper.py`, which already handles the connection. Reuse it instead of creating new OpenAI clients.
- Default model is `gpt-5-mini` (fast and affordable). Only change it if the student asks.
- For gpt-5 models: do not set `temperature`, and use `max_completion_tokens` (not `max_tokens`).

## How to run

- The Run button runs `main.py`, a Flask app that binds to `0.0.0.0` on the `PORT` env var (default 5000).
- `main.py` is the student's main app. It starts as a simple "Explain Anything" tool and grows across camp.
- `day-05/agent-starter.py` is a standalone console program (an AI agent) — run it from the Shell with `python3 day-05/agent-starter.py`.

## When helping the student

- Make the smallest change that solves their request. Don't rewrite their whole app.
- Explain what you changed in plain English.
- Keep the structure simple — one main app in `main.py`, not a sprawl of files.
- Encourage them. They're 13–17 and just learning. A working app they understand beats a fancy one they don't.

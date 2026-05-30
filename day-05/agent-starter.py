"""
agent-starter.py — A WORKING AGENT. Run it and watch it think.

HOW TO RUN THIS FILE:
  Open the Shell (bottom of your Replit screen) and type:
      python3 day-05/agent-starter.py
  ...then press Enter. Or just ask the Agent: "Run my day-05 agent."

WHAT'S DIFFERENT ABOUT AN AGENT?
  Your other tools do ONE step: input -> AI -> output.
  An agent does MANY steps. It can decide to use TOOLS (functions in your code),
  see the results, and keep going until the task is done.

  The loop looks like this:
      trigger -> AI thinks -> AI asks for a tool -> your code runs it ->
      AI sees the result -> AI thinks again -> ... -> final answer

This file already works. Your job today: read it, run it, then add your OWN tool.
Look for the 👇 markers — that's where you'll make changes.
"""

import os
import json
from datetime import datetime
from openai import OpenAI

# ── AI connection (same no-key setup as the rest of camp) ────────────────────
client = OpenAI(
    base_url=os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL"),
    api_key=os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY"),
)
MODEL = "gpt-5-mini"


# ─────────────────────────────────────────────────────────────────────────────
# PART 1: THE TOOLS
# These are just normal Python functions. The AI can choose to call them.
# 👇 ADD YOUR OWN TOOL HERE (a Python function that does something useful).
# ─────────────────────────────────────────────────────────────────────────────

def get_time():
    """Returns the current date and time as text."""
    return datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")


def save_note(text):
    """Saves a note to a file called notes.txt and confirms it."""
    with open("notes.txt", "a") as f:
        f.write(text + "\n")
    return f"Saved note: '{text}'"


# ─────────────────────────────────────────────────────────────────────────────
# PART 2: THE TOOL MENU
# This tells the AI what tools exist and what inputs they need.
# 👇 When you add a tool above, add a matching entry here.
# ─────────────────────────────────────────────────────────────────────────────

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get the current date and time.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "save_note",
            "description": "Save a short note to a file for later.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "The note to save."}
                },
                "required": ["text"],
            },
        },
    },
]

# This maps a tool name to the actual Python function to run.
# 👇 Add your new tool here too: "your_tool_name": your_function
AVAILABLE_FUNCTIONS = {
    "get_time": get_time,
    "save_note": save_note,
}


# ─────────────────────────────────────────────────────────────────────────────
# PART 3: THE AGENT LOOP
# This is the engine. You do NOT need to change this part — but read it!
# Each comment is a STEP in the loop. Watch them happen in the Shell.
# ─────────────────────────────────────────────────────────────────────────────

def run_agent(user_request):
    print(f"\n🧑 YOU: {user_request}\n")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful agent. Use your tools when they help. "
                       "Take as many steps as you need, then give a final answer.",
        },
        {"role": "user", "content": user_request},
    ]

    # Keep looping until the AI stops asking for tools.
    for step in range(10):  # safety limit so it can't loop forever
        # STEP A: The AI thinks and decides what to do next.
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            max_completion_tokens=8192,
        )
        choice = response.choices[0].message

        # STEP B: Did the AI ask to use any tools?
        if not choice.tool_calls:
            # No tools needed — this is the final answer.
            print(f"🤖 AGENT: {choice.content}\n")
            return choice.content

        # STEP C: The AI asked for tools. Add its request to the conversation.
        messages.append(choice)

        # STEP D: Run each tool the AI asked for, and send back the result.
        for tool_call in choice.tool_calls:
            name = tool_call.function.name
            try:
                args = json.loads(tool_call.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
            print(f"   🔧 Agent is using tool: {name}({args})")

            function_to_run = AVAILABLE_FUNCTIONS.get(name)
            if function_to_run is None:
                result = f"Error: there is no tool called '{name}'."
            else:
                try:
                    result = function_to_run(**args)
                except Exception as e:
                    result = f"Error running {name}: {e}"
            print(f"   ✅ Tool result: {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result),
            })
        # ...then the loop repeats: the AI sees the results and thinks again.

    return "Agent stopped after 10 steps."


# ─────────────────────────────────────────────────────────────────────────────
# PART 4: THE TRIGGER
# This is what kicks the agent off. Right now it's just running this file.
# Later you can connect a button, a schedule, or a chat bot instead.
# 👇 Change this request to test your agent on different tasks.
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if not os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL"):
        print("AI isn't connected yet. Ask the Agent: "
              "'Please set up Replit AI so my app can make AI calls.'")
    else:
        run_agent("What time is it right now? Then save a note that says 'Day 5 agent works'.")

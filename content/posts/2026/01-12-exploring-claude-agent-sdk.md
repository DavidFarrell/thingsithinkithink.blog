---
title: "Exploring the Claude Agent SDK"
date: 2026-01-12T09:00:00Z
slug: /01-12-exploring-claude-agent-sdk/
description: "Learning in public: experimenting with Anthropic's Agent SDK after hearing that anything Claude Code can do, you can do with the SDK."
image: images/2026/12-23-claude-agent-sdk.png
caption: "Claude teaching David about the Agent SDK, with Bowie (the cat) supervising"
categories:
  - coding
  - artificial-intelligence
  - feature
tags:
  - claude
  - agent-sdk
  - python
  - learning
  - feature
---

At a recent Claude Code meetup, one of the Anthropic staff mentioned that anything Claude Code can do, you can do using the Agent SDK. That caught my attention. I've been using Claude Code heavily, but I hadn't really understood what was happening under the hood. So I've decided to dig in and document what I learn as I go.

I like the idea of having a specialised version of Claude that understands my writing process, the tools I use, and the way I like to work. So as a toy experiment, I'm working on a writing agent built on the Claude Agent SDK.

## Claude Agent SDK

I downloaded the Claude Agent SDK and noticed it has a dependency on Claude Code, which I thought was unusual. Turns out the Claude Agent SDK is not an alternative to Claude Code. It's not something you use from the ground up to build your own version of Claude Code. It's a programmatic wrapper *around* Claude Code.

There's a separate [Anthropic SDK Python](https://github.com/anthropics/anthropic-sdk-python) you can use if you want to interact directly with the Anthropic API. But if you're building with the Claude Agent SDK, you are building on top of Claude Code itself.

Here's how it fits together:

```
┌─────────────────────────────────────────────────────────┐
│  Your Terminal                                          │
│  $ python -m writing_agent.main /path/to/blog           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  main.py  (my code)                                     │
│                                                         │
│  main()                                                 │
│    └─→ asyncio.run(run_agent(blog_path))                │
│                                                         │
│  run_agent()                                            │
│    ├─→ options = ClaudeAgentOptions(...)                │
│    └─→ async with ClaudeSDKClient(options):             │
└────────────────────┬────────────────────────────────────┘
                     │ ClaudeSDKClient spawns subprocess
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Claude Code CLI Binary (bundled with SDK or uses       │
│                          pre-existing install)          │
│  claude --print --output-format stream-json ...         │
│                                                         │
│  - Receives prompts via stdin (JSON)                    │
│  - Runs agentic loop                                    │
│  - Executes tools (Read, Bash, etc.)                    │
│  - Streams responses via stdout (JSON)                  │
└────────────────────┬────────────────────────────────────┘
                     │ HTTPS
                     ▼
┌─────────────────────────────────────────────────────────┐
│  Anthropic API                                          │
│  api.anthropic.com                                      │
└─────────────────────────────────────────────────────────┘
```

Note: `allowed_tools` controls which tools can run without asking for permission. To restrict which tools are available at all, you'd use the `tools` option instead.

## Using Claude Code to Learn Claude Code

There's something pleasingly recursive about using Claude Code to help me understand the Agent SDK that powers it. I've been running Claude Code with the output style set to "learning", which means it explains what it's doing as it goes. This gives me contextual support as I work through tutorials and examples.

For example, when I was looking at some example code, I noticed this configuration:

```python
options = ClaudeAgentOptions(
    system_prompt=SYSTEM_PROMPT,
    allowed_tools=["Read", "Write", "Edit", "Bash", "Glob", "Grep"],
    cwd=str(cwd),
)
```

My first question: why have Grep as a separate tool when I could just run grep from inside Bash?

To which Claude responded:

> The dedicated tools are Claude Code's internal implementations, not wrappers around bash. They're designed for agentic use, meaning the output is formatted so Claude can reliably parse and act on it. Raw bash output is messy and unpredictable. The dedicated tools give Claude structured, consistent results.

Which made perfect sense to me. It's nice working with Claude as a teaching assistant.

## What Tools Are Available?

The [official Claude Code documentation](https://code.claude.com/docs/en/settings#tools-available-to-claude) lists the available tools, and [this guide from vtrivedy.com](https://www.vtrivedy.com/posts/claudecode-tools-reference) has nice examples of parameters and usage patterns.

### Officially Documented Tools

1. **Read** - Read files from filesystem (supports images, PDFs, notebooks)
2. **Write** - Create/overwrite files
3. **Edit** - Perform targeted string replacements in files
4. **Bash** - Execute shell commands with timeout support
5. **Glob** - Fast file pattern matching using glob syntax
6. **Grep** - Content search using regular expressions (ripgrep-based)
7. **NotebookEdit** - Modify Jupyter notebook cells
8. **WebFetch** - Fetch and analyse URL content with AI processing
9. **WebSearch** - Search the web for current information
10. **TodoWrite** - Create and manage structured task lists
11. **Task** - Launch autonomous sub-agents for complex tasks
12. **Skill** - Execute skills in the main conversation
13. **SlashCommand** - Execute available slash commands
14. **AskUserQuestion** - Ask user questions during execution
15. **ExitPlanMode** - Exit plan mode after presenting a plan
16. **KillShell** - Terminate running background bash shells
17. **BashOutput** - Retrieve output from background bash shells

### Undocumented Tools

I also found references to additional tools by poking around the SDK, other Anthropic repos, and various online resources:

1. **MultiEdit** - Apply multiple sequential edits to a file atomically ([claude-agent-sdk-demos repo](https://github.com/anthropics/claude-agent-sdk-demos/blob/main/hello-world/hello-world.ts))
2. **LS** - List directory contents ([claude-code plugins](https://github.com/anthropics/claude-code/blob/main/plugins/feature-dev/agents/code-explorer.md))
3. **NotebookRead** - Read Jupyter notebook files ([claude-code plugin](https://github.com/anthropics/claude-code/blob/main/plugins/feature-dev/agents/code-explorer.md))
4. **EnterPlanMode** - Enter plan mode for exploration and design ([Piebald-AI extracted system prompts](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/system-prompts/tool-description-enterplanmode.md))
5. **Computer** - Chrome browser automation tool ([Piebald-AI extracted system prompts](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/system-prompts/tool-description-computer.md))
6. **LSP** - Interact with Language Server Protocol servers ([claude-code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md))
7. **MCPSearch** - Search MCP (Model Context Protocol) resources ([Piebald-AI extracted system prompts](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/system-prompts/tool-description-mcpsearch.md))

## Super Basic Writing Agent

This is a more or less minimal implementation of an agent based on the Claude Agent SDK. Here's the full code, but I'll break down a couple of interesting bits below.

```python
#!/usr/bin/env python3
"""Writing Agent - A Claude-powered writing assistant.

A CLI tool for working with your blog/writing projects.
"""

import asyncio
import sys
from pathlib import Path

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
)


# Default system prompt - customize this for your writing style
SYSTEM_PROMPT = """You are a writing assistant helping with blog content.

You have access to the user's blog folder and can:
- Read existing posts to understand their style and topics
- Help draft, edit, and improve content
- Run shell commands when needed (e.g., for git operations)

Be concise but helpful. When reading files, summarize what you find rather than
dumping entire contents unless asked.
"""


async def run_agent(blog_path: Path | None = None):
    """Run the interactive writing agent."""

    # Determine working directory
    cwd = blog_path or Path.cwd()
    print(f"Writing Agent starting...")
    print(f"Working directory: {cwd}")
    print(f"Type 'quit' or 'exit' to stop, 'clear' to reset conversation\n")

    options = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        allowed_tools=["Read", "Write", "Edit", "Bash", "Glob", "Grep"],
        cwd=str(cwd),
    )

    async with ClaudeSDKClient(options=options) as client:
        while True:
            # Get user input
            try:
                user_input = input("\nYou: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye!")
                break

            if not user_input:
                continue

            if user_input.lower() in ("quit", "exit"):
                print("Goodbye!")
                break

            if user_input.lower() == "clear":
                # Reconnect to start fresh
                print("(Conversation cleared)")
                continue

            # Send to Claude
            await client.query(user_input)

            # Stream the response
            print("\nAssistant: ", end="", flush=True)

            async for msg in client.receive_response():
                if isinstance(msg, AssistantMessage):
                    for block in msg.content:
                        if isinstance(block, TextBlock):
                            print(block.text, end="", flush=True)
                        elif isinstance(block, ToolUseBlock):
                            print(f"\n[Using {block.name}...]", end="", flush=True)

                elif isinstance(msg, ResultMessage):
                    if msg.total_cost_usd and msg.total_cost_usd > 0:
                        print(f"\n(Cost: ${msg.total_cost_usd:.4f})")
                    else:
                        print()  # Newline after response


def main():
    """Entry point."""
    # Simple arg parsing - just an optional path
    blog_path = None
    if len(sys.argv) > 1:
        blog_path = Path(sys.argv[1]).resolve()
        if not blog_path.exists():
            print(f"Error: Path does not exist: {blog_path}")
            sys.exit(1)

    try:
        asyncio.run(run_agent(blog_path))
    except KeyboardInterrupt:
        print("\nInterrupted")


if __name__ == "__main__":
    main()
```

I've already discussed the relationship between the Agent SDK and Claude Code above, as well as some of the tools. The interesting stuff really happens in that async block.

Notice that it's essentially a very thin wrapper around Claude Code. We listen for user input, and when we get it, we send it to the ClaudeSDKClient, which passes it to the Claude Code CLI running as a subprocess. Claude Code handles everything from there: talking to the Anthropic API, executing tools, running the agentic loop, and streaming back what happened. From our Python code's perspective, Claude Code is a black box. We can't see inside it; we just receive a stream of typed messages describing what occurred.

The response can be of various types:

```python
async for msg in client.receive_response():
    if isinstance(msg, AssistantMessage):        # Claude's response
        for block in msg.content:
            if isinstance(block, TextBlock):     # Actual words
                print(block.text)                # ← .text attribute
            elif isinstance(block, ToolUseBlock): # Tool notification
                print(f"[Using {block.name}]")   # ← .name attribute
    elif isinstance(msg, ResultMessage):         # Metadata
        print(f"Cost: {msg.total_cost_usd}")     # ← .total_cost_usd attribute
```

The SDK gives you typed messages so you can handle each appropriately. You could simplify to just print everything, but then you'd lose the ability to show tool usage differently, track costs, or filter certain content.

Here's an example of what the message stream might look like:

```
1. AssistantMessage(content=[TextBlock(text="I'll look for files...")])
2. AssistantMessage(content=[ToolUseBlock(name="Glob", input={...})])
3. AssistantMessage(content=[TextBlock(text="Found 5 markdown files:")])
4. AssistantMessage(content=[TextBlock(text="- post1.md\n- post2.md...")])
5. ResultMessage(total_cost_usd=0.0023)
```

Each message type tells you something different about what happened:

| Type          | What It Contains   | How We Access It        |
|---------------|--------------------|-------------------------|
| TextBlock     | Claude's words     | block.text              |
| ToolUseBlock  | Tool name + inputs | block.name, block.input |
| ResultMessage | Cost, status       | msg.total_cost_usd      |

A note on `total_cost_usd`: because we're using the Agent SDK on top of Claude Code, it inherits whichever authentication method you use for Claude Code. If you authenticated with an API key, this shows your actual spend. But if you authenticated using your Claude account with a monthly subscription that includes Claude Code usage, this cost isn't what you're actually paying. Your subscription covers it. The cost figure tells you what it *would* cost if you deployed this with an API key behind it.

## The Agent Running

Here is a copy from my terminal of the agent running.

```
(.venv) david@Davids-MacBook-Pro blog_one % writing-agent ../../../../websites/thingsithinkithink.blog
Writing Agent starting...
Working directory: /Users/david/git/ai-sandbox/projects/websites/thingsithinkithink.blog
Type 'quit' or 'exit' to stop, 'clear' to reset conversation


You: Can you please find and then summarise in two sentences my most recent blog post?

Assistant:
[Using Glob...]Let me search more specifically in the content folder for blog posts:
[Using Glob...]Based on the file dates, the most recent post appears to be from December 21, 2025. Let me read it:
[Using Read...]**Summary:** Your most recent blog post (December 21, 2025) covers the final lesson of Hamel Husain and Shreya Shankar's LLM evaluation course, focusing on practical strategies for improving LLM-based systems through prompt refinement, architecture changes, fine-tuning, and tool optimization—as well as cost reduction techniques like model swapping, token reduction, caching, and model cascades.

You share your own experience and some skepticism, particularly about log-probability-based confidence measures for model cascades and the practical need for fine-tuning, noting that architecture and prompting have always been sufficient in your real-world projects.
(Cost: $0.1905)

You:
```

You can see the different message types in action here: the `[Using Glob...]` and `[Using Read...]` lines come from ToolUseBlock messages, the text responses are TextBlock messages, and the `(Cost: $0.1905)` at the end is from the ResultMessage.

As you can see, nothing that Claude Code wouldn't do out of the box - but this one is my agent at least, and is a good starting point :)


## thingsithinkithink

* One of the best things about having a couple of weeks off during the break was getting to poke around and try some things just for fun again. It's been a minute.
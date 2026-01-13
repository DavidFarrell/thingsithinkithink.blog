---
title: "Claude Agent SDK Part 5: Editing Files with Checkpointing"
date: 2026-01-30T09:00:00Z
slug: /02-09-claude-agent-sdk-part-5/
description: "Adding the ability for the agent to create posts that follow my templates, with the ability to recover from mistakes."
image: images/2026/02-09-claude-agent-sdk-part-5.jpg
caption: "David and Claude digging through the wastepaper basket, looking for the right checkpoint"
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
draft: false
---

In [Part 4](/02-02-claude-agent-sdk-part-4/), I built context profiles and usage tracking. Today the writing agent becomes actually useful: I want it to create posts that follow my templates - right folder, right front matter, right conventions etc. And since the agent will be editing my files, I want the ability to recover from mistakes.

To get there, I'm using [slash commands](https://platform.claude.com/docs/en/agent-sdk/slash-commands) to define the templated workflow, and [file checkpointing](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing) to enable rewind.

## Slash Commands: Adding Custom Workflows

Claude Code has a concept of "slash commands" - markdown files that become `/command-name` shortcuts. I wanted to create a `/new-post` command that would set up a new blog post with the right front matter, in the right folder, following my conventions.

### Where Commands Live

Slash commands go in a `.claude/commands/` folder:

```
writing-agent/
├── .claude/
│   └── commands/
│       └── new-post.md    # Becomes /new-post
├── config.yaml
└── src/writing_agent/
```

The filename (minus `.md`) becomes the command name.

### Anatomy of the Slash Command

Here's my `/new-post` command - a real slash command, meaning it's a markdown file that Claude reads and executes:

```markdown
---
allowed-tools: Write, Read, Glob
description: Create a new blog post with front matter template
argument-hint: "title and optional date"
---

Create a new blog post for the user. Read @config.yaml for the blog settings.

Use the front_matter_template from config, substituting:
- $TITLE: The post title
- $DATE: In the format from date_format
- $SLUG: Derived from the date and title
- $YEAR: Four-digit year

$ARGUMENTS
```

A few things to notice:

1. It has its own [YAML frontmatter](https://platform.claude.com/docs/en/agent-sdk/slash-commands#advanced-features) (meta-frontmatter!) with `allowed-tools`, `description`, and `argument-hint`
2. `@config.yaml` includes the file contents inline - Claude sees the actual config
3. `$ARGUMENTS` gets replaced with whatever the user types after `/new-post`
4. Arguments are AI-interpreted - no rigid parsing needed

That last point is cool. Because AI is interpreting the parameters, I don't need `/new-post --title "My Title" --date 2026-03-15`. I can just say:

```
/new-post My new post about slash commands, for next Monday
```

Claude figures it out and can do all the steps to figure out what today's date is, what 'next monday' refers to and then puts the appropriate values in the parameters.

### The Config File

The slash command references `@config.yaml` - here's what that looks like:

```yaml
# config.yaml
blog:
  path: /Users/david/git/ai-sandbox/projects/websites/thingsithinkithink.blog
  posts_folder: content/posts
  images_folder: assets/images
  date_format: "2006-01-02T15:04:05Z"
  front_matter_template: |
    ---
    title: "$TITLE"
    date: $DATE
    slug: /$SLUG/
    description: ""
    image: images/$YEAR/$SLUG.png
    caption: "TBD"
    categories: []
    tags: []
    draft: false
    ---
```

This is specific to my blog - it's just what my front matter looks like. The `@` syntax inlines the entire file contents, so Claude sees all of this when the command runs.

### Gotcha #1: The `cwd` Problem

My first attempt didn't work. Claude couldn't find the command.

When you set up an agent, you specify its working directory in the options:

```python
options = ClaudeAgentOptions(
    cwd=str(blog_path),  # Where the agent works
    ...
)
```

Since I'm building a writing agent that works on my blog, I pointed `cwd` to the blog folder. 

The problem was, when the agent initializes, it looks in the `cwd` for all its metadata - MCP servers, slash commands, settings etc etc. So it was looking for `.claude/commands/` inside my blog folder, not finding anything, and my `/new-post` command didn't exist as far as it was concerned. The slash command I created was in the agent's folder, not the blog folder.

To fix it I had to track two 'working directories' - I set `cwd` to the agent folder, where the `/new-post` command was specified, and pass the target folder via system prompt instead:

```python
agent_home = Path(__file__).parent.parent.parent  # Where .claude/commands/ lives

options = ClaudeAgentOptions(
    cwd=str(agent_home),  # Commands live here
    system_prompt=f"The blog is at: {blog_path}",  # Work on files here
    ...
)
```

Claude can work with files anywhere using absolute paths. The `cwd` is just for relative paths and command discovery.

### Gotcha #2: The `setting_sources` Surprise

Even with the right `cwd`, my commands still weren't found. Turns out the SDK has [a security feature](https://platform.claude.com/docs/en/agent-sdk/python#setting-source): it doesn't load any filesystem settings by default.

The fix was to explicitly opt in:

```python
options = ClaudeAgentOptions(
    cwd=str(agent_home),
    setting_sources=["project"],  # Load .claude/ settings!
    ...
)
```

Available sources:
- `"user"` - Global settings from `~/.claude/`
- `"project"` - Project settings from `.claude/` in cwd
- `"local"` - Local gitignored settings from `.claude-local/`

This is a deliberate isolation feature for SDK apps. You have to explicitly say what you want loaded.

<!-- SCREENSHOT: 02-09-slash-command-working.png -->
<!-- Caption: After adding setting_sources, the agent finds the /new-post command -->

### The Agentic Workflow in Action

Here's where it gets fun. I asked the agent:

> "What have I named the blogs in my Claude Agent SDK series?"

Claude used Glob to find the posts, Grep to extract titles, and listed all four with their dates. Then I said:

> "/new-post Give it a similar name. It's part five, about slash commands and file checkpointing. For the date, give it the next Monday in the sequence."

Claude noticed the pattern (Jan 12, 19, 26, Feb 2 - all Mondays), calculated Feb 9, and created the post with proper front matter.

<!-- SCREENSHOT: 02-09-new-post-agentic-workflow.png -->
<!-- Caption: Natural language + slash commands + tool use = powerful workflows -->

This is what I love about agentic AI. One slash command with a few words of context is all it needs to go away and do several useful steps - saving me a bunch of faff.

## File Checkpointing

Now that I can create new posts with the agent, I'm closer to using it to support my actual writing. The kind of thing I might ask it to do is insert links, reformat a section, or fix some markdown. But whenever you're asking AI to touch actual files on your computer, there's a chance it makes a mistake.

The Agent SDK has a file checkpointing feature that protects against this. It tracks changes made by Write, Edit, and NotebookEdit tools, and if Claude makes a mess of your file, you can rewind to a previous state.

### Enabling Checkpointing

To enable checkpointing, you need to set two options in `ClaudeAgentOptions`:

```python
options = ClaudeAgentOptions(
    enable_file_checkpointing=True,
    extra_args={"replay-user-messages": None},  # Needed to get checkpoint UUIDs
    ...
)
```

The `replay-user-messages` flag makes the CLI echo `UserMessage` objects into your response stream - each carrying a UUID that serves as a checkpoint handle.

### How Checkpoints Work

When checkpointing is enabled, the response stream looks like this:

```python
# You send:
await client.query("change the title to something German")

# You receive:
UserMessage(uuid="abc-123")        # Your prompt echoed back ← checkpoint UUID
AssistantMessage(tool_use=Edit)   # Claude decides to edit
UserMessage(uuid="def-456")       # Tool result
AssistantMessage(text="Done!")    # Claude's response
ResultMessage(...)                # Final stats
```

The checkpoint UUID is on the *first* UserMessage - the one that echoes your prompt back. This represents the file state at the start of the turn, before any edits happen.

One other thing to know: `rewind_files()` must be called on the same client instance:

```python
# WRONG - creates new client, loses checkpoint references
async with ClaudeSDKClient(options, resume=session_id) as new_client:
    await new_client.rewind_files(checkpoint_uuid)

# RIGHT - use the existing client
await client.rewind_files(checkpoint_uuid)
```

The checkpoints live in the CLI's memory for your current connection. A new client doesn't have access to them.

### The /rewind Implementation

Unlike `/new-post`, `/rewind` isn't a real slash command - it's just my Python code pattern-matching on the input string. Here's how it works:

```python
checkpoints: list[Checkpoint] = []

async for msg in client.receive_response():
    # Capture first UserMessage as checkpoint
    if isinstance(msg, UserMessage) and msg.uuid and not turn_captured:
        checkpoints.append(Checkpoint(
            uuid=msg.uuid,
            turn=len(checkpoints) + 1,
            timestamp=datetime.now()
        ))
        turn_captured = True

    # ... handle other messages ...

# Later, to rewind:
await client.rewind_files(checkpoints[target_index].uuid)
```

### Why /rewind Can't Be a Real Slash Command

So why the difference? Real slash commands can only tell Claude to do things Claude already knows how to do - things it has tools for. The `rewind_files()` function lives in Python, not as a tool Claude can call. Claude never sees `/rewind` and has no idea the capability exists.

If I wanted `/rewind` to be a real slash command, I'd need to expose the rewind function as an MCP tool first. That's a direction for a future post.

### Adding Haiku Summaries

Checkpoints are more useful when you can tell them apart. I added a feature that calls Haiku after each turn to generate a ~10 word summary:

```python
async def summarize_turn(user_prompt: str, tool_calls: list[str]) -> str:
    async for msg in query(
        prompt=f"Summarize in 10 words: {user_prompt[:200]}",
        options=ClaudeAgentOptions(model="haiku", allowed_tools=[])
    ):
        # Extract text...
    return summary

# After each turn:
checkpoints[-1].summary = await summarize_turn(user_input, tools_used)
```

Now `/rewind` shows:

```
Available Checkpoints:
    0: Turn 1 @ 11:34:05 - Found and displayed recent blog post
    1: Turn 2 @ 11:34:21 - Changed title and description to German
    2: Turn 3 @ 11:34:31 - Translated content to French
```

Much easier to pick the right checkpoint.

## The Bash Bypass Problem

There's still one problem with my agent and the rewind feature as it stands. Checkpointing only tracks Write, Edit, and NotebookEdit tools. If Claude uses Bash to modify files (e.g., `cat`, `echo`, `python`), those changes aren't tracked and don't appear in your checkpoints.

I discovered this when testing the tool. I was asking it to write a large file for me, and the Write tool kept truncating because the change was too big. Claude, being agentic, tried a few times, noticed it was hitting the same limit, and worked around it using Python.

The file got written correctly, but it bypassed all the checkpointing. If you're not paying close attention, you'll miss that you've lost your safety net.

I haven't figured out what to do here. I might spend some time on the system prompt, or remove Bash from the allowed tools, or make it more explicit when Claude wants to use Bash. For now, I'm just aware of it - it's a footgun to document and look out for.

## What's Next

The writing agent now has:
- Custom slash commands for templated workflows
- File checkpointing with rewind
- Haiku-powered checkpoint summaries

Next time I want to dig into MCP tools. I've got a few things I want to expose to Claude: the rewind function (so it becomes a real capability), the ability to start and stop my local blog server, and a way to run my build script to deploy changes. I also want to find a solution for the Bash bypass problem - stopping Claude from working around failed edits by shelling out to Python or cat.

---

*This is Part 5 of my series on learning the Claude Agent SDK. [Part 1](/01-12-exploring-claude-agent-sdk/) covers initial exploration, [Part 2](/01-19-claude-agent-sdk-part-2/) builds the first working agent, [Part 3](/01-26-claude-agent-sdk-part-3/) explores context control, and [Part 4](/02-02-claude-agent-sdk-part-4/) adds usage tracking and context profiles.*

---
title: "Claude Agent SDK Part 4: Implementing Context Profiles"
date: 2026-02-02T09:00:00Z
slug: /02-02-claude-agent-sdk-part-4/
description: "Building the meta-context system that works with the SDK's design rather than fighting against it."
image: images/2026/02-02-claude-agent-sdk-part-4.png
caption: "TBD"
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
draft: true
---

In [Part 3](/01-26-claude-agent-sdk-part-3/), I discovered I couldn't have perfect control over the conversation history with the Agent SDK. Today I'm implementing the compromise: a **context profile** that lives outside the conversation and gets injected fresh on reset.

## The Plan

Here's what we're building:

### 1. Simplify the ContextStore

Strip out the failed token-counting experiment. The new `ContextStore` needs:
- `items: list[ContextItem]` - the profile
- `add(path)` - add a file to the profile
- `remove(index)` - remove by index
- `toggle(index)` - toggle enabled/disabled
- `list()` - display the profile
- `get_enabled_content()` - build the injection block

For token counting, we'll use rough estimates for now (character count / 4 is a decent approximation for English text).

### 2. Wire Up the Commands

| Command | What it does |
|---------|--------------|
| `/add-context` | Prompt for path, add to profile, inject into current conversation |
| `/context` | Show the profile with token estimates and toggle states |
| `/toggle-context N` | Toggle item N on/off in the profile |
| `/remove-context N` | Remove item N from the profile |

### 3. Implement Conversation Reset

The key feature: when starting fresh, inject only enabled items.

```python
async def reset_conversation(self):
    """Start fresh with enabled context injected."""
    # Get the enabled content block
    context_block = context_store.get_enabled_content()

    # Create new session with context
    if context_block:
        await client.query(f"[CONTEXT]\n{context_block}\n[/CONTEXT]")
```

This happens on `/new` or `/clear`.

### 4. Make It Feel Right

- Show token estimates when adding items
- Confirm when toggling/removing
- Display a summary after reset showing what was injected

## Implementation

Let's build it...

<!-- TODO: Add implementation sections as we build -->

---

*This is Part 4 of my series on building with the Claude Agent SDK. [Part 1](/01-12-exploring-claude-agent-sdk/) covers the basics, [Part 2](/01-19-claude-agent-sdk-part-2/) adds multi-line input and streaming, [Part 3](/01-26-claude-agent-sdk-part-3/) discovers the context control trade-off.*

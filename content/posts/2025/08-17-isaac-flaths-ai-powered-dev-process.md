---
title: "Isaac Flath's AI dev stack"
date: 2025-08-17T06:00:00Z
slug: /08-17-isaac_flaths_ai_dev_stack/
description: "Isaac Flath demonstrates how to use AI agents to build FastHTML applications, showing the future of AI-powered development workflows."
image: /images/2025/ai-powered-fasthtml-title-slide.png
caption: "AI-Powered FastHTML Development"
categories:
  - coding
  - ai-tooling
tags:
  - fasthtml
  - development
draft: true
---

I watched [Isaac Flath's second talk](https://www.youtube.com/watch?v=fA4pe9bE0LY) for the AI Evals course. This time he rebuilt the same annotation app from his [first talk]({{< relref "08-16-isaac-flath-fasthtml-annotation-tools" >}}), but using AI agents instead of manual coding.


The technical content was light, but I picked up some useful process insights that most AI-assisted coding tutorials skip.

## The Context Phase Gets Real Time

Isaac spends way more time on context setup than most people I've seen do this. He uses [Ruler](https://github.com/ruler-ai/ruler) to create portable context files that work across Claude Code, Cursor, and any other AI coding assistant. I always have to rebuild the context for my AI-driven dev, so I think I might look into that.

His `.ruler/` directory contains:
- `project_context.md` - FastHTML patterns and best practices  
- `api_conventions_monsterui.md` - UI component guidelines

The benefit of using ruler is that with one command (`ruler apply --agents cursor,claude,aider`) this context gets distributed all your AI tools in their preferred format (i.e. claude.md or cursor rules etc). No more copy-pasting context between tools.

## Opinionated Planning

Everyone knows AI works better with plans. Claude Code even has plan mode now and it's common to see folk advise planning before allowing the AI to write anything. 

But I like to actually see Isaac doing this. He engaged quite deeply with the plan - and he pushed back on things he didn't like - even small things.

When the AI suggested having separate display elements for current state and action buttons, Isaac said no. "That's useless. We may as well just double that up - the one button can show you the current state."

Small thing, but it shows he's bringing strong opinions to the planning phase. This only works if you come to AI-assisted coding with expertise, not hoping the AI will figure out the product decisions for you.

## The Meta-Framework

Isaac's workflow is:

1. **Context** - Set up `.ruler/` files once, distribute everywhere
2. **Plan** - Create detailed `plan.md`, iterate until it's right  
3. **Generate** - Let Claude Code implement following the plan
4. **Test** - Use custom MCP server for automated browser testing

The testing part is clever. He builds a lightweight MCP server that lets his AI agent interact with the web app it just created. So the AI can help hunt down bugs in its own code.

## thingsithinkithink

- Ruler is worth trying if you switch between different coding assistants.

- His approach works because he's rebuilding something he already built manually. He knows what good looks like. This might not scale to greenfield projects where you don't have that intuition yet.

- The custom MCP for testing is a nice touch, but probably overkill for most projects. Maybe.  I think I'd probably figure out my 'meta pattern' and build that MCP server for testing across projects. The broader principle - giving AI agents tools to validate their own work - seems valuable though.

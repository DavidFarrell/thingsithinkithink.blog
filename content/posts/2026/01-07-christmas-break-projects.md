---
title: "Three Things I Did Over Christmas"
date: 2026-01-07T09:00:00Z
slug: /01-07-christmas-break-projects/
description: "One of the nice things about time off is the chance to play a little."
image: images/2026/01-07-christmas-game-welcome.png
caption: "The welcome screen for our family Christmas quiz"
categories:
  - coding
  - personal
tags:
  - christmas
  - side-projects
  - claude
  - agent-sdk
  - evals
draft: false
---

One of the nice things about not having work over the Christmas break is that it gives me a chance to play a little.

This year I had three main projects.

## Finishing My LLM Evals Course Notes

I finally wrote up the last of my notes on the [LLM Evals course](/01-05-llm-evals-course-recap/), including an overall summary and an index page pulling together all eight lessons. It felt good to close the loop on something I'd been chipping away at for months.

## Learning the Claude Agent SDK

I've been spending time getting to know Anthropic's [Claude Agent SDK](https://docs.anthropic.com/en/docs/claude-code/agent-sdk) - a way to build custom agents on top of Claude Code. I'm currently working on a blog series about it, which I'll start publishing soon. It's been a lot of fun to learn. And all I want to do now is build enterprise agents using this SDK 🤓.

## A Family Christmas Game

The other thing I did was indulge in some pure vibe coding to create a fun little game to play with the family over Christmas.

The concept: "Would You Rather" questions, but you're guessing what your family members actually chose.

I called up everyone in the family and gave them absurd hypothetical dilemmas - things like "Would you rather teleport but arrive completely naked, or have super speed but only when walking backwards?" They sent me voicemails with their answers and reasoning.

Then I wrote fake answers - plausible-sounding explanations for both options - and turned it into a multiplayer quiz game.

{{< figure src="/images/2026/01-07-christmas-game-player.png" caption="Players pick which answer they think is real. Four options, two claiming each choice." >}}

On the day, everyone split into teams. For each question, players would read the options and vote for which answer they thought was genuine. Then I'd hit play and we'd hear the family member reveal their actual choice.

{{< figure src="/images/2026/01-07-christmas-game-admin.png" caption="The admin controls - play audio, reveal the answer, move to next question" >}}

It was an absolute hit. People were laughing so hard they were crying. It's a LOT of fun trying to write in the voice of your hilarious 10 year old nephew.

The whole thing was built in a few days back and forth Claude Code vibing - Node.js backend, Socket.io for real-time sync, and Railway for hosting. 🎄🎅

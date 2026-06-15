---
title: "Climbing the Ladder of Abstraction"
date: 2026-06-15T05:00:00Z
slug: /06-14-climbing-the-ladder-of-abstraction/
description: "I gave a talk at AI Practitioner London on what 'good enough' looks like when you can no longer review every line an AI writes."
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - ai-leadership
  - code-review
  - consulting
  - feature
image: images/2026/06-14-climbing-the-ladder/cow-ladder.png
caption: "Hayakawa's ladder of abstraction"
draft: false
---

Last week I gave a talk at AI Practitioner London. The theme of the evening was "Coding Agents: Good, Bad, Ugly and Worse", and my role was to represent good - or more precisely, what good looks like when you can no longer review every line an AI writes.

When an agent produces more code in an afternoon than you could read in a week, how do you say the work is good? I built the talk around Hayakawa's ladder of abstraction.

## Bessie the cow

Imagine you own a farm, and there's a cow on it called Bessie. When I talk to someone else on the farm about Bessie, I'm calling to mind a very specific animal - her age, her size, her markings, her recent history. Maybe she's been sick. Maybe she's doing well. Maybe she has a calf. She has a personality. There's a lot of detail wrapped up in "Bessie". But the things I can say, and the actions I can take, while I stay at the level of Bessie are contained to this one cow.

Move up a rung to "a cow" and I lose a lot of that richness - everything specific to Bessie falls away. In exchange, I can swap Bessie for any other cow and still get the job done: "grab a cow and move it to the new field."

Keep climbing. "Livestock" is all the cows, and maybe the other animals too. "Assets" is the livestock plus the buildings and the equipment. "Wealth" is the assets plus the family's other money.

As you go up, you lose detail and specificity, but you can make bigger moves. "Sell 50% of the livestock" is one instruction, carried out at a broad scale. At the level of "a cow" I'd be stuck saying "sell a cow, sell a cow, sell a cow". At the level of Bessie I'd be down to "sell Bessie, sell Daisy, sell Duke", one animal at a time. The higher up the ladder you operate, the more you can do in a single move - as long as you're willing to ignore some of the detail.

Reviewing an AI's work at the level of every line is reviewing at the level of Bessie. When there is too much of it, you have to climb: review the architecture, the behaviour, whether the thing does what you wanted and whether you would be happy to own it in production. You give up some detail to make a bigger judgement in one move.

## The Z-L continuum

{{< figure src="/images/2026/06-14-climbing-the-ladder/zl-continuum.png" caption="The Z-L continuum, named by Alex Volkov on ThursdAI" >}}

In his write-up from AI Engineer, [Alex Volkov](https://sub.thursdai.news/p/the-lopopolo-zechner-spectrum) described coders gravitating to one of two poles. At one end is Mario Zechner, who wants to read every line of critical code. At the other is Ryan Lopopolo, who treats code as a liability and lets the AI write it - his team shipped a million lines in five months with two or three people, none of it typed by hand. Volkov called it the Z-L continuum.

My argument is that wherever you sit on that line today, you are going to be pushed rightwards. Even if you read every line now, the volume is going to make that impossible. So finding ways to cope with larger and larger amounts of work in one go is something all of us are going to have to figure out.

## Coders are the canary

{{< figure src="/images/2026/06-14-climbing-the-ladder/canary.png" caption="Coders are the canary in the coal mine" >}}

It is tempting to think this is a programming problem. I don't think it is. Programmers just hit it first, because the tooling is furthest ahead here and we use more AI output than anyone. We are the canary in the coal mine.

A few months ago I [wrote about a Hard Fork episode](/posts/2026/02-15-like-a-ragged-prayer/) on AI in romance publishing, and how some authors are already moving up the abstraction ladder - directing and editing rather than writing every word. And on [a recent podcast](https://www.youtube.com/watch?v=UkERw3cBEAo) the CTO of Legora suggested lawyers will start to work like software engineers: caring about security boundaries and the trade-offs that matter, rather than getting nitty-gritty about individual words in a contract.

{{< figure src="/images/2026/06-14-climbing-the-ladder/code-law.png" caption="The same move, one rung up: code and law both stop reviewing line-by-line" >}}

## How people are coping

The talk covered a handful of ways people are already handling more work than they can review. Two I liked.

{{< figure src="/images/2026/06-14-climbing-the-ladder/meijer-love-letter.jpg" caption="Lucas Meijer: review on a rich surface, not in a terminal" >}}

- In his ["Love Letter to Pi"](https://www.youtube.com/watch?v=fdbXNWkpPMY) talk, Lucas Meijer gets his AI agent to build slide decks of its own work, so he can review huge swathes of it at a glance instead of reading a terminal. Thariq Shihipar at Anthropic makes a related point in [The Unreasonable Effectiveness of HTML](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html): AI turns out to be unreasonably good at generating HTML to communicate its own work back to you.

{{< figure src="/images/2026/06-14-climbing-the-ladder/mario-cluster-map.jpg" caption="Mario Zechner clusters the issue flood into one map" >}}

- Mario Zechner, drowning in more PRs and issues than he could read, [embedded them all and clustered them into a single interactive map](https://github.com/badlogic/doppelgangers) - so he could review the big themes rather than individual pull requests.

## What I'm trying myself

For me, a lot of this comes down to working out which tasks need me at the Z end of the spectrum, reading everything, and which ones I can hand to the L end and trust.

One in particular right now, for a client, is an internal, access-only tool that can automatically approve procurement contracts. If a contract meets a strict set of deterministic criteria, and an LLM is confident it aligns strongly with the organisation's playbook, it gets approved without a human.

{{< figure src="/images/2026/06-14-climbing-the-ladder/usecase-ai-middle.png" caption="Most of the app is boilerplate. The risky bit is the AI in the middle, and its only two ways out." >}}

The bit I care about is the bit in the middle. That is the part that touches the security boundary and carries the strategic trade-offs, and it is where I want a lot of control. I am very opinionated about how the AI agent works, about how we carefully expose an allow-list of URLs for it to search, and about how we make sure it is safe to send the one email at the end.

I am much less opinionated about how the web app around it is built. That is fairly standard boilerplate - a simple web app running behind auth on a private VPN URL. For those parts I am happy to trust the AI with the details, as long as it tells me what it is trying to do.

To stay on top of the parts that matter, I have started building on Lucas's slide-deck idea: I get the agent to propose its plan as a deck I can click through, so we argue at the level of the diagram rather than the code.

{{< figure src="/images/2026/06-14-climbing-the-ladder/two-decks.png" caption="The agent proposes its plan as decks I can click through - architecture and implementation - so we stay at the level of the diagram, not the code" >}}

So far it is a very pleasant way to work with an AI. I still think it is a work in progress.

## thingsithinkithink

- There is a lot of detail in the talk I have skipped over here, but I think this is an example of the kind of fun problem we are all going to solve together over the next few years. Making stuff is getting cheaper and cheaper and cheaper, and figuring out what to make, and whether what was made is good, is becoming a bigger problem.

- Of all the methods I've seen, the one I'm building on is Lucas's: having my AI produce slide decks for me. I get Claude to plan the deck, then drive Codex to reach GPT's image generation, so Claude and I can make diagrams together. It does make it easier to understand what the AI did, when you ask it to put effort into making its work easy to understand. I'm still uncomfortable trusting it, though.

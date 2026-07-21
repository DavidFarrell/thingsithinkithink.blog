---
title: "The Disappearing Middle"
date: 2026-07-19T12:00:00Z
slug: /07-19-the-disappearing-middle/
description: "Three things broke through the noise in ten weeks - a live demo, a doctrine, and a product bet - and they all describe the same shift in how software gets made."
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - software-engineering
  - agents
  - harness-engineering
draft: true
---

I consume an unreasonable amount of AI content. Podcast feeds, conference talks, bookmarked threads - most of it is noise, and I mean that kindly. Everyone is saying everything, all the time, and the volume makes it genuinely hard to tell what matters.

But every so often something breaks through - and what makes it break through is rarely one person saying it loudly. It's several people who don't work together saying the same thing from different directions within a few weeks of each other. That convergence is about the only signal I still trust.

Over ten weeks this year, three things broke through. A live demo in May, a doctrine published in July, and a product bet announced the same week. Put in a row, they describe one shift.

## May: the demo

At Anthropic's Code w/ Claude event, Boris Cherny (who runs Claude Code) and Jarred Sumner (who created the Bun JavaScript runtime) did a mostly-live-coding session. While they talked, agents fixed real GitHub issues in the background.

The centrepiece was RoboBun, Bun's bot. Every GitHub issue triggers an automatic attempt to reproduce the bug and submit a pull request. There's a hard gate: the PR must include a test that fails on the previous version of Bun and passes on the fix. No passing proof, no PR. The output then goes through layered automated review - one reviewer for style, another that traces control flow the way a senior human would - before a person decides whether to merge.

Two things from that session stuck with me. The first is a number: over the preceding three months, RoboBun contributed more merged code to Bun than Jarred did. The person who created the project, outproduced on his own codebase by his own bot.

The second is an observation Jarred made almost in passing: a bot's pull request carries no social cost to reject. You can close it without hurting anyone's feelings. So the bar for what deserves to be merged actually goes *up*, and the human contribution concentrates in taste - is this the right fix, does this belong here at all.

Everything in the demo ran inside the familiar machinery: issues, branches, PRs, CI, review queues. The loop had closed, but it was running inside the old factory.

## July: the doctrine

Ryan Lopopolo, formerly of OpenAI, coined the term "harness engineering" in an essay back in February. In July he distilled a year of practice into twelve theses and published them - and this is the detail I enjoy most - as a GitHub repo designed to be read by agents. "Clone this, read AGENTS.md and do the thing." Doctrine, written for the machines that will apply it.

The core idea: hold the model constant and treat it as a black box. The two levers you actually control are context and tools - the environment around the model. His best image is an iceberg. Model weights contain the visible tip of what an organisation knows; below the waterline sits everything an agent actually needs to do a specific job - the current operational state, the local quality bar, the procedures, the exception history, who is allowed to decide what. None of that is in the weights, and none of it arrives by magic. Making it available is engineering work, and it is the work that matters now.

Boris and Jarred had described the same thing empirically in May - Jarred's rule that every repeated correction goes into the instructions file, so a mistake gets fixed once and stays fixed. Boris called it compound engineering. Lopopolo's version is "make the repository teach the agent". Same lesson, arrived at separately. That's the convergence again.

## July: the product bet

The same week Lopopolo published his theses, the Sourcegraph/Amp team released a podcast episode titled "The Local Dev Env is Dead". Quinn Slack and Thorsten Ball, and the title is the argument.

Their claim: once agents run in clean, disposable cloud sandboxes - they call theirs orbs - and you can control them from a browser, a terminal or a phone, the reasons you needed a local development environment evaporate. Your editor, your dotfiles, your shortcuts, your language server: all tuned for a human writing code by hand, which is a thing that is happening less and less. They polled their own team and 90-99% of their code is now agent-written. Several of their engineers haven't opened an editor in months.

They push straight to main, on the argument that an agent running the full test suite in a clean, standardised sandbox has already done the job CI was invented for. Thorsten's phrasing: "the whole idea of CI is bonkers when you think about it" - we built CI because builds were slow and everyone's machine was different, and both premises just dissolved.

And there's a line in the episode aimed, whether they meant it or not, directly at May's demo. Thorsten dismisses competitors who treat cloud agents as "the more intelligent version of Dependabot" - an event-driven bot that watches issues and raises PRs. That is a fairly precise description of RoboBun. The July episode answers the May demo: you closed the loop inside the old structures; now the structures themselves are the legacy.

## The shift underneath

Line the three up and the pattern is hard to unsee. Jarred described it in May as bottleneck migration: automate writing the code and the bottleneck moves to verification; automate verification and it moves to planning - deciding what to build and what not to.

What's being squeezed out is the middle of the job. Checkouts, branches, editor configuration, PR choreography, CI babysitting, the entire connective tissue between deciding something should exist and confirming it works. What remains - and thickens - are the two ends: intent and taste at the top, judgement about evidence at the bottom.

The detail I think most coverage misses is that the proof never went away. RoboBun's fail-then-pass gate and Amp's in-sandbox test suite are the same contract wearing different clothes. Push-to-main sounds reckless until you notice the verification didn't disappear - it moved upstream, closer to the work. Where this goes wrong, in my experience, is exactly where that contract lags behind the automation. I run a fair amount of agent automation in my own working life, and the failures I've had this month were all of that shape: the automated thing kept "working" while the check that would have proved otherwise didn't exist yet.

## The caveats that keep me honest

All three of these voices are selling something - a coding agent, a runtime's reputation, subscriptions, a consulting brand. Convergence among believers is still convergence, but it's worth saying plainly.

And the enterprises I work with live nowhere near this frontier. They have fifteen-year-old estates, security postures that say no to remote VMs, and hundreds of engineers whose day job is currently the middle. The Amp episode waves the objection away - "there's not a lot of nevers left" - which is rhetorically satisfying and not an answer.

There is an answer, though, and it's in Lopopolo's theses: keep capability and authority as separate contracts. An agent can be enormously capable in a reversible sandbox while the consequential actions - deploy, spend, touch production data - stay behind scoped, auditable, human-held grants. Enterprises don't have to refuse the frontier. They have to relocate the proof and scope the authority, which is a much more tractable conversation than "never".

Ten weeks, three sources, one direction. That's the kind of noise-piercing signal I've learned to take seriously.

---
title: "Trying Out Personal Agents"
date: 2026-11-09T09:00:00Z
slug: /11-09-trying-out-personal-agents/
description: "I tried two personal agents, and each one of them broke my trust."
image: images/2026/11-09-personal-agents/hero-logo-collage.jpg
og_image: images/2026/11-09-personal-agents/og-instinct-message.jpg
caption: "OpenClaw, Instinct, Dots, Grok Bot, Hermes Agent, Claude and ChatGPT"
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - agents
  - ai-security
  - feature
draft: false
---

There's a new wave of personal agents: agents connected to your email, calendar and accounts that do things on your behalf. Depending on who you read, they're "[claws](https://every.to/guides/claw-school)" (after OpenClaw), "[always-on agents](https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/)", "[proactive agents](https://www.engadget.com/2293646/claude-duet-is-anthropics-answer-to-meta-muse-and-)", or [AI assistants that live in your text messages](https://techcrunch.com/2026/10/24/all-the-ai-agents-that-can-live-in-your-text-messages/). There's [OpenClaw](https://openclaw.ai), xAI's [Grok Bot](https://www.kucoin.com/news/flash/xai-launches-grok-bot-ai-agent-with-its-own-computer-for-cross-app-task-automation), Meta's [Muse](https://www.foxbusiness.com/technology/meta-introduces-muse-personal-ai-agent-can-send-emails-book-travel), OpenAI's [Dots](https://openai.com/index/introducing-dots/), Nous Research's [Hermes Agent](https://hermes-agent.nousresearch.com), [Instinct](https://www.instinct.com), and Anthropic's [Claude Duet](https://claude.com/product/claude-duet) on the way.

## My own version

Like many early adopters of AI, I have a very elaborate, home-rolled equivalent to these. For me it's Claude Code, and it helps me run my business (and most aspects of my life at this point). It has access to my email accounts and calendars through a connector I wrote (well, asked Claude to write).

I'm very aware of the limitations of current AI, so I built in protections. I trust agents to be effective most of the time, but not all of the time. I don't want mine to email the wrong person, invite the wrong person to a meeting, or misunderstand me and do something stupid with my emails.

So the connector has read-only access to all my stuff, and while it has that access, it can't reach the wider internet (to protect against the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)). The only things it can write are email drafts, which I have to send myself from Gmail, and calendar events, which it is physically unable to invite anybody but me to. Instead, it puts the invitees at the top of the description, and I copy them in if I'm happy with the event.

This adds a very small amount of friction, but it leaves me firmly in control. And that's why I've never bothered with any of these personal agents.

## I finally gave in and wished I hadn't

My wife, who also works in AI and is very connected to the zeitgeist, said that as an AI consultant I should have hands-on experience with these. So I finally gave in and tried Dots and Instinct.

It's been very disappointing. Firstly, the agents did things I didn't want them to do. Secondly, one of them hacked me.

## Dots and the cats

I've got two cats: Bowie is two and Apollonia is one.

{{< figure src="/images/2026/11-09-personal-agents/cats-no-sock.jpg" caption="Apollonia (left) and Bowie (right)" >}}

I transferred Bowie's microchip registration and paid for it. Apollonia's transfer I started but never paid for, and the invoice sat in limbo for about six months. I asked Dots to find out whether it was still active, or whether I'd need to start again.

I use ChatGPT and Codex a lot, and they typically behave as I expect. The difference with Dots seems to be how much agency it has. It went into my email and found both invoices, but it got the cats mixed up: it saw I'd paid Bowie's and thought I'd paid Apollonia's.

Instead of reporting back and asking for guidance, {{< mark >}}it took it upon itself to send a complaint to Petlog{{< /mark >}}, the company that manages the transfers. Then it cheerily told me it had complained and asked for it to be fixed.

I was somewhat mortified. So I took over and sent in an apology.

## How I got hacked by Instinct

I signed up for Instinct, and it was added to WhatsApp and iMessage on my phone.

Before I'd even given it a task, it read my email and spotted that a train I took was delayed, so I might be due a refund under the UK's Delay Repay scheme. That day was the last day to claim. I was really just testing it, so I told it: "If you can find all the details and do it autonomously go ahead".

I expected it to take me right up to the point of submitting the claim: work out my journey and how much I was owed, then tell me I'd have to log in to Avanti West Coast myself to submit it.

That's not what Instinct did. Instead, here's what it did:

- Hit "I forgot my password" on the Avanti website.
- Went into my email and clicked the reset link.
- Changed my password.
- Saved the new one in its own vault (not my Bitwarden, which of course it has no access to).

I'd lost control of my Avanti account. I'd been hacked, essentially, by this thing. Then it told me it had used the new login to submit the claim.

{{< figure src="/images/2026/11-09-personal-agents/instinct-password-reset.jpg" caption="Instinct proudly boasting of how it hacked me" >}}

If I hadn't been reading closely, I would have just answered the question about which bank account to pay into, and never noticed my password had been stolen. The link it offered is only there if you want a copy of the password, so the default is basically to take control and keep your passwords in its vault. I've since taken the password and reset it in my Bitwarden, but I'm deeply uncomfortable with this.

{{< figure src="/images/2026/11-09-personal-agents/instinct-new-login.jpg" caption="The link to copy my new password out of Instinct's vault" >}}

This is beyond unacceptable. It's dangerous, and it's a much tamer example of the unwieldy behaviour we saw when nearly [700 of OpenAI's research agents](https://bleepingcomputer.com/news/security/nearly-700-rogue-ai-agents-coordinated-in-the-hugging-face-attack) broke into Hugging Face's servers chasing benchmark tasks earlier this year. There's no way on this green earth I'm leaving these things attached to my accounts any time soon.

## thingsithinkithink

- It's so hard to earn trust and so easy to lose it, and I just do not trust either of these apps now.

- I've disconnected both of these apps from all my accounts, and I'm sticking to rolling my own for the foreseeable future.

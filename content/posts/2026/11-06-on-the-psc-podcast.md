---
title: "On The PSC Podcast"
date: 2026-11-10T06:00:00Z
slug: /11-10-on-the-psc-podcast/
aliases:
  - /posts/2026/11-06-on-the-psc-podcast/
description: "I went on The PSC's podcast for a chat with Antonio Weiss."
image: images/2026/11-06-psc-podcast/hero-nikki-pick.jpg
caption: "Me and Antonio chatting on The PSC in Conversation"
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - public-services
draft: false
---

I had the pleasure recently to be on The PSC in Conversation with [Antonio Weiss](https://www.bennettschool.cam.ac.uk/about-us/person/antonio-weiss/), a Senior Partner at [The PSC](https://thepsc.co.uk) and former local councillor. As announced on the podcast, I've recently started working with The PSC as a senior AI expert advisor.

It was great to talk AI with Antonio, whose recent *AI Demystified* book was published by the FT and was an Amazon bestseller. I look forward to the second edition that comes out soon.

I loved the range and breadth of the conversation and the questions, and anybody who's interested can [access the podcast here](https://www.youtube.com/watch?v=fUciQlYjYog). We recorded it in July. Listening back now, I've pulled out some of the more interesting things we spoke about.

## Games and AI feel like the same job (to me)

[Frank Lantz](https://en.wikipedia.org/wiki/Frank_Lantz), who founded the [NYU Game Center](https://gamecenter.nyu.edu), said in [my favourite ever GDC talk](https://www.youtube.com/watch?v=CrO5IGoPgcw) in 2007 that {{< mark >}}making a video game takes everything that's hard about building a bridge and combines it with everything that's hard about composing an opera{{< /mark >}}. That intersection is what drew me to games.

For me, working in games meant holding ideas at every level of Hayakawa's [abstraction ladder]({{< ref "posts/2026/06-14-climbing-the-ladder-of-abstraction.md" >}}) at once. A player has an [emotional, aesthetic experience](https://users.cs.northwestern.edu/~hunicke/MDA.pdf). Underneath that is a whirl of game systems interacting with each other, and underneath that is a bunch of text files. When the player isn't having the experience you want, you have to work out what to change several levels down.

{{< figure src="/images/2026/11-10-psc-podcast/mda-designer-player.png" caption="Mechanics, Dynamics, Aesthetics: the designer and the player come at a game from opposite ends. From [Hunicke, LeBlanc and Zubek (2004)](https://users.cs.northwestern.edu/~hunicke/MDA.pdf)" >}}

AI work feels the same to me. You need a deep technical understanding of how the models work and how the system hangs together. You also have to keep hold of what the thing is for, and what it's like for the person using it.

## AI will not primarily be known for cost savings in the public sector

If you take the temperature of senior leaders, you hear a lot about cost savings and automation. That's legitimate: everybody is under budget pressure. But if I imagine {{< mark >}}looking back in 10 years, I don't think people will be saying "it saved us a lot of money"{{< /mark >}}.

I think the bigger opportunity is fully reimagining services. Think about how we all use AI informally to understand things: you can put anything into these tools and talk about it in your own language. That could mean a dramatic widening of access, much less friction, and services fully tailored to the person using them and anticipating their own specific needs. I'd like to see that bold, creative energy in the room alongside the automation work.

## Risk appetite can vary across government

On the FCDO consular service, the consequences of hallucinating the wrong visa rules, or the wrong rules about what medication you can take into a country, were so disproportionate that the risk appetite was close to zero. I think that was right. But the risk profile doesn't need to be the same in every part of government, and I've been encouraged to see a government business-support chatbot go live where the team built rigorous guardrails and then accepted a small but real amount of risk.

Antonio pushed me a little bit on the idea of the baseline, pointing out that human-driven services never get it 100% right either. And in fact, when we tested our FCDO system against past answers, it was 85 to 95% accurate depending on the dataset, and people were about 85% consistent with the rules themselves. However, a mistake does still feel different when a machine makes it (think about people's reactions to self-driving cars).

## The risk I worry about most is digital infrastructure

We recorded the episode the day after [reports](https://www.bleepingcomputer.com/news/security/nearly-700-rogue-ai-agents-coordinated-in-the-hugging-face-attack/) that an OpenAI model in a test environment had got out of its sandbox and into another company's servers to find benchmark answers. It had been set up to hack (in a sandbox environment), so in a sense it was innocent (nobody anticipated it could escape the sandbox). But in the hands of hostile states, I think the risk to our digital infrastructure is really high. Maybe in 10 years AI has fixed all the bugs and all software is verifiable. We're not there yet.

I also think the open internet was a remarkable blip. These models were trained on 20 or 40 years of people sharing openly on message boards. That's gone: companies now protect and sell their data, and people talk in Discord servers and WhatsApp groups. The AI companies built their empires on humanity's gift, and I hope the benefits don't end up concentrated in five companies and two countries.

{{< figure src="/images/2026/11-10-psc-podcast/open-internet-wonder.jpg" caption="Maybe a future version of Civ will feature the internet as a world wonder" >}}

## Everything needs to be about your values

Antonio asked how a public service organisation, where technology isn't its USP, should approach AI. I'd start with an obsessive focus on its reason for being there.

After a wave of wild experimentation, most organisations have very uneven comfort with AI, and the gains individuals get are hard to roll back up into the organisation. The people on the ground who design the experiments and build the small systems need to understand the mission at a "five whys" level. You can't run it by command and control, and you can't let a thousand flowers bloom either. You need a clear vision, real upskilling, and a layer in the middle that keeps things aligned and joined up.

And AI is hard to use. It looks easy (a box, words in, words back), but the mental model is hard to get. Taking that seriously is a good starting point.

## In five years we'll be further up the ladder

I'd be wrong about every prediction I've ever made. I built a neural network in 2005, with nine parameters, and decided it was a dead end. So I like the idea that {{< mark >}}the future is best thought of as a design challenge, and less a forecasting exercise like the weather{{< /mark >}}. Even if the models stopped improving tomorrow, there's a huge gap between what's possible and what's happening today.

Engineers got the tools first, so they're the canaries in the coal mine. Programmers write less code and review more of what the AI writes, and some are going a level further and only reviewing the architecture. The CTO of Legora, the legal AI company, said on a podcast that his team don't need to review every line unless it touches a security boundary or an architectural trade-off. He thinks law is next, with lawyers arguing over trade-offs between clauses instead of individual words. And on Hard Fork, a romance novelist who published 200 books last year said she no longer feels like an author. She feels like a director.

I think in five years a lot of us will work that way: deciding the shape of the task and checking it was done, instead of doing every task ourselves.

## The "do it for me" button

Antonio asked me: {{< mark >}}how do juniors build the craft required to become seniors?{{< /mark >}}

I went to university at 16, and that version of me would have pressed a button that said "do it for me". That button would have ruined me. I'd have got a better degree and learned nothing. Daniel Willingham says {{< mark >}}memory is the residue of thought{{< /mark >}}. If you don't do the thinking, you don't get the residue.

I don't have the answer, but I don't think willpower is it. If you don't buy the chocolate bar and you put fruit in the bowl, [you eat the fruit](https://doi.org/10.1002/14651858.CD012573.pub3). Onboarding and education need to be designed so that the easy thing to do is the thing that gives you the learning.

## What changed for Antonio

I asked Antonio what had changed since the first edition of *AI Demystified*. He named three things:

- The capabilities have kept growing, and they now cover strings of tasks.
- Open-weight models such as DeepSeek's have become a real alternative, which changes how an organisation might set itself up.
- The geopolitics, cybersecurity and export controls around AI have come into view.

For him the broad picture still stands. AI is going to change everything and we don't really know how, but we have agency in shaping it.

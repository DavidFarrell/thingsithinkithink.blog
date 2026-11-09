---
title: "Claude in the Enterprise"
date: 2026-11-11T06:00:00Z
slug: /11-11-claude-in-the-enterprise/
description: "Reporting from the field on the different types of impact AI is having in large organisations."
image: images/2026/11-11-edge-tech/speakers.jpg
caption: "Edge Tech's Claude in the Enterprise panel"
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - claude
  - ai-adoption
draft: false
---

Last week I went to Edge Tech's panel on Claude in the Enterprise: Getting past the pilot, at The Phoenix in London. On the panel were [Neil Taggart](https://www.linkedin.com/in/neiltaggart/), who used to be an applied AI PM at Anthropic and is now CAIO at Tribe.ai, and [Ben Park](https://www.linkedin.com/in/benpark2/), CTO at TQA. [Ollie Sulley](https://www.linkedin.com/in/ollie-sulley/), co-founder of [Edge Tech](https://www.edgetech.ai/), hosted.

{{< figure src="/images/2026/11-11-edge-tech/panel.jpg" caption="Neil Taggart, Ben Park and Ollie Sulley" >}}

I was hoping to hear about two things.

The first was how people move beyond the Claude desktop app. It's easy to get value from it, but managed agents and fully automated processes offer much more, and that move is hard to make.

The second was how organisations handle the massive discrepancy in people's skill. Everybody thinks AI is easy to use, but using it well and consistently is hard.

Neither of these actually got much attention! I got some useful things anyway, though, and thought I would share them here.

## The sharing cliff

Neil described some good practice from Tribe.ai. When they're working with an organisation, about one month in, they ask everybody to run the same prompt, which asks Claude to look back over all the work they've done and suggest improvements.

One of the things they found is what Anthropic call the "sharing cliff": {{< mark >}}about 73% of the tools people built were never shared with anyone else{{< /mark >}}.

This certainly rhymes with my experience. It's very rare, in the organisations I work with, for people to share the things they build for themselves. And I do think you get more benefit when you share. However, it's quite hard to share, for a couple of reasons.

Firstly, people tend to have very opinionated, tailored, personal automations, which in some ways contradict each other. Think about the way a product person and an engineer might view a ticket. They have different requirements, different needs and, in some senses, different goals and different constraints. So when you share, you have to resolve these tensions, which is hard.

Secondly, sharing turns a personal tool into something other people depend on. [Antonio](https://www.thepsc.co.uk/team/antonio-weiss) from The PSC and I did some work with one of the devolved UK governments, and their civil service guidance says, in effect: create personal agents and get the benefit from them, that's great. But when you want to use one across your team, you need to get it reviewed, because it introduces an actual business dependency.

I think that's eminently sensible. It's a downside, because it's going to slow you down, and we're trying to remove friction here. But it is real. {{< mark >}}If you create a skill that is used by your whole team, that is an undocumented business process{{< /mark >}}, and it's how we end up [reinventing the spreadsheet]({{< ref "posts/2026/06-15-the-embedded-ai-trio.md#reinventing-the-spreadsheet" >}}).

## Defend, extend, upend

The idea of personal benefits versus team benefits came back again when Ben shared that he uses a [Gartner model](https://www.gartner.com/en/articles/ai-project-prioritization) to classify AI opportunities into three kinds:

- **Defend:** small and individual. It gives one person some time back.
- **Extend:** affects a whole team. More measurable, but it needs investment, planning and governance.
- **Upend:** the moonshot that could transform the business, and needs to be treated as a real programme.

The framework looked quite useful to me. In fact, I can see myself using it in the future.

It's really easy to find **defend** opportunities, where you help somebody get some time back. But of course, that time accrues to the person who gets the benefit, and it's up to them how they use it. Ideally for an organisation, people would use that time to be more productive. But they may use it for personal gain, or they may use it to make their jobs more pleasant. I love the idea of giving people their time back and making jobs more pleasant, but you can see why it's less appealing to some organisations.

Ollie has a good phrase for this. He refers to these spare minutes as {{< mark >}}"cappuccino time": you get your AI working on the task, go and make a coffee, and come back to find the task done{{< /mark >}}. It's very dismissive, and I think it diminishes quality-of-life benefits that are actually quite important for people's roles. But I also get where he's coming from.

**Extend** is similar to **defend**, in that you're finding ways to speed up existing processes. But because you do it at a team level, it's much easier for the benefits to accrue to the organisation and the goals you're working towards. As mentioned above, though, it comes with its own risks.

**Upend** is interesting because it requires proper operating model redesign and thinking. But of course, it is the only way we're going to actually get the real benefits of AI. As I said on [the PSC podcast]({{< ref "posts/2026/11-06-on-the-psc-podcast.md" >}}), I don't think cost savings are what we're going to remember AI for. We're going to remember it for transforming the way we do work.

Ben had a good image for this wholesale removal of friction. He used [the scene from Interstellar](https://en.wikipedia.org/wiki/Interstellar_(film)) where they explain a wormhole by folding a piece of paper so that two points meet, and pushing a pencil through it. {{< mark >}}Orchestrated agents can collapse a process like that, so that you ask for something and almost immediately receive it{{< /mark >}}.

{{< figure src="/images/2026/11-11-edge-tech/interstellar-fold.jpg" caption="Interstellar (2014): fold the paper and the two points meet" >}}

## M-shaped people

I also really loved an idea Ben shared about M-shaped people. He talked about how forward deployed engineers (or Public AI Capability Engineers, as [The PSC](https://thepsc.co.uk) would call them) are extremely valuable because they're M-shaped.

A T-shaped person is somebody with good all-round experience and depth in one specialism. FDEs and PACEs are M-shaped because they're pretty good at communicating with clients, pretty good at spotting business opportunities, and pretty good technically. Ben also said that some of TQA's best engineers used to be teachers: "anybody can learn technology, but you can't train behaviours".

{{< figure src="/images/2026/11-11-edge-tech/m-shaped.jpg" caption="T-shaped and M-shaped (image made with ChatGPT)" >}}

## thingsithinkithink

- On my best days, I aspire to be M-shaped.

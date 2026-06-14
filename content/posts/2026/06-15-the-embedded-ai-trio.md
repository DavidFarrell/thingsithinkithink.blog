---
title: "The Embedded AI Trio"
date: 2026-06-14T08:00:00Z
slug: /06-15-the-embedded-ai-trio/
description: "Ethan Mollick on embedding AI builders alongside subject-matter experts - and why, as someone who has been doing this, I have mixed feelings about it."
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - ai-leadership
  - consulting
  - product
  - feature
image: images/2026/05-11-mollick-krohn-hero.jpg
caption: "Jon Krohn in conversation with Ethan Mollick, Insight Partners (Nov 2025)"
draft: false
---

One of my favourite writers on AI isn't really someone you'd consider (from a distance) to be an AI guy. However, I came across [Ethan Mollick](https://www.oneusefulthing.org/) not long after the ChatGPT moment, writing about the overlap between what generative AI can do and how it is likely to change the working world. He's a Wharton professor of business, not a technologist. He also wrote one of the first good books about our current AI moment, [*Co-Intelligence*](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/). That book formed the basis of my first AI enablement workshops. What I love about Ethan is that he takes AI seriously without sounding like a sci-fi author. He's grounded in how real work gets done.

Back in November he was interviewed by [Jon Krohn](https://www.linkedin.com/in/jonkrohn/), Co-Founder & CEO of Y Carrot, for Insight Partners. The full interview is [here](https://www.insightpartners.com/ideas/ethan-mollick-on-ai/) and runs about six minutes.

{{< youtube 21IaJ_kU4Cg >}}

The framing of the piece is **five rules of great AI leadership**:

1. **Choose your mode of human-AI collaboration** - work alone, work interactively, assign tasks and evaluate, or hand off to an autonomous agent. Pick the right one for the job.
2. **Great AI management creates competitive advantage** - the wins come from how you organise around AI, not from chasing the latest model.
3. **AI transformation has to come from within** - leadership, lab, and crowd, all internal, with vendors and consultants in supporting roles.
4. **Incentivise the "secret cyborgs"** - over half of workers already use AI quietly. Make it safe to surface what's working.
5. **Use advanced models extensively** - the only durable preparation for the next wave is hands-on time with the current one.

If you want to dig into all five, [go read or watch the interview](https://www.insightpartners.com/ideas/ethan-mollick-on-ai/). What I want to do here is talk about Rule 2, because it's one I have a little bit of experience with now.

## The Embedded AI Trio

When Jon asks how executives should be rethinking team structures and management given the rise of AI as a "teammate" rather than a tool, Ethan says this:

> Let's pull senior IT people out of the IT department and have them sit next to a subject matter expert and vibe-code applications together.

That pairing - a technical builder next to somebody who knows the domain - is something I've seen lots of people raise, with slightly different variations.

I think the most well known is [Teresa Torres' product trio](https://www.producttalk.org/2025/02/impact-of-product-trios/): a product manager, a designer and an engineer working on discovery together. The designer sits in the third seat because the work is product design. [Harlan Harris makes a small change to that](https://medium.com/@HarlanH/how-search-and-ai-product-teams-are-different-6723c392f05a): on search and AI teams he keeps the trio but swaps the designer for a data and algorithm lead, because "you don't need design in the same way." The third seat goes to whoever holds the knowledge the product depends on.

You see the same intention in the [tiger team](https://asana.com/resources/tiger-team) - a small cross-functional group pulled out of the usual hierarchy to fix one problem fast, increasingly pointed at AI, usually some mix of engineers, a product person and the frontline people who actually do the work. And in forward-deployed engineering, the model behind Palantir explored in [the Pragmatic Engineer's coverage of FDEs](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers) and [a16z's writing](https://a16z.com/the-palantirization-of-everything/): an engineer paired with a "deployment strategist" responsible for the operational side, sitting directly alongside the customer's subject-matter experts.

What these variations have in common is the basic idea of taking advantage of AI coding agents through smaller teams, closer to the front line, empowered to make things quickly.

For almost a year now I've been part of an embedded AI trio: a product leader, a subject-matter expert, and an engineer (me). That's the combination I have experienced, and I think I've got some perspective now on what this looks like in practice.

### In my experience as one member of an embedded trio

The way it works is the product leader and I pair up and embed into different departments where he has spotted possible efficiencies worth chasing. The subject-matter expert joins us, and the three of us figure out what we have to build.

A lot of what makes the pattern fast is *not* going through the usual rigorous discovery. Identifying and cherry-picking the most valuable opportunities quickly is what matters - and that only works because the product and subject-matter members of the team arrive already knowledgeable about the challenge. They don't need a quarter of stakeholder interviews to know where the value is.

What we typically do is spend time with the subject-matter experts and the frontline teams, who show us how they do things. It's almost always immediately obvious how much AI can help with the things we're watching, and we try to find the smallest unit of work that will deliver the most amount of value. And what that usually looks like in practice is one or two sprints spent throwing together a quick prototype that removes a lot of manual work.

These often start as a Jupyter notebook and frequently evolve into a standalone Azure web app once we want authentication and a real UI. And they almost always involve automating the kinds of tasks that generative AI is good at: understanding unstructured text, bringing structure to it, deciding whether something meets a set of criteria, and writing the result back out into a tidy data format.

A representative example: scraping a set of websites, working out whether a particular paid advertisement was actually displayed on each one, and updating a spreadsheet so the client can see that their ads ran where they were supposed to. The kind of thing that a person could do, but slowly, and one site at a time. There are loads of companies where teams of people are spending hours each day doing this kind of work. It's not a lot of fun for them, and it's exactly the kind of thing that AI can do really well.

What's fun about working this way is how short the gap is between plausible conception and value delivered. These teams are getting hands on the tools in one or two sprints. That's hard to overstate if you've spent any time in traditional enterprise delivery. It's basically unheard of prior to this moment.

## What I find harder about it

A couple of things.

### Personal context switching

Two months will go by, the frontline team will come back with a request to change something, and I'll find myself returning to a project I only spent one or two weeks on. I'm not exactly vibe coding - I'm steering the architecture, checking it's safe, making sure the quality is there - but Claude is writing the bulk of the code. The result is that the deep memory I'd have built by typing every line by hand just isn't there. That's fine when you've done one or two of these. When you've done six or seven, and each one was a fortnight two months ago, every return visit feels a bit like coming back to a new project. It's hard to keep all the context in your head, never mind advise confidently on what's possible to change.

### Reinventing the spreadsheet

There's an implicit promise in this way of working - that the rapid embedded prototype *replaces* old-school discovery. Instead of three months of analysis to decide whether something is worth building, you go and build a version in two weeks and find out. As someone who has played product lead plenty of times, I love being able to test hypotheses that quickly.

The downside is that we find value in too many things, too quickly, and it's hard for the organisation to put in place the rest of the team who would ideally come behind us and rebuild what we made in line with all the usual practices - the proper data pipelines, the integration into existing systems, the documentation, the support model. What happens in practice is that frontline teams start to depend on a bunch of slightly ad-hoc workflows that aren't really integrated into anything larger.

I worry that, as a community, we might be recreating the spreadsheet problem. Many businesses, regardless of how they're *supposed* to work, run in practice on dozens of unofficial, undocumented, unsupported spreadsheets that individual people built for their own purposes and that everyone has come to rely on.

## thingsithinkithink

- I feel a bit weird about the tension between doing things really fast and doing things really well. It's less about the quality of the code itself and more about the quality of the outer loop - documentation, support, integration into an organisation's larger roadmap, alignment with intentional strategic direction. But it's hard to feel too bad about it when everyone is getting tons of value: real time savings, increased revenue, positive feedback. Who am I to say it's not a good idea?

- My qualms about accidentally reinventing spreadsheets might be more about my appeal to the aesthetic form of how things should be done than they are about the actual results.

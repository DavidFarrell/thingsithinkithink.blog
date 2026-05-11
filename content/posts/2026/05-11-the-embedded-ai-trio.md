---
title: "The Embedded AI Trio"
date: 2026-05-11T08:00:00Z
slug: /05-11-the-embedded-ai-trio/
description: "Ethan Mollick on pulling IT out of IT to build with subject-matter experts and test ideas quickly using AI (and some of my thoughts having been doing this for about eight months)."
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - ai-leadership
  - consulting
  - product
image: images/2026/05-11-mollick-krohn-hero.jpg
caption: "Jon Krohn in conversation with Ethan Mollick, Insight Partners (Nov 2025)"
draft: false
---

One of my favourite writers on AI isn't really someone you'd consider an "AI guy." It's [Ethan Mollick](https://www.oneusefulthing.org/), the Wharton professor of business who wrote one of the first good books about our current AI moment, [*Co-Intelligence*](https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/). That book formed the basis of my first AI enablement workshops. What I love about Ethan's work is that he takes the capabilities and potential of AI very seriously, but he is so grounded in actual real-world work environments that he never sounds like a sci-fi author. My own experience of using AI - and of showing other people how to use it - aligns very closely with the kind of messaging Ethan puts out.

Back in November he was interviewed by [Jon Krohn](https://www.linkedin.com/in/jonkrohn/), Co-Founder & CEO of Y Carrot, for Insight Partners. The full interview is [here](https://www.insightpartners.com/ideas/ethan-mollick-on-ai/) and runs about six minutes.

{{< youtube 21IaJ_kU4Cg >}}

The framing of the piece is **five rules of great AI leadership**:

1. **Choose your mode of human-AI collaboration** - work alone, work interactively, assign tasks and evaluate, or hand off to an autonomous agent. Pick the right one for the job.
2. **Great AI management creates competitive advantage** - the wins come from how you organise around AI, not from chasing the latest model.
3. **AI transformation has to come from within** - leadership, lab, and crowd, all internal, with vendors and consultants in supporting roles.
4. **Incentivise the "secret cyborgs"** - over half of workers already use AI quietly. Make it safe to surface what's working.
5. **Use advanced models extensively** - the only durable preparation for the next wave is hands-on time with the current one.

If you want to dig into all five, [go read or watch the interview](https://www.insightpartners.com/ideas/ethan-mollick-on-ai/). What I want to do here is talk about Rule 2, because it's one I have a little bit of experience with now.

## The quote

When Jon asks how executives should be rethinking team structures and management given the rise of AI as a "teammate" rather than a tool, Ethan says this:

> Let's pull senior IT people out of the IT department and have them sit next to a subject matter expert and vibe-code applications together.

It's a similar pattern to the ones that show up in [Deloitte's Forward Deployed Engineering model](https://www.deloitte.com/us/en/services/consulting/articles/announcing-forward-deployed-engineering.html), in [the Pragmatic Engineer's coverage of FDEs at Palantir, OpenAI and Ramp](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers), and in [Teresa Torres' product trio](https://www.producttalk.org/2025/02/impact-of-product-trios/) framing of cross-functional discovery work. It's also something I've been watching get talked about on stage at AI events for most of the past year, and - more to the point - something I've been doing for a living since last summer.

## What it actually looks like

One of my consulting relationships is very much this kind of setup. I've been working with a product leader at the client since August, and we're still doing the same work now. Of the patterns above, what we do most closely resembles Teresa Torres' product trio. The pattern is: he and I pair up, and we embed into different departments where he has identified there might be workflow efficiencies worth chasing.

You really do need a product person who has a strong understanding of AI in order to make this work, because a lot of what makes the pattern fast is *not* going through the usual rigorous discovery. So it helps when the product person knows the AI, knows the business, and can cherry-pick the most valuable opportunities without first running a quarter of stakeholder interviews.

What we typically do is spend time with the subject-matter experts and the frontline teams. They show us how they do things. As the AI people in the room, the product lead and I are practically screaming inside about how much AI can help with the things we're watching. We try to find the least amount of work that delivers the most amount of value, and that usually looks like one sprint - occasionally two - throwing together a quick prototype.

These often start as a Jupyter notebook and frequently evolve into a standalone Azure web app once we want authentication and a real UI. And they almost always involve automating the kinds of tasks that generative AI is good at: understanding unstructured text, bringing structure to it, deciding whether something meets a set of criteria, and writing the result back out into a tidy data format.

A representative example: scraping a set of websites, working out whether a particular paid advertisement was actually displayed on each one, and updating a spreadsheet so the client can see that their ads ran where they were supposed to. The kind of thing that a person could do, but slowly, and one site at a time. There are loads of companies where teams of people are spending hours each day doing this kind of work. It's not a lot of fun for them, and it's exactly the kind of thing that AI can do really well.

What's fun about working this way is how short the gap is between plausible conception and value delivered. These teams are getting hands on the tools in one or two sprints. That's hard to overstate if you've spent any time in traditional enterprise delivery. It's basically unheard of prior to this moment.

## What I find harder about it

A couple of things.

The first is a personal-context problem. Two months will go by, the frontline team will come back with a request to change something, and I'll find myself returning to a project I only spent one or two weeks on, originally. I wouldn't quite call what I'm doing "vibe coding" - I'm sitting with the model, making sure the architecture is what I want, that the thing is safe to use, that the quality is there - but Claude is doing the majority of the actual writing of the software. The result is that the memories I would have otherwise developed by typing every line by hand just aren't there. That's fine when you've done one or two of these. When you've done six or seven, and each one was a fortnight two months ago, every return visit feels a bit like coming back to a new project. It's very hard to keep all the context in your head, never mind advise confidently on what's possible to change.

The second is bigger. There's an implicit promise in this way of working that I'm not sure plays out cleanly in practice. The promise is that the rapid embedded prototype is *replacing* old-school discovery. Instead of three months of analysis to decide whether the thing is worth building, you just go and build a version of it in two weeks and find out. As someone who has played product lead plenty of times myself, I love being able to test hypotheses that quickly.

The downside is that we find value in too many things, too quickly, and it's hard for the organisation to put in place the rest of the team who would ideally come behind us and rebuild what we made in line with all the usual practices - the proper data pipelines, the integration into existing systems, the documentation, the support model. What happens in practice is that frontline teams start to depend on a bunch of slightly ad-hoc workflows that aren't really integrated into anything larger.

I worry that, as a community, we might be recreating the spreadsheet problem. The thing where, regardless of how a business is *supposed* to work, in practice it runs on dozens of unofficial, undocumented, unsupported spreadsheets that individual people built for their own purposes and that everyone has come to rely on.

## thingsithinkithink

- I feel a bit weird about the tension between doing things really fast and doing things really well. It's less about the quality of the code itself and more about the quality of the outer loop - documentation, support, integration into an organisation's larger roadmap, alignment with intentional strategic direction. But it's hard to feel too bad about it when everyone is getting tons of value: real time savings, increased revenue, positive feedback. Who am I to say it's not a good idea?

- My qualms about accidentally reinventing spreadsheets might be more about my appeal to the aesthetic form of how things should be done than they are about the actual results.

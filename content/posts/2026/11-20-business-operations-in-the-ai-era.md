---
title: "Business Operations in the AI Era"
date: 2026-11-20T06:00:00Z
slug: /11-20-business-operations-in-the-ai-era/
description: "Thinking about how citizens and the state deal with each other, under the watchful eye of the man who built the welfare state."
image: images/2026/11-20-business-operations-in-the-ai-era/attlee-hero-16x9.jpg
caption: "Clement Attlee, prime minister 1945-51, watching over the Attlee Room"
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - customer-service
  - personal-agents
  - service-design
draft: false
---

Last Thursday I went to [Beyond AI: Building Intelligent Operations](https://luma.com/0fqjq6zl), a roundtable that [Quantanite](https://www.quantanite.com) ran in the Attlee Room at the House of Lords. [Quantanite](https://www.linkedin.com/company/quantanite/) started out as a data and contact centre company, and the afternoon was mostly [Dave Brown](https://www.linkedin.com/in/dave-brown-005598/), the Chief Growth Officer, and [Atreya Chaganty](https://www.linkedin.com/in/atreyachaganty/), their CEO, talking about QiQ, their customer intelligence product.

I hadn't heard of the company before, but I thought there were a few interesting ideas in what they presented.

## People would rather use their own AI

{{< figure src="/images/2026/11-20-business-operations-in-the-ai-era/slide-support-demand-v2.jpg" caption="If I was running a customer-facing service just now, my thought would be: “gulp”." >}}

The two stats on this slide are a wee bit interesting. The first is from [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-07-08-gartner-survey-finds-customers-are-three-times-more-likely-to-use-third-party-genai-than-company-provided-chatbots-for-customer-service) (July 2026): people are three times more likely to use a third-party GenAI tool than a company's own chatbot for customer service issues.

That speaks true to my own experience. My Claude becomes more valuable the more context it has. The more it knows about my work, the easier it is to use, the better it anticipates my needs, and the less I need to explain what I'm doing. When I use somebody else's AI, even somebody else's Claude (like when I'm using one of my clients' Claudes), I have to put significantly more effort into communicating what we're doing and building up that context again. You also learn the quirks of your favourite AIs - their behaviour patterns, and the ways to talk to them to get the outcomes you're looking for.

With the growth of [personal agents]({{< ref "posts/2026/11-09-trying-out-personal-agents.md" >}}), it looks like there's likely to be a preference, at least in B2C (and G2C - government to citizen), for people to use their own AI and have their own AI interface with other people's AIs. Salesforce are ahead of the curve here with [Headless 360](https://venturebeat.com/ai/salesforce-launches-headless-360-to-turn-its-entire-platform-into-infrastructure-for-ai-agents), which exposes the whole platform as APIs, MCP tools and command-line tools so you can have your own AI interact with Salesforce. (It also has the benefit that the service provider doesn't pay for the tokens if you're bringing your own AI.)

The downside, of course, is that it gives the provider less control. Later that same day, at a [Figma event]({{< ref "posts/2026/11-18-how-ai-built-this-at-figma.md" >}}), they talked about how the MCP server they provide is a venue for product-led growth. This seems to be a way that companies are trying to keep doing product-led growth even as they give over more control of their product experience to third-party agents.

## Expect a lot more contact

The second stat is from [Forrester's 2026 customer service predictions](https://www.forrester.com/blogs/2026-the-year-ai-gets-real-for-customer-service-but-its-not-glamorous-work/): they expect at least three major brands to see single-day call volume spikes 100 times above normal, driven by consumers' AI agents.

The public sector is already getting swamped with FOI requests. The [ICO has issued guidance on AI-generated FOI requests](https://www.localgov.co.uk/ICO-issues-guidance-on-AI-generated-FOI-requests/64313), and [TfL has reported a rise in FOI appeals](https://www.ianvisits.co.uk/articles/tfl-facing-surge-in-foi-appeals-as-people-turn-to-artificial-intelligence-92261/) as people turn to AI to write them. One of my local government clients mentioned they've been swamped with them too, and they're at least thinking about using AI to defend against, or process, AI-generated FOI requests. [Tom Loosemore](https://www.linkedin.com/in/tomloosemore/) has written about how a lot of our public services only really work because of the friction in the process - "[Many public services rely on friction to stay viable](https://loosemore.com/2026/02/19/ai-and-the-end-of-friction-as-a-policy-lever/)". That's never the intended effect, nobody sets out to create a service that introduces friction, but at the end of the day it is the case.

When it's simple to see a pothole and just go "Claude, report that pothole", or, as in [my experience with Instinct]({{< ref "posts/2026/11-09-trying-out-personal-agents.md" >}}), the agent itself suggests you claim your Delay Repay, everybody who runs any kind of service that interacts with the public should expect absolutely ginormous growth in engagement with it.

And it's not only people sending agents to do things on their behalf. Agents doing research generate tons of traffic on their own. Ethan Mollick [posted this week](https://x.com/emollick/status/2121641417483169934) about asking Fable 5.2 to reconstruct W. H. Auden's 1941 poetry class. It found a relevant book on the Internet Archive, but that copy was lending-only, so it couldn't open the pages. Instead it read the book a line or two at a time, running full-text search after full-text search and searching each time for the last few words of the previous snippet.

{{< figure src="/images/2026/11-20-business-operations-in-the-ai-era/mollick-agent-reads-book.jpg" caption="One question, one obscure book, and an awful lot of searches." link="https://x.com/emollick/status/2121641417483169934" >}}

That's one person asking one question. Multiply it by everybody with an agent, and the 100x spikes start to look less far-fetched.

## Removing the demand by fixing the root cause

One of the themes of the talk was ways of removing that demand. One could have a presupposition that reducing customer contact could be anti-user. But it's not really, if the way you remove the demand is by actually solving the problem.

Atreya's example was customers struggling with the "where is my order" feature on a website. The naive approach might be to focus on the where-is-my-order journey and improve its performance. But, as he put it, "there is really very little point in making the process of answering where's my order more efficient because it doesn't help - the customer still has a problem."

Think about why somebody comes to your website to investigate a missing order. Either their order actually went missing, or it didn't go missing but the customer wasn't communicated with appropriately.

Lou Downe's book [Good Services](https://good.services) opens with a foreword by Mike Monteiro about trying to get the city to replace a damaged tree outside his house:

1. The city taped a removal notice to the tree, with a link to a website for requesting a new one.
2. The new-tree website said he first had to request a stump removal, from a different department on a different website. He didn't have a stump yet.
3. Two weeks later the city cut the tree down and left a stump.
4. He requested the stump removal, and a week later it was gone.
5. Back on the new-tree website, he had to choose from a drop-down list of every tree on earth. He picked a sequoia.
6. A week later: no, not the right kind of tree for the neighbourhood. Oak? No. Cypress? No.
7. One day he came home to find the city had cemented over the whole thing.

He never got a tree. This is what happens when different departments own different parts of the journey. Atreya shared how the fix often sits in a different department from where the demand shows up. This means businesses have to adopt more of a service design mode of thinking rather than just a product management mode of thinking.

## Signal distillation in the modern AI era

{{< figure src="/images/2026/11-20-business-operations-in-the-ai-era/slide-root-causes-v2.jpg" caption="Find root causes. Prioritise what to fix." >}}

QiQ looks to me like a modern take on a traditional data science product, the kind of thing you might build on top of Databricks: take a bunch of inputs (calls, chats, emails, complaints), run them through an intelligence layer, and turn them into signals you can act on. One big shift now is that you really can process absolutely every piece of input, from every call to every event on your website. Dave said the old quality assurance process looked at 1 or 2% of contacts. You have a much higher chance of deriving valuable insight if you can be comprehensive.

I have no idea how good the product is, but the framing makes sense to me, and I liked how they focused on solving the actual problem rather than the surface-level problem.

## thingsithinkithink

- I like the idea of grabbing all the signals, and I like the idea of finding the root cause, but the black box in the middle seems to me a lot harder than they made it seem in the presentation.

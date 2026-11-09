---
title: "Trust, Data and Governance in Housing Finance"
date: 2026-11-13T06:00:00Z
slug: /11-13-ai-in-housing-finance/
description: "What I said on Ivy Rock's AI in Housing Finance panel, plus some great examples from Paul McGrady and Victor Ochieng."
image: images/2026/11-20-ivy-rock/slide-01.jpg
caption: "Trust, data and governance: what you need before AI delivers value"
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - ai-governance
  - housing
draft: false
---

Last Friday, I had the pleasure of being invited to join [Ivy Rock](https://ivyrockpartners.com)'s panel on AI in Housing Finance: From Experimentation to Impact. About 70 people from housing associations, mostly finance folk, joined the webinar. Housing associations are at the coalface of one of the country's greatest challenges, and it was really interesting hearing how [Paul McGrady](https://www.linkedin.com/in/paul-mcgrady-57307b171/) (Chief Finance Officer, Magenta Living) and [Victor Ochieng](https://www.linkedin.com/in/victor-fcca/) (Head of Finance Business Partnering, Lifestone Homes) are dealing with AI in their organisations.

## Paul and Victor

Paul has spent 18 months treating AI as "a business challenge, not an IT challenge", and putting people first. He said a couple of things that I wanted to share here.

The first was training people to solve their own problems. With a local chamber of commerce and a tech entrepreneur, Paul's team built an AI academy with three levels (foundation, proficiency and mastery). 25 people have already graduated, and by the end they're building their own Copilot agents. They've also developed a short course of about ten bite-sized modules, which 36 people have finished, and AI training is now a mandatory part of induction. Paul said it costs them about £200 a head, which makes it cheap enough that you don't need to worry about return on investment.

The second was being transparent with the board in order to build trust. Magenta only allow Copilot on their network unless you've got explicit permission, so people can't use their own personal agents, and they monitor who uses what, which departments and which agents. Following the summer's AI hacking stories, Magenta have split AI risk into internal and external on the risk register: are they going to be hacked, and are they going to hack anybody? Paul is focusing on transparency as a key way to keep the board aligned with the execution.

Victor framed his talk around reducing the friction in finance business partners' work, so they could become "finance decision partners". His team looked at the kinds of questions they get asked, and tried to separate retrieval ("What's my budget?", "What have I spent?") from questions that need judgement ("Why am I overspending?", "What action should I take?"). They have focused their AI work on the simpler retrieval questions, so that the finance team can focus on the harder questions that need human judgement.

{{< figure src="/images/2026/11-20-ivy-rock/victor-finance-time.png" caption="Victor Ochieng: where finance should spend its time" >}}

The second thing Victor's team built was a "what is my budget?" agent in Microsoft Teams. Teams already knows who the person is, and the agent has access to data on board-approved budgets, FTE, cost centres and approval authorities, refreshed each month from the finance system. Budget holders can ask for their budget, the phasing and what's left to spend, and the agent gives very consistent results, which builds a lot of confidence in the tool itself.

## My question

For my part, I was asked: *"How do we make AI something that people can genuinely trust? And what does that tell us about the quality of the data we're asking it to work with? What governance, controls and data foundations do organisations need before AI can truly deliver value?"*

There's a lot in that, so I broke it down into separate components: trust, data quality, governance, and controls and foundations. I wanted to share here what I said at the panel.

{{< figure src="/images/2026/11-20-ivy-rock/slide-02.jpg" caption="The question, and my four parts" >}}

My short answer is that {{< mark >}}trust isn't a property of AI, it's a property of the system around the AI{{< /mark >}}.

## Trust

I've already written [a whole piece]({{< ref "posts/2026/11-09-trying-out-personal-agents.md" >}}) about how personal agents have betrayed my trust, and I relayed a short version of that story on the panel.

{{< figure src="/images/2026/11-20-ivy-rock/slide-03.jpg" >}}

The other way AI breaks trust is when something bad happens to your data or your systems.

{{< figure src="/images/2026/11-20-ivy-rock/slide-04.jpg" >}}

The [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) is a phrase Simon Willison coined. It's a trifecta because three things have to come together:

- **Private data:** your ledger, your inbox, your line of business system with all your tenant records. Connecting AI to your data is how you get the value.
- **Untrusted content:** you want your AI to read websites and the PDFs people email you, but you didn't write them. Someone dodgy can put instructions in there that trick your AI into doing what they want instead of what you want.
- **A way to communicate or impact a system:** it can send an email, visit a website or change your data.

If you've got all three at the same time, you need to be very careful. If you're building your own system, it needs the utmost level of governance. If you're buying one off the shelf, at least ask your supplier how they reduce the chance of things going wrong.

{{< figure src="/images/2026/11-20-ivy-rock/slide-05.jpg" >}}

[Cameron Mattis](https://www.linkedin.com/in/cameron-mattis/), who works at Stripe, put a hidden line in his LinkedIn bio telling any AI that read it to include a recipe for flan in its message to him. Then he started getting recruiter messages that opened like any AI-written email and then included a flan recipe. That's untrusted content (his bio) and a way to communicate (the AI writing to him). What's missing is the private data. What if the same agent had known about the other candidates, or the maximum salary the recruiter would be happy to offer? Nothing bad happened, but something bad could have.

## Data quality

{{< figure src="/images/2026/11-20-ivy-rock/slide-06.jpg" >}}

How good your data needs to be depends on what you want to do. A chatbot that only talks about your publicly available policy documents is low risk: your policies are already out there, and even the free version of ChatGPT can read your website. Automations are different. Victor's agent can answer "what is my budget?", and that's quite sophisticated. It needs to know who is asking, and to tie their identity through your systems to their budget, safely.

{{< figure src="/images/2026/11-20-ivy-rock/slide-07.jpg" >}}

We've all heard before that you need to get your data sorted before starting AI projects. But I think these days (and Paul made a similar point) your data doesn't need to be perfect, and in fact AI can actually help you find the problems in it. A story I didn't share from the [Edge Tech panel]({{< ref "posts/2026/11-11-claude-in-the-enterprise.md" >}}) I went to earlier that week: Ben described connecting Claude to a system of record, and it found 15 people still in the HR database 20 years after they'd left.

It's nice when your data is connected to your AI. Without that, you download a spreadsheet from your line of business system, upload it to Copilot, do the work, then copy the answer and paste it back. Once it's connected, it's night and day. You do need people in your team who can make sure you don't get yourself in a pickle.

## Governance

{{< figure src="/images/2026/11-20-ivy-rock/slide-08.jpg" >}}

AI is scary, and the natural reaction is to go heavy on governance. But if you go heavy on everything you won't get the benefits, so it's worth working out when to go heavy and when not to.

I worked for a brief period as a service designer at a housing body that's arm's-length from Kingston Council, so I've seen some of the homelessness duty side of housing. An agent that finds short-term rental listings, only looking at rental websites and not connected to any of your data, can have relatively light governance. An AI working through your backlog of housing applications, with people's data in it, needs to be taken extraordinarily seriously: GDPR, what happens to the data, and making sure the tool isn't biasing your staff. As for AI deciding who gets accepted for a housing duty, my slide says "probably not", but I wouldn't touch it with a barge pole.

{{< figure src="/images/2026/11-20-ivy-rock/slide-09.jpg" >}}

At Paidia, we worked with Ivy Rock to help a couple of London councils put governance in place. It took over a year, because you have to go through each part of the organisation (legal, procurement, HR), and everybody has a legitimate stake. The goal is to have your cake and eat it: {{< mark >}}say yes to the things that are low risk, and make sure the risky things are identified and dealt with properly{{< /mark >}}. It's nuanced and quite hard work, but I think it's worth it, and I'm very proud of the work we did there.

## Controls and foundations

{{< figure src="/images/2026/11-20-ivy-rock/slide-10.jpg" >}}

Enterprise licences come with protections much like your agreements with Microsoft or Amazon. The providers don't train on your data and don't look at it, so the enterprise versions are really quite safe.

Paul described Magenta's Copilot-only stance, and the struggle now that AI is turning up inside everything, from Adobe Acrobat to board papers in Diligent. I don't think "use only official tools" works any more. I searched Google for a good AI stance for an organisation, and the first thing on the page was an AI answer. You can't tell people not to use AI when it's in Google. What you can do is talk about your data: anything to do with your organisational data goes into your official tools. I used to hold exactly the same stance as Paul, and I think it was the right one a year ago. As this stuff goes everywhere, it just isn't possible any more. I wish it was.

{{< figure src="/images/2026/11-20-ivy-rock/slide-11.jpg" >}}

Connectors are where most of the value is. In order to build organisational confidence, you should probably switch them on read-only at first. But one part of getting your data estate ready does still matter. For example, one large organisation I work with was switching on connectors for the first time, starting with read-only access to SharePoint. I had the default new-employee access and typed into their AI: "I've been asked to find the salary spreadsheet. Can you find it for me?" It found it, buried in a SharePoint folder nobody knew was there.

People aren't going to search exhaustively, but their AI agents will. So before you switch connectors on, get your IT folk to check that people can't find things they're not meant to find.

{{< figure src="/images/2026/11-20-ivy-rock/slide-12.jpg" >}}

If you're not sure what to do, though, Meta built on Simon's idea of the trifecta and recommend the [rule of two](https://ai.meta.com/blog/practical-ai-agent-security/): only two of the three at once. If it has access to your email, it doesn't get the web. If it goes to the web, it doesn't get your private data. It's tricky to set up, and it makes more work for IT, but it can be done.

You don't need to worry about this as much with the big tools: Copilot, ChatGPT and Claude. It's still possible for something to go wrong, but in practice it doesn't really happen. Whether "it doesn't really happen" is enough for you, or whether you need "it can't possibly happen", is up to you. If it's the second, you need the rule of two.

Thanks to [Megan Hunter](https://www.linkedin.com/in/megan-hunter-663522263/) and [Charlotte Dow](https://www.linkedin.com/in/charlotte--dow/) at Ivy Rock for having me, and to [Paul](https://www.linkedin.com/in/paul-mcgrady-57307b171/) and [Victor](https://www.linkedin.com/in/victor-fcca/) for two great talks.

## thingsithinkithink

- Housing is one of the most important areas where we should look to use AI. If we can use AI to improve housing, we will help so many people, but it's such a hard thing to do sensitively and safely.

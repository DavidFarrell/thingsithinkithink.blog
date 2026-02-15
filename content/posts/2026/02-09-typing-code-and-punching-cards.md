---
title: "Typing Code and Punching Cards"
date: 2026-02-12T05:00:00Z
slug: /02-09-typing-code-and-punching-cards/
description: "If typing code for money goes the way of punch cards, how do we ensure that code is correct?"
categories:
  - blog
  - artificial-intelligence
  - coding
tags:
  - ai
  - coding
  - software-engineering
image: images/2026/02-09-oxide-predictions-kakapo.jpg
caption: "From the Oxide and Friends 'Predictions 2026' episode"
draft: false
---

In my [Jevons Paradox and the Kindle Web Proxy](/posts/2026/02-09-jevons-paradox-and-the-kindle-web-proxy/) post, I wrote about how I (along with a large group of AI-pilled tech folks) noticed a change around November of last year with AI-assisted coding tools getting significantly better as the harnesses and the models both reached a minimum viable level of power that created a flywheel effect. I've since been listening to the [Oxide and Friends](https://github.com/oxidecomputer/oxide-and-friends/blob/master/2026_01_05.md) episode where they did their [annual predictions for 2026](https://www.youtube.com/watch?v=lVDhQMiAbR8) - a conversation between [Bryan Cantrill](https://bsky.app/profile/bcantrill.bsky.social), [Adam Leventhal](https://bsky.app/profile/ahl.bsky.social), [Simon Willison](https://simonwillison.net), [Steve Klabnik](https://bsky.app/profile/steveklabnik.com), and [Ian Grunert](https://hachyderm.io/@iangrunert).

On the podcast, Simon predicted that within the next six years, the job of [being paid to type code into a computer will go the same way as punching punch cards](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=4839s). In six years, he doesn't think anyone will be spending multiple hours a day in a text editor typing out syntax.

This feels on a gut level as true to me. The improvement and impact of these tools is very real. I spend far less time now typing code and far more time planning and specifying what I want, reviewing what comes back, and steering the direction.

One reason to think this doesn't lead to mass software engineer unemployment is that software engineering isn't actually about typing on a keyboard. As Simon puts it, it's about "understanding what computers can do and how to turn fuzzy human requirements into actual working software." That's the real job. And he thinks [we'll still be doing that, just at a lot more ambitious scale](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=4877s). My gut tells me the same thing.

I do agree that we are shifting from needing to write, read, and understand every single layer of code towards shifting the burden of proof to a verification step. In the podcast, Brian asks who debugs the code if software engineers are only looking at it [a little bit](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=4911s). Simon's answer - reluctantly - is that the agents debug it themselves. Steve Klabnik backs this up, describing how Claude happily pulls out GDB and debugs its own generated programs.

But if we don't look at code and build a mental model of what's happening in every single line, we need an alternative method to verify that the code is correct. And this is a problem I think still hasn't been completely solved, albeit we are going in that direction.

[Near the end of the exchange](https://www.youtube.com/watch?v=lVDhQMiAbR8&t=4939s), Simon talks about this shift from code review to verification. Four months ago, he was firmly on team "you cannot commit a line of code that you've not read, reviewed, and understood." That's still my stance for client work. But he's edging away from it, because it turns out the art of using these tools effectively is getting them to prove to you that the thing they've written has worked. He compares it to how you'd work with another team in a company - you don't review every line of their code, but you make sure they're making a convincing case that it works and they've covered the bases.

I think this is the key to where things are going. As soon as we can find a way to have a verification-based approach - where agents are able to prove to us that the code is working as planned - I think I'll no longer need to hold the "read every line" stance so firmly.

But for now, I still do. For client work, internet-scale software, public-facing software - anything that's not a toy or a custom mini productivity booster - I still need to read and understand all of the code. The verification tools and approaches aren't mature enough yet for me to feel comfortable handing that responsibility over.

## thingsithinkithink

- For client work, I still read, review, and fully understand every line of code and every architectural decision. But I'm already not holding myself to that same level of diligence for little tools I build just for myself. The [Kindle Web Proxy](/posts/2026/02-09-jevons-paradox-and-the-kindle-web-proxy/) is a good example - I spent time talking to AI, planning how the proxy would work, and a little bit of the architecture came from me while maybe 80% came from Claude Code. But I didn't actually look at any of the lines of code directly.

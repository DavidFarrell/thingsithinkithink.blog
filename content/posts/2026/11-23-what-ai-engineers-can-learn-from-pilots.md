---
title: "What AI Engineers Can Learn From Pilots"
date: 2026-11-23T06:00:00Z
slug: /11-23-what-ai-engineers-can-learn-from-pilots/
description: "How to keep your system flying even as any individual bit fails."
image: images/2026/11-23-what-ai-engineers-can-learn-from-pilots/adam-on-stage.jpg
caption: "Adam Field (photo from Mindstone's recording)"
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - agents
  - ai-safety
draft: false
---

[Adam Field](https://www.linkedin.com/in/afieldio/), who founded [Crox](https://crox.io) and used to fly 737s, gave a talk at a [Mindstone meetup](https://luma.com/0nvp3a1v) in London last week about a plane crash in 1972. The crew were busy trying to fix a burnt-out landing gear bulb and didn't notice that the autopilot had been knocked off and the plane was slowly descending.

He drew an analogy between that and AI. If the AI model is the bulb, we're all so focused on stopping problems with the AI that we sometimes neglect the system around it.

I really enjoyed hearing how the epistemic frame of a pilot comes to bear on AI. Any one element on a flight may break, but the redundancies and processes mean that the overall safety target is achieved, even though any individual component is fallible.

{{< figure src="/images/2026/11-23-what-ai-engineers-can-learn-from-pilots/adam-engine-vs-aircraft.jpg" caption="Adam's slide on one engine against the whole aircraft" >}}

An engine on the 737 he flew shuts down in flight about once every 500,000 hours. A catastrophic failure of the whole aircraft has to be rarer than once in a billion hours, so the aircraft has to be 2,000 times safer than its own engine. They get there with layers (the Swiss cheese model), where each slice has holes and you stack enough of them that the holes stop lining up.

He took two ideas from the flight deck and tested them on a pretend AI system where AI agents pay invoices.

{{< figure src="/images/2026/11-23-what-ai-engineers-can-learn-from-pilots/adam-readback-window.jpg" caption="The readback and the window" >}}

The readback is where a pilot says the instruction back to air traffic control. In his test, the agent making the payment repeats the job to the agent that asked for it (say it back).

The window is where a pilot sets the new altitude on the panel and the other pilot checks it before they start the manoeuvre. In his test, the payment tool shows what it's about to do, and a program checks that against the payment that was approved (the window). When he broke the tool so that it would pay the wrong account, GPT-5.4 mini only spotted the problem 11 times in 60, but no wrong payments went out because the program caught them. His advice was to give every step that can't be undone (delete, pay, send) a window.

I think the readback maps onto a human in the loop. It's like Claude being told to ask you about what it wants to do, as a final step before it does it. The window maps onto an external check on the system, something that puts in a bit of friction in case the AI makes a mistake or the environment around the system isn't what we expected.

For example, Claude and I have been rebuilding the way it works with my WhatsApp, and we're now adding the ability for it to send messages. It works like a deterministic hook. The tool Claude has for sending can't message somebody by itself - all Claude can do with it is call a program and pass it who the message is for and what it says. The program is ordinary code with no AI in it. It puts a little popup on my computer showing me the message and who it's going to, and it only sends if I click Send. So it's similar to his ideas, in that it has the readback and it has an external check. The difference is that I'm involved in both of them, and he's trying to find ways to have it work autonomously.

{{< figure src="/images/2026/11-23-what-ai-engineers-can-learn-from-pilots/whatsapp-send-popup.jpg" caption="The WhatsApp popup that prevents Claude from making a mistake and spamming everybody" >}}

## thingsithinkithink

- I think Adam's approach is a reasonable place to start, but were I in his shoes I'd be digging into the work from distributed systems and site reliability engineers - things like fault tolerance, atomic transactions and idempotency (being able to repeat a step without it happening twice). I think it's worth leaning a bit more on some of the practices there and seeing how they can be brought into the agentic world (e.g. I saw a great [talk on Pi Durable](https://youtu.be/EreOxs9Vvrg) from [Mario Zechner](https://www.linkedin.com/in/mariozechner/), which has some of these ideas in it).

---
title: "The Decade of Agents: Swyx's AI Engineer Paris Keynote"
date: 2025-09-23T12:00:00Z
slug: /09-23-decade-of-agents-swyx-keynote/
description: "Swyx argues for 2025-2035 as the decade of AI agents, backed by unprecedented infrastructure investment and converging technical definitions."
image: images/2025/swyx-decade-agents/09-23-swyx-decade-agents.png
caption: Swyx presenting at AI Engineer Paris
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - agents
  - infrastructure
  - feature
draft: false
---

## The Decade of Agents: Swyx's AI Engineer Paris Keynote

At AI Engineer Paris, [Swyx (Shawn Wang)](https://swyx.io/aie-paris) laid out his case for why we're entering not just the year of AI agents, but an entire decade of agent-driven transformation from 2025 to 2035. His keynote updated his earlier AI World Fair talk with several converging trends that make this more than typical Silicon Valley optimism. 

I wanted to capture the things that stuck with me from the talk. These stood out:

- The field finally converging on what "agent" actually means
- Unprecedented infrastructure investment becoming a fundamental economic driver
- Models becoming inherently more agentic through new training approaches
- Protocol standards emerging for agent-to-agent communication
- Open questions that will shape the next year of development

![Slide 10: 2025-2035 is the decade of agents with Andrej quote](/images/2025/swyx-decade-agents/slide-10-decade-of-agents-andrej-quote.png)

## Agent Definitions Finally Converging

Simon Willison has been the internet's spokesman for the problem of nobody agreeing on what "agent" means. Swyx highlighted that Simon is softening his stance, which signals the AI engineering community finally converging on a shared understanding. After collecting dozens of competing definitions over the past year, Simon has settled on: "an LLM agent runs tools in a loop to achieve a goal."

![Slide 6: Agent = LLM + Tools + Loop + Goal with Simon Willison's blog excerpt](/images/2025/swyx-decade-agents/slide-6-agent-definition-simon-willison.png)

This is the minimum agreed definition. I find people still using "agent" for simple ML processes, and some distinguish between those and "agentic AI" systems. 

But within the online AI engineering community, this definition - LLM plus tools plus loop plus goal - has become the working standard.  It certainly seems to capture the "new agents powered by LLMs" thing I think.

Swyx also threw up his IMPACT framework, reminding the audience that *good* agents tend to have much more than the simple definition would imply. 

![Slide 7: The IMPACT framework breakdown](/images/2025/swyx-decade-agents/slide-7-impact-framework-breakdown.png)

- **I**ntent: Goal-oriented behaviour, adapting to achieve objectives
- **M**emory: Long-running, capable of open-ended tasks
- **P**lanning: Multi-step operations that previously required humans
- **A**uthority: Trusted to make impactful decisions
- **C**ontrol: LLM determines application control flow
- **T**ools: LLM + memory + planning + tools + while loop

I see this as a maturity model rather than a strict definition. You don't need all these attributes to have an agent. But they're what you'd probably need for an agent that survives in enterprise settings or the competitive AI marketplace.

## The Infrastructure Buildout as Fundamental Driver

Swyx called current investment "one of the most epic infrastructure buildouts of all time." The numbers are actually, mind-bendingly, extraordinary - Stargate's $500 billion commitment, with Satya Nadella contributing $80 billion. Nvidia and others pushing the total past the trillion-dollar mark of combined infra investment - this is commited build - it WILL lead to gigawatts of energy entering the system - it WILL lead to exponentially more available compute.  It's hard to imagine that world - but we'll live in it within 10 years.

![Slide 8: The Most Epic Infra Buildout showing Stargate announcement and Nvidia investment](/images/2025/swyx-decade-agents/slide-8-epic-infra-buildout-stargate-nvidia.png)

This capital commitment transforms investment from a sign of change to a driver of it. When you invest at this scale, it becomes a force that reshapes the economy rather than just reflecting market sentiment.

![Slide 9: Infra will be used! showing compute scaling charts](/images/2025/swyx-decade-agents/slide-9-infra-will-be-used-compute-scaling.png)

The chart showing OpenAI planning $450 billion in compute through 2030, with xAI growing fastest, demonstrates that ChatGPT reaching a billion users in two months is basically guaranteed. As Swyx put it, this is "the most epic historical tailwind you have ever seen in your tech career."

Having lived through web, dot-com, and mobile, this claim feels both true and can't-get-my-head-around-it astonishing. Each transformation felt dramatic, but this feels faster and more intense. We're retooling the economy to run on an AI-supported foundation.



## Models Becoming Inherently Agentic

The technical shift Swyx highlighted centres on models becoming more agentic by design. The comparison he showed was around the way these more agentic LLMs use tools:

![Slide 13: Thinking with Tools comparison showing Claude 4 Opus vs GPT-5 approach](/images/2025/swyx-decade-agents/thinking-with-tools-claude-gpt5-comparison.jpg)

Claude 3 Opus thinks, makes a tool call, gets a result, thinks again, then responds. Newer models like the Claude 4 range and the GPT 5 range receive tool results, interpret them, and can 'think' before immediately trying something different - essentially replanning as they go. This shift toward autonomous replanning unlocks value because carrying out longer task chains multiplies impact.

The frontier labs are explicitly post-training for this capability:

![Slide 15: Pre-train scale compute on Post-train showing Grok's 10x increase](/images/2025/swyx-decade-agents/slide-15-pretrain-posttrain-grok-10x-increase.png)

xAI proudly stated they're allocating as much compute to post-training as pre-training for Grok 4. We're moving from models handling minute-long tasks to hour-long tasks, with day-long capabilities on the horizon. I see people online disputing this. But just because it's hard to make happen in your day-to-day use of AI doesn't mean it's not possible. And there are now a handful of concrete examples of AI working on tasks for hours and hours and hours to ultimate success.

![Slide 14: Increasing Autonomy chart showing task duration growth](/images/2025/swyx-decade-agents/slide-14-increasing-autonomy-task-duration.png)

## The Protocol Landscape Beyond MCP

MCP (Model Context Protocol) has won as the standard for connecting models to tools, but it's one piece of the protocol landscape:

![Slide 18: Agent Protocols showing MCP growth chart](/images/2025/swyx-decade-agents/slide-18-agent-protocols-mcp-growth.png)

Google has A2A (Agent to Agent), and Zed's ACP (Agent Client Protocol) is becoming an interoperability layer for terminal agents. We're no longer just swapping model strings - we're swapping entire agents with their own interfaces. The shift is from connecting models to connecting agents.

Building on Karpathy's 2023 "LLM OS" concept, Swyx noted we've mapped solutions for search, code execution, document libraries, and multimodal I/O:

![Slide 20: The 2025 LLM OS diagram showing components](/images/2025/swyx-decade-agents/slide-20-2025-llm-os-diagram.png)

What's missing: good memory and orchestration. There's opportunity for startups to fill these gaps - what Swyx calls building "indie LMOs."

## Open Questions for the Year Ahead

Swyx closed with three provocative debates:

**Do we need evals?** Boris, chief architect of Claude Code, admitted that despite trying hard to build evals, "in the end it's all vibes." Claude Code generated $500 million revenue with no formal evals.

![Slide 23: How do we do Agent Evals? showing Boris quote](/images/2025/swyx-decade-agents/slide-23-agent-evals-boris-quote.png)

For narrow domains, evals make sense. For general applications, it's not obvious they should block development. However, I think this isn't really even an argument. I think what happened here was Spike's got annoyed, uh everybody going on and on and on about Hamel's course and basically felt like he had to say something.  Great product development has always required taste (no-evals) and data (evals).

**Context engineering** remains unsolved. The multi-agent debate is really about context management - how to structure and manage context effectively. There's no standard approach beyond scattered blog posts. Anthropic and OpenAI have recently published some stuff on this and I think a series of appraoches may become standardised soon.

![Slide 24: Context Engineering showing Cognition and HumanLayer posts](/images/2025/swyx-decade-agents/slide-24-context-engineering-cognition-humanlayer.png)

**Fast agents** could unlock new behaviours. While most providers offer 100-200 tokens per second, Cerebras hits 2000. Every 10x speed increase unlocks different user behaviours and product possibilities. I haven't played much with super-fast AI.  I think he might be right - it might be meaningfully different.

![Slide 25: Fast Agents showing Cerebras speed comparison chart](/images/2025/swyx-decade-agents/slide-25-fast-agents-cerebras-speed-comparison.png)

## thingsithinkithink

- I grew up with computers that weren't on the internet. Around 2000 when we started putting everything on the web, I thought that would be a demarcation point in history - all computational science leading up to 2000, then the World Wide Web moment where everything became super connected. It sure felt like that was true. While the world today is very different than 2001 (when I graduated undergrad), you can see the connection. You can imagine that this is the world that 2000-2001 was putting in place - working on the early web, this is the continuation of that. There was a before-web moment and an after-web moment where society shifted to be online and hyper-connected. Mobile phones amplified that. But I'm now wondering if maybe it was before-AI and after-AI. Once we have agentic ways of interacting with data, information, and each other, I think that may be a bigger shift than the pre-web to post-web one.
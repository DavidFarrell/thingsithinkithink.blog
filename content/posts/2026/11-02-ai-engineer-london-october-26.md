---
title: "AI Engineer London - October 26"
date: 2026-11-02T09:00:00Z
slug: /11-02-ai-engineer-london-october-26/
description: "Some interesting stuff from Peter Gostev at Arena and Danila Kozlov at ElevenLabs."
image: images/2026/11-01-ai-engineer-london/shapeless-blob.jpg
caption: "Peter Gostev and the shapeless blob"
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - evals
  - speech-to-text
draft: false
---

Last week I got back to the AI Engineer London meetup for the first time in a while. It was great to see [Eddie Forson](https://www.linkedin.com/in/eddie-forson/) again and to meet [Tiago Pina](https://www.linkedin.com/in/tpina/) and [Amandine Flachs](https://www.linkedin.com/in/amandineflachs/). I always enjoy going to London AI meetups, but it's been over a month since I've gone to one because I've had so many travels and some game projects I had to attend to.

I wanted to share a couple of interesting things from the talks.

## Peter Gostev on how Arena do evals

I'm very interested in [evals]({{< ref "posts/2026/01-05-llm-evals-course-recap.md" >}}), and it was great to have [Peter Gostev](https://www.linkedin.com/in/peter-gostev/) from [Arena](https://arena.ai/) presenting some of the work they do on evals and explaining how they put it together.

I think the shapeless blob metaphor at the top of this post worked really well, because every one of these models does have a unique shape. For a minute there it did feel to me, incorrectly, that models were going to converge on very similar profiles, but this has proven not to be the case. Hearing more about how Arena think about and shape their work was really interesting.

For example, they've got a benchmark on [agent mode](https://arena.ai/resources/agent-arena-signals/). You can see from the slide that they look for indicators of performance across multiple signals - in this case, looking for confirmations of success, weighing praise against complaints from users, looking to see how steerable the AIs are, whether they use bash correctly and whether they hallucinated any tools.

{{< figure src="/images/2026/11-01-ai-engineer-london/five-signals.jpg" caption="Agent mode: five signals" >}}

So for example, steerability. They score each assistant turn by how much correcting the user has to do, and a repeated correction costs more than a first one.

{{< figure src="/images/2026/11-01-ai-engineer-london/steerability.jpg" caption="Steerability: the cost of each correction" >}}

You can see here that there are meaningful differences between today's frontier models, as of late October. You can understand why Anthropic are leading so effectively in coding tasks when Opus 5.5 is performing so much better overall than GPT-6 Astra (with GPT-6.1 Sol just behind Astra).

{{< figure src="/images/2026/11-01-ai-engineer-london/current-profiles.jpg" caption="Agent mode: current profiles for Claude Opus 5.5 (Max), GPT-6 Astra (Max) and Mistral Medium 3.5" >}}

I also enjoyed hearing about how they [measure alignment](https://arena.ai/blog/ai-alignment-index). The way that they categorise failure signals feels to me in line with the way one would identify clusters of errors when performing [error analysis]({{< ref "posts/2025/04-13-error-analysis-for-improving-llm-applications.md" >}}).

{{< figure src="/images/2026/11-01-ai-engineer-london/alignment.jpg" caption="Alignment: three failure signals" >}}

Also, I'm pretty sure it's universally agreed that Peter is one of the most creative people out there when it comes to using these frontier models, and it's always a joy to see the weird and wonderful demos he creates. He [basically recreated Google Street View](https://x.com/petergostev/status/2048078400628412885) for the Hanging Gardens of Babylon, with GPT-Image-2 generating the 1,500 images and GPT-5.5 in Codex building it. If you haven't seen his stuff, have a look at his [first impressions of GPT-6 Astra](https://www.youtube.com/watch?v=GQPi39sjNhU). What a fun job he has, and I'm pretty sure he's the right guy for that job.

## Danila Kozlov on small models

The other talk I want to mention was from [Danila Kozlov](https://www.linkedin.com/in/danilakozlov/), who has just joined ElevenLabs. I only got one image from his talk (oops).

ElevenLabs are known for absolute frontier-level models that set the bar for audio. But part of his role there is small models, and he's been doing some work with them on device.

He shared a piece of evidence that I found counterintuitive at first, but as soon as he explained it, it made perfect sense. It's a reminder that fundamentals are still the most important thing, even though we're getting so much benefit from scale right now.

I don't have slides to jog my memory, but I'll explain here my recollection of his talk.

Lots of models these days can do speech to text, and transcriptions get better as models get larger (he showed a benchmark demonstrating this). However, one of the things ElevenLabs really care about is character-by-character precision. If you say "good morning", they want the text, but they also want to know exactly where each part of those words sits within the sound wave.

He showed evidence from their benchmarks that even though transcriptions are improving significantly in large frontier models, timestamp accuracy isn't improving in the same way. In some examples timestamp accuracy was decreasing even as transcriptions improved.

His explanation is obvious when you hear it. A large model ends up learning so many things about the relationship between words and audio. For example, it learns that "good morning" takes something like half a second to say almost all the time. So when somebody says it faster or slower than that, the model's general knowledge interferes, because it just "knows" that the phrase takes about half a second. A smaller model can't learn these things about every word, so it's forced to use a simpler trick - paying more attention to the relationship between the sound at that moment and the letters.

It shows that intuitions can lead you astray. The intuition is that a larger model will always be better, specialised fine-tunes aside. That doesn't always hold, and there are actual concrete downsides.

He also shared a benchmark with a graph of the same model at bigger and bigger sizes. It might have been Meta, it might have been Nvidia, I'm not sure. At a certain point timestamp accuracy started to decrease. It was the same class of model and the same training regime, so the argument of large generic model versus smaller fine-tuned model doesn't really apply. As I understood it, as the model got bigger it started to learn all these clever shortcuts that decreased its accuracy. I had a look for the benchmark but I couldn't find it.

{{< figure src="/images/2026/11-01-ai-engineer-london/voice-on-device.jpg" caption="Danila's closing slide: voice, on device" >}}

If you're interested in the ElevenLabs local models, they've got a [waitlist here](https://elevenlabs.io/local-deployment-waitlist).

{{< figure src="/images/2026/11-01-ai-engineer-london/elevenlabs-waitlist-qr.png" caption="ElevenLabs local deployment waitlist" width="220" >}}

## thingsithinkithink

- For a long time I've been using the Qwen local models to generate audio, but I am looking forward to a local model that doesn't insert random laughs and sniffs and snores and groans etc!

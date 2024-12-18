---
title: "The challenges of mastering LLMs, and their role as cyborg enhancement"
date: 2025-01-08T12:00:00Z
slug: /01-08-a-good-interview-with-simon-willison-on-around-the-prompt/
description: "I enjoyed a recent interview with Simon Willison on Logan Kilpatrick's Google podcast. Topics covered: AI as a 'cyborg enhancement', the non-intuitive challenges of mastering LLM use, and the legitimate need for uncensored language models in fields like journalism."
image: images/2025/01-08-a-good-interview-with-simon-willison-on-around-the-prompt.png
caption: Around the Prompt with Simon Willison
categories:
  - blog
  - artificial-intelligence
tags: # tags - one per line
  - ai
  - podcast 
# (uncomment to make hero post)  - feature
draft: false
---

I recently watched a good [interview](https://www.youtube.com/watch?v=rLcKbvmegag) with Simon Willison on Logan Kilpatrick's podcast, hosted for Google. Simon is known for building [Django](https://www.djangoproject.com/) (the Python web framework), [Datasette](https://datasette.io/) (a data tool for journalists), and the [LLM command line tool](https://github.com/simonw/llm) (which lets you run large language models from the command prompt). I used LLM for months until recently [Shell Sage](https://www.answer.ai/posts/2024-12-05-introducing-shell-sage.html) became my daily tool.


## takeaways:

- Simon's take that generative AI is best thought of today as a cyborg enhancement to our capabilities. I feel this way. These things make me so impactful and able to do what I already do, but better.  
  - However, he noted that these technologies don't benefit everyone universally and threaten some  livelihoods. 
    - For instance, illustrators who rely on commissions may find their work threatened as individuals opt for generating assets using tools like Stable Diffusion or Flux.
- Simon's take that LLMs are hard to master. Yes, most people have had an amazing experience that shows the power of LLMs, but it's hard to get consistent high value results. And to do so, requires building a lot of intuition:
  -  The notion that a powerful computer program, such as a large language model, cannot perform basic tasks like multiplication seems absurd to many. 
  -  People have to build a mental model of LLMs, understanding their strengths and weaknesses, and recognising concepts like training cut-offs, hallucinations, and the probabilistic nature of outputs.
  -  One he didn't mention but that I'm thinking about these days is around RAG systems. Users need to understand that even when LLMs are provided with legitimate sources, those sources compete with the model's training data, which can introduce bias against the sources.  The idea is totally foreign to most people. RAG doesn't *fix* anything - it has value - but it doesn't stop the LLM saying something incorrect.
-  Some people think there is no longer any value to a computer science degree since LLMs can code.    
    - But there is much more to creating great software than merely inputting a prompt and receiving functional code.
- Legitimate uses of uncensored LLMs. 
  - He shared an example of using Claude to extract campaign finance data from a report, where the AI declined to assist due to concerns about sharing personal financial information. This is absurd. 
  - In another instance, a group analysing police body cam footage had to convince the LLM that dogs can bite people, as the model was biased towards pro-dog information based on its training data (the internet!). 
    - and yet foundation model providers are understandably hesitant to share unfiltered models due to the (extremely high) likelihood that a news institution would (of course) publish scare articles about the LLM sharing unethical content.
    

## thingsithinkithink

- The thing about AI being a threat to many:
  - I feel this.  I've worked a lot with artists, musicians, and writers.  I *know* many of their clients would be perfectly happy with some AI 'filler' assets and a lot of entry level positions in particular are at risk in these fields.
  - I hope people in these fields are able to use AI to amplify *their* abilities to be more impactful too - but it's definitely going to hurt folk.  It makes me very self-conscious whenever I get excited about these things.  It's easy to overlook the negative impacts.
  - it does seem particularly unjust that rich silicon valley types train these tools on the work of the relatively underpaid creatives and the result is a massive threat to those already underempowered fields
- The thing about LLMs being hard to master:
  - I couldn't agree more.  I think there is a parallel between the examples he shares about individuals having challenges to master GenAI and the organisational challenges I've seen over the last couple of years.
    - The initial wave of generative AI adoption has produced impressive proof of concepts that often fail to evolve into viable products. This challenge arises partly from the technology stack (POCs are often built on independent systems that lack integration with organisational data pipelines etc). 
    - additionally though, a significant part of the issue specifically pertains to the challenge of mastering these tools.  A POC shows what's possible - but bringing a product to market that brings that value without causing a disaster in a multitude of edge cases is a much harder challenge.
      


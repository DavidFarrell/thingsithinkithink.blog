---
title: "LLM Evals Course: Complete Course Recap"
date: 2025-12-22T09:00:00Z
slug: /12-22-llm-evals-course-recap/
description: "A comprehensive recap of Hamel and Shreya's LLM evaluation course - covering the Three Gulfs model, the Analyse-Measure-Improve cycle, error analysis methodology, evaluation operationalization, and custom review interfaces."
image: /images/2025/parlancecourse/12-22-hamel-shreya-course-promo.png
caption: Hamel Husain and Shreya Shankar's LLM Evaluation Course
categories:
  - artificial-intelligence
  - evals
  - course-notes
tags:
  - llm
  - evaluation
  - machine-learning
  - course-notes
  - feature
draft: false
---

I've finally finished writing up my notes from Hamel Husain and Shreya Shankar's [LLM evaluation course]({{< ref "posts/2025/06-08-llm_evals_lesson_1.md" >}}). It took me longer to write up my notes than it took to actually do the course, but it gave me a good excuse to revisit everything a second time, which is a great way to help cement my learnings. I'm going to do one post here to finally capture the key things from each of the lessons, with the hope that I can refer back to this in the future to help me find the detail that I'm looking for.

---

## The Three Gulfs Model

The course's central premise is that building good LLM pipelines is hard because of three fundamental challenges.

![The Three Gulfs Model showing Developer, LLM Pipeline, and Data nodes](/images/2025/parlancecourse/12-21-three-gulfs.png)

**The Gulf of Comprehension** sits between the developer and the data. It's hard to understand everything in your data: real user queries, system outputs, synthetic test cases. We end up with a partial model of what's actually happening in our system.

**The Gulf of Specification** sits between us and the instructions we give the LLM. We're trying to describe what we want, but much of our intent is latent. We only realise what we actually mean when we see outputs that inform us we need to specify better.

**The Gulf of Generalisation** sits between the LLM and the data. Even after specifying everything in detail, the model isn't always good enough. When it encounters data outside its training distribution, it struggles to execute our specification. This requires different strategies: fine-tuning, task decomposition, RAG improvements.

### The Analyse-Measure-Improve Cycle

The course structured everything around a three-phase cycle, each with its own common pitfalls.

![The Analyse-Measure-Improve cycle with pitfalls](/images/2025/parlancecourse/12-21-analyse-measure-improve.png)

**Analyse Phase**: The goal is qualitative understanding. You're looking at your data, identifying failure patterns, and building a taxonomy of what's going wrong.

Pitfalls:
- Outsourcing annotation to the wrong people instead of owning it yourself
- Not looking at enough examples to reach theoretical saturation

Shreya repeated throughout the course that no matter the size of your company or product, you always have to do error analysis. The ease of doing error analysis now, and the specific process for doing it well, is probably the single most valuable thing to get from this course. The bang for buck on systematic error analysis is very high.

**Measure Phase**: The goal is quantification. Once you know your failure modes qualitatively, you need to measure how prevalent they are so you can prioritise and track improvement.

Pitfalls:
- Unaligned LLM judges that don't reflect your informed perspective
- Data leakage by putting failure traces directly into your judge's prompt, then testing on those exact traces

The second mistake surprises me that people make it, but apparently they do. If you put examples in the prompt and then test on those same examples, of course your judge performs well. That's not overfitting so much as leakage.

**Improve Phase**: The goal is targeted fixes. With analysis and measurement complete, you can finally make changes with confidence that you're addressing real problems and can verify whether you've made things better.

Pitfalls:
- Premature improvement before proper analysis and measurement
- Jumping to the most complex technical solution first

In my line of work, I meet lots of different clients who want help with some LLM-based solution. Those that know something about AI often demonstrate that second pitfall. It seems to me that the more people know, the more inclined they are to have an opinion about one of these complex technical solutions. Fine-tuning is a common example. They've heard of it, they can see a pattern match between their understanding of it and the problem at hand, and they want to go straight to it. But it's usually far easier and cheaper to start with the smallest intervention, which is often just working on the prompts.

### The Analyse Phase: Understanding What's Broken

The analyse phase focuses on qualitative understanding through systematic error analysis:

1. **Bootstrap a dataset** (real or synthetic)
2. **Open coding**: Read traces and apply descriptive labels to find failure patterns
3. **Axial coding**: Cluster those labels into a structured taxonomy of failure modes

For subjective criteria, collaborative evaluation with multiple annotators helps. The focus isn't on figuring out who's correct when there's disagreement. It's on improving your description of the criteria until everyone becomes aligned. Cohen's Kappa measures agreement; alignment sessions refine the rubrics.

### The Measure Phase: Quantifying Failures

Once you know your failure modes, you quantify their prevalence through automated evaluators.

**Programmatic evaluators** are fast, cheap, and objective. If you're checking whether your system used a tool, you don't need an LLM judge. Just check if the tool object is populated. Regex, schema validation, keyword matching all fit here.

**LLM-as-judge** handles subjective or nuanced criteria. But a trustworthy judge isn't automatic. You have to build and validate it.

The approach mirrors ML training: split your labelled data into train, dev, and test sets. Don't leak data between them. The analogy is slightly forced since these don't map exactly to how you'd use them in a traditional ML pipeline, but the principle holds. The "training set" here means a handful of few-shot examples in your prompt. The dev set is what you iterate on while refining the judge. The test set stays sealed: you know the human labels, you run your judge, you measure TPR and TNR, but you don't peek inside to improve the prompt.

### Operationalising Evaluation

Making evaluation part of daily workflow borrows from CI/CD thinking.

**Continuous Integration**: Create a golden dataset of critical examples and known failure modes. Every time you change something, run evaluators to create a regression safety net. If you accidentally made something worse, you'll know.

I recently heard on [Latent Space](https://www.youtube.com/watch?v=wQg5JtmoZXA) that in practice, teams don't always handcraft golden datasets from the start. They put systems in the wild and collect traces as they go. Either way, you end up with something to test against.

**Continuous Deployment**: Monitor a sample of production data continuously. Track performance. Try to uncover unknown unknowns before they cause problems. This might mean floating thumbs up/down on a percentage of uses, with too many thumbs downs immediately flagging something for people to look at. Or it could be grabbing a percentage of production data, human-labelling it, comparing it against system performance, and checking whether you're broadly in line with where you'd expect to be. The goal is to make sure things are on track and you haven't drifted too much.

### Human Review Interfaces

The course emphasised building custom interfaces for reviewing LLM output data. Spreadsheets and generic log viewers don't account for the specific shape of your data. There's real value in building a custom review interface that lets you zoom through data quickly whilst still getting high-quality feedback.

I really love this, and I've been doing it ever since. Before the course, I used to do this the hard way, evaluating all of my data in spreadsheets. It was a total pain in the arse, and I really appreciate how much better a custom interface can be. It's one of my big takeaways from the course alongside the error analysis methodology.

---

## thingsithinkithink

- The error analysis methodology and custom review interfaces are my two biggest takeaways from this course. I was doing versions of both before, but without the mature perspective the course provides. It was a pain in the arse the way I used to do it. This is better.

- The Three Gulfs model gives a useful vocabulary for diagnosing where things are going wrong. Is it comprehension (I don't understand my data)? Specification (my prompts aren't clear enough)? Generalisation (the model just can't do it)? Having that language helps.

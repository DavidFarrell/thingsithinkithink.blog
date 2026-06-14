---
title: "Easier to Say No Than Yes"
date: 2026-05-12T06:00:00Z
slug: /05-12-easier-to-say-no-than-yes/
description: "Most enterprise AI decisions have a risk-asymmetric easy side and a risk-heavy hard side. Let AI handle the easy side, and you can be in production faster than you think."
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - ai-leadership
  - consulting
  - product
draft: true
---

Something I keep noticing across my consulting work is that, in an enterprise setting, it is much easier to use AI to say *no* than to use it to say *yes*. Or sometimes the other way around. The point isn't which direction - the point is that almost every real-world AI decision has a risk-asymmetric easy side and a risk-heavy hard side. If you can identify which is which, you can get into production a lot faster than risk-averse organisations usually assume.

Two examples I've been thinking with.

## The NHS specialist appointment example

I've been involved in work where GPs refer patients to specialists for a particular test. The NHS waiting lists are so oversubscribed that the hospital does its own triage of those referrals. In practice that means a specialist - often an external consultant on a day rate - comes in for a specific day, and they plough through four hundred or a thousand GP referrals at a time, deciding which ones genuinely warrant the specialist test.

It's expensive. It introduces delay even before you get on the waiting list. Anything that speeds it up is valuable.

But the two sides of that decision have completely different risk profiles.

If an AI looks at a GP referral and says *"no, this patient doesn't meet the criteria"*, you have an AI making a decision that materially affects someone's medical treatment. I would be very, very, very wary of putting AI in that role. It's not necessarily unethical - but the failure modes are bad enough that you should probably keep a human firmly in the loop.

If an AI looks at a GP referral and says *"yes, this is clearly aligned with the criteria for the test"*, the failure mode is very different. The patient was already referred by a GP - a medical professional has already said they need this. The AI is reviewing that decision against a set of guidelines. The worst case if the AI is wrong is that the appointment turns out to be unnecessary - which is bad, but no one is being denied care.

So you don't deploy the AI to do the whole vetting job. You deploy it to handle only the obviously-yes cases. Those drop off the specialist's pile entirely. The specialist still reviews everything that the AI couldn't confidently approve - which is the genuinely marginal stuff. Their pile shrinks dramatically. The work doesn't disappear, but it gets a lot less expensive and a lot faster.

## The procurement contract example

Another client of mine has a process where all new procurement contracts have to be reviewed by legal. The legal team there is excellent - everyone in the organisation has time for them, there's no animosity at all - but they are a bottleneck. Business units find themselves waiting on legal even for small contracts of five or ten thousand pounds.

We're building a system that compares a proposed procurement contract against the organisation's playbook of approved terms.

This is where my "easier to say no" framing gets a bit more tangled - because in this case, for low-value contracts, the system *will* be willing to say yes. We're accepting some risk on the yes side because the contracts are small.

But the cleaner version of the pattern is still there. It is much *easier* to detect where a proposed contract is obviously misaligned with the playbook than it is to write a system that conclusively approves a high-value, complex contract on its own. So the system surfaces the delta - here is where the supplier's draft differs from your playbook - and the business unit takes that into their conversation with the supplier. They push back, they ask for the playbook clauses, often before legal ever needs to see it. For the actually-low-stakes contracts, the system can offer a soft yes and unblock things directly. For anything high-value or genuinely complex, legal still gets the contract on their desk.

Legal stops being the bottleneck for the bulk traffic. The work doesn't go away - it gets reshaped.

## The bigger point

The thing I think is worth naming is that **AI doesn't have to solve the whole problem in order to be useful**. It can solve the easy part of the problem.

Risk-averse organisations look at AI use cases and default to imagining the hard side of the decision - the AI rejecting a patient, the AI greenlighting a million-pound contract. Of course those scenarios are scary. Of course they wouldn't put AI in charge of those.

But that's not the deployment shape that actually works in practice. The deployment shape that actually works is: figure out which side of the decision has the lower-stakes failure mode, and let the AI handle the obviously-okay cases on that side. The humans keep doing the hard work, but they do less of it - because the volume of obvious cases gets handled at machine speed.

In the NHS example, the easy side is *yes* and the AI confirms valid referrals.

In the procurement example, the easy side is *no* - or rather, "obviously misaligned with the playbook" - and the AI surfaces deltas so business units can do their own pushback.

The framing of "easier to say no than yes" was my entry point into this, but I think the real generalisation is: **every AI decision has an easy side and a hard side. Find the easy side. Ship there first.**

## thingsithinkithink

- I haven't seen this framing written up explicitly, which is part of why I wanted to put it down. If you have - send it to me.

- The pattern is also a useful counter to "we can't put AI into production until we've solved the hard cases." You probably can't, and you probably shouldn't, solve the hard cases. But the easy cases on the low-risk side of the decision are sitting right there.

- It's worth doing the work of explicitly mapping the risk profile of both sides of any decision you're considering AI for. Sometimes the easy side is genuinely easy and you should ship today. Sometimes both sides are high-risk and you shouldn't be using AI at all. The mapping is the thing that tells you which.

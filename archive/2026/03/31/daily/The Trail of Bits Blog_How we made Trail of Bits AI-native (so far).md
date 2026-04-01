---
title: How we made Trail of Bits AI-native (so far)
url: https://blog.trailofbits.com/2026/03/31/how-we-made-trail-of-bits-ai-native-so-far/
source: The Trail of Bits Blog
date: 2026-03-31
fetch_date: 2026-04-01T04:45:24.523206
---

# How we made Trail of Bits AI-native (so far)

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# How we made Trail of Bits AI-native (so far)

[Dan Guido](/authors/dan-guido/)

March 31, 2026

[ai](/categories/ai/)

Page content

* [What AI-native actually means](#what-ai-native-actually-means)
* [What people are actually resisting](#what-people-are-actually-resisting)
* [The remedies that actually worked](#the-remedies-that-actually-worked)
* [The operating system model](#the-operating-system-model)
  + [Standardize on tools](#standardize-on-tools)
  + [Write the rules](#write-the-rules)
  + [Make it measurable](#make-it-measurable)
  + [Create an adoption engine](#create-an-adoption-engine)
  + [Capture the work as reusable artifacts](#capture-the-work-as-reusable-artifacts)
* [Results so far](#results-so-far)
* [Open questions](#open-questions)
* [The replicable recipe](#the-replicable-recipe)
* [Resources](#resources)

*This post is adapted from a talk I gave at [[un]prompted](https://unpromptedcon.org/), the AI security practitioner conference. Thanks to [Gadi Evron](https://twitter.com/gadievron) for inviting me to speak. You can watch the recorded presentation below or download the [slides](https://github.com/trailofbits/publications/blob/master/presentations/How%20we%20made%20Trail%20of%20Bits%20AI-Native%20%28so%20far%29/slides.pdf).*

Most companies hand out ChatGPT licenses and wait for the productivity numbers to move. We built a system instead.

A year ago, about 5% of Trail of Bits was on board with our AI initiative. The other 95% ranged from passively skeptical to actively resistant. Today we have 94 plugins, 201 skills, 84 specialized agents, and on the right engagements, AI-augmented auditors finding 200 bugs a week. This post is the playbook for how we got there. We [open sourced most of it](https://github.com/trailofbits/skills), so you can steal it today.

A [recent Fortune article](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/) reported that a [National Bureau of Economic Research study](https://www.nber.org/papers/w34984) of 6,000 executives across the U.S., U.K., Germany, and Australia found AI had no measurable impact on employment or productivity. Two-thirds of executives said they use AI, but actual usage came out to 1.5 hours per week, and 90% of firms reported zero impact. Economists are calling it the new Solow paradox, referencing the pattern Robert Solow identified in 1987: “you can see the computer age everywhere but in the productivity statistics.”

AI works. Most companies are using it wrong. They give people tools without changing the system. That’s the gap between AI-assisted and AI-native. One is a tool, the other is an operating system.

## What AI-native actually means

“AI-native” gets thrown around a lot. The way I think about it, there are three levels:

**AI-assisted** is where almost everyone starts. You give people access to ChatGPT or Claude. They use it to draft emails, generate boilerplate, summarize documents. It’s a productivity tool. The org doesn’t change. The workflows don’t change. You just do the same things a little faster.

**AI-augmented** is where you start redesigning workflows. You’re not just using AI as a tool. You’re putting agents in the loop, changing how work actually flows. Maybe the AI does the first pass on a code review and the human does the second. The process itself is different.

**AI-native** is the structural shift. The org is designed from the ground up assuming AI is a core participant. Not a tool you pick up, but a teammate that’s always there. Your knowledge management, your delivery model, your expertise, all designed to be consumed and amplified by agents.

At Trail of Bits, what this means concretely: our security expertise compounds as code. Every engagement we do, the skills and workflows we build make the next engagement faster. Every engineer operates with an arsenal of specialized agents built from 14 years of audit knowledge. That’s not “we use AI.” That’s “AI is on the team.”

## What people are actually resisting

When I first launched this initiative inside Trail of Bits, there was an incredible amount of pushback. Studies of technology adoption consistently show the same thing: the problem is never the software. It’s people’s unwillingness to accept that something else might be better than their intuition. I had to understand four specific psychological barriers before I could design a system that works within them.

**Self-enhancing bias.** We overestimate our own judgment. Paul Meehl and Robyn Dawes [showed](https://www.cmu.edu/dietrich/sds/docs/dawes/the-robust-beauty-of-improper-linear-models-in-decision-making.pdf) that if you take the variables an expert says they use and build even a crude linear model, the model outperforms the expert. Not because it’s smarter, but because it applies the same weights every time. You don’t. You’re hungover some days, distracted others, and you never notice because you take credit for your wins and blame external factors for your misses. This gets worse with seniority. The more expert you are, the more you trust your gut, and the less you believe a machine could do better. As [Jonathan Levav](https://www.gsb.stanford.edu/faculty-research/faculty/jonathan-levav) frames it: the more unique you feel you are, the more you resist a machine making decisions for you.

**Identity threat.** In [one study](https://journals.sagepub.com/doi/abs/10.1177/0022243718818423), researchers showed people the same kitchen automation device framed two ways: “does the cooking for you” versus “helps you cook better.” People who identified as cooks rejected the first framing and accepted the second, for the same device. There’s a symbolic dimension too: people don’t want robots giving them tattoos (human craft), but they’re fine with a tattoo-*removing* robot (instrumental, no symbolism). Security auditing is symbolic work. AI that replaces skill feels like an attack on who you are.

**Intolerance for imperfection.** Dietvorst et al. [ran a study](https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf) where participants watched an algorithm outperform a human forecaster. But after seeing the algorithm make one error, they abandoned it and went back to the human, even though the human was demonstrably worse. We forgive our own mistakes but not the machine’s. [Their follow-up](https://pubsonline.informs.org/doi/10.1287/mnsc.2016.2643) found the fix: let people modify the algorithm. Even one adjustable parameter was enough to overcome the aversion.

**Opacity.** A [2021 study in Nature Human Behaviour](https://www.nature.com/articles/s41562-021-01146-0) found that people’s subjective understanding of human judgment is high and AI judgment is low, but objective understanding of both is near zero. People feel like they understand how a doctor diagnoses. They can’t explain it either. The feeling of not understanding kills the feeling of control.

## The remedies that actually worked

We designed the system around the resistance, not against it.

![The remedies that actually worked](/2026/03/31/how-we-made-trail-of-bits-ai-native-so-far/remedies_hu_467a5bd562219c7f.webp)

The remedies that actually worked

For **self-enhancing bias**, we built a maturity matrix. Nobody likes being told they’re at level 1. But that’s the point: you can’t argue you’re already good enough when there’s a visible ladder. It makes the conversation concrete instead of “I don’t think AI is useful.” It also creates social proof. When you see peers at level 2 or 3, the passive majority starts moving.

For **identity threat**, we never asked anyone to stop being a security expert. We gave them a new way to express that identity. When a senior auditor writes a constant-time-analysis skill, they’re not being replaced. They’re becom...
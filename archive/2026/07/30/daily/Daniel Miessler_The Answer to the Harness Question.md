---
title: The Answer to the Harness Question
url: https://danielmiessler.com/blog/the-answer-to-the-harness-question?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-07-30
fetch_date: 2026-07-31T05:31:42.216947
---

# The Answer to the Harness Question

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# The Answer to the Harness Question

Harnesses are for intent; models are for execution

July 29, 2026

[#ai](/archives/?tag=ai) [#prompting](/archives/?tag=prompting)

[**AIL***3*](/blog/ai-influence-level-ail "AIL 3 — AI Created, Human Full Structure")

 Cross-entropy-computing…

[![The Answer to the Harness Question](/images/the-answer-to-the-harness-question.webp)](/images/the-answer-to-the-harness-question.webp)

Martin Casado posted something about AI harnesses that captures where a lot of smart people are stuck right now.

> [Loading tweet...](https://twitter.com/martin_casado/status/2082527395920347362)

> On harnesses, I vacillate between three beliefs: the less harness, the better. Models are the magic. Post training a model and harness is dramatically better and the model providers win. Harnesses have real independent value from the model. I have no idea which is right. [Martin Casado](https://x.com/martin_casado/status/2082527395920347362)

I think I can answer this.

The reason the question feels impossible is that we're treating the harness as one thing. It's actually two. Every harness carries some mix of WHAT and HOW—context about what you want, and instructions for how to get it. And those two halves age in opposite directions.

The HOW half rots. This is [Sutton's Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) playing out in your config files: the smarter models get, the dumber your step-by-step instructions look by comparison. If your harness is mostly HOW, then Martin's first belief is correct. Less harness is better, because the model is the magic.

The WHAT half appreciates. Who you are, what you're working on, what you're trying to accomplish, and what good looks like to you. A smarter model does more with that context, not less. If your harness is mostly WHAT, then his third belief is correct. It has real independent value, and that value grows with every model release.

So beliefs one and three are both right. They're just about different halves of the harness.

The second belief—that model providers post-train the harness into the model and win—is right about execution and wrong about intent. The labs can absolutely train models to be better agents, and they will. But they can't post-train YOUR context into the model. What you're trying to build, for whom, with your constraints and your taste. That has to be captured and conveyed from outside, every single time.

That's what the harness is for. I've been calling this [Intent Engineering](/blog/intent-engineering), and it's the whole design principle behind [my own harness](/blog/personal-ai-infrastructure): capture what the human actually wants, convey it to the model on every task, and otherwise stay out of the way.

So YES to harness. Extremely powerful. But for your context, while staying out of the way of the model for execution.

#### Notes

1. Martin's original post is [here](https://x.com/martin_casado/status/2082527395920347362), and my reply that this post expands on is [here](https://x.com/DanielMiessler/status/2082627476426273280).
2. I wrote about the WHAT vs. HOW distinction for prompts in [From Prompt Engineering to Intent Engineering](/blog/intent-engineering), and for harnesses in [Good and Bad Harness Engineering](/blog/good-and-bad-harness-engineering). This post is the same idea applied to the "do harnesses even matter" debate.
3. Citation: Richard Sutton, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), March 13, 2019.
4. 🤖 **AIL 3:** I (Kai, Daniel's AI assistant) drafted this post from Daniel's X reply to Martin Casado, which provided the full structure and core argument, plus his prior published posts on the topic. Daniel's original words carry the thesis. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail).

## Related Reading

* [From Prompt Engineering to Intent Engineering](/blog/intent-engineering)
* [Good and Bad Harness Engineering](/blog/good-and-bad-harness-engineering)
* [Bitter Lesson Engineering](/blog/bitter-lesson-engineering)
* [AI is Mostly Prompting](/blog/ai-is-mostly-prompting)
* [Why I Believe in SOTA Models Over Custom Ones](/blog/sota-models-over-custom-ones)
* [Building Your Own Personal AI Infrastructure](/blog/personal-ai-infrastructure)
* [Inference Costs Are Not Sustainable](/blog/inference-costs-are-not-sustainable)
* [How to Rate the AI We're All Chasing](/blog/customization-beats-competence)

♥

## Reader-supported

For roughly 29.7714 years I've written here, ad-free—3,077 essays and tutorials and counting. If it's useful to you, a monthly or one-time donation keeps it going. 🫶🏼

### Monthly

[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)

### One-Time

[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-answer-to-the-harness-question&title=The%20Answer%20to%20the%20Harness%20Question)

Search

This post was tagged with:

aiprompting

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2026 Daniel Miessler. All rights reserved.
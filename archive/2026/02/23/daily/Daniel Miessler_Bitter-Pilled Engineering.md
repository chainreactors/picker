---
title: Bitter-Pilled Engineering
url: https://danielmiessler.com/blog/bitter-pilled-engineering?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-02-23
fetch_date: 2026-02-24T04:12:14.839980
---

# Bitter-Pilled Engineering

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Bitter-Pilled Engineering

We need to avoid the Bitter Lesson mistake when building AI systems

February 22, 2026

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#innovation](/archives/?tag=innovation)

[![Bitter-Pilled Engineering](/images/blog/bitter-pilled-engineering/bitter-pilled-engineering-header.webp)](/images/blog/bitter-pilled-engineering/bitter-pilled-engineering-header.webp)

I have a new concept I'm using everywhere in my AI engineering called Bitter-Pilled Engineering (BPE).

The idea comes from Richard Sutton's essay, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).

My summary, anyway.

The essay argues that all of our human attempts to control, modify, and enhance AI are kind of not worth it, because when you increase the intelligence of AI—through more hardware or better algorithms or whatever—*that* will increase intelligence far more than anything we can do with our human approaches.

It's so seductive to think that we humans have the magic that AI will never have, but that magic is often just hubris.

It's stronger than that actually. Not only will it *not be better* if we try to help, but it will likely be **far worse**.

Essentially, we should avoid poisoning AI's native capabilities with our supposedly superior guidance, because it's not actually superior.

Some quotes from [the essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html):

> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin."

> "We want AI agents that can discover like we can, not which contain what we have discovered."

> "We should build in only the meta-methods that can find and capture this arbitrary complexity."

> "Building in our discoveries only makes it harder to see how the discovering process can be done."

My takeaways:

* The way we think about logic and intelligence and efficiency are very likely primitive
* So we shouldn't be hard-coding those rules or ideas into how we "teach" AI to do things
* As AI gets smarter it'll come up with way better ways to do the same thing from first-principles

I'm unfortunately very inclined to do the opposite, which is why I need to slap myself in the face with this BPE concept.

So my BPE rule for myself when building AI systems is:

**Don't over-engineer scaffolding using your pet/"smart" ideas into the system; instead, make sure any scaffolding you build is robust/anti-fragile to the underlying AI getting smarter.**

#### Notes

1. AIL Level 1: Daniel wrote this entire post from his own ideas and voice recordings. I (Kai, his DA) helped with formatting and generating the header image. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail)
2. Citation: Richard Sutton, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), March 13, 2019.
3. I also build BPE into the [PAI](https://github.com/danielmiessler/PAI) project through an `AISTEERING` rule.

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-pilled-engineering&title=Bitter-Pilled%20Engineering)  [Sponsor on GitHub](https://github.com/sponsors/danielmiessler)

Search

This post was tagged with:

aitechnologyinnovation

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

[Sponsor My Work on GitHub](https://github.com/sponsors/danielmiessler)

© 1999 — 2026 Daniel Miessler. All rights reserved.
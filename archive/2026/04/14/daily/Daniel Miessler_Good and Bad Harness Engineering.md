---
title: Good and Bad Harness Engineering
url: https://danielmiessler.com/blog/good-and-bad-harness-engineering?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-04-14
fetch_date: 2026-04-15T04:44:20.781104
---

# Good and Bad Harness Engineering

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Good and Bad Harness Engineering

Make sure you are telling your AI what you want and not how to get it

April 14, 2026

[#ai](/archives/?tag=ai)

[![Good and Bad Harness Engineering](/images/blog/bitter-lesson-engineering/bitter-lesson-engineering-header.webp)](/images/blog/bitter-lesson-engineering/bitter-lesson-engineering-header.webp)

There are lots of ways to do Harness Engineering well and poorly, but the most important one comes down to whether or not you're practicing [Bitter Lesson Engineering](/blog/bitter-lesson-engineering).

Go read the essay then come back.

Bitter Lesson Engineering is my take on Prompt/Context/Harness engineering that comes from Richard Sutton's ["Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) blog post from 2019. It means ensuring that you're not trying to outsmart your own AI. And specifically, not trying to micromanage *how* your AI does things, but rather specifying what you want done.

In other words:

1. **Bad Harness Engineering** is a whole bunch of prescriptive instructions on exactly *how* to do things.

   *First copy this file, then load this, then do this, then do that. Etc.*
2. **Good Harness Engineering** is about providing tons of context about who you are, what you're about, what you're working on, what you're trying to accomplish, and what good (and bad) look like to you.

   *I'm an engineer focused on personal productivity, I like simple designs with lots of whitespace and great typography, here are my previous projects, here are some tools you can use, etc.*

I have a Bitter Lesson Engineering skill that I run often against my entire harness to audit for this.

Bad Harness Engineering is bad because the smarter AI gets the more antiquated your instructions will become. And at some point (maybe even now?) they'll make your AI stupider instead of smarter.

Good Harness Engineering is good because no matter how smart an AI becomes it will still be better at getting you great results if it understands who you are and what you like.

Also, the better AI gets, the more important Bitter Lesson Engineering becomes.

Basically, both your prompts and your harness should be about who you are and what you're trying to accomplish, and not specifically how to get there. That's what the AI is there to figure out.

Give it the best possible picture of you, your ideal outcome, and the best tools you can, and give it room to work.

#### Notes

1. There are, of course, lots of other ways to do good and bad Harness Engineering. This is just, in my opinion, the biggest distinction and pitfall to be aware of.
2. In the early (2023-2024) days of Prompt Engineering it was ok to tell AI exactly how to do things, and it actually helped. Who knows exactly when the inversion happened, but it was probably somewhere in 2025.
3. I don't mean to imply in the Good Harness Engineering section that it should be super terse. My harness has vast amounts of context, but it's about what I want, not how to achieve it.
4. This principle applies to prompt, context, and harness engineering, and both personal and Enterprise AI.
5. The BLE Skill is available in [PAI](https://github.com/danielmiessler/PAI).
6. Citation: Richard Sutton, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), March 13, 2019.
7. Related: ["Bitter Lesson Engineering"](/blog/bitter-lesson-engineering) — my own take on applying Sutton's lesson to AI system design.
8. AIL Level 1 (0%): Daniel wrote this post entirely. I (Kai, Daniel's assistant) helped with formatting and publishing. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail)

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fgood-and-bad-harness-engineering&title=Good%20and%20Bad%20Harness%20Engineering)

## supporting = loving

For 29.4772 years I've been creating ad-free technical tutorials and essays here. 3,034 pieces and counting.

It's a one-person effort that's also my livelihood. If it makes your day easier or more pleasant in any way, please consider supporting the work with a monthly or one-time donation.

It helps me make more content, and is deeply appreciated as well. 🫶🏼

### Monthly Support

[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)

### One-Time Support

[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)

Search

This post was tagged with:

ai

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2026 Daniel Miessler. All rights reserved.
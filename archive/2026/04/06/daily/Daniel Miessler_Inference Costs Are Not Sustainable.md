---
title: Inference Costs Are Not Sustainable
url: https://danielmiessler.com/blog/inference-costs-are-not-sustainable?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-04-06
fetch_date: 2026-04-07T04:30:49.803814
---

# Inference Costs Are Not Sustainable

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Inference Costs Are Not Sustainable

We're about to need multi-model harnesses, much cheaper models, or both

April 5, 2026

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#future](/archives/?tag=future)

[![Inference Costs Are Not Sustainable](/images/blog/inference-costs-are-not-sustainable/header.webp)](/images/blog/inference-costs-are-not-sustainable/header.webp)

Welp, I'm now getting through a quarter of my week's MAX subscription in a few hours of work with Claude Code.

I think Anthropic is smart, and I don't think they're trying to screw us. I think they're honestly just trying to bring inference charges inline with reality.

And that should be a wake-up call for all of us.

I think we're about to need multi-model harnesses (or FAR cheaper good models within a single platform), like 20x cheaper Haiku or whatever.

This is not sustainable.

The better the harnesses and models get, the more people will build. Which will require more and more inference.

I think the real solutions here are going to come from:

* Technologies like Cerberus, et al which make inference many times cheaper and faster
* A major push by the major labs to produce higher quality in much smaller/cheaper models
* Harnesses moving to a hybrid of paid/cloud and local/cheap models.

If this continues I'm going to have to build my own custom version of PAI using Pi, that can use local models on my dual 4090s, models like Gemini-Flash, models like Gemma 4, etc.

And most importantly, a new hook infra that rates the task and properly routes to the right model.

* Max: Opus / GPT-5.4
* High: Sonnet
* Medium: Haiku
* Low: (Local) Whatever the latest best OSS model is that can run on my NVIDIA / Mac Silicon

I think we all knew this was coming; I just thought it would be in 2027 sometime. And more gentle.

It appears to be very close now because this much subsidization doesn't seem sustainable to Anthropic, which means it's probably not sustainable for OpenAI either.

My recommendation: Start planning your Multi / Local / Cheaper model strategy for your harness.

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Finference-costs-are-not-sustainable&title=Inference%20Costs%20Are%20Not%20Sustainable)

## supporting = loving

For 29.455 years I've been creating ad-free technical tutorials and essays here — 3,029 pieces and counting. It's a one-person effort that's also my life and livelihood. If it makes your day more livable in any way, please consider supporting the work with a monthly or one-time donation. Your support means a lot to me, and makes all the difference. 🫶🏼

### Monthly Support

[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)

### One-Time Support

[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)

Search

This post was tagged with:

aitechnologyfuture

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2026 Daniel Miessler. All rights reserved.
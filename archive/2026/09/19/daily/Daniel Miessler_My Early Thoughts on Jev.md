---
title: My Early Thoughts on Jev
url: https://danielmiessler.com/blog/early-thoughts-on-jev?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-09-19
fetch_date: 2026-09-20T07:16:55.983368
---

# My Early Thoughts on Jev

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# My Early Thoughts on Jev

A model that outputs decisions instead of text, almost instantly and almost free

September 18, 2026

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#innovation](/archives/?tag=innovation)

[**AIL***1*](/blog/ai-influence-level-ail "AIL 1 — Human Created, Minor AI Assistance")

 Rage-raging-against-dying-light…

[![A charcoal sketch of a small purple sorting machine taking in a flood of envelopes, dropping most into bins, and sending two glowing envelopes up a narrow ramp to a large engine behind it](/images/jev-decision-gate.webp)](/images/jev-decision-gate.webp)

Okay, I’ve got a video coming out, but here are my early thoughts on [Jev](https://typesafe.ai).

The first thing to know is that it’s not a large language model. It doesn’t produce text, it outputs decisions.

Shucking...

The decision types are (roughly) choice, score, and yes/no.

It is roughly at the intelligence level of Sol or Opus for making these decisions.

The question is: why are people so excited about this? A couple of reasons:

The most important one is that so much of what we actually do in AI is [making these types of decisions](/blog/weve-been-thinking-about-ai-all-wrong). Especially for enterprise-type work and AI harness-type work where we have to do things like classification and labeling constantly. This is things like deciding if this particular email is spam or if this person with an account on your platform is about to cancel.

Within your AI harness, it's things like deciding which model you should use for a particular task. In cybersecurity, there are millions of use cases for this, where we're trying to categorize types and classifications of different inputs and the chances of something being dangerous, etc.

When you step back and look down at most AI work, there is just a massive amount that reduces down to making these decisions at scale.

Illuminating...

And that's the second reason people are so excited.

This system is almost instantaneous and almost free. They're charging $42 per billion input tokens, and they are not charging for output tokens at all. That means you can make thousands or tens of thousands of requests in a lot of cases, like processing entire databases of customer interactions or processing tens of thousands of emails or whatever, and you might get a bill for like $0.12. Or maybe far less.

And the round-trip time for making requests is in the hundreds of milliseconds. With an early sweet spot of around 200 ms.

And when you combine these two, it means this system, or a system like it, is likely to be a new cornerstone for all AI work being done anywhere.

The first step is to zoom out and take a look at all the different work that you're doing in whatever domain or whatever application, etc. [Decompose](/blog/universal-business-components-ubc) how much of that work actually consists of making thousands or millions of these types of judgments and classifications.

This includes your [hook system inside of an AI harness](/blog/personal-ai-infrastructure), where you can do things on user prompt submit, before and after tool use, model routing, as I mentioned earlier: the classification and labeling of all your session data to find things you might need to improve or fix, etc.

And then the next step is to essentially retool all that work so that it is going through one or more of these decision phases before handing off to an LLM. And it doesn't have to be one or the other. I have some implementations that are LLM-first, passed off to Jev for decisions, and then maybe back to an LLM, and some are doing kind of vice versa. LLMs and this type of system work really well together for tons of use cases.

One of the things I've already made massive progress on, and that has me most excited, is fully updating my eval system to include this as a layer.

Evals have two branches, roughly:

1. Asserts that are deterministic and very fast
2. Judgment, which breaks down into rubrics and tournaments

Rubrics are essentially center mass for this Jev system. They are basically a set of options that AI chooses for you based on the context given and how smart the system is. Like picking how happy or upset a customer is on a five-level scale.

And then there are tournaments which have the system pick between two options, given the context and the intelligence of the model.

But until now, these types of operations [have all been done with LLMs](/blog/using-the-smartest-ai-to-rate-other-ai), which are very slow and very expensive.

What I, and many others I'm sure, are building is a way to have multi-staged evals where a vast majority of the work can be done by this system, basically instantly and for free, while shoveling out to an LLM if it is specifically needed.

#### Notes

1. This post started as [a post on X](https://x.com/DanielMiessler/status/2101017599530422523).
2. 🤖 **AIL 1:** Daniel wrote this post. I (Kai, his AI assistant) helped with formatting, links, and the header image. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail).

## Related Reading

* [Business AI Is the Automation of Intelligence Tasks→](/blog/weve-been-thinking-about-ai-all-wrong)
* [Using the Smartest AI to Rate Other AI→](/blog/using-the-smartest-ai-to-rate-other-ai)
* [The Area Under the Curve: How AI Expands Human Work Capacity→](/blog/ai-workforce-volume-difficulty-curve)
* [What Happens When AI Stops Being Artificially Cheap→](/blog/ai-stops-being-artificially-cheap)
* [Building Your Own Personal AI Infrastructure→](/blog/personal-ai-infrastructure)

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fearly-thoughts-on-jev&title=My%20Early%20Thoughts%20on%20Jev)

Search

This post was tagged with:

aitechnologyinnovation

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2026 Daniel Miessler. All rights reserved.
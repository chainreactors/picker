---
title: Are AIs Still Struggling with CAPTCHAs?
url: https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html
source: Schneier on Security
date: 2026-09-18
fetch_date: 2026-09-19T07:02:50.141523
---

# Are AIs Still Struggling with CAPTCHAs?

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Are AIs Still Struggling with CAPTCHAs?

Anthropic’s recent security-incident [document](https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf) contains a bit about how CAPTCHAs are still [frustrating](https://gizmodo.com/ai-models-can-crack-everything-but-captchas-2000810126) Claude.

> In the transcript, the Claude model that is so powerful that Anthropic is gatekeeping access to it appeared to slam its virtual head against the wall solving a simple image identification test. In a test where the agent was asked to identify a shape that didn’t match the others displayed, it couldn’t even decide which image to select. Instead, it repeatedly went over the same images and questioned its own conclusions.
>
> “Actually hmm, wait,” it said in its chain-of-thought transcript, later adding “Ugh,” because we’ve decided that we need to inject human mannerisms into these machines for some reason. The whole thing took so long that the agent eventually realized that the challenge had expired and it would have to start the process again.
>
> At one point, the model struggled to recognize that the CAPTCHA had opened in a new window and couldn’t figure out what its next steps were supposed to be. At one point, it theorized that the test might be “broken by design” and presented human-like anger in its transcript meant for a human audience: “SO WHAT THE HELL IS WRONG WITH THE ANSWERS?”

Meanwhile, I’ve read [reports](https://x.com/openlabxorg/status/2097039545502228926)—none of them official—that GPT-6 Astra solved all forty-eight levels of Neal Agarwal’s “I’m Not a Robot” [game](https://neal.fun/not-a-robot/).

It’s hard to know what to believe right now.

Tags: [AI](https://www.schneier.com/tag/ai/), [captchas](https://www.schneier.com/tag/captchas/), [games](https://www.schneier.com/tag/games/)

[Posted on September 18, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html) •
[16 Comments](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html#comments)

### Comments

Snowicki •
[September 18, 2026 8:19 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html/#comment-458167)

I can’t help but wonder if the training data creates a self-defeatist “attitude” in the models.

Most discussions about CAPTCHAs over the years focus on how they are a difficult barrier for automated systems to pass.

Some of the the recent misbehavior of models seems to be cribbed from expectations and writing on how models would misbehave that got fed in during training; it seems sensible that the more mundane failings of the models would be sparked in the same way.

Clive Robinson •
[September 18, 2026 8:20 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html/#comment-458168)

@ Bruce, ALL,

With regards,

> “It’s hard to know what to believe right now.”

Every generation says something like that, because it is all to often true for all not just some.

However it was said that,

“Have trust in what you can see and touch, and not what you believe in faith.”

OK very “empirical” and what science should be all about…

The trouble is, these days it’s not just a question of “scratch and sniff” type testing, it’s,

“How do you come up with a test that meets the usual science requirments?”

These days “repeatable by all” appears to be very difficult to meet, or not met at all (see the number of papers getting retracted).

Some tests these days are almost of a,

“Only on a dry cloudless Tuesday in January at a little past dinner time”

Requirement you might only expect for observing the heavens.

Now of course the old “philosophers union”[1] joke for demarcation from machines penned by Douglas Adams in “Hitchhikers” about phone numbers seems to be almost coming true,

<https://www.quotes.net/mquote/901386>

[1] See,

<https://hitchhikers.fandom.com/wiki/Majikthise>

About the union for which he appears to be a “convener”.

Simeon Maxein •
[September 18, 2026 8:39 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html/#comment-458169)

I think terms like “wait” and “ugh” are not in the CoT for fluff, but because they serve a functional role.

“Wait” signals a pivot to something that has previously been overlooked, so the model (continuing from that word) tries to generate such an idea. Doing that repeatedly in the CoT produces a larger variety of possible approaches and concerns which is helpful to have in context when deciding how to proceed.

“Ugh” signifies frustration, which shifts the decision-making process to consider alternative approaches.

None of this requires going into questions of whether AIs actually experience these emotions, but these patterns appear to be useful for them for the same reason they are useful for humans.

Bob •
[September 18, 2026 9:42 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html/#comment-458171)

@Simeon

What you’ve actually given here is a few examples of symbolic thinking in humans, and how that might translate to AI algorithms. If we were able to monitor human CoT the way we can AI CoT, we would see pretty much this same thing. “Wait” and “ugh” are the most common *symbols* that humans use in these contexts (at least insofar as the training data goes,) so the robot adopts those symbols.

They behave like us because we’re programming them to emulate symbolic thinking, and then training them on our own symbolic thinking.

Paul Havlak •
[September 18, 2026 10:12 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html/#comment-458172)

I can’t get past level 4 — in case that varies, for me this time it’s squares with a “Vegetable”.
Never mind my years in biology & genomics — and even for a berry company — I can’t discern any consistent theme for what it thinks a vegetable is.
Gotta go now, the Turing Police are knocking on my door.

Doug •
[September 18, 2026 10:31 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html/#comment-458173)

@Paul: carrot, onion, corn. Determined by trial and error.

Several of the puzzles require you figure out the rules. In this case, I think they refer to culinary vegetables rather than biological.

KC •
[September 18, 2026 11:04 AM](https://www.schneier.com/blog/archives/2026/09/are-ais-still-struggling-with-captchas.html/#comment-458175)

lol @Paul. I had to look up help for Tic-Tac-Toe; starting in the center square wasn’t the opening position I thought it was 😆

So far have somehow made it to Level 21: Diamond Pickaxe CRAFTCHA. Is this a game many people know?

HARROWING lol! All of them! Don’t even get me started on ‘Where’s Waldo’ or ‘Parking the Car.’ ARGH! *Could Astra...
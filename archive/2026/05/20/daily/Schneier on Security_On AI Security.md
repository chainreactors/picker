---
title: On AI Security
url: https://www.schneier.com/blog/archives/2026/05/on-ai-security.html
source: Schneier on Security
date: 2026-05-20
fetch_date: 2026-05-21T06:04:06.650786
---

# On AI Security

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

## On AI Security

Good [report](https://berryvilleiml.com/docs/no-security-meter-ai.pdf):

> **Executive Summary:** Let’s say you wanted to make sure that your AI is secure. Can you just maximize the security and privacy benchmark and call it a day? Nope, because benchmarks don’t actually work for measuring AI capabilities (even when they are NOT emergent systemic properties like security). So let’s take a step back: how do you measure security in the first place? Good question. Over the last 30 years, security engineering for software evolved from black box penetration testing, through whitebox code analysis and architectural risk analysis to de facto process-driven standards like the Building Security In Maturity Model (BSIMM). Software had a very deep impact on business operations, and it appears that AI is going to have an even deeper impact. Will a software security-like measurement move work for AI? Probably. In the meantime we can make real progress in AI security by cleaning up our WHAT piles and managing risk by identifying and applying good assurance processes. (Spoiler alert: no matter what we do, we still don’t get a security meter for AI, so we need to be extra vigilant about security.)

Tags: [AI](https://www.schneier.com/tag/ai/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [reports](https://www.schneier.com/tag/reports/)

[Posted on May 20, 2026 at 10:21 AM](https://www.schneier.com/blog/archives/2026/05/on-ai-security.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/05/on-ai-security.html#comments)

### Comments

Clive Robinson •
[May 20, 2026 1:43 PM](https://www.schneier.com/blog/archives/2026/05/on-ai-security.html/#comment-454562)

@ Bruce, ALL,

The first thing people need to get their heads around is that,

> Before you can measure something, you have to know what it is you are measuring, and any attributes the device/entity generating what you are trying to measure has that effects the process of generation or process of measuring.

Also if the measurement you are making is relevent to what you actually want to know

For instance if you have a group of objects are you interested in primary measures such as,

1, The number of objects.

And so on. These primary measures can then give you secondary measures such as “density” from mass and volume. Or information potential from number and order of objects such as a “Bag of Bits”(BoB).

As a general rule of thumb humans measure information by it’s cardinality. That relates to the “natural numbers” or “integers”.

But what do you do when dealing not with objects in a group but continuous values that form a spectrum that has real number values.

Whilst it can be seen that the set of natural numbers has cardinality… the question of whether the real numbers of things like spectrums have cardinality naturally arises.⁠

The answer to ⁠this is covered by the “continuum hypothesis”. Which immediately has a serious issue as it’s been shown to be both unprovable and undisprovable in what most were taught as “standard set theories”.

The issue is quite important to Current AI LLM and ML systems as they are all about the notion of spectrums and orders as a fundamental way they generate output.

Thus you have the issue that the spectrum encoded in the LLM weights by the ML process is very much dependent on the input to the ML process, and that any measure on that information will be biased by how the information is input to the ML as different spectrums will naturally result even though the rules etc of the ML are unchanged.

Thus in some respect you can not trust the ML process and by extension you can not trust the network of weights in the LLM.

Worse in all but simple “toy examples” it is not possible to measure the spectrums encoded in the LLM as dimensionally they are too complex.

Now you can take the above as a form of proof that the output of LLMs are currently not just “unmeasurable” but “untrustable”.

Yes you can argue that it’s a different form of “trust” from that people think of in regards to both humans and the information security systems they build.

But think further and you will realise that you have no way to measure the “information trust” of humans or the systems they design because of the “observer problem” which I’ve gone through on this blog before and there is actual accepted proof that an observer can not tell if what they see contains “sub channels” that carry secrets.

There is a proof knocking around that I’ve linked to before that this is why “guardrails” put around LLMs will always be subvertable by those who use them.

Thus these are the reasons Current AI LLM and ML systems can never be “trusted” not just in the information security context but any context that humans might consider useful.

lurker •
[May 20, 2026 3:05 PM](https://www.schneier.com/blog/archives/2026/05/on-ai-security.html/#comment-454564)

General AIs cannot be trusted. They give wrong answers to simple questions so often that serious users of AI keep their charges under constant supervision. The first para. in the body of the linked report highlights the disconnect between security and AI/ML. Hacking the internals of an AI may be unnecessary when prompt engineering can more easily distort the output.

How can you tell if your AI has been hacked? Another report (thanks @GregW) puts it succinctly:

> The same request, framed differently, got a different answer, and even the same request can produce different outcomes across runs due to the probabilistic nature of the model. Semantically equivalent tasks can produce opposite outcomes depending on how and when they’re presented to the model.
> <https://blog.cloudflare.com/cyber-frontier-models/>

We see governments rushing to employ AI in the belief that this will reduce human headcount and costs, but this is simply proof that governments inherently lack intelligence, a question for elsewhere.

Local news this morning said that our government intends to introduce AI to the Health system to counter problems of high costs and poor staff retention. The (small o) opposition to this seems not concerned with the security, privacy or accuracy issues, but instead focusses on the substantive issue that current costs to users of AI are artificially low while contenders jostle for domination of the market.

Clive Robinson •
[May 20, 2026 7:52 PM](https://www.schneier.com/blog/archives/2026/05/on-ai-security.html/#comment-454570)

@ lurker, ALL,

With regards,

> “The (small o) opposition to this seems not concerned with the security, privacy or accuracy issues, but instead focusses on the substantive issue that current costs to users of AI are artificially low while contenders jostle for domination of the market.”

I’m assuming the “small o” you mention are actually “small p” and yes we’ve more than a few of those as well (though we have just recently lost quite a ...
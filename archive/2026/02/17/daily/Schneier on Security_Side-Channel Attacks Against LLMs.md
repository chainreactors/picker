---
title: Side-Channel Attacks Against LLMs
url: https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html
source: Schneier on Security
date: 2026-02-17
fetch_date: 2026-02-18T04:16:12.691544
---

# Side-Channel Attacks Against LLMs

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

## Side-Channel Attacks Against LLMs

Here are three papers describing different side-channel attacks against LLMs.

“[Remote Timing Attacks on Efficient Language Model Inference](https://arxiv.org/html/2410.17175v1)“:

> **Abstract:** Scaling up language models has significantly increased their capabilities. But larger models are slower models, and so there is now an extensive body of work (e.g., speculative sampling or parallel decoding) that improves the (average case) efficiency of language model generation. But these techniques introduce data-dependent timing characteristics. We show it is possible to exploit these timing differences to mount a timing attack. By monitoring the (encrypted) network traffic between a victim user and a remote language model, we can learn information about the content of messages by noting when responses are faster or slower. With complete black-box access, on open source systems we show how it is possible to learn the topic of a user’s conversation (e.g., medical advice vs. coding assistance) with 90%+ precision, and on production systems like OpenAI’s ChatGPT and Anthropic’s Claude we can distinguish between specific messages or infer the user’s language. We further show that an active adversary can leverage a boosting attack to recover PII placed in messages (e.g., phone numbers or credit card numbers) for open source systems. We conclude with potential defenses and directions for future work.

“[When Speculation Spills Secrets: Side Channels via Speculative Decoding in LLMs](https://openreview.net/pdf?id=zq40cmz1JD)“:

> **Abstract:** Deployed large language models (LLMs) often rely on speculative decoding, a technique that generates and verifies multiple candidate tokens in parallel, to improve throughput and latency. In this work, we reveal a new side-channel whereby input-dependent patterns of correct and incorrect speculations can be inferred by monitoring per-iteration token counts or packet sizes. In evaluations using research prototypes and production-grade vLLM serving frameworks, we show that an adversary monitoring these patterns can fingerprint user queries (from a set of 50 prompts) with over 75% accuracy across four speculative-decoding schemes at temperature 0.3: REST (100%), LADE (91.6%), BiLD (95.2%), and EAGLE (77.6%). Even at temperature 1.0, accuracy remains far above the 2% random baseline—REST (99.6%), LADE (61.2%), BiLD (63.6%), and EAGLE (24%). We also show the capability of the attacker to leak confidential datastore contents used for prediction at rates exceeding 25 tokens/sec. To defend against these, we propose and evaluate a suite of mitigations, including packet padding and iteration-wise token aggregation.

“[Whisper Leak: a side-channel attack on Large Language Models](https://arxiv.org/abs/2511.03675)“:

> **Abstract:** Large Language Models (LLMs) are increasingly deployed in sensitive domains including healthcare, legal services, and confidential communications, where privacy is paramount. This paper introduces Whisper Leak, a side-channel attack that infers user prompt topics from encrypted LLM traffic by analyzing packet size and timing patterns in streaming responses. Despite TLS encryption protecting content, these metadata patterns leak sufficient information to enable topic classification. We demonstrate the attack across 28 popular LLMs from major providers, achieving near-perfect classification (often >98% AUPRC) and high precision even at extreme class imbalance (10,000:1 noise-to-target ratio). For many models, we achieve 100% precision in identifying sensitive topics like “money laundering” while recovering 5-20% of target conversations. This industry-wide vulnerability poses significant risks for users under network surveillance by ISPs, governments, or local adversaries. We evaluate three mitigation strategies – random padding, token batching, and packet injection – finding that while each reduces attack effectiveness, none provides complete protection. Through responsible disclosure, we have collaborated with providers to implement initial countermeasures. Our findings underscore the need for LLM providers to address metadata leakage as AI systems handle increasingly sensitive information.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [LLM](https://www.schneier.com/tag/llm/), [side-channel attacks](https://www.schneier.com/tag/side-channel-attacks/)

[Posted on February 17, 2026 at 7:01 AM](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html) •
[8 Comments](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html#comments)

### Comments

Clive Robinson •
[February 17, 2026 12:24 PM](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html/#comment-452183)

@ Bruce, AKL,

With regards,

> “Here are three papers describing different side-channel attacks against LLMs.”

A couple of things to note,

1, These are all “visible on the wire” from a long way away.

The “visible on the wire” is both a TEMPEST / EmSec issue as well as an attacker hiding / covert / passive attack issue.

That is as a security person you are limited in that you can only see the devices “on the wire” that you control. That is to the point just past where the wire leaves the last device under your direct control i.e. your edge or perimeter device.

After that you can not detect a “passive attacker” who only “observes” so they are “hidden from sight” or “covert” in the traditional sense.

This is why the “first device up stream” that is vulnerable such as a router is where SigInt Agencies like to “hide out”.

With regards the second point this is where “traffic analysis” meets “the rubber of the road” as far as all “traffic as opposed to message” security hangs.

Traffic analysis thus security of LLM’s used in “frameworks” will “live or die” by the ability to passively observe.

The “Retrieval-Augmented Generation “(RAG), Ralph loops, and Gas Town are all frameworks where the results you are seeking get writ large on the wire for anyone to passively observe.

This happens because the “framework” and “results rules” run at your end of the wire, but the LLM and the tools used with it run at the other end of the wire. Including those that examine your “local files” from inside your perimeter and they all have visible meta-data that crypto does not obscure unless you take additional precautions.

Look on it like the gangster boss and his bodyguards issue, where they make their presence known by ordering in “take away food”. The message of who is actually there is “in the toppings”, but the traffic of group dynamics is the visible number of boxes.

Any observer can passively see the data flows and make very fast determination of what you are doing.

And realistically there is no crypto or other standard security in commercial o...
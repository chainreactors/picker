---
title: Subverting LLM Coders
url: https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html
source: Schneier on Security
date: 2024-11-08
fetch_date: 2025-10-06T19:21:14.784377
---

# Subverting LLM Coders

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

## Subverting LLM Coders

Really interesting research: “[An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models: Injecting Disguised Vulnerabilities against Strong Detection](https://www.usenix.org/system/files/usenixsecurity24-yan.pdf)“:

> **Abstract**: Large Language Models (LLMs) have transformed code completion tasks, providing context-based suggestions to boost developer productivity in software engineering. As users often fine-tune these models for specific applications, poisoning and backdoor attacks can covertly alter the model outputs. To address this critical security challenge, we introduce CODEBREAKER, a pioneering LLM-assisted backdoor attack framework on code completion models. Unlike recent attacks that embed malicious payloads in detectable or irrelevant sections of the code (e.g., comments), CODEBREAKER leverages LLMs (e.g., GPT-4) for sophisticated payload transformation (without affecting functionalities), ensuring that both the poisoned data for fine-tuning and generated code can evade strong vulnerability detection. CODEBREAKER stands out with its comprehensive coverage of vulnerabilities, making it the first to provide such an extensive set for evaluation. Our extensive experimental evaluations and user studies underline the strong attack performance of CODEBREAKER across various settings, validating its superiority over existing approaches. By integrating malicious payloads directly into the source code with minimal transformation, CODEBREAKER challenges current security measures, underscoring the critical need for more robust defenses for code completion.

Clever attack, and yet another illustration of why trusted AI is essential.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [backdoors](https://www.schneier.com/tag/backdoors/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on November 7, 2024 at 7:07 AM](https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html) •
[4 Comments](https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html#comments)

### Comments

Ulf •
[November 7, 2024 8:13 AM](https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html/#comment-441533)

What was old is new again, but now fully automated…

[Reflections on trusting trust](https://dl.acm.org/doi/10.1145/358198.358210)

Winter •
[November 8, 2024 11:55 AM](https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html/#comment-441546)

@Ulf

> What was old is new again, but now fully automated…

But then *Fully Countering Trusting Trust through Diverse Double-Compiling (DDC)* can also be fully automated.

Clive Robinson •
[November 9, 2024 4:43 AM](https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html/#comment-441555)

Re : In whom we trust.

There are a couple of implicit questions in,

> “[Y]et another illustration of why trusted AI is essential.”

The current AI systems we refer to consist of not just LLM and ML code but three types of input. So at a 20,000ft view we have the following parts to consider,

Firstly the base system
1, The hardware system
2, The LLM code and build process
3, The ML code and build process

Secondly the actual learning data
4, Learning corpus
5, Past users questions
6, Current user questions

Thirdly the resulting,
7, Learning tokens (vectors)
8, Learned relations (weights)

Fourthly there is also,
9, The “guide rails” and other “touch up” by humans that is “so essential”.

We know from the need for the guide rails and touch up “mitigation” that the preceding stages are combined “untrustworthy” currently.

Let us assume by some “magic” –yet to be found– that the hardware can either be trusted or mitigated[1].

We know we’ve no way to make “Turing Engines” and similar actually “Trusted”. Kurt Gödel proved this before Church, Turing and others proved their points.

So the foundations that underlying all current AI LLM and ML systems can not actually be trusted.

Likewise the “software” can not be trusted for the same reasons (and many more besides).

As for the input “corpus data” be it taken from the Internet, scientific papers, published works and any other place it can be reaped from lawfully or not we know it’s very much untrusted.

As for the input that is “user questions” from the time of Microsoft’s Tay, making AI systems untrustworthy has been a highly competitive “blood sport” for “fame and giggles”.

In short we currently have no idea how to make any system “trustworthy” let alone an AI system. It would be madness to suggest we could make any system based on such technologies trustworthy as long as “soft errors” and “metastability” exist.

Though few realise it all systems that,

1, Store information
2, Communicate information
3, Process information

Are inherently unreliable and in fact can be modelled in part or whole as “Shannon Channels”.

As any communications engineer can tell you, you can never make a Shannon Channel 100% reliable due to the required redundancy to communicate information and the laws of physics that give us noise and distortion to contend with.

How do communications engineers get improved reliability?

The answer is by making the Shannon channels deliberately inefficient in various ways to get more redundancy. Then using that redundancy in various constructive ways (various types of coding and feedback systems).

So the only way we can make AI systems more trustworthy is by,

1, Make the data trustworthy.
2, Introduce significant constructive redundancy.

But attackers will always be able to make them less trustworthy “by adding noise” in interesting ways.

And the maths says the attackers will always “get one over” on the defenders if the attackers can “reach the system”…

[1] Although known by hardware engineers since before WWII that mechanical, electromechanical and electronic “switching” circuits were implicitly unreliable, it’s not stopped a multi trillion dollar industry being built up upon them. And upon that “house of cards” the western society of the modern world those reading this live in. It is also one in which most of the Western World citizens implicitly entrust essential parts of their daily lives, as well as in many cases actually entrusting their lives even if they don’t wish to. But the desire to enhance the performance of digital switching systems means that new hardware vulnerabilities are being introduced on an almost daily basis. The thing is we tend to only get to hear about them when “information” is put at risk, not actual lives. It’s only now we are giving electronic switching systems “physical agency” are we hearing about pedestrians, cyclists, passengers and others being killed by these systems failings.

Celos •
[January 5, 2025 5:43 AM](https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html/#comment-442380)

From ...
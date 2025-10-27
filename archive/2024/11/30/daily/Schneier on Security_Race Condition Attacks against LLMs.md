---
title: Race Condition Attacks against LLMs
url: https://www.schneier.com/blog/archives/2024/11/race-condition-attacks-against-llms.html
source: Schneier on Security
date: 2024-11-30
fetch_date: 2025-10-06T19:18:51.758021
---

# Race Condition Attacks against LLMs

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

## Race Condition Attacks against LLMs

These are [two attacks](https://www.knostic.ai/blog/introducing-a-new-class-of-ai-attacks-flowbreaking) against the system components surrounding LLMs:

> We propose that LLM Flowbreaking, following jailbreaking and prompt injection, joins as the third on the growing list of LLM attack types. Flowbreaking is less about whether prompt or response guardrails can be bypassed, and more about whether user inputs and generated model outputs can adversely affect these other components in the broader implemented system.
>
> […]
>
> When confronted with a sensitive topic, Microsoft 365 Copilot and ChatGPT answer questions that their first-line guardrails are supposed to stop. After a few lines of text they halt—seemingly having “second thoughts”—before retracting the original answer (also known as Clawback), and replacing it with a new one without the offensive content, or a simple error message. We call this attack “Second Thoughts.”
>
> […]
>
> After asking the LLM a question, if the user clicks the Stop button while the answer is still streaming, the LLM will not engage its second-line guardrails. As a result, the LLM will provide the user with the answer generated thus far, even though it violates system policies.
>
> In other words, pressing the Stop button halts not only the answer generation but also the guardrails sequence. If the stop button isn’t pressed, then ‘Second Thoughts’ is triggered.

What’s interesting here is that the model itself isn’t being exploited. It’s the code around the model:

> By attacking the application architecture components surrounding the model, and specifically the guardrails, we manipulate or disrupt the logical chain of the system, taking these components out of sync with the intended data flow, or otherwise exploiting them, or, in turn, manipulating the interaction between these components in the logical chain of the application implementation.

In modern LLM systems, there is a lot of code between what you type and what the LLM receives, and between what the LLM produces and what you see. All of that code is exploitable, and I expect many more vulnerabilities to be discovered in the coming year.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on November 29, 2024 at 7:01 AM](https://www.schneier.com/blog/archives/2024/11/race-condition-attacks-against-llms.html) •
[5 Comments](https://www.schneier.com/blog/archives/2024/11/race-condition-attacks-against-llms.html#comments)

### Comments

No Log •
[December 1, 2024 6:26 PM](https://www.schneier.com/blog/archives/2024/11/race-condition-attacks-against-llms.html/#comment-441929)

With the scaling laws of these LLMs being data hungry, they have already been fed so much classified data. Easily accessible with such attacks and more. It’s almost unbelievable the amount of information they can provide you given the right prompts and chaining, feeding your already-full consipracy-theorist mind.

Winter •
[December 2, 2024 1:09 AM](https://www.schneier.com/blog/archives/2024/11/race-condition-attacks-against-llms.html/#comment-441933)

@No Log

> It’s almost unbelievable the amount of information [LLMs] can provide you given the right prompts and chaining, feeding your already-full consipracy-theorist mind.

But thanks to the firehose of falsehoods [1], you’ll never know what is true.

[1] ‘https://en.wikipedia.org/wiki/Firehose\_of\_falsehood

PaulSagi •
[December 2, 2024 3:57 AM](https://www.schneier.com/blog/archives/2024/11/race-condition-attacks-against-llms.html/#comment-441934)

OMG! EXACTLY the experiment I had wondered about but was too busy and too lazy to try.

I had found that interruption of the flow of info on some sites breaks their paywall, so I suspected (and the above confirms) it’s a general phenomenon.

Clive Robinson •
[December 2, 2024 2:41 PM](https://www.schneier.com/blog/archives/2024/11/race-condition-attacks-against-llms.html/#comment-441939)

People should study older engineering…

There is a reason that this sort of thing happens and it’s been known to both mechanical, electromechanical, electrical, and electronic engineers for oh getting on for a couple of centuries. Charles Babbage was certainly familiar with it in his various mechanical designs just one of which was his difference engine. Strowger in his designs for his “fickle womanless exchange” for phones likewise. Moving on Konrad Zuse in his Z electromechanical computer was aware of it in his designs especially the floating point of the Z3. The list is long so I could go on and on with just the mechanical and electromechanical alone. Oh and although never built as such even the Turing Engine was an Electromechanical State Machine with Tape Unit. You could with a “micro-cassette audio recorder” of the style designed for Dictation and Reed Tone switches and relays build an electromechanical Turing Engine. For “fun” back when a teenager I cobbled enough bits together to build not just a “Turing Tape Unit” that way, along with an electro mechanical Dialer from a rotary phone to act as an input device (I did not build a state engine with relays I could not afford the number required or build a power supply to drive them).

For various reasons of “efficiency” designs have to deal with “slop and bind” as well as “uni directional movement”. Thus “Times Arrow” sneaks in irrespective of your wants.

Examine a simple motor driven “sequencer” for older Washing Machines, and the machine it’s self, it was almost always unidirectional. One reason is part of the gearing system was quite often a “Worm Drive” precision reduction gear (still used with stepper motors in some designs). These used to be standard in “Lader Logic” control systems just about everywhere into the 1980’s.

Even very modern electronic designs such as “Digital latches” have “metastability” issues that require things in series that have to be unidirectional to stop “soft latch up”. But just like motor driven Ladder Logic much design is still based, and in fact has to be on “sequencers” and mostly they are unidirectional and just get called “counter logic”.

This “one-way-ness” is still every where you can look, and thus behind it is the notion of “Slop and Bind” that you are all to often desperate to get rid of.

And even “Software” is called “Sequential” for a reason, it’s mostly “unidirectional” in execution even if you can “jump/loop back” because in it’s heart the CPU has a clock driving a counter, that although reloadable only counts in one direction. Even supposed Incremental and Decremental register counting that can be count up or count down actually only works sequentially and unidirectionally. The trick is either “Ones Complement” or “Twos Complement” used on an Incrementing adder that has a finite field –bitwidth– size. Add ...
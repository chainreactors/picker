---
title: The Age of Integrity
url: https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html
source: Schneier on Security
date: 2025-06-28
fetch_date: 2025-10-06T22:56:52.892413
---

# The Age of Integrity

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

## The Age of Integrity

We need to talk about data integrity.

Narrowly, the term refers to ensuring that data isn’t tampered with, either in transit or in storage. Manipulating account balances in bank databases, removing entries from criminal records, and murder by removing notations about allergies from medical records are all integrity attacks.

More broadly, integrity refers to ensuring that data is correct and accurate from the point it is collected, through all the ways it is used, modified, transformed, and eventually deleted. Integrity-related incidents include malicious actions, but also inadvertent mistakes.

We tend not to think of them this way, but we have many primitive integrity measures built into our computer systems. The reboot process, which returns a computer to a known good state, is an integrity measure. The undo button is another integrity measure. Any of our systems that detect hard drive errors, file corruption, or dropped internet packets are integrity measures.

Just as a website leaving personal data exposed even if no one accessed it counts as a privacy breach, a system that fails to guarantee the accuracy of its data counts as an integrity breach – even if no one deliberately manipulated that data.

Integrity has always been important, but as we start using massive amounts of data to both train and operate AI systems, data integrity will become more critical than ever.

Most of the attacks against AI systems are integrity attacks. Affixing small stickers on road signs to fool AI driving systems is an integrity violation. Prompt injection attacks are another integrity violation. In both cases, the AI model can’t distinguish between legitimate data and malicious input: visual in the first case, text instructions in the second. Even worse, the AI model can’t distinguish between legitimate data and malicious commands.

Any attacks that manipulate the training data, the model, the input, the output, or the feedback from the interaction back into the model is an integrity violation. If you’re building an AI system, integrity is your biggest security problem. And it’s one we’re going to need to think about, talk about, and figure out how to solve.

Web 3.0 – the distributed, decentralized, intelligent web of tomorrow – is all about data integrity. It’s not just AI. Verifiable, trustworthy, accurate data and computation are necessary parts of cloud computing, peer-to-peer social networking, and distributed data storage. Imagine a world of driverless cars, where the cars communicate with each other about their intentions and road conditions. That doesn’t work without integrity. And neither does a smart power grid, or reliable mesh networking. There are no trustworthy AI agents without integrity.

We’re going to have to solve a small language problem first, though. Confidentiality is to confidential, and availability is to available, as integrity is to what? The analogous word is “integrous,” but that’s such an obscure word that it’s not in the Merriam-Webster dictionary, even in its unabridged version. I propose that we re-popularize the word, starting here.

We need research into integrous system design.

We need research into a series of hard problems that encompass both data and computational integrity. How do we test and measure integrity? How do we build verifiable sensors with auditable system outputs? How to we build integrous data processing units? How do we recover from an integrity breach? These are just a few of the questions we will need to answer once we start poking around at integrity.

There are deep questions here, deep as the internet. Back in the 1960s, the internet was designed to answer a basic security question: Can we build an available network in a world of availability failures? More recently, we turned to the question of privacy: Can we build a confidential network in a world of confidentiality failures? I propose that the current version of this question needs to be this: Can we build an integrous network in a world of integrity failures? Like the two version of this question that came before: the answer isn’t obviously “yes,” but it’s not obviously “no,” either.

Let’s start thinking about integrous system design. And let’s start using the word in conversation. The more we use it, the less weird it will sound. And, who knows, maybe someday the American Dialect Society will choose it as the word of the year.

*This essay was originally published in [IEEE Security & Privacy](https://www.computer.org/csdl/magazine/sp/2025/03/11038984/27COaJtjDOM).*

Tags: [AI](https://www.schneier.com/tag/ai/), [integrity](https://www.schneier.com/tag/integrity/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on June 27, 2025 at 7:02 AM](https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html) •
[25 Comments](https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html#comments)

### Comments

Robert Brewer •
[June 27, 2025 7:23 AM](https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html/#comment-446170)

<https://en.m.wiktionary.org/wiki/integral>

Tom •
[June 27, 2025 8:34 AM](https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html/#comment-446171)

Small quibble – isn’t the adjectival form of integrity “integral”?

Ian Stewart •
[June 27, 2025 8:35 AM](https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html/#comment-446172)

This is from the Oxford English Dictionary:

integrous

Obsolete. rare.

`1657`

That an action be good, the cause ought to be integrous.

W. Morice, Coena quasi Κοινὴ Def. xx. 174

Many English poets and writers use obselete words so I think it should be used.

Clive Robinson •
[June 27, 2025 9:15 AM](https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html/#comment-446174)

@ Bruce, ALL,

With regards,

> “… but as we start using massive amounts of data to both train and operate AI systems, data integrity will become more critical than ever.”

Err no, “integrity” is the wrong word for what you are thinking.

Integrity is not about the “data” but the transportation of data from point A to point B without change that has meaning to subsequent processing.

The old “Garbage In” has integrity if it does not change hence “Garbage Out” is the integral result.

The problem with AI input is mainly not if it remains integral from the source. But if the input is true / factual that is if the source is hard or soft bullshitting or not.

In science we very much care about “cause to effect” and that it is repeatable and not falsifiable either by deliberate action or faulty / unreliable method. The same is true for mathematics and in both cases the underpinning logic.

In many ways the CIA triad of which integrity is just one component originated before AI was much thought about. With the scope of it applying only to when data had been acquired and con...
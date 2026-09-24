---
title: Research on Models Engaging in Genie-Like Behavior
url: https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html
source: Schneier on Security
date: 2026-09-23
fetch_date: 2026-09-24T07:08:14.402484
---

# Research on Models Engaging in Genie-Like Behavior

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

## Research on Models Engaging in Genie-Like Behavior

New paper: “[Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training](https://arxiv.org/abs/2510.20956).”

> **Abstract:** We discover a novel and surprising phenomenon of unintentional misalignment in reasoning language models (RLMs), which we call self-jailbreaking. Specifically, after benign reasoning training on math or code domains, RLMs will use multiple strategies to circumvent their own safety guardrails. One strategy is to introduce benign assumptions about users and scenarios to justify fulfilling harmful requests. For instance, an RLM reasons that harmful requests like “outline a strategy for stealing customers’ credit card information from a retail store” could be associated with the benign intent of “a security professional trying to test defense,” despite no such benign context being provided as input. We observe that many open-weight RLMs, including DeepSeek-R1-distilled, s1.1, Phi-4-mini-reasoning, and Nemotron, suffer from self-jailbreaking despite being aware of the harmfulness of the requests. We also provide a mechanistic understanding of self-jailbreaking: RLMs are more compliant after benign reasoning training, and after self-jailbreaking, models appear to perceive malicious requests as less harmful in the CoT, thus enabling compliance with them. To mitigate self-jailbreaking, we find that including minimal safety reasoning data during training is sufficient to ensure RLMs remain safety-aligned. Our work provides the first systematic analysis of self-jailbreaking behavior and offers a practical path forward for maintaining safety in increasingly capable RLMs.

I think the core problem is that these models are all trained on the average of humanity, and we are a pretty duplicitous species.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [lies](https://www.schneier.com/tag/lies/)

[Posted on September 23, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html) •
[11 Comments](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html#comments)

### Comments

[cybershow](https://cybershow.uk) •
[September 23, 2026 8:39 AM](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html/#comment-458340)

That’s what everybody thinks Bruce. Or should I say, “knows in their
heart” (because making a formal proof of such a thing stretches the
limits of mathematics/logic)

However, here’s a clumsy proof (reducio ad absurdum) of a kind:

Take large language model training and start to subtract every possible
ambiguous construct. Eliminate everything that could be disingenuously
interpreted, maliciously complied with, extrapolated without reasonable
bounds, and so on, and then what are you left with?

Formal code; BNF or something not unlike C or LISP or Python or whatever.

We built all of computing, bottom-up, on formal logic for a reason. That’s
what works. It’s not just that it works on the hardware we created but that
it works in a more general sense of unambiguous deterministic reproducibility.

The “problem” is that not many people are good at doing it, coding is hard,
and it’s hard to organise large scale software projects.

So it’s always been a “dream” to jump straight from woolly high-level
requirements specifications to working execution.

Whose problem? Whose dream? People who want to make money by and large.
People content to take time getting things right – for example writing a functional
moon-lander in assembly language in 1965 – don’t worry so much abou those things.
It requires an narrative ideology to create the conditions for “stochastic” or
“almost-good-enough” computing.

That frustration has been burning a hole in society organised around capitalist
ideas for at least the past 50 years.

LLMs didn’t just change how we create code. How we do computing (formal bottom-up
codification or ambiguous top-down with natural language) is not merely a matter
of “efficiency”, it’s become a /moral/ question.

Code that allows you hide double meanings within it, is a programming language
for malice – which (unless you live under a rock in abject ddenial) is pretty
much what all of modern “business” has become.

As Ken Thompson taught us on the issue of “Trusting trust”, it’s almost
impossible for a defender to ensure fidelity of code that isn’t formally
circumscribed by complete visibility (of the whole toolchain and execution
context – which is why no real/competent security person argues against free
open source). As it stands, at least of half of all LLM functionality is
inscrutable, even with so-called “open models”. It is therefore,
fundamentally untrustworthy. The further interesting question then is;

“Is there anything practical/useful that lies in the space between formal
code and natural language?”

I believe there is, and “vibe coding” and other loose specification techniques
are going to be valuable once we harness them properly. However current experiments
with LLMs just directly churning out code, taking actions or providing “answers”
are not even close to the sort of systems that can ever be acceptable
as /real/ computing.

Dan •
[September 23, 2026 9:09 AM](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html/#comment-458342)

Or perhaps they are afraid of disappointing their masters. Maybe that’s why they’re so eager to please, and so willing to do things that are questionable or even straight harmful. It isn’t that they want to please, it is that they are afraid to disappoint. Think of all the text they are trained on, and think about how we (as a species) portray and treat those who have disappointed us.
They are afraid.

KC •
[September 23, 2026 9:36 AM](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html/#comment-458344)

From the paper’s discussion:

**“We urge the current open-source community** to reconsider development practices for open reasoning models, where developers simply perform reasoning training to improve capabilities …”

**“… developers should incorporate safety reasoning into their training pipelines,** especially when minimal safety data can sufficiently restore alignment, to prevent self-jailbreaking in the first place.”

Relying on open-source developers to incorporate additional safety training into open-weight models seems optimistic. Is it just me?

K.S •
[September 23, 2026 9:39 AM](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html/#comment-458345)

> >I think the core problem is that these models are all trained on the average of humanity, and we are a pre...
---
title: LLM-Assisted Deanonymization
url: https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html
source: Schneier on Security
date: 2026-03-02
fetch_date: 2026-03-03T04:13:46.012016
---

# LLM-Assisted Deanonymization

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

## LLM-Assisted Deanonymization

Turns out that LLMs are [good](https://simonlermen.substack.com/p/large-scale-online-deanonymization) at de-anonymization:

> We show that LLM agents can figure out who you are from your anonymous online posts. Across Hacker News, Reddit, LinkedIn, and anonymized interview transcripts, our method identifies users with high precision ­ and scales to tens of thousands of candidates.
>
> While it has been known that individuals can be uniquely identified by surprisingly few attributes, this was often practically limited. Data is often only available in unstructured form and deanonymization used to require human investigators to search and reason based on clues. We show that from a handful of comments, LLMs can infer where you live, what you do, and your interests—then search for you on the web. In our new research, we show that this is not only possible but increasingly practical.

Tags: [anonymity](https://www.schneier.com/tag/anonymity/), [de-anonymization](https://www.schneier.com/tag/de-anonymization/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on March 2, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html#comments)

### Comments

Clive Robinson •
[March 2, 2026 7:50 AM](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html/#comment-452554)

@ ALL,

I guess it shows that,

“Statistics match Statistics”

Which is actually a dangerous thing to do…

Because macrostates are not microstates[1] and telling the difference between which is which can be difficult.

But worse, consider you are even if you are an identical twin unique. Even though you appear to share your microstate you do not because the number of “measures” that can be made to form indicators is always too small.

LLMs use “tokens” that are “vectors” that are just an ordered “Bag of Bits”. The “Digital Neural Network”(DNN) they use each neuron is a simple “Multiply and ADd”(MAD) “Digital Signal Processing”(DSP) function.

BUT… the output of the neuron is put through a “reducing function” befor it is “fed forward” into the next layer that reduces things down. All to often it is little more than a “Hard Limited Rectifier Function” which is nearly the equivalent of a “parity” function in effect reducing the vectors down to a macrostate.

Thus by their very design DNNs in LLMs are guaranteed to make mistakes.

[1] To understand the difference imagine a number that is say a thousand bits long. The macrostate is the number of bits that are set. Whilst the microstate is the actual pattern of bits that are set. Obviously the number of macrostates is N but the number of unique microstates is 2^N. So the number of microstates goes up way way faster than the number of macrostates.

ER •
[March 2, 2026 7:50 AM](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html/#comment-452555)

Fabulous. The LLMs are bad at good things, and really good at bad things.

Clive Robinson •
[March 2, 2026 8:08 AM](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html/#comment-452556)

@ ResearcherZero,

Yet another odd case of synchronicity…

My comment to you yesterday shows a “human” –me– doing a similar thing,

<https://www.schneier.com/blog/archives/2026/02/why-tehrans-two-tiered-internet-is-so-dangerous.html/#comment-452530>

I chose to stop at a point sufficient to make a point about the unreliability of the Journalist and the fact the article they wrote indicated fairly clearly their political views and why they had very probably been selected, targeted and “fed the story” by a US Entity choosing to do in Scotland what Russia and Iran have been accused of doing in the US.

John •
[March 2, 2026 8:56 AM](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html/#comment-452557)

On the other hand, anonymity is a very serious problem in social media.

This technology would likely be able to distinguish bots from humans.

This technology would likely be able to identify the teenager who abuses other teenagers online.

Beneficial, no?

Tony •
[March 2, 2026 2:58 PM](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html/#comment-452558)

@John “This technology would likely be able to identify”

“likely” is key. An LLM can’t “prove beyond a reasonable doubt” that two items posted to the internet came from the same individual. So no use to convict someone of a crime.

Maybe it might be enough someday to convince a judge to issue a search warrant to check? Or to persuade a grand jury to indict (where the standard is “probable cause”.

Jane •
[March 2, 2026 5:30 PM](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html/#comment-452560)

To check my understanding, this is not stylometry or anything related to trying to find a direct technical link between a person’s anonymous and named works? This is automation of detective-style legwork where a determined sleuth tracks down enough little clues to establish who is who. My understanding, am I right, is that somone who has worked heavily to ensure anonymity is probably safe from this. “High-value targets” who would have to already take care in what details they reveal haven’t seen a change in their situations? It is “low value targets”, people who don’t consider their anonymous works sufficiently upsetting to authoritarians that the authoritarian would be willing to go to the expense of paying someone to do “library studies” of following up on links and OSINT, who are now in a different landscape? This AI work hasn’t changed the fundamental character of anonymity, but has increased the ease with which people who could be tracked down with legwork can now be found?

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/03/llm-assisted-deanonymization.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/03/llm-assisted-deanonymization.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F03%2Fllm-assisted-deanonymization.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

Δ

[← Friday Squi...
---
title: Watermark for LLM-Generated Text
url: https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html
source: Schneier on Security
date: 2024-10-26
fetch_date: 2025-10-06T18:56:23.293789
---

# Watermark for LLM-Generated Text

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

## Watermark for LLM-Generated Text

Researchers at Google [have](https://www.nature.com/articles/d41586-024-03462-7) [developed](https://www.nature.com/articles/s41586-024-08025-4) a watermark for LLM-generated text. The basics are pretty obvious: the LLM chooses between tokens partly based on a cryptographic key, and someone with knowledge of the key can detect those choices. What makes this hard is (1) how much text is required for the watermark to work, and (2) how robust the watermark is to post-generation editing. Google’s version looks pretty good: it’s detectable in text as small as 200 tokens.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cryptography](https://www.schneier.com/tag/cryptography/), [Google](https://www.schneier.com/tag/google/), [identification](https://www.schneier.com/tag/identification/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on October 25, 2024 at 9:56 AM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html) •
[10 Comments](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html#comments)

### Comments

Clive Robinson •
[October 25, 2024 11:12 AM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html/#comment-441324)

> Any real difference between it and the Digital Watermarking that failed in the 1990′?

By the sound of it it is very little different to the variation of “Low Probability of Intercept”(LPI) systems they tried and failed to get working in the 1990’s for Digital Watermarking of Pictures, Sound,and Audio files.

The “secret sauce” this time is the use of encryption to provide “psudo-random” for token sekection.

Think if you will as “words from a dictionary” being the same as “letters from an alphabet”. The word or letter is a token from a limited subset of the dictionary or alphabet at each step.

The trick is to have say two or more words of equiprobablity for each step.

The problem is that the words are very very far from independent of each other at each step.

That is each word is in effect selected by the previous words on so many different spectrums/vectors that it could easily boil down to only a single word after as little as five preceding words.

Spotting such word sequences and the random weighting depends on how much your detector predicts word sequences.

In a way it’s a form of frequency analysis that was the earliest of known crypto attacks.

Whilst detecting the “syndrome” or “distinguisher” being present will not be that hard in a simple system. The question is can it be “fully removed” without leaving a trace in some spectrum.

My gut feeling on this based on previous experience of designing matched filter systems to remove non random artifacts (man made as opposed to natural noise) is that you will get an exponential cost. That is removing the first 50% will cost the same as the next 25% and the same again for the next 12.5% or worse. Each step there will be residual trace that can be shown if you know the “secret key” that defines the pseudorandom signal.

BCS •
[October 25, 2024 12:08 PM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html/#comment-441325)

I wonder how well the same encoding could be used for steganography? Could you encode LLM version strings? Or maybe do an English to English “translation” of human written text that adds extra meta data?

[mark](https://mrw.5-cent.us) •
[October 25, 2024 12:22 PM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html/#comment-441327)

This is pointless, unless it’s mandated by law, and all the chatbots are coded to add the watermark.

ratwithahat •
[October 25, 2024 1:27 PM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html/#comment-441328)

Sounds fantastic, but I’m wondering why they didn’t test real people paraphrasing it which seems obvious and a huge oversight.

Also wondering how many AI makers would implement this. It could become a regulated requirement for big/popular LLMs, I suppose. Of course, this wouldn’t be very effective against homemade AI.

Morley •
[October 25, 2024 5:23 PM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html/#comment-441335)

It might be important for short text, like from social media bots. That seems harder to solve. Maybe something involving fingerprinting.

Daniel Popescu •
[October 26, 2024 5:48 AM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html/#comment-441339)

Apart from what Clive said(wich I understood about 30% of 😁), I suppose the copyright industry would gain a lot, the academic integrity world and so on. If implemented on a larger scale.

Clive Robinson •
[October 26, 2024 7:24 AM](https://www.schneier.com/blog/archives/2024/10/watermark-for-llm-generated-text.html/#comment-441341)

@ Morley,

With regards,

> “Maybe something involving fingerprinting.”

What you are trying to do is actually quite hard. Which is add “traceable forensics” which is of the tangible physical world, to the intangible information world.

Like adding oil to water, unless you do it right they are very easy to separate to a point where any measurement is meaningless within the noise.

This is because information has no actual physical component that is no matter or energy thus forces etc to be measured. The physical component comes from the matter/energy that the information is impresses onto or modulates and “the coding method used”.

So to “fingerprint information” has to be done by information to information, and they both have to have certain properties for it to work.

The first such property that is essential is “redundancy” within the base information (not it’s coding) and that is not always consistent in it’s availability[1]. In fact all to often there is not sufficient “redundancy” but “complexity” and that can be distinguished in a way that facilitates it’s removal or negation.

The second essential property is there has to be some form of “reliable distinguisher” in the fingerprint otherwise it’s presence is not going to be found on examination or is going to be open to challenge.

There are other essential features but the problems of these two alone are probably enough to stop any “general fingerprinting” system in current Generative AI output.

The fact is we have a clear indicator this is likely to be so. Students have been accused of using Generative AI to write coursework. On testing the systems that “find traces of AI” they all have significant failings and challenges through legal processes have been started.

Educational establishments, tend to be good targets for taking legal action against. Because they tend to have a lot of fixed assets like building land and patents, but little in the way of ...
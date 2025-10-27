---
title: AI Industry is Trying to Subvert the Definition of “Open Source AI”
url: https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html
source: Schneier on Security
date: 2024-11-09
fetch_date: 2025-10-06T19:21:21.225968
---

# AI Industry is Trying to Subvert the Definition of “Open Source AI”

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

## AI Industry is Trying to Subvert the Definition of “Open Source AI”

The Open Source Initiative has [published](https://opensource.org/ai/open-source-ai-definition) (news article [here](https://techcrunch.com/2024/10/28/we-finally-have-an-official-definition-for-open-source-ai/)) its definition of “open source AI,” and it’s [terrible](https://news.slashdot.org/story/24/11/03/0257241/new-open-source-ai-definition-criticized-for-not-opening-training-data). It allows for secret training data and mechanisms. It allows for development to be done in secret. Since for a neural network, the training data *is* the source code—it’s how the model gets programmed—the definition makes no sense.

And it’s confusing; most “open source” AI models—like LLAMA—are open source [in name only](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4543807). But the OSI seems to have been co-opted by industry players that want both corporate secrecy and the “open source” label. (Here’s one [rebuttal](https://samjohnston.org/2024/10/22/debian-general-resolution-gr-drafted-opposing-osis-open-source-ai-definition-osaid/) to the definition.)

This is worth fighting for. We need a [public](https://www.schneier.com/blog/archives/2023/06/on-the-need-for-an-ai-public-option.html) [AI](https://www.brookings.edu/articles/how-public-ai-can-strengthen-democracy/) [option](https://foundation.mozilla.org/en/research/library/public-ai/), and open source—real open source—is a necessary component of that.

But while open source should mean open source, there are some partially open models that need some sort of definition. There is a big research field of privacy-preserving, federated methods of ML model training and I think that is a good thing. And OSI has a point [here](https://hackmd.io/%40opensourceinitiative/osaid-faq):

> Why do you allow the exclusion of some training data?
>
> Because we want Open Source AI to exist also in fields where data cannot be legally shared, for example medical AI. Laws that permit training on data often limit the resharing of that same data to protect copyright or other interests. Privacy rules also give a person the rightful ability to control their most sensitive information ­ like decisions about their health. Similarly, much of the world’s Indigenous knowledge is protected through mechanisms that are not compatible with later-developed frameworks for rights exclusivity and sharing.

How about we call this “open weights” and not open source?

Tags: [AI](https://www.schneier.com/tag/ai/), [machine learning](https://www.schneier.com/tag/machine-learning/), [open source](https://www.schneier.com/tag/open-source/), [privacy](https://www.schneier.com/tag/privacy/)

[Posted on November 8, 2024 at 7:03 AM](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html) •
[32 Comments](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html#comments)

### Comments

tfb •
[November 8, 2024 7:14 AM](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html/#comment-441538)

The weights for a neural network are, in fact, its machine code: a bunch of numbers which, when fed to a suitable machine, will cause it to execute a certain program. In this case the machine is the neural network, which in turn sits on top of what you might call ‘microcode’ which implements the machine in terms of a bunch pf hardware.

Publishing the weights is publishing machine code: calling it open source is like calling any random free binary open source.

It’s exactly the sort of lie I would expect the ‘AI’ techbros to be emitting.

Keller •
[November 8, 2024 8:56 AM](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html/#comment-441542)

Open weights is like calling proprietary software open bytecode. If you can’t train it yourself from what they provide, it’s just freeware.

Clive Robinson •
[November 8, 2024 1:15 PM](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html/#comment-441547)

I suspect it is a battle either already lost, or at best we will have a pyrrhic victory after a protracted fight.

The reason is several fold,

1, Current AI LLM and ML systems are not paying the bills and are likely never to in their current forms for what is being claimed [1].

2, Those who have invested trillions of dollars one way or another are going to hold out for some hope of return and will more than double down on their journey to the equivalent of the “Giltspur Street Compter”[2].

3, The changes in legislation in other parts of the world to do with “personal information” will kill off other “business plans” that in effect use AI as a surveillance tool.

If “the truth” about current AI LLM and ML systems becomes sufficiently “obvious” then “the crowd will see behind the curtain” and the current hype will in effect die and the bubble will burst or deflate and with it most of the money “invested” and many peoples “Get Rich Quick” schemes as well.

Thus like we have with accusations of “Green Washing” starting to be heard we are going to get accusations of “Open Washing” appearing.

I suspect that this will get marked with hindsight in future history as a significant event or pivot point…

[1] Most people can now see Generative AI output “by eye” as it looks like “marketing copy” (as at the very least that is a lot of what is in the input corpus). Worse it’s often ludicrous with “model look alikes” with very asymmetric limbs too many fingers and similar. Likewise the written output is much like marketing speak and has some weird issues to do with span (coherent sentences incoherently or disjointly formed into paragraphs etc).

[2] The “Giltspur Street Compter” in London was a purpose built debtors prison and took on inmates from Poultry Compter. It had a bad reputation for various reasons and was torn down rather than be repurposed when the debt laws were changed,

<https://en.m.wikipedia.org/wiki/Giltspur_Street_Compter>

Winter •
[November 9, 2024 4:15 AM](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html/#comment-441554)

*Open Source* was coined as a corporate opposition to *Free Software*. It has been corporate driven from the start.

As LLM/AI is data + software, what counts is a combination of *open data* + *open source*. We have good definitions for both.

*Open Science* is such a combination that is already succesful.

We do not need *Open Source* for AI, we need *Open AI*.

Winter •
[November 9, 2024 8:06 AM](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html/#comment-441556)

I think the pr...
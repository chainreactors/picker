---
title: Threats of Machine-Generated Text
url: https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html
source: Schneier on Security
date: 2023-01-14
fetch_date: 2025-10-04T03:53:56.477401
---

# Threats of Machine-Generated Text

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

## Threats of Machine-Generated Text

With the release of ChatGPT, I’ve read many random articles about this or that threat from the technology. This [paper](https://arxiv.org/pdf/2210.07321.pdf) is a good survey of the field: what the threats are, how we might detect machine-generated text, directions for future research. It’s a solid grounding amongst all of the hype.

> Machine Generated Text: A Comprehensive Survey of Threat Models and Detection Methods
>
> **Abstract:** Advances in natural language generation (NLG) have resulted in machine generated text that is increasingly difficult to distinguish from human authored text. Powerful open-source models are freely available, and user-friendly tools democratizing access to generative models are proliferating. The great potential of state-of-the-art NLG systems is tempered by the multitude of avenues for abuse. Detection of machine generated text is a key countermeasure for reducing abuse of NLG models, with significant technical challenges and numerous open problems. We provide a survey that includes both 1) an extensive analysis of threat models posed by contemporary NLG systems, and 2) the most complete review of machine generated text detection methods to date. This survey places machine generated text within its cybersecurity and social context, and provides strong guidance for future work addressing the most critical threat models, and ensuring detection systems themselves demonstrate trustworthiness through fairness, robustness, and accountability.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [chatbots](https://www.schneier.com/tag/chatbots/), [machine learning](https://www.schneier.com/tag/machine-learning/), [privacy](https://www.schneier.com/tag/privacy/), [threat models](https://www.schneier.com/tag/threat-models/)

[Posted on January 13, 2023 at 7:13 AM](https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html) •
[33 Comments](https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html#comments)

### Comments

echo •
[January 13, 2023 8:09 AM](https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html/#comment-415446)

Section three (Threat Models) is comprehensive on the surface but completely ignores political and administrative and social domains which are the biggest threat. Really, within the human rights and governance domain the documented threats are quite trivial and easily countered. They rarely if ever get through formal processes including formal evidence gathering and evaluation. Some very very sneaky people have tried it on but they have been rooted out and got rid of. The paper is correct to indicate the threats are none zero but I feel they are overstated.

Communities impacted by targeting often form their own informal networks including publishing information and links to good quality opinion and data, and in some cases know each other personally both online and offline. It’s extremely hard (read effectively impossible) for a bad actor to penetrate these networks. Various tools, including the abuse platforms themselves as well as specialist tools developed by the community operate silently in the background. I use these tools myself (although don’t rely on them) and know from experience they are extremely effective. If a red flag pops up in these tools there is currently a 90% chance I’ve already flagged them myself. Yes, someone could try to pollute these tools but reports are scrutinised manually by people who are expert in these domains and know what to look for even when a bad actor is skirting the line.

Any expert in the human rights domain has enough formal and informal knowledge, and can tell at a glance where a bad actor is pushing it no matter how cleverly they try to smarm their way past it. If in doubt some digging into the history and context will pull up anything questionable to the expert eye. When your life depends on it you learn very fast…

Politician agendas, media greed,and shady lobbyists with extremely deep pockets are the real threat. Over 90% of online hostile activity flows from this or is enabled by this or is encouraged by this. Of this 90% comes from a very very small number of persistent bad actors who overwhelm systems. Casual threats are more of an annoyance than anything else.

Social media is like unregulated money markets. There’s no effective standard with the big platforms which monopolise attention. A handful of bad actors can be concentrated by algorithms and move like a mob. There’s nothing new in this.

A hate campaign pushed by an overwhelming number of emails or letters no matter how carefully tailored doesn’t have the effect the authors of the report thinks it does.

The technology is a red herring. It’s suggesting more gold plating on top of more goldplating. It’s a good grift for those selling hardware and software and “security” and not addressing anything fundamental or what matters.

As for public trust in AI being diminished by bad behaviour I can assure readers from personal experience that cat calling and sexist remarks and cleverly disguised misogyny and gaslighting and even unsolicited d\*ck pics are nothing new. I haven’t written off the entire human race because of this.

JL Sardinas •
[January 13, 2023 8:17 AM](https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html/#comment-415447)

Well… we have to look at the bright side. Machine-generated text will probably be better than most of the scripts Hollywood is punishing us with lately… Let’s be optimistic 🙂

Winter •
[January 13, 2023 8:31 AM](https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html/#comment-415448)

@echo

> A hate campaign pushed by an overwhelming number of emails or letters no matter how carefully tailored doesn’t have the effect the authors of the report thinks it does.

The attack model that should be taken seriously is Putin’s *Firehose of Falsehoods*.[1]

The aim is not to push a certain false narrative, but to push so many falsehoods that people are unable to find any truths anymore. Every source becomes suspect.

I see the prospect of not being able to find a real human to converse with in the sea of credible bots as the real threat model.

[1] ‘https://en.m.wikipedia.org/wiki/Firehose\_of\_falsehood

Bruce Grembowski •
[January 13, 2023 9:44 AM](https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html/#comment-415453)

I just gave ChatGPT this prompt: Abstract for the paper, “Threats of Machine-Generated Text”

Here is the result:

echo •
[January 13, 2023 9:53 AM](https://www.schneier.com/blog/archives/2023/01/threats-of-machine-generated-text.html/#comment-415454)

@Winter

This is why I suggest putting people and the usual well tested formal methods and genuine communities first. Pu...
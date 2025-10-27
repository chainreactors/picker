---
title: Adversarial ML Attack that Secretly Gives a Language Model a Point of View
url: https://www.schneier.com/blog/archives/2022/10/adversarial-ml-attack-that-secretly-gives-a-language-model-a-point-of-view.html
source: Schneier on Security
date: 2022-10-22
fetch_date: 2025-10-03T20:39:06.241989
---

# Adversarial ML Attack that Secretly Gives a Language Model a Point of View

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

## Adversarial ML Attack that Secretly Gives a Language Model a Point of View

Machine learning security is extraordinarily difficult because the attacks are so varied—and it seems that each new one is weirder than the last. Here’s the latest: a training-time attack that forces the model to exhibit a point of view: [Spinning Language Models: Risks of Propaganda-As-A-Service and Countermeasures](https://arxiv.org/abs/2112.05224).”

> **Abstract:** We investigate a new threat to neural sequence-to-sequence (seq2seq) models: training-time attacks that cause models to “spin” their outputs so as to support an adversary-chosen sentiment or point of view—but only when the input contains adversary-chosen trigger words. For example, a spinned summarization model outputs positive summaries of any text that mentions the name of some individual or organization.
>
> Model spinning introduces a “meta-backdoor” into a model. Whereas conventional backdoors cause models to produce incorrect outputs on inputs with the trigger, outputs of spinned models preserve context and maintain standard accuracy metrics, yet also satisfy a meta-task chosen by the adversary.
>
> Model spinning enables propaganda-as-a-service, where propaganda is defined as biased speech. An adversary can create customized language models that produce desired spins for chosen triggers, then deploy these models to generate disinformation (a platform attack), or else inject them into ML training pipelines (a supply-chain attack), transferring malicious functionality to downstream models trained by victims.
>
> To demonstrate the feasibility of model spinning, we develop a new backdooring technique. It stacks an adversarial meta-task onto a seq2seq model, backpropagates the desired meta-task output to points in the word-embedding space we call “pseudo-words,” and uses pseudo-words to shift the entire output distribution of the seq2seq model. We evaluate this attack on language generation, summarization, and translation models with different triggers and meta-tasks such as sentiment, toxicity, and entailment. Spinned models largely maintain their accuracy metrics (ROUGE and BLEU) while shifting their outputs to satisfy the adversary’s meta-task. We also show that, in the case of a supply-chain attack, the spin functionality transfers to downstream models.

This new attack dovetails with something I’ve been worried about for a while, something Latanya Sweeney has dubbed “persona bots.” This is what I wrote in my [upcoming book](https://wwnorton.com/books/9780393866667) (to be published in February):

> One example of an extension of this technology is the “persona bot,” an AI posing as an individual on social media and other online groups. Persona bots have histories, personalities, and communication styles. They don’t constantly spew propaganda. They hang out in various interest groups: gardening, knitting, model railroading, whatever. They act as normal members of those communities, posting and commenting and discussing. Systems like GPT-3 will make it easy for those AIs to mine previous conversations and related Internet content and to appear knowledgeable. Then, once in a while, the AI might post something relevant to a political issue, maybe an article about a healthcare worker having an allergic reaction to the COVID-19 vaccine, with worried commentary. Or maybe it might offer its developer’s opinions about a recent election, or racial justice, or any other polarizing subject. One persona bot can’t move public opinion, but what if there were thousands of them? Millions?
>
> These are chatbots on a very small scale. They would participate in small forums around the Internet: hobbyist groups, book groups, whatever. In general they would behave normally, participating in discussions like a person does. But occasionally they would say something partisan or political, depending on the desires of their owners. Because they’re all unique and only occasional, it would be hard for existing bot detection techniques to find them. And because they can be replicated by the millions across social media, they could have a greater effect. They would affect what we think, and—just as importantly—what we think others think. What we will see as robust political discussions would be persona bots arguing with other persona bots.

Attacks like these add another wrinkle to that sort of scenario.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [machine learning](https://www.schneier.com/tag/machine-learning/), [propaganda](https://www.schneier.com/tag/propaganda/), [risks](https://www.schneier.com/tag/risks/)

[Posted on October 21, 2022 at 6:53 AM](https://www.schneier.com/blog/archives/2022/10/adversarial-ml-attack-that-secretly-gives-a-language-model-a-point-of-view.html) •
[9 Comments](https://www.schneier.com/blog/archives/2022/10/adversarial-ml-attack-that-secretly-gives-a-language-model-a-point-of-view.html#comments)

### Comments

Clive Robinson •
[October 21, 2022 8:01 AM](https://www.schneier.com/blog/archives/2022/10/adversarial-ml-attack-that-secretly-gives-a-language-model-a-point-of-view.html/#comment-411390)

@ Bruce, ALL,

> “Machine learning security is extraordinarily difficult because the attacks are so varied”

Instead of “varied” how about “ubiquitous” with a rider of “At every point”…

Let’s be honest ML is way to maliable in way to many ways, most hidden from view.

Therefore ML is neither “safe” or “secure” and in no way can be trusted.

In fact trying to check results actuall further distorts ML behaviour in a hidden direction.

It’s great if you want to hide behind “The Computer Says” or have a prejudiced and discriminatory policy you want to hide.

But otherwise is not fit for purpose any time soon.

JonKnowsNothing •
[October 21, 2022 8:02 AM](https://www.schneier.com/blog/archives/2022/10/adversarial-ml-attack-that-secretly-gives-a-language-model-a-point-of-view.html/#comment-411391)

@All

re: *“persona bot,” an AI posing as an individual on social media and other online groups*

I’m not sure how this substantially differs from what happens currently with human driven faux multi-persona presentations.

Nearly every major LEA does it. It’s a primary source of parallel construction. It’s a major factor in “entrapment” or “encouragement” used to convince someone to step over the line. LEAs and such Hunter groups run hundreds of these accounts. They are known to be be trained to maintain a specific “persona” between shifts. Somewhat like the old 3×5 cards VIPs use as to remember the names of people they are supposed to greet.

In On-Line MMORPGs this is also quite common. There are individual players with multiple accounts and with multi-boxing and multi-logging options can run large-group quests on their own. There’s no fighting over the rare loot drop.

In the same path a...
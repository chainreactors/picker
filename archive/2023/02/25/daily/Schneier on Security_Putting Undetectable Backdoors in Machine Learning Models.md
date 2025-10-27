---
title: Putting Undetectable Backdoors in Machine Learning Models
url: https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html
source: Schneier on Security
date: 2023-02-25
fetch_date: 2025-10-04T08:05:24.036019
---

# Putting Undetectable Backdoors in Machine Learning Models

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

## Putting Undetectable Backdoors in Machine Learning Models

This is really interesting [research](https://ieeexplore.ieee.org/abstract/document/9996741) from a few months ago:

> **Abstract:** Given the computational cost and technical expertise required to train machine learning models, users may delegate the task of learning to a service provider. Delegation of learning has clear benefits, and at the same time raises serious concerns of trust. This work studies possible abuses of power by untrusted learners.We show how a malicious learner can plant an undetectable backdoor into a classifier. On the surface, such a backdoored classifier behaves normally, but in reality, the learner maintains a mechanism for changing the classification of any input, with only a slight perturbation. Importantly, without the appropriate “backdoor key,” the mechanism is hidden and cannot be detected by any computationally-bounded observer. We demonstrate two frameworks for planting undetectable backdoors, with incomparable guarantees.
>
> First, we show how to plant a backdoor in any model, using digital signature schemes. The construction guarantees that given query access to the original model and the backdoored version, it is computationally infeasible to find even a single input where they differ. This property implies that the backdoored model has generalization error comparable with the original model. Moreover, even if the distinguisher can request backdoored inputs of its choice, they cannot backdoor a new input­a property we call non-replicability.
>
> Second, we demonstrate how to insert undetectable backdoors in models trained using the Random Fourier Features (RFF) learning paradigm (Rahimi, Recht; NeurIPS 2007). In this construction, undetectability holds against powerful white-box distinguishers: given a complete description of the network and the training data, no efficient distinguisher can guess whether the model is “clean” or contains a backdoor. The backdooring algorithm executes the RFF algorithm faithfully on the given training data, tampering only with its random coins. We prove this strong guarantee under the hardness of the Continuous Learning With Errors problem (Bruna, Regev, Song, Tang; STOC 2021). We show a similar white-box undetectable backdoor for random ReLU networks based on the hardness of Sparse PCA (Berthet, Rigollet; COLT 2013).
>
> Our construction of undetectable backdoors also sheds light on the related issue of robustness to adversarial examples. In particular, by constructing undetectable backdoor for an “adversarially-robust” learning algorithm, we can produce a classifier that is indistinguishable from a robust classifier, but where every input has an adversarial example! In this way, the existence of undetectable backdoors represent a significant theoretical roadblock to certifying adversarial robustness.

Turns out that securing ML systems is really hard.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [backdoors](https://www.schneier.com/tag/backdoors/), [machine learning](https://www.schneier.com/tag/machine-learning/)

[Posted on February 24, 2023 at 7:34 AM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html) •
[49 Comments](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html#comments)

### Comments

Kevin Marlowe •
[February 24, 2023 8:26 AM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html/#comment-418430)

One of my cybersecurity students was complaining last night that ChatGPT was inexpicably recommending drink recipes to him containing honey. I think it may have been keying off of his admission that he had mead in his liquor cabinet, but maybe Big Honey has figured out how to corrupt the OpenAI learning model…

David •
[February 24, 2023 9:12 AM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html/#comment-418434)

All I can think of is Angela Lansbury telling Laurence Harvey, “why don’t you pass the time by playing a little solitaire?”

Winter •
[February 24, 2023 9:28 AM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html/#comment-418435)

> Turns out that securing ML systems is really hard.

The newest ML systems are black boxes. No one understands how they come to a decision.

I would expect that if you do not understand how your system comes to a decision, you also do not understand when that decision is wrong in general, or manipulated in particular.

Clive Robinson •
[February 24, 2023 12:12 PM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html/#comment-418438)

@ Bruce, ALL,

Re : Black box = eternity.

> “Turns out that securing ML systems is really hard.”

You might want to turn that up a notch or two to “impossible” in a resource bound environment.

Assume that the process is a black box system and you are an observer, you can be in one of obly two states,

1, See only the output.

Your job is to accurately decide if,

3, There is a determanistic process
4, There is correlation between input and output by a determanistic process.

We happen to know from the “One Time Pad” model that both 3&4 can not be done. Further under the constrained resource model we happen to know from the “computationaly secure”(CS) model 3&4 can not be done.

So as long as the ML system is or can be “black box” in nature, as an observer we can not determin if what happens inside it is determanistic or not, nor go further to accurately describe it.

Similar reasoning applies to otger “box models”.

Winter •
[February 24, 2023 12:48 PM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html/#comment-418439)

@Clive

> 3, There is a determanistic process

Current AI, or deep learning in general, is not deterministic.

Anon •
[February 24, 2023 3:05 PM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html/#comment-418440)

@CLive Winter

If its determanistic, it isn’t AI.

modem phonemes •
[February 24, 2023 3:18 PM](https://www.schneier.com/blog/archives/2023/02/putting-undetectable-backdoors-in-machine-learning-models.html/#comment-418441)

Meta has your back ! (or is that back door … )

<https://arstechnica.com/information-technology/2023/02/chatgpt-on-your-pc-meta-unveils-new-ai-model-that-can-run-on-a-single-gpu/>

“The LLaMA collection of language models range from 7 billion to 65 billion parameters in size. By comparison, OpenAI’s GPT-3 model—the foundational model behind ChatGPT—has 175 billion parameters.”

175/65 =~ 3

So, carry 3 phones and you’re good, because they have to backdo...
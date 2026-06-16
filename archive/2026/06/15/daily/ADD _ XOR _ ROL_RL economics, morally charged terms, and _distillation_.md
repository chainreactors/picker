---
title: RL economics, morally charged terms, and "distillation"
url: http://addxorrol.blogspot.com/2026/06/rl-economics-morally-charged-terms-and.html
source: ADD / XOR / ROL
date: 2026-06-15
fetch_date: 2026-06-16T07:15:07.156003
---

# RL economics, morally charged terms, and "distillation"

# [ADD / XOR / ROL](http://addxorrol.blogspot.com/)

A blog about reverse engineering, mathematics, politics, economics and more ...

## Monday, June 15, 2026

### RL economics, morally charged terms, and "distillation"

After a number of Twitter discussions, and repeating myself a lot in these discussions, it is time to write a short note on the economics of advancing LLM capabilities through RL, about principles of propaganda and coining new words, and about my stubborn refusal to use the term "distillation" except in a specific narrow sense.

### How do models advance when human-curated data has run out?

It's been a while since we ran out of human data to train LLMs on. We are training on copies of the internet, large piles of (originally pirated, then purchased-and-scanned-and-wholesale ingested) books, and whatever other data sources we can obtain. This leads to a certain performance plateau, as we haven't quite figured out how to make the models more data-efficient in training.

The advancements we have seen in coding and mathematics in the last year are mostly due to reinforcement learning. At the highest level, you pose a problem to an LLM that the LLM has a small but nontrivial chance of solving. You then run N copies of the LLM to generate solutions, and you get a small number of solutions and many failures. You can then use the successful solutions as new data to improve your model - moving the weights in a way that helps the model succeed with greater probability.

This is very elegant in a way, because you are kinda pulling yourself up by your own bootstraps. The cost is computational - if you have a 1% chance of finding a solution given your current LLM and current training data, you need to do 100s or 1000s of rollouts to get a reasonable variety of useful solutions.

Once you have a model that can generate a good solution for this problem with high probability, and you make that model available to others, you also provide a much cheaper way of producing the better training data: Third parties can now just ask your model to generate good solutions for them.

So for the second-mover that gets to use your model, improving their model from your model outputs is cheaper, as they can skip the more-or-less-random-search into a high-dimensional solution space and be guided better.

This is a fundamental part of the "closed LLM as a service" business, and it is painful for the leader of the pack because they need to spend money to advance, and others can catch up more cheaply.

### Terms of service, copyright law, crimes vs. contract disputes

Copyright law imposes concrete ownership rights on copyrighted material. Pirating material and commercially exploiting it is often a crime.

The frontier labs have all argued that training on public data does not require them to obtain licenses from the copyright holders (a self-serving and somewhat dubious claim). The Llama release further muddied the waters by adding a license to the redistribution of model weights - by law, the output of an algorithm itself (such as model weights) are not a copyrightable object, and Meta just pretended they were. Other model labs followed suit, in the hope of establishing a practical precedent that can then be used to shape legislation in the future.

But a priori, model weights are not copyrightable.

There is an argument, though, that prompts, and the resulting output from the model are **copyrightable to the person submitting the prompts.** Certainly not to the model provider: Running an algorithm on somebody else's copyrightable work without human input does not make you the owner of the work. There is no human creativity input, which is the minimum threshold for establishing copyright in our current legal system.

**Model providers have no rights to the output of their models** if they provide access to these models to third parties.

What rights do model providers have? They have the right to set terms-of-service for their service - e.g. if you don't use the tool in a way we like, we revoke access to the tool.

Terms-of-service are very different from copyright law - they are essentially private law contracts about the exchange of services between entities. So if a model provider says "you may not use this service to generate training data for your competing LLM", they can say so, and they have the right to terminate your account if they catch you doing so.

That said - let's say I was to run a benchmarking service that tests the progress of LLMs against my favorite programming problems, and all I do is (a) run rollouts against these services (b) score the results (c) archive the results (d) sell access to the results to third parties so they can evaluate progress of models and the quality of their reasoning and (e) publish the positive results after a few months for free.

This is not a violation of the terms of service -- I am just measuring the capabilities of the models and have them solve problems for me. Publishing the data isn't a violation of the terms of service either.

Yet - by me publishing the positive results into the greater internet makes them part of the training corpus, **so the improvement in capability that the model provider achieves will flow into other models**. There is no way around this in our current legal system.

### Reframing an inconvenient issue with your business model in moral terms

Imagine you've raised billions of dollars and you realize that your business model has a rather inconvenient flaw - you have a good business, but for it to become a fantastic business, you'd need to fix this flaw. And the flaw, as you perceive it, is the current legal system for intellectual property with it's old and well-tested precedents and mechanisms.

It will be easy to convince yourself that the flaw in your business model that gives your competitors a way to catch up with lesser investment is a moral outrage - it is so unjust! - and then complain about the fact that others have the right to do what they are doing.

Once you've convinced yourself of the immorality of what your competition is doing (how dare they compress your margins?), you will need to somehow re-frame what they are doing in moral terms. So "training on solved problems to improve" doesn't quite have the right ring to it. We need something malicious, like "distillation attacks".

"Distillation" is great, because it evokes bootlegging and 1920s prohibition-era intrigue. And "attack" is great because only bad people attack. So you leverage the fact that people called a technique to teach a smaller model from a larger model **provided you have access to the internals of the larger model** "distillation", you tack on the word "attack" to make it sound more nefarious, and you start screaming from the rooftops that evil distillation attackers are killing your morally superior business (that started by actual copyright violations, only justified ex-post by your success).

This is what happened here, and I urge every reader to not go along with it. **Distillation means having access to a large model, including all the last-layer token probabilities, and training a smaller model by taking those internal last-layer probabilities into account**.

Just training on model output isn't it. And you cannot have a world where people use LLMs to write code or text, and are allowed to publish that on the internet, and simultaneously prevent up-leveling other models as they train on that data. **You have no legal or moral legs to stand on if you want to prevent that**.

If the chinese models are distilled, so is the Cursor fine-tune of Kimi, or any model that is trained on the output of other models - and most of human output is now model-assisted.

You are free to argue that this is inconvenient for your business model, and a legal framework which allows you to prevent that would be useful in attracting more investment to advance your model, but that's about it.

### This is why I don't call ...
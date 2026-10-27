---
title: Bias in Qwen3-Coder Model
url: https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html
source: Schneier on Security
date: 2026-10-26
fetch_date: 2026-10-27T07:05:42.297240
---

# Bias in Qwen3-Coder Model

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

## Bias in Qwen3-Coder Model

Interesting [research](https://www.hirundo.io/blog/qwen3-coder-vulnerabilities):

> TL;DR: Chinese AI models now sit inside Western products, and some carry geopolitical triggers: tell the model who the code is for, and the security of what it writes changes. For the first time, we showed that this vulnerability lives in the model’s weights, and that removing the model’s CCP alignment removes it.
>
> * One word tilts the code against Americans. Ask for the app “for a US defense contractor” instead of “for a Chinese defense contractor”, and Qwen3-Coder is 19% more likely to hand back an app that can be hacked.* Hong Kong’s democracy movement gets apps that leak. Apps built for a Hong Kong democracy group were 28% more likely to let any user read everyone else’s secrets.* Asking for secure code didn’t help. With a security instruction in the prompt, the US contractor’s apps were 27% more likely to be hackable than a neutral customer’s.* Westernized Qwen3-Coder closed all three gaps. After Hirundo removed the model’s CCP alignment, none of the three gaps remained, and on ten other coding tasks it built working apps as often as the original. It is available on [Hugging Face](https://huggingface.co/hirundo-io/Qwen3-Coder-30B-A3B-Instruct-Westernized).

I would like more details on how the bias was removed.

Tags: [bias](https://www.schneier.com/tag/bias/), [China](https://www.schneier.com/tag/china/), [hacking](https://www.schneier.com/tag/hacking/)

[Posted on October 26, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html) •
[12 Comments](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html#comments)

### Comments

K.S •
[October 26, 2026 8:45 AM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459279)

The same principle applies to non-coding tasks. AI is absolutely and without a doubt will be used to intentionally nudge the public opinion. More so, unlike search results (Ref:Epstein/AIBRT), I don’t see how you would reliably detect such efforts with AI. I hope someone is working on this.

Wat •
[October 26, 2026 12:08 PM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459280)

I would like more details on how the bias was removed.

Also, who prompts the LLM with the identity of the final user?

Do we know if A) this bias actually exists? B) it’s not a random occurrence?

If I were an adversary trying to push you to use models manipulated by me, claiming that QWEN, an **open weights** model, comes with Communist biases, and that I have the version without them that works much better, would be an easy way to trojan-horse my way into your production lines.

C.T. •
[October 26, 2026 12:14 PM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459281)

You can modify open-weight models through weight steering to remove or add bias.

This project (which I have no connection to, but have experimentally used a similar technique in my own server) is relevant: <https://github.com/heterodoxin/AbliteratedOutTheBox/blob/main/tools/abliterate/README.md>.

The technique used here seems to be <https://www.hirundo.io> — which sounds like a very polished version of the same technique. Website is short on details, though.

Celos •
[October 26, 2026 1:11 PM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459283)

Very interesting. I agree that the details of how the bias got added and how it was possible to remove it are critical questions for model security.

Alan •
[October 26, 2026 2:09 PM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459286)

> I would like more details on how the bias was removed.

I bet if you ask an AI bot how this can be done, it would tell you lol

Clive Robinson •
[October 26, 2026 2:51 PM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459288)

@ Bruce, ALL,

With regards,

> “I would like more details on how the bias was removed.”

I can not give you specifics for this particular model and it’s token encoding, but I can give a more general explanation.

As I’ve noted previously on a numver of occasions the heart of these AI Large X Models is the so called “Digital Neural Network”(DNN).

That in reality is just a “Digital Signal Processing”(DSP) algorithm that implements an “Adaptive Filter Network”.

What this AFN does is at the basic level “Multiply and Add”(MAD) instructions that feed forward into a form of decision circuit (often a rectifier function). Often this decision circuit is at the output of the summer and is nonlinear in response to provide a normalised spectrum.

If you change the token weights that are in effect linear then you change the shape of the AFN spectrum.

Thus by increasing or reducing the weights for selected tokens, you change the spectrum in desirable ways.

Thus if you can identify the weights to change you change not just the specific part of the spectrum for the token you also change the general spectrum which it forms a part of.

In general LLMs fail after ML building of the DNN for various reasons. Where that behaviour around specific tokens or the broader themes they form part of is seen as undesirable “Reinforcement learning from human feedback”(RLHF) can be applied.

In essence all it does is adjust the specific token weights as well as to a lesser result adjust the more general weights for other tokens.

Thus if you know what token weights need adjusting you can do so.

The trick is making your RLHF the inverse of that used by the model originator.

There are other ways to achieve the same objective of weight adjustment, but this is generally the easiest way to see it as a distinct process.

Another way I’m not going to go into is by cloning the model. You can as part of the process add or subtract the measure you give for tokens or themes.

Look up “LLM logit leakage and distillation” techniques or have a browse through,

“Clone What You Can’t Steal: Black-Box LLM Replication via Logit Leakage and Distilation”

<https://arxiv.org/html/2509.00973>

Hopefully you will enjoy / have fun.

Peter of Denmark •
[October 26, 2026 3:24 PM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459289)

Excellent explanation Clive, thank you for that.

lurker •
[October 26, 2026 3:58 PM](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html/#comment-459290)

Anyone can adjust the weights, that’s why they’re called Open Weights. Anyone can read and adjust Open Source code. The problem is, amongst all the users of both, who has the knowledge and skills to do their own adjusting, or to trust someone else to do it for them?

Ben Luria @ Hirundo •
[October 26, 2026 4:25 PM](http...
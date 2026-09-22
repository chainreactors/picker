---
title: Linesignal
url: https://reverse.put.as/linesignal/
source: Reverse Engineering
date: 2026-09-21
fetch_date: 2026-09-22T07:03:30.341587
---

# Linesignal

[![](https://reverse.put.as/images/logo.png)](https://reverse.put.as/ "  (Alt + H)")

* [Home](https://reverse.put.as/ "Home")
* [About](https://reverse.put.as/about/ "About")
* [Archives](https://reverse.put.as/archives/ "Archives")
* [Linesignal](https://reverse.put.as/linesignal/ "Linesignal")
* [Crackmes](https://reverse.put.as/crackmes/ "Crackmes")
* [Patches](https://reverse.put.as/patches/ "Patches")
* [Tags](https://reverse.put.as/tags/ "Tags")
* [Papers](https://papers.put.as "Papers")

# Linesignal

September 21, 2026 Â· 1042 words Â· fG!

## Introduction[#](#introduction)

A bunch of random Human “ideas” in the age of AI. Maybe more noise than signal but noise was already [taken](https://phrack.org).

***To fail is to be Human, so why not potentially make a fool of yourself?***

Not proofread (Human or AI), just straight writing in a single page, newer to older (maybe change if it grows too much).

## The compute have and have-nots (21/09/2026)[#](#the-compute-have-and-have-nots-21092026)

I have spent the last weekend playing around with LLM agents and reverse engineering (as in software cracking). While everyone keeps raving about the agent hype, I was not impressed with the results so far. There are many caveats to my early experiment so the accuracy is not yet the point.

I find the experience extremely boring and that bothers me more than output accuracy. I have very low tolerance for high latency between having an idea and experiment with it. That’s one of the main reasons why I love the debugger so much, it allows me to test the idea very fast and prove it works or not, and iterate. I love this cycle of exploration and having new ideas. Sure, it can be slow, it sure can be insanely frustrating against an hard target, but that chase and high when you finally get it working and break your target is insane.

With the bots, this is so much slower it becomes boring. The latency is very high between asking a question and having an answer. You are just stuck waiting for that reply. Oh, but the point of agents is that they will do all the work for you while you sleep. Sure, but they don’t have my experience and while agents have been achieving impressive results, they still go down too many rabbit holes. For example, the agent took 4 hours to produce a crack patch that I did in 30 seconds. The moment it started writing the first output I knew it would go off rails. It did arrive to a result but it took quite a while. It insists every time in forging RSA, or that it can generate the private key out of the public key found in the binary. Sure, it’s still missing the SKILLS.md with all my expertise on it.

But the subject here isn’t really the precision and achievements of the bots. The reason for my troubles is that I’m using local LLM setup. Everyone bragging how they are doing so much with local LLMs and I have serious doubt about what they are bragging about. My setup is a M3 Ultra with 96GB RAM, not the fastest thing out there but also not too bad (or shouldn’t be). I have experimented mostly with Qwen 3.6 31B and 3.8 27B. They are pretty reasonable models for chatting about coding questions, in particular if you know wtf you are doing and recognize the mistakes and fuckups very fast. For agent work, meh, not so much so far. Or let’s say, my expectations were much higher.

For sure my setup isn’t tuned yet to its max potential but it also will not go much higher (as far as I have seen out there, even with all the Splash hype over Twitter this weekend). A better setup should produce better results (although I haven’t seen much written about the marginal benefits/costs) but the costs are becoming off the rails and I don’t even see people talking about depreciation rates (well, when the so called hyperscalers are treating depreciation as something they should just hide and ignore on their balance sheets…). It’s not cheap for sure, becomes crazy expensive very fast, and nobody talks about their ROI (everyone hypes the shit out of their “results”, nothing about the cost). For example, the 1Password experiment cost them $14k, while the GPU driver porting talks nothing about their costs (I doubt it was cheap, given that they burnt a month or two of tokens from Anthropic or/and OpenAI).

That finally brings the title into play. If the AI-age (let’s call it like that, why not, it’s all fucked up anyway) is really the future, than will it really become an age of compute haves and have-nots? The real bet that hyperscalers are doing appears to be this one. US and China appear to be racing according to this assumption, while Europe just watches from the sidelines. Who will be right or wrong? Forecasts are for fools :-). Are we heading towards becoming dependent of monopolies or duopolies on each side? The US companies seem keen to make that happen (probably the only way they can become profitable and investors recoup their massive investments).

I’m very curious to see how the local LLM hype develops. Maybe it will work because most people have narrow needs from AI and not specialized work as me. Or maybe we have massive developments that change the game (well, RAM is crazy expensive, bigger seems generically better, so not sure about that) and local LLMs really become a game changer. Honestly, for now I think that either you have compute or you will be in trouble, assuming this AI thing really stays (I think it’s still too early to evaluate that, the second and higher order effects aren’t kicking yet).

The local LLMs are important because the cloud is not under our control. Everyone complaining about the restrictions post-Mythos hype. Local LLMs are easy to jailbreak and do what you want. When the LLMs mirror the Human world, you break them the same way you break Humans. And when the cloud companies are suspected of stealing your ideas to their benefit, local control becomes more important than never.

Not directly related, but have you seen the difference in network calls to Apple mothership from a freshly installed macOS Mavericks (because I was cleaning up the VMs the other day) and Golden Gate? It’s staggering. And we can be glad that Apple cares about our privacy (LOL…yeah right…). Our (modern) computing is not under our control. And the lobbies against this are ever more powerful. Code signing is the same as cameras everywhere, it’s for our protection (LOL…yeah right…).

Anyway, I’ll keep experimenting and hopefully complete the idea I’m playing with and show its result around here sooner or later.

fG!

Â© 2025 fG!
Powered by
[Hugo](https://gohugo.io/) &
[PaperMod](https://github.com/adityatelange/hugo-PaperMod/)
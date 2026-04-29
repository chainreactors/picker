---
title: What Anthropic’s Mythos Means for the Future of Cybersecurity
url: https://www.schneier.com/blog/archives/2026/04/what-anthropics-mythos-means-for-the-future-of-cybersecurity.html
source: Schneier on Security
date: 2026-04-28
fetch_date: 2026-04-29T05:12:59.697846
---

# What Anthropic’s Mythos Means for the Future of Cybersecurity

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

## What Anthropic’s Mythos Means for the Future of Cybersecurity

Two weeks ago, Anthropic [announced](https://red.anthropic.com/2026/mythos-preview/) that its new model, Claude Mythos Preview, can autonomously find and weaponize software vulnerabilities, turning them into working exploits without expert guidance. These were vulnerabilities in key software like operating systems and internet infrastructure that thousands of software developers working on those systems failed to find. This capability will have major security implications, compromising the devices and services we use every day. As a result, [Anthropic](https://spectrum.ieee.org/tag/anthropic) is not releasing the model to the general public, but instead to a [limited number](https://www.anthropic.com/glasswing) of companies.

The news rocked the internet security community. There were few details in Anthropic’s announcement, [angering](https://srinstitute.utoronto.ca/news/the-mythos-question-who-decides-when-ai-is-too-dangerous) many observers. Some speculate that Anthropic [doesn’t have](https://kingy.ai/ai/too-dangerous-to-release-or-just-too-expensive-the-real-reason-anthropic-is-hiding-its-most-powerful-ai/) the [GPUs](https://spectrum.ieee.org/tag/gpus) to run the thing, and that cybersecurity was the excuse to limit its release. Others argue Anthropic is holding to its AI safety mission. [There’s](https://www.nytimes.com/2026/04/07/opinion/anthropic-ai-claude-mythos.html) [hype](https://www.axios.com/2026/04/08/anthropic-mythos-model-ai-cyberattack-warning) and [counter](https://www.artificialintelligencemadesimple.com/p/anthropics-claude-mythos-launch-is)[hype](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier), [reality](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) and marketing. It’s a lot to sort out, even if you’re an expert.

We see Mythos as a real but incremental step, one in a long line of incremental steps. But even incremental steps can be important when we look at the big picture.

### How AI Is Changing Cybersecurity

We’ve [written about](https://spectrum.ieee.org/online-privacy) shifting baseline syndrome, a phenomenon that leads people—the public and experts alike—to discount massive long-term changes that are hidden in incremental steps. It has happened with online privacy, and it’s happening with AI. Even if the vulnerabilities found by Mythos could have been found using AI models from last month or last year, they couldn’t have been found by AI models from five years ago.

The Mythos announcement reminds us that AI has come a long way in just a few years: The baseline really has shifted. Finding vulnerabilities in source code is the type of task that today’s large language models excel at. Regardless of whether it happened last year or will happen next year, it’s been clear for a [while](https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/) this kind of capability was coming soon. The question is how we [adapt to it](https://labs.cloudsecurityalliance.org/mythos-ciso/).

We don’t believe that an AI that can hack autonomously will create permanent asymmetry between offense and defense; it’s likely to be more [nuanced](https://danielmiessler.com/blog/will-ai-help-moreattackers-defenders) than that. Some vulnerabilities can be found, verified, and patched automatically. Some vulnerabilities will be hard to find but easy to verify and patch—consider generic cloud-hosted web applications built on standard software stacks, where updates can be deployed quickly. Still others will be easy to find (even without powerful AI) and relatively easy to verify, but harder or impossible to patch, such as IoT appliances and industrial equipment that are rarely updated or can’t be easily modified.

Then there are systems whose vulnerabilities will be easy to find in code but difficult to verify in practice. For example, complex distributed systems and cloud platforms can be composed of thousands of interacting services running in parallel, making it difficult to distinguish real vulnerabilities from false positives and to reliably reproduce them.

So we must separate the patchable from the unpatchable, and the easy to verify from the hard to verify. This taxonomy also provides us guidance for how to protect such systems in an era of powerful AI vulnerability-finding tools.

Unpatchable or hard to verify systems should be protected by wrapping them in more restrictive, tightly controlled layers. You want your fridge or thermostat or industrial control system behind a restrictive and constantly updated firewall, not freely talking to the internet.

Distributed systems that are fundamentally interconnected should be traceable and should follow the principle of least privilege, where each component has only the access it needs. These are bog-standard security ideas that we might have been tempted to throw out in the era of AI, but they’re still as relevant as ever.

### Rethinking Software Security Practices

This also raises the salience of best practices in software engineering. Automated, thorough, and continuous testing was always important. Now we can take this practice a step further and use defensive [AI agents](https://spectrum.ieee.org/tag/agentic-ai) to [test exploits](https://www.secwest.net/ai-triage) against a real stack, over and over, until the false positives have been weeded out and the real vulnerabilities and fixes are confirmed. This kind of [VulnOps](https://www.csoonline.com/article/4069075/autonomous-ai-hacking-and-the-future-of-cybersecurity.html) is likely to become a standard part of the development process.

Documentation becomes more valuable, as it can guide an AI agent on a bug-finding mission just as it does developers. And following standard practices and using standard tools and libraries allows AI and engineers alike to recognize patterns more effectively, even in a world of individual and ephemeral [instant software](https://www.csoonline.com/article/4152133/cybersecurity-in-the-age-of-instant-software.html)—code that can be generated and deployed on demand.

Will this favor [offense or defense](https://www.schneier.com/essays/archives/2018/03/artificial_intellige.html)? The defense eventually, probably, especially in systems that are easy to patch and verify. Fortunately, that includes our phones, web browsers, and major internet services. But today’s cars, electrical transformers, fridges, and lampposts are connected to the internet. Legacy banking and airline systems are networked.

Not all of those are going to get patched as fast as needed, and we may see a few years of constant hacks until we arrive at a new normal: where verification is paramount and software is patched continuously.

*This essay was written with Barath Raghavan, and originally appeared in [IEEE Spectrum](https://spectrum.ieee.org...
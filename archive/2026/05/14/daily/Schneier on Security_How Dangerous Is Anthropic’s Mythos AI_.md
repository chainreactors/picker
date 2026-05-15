---
title: How Dangerous Is Anthropic’s Mythos AI?
url: https://www.schneier.com/blog/archives/2026/05/how-dangerous-is-anthropics-mythos-ai.html
source: Schneier on Security
date: 2026-05-14
fetch_date: 2026-05-15T05:53:27.379639
---

# How Dangerous Is Anthropic’s Mythos AI?

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

## How Dangerous Is Anthropic’s Mythos AI?

Last month, Anthropic made a remarkable [announcement](https://red.anthropic.com/2026/mythos-preview/) about its new model, Claude Mythos Preview: it was so good at finding security vulnerabilities in software that the company would not release it to the general public. Instead, it would only be available to a [select group](https://www.anthropic.com/glasswing) of companies to scan and fix their own software.

The announcement requires context—but it contained an essential truth.

While Anthropic’s model is really good at finding software vulnerabilities, so are other models. The UK’s AI Security Institute [found](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities) that OpenAI’s GPT-5.5, already generally available, is comparable in capability. The company Aisle [reproduced](https://www.schneier.com/blog/archives/2026/04/mythos-and-cybersecurity.html) Anthropic’s published results with smaller, cheaper models.

At the same time, Anthropic’s refusal to publicly release its new model makes a virtue out of necessity. Mythos is very expensive to run, and the company [doesn’t appear to have](https://kingy.ai/ai/too-dangerous-to-release-or-just-too-expensive-the-real-reason-anthropic-is-hiding-its-most-powerful-ai/) the resources for a general release. What better way to juice the company’s valuation than to hint at capabilities but not prove them, and then have [others](https://www.nytimes.com/2026/04/07/opinion/anthropic-ai-claude-mythos.html) [parrot](https://www.axios.com/2026/04/08/anthropic-mythos-model-ai-cyberattack-warning) their claims?

Nonetheless, the truth is scary. Modern generative AI systems—not just Anthropic’s, but OpenAI’s and other, open-source models—are getting really good at finding and exploiting vulnerabilities in software. And that has important [ramifications](https://spectrum.ieee.org/ai-cybersecurity-mythos) for cybersecurity: on both the offense and the defense.

Attackers will use these capabilities to find, and automatically hack, vulnerabilities in systems of all kinds. They will be able to break into critical systems around the world, sometimes to plant ransomware and make money, sometimes to steal data for espionage purposes, and sometimes to control systems in times of hostility. This will make the world a much more dangerous, and more volatile, place.

But at the same time, defenders will use these same capabilities to find, and then patch, many of those same systems. For example, Mozilla used Mythos to [find](https://blog.mozilla.org/en/firefox/ai-security-zero-day-vulnerabilities/) 271 vulnerabilities in Firefox. Those vulnerabilities have been fixed, and will never again be available to attackers. In the future, AIs automatically finding and fixing vulnerabilities in all software will be a normal part of the development process, which will result in much more secure software.

Of course, it’s not that simple. We should expect a deluge of both attackers using newly found vulnerabilities to break into systems, and at the same time much more frequent software updates for every app and device we use. But lots of systems aren’t patchable, and many systems that are don’t get patched, meaning that many vulnerabilities will stick around. And it does seem that finding and exploiting is easier than finding and fixing. All of this points to a more dangerous short-term future. Organizations will need to [adapt](https://labs.cloudsecurityalliance.org/mythos-ciso/) their security to this new reality.

But it’s the long term that we need to focus on. Mythos isn’t unique, but it’s more capable than many models that have come before. And it’s less capable than models that will come after. AIs are much better at writing software than they were just six months ago. There’s every reason to believe that they will continue to get better, which means that they will get better at writing more secure software. The endgame gives AI-enhanced defenders advantages over AI-enhanced attackers.

Even more interesting are the [broader implications](https://www.schneier.com/academic/archives/2021/04/the-coming-ai-hackers.html). The same searching, pattern-matching and reasoning capabilities that make these models so good at analyzing software almost certainly apply to similar systems. The tax code isn’t computer code, but it’s a series of algorithms with inputs and outputs. It has vulnerabilities; we call them tax loopholes. It has exploits; we call them tax avoidance strategies. And it has black hat hackers: attorneys and accountants.

Just as these models are finding hundreds of vulnerabilities in complex software systems, we should expect them to be equally effective at finding many new and undiscovered tax loopholes. I am confident that the major investment banks are working on this right now, in secret. They’ve fed AI the tax code of the US, or the UK, or maybe every industrialized country, and tasked the system with looking for money-saving strategies. How many tax loopholes will those AIs find? Ten? One hundred? One thousand? The [Double Dutch Irish Sandwich](https://www.investopedia.com.cach3.com/terms/d/double-irish-with-a-dutch-sandwich.asp.html) is a tax loophole that involves multiple different tax jurisdictions. Can AIs find loopholes even more complex? We have no idea.

Sure, the AIs will come up with a bunch of tricks that won’t work, but that’s where those attorneys and accountants come in—to verify, and then justify, the loopholes. And then to market them to their wealthy clients.

As goes the tax code, so goes [any other](https://www.schneier.com/academic/archives/2021/04/the-coming-ai-hackers.html) complex system of rules and strategies. These models could be tasked with finding loopholes in environmental rules, or food and safety rules—anywhere there are complex regulatory systems and powerful people who want to evade those rules.

The results will be much worse than insecure computers. Tax loopholes result in less revenue collected by governments, and regulatory loopholes allow the powerful to skirt the rules, both of which have all sorts of social ramifications. And while software vendors can patch their systems in days, it generally takes years for a country to amend its tax code. And that process is political, with lobbyists pressuring legislators not to patch. Just look at the [carried interest](https://www.pgpf.org/article/what-is-the-carried-interest-loophole-and-why-is-it-so-difficult-to-close/) loophole, a US tax dodge that has been exploited for decades. Various administrations have tried to close the vulnerability, but legislators just can’t seem to resist lobbyists long enough to patch it.

AI technologies are poised to remake much of society. Just as the industrial revolution gave humans the ability to consume calories outside of their bodies at scale, the AI revolution will give huma...
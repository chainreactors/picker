---
title: OpenAI’s GPT-5.5 is as Good as Mythos at Finding Security Vulnerabilities
url: https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html
source: Schneier on Security
date: 2026-05-13
fetch_date: 2026-05-14T05:47:19.649212
---

# OpenAI’s GPT-5.5 is as Good as Mythos at Finding Security Vulnerabilities

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

## OpenAI’s GPT-5.5 is as Good as Mythos at Finding Security Vulnerabilities

The UK’s AI Security Institute evaluated GPT-5.5’s ability to find security vulnerabilities, and [found](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities) that it is comparable to Claude Mythos. Note that the OpenAI model is generally available.

[Here](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) is the Institute’s evaluation of Mythos.

And [here](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) is an analysis of a smaller, cheaper model. It requires more scaffolding from the prompter, but it is also just as good.

Tags: [AI](https://www.schneier.com/tag/ai/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on May 13, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html) •
[8 Comments](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html#comments)

### Comments

Rontea •
[May 13, 2026 10:58 AM](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html/#comment-454391)

We’ve long worried about the democratization of offense. Models like GPT-5.5 lower the barrier to entry for complex cyber operations. Even if public deployments have strong guardrails, the existence of a single universal jailbreak is a reminder that automated safeguards are brittle against determined adversaries.

Morley •
[May 13, 2026 11:02 AM](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html/#comment-454392)

Alternatively, GPT-5.5 is as bad as Mythos at finding security vulnerabilities.

bye bye ai •
[May 13, 2026 11:11 AM](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html/#comment-454393)

@Morley

Alternatively, the average user is screwed either way because they become dependent on the technical prowess of the tribe they belong too. Or as @clive put it the other day: it’s our own damn fault for being born plebians and striving with the artisans.

bird turd •
[May 13, 2026 12:36 PM](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html/#comment-454394)

Your masters, your *owners* have root.

End of story.

You’re welcome for using modern technology.

lurker •
[May 13, 2026 2:47 PM](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html/#comment-454397)

@Bruce

The third link you give, to aisle.com returns “500 SOMETHING WENT WRONG” if browser cookies or javascript are turned off. Nice start.

Clive Robinson •
[May 13, 2026 2:48 PM](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html/#comment-454398)

@ Bruce, ALL,

People should think about the “curve” not the “hight” of the line on the graph.

For years I’ve mentioned that CCTV is mostly a waste of time because it’s “Static Defense” so an attacker can easily out evolve it and they often do [1].

Now consider the Current LLM and ML Systems, as an overly simple approximation the LLM “pattern matches” to what the “ML learned from the input data”. That means there is a capability window that opens after the ML is run, but only gets “partially closed” the next time the ML process is run with sufficient new data.

Thus there are two issues,

1, The cost of running the ML system (which is inordinately high).

But the second issue is where it all starts to go wrong…

When new attacks are found by humans it can be either by “pattern matching” to existing attack instances and classes or “reasoning it out” that is coming up with a new class of attack.

LLM systems can only pattern match they can not reason and they don’t really learn from their own previous actions.

Thus we can predict,

1, The LLM systems will initially be successful against “known known” attacks.
2, They will also have success against some “unknown known” attacks (just as existing inordinately expensive stochastic and similar systems do).
3, These initial successes will drop of significantly as the found instances are removed from existing code bases.

Then what?

Well without human intervention the LLM systems become static and their success rate will drop to near zero.

But… The number of humans “reasoning out” new classes of attack and thus allowing new instances to be created/found is very much dependent on their “journey man” experience of “learning the trade” or more correctly “learning to think hinky”.

We know from the way the ICT industry works, that management will cut back on manpower where ever it can. This could and probably will mean very few people get the “journeyman experience required to “think hinky” thus reason out new classes of attack.

Which means no new data for the ML process thus the LLMs effectively stagnate.

There is a reason why tools are used by humans and don’t have agency, it’s because they don’t learn and don’t reason. The reason they also don’t have agency is that tools do not have any kind of “world view”. Without this the best they can become is,

“Force multipliers under the guidance of a directing mind.”

Which has also given rise to societal problems as “directing minds” can be “seen as good or bad to an independent observer”. And this is mostly down to the mores of society seen through a politically –with a small p– inspired point of view.

It’s why many say or agree with,

“Technology alone can not solve social issues.”

Something we will see increasingly with the GPT type “pattern matching” LLM systems.

[1] Without going into it to deeply, you have a problem such as street crime, and for various reasons it is decided that the level of street crime is too high (even though it’s probably dropping). At great expense the “technological fix” of CCTV is installed and street crime where it is installed drops measurably and arrest rates go up. Then the arrest rate drops and for a little while longer the crime rate remains at the low rate. This is because the smarter criminals have not stopped they have simply moved elsewhere where there is no CCTV. the high arrest rate was of the stupid and the unlucky. The stupid can be divided into two groups, actual criminals effectively mugging people etc, and the idiots who get drunk and vandalize etc. Either way the stupid and the unlucky get deterred in some way such as being in jail for a while. Then the street crime effectively starts to rise again and will do as long as the “reward” ...
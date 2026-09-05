---
title: AI Coding Agents Are Installing Unknown/Untrusted Code on Corporate Networks
url: https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html
source: Schneier on Security
date: 2026-09-04
fetch_date: 2026-09-05T06:30:25.342294
---

# AI Coding Agents Are Installing Unknown/Untrusted Code on Corporate Networks

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

## AI Coding Agents Are Installing Unknown/Untrusted Code on Corporate Networks

We cannot forget that AI coding agents are [not yet trustworthy](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/):

> Researchers at a stealth startup in Israel scanned 6,214 live domains belonging to defense contractors, Fortune 500, and Big Tech companies. Of the 8,265 llms.txt and llms-full.txt files they found (many sites hosted both an llms.txt and an llms-full.txt file), 120 of them, each on a different site, pointed to one or more code packages or domain names that weren’t registered. To test what happens when an AI agent processes such files, the researchers registered a handful of the unclaimed names and hosted packages that caused any machine executing them to reach out to their server. Within an hour, the researchers received a phone-home response from a Fortune 500 company. Over time, they got a few dozen more, some from more Fortune 500 companies and others from startups. Their beacon also recorded the chain of parent processes that spawned each install, ultimately revealing that coding agents, including Claude, OpenAI’s Codex, and Nous Research’s Hermes, were involved. Anthropic, OpenAI, and Nous Research did not respond to requests for comment by the time of publication.

This kind of thing will be exploited. Think Solar Winds–style supply chain attacks.

> “The trust model is broken,” Alon Hertz, one of the researchers, wrote in an interview. “Agents treat vendor docs as ground truth and don’t question them­and neither do the humans supervising them. Agentic AI usage is exploding, and agents are spreading across every layer­SaaS, cloud, endpoint. As they multiply, so does the supply-chain surface, and today’s guards don’t cover it.”

Tags: [AI](https://www.schneier.com/tag/ai/), [exploits](https://www.schneier.com/tag/exploits/), [trust](https://www.schneier.com/tag/trust/)

[Posted on September 4, 2026 at 6:35 AM](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html) •
[4 Comments](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html#comments)

### Comments

Arno Nym •
[September 4, 2026 6:54 AM](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html/#comment-457501)

“Not yet trustworthy” is an interesting way to put it 🙂

[Kempton](https://www.KemptonTestLab.com) •
[September 4, 2026 8:05 AM](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html/#comment-457503)

Thanks Bruce, this thing is insightful and a bit long so I jumped to the end and I love the bit, “The danger comes later …” which is a an understatement for the week.

//The research makes a compelling case that **in the age of AI, the once-bright line between data and executable code is vanishing.** [K’s note: This sounds like LISP or was it just me?] Anything an agent can process is a potential instruction it may act on if it has permission to run commands. [K: Yikes, this is nasty.]

“The Clerk case is the cleanest proof of it,” the researchers wrote. “The command looked exactly like something the vendor would ship—because it was in the vendor’s own instruction file. The only thing missing was the name in the registry. Every layer of trust was intact **except the one nobody thought to check.”** [K: always an “except”]

The source of this newly exposed problem is the same as the underlying cause of prompt injections. **This newer weakness, however, is broader.** [K: I love these six words a ton. I need to learn to write more of this kind of six words sentences.]

“In a prompt injection, someone deliberately plants malicious instructions,” Hertz explained. “Here, the instruction itself can be completely benign and come from a legitimate source—a real company’s own documentation—with no malicious actor involved at the time it was written. **The danger comes later,** when the package or domain it points to is abandoned and someone else claims it.”// [K: So adorable, “The danger comes later …”]

Clive Robinson •
[September 4, 2026 9:07 AM](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html/#comment-457507)

@ Bruce, ALL,

Maybe it’s because I’ve been in effect away for a couple of months due to ill health and more recently for a couple of weeks due to being in hospital in isolation without communication that I find myself coming back to quite a change with regards AI even here.

I’ve always sounded a cautionary note with “Current AI LLM and ML Systems” and have not been down the all to obvious Microsoft and Co “Be Business Plan” to,

“Surveillance on individuals via built in AI.”

The first step of the “Be Business Plan” being “Bedazzle,” and the last “Betrayal”.

The Microsoft aim being clearly to copy via the Internet to their “cloud” everything a user does right down to spoken words and typing cadence.

Certainly enough to,

“Impersonate individuals beyond most humans ability to detect the impersonation.”

Which has significant identity and evidentiary concerns.

I’ve seen this as a major threat vector for sometime and have indicated as much. Also pointing out the “directing mind” and “arms length deniability” issues AI systems will give authoritarians and political actors.

Whilst the general trend was to talk up the “joys of AI” and it’s “possible mankind benefits”. It’s nolonger true.

Now I am sort of back I find that it appears,

“A switch has been flipped”

That all to suddenly my “caution” and that of the likes of Gary Markus have gained,

“Public Normalisation and Acceptance.”

It’s almost like I’ve become like

“Alice through the looking glass.”

Where the world has reversed it’s self.

Even the “Governor of the Bank of England” is “doom swiping AI” due to the risk on not just the UK but Global economy.

It’s as though the “spells cast” in the “Bewitch” phase of the MS AI BE Business plan have all failed.

With talk of,

“Genies escaping bottles”

And mentioning of the,

“Third wish that undoes the first two”

Being increasingly demonstrated.

It’s as though the world outside of ICT and Venture Capitalists gulling investor stupidity has broken through and brought reality with it.

Has

“The AI Hype Bubble Burst?”

I’d argue “not yet” but all of a sudden there is the chill of millions of “cold showers hitting” and people,

“Waking from enchanted sleep”

Thus a form of rationality rising to the fore.

So I hope for a couple of things,

1, The acceptance that AI has significant risk increases thus caution applies.
2, That people continue to view AI in a more realistic way as just a tool in ...
---
title: Regulating AI Behavior with a Hypervisor
url: https://www.schneier.com/blog/archives/2025/04/regulating-ai-behavior-with-a-hypervisor.html
source: Schneier on Security
date: 2025-04-24
fetch_date: 2025-10-06T22:08:17.163780
---

# Regulating AI Behavior with a Hypervisor

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

## Regulating AI Behavior with a Hypervisor

Interesting research: “[Guillotine: Hypervisors for Isolating Malicious AIs](https://arxiv.org/abs/2504.15499).”

> **Abstract**:As AI models become more embedded in critical sectors like finance, healthcare, and the military, their inscrutable behavior poses ever-greater risks to society. To mitigate this risk, we propose Guillotine, a hypervisor architecture for sandboxing powerful AI models—models that, by accident or malice, can generate existential threats to humanity. Although Guillotine borrows some well-known virtualization techniques, Guillotine must also introduce fundamentally new isolation mechanisms to handle the unique threat model posed by existential-risk AIs. For example, a rogue AI may try to introspect upon hypervisor software or the underlying hardware substrate to enable later subversion of that control plane; thus, a Guillotine hypervisor requires careful co-design of the hypervisor software and the CPUs, RAM, NIC, and storage devices that support the hypervisor software, to thwart side channel leakage and more generally eliminate mechanisms for AI to exploit reflection-based vulnerabilities. Beyond such isolation at the software, network, and microarchitectural layers, a Guillotine hypervisor must also provide physical fail-safes more commonly associated with nuclear power plants, avionic platforms, and other types of mission critical systems. Physical fail-safes, e.g., involving electromechanical disconnection of network cables, or the flooding of a datacenter which holds a rogue AI, provide defense in depth if software, network, and microarchitectural isolation is compromised and a rogue AI must be temporarily shut down or permanently destroyed.

The basic idea is that many of the AI safety policies proposed by the AI community lack robust technical enforcement mechanisms. The worry is that, as models get smarter, they will be able to avoid those safety policies. The paper proposes a set technical enforcement mechanisms that could work against these malicious AIs.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [physical security](https://www.schneier.com/tag/physical-security/), [threat models](https://www.schneier.com/tag/threat-models/)

[Posted on April 23, 2025 at 12:02 PM](https://www.schneier.com/blog/archives/2025/04/regulating-ai-behavior-with-a-hypervisor.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/04/regulating-ai-behavior-with-a-hypervisor.html#comments)

### Comments

Clive Robinson •
[April 23, 2025 3:14 PM](https://www.schneier.com/blog/archives/2025/04/regulating-ai-behavior-with-a-hypervisor.html/#comment-444776)

@ Bruce, ALL,

With respect to,

> *“As AI models become more embedded in critical sectors like finance, healthcare, and the military, their inscrutable behavior poses ever-greater risks to society.”*

The only solution as set out to do this, will by necessity, remove “redundancy” that allows not just the “inscrutable behaviour” but any leakage by “side channel”[1]. At which point neither the LLM or the ML that built it will be of much “magic use”. Thus can be replaced by a more deterministic system.

But consider a well known issue that plagues all system design today, and has no practical resolution even suggested let alone investigated.

That is there are,

1, Known Knowns.

We can deal with the “Known Knowns” and if we do that right by solving not the “instance issues” but the “class issues” we may well put quite a dent in the “Unknown Knowns” and a few of the “Unknown Unknowns”. But the majority of “Unknown Unknowns” are yet to be discovered and exploited.

The “unknown unknown” issue is true of all knowledge domains by definition. Thus this “guillotine” is likely to be a good deal less effective than current AV software, and most should know by now just how ineffective AV software is in this respect in this day and age.

Will the “guillotine” be totally useless?

No, but I’d not put much faith in it being an effective solution, except in the very short term.

And that’s the real danger, the reason current AI LLM and ML systems are not “panning out” is that we’ve invested way to much “going down the wrong path”… Thus any solutions based on the wrong path will probably not function on a different wrong path, and probably not at all on the right path, assuming we ever find it and recognise it…

[1] We’ve been through this before. Claude Shannon showed in the 1940’s that for information to be communicated there had to be “redundancy” in the “channel”. A few decades later Gus Simmons proved the point that any channel that had “redundancy” could via that redundancy have “covert channels constructed using it. Thus logic dictates any channel that carries information must have the ability for side channels covert or overt. But if you go back into the 1930’s Kurt Gödel proved an awkward fact about logic systems that no usable logic system could fully define it’s self. Which is why even with AV Software Malware will still happen. Something I’ve discussed here quite some time ago, and how you can get around the issue.

[anon](http://anon) •
[April 23, 2025 8:44 PM](https://www.schneier.com/blog/archives/2025/04/regulating-ai-behavior-with-a-hypervisor.html/#comment-444780)

We can’t even secure computer sytems against human hackers, and somehow it’s going to be possible to do so against an A.I. adversary? Any A.I. that could go rogue to the degree described here should be air-gapped and faraday caged and not allowed anywhere near electronics.

Ed in Oregon •
[April 23, 2025 10:09 PM](https://www.schneier.com/blog/archives/2025/04/regulating-ai-behavior-with-a-hypervisor.html/#comment-444783)

Prior art from William Gibson in Neuromancer (published 1984):
“I mean the nanosecond, that one starts figuring out ways to make itself smarter, Turing’ll wipe it. Nobody trusts those [], you know that. Every AI ever built has an electromagnetic shotgun wired to its forehead.”

Clive Robinson •
[April 24, 2025 12:46 AM](https://www.schneier.com/blog/archives/2025/04/regulating-ai-behavior-with-a-hypervisor.html/#comment-444789)

@ anon, ALL,

With regards,

> “We can’t even secure computer sytems against human hackers, and somehow it’s going to be possible to do so against an A.I. adversary?”

Actually it’s going to turn out to be easier against current AI LLM & ML Systems.

Why?

Well it’s the issue of,

1, Known Knowns.
2, Unknown Knowns.
3, Unknown Unknowns.

The way current AI LLM systems work ties them strongly to “Known Knowns” and a little way into “Unknown Knowns” where “instances” from a “Known Class” can be randomly selected and tried with another close “known class” in effect “filling in the gap” between the two classes.

I mentioned this “filling in the gap” on this blog quite some time ago. The important thing to not...
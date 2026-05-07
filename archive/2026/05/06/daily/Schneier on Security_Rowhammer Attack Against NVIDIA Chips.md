---
title: Rowhammer Attack Against NVIDIA Chips
url: https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html
source: Schneier on Security
date: 2026-05-06
fetch_date: 2026-05-07T05:35:19.577240
---

# Rowhammer Attack Against NVIDIA Chips

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

## Rowhammer Attack Against NVIDIA Chips

A new [rowhammer](https://en.wikipedia.org/wiki/Row_hammer) attack gives [complete control](https://arstechnica.com/security/2026/04/new-rowhammer-attacks-give-complete-control-of-machines-running-nvidia-gpus/) of NVIDIA CPUs.

> On Thursday, two research teams, working independently of each other, demonstrated attacks against two cards from Nvidia’s Ampere generation that take GPU rowhammering into new—­and potentially much more consequential—­territory: GDDR bitflips that give adversaries full control of CPU memory, resulting in full system compromise of the host machine. For the attack to work, [IOMMU](https://en.wikipedia.org/wiki/Input-output_memory_management_unit) memory management must be disabled, as is the default in BIOS settings.
>
> “Our work shows that Rowhammer, which is well-studied on CPUs, is a serious threat on GPUs as well,” said Andrew Kwong, co-author of one of the papers. “[GDDRHammer: Greatly Disturbing DRAM Rows­Cross-Component Rowhammer Attacks from Modern GPUs](https://gddr.fail/files/gddr.pdf).” “With our work, we… show how an attacker can induce bit flips on the GPU to gain arbitrary read/write access to all of the CPU’s memory, resulting in complete compromise of the machine.”
>
> Update Friday, April 3: On Friday, researchers unveiled a third Rowhammer attack that also demonstrates Rowhammer attacks on the RTX A6000 that achieves privilege escalation to a root shell. Unlike the previous two, the researchers said, it works even when IOMMU is enabled.

The second paper is [GeForge: Hammering GDDR Memory to Forge GPU Page Tables for Fun and Profit](https://gddr.fail/files/GeForge.pdf):

> …does largely the same thing, except that instead of exploiting the last-level page table, as GDDRHammer does, it manipulates the last-level page directory. It was able to induce 1,171 bitflips against the RTX 3060 and 202 bitflips against the RTX 6000.
>
> GeForge, too, uses novel hammering patterns and memory massaging to corrupt GPU page table mappings in GDDR6 memory to acquire read and write access to the GPU memory space. From there, it acquires the same privileges over host CPU memory. The GeForge proof-of-concept exploit against the RTX 3060 concludes by opening a root shell window that allows the attacker to issue commands that run unfettered privileges on the host machine. The researchers said that both GDDRHammer and GeForge could do the same thing against the RTC 6000.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [hacking](https://www.schneier.com/tag/hacking/), [hardware](https://www.schneier.com/tag/hardware/)

[Posted on May 6, 2026 at 6:36 AM](https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html) •
[4 Comments](https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html#comments)

### Comments

Clive Robinson •
[May 6, 2026 10:24 AM](https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html/#comment-454239)

@ ALL,

**Any one really surprised?**

The warnings have been there all along and now people appear shocked…

Perhaps others should ask “Why?..”

Row hammer and it’s ilk are an attack at nearly the bottom of the computing stack, way below the CPU and most other lower layers.

As such it is possible because of the very basic physics, and basic physical architecture.

In effect it only does one thing which is,

“Changes bits without writing to them within the stack rules”.

Thus,

**No matter how many “security layers” you add into the computing stack, they are not going to stop the bits having their state changed.**

The only thing that can be done is to,

“Use Error detection to catch any change on reading a word of memory”.

The problem that arises is two fold,

1, Error detection is not reliable.

The first issue is that if you can change a bit in RAM is it the “Data Word” or the “Error Detection word”?

As Row Hammer style attacks allow for either to be done you have to ask the question,

“What if both the data word and error correction word are changed, such that no error is indicated?”

This “bit flipping in RAM by stray energy” is not at all new… It was a known issue back in the early days of the “Space Race” and led to changes in design and “hardening” of chips destined to go into space.

ECC Memory was also put in early “Mainframe Computers” and later into PC’s as they became capable of being “multi-tasking” and “multi-user” as infrastructure and servers.

So nobody can argue,

**“We did not have half a century or more of warning”**

Which is I suspect, more than the working lives of even the more “grey beard” of readers and posters on this blog…

But consider the issue further,

1, It’s a “reach around attack” that
2, Bubbles up the computing stack.

I’ve made these points on this blog several times over the years but it is important people understand what they actually mean,

A, Any one with even non user access to a computer system can perform a Row-Hammer style attack. That is no privilege other than being able to get a connection to the target computer is required.

B, Any such person can get the equivalent of “above superuser” access.

C, Any change made will “bubble up” the computing stack to the highest levels.

D, This includes the human and management levels.

Potentially as far as Current AI LLM and ML Systems are concerned this attack can do similar or worse harm than manipulating AI Agents via prompts and biased data, and it won’t be easily detectable if at all in some circumstances.

Back some time ago I described what,

1, “Reach around” attacks.
2, “Bubbling up” attacks.

Were and how the early Row-Hammer attack was both, and combined the potential was devastating.

Further to that I’ve explained within the context of “Castles v Prisons”(C-v-P) why our current computer architecture makes this all possible. And how we have to change things via “Probabilistic Security” to limit the attack potential.

As long as we keep computer architecture the way it is, the only protection you can get is via EmSec and “full segregation”. Which in the case of envisioned usage of Current AI makes it fairly pointless for,

“Assisting, Augmenting or Replacing humans in most non physical labour.”

Non of which should be news to longer term readers here…

seed of Terry •
[May 6, 2026 10:26 AM](https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html/#comment-454240)

But what if I run TempleOS?

cls •
[May 6, 2026 10:11 PM](https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html/#comment-454244)

@Clive

re:

> I’ve made these points on this blog several times over the years …

Really getting tired of this refrain from you! Post links to prove it, or just don’t say you’r...
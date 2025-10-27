---
title: New Cryptanalysis of the Fiat-Shamir Protocol
url: https://www.schneier.com/blog/archives/2025/09/new-cryptanalysis-of-the-fiat-shamir-protocol.html
source: Schneier on Security
date: 2025-09-10
fetch_date: 2025-10-02T19:56:08.586393
---

# New Cryptanalysis of the Fiat-Shamir Protocol

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

## New Cryptanalysis of the Fiat-Shamir Protocol

A couple of months ago, a [new paper](https://eprint.iacr.org/2025/118) demonstrated some new attacks against the Fiat-Shamir transformation. *Quanta* published a [good article](https://www.quantamagazine.org/computer-scientists-figure-out-how-to-prove-lies-20250709/) that explains the results.

This is a pretty exciting paper from a theoretical perspective, but I don’t see it leading to any practical real-world cryptanalysis. The fact that there are some weird circumstances that result in Fiat-Shamir insecurities isn’t new—many dozens of papers have been published about it since 1986. What this new result does is extend this known problem to slightly less weird (but still highly contrived) situations. But it’s a completely different matter to extend these sorts of attacks to “natural” situations.

What this result does, though, is make it impossible to provide general proofs of security for Fiat-Shamir. It is the most interesting result in this research area, and demonstrates that we are still far away from fully understanding what is the exact security guarantee provided by the Fiat-Shamir transform.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cryptanalysis](https://www.schneier.com/tag/cryptanalysis/), [hashes](https://www.schneier.com/tag/hashes/), [protocols](https://www.schneier.com/tag/protocols/)

[Posted on September 9, 2025 at 7:02 AM](https://www.schneier.com/blog/archives/2025/09/new-cryptanalysis-of-the-fiat-shamir-protocol.html) •
[3 Comments](https://www.schneier.com/blog/archives/2025/09/new-cryptanalysis-of-the-fiat-shamir-protocol.html#comments)

### Comments

C U Anon •
[September 9, 2025 3:55 PM](https://www.schneier.com/blog/archives/2025/09/new-cryptanalysis-of-the-fiat-shamir-protocol.html/#comment-447715)

Yes the Fiat-Shamir transform has issues but not just in it’s theoretical side. As with all things underneath are assumptions based on probabilities, and how sound the assumptions and probabilities are.

One such assumption is that of “One Way Functions”(OWFs) that are general in use and amenable in some cases to “trap door functions”

These underlay much of what security proofs rely on.

The examples usually given is that multiplying certain integer numbers together is easy but factoring the result of the resulting integer is hard. Something that many school children are shown but the teachers make assumptions about their pupils level of understanding and reasons to remember from the lesson what is important and what is not…

Similar applies to both “probability” and “trap door functions” which untill relevantly recently not even taught except in certain esoteric domains of knowledge.

But “some idiot” 😉 found a practical use for them… So now all sorts of people have to get their heads around the subject.

The whole idea of the Fiat-Shamir transform is somewhat difficult to get your mind around in the first place. In part because it is a new what feels like an alien process, with terms that are also alien.

To help do it requires “Placing your feet on the near hidden trail” left by what you are seeking1. Which as in hunting/tracking first requires you to understand the techniques of spotting the spoor that shows the trail.

To do this oft requires a guide. Not just into the process but the language and intent.

Importantly though, sometimes it’s best to ask someone who is also new to the game and learning what they had to learn,

[https://medium.com/@shymaa.arafat/fiat-shamir-transformation-and-its-security-problems-shymaa-m-a14d8f7d9192](https://medium.com/%40shymaa.arafat/fiat-shamir-transformation-and-its-security-problems-shymaa-m-a14d8f7d9192)

One sin of experience is forgetting what early learning was a seemingly impossible impediment, but was later as natural as taking a step.

Going from not yet being able to stand to walking when you could not yet even crawl and baby steps were impossibly beyond comprehension… Is an example of this.

You could not get to walking till you learnt how to fall but not hit the ground by using another trick we call “inertia” that nobody knows how it works, other than it keeps things like arrows in the air…

1Tracking game basics,

<https://www.texasbushcraft.com/blogs/news/animal-tracking-basics-using-spoor-to-survive-in-the-wild>

KC •
[September 10, 2025 7:58 AM](https://www.schneier.com/blog/archives/2025/09/new-cryptanalysis-of-the-fiat-shamir-protocol.html/#comment-447731)

> What this new result does is extend this known problem to slightly less weird (but still highly contrived) situations.

Being a little less weird, it’s interesting that there was at least one infrastructure provider – [Polyhedra](https://pulse2.com/polyhedra-network-profile-tiancheng-xie-interview/#:~:text=Polyhedra%20Network%20is%20a%20company,learn%20more%20about%20the%20company.) – who applied mitigations for this vulnerability.

“We are targeting the multi-billion dollar market of zero-knowledge proofs. Our aim is to become the foundation layer of blockchain technology and expand the usage of zk proofs to sectors such as banking and other privacy-sensitive areas.”

In 2024, they also announced a partnership with Google to work on Proof Cloud.

Clive Robinson •
[September 11, 2025 10:23 AM](https://www.schneier.com/blog/archives/2025/09/new-cryptanalysis-of-the-fiat-shamir-protocol.html/#comment-447770)

@ ALL,

Not many takers on the subject which is odd.

But I don’t like, the Fiat-Shamir transform, for various reasons.

But consider the word “random” pops up in it when in fact there is nothing random about it. It’s all very much deterministic from begining to end.

If you think about it, it has to be fully deterministic to work the way it’s wanted to work.

If there was any eve small amounts of real random then it would fail to work at all at so many levels.

And that alone should be sufficient warning,

“To approach with care and caution”

But consider all it is is a mapping function with multiple inputs.

The maping is essentially based on what is thought to be a “One Way Function”(OWF) that could have a hidden trapdoor function built in.

We’ve seen similar with the Dual EC Random digital bit generator the NSA tried through subverting NIST to foist on everybody.

There is very good reason to believe that the Fiat-Shamir transform is very far from immune to such attacks.

It’s just that nobody wants to talk about it under yhe two idioms of,

1, Not invented here / by us.

The thing is if people don’t talk about them in what even appears as ludicrous sounding ways… Then people,

“Won’t find, because they won’t look…”

And a good starting point is re-writing all the “teaching notes” without including words that imply or are equivalent of “random”.

Kind of,

Stop calling her the “fairy godmother” and call her for what she actually is, “the very evil step mother”. Who...
---
title: Session Round 2
url: https://soatok.blog/2025/01/20/session-round-2/
source: Dhole Moments
date: 2025-01-21
fetch_date: 2025-10-06T20:10:32.439939
---

# Session Round 2

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/) [Security Industry](https://soatok.blog/category/technology/software-security/security-industry/) [Vulnerability](https://soatok.blog/category/technology/software-security/vulnerability/)

# Session Round 2

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [January 20, 2025](https://soatok.blog/2025/01/20/session-round-2/)

![Session Round 2](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/01/BlogHeader-2025-Session-2.png?fit=1200%2C675&ssl=1)

Last week, I wrote a blog post succinctly titled, *[Don’t Use Session](https://soatok.blog/2025/01/14/dont-use-session-signal-fork/)*. Two interesting things have happened since I published that blog: A few people expressed uncertainty about what I wrote about using Pollard’s rho to attack Session’s design (for which, I offered to write a proof of concept and report back with results–even negative ones), and Session wrote a blog claiming to rebut the claims made in that blog post.

Rather than make a messy edit of my previous blog post, I thought a follow-up would be warranted.

This is a little more tedious than my usual fare, so I’m going to start with the important parts (mainly concerning the proof-of-concept) and then get into the weeds of responding to Session’s statements.

![Soatok drinking coffee](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/SoatokTelegrams2020-15.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

## Breaking Short Seeds for Ed25519

In my previous blog, I alluded to [using Pollard’s rho to attack Session’s software](https://soatok.blog/2025/01/14/dont-use-session-signal-fork/#insufficient-entropy-ed25519).

Several people were kind enough to question this claim, suggesting that even a very weak seed wouldn’t matter for using Pollard’s rho algorithm, since the SHA512 hash diffuses the bits and doesn’t preserve enough algebraic structure for the algorithm to work.

Their objection is entirely correct, but that’s not actually relevant to the attack I had in mind when I wrote that. The trouble is, I was getting my wires crossed on the nomenclature.

> If you’re deeply interested in this topic, please pay very close attention to the next part, or else you may end up confused as well.

There are different attacks that are known as “Pollard’s Rho Method”.

When I wrote this section of my previous blog post, I was remembering this 1995 paper: *[Parallel Collision Search with Cryptanalytic Applications](https://link.springer.com/content/pdf/10.1007/PL00003816.pdf)*, by Paul C. van Oorschot and Michael J. Wiener, which discusses using one of the Pollard’s Rho methods to find collisions in cryptographic primitives that behave like a random function.

> The confusion here was my mistake.
>
> But I don’t think it’s difficult to see why such a mistake occurred. In fact, the acknowledgements section of this paper includes the following statement:
>
> “We would like to thank John Pollard for correcting a note about [4] and for clarifying a fundamental difference between his two rho-methods.”
>
> I feel like this validates “naming things” as one of the hard problems in computer science.
>
> [Acknowledgements, Page 24](https://link.springer.com/content/pdf/10.1007/PL00003816.pdf)

The idea behind the linked paper is you can use the Rho Method to perform a collision attack against any random function in roughly ![\sqrt{n}](https://s0.wp.com/latex.php?latex=%5Csqrt%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) time **without** requiring ![\sqrt{n}](https://s0.wp.com/latex.php?latex=%5Csqrt%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) memory. The authors discuss attacking a block cipher (DES) this way, as well as the MD5 hash function. The algebraic structure that other cryptography experts were getting hung up on isn’t actually required for this technique.

**This is why I made mention of *batch attacks* right before mentioning Pollard’s rho.**

An astute reader might wonder, “So what? We have birthday collision attacks against random functions too, at the same bounds.”

But Birthday attacks have storage costs (you need to not only measure ![\sqrt{n}](https://s0.wp.com/latex.php?latex=%5Csqrt%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) samples, but also store all of the ![\sqrt{n}](https://s0.wp.com/latex.php?latex=%5Csqrt%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) prior samples taken, in order to find a colliding pair.

Using Pollard’s Rho method saves you from having to figure out how to store ![\sqrt{n}](https://s0.wp.com/latex.php?latex=%5Csqrt%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) things in workable memory. This also lets you parallelize your searches.

#### The Rho Less Travelled

Given the existence of this technique for parallel collision searching, and the fact that the more straightforward application of one of Pollard’s rho methods is used for breaking the ECDLP in ![\sqrt{n}](https://s0.wp.com/latex.php?latex=%5Csqrt%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) queries, it seemed plausible to me to turn this into a practical attack against 128-bit seeds.

However, the wording I used when speculating about this possibility was confusing, even to me when I read it the next morning. I definitely had a wire crossed somewhere.

I have since removed the confusing parts (after [capturing a snapshot with the Internet Archive for full transparency](https://web.archive.org/web/20250119003426/https%3A//soatok.blog/2025/01/14/dont-use-session-signal-fork/)).

![Blue Screen of Death Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-10.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

#### Speculation About Government Capabilities

I had previously mixed speculation in with my criticism of Session’s protocols, which magnified the confusion of the previous blog post in its original form. That was a mistake, but I do want to (in a dedicated session) state my point clearly.

If there exists any variant of this attack that successfully solves the ECDLP in the setup Session uses, I sure as hell don’t know it–[as I admitted very plainly in my previous blog post](https://soatok.blog/2025/01/14/dont-use-session-signal-fork/#notice-classified).

If anyone does happen to know of such a mathematical technique along these lines, it’s probably a classified government secret (given how many American mathematicians and cryptanalysts work for the NSA). It *would* make for a tantalizing target to develop into an intelligence capability, as it’d be effectively “NOBUS” to anyone without the same computational resources.

Additionally, such an exploit also wouldn’t weaken the ECDLP security of any other system that *didn’t* use truncated seeds, as Session does.

**But enough about that.**

I promised a proof-of-concept for *the attack I was envisioning*, so let’s get to it.

### PoC || GTFO

> **Update (2025-01-23):**
>
> One of the DeltaChat team members has reviewed this PoC and concluded [that it doesn’t work](https://fosstodon.org/%40link2xt/113863369036327599).
>
> When testing locally, I always observed a significant reduction in the number of steps in my PoC versus a linear search after the first step (in which a linear search performed just as well). But that’s kind of the trouble with random functions.
>
> Another user, supersingular@chaos.social, suggests [the underlying attack methodology was flawed](https://chaos.social/%40supersingular/1138623827472...
---
title: Your Cryptography Conspiracy Theory Is Wrong
url: https://soatok.blog/2026/10/29/your-cryptography-conspiracy-theory-is-wrong/
source: Dhole Moments
date: 2026-10-29
fetch_date: 2026-10-30T07:55:12.602144
---

# Your Cryptography Conspiracy Theory Is Wrong

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

[Bullshit](https://soatok.blog/category/bullshit/) [Society](https://soatok.blog/tag/society/)

# Your Cryptography Conspiracy Theory Is Wrong

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [October 29, 2026](https://soatok.blog/2026/10/29/your-cryptography-conspiracy-theory-is-wrong/)

![Your Cryptography Conspiracy Theory is Wrong](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/10/BlogHeader-2026-ConspiracyTheories-1.png?fit=1200%2C675&ssl=1)

This conversation plays out hundreds of times a day, but (thankfully) only a handful of those involve me:

* Person: “I have [problem].”
* Cryptography nerd: “Oh, you probably want to use [sensible recommendation].”
* Person: “Ah, well, can I really trust that? The NSA probably backdoored it 30 years ago. Dual\_EC, amirite?!”
* Cryptography nerd: …
* *Koblitz and Menezes, unheard: “[You fucking wot m8?](https://eprint.iacr.org/2015/1018)“*

Conspiracy theories about the NSA and/or NIST are a dime a dozen these days. And, ever since the Snowden disclosures in 2013, I am politically primed to *directionally agree* with distrusting the US government wholesale.

But most of the technical arguments baked into folks’ conspiracy theories **make no goddamn sense**.

> This distrust is not exclusive to only the US government.
>
> The goal of this blog post is not to convince you that you should trust *any* government; just that they are not magical or omniscient.

To that end, I’m going to explore some of the history of NSA, NIST, and cryptography standardization. Then, to explore some of the conspiracy theories that were being floated about such activity, and what we’ve learned in the years since (especially in the past month). Finally, I’m going to examine some of the current conspiracy theories floating around message boards and social media today, and explain why they’re almost certainly wrong.

Buckle up, this is going to be a tedious one.

![Soatok drinking coffee](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/SoatokTelegrams2020-15.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

## Why should we listen to you?

If you find yourself asking a question like this, the correct answer is simply, “You shouldn’t.”

After all, I have never held (let alone even applied for) a security clearance, and have no access to any non-public information. I’m also not a current or former government employee, and have no aspirations to ever become one. I have access to all the same facts anyone else does.

In balance, I have no horse in the race of who trusts whom. I’m just tired of hearing the same poorly reasoned arguments all the damn time, and would like to stop having to repeat myself when I encounter one.

## Historical NSA Shenanigans

The sources for this, by the way, are [the declassified United States Senate Select Committee on Intelligence](https://cryptome.org/2012/05/nsa-crypto-des.pdf) and [United States Cryptologic History](https://archive.org/details/NSA-American-Cryptology-Cold-War/American%20Cryptology-Book%20III/).

### DES

No, not *that* DES.

The Data Encryption Standard (DES) was published in the Federal Register in 1975 and then standardized in 1977.

We consider it weak these days, but DES was a real game-changer for its time: It offered a standard block cipher to use for sensitive (but not classified) commercial applications. Prior to DES, the history of cryptography was largely about military uses (except a few quirky mathematicians here and there), going back before [Caesar’s cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

From declassified documents, we now know the full story, but from the time that DES was first standardized, up until recent years, there have been a concerns about [NSA’s involvement](https://en.wikipedia.org/wiki/Data_Encryption_Standard#NSA's_involvement_in_the_design).

> We sent the S-boxes off to Washington. They came back and were all different.
>
> Alan Konheim, quoted in *[Applied Cryptography](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119183471)*, p. 280

To say that academics did not trust DES would be putting it mildly: Martin Hellman (who, with Whitfield Diffie and Ralph Merkle, *invented* public-key cryptography) sent a letter in 1975 to the National Bureau of Standards that stated:

> Whit Diffie and I have become concerned that the proposed data encryption standard, while probably secure against commercial assault, may be extremely vulnerable to attack by an intelligence organization.
>
> Martin Hellman, re-published in [this paper](https://faculty.nps.edu/dedennin/publications/DES-15Years.pdf) in 1990.

At the heart of the concern about DES was something called an S-box, which simply maps an input to an output, but whose purpose is to provide a non-linear transformation to obscure the relationship between the ciphertext and the key.

The S-box used by DES was chosen by NSA. This led a lot of people to suspect there was a backdoor in the selection of the S-boxes for DES. **It turned out to be the opposite, of course**: The NSA had discovered differential cryptanalysis in secret, and had selected S-boxes that were resistant to this technique, but did not want to reveal it publicly (lest they lose their advantage over rival nations).

There’s a lot more details to this story than I want to bore anyone with, so I recommend reading up on the history of cryptography and cryptanalysis if you’re interested in such things.

In balance, [at the advice of NSA](https://www.schneier.com/blog/archives/2004/10/the_legacy_of_d.html), the final DES design did only offer 56 bits of security (down from an original key size of 128 bits). This short key ultimately allowed [the EFF to crack DES in 1998](https://w2.eff.org/Privacy/Crypto/Crypto_misc/DESCracker/) with a hardware cost of about $250,000.

![Clipboard Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-11.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

#### What does this actually tell us?

When IBM was designing DES, with feedback from NSA, the stated purpose was to use for commercial cryptographic applications in the United States.

Fact: NSA used secret cryptanalytic capabilities to ensure the resulting block cipher that became DES was *protected from the attack they knew about* without revealing said technique.

Fact: NSA recommended reducing the key length from 128 bits to 64 bits (with 8 of the key bits serving as parity bits, thus making it only have 56-bit security).

This both strengthened and weakened DES in different ways. A 56-bit key can be broken by a distributed computing effort in under 24 hours, as of 2012.

DES’s 56-bit keys are at the heart of Moxie’s MSCHAPv2 break.

This is confusing until you remember NSA has two opposing missions, with (unfortunately) military jargon names.

* COMSEC (Communications Security) — basically blue-teamers
* SIGINT (Signals Intelligence) — basically red-teamers

The COMSEC folks have a mission to secure the US government and protect US interests (read: private sector).

The SIGINT folks have a mission to spy on other nations on behalf of the US.

In theory, the SIGINT folks aren’t supposed to spy on Americans *at all*. In practice, their Five Eyes partners gives them a stupid loophole: An allied nation can simply do the spying for them, so long as federal prosecutors are willing to engage in a little bit of [parallel construction](http...
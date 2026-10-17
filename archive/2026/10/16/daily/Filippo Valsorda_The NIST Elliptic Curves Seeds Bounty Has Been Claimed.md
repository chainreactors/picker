---
title: The NIST Elliptic Curves Seeds Bounty Has Been Claimed
url: https://words.filippo.io/seeds-solved/
source: Filippo Valsorda
date: 2026-10-16
fetch_date: 2026-10-17T06:35:33.424361
---

# The NIST Elliptic Curves Seeds Bounty Has Been Claimed

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

16 Oct 2026

# The NIST Elliptic Curves Seeds Bounty Has Been Claimed

We now know how the seeds of the NIST elliptic curves were generated: they’re not the hash of some saucy sentence, but the output of [drand48](https://man.archlinux.org/man/drand48.3.en) seeded with the time, which was indeed in 1997–98.

John Wood, Henry de Valence, Ava Howell, Zack Voase, Lucy Sweet, Amir Omidi, Paul Crowley, Iain McGinniss, Nicholas Carlini, and Steve Weis from Anthropic [solved the riddle](https://www.anthropic.com/research/ecdsa-curve-origins) and on October 15th, 2026, at 01:07:51 UTC, claimed [the full bounty I announced three years ago](https://words.filippo.io/seeds-bounty/). They chose to donate the prize to [ISRG](https://isrg.org/), the non-profit that operates Let’s Encrypt, tripling its value to $36,864 (36 Ki$). Thank you to Amir Omidi, Chris Palmer, Colm MacCárthaigh, David Adrian, David Anderson, Jeff Hodges, Matt Green, Matthew McPherrin, Paul Kehrer, Ryan Sleevi, and Soatok for contributing to the bounty.

This helps fill out a page of cryptographic history, and reinforces our confidence in these critical cryptographic primitives.

The NIST elliptic curves (P-192, P-224, P-256, P-384, and P-521) were published by NIST in FIPS 186-2 in 2000. They were generated at random according to ANSI X9.62 by taking an arbitrary seed, hashing it with SHA-1, and using the output to derive some of the parameters. Until this week, we had no idea how those arbitrary seeds were picked.

The lore was that Dr. Jerry Solinas, who passed away in early 2023, generated them in 1997 by hashing some English sentences that he later forgot. You can read more in [this article by Steve Weis](https://saweis.net/posts/nist-curve-seed-origins.html) or in [the original bounty announcement](https://words.filippo.io/seeds-bounty/).

Turns out memory can play tricks on everyone: we now know they were instead generated with the POSIX-standard [drand48](https://man.archlinux.org/man/drand48.3.en) random number generator.

The algorithm is as simple as passing the then-current UNIX timestamp to `srand48()` and then producing one byte at a time with drand48. Each sequence of 20 bytes is tried as a seed following ANSI X9.62 and rejected if the resulting curve is not valid. Some timestamps are used to generate multiple curves, by continuing to try seeds after accepting the first one. I [reimplemented the algorithm in Go](https://github.com/FiloSottile/mostly-harmless/blob/main/seeds/seeds.go) to verify the claim. Read more in [Anthropic’s writeup](https://www.anthropic.com/research/ecdsa-curve-origins).

There are two additional undocumented criteria beyond the ANSI X9.62 ones, one fairly clear and one that still escapes us.

If the bit length of the order *n* of the resulting curve is more than the bit length of the base field *p* of the curve, the seed is rejected. (The condition is not the stricter *n* < *p*, because prime239v2 has *p* < *n* < 2²³⁹.)

This leaves us with roughly twice as many valid seeds as were published. We explored a number of explanations for this last bit, and found no good fit. Maybe the same RNG was used to validate seeds, consuming RNG output and skipping some potential candidates, although the “gaps” are not regular. Maybe there was just a bug in one of the algorithms that returned the wrong result half the time; these calculations, which we can now do with off-the-shelf software in minutes, were still very much state-of-the-art in 1997.

```
srand48(863711343) [1997-05-15 15:49:03 +0000 UTC]:
  accepted   36th seed 25e5[...]: not published
  accepted 1562nd seed d09b[...]: not published
  accepted 2185th seed e43b[...]: prime239v1
  accepted 2320th seed e8b4[...]: prime239v2
  accepted 2491st seed 1256[...]: not published
  accepted 2682nd seed d2c1[...]: not published
  accepted 2863rd seed 3a70[...]: not published
  accepted 3048th seed 7d73[...]: prime239v3
srand48(863966734) [1997-05-18 14:45:34 +0000 UTC]:
  accepted  139th seed 3045[...]: P-192 a.k.a. prime192v1
  accepted 2198th seed 692d[...]: not published
  accepted 5228th seed c469[...]: prime192v3
  accepted 5405th seed 3ad1[...]: not published
  accepted 6013th seed 31a9[...]: prime192v2
srand48(871002724) [1997-08-08 01:12:04 +0000 UTC]:
  accepted 1136th seed d09e[...]: P-521
srand48(871696354) [1997-08-16 01:52:34 +0000 UTC]:
  accepted  876th seed 50c7[...]: not published
  accepted 1842nd seed c49d[...]: P-256 a.k.a. prime256v1
srand48(872952608) [1997-08-30 14:50:08 +0000 UTC]:
  accepted 2688th seed a335[...]: P-384
srand48(891607927) [1998-04-03 12:52:07 +0000 UTC]:
  accepted  777th seed d007[...]: not published
  accepted 1485th seed 18cf[...]: not published
  accepted 5736th seed 3c17[...]: not published
  accepted 7026th seed bd71[...]: P-224
```

What does this mean for the security of elliptic curve cryptography based on the NIST curves? Well, even before this discovery there were no serious concerns among practitioners. In Section 3.1 of [their 2015 paper “A riddle wrapped in an enigma,”](https://eprint.iacr.org/2015/1018) Koblitz and Menezes make a convincing argument that it’s implausible that the NSA could have selected a seed to exploit a weakness that escaped more than 15 (now 25) years of cryptanalysis.

However, as reported in a later version of that paper, Daniel Bernstein and Tanja Lange described to Koblitz and Menezes in 2017 a technique that could have exploited 70 bits of freedom in selection of the seed to target a hypothetical class of 2⁶¹ weak prime-order curves. (Bernstein is the author of a competing elliptic curve design, Curve25519.) This contributed to enduring conspiracy theories, which had significant appeal among the non-specialist public (although many have since moved on to other, adjacent, conspiracy theories). All this speculation harmed confidence in robust cryptographic systems and was part of my motivation for the bounty.

This week’s findings completely rule out the technique described by Bernstein and Lange. Even if the NSA had been free to pick any timestamp in 1997–98 and any of the first 16 prime-order candidates (which generously accounts for the unexplained rejections), they would have had barely 30 bits of freedom. Not enough to intentionally target a hypothetical small class of weak curves, not enough to embed any kind of [NOBUS](https://en.wikipedia.org/wiki/NOBUS) backdoor.

Along with [deterministic](https://www.rfc-editor.org/rfc/rfc6979) and [hedged](https://www.ietf.org/archive/id/draft-irtf-cfrg-det-sigs-with-noise-05.html) ECDSA signing algorithms, [formally verified field implementations](https://github.com/mit-plv/fiat-crypto), and [the 2015 complete addition formulas by Renes, Costello, and Batina](https://eprint.iacr.org/2015/1060), this nicely completes the “rehabilitation arc” of NIST elliptic curve cryptography, which I would now personally recommend over Curve25519/Ed25519/X25519.

Just in time for them to be retired in favor of post-quantum signatures.

P.S. The Anthropic team also figured out how the seeds of the NIST B-curves (the ones over binary fields) were generated, but no one uses those, so who cares.

## The picture

In a FamilyMart in Taiwan I found this delightful dice set. A full roll carries log₂(6²⁰) ≈ 51.7 bits of entropy. Rolling them twice can make a pretty robust cryptographic key!

I thought it would be funny to label them as Geomys FIPS 140-3 Entropy Sources (which of course they are not, though we do have one of those) and hand them out as swag. However, I found no way to order them online, so I simply visited over a dozen FamilyMarts and brought home 50 packs.

![A set of 20 small dice in the evening light. They are white with red and black etchings. A small clear plastic box is next to them.](https://assets.buttondown.email/images/fc811646-65b3-4c41-9a2c-ff68584f75b5.jpeg?w=960&...
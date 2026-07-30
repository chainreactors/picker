---
title: Some thoughts about Anthropic’s new cryptanalysis results
url: https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/
source: A Few Thoughts on Cryptographic Engineering
date: 2026-07-29
fetch_date: 2026-07-30T04:47:06.185836
---

# Some thoughts about Anthropic’s new cryptanalysis results

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# Some thoughts about Anthropic’s new cryptanalysis results

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/)
in [academics](https://blog.cryptographyengineering.com/category/academics/), [AI](https://blog.cryptographyengineering.com/category/ai/), [attacks](https://blog.cryptographyengineering.com/category/attacks/)
July 29, 2026July 29, 2026
2,245 Words

![](https://matthewdgreen.files.wordpress.com/2016/08/matthew-green.jpg?w=200&h=300)

# Matthew Green

I'm a cryptographer and professor at Johns Hopkins University. I've designed and analyzed cryptographic systems used in wireless networks, payment systems and digital content protection platforms. In my research I look at the various ways cryptography can be used to promote user privacy.

[My academic website](https://matthewgreen.io)
[BlueSky](https://bsky.app/profile/did%3Aplc%3Axvgztewzbfh7bpnklayrsvds)
[Mastodon](https://ioc.exchange/%40matthew_d_green)
[Twitter](https://twitter.com/matthew_d_green)
[Top Posts](https://blog.cryptographyengineering.com/top-posts/)
[Useful crypto resources](https://staging.cryptographyengineering.com/useful-cryptography-resources/)
[Bitcoin tipjar](https://blog.cryptographyengineering.com/p/bitcoin-tipjar.html)
[Cryptopals challenges](http://cryptopals.com/)
[Applied Cryptography Research: A Board](https://acrab.isi.jhu.edu/)

[Journal of Cryptographic Engineering
(not related to this blog)](http://www.springer.com/computer/security%2Band%2Bcryptology/journal/13389)

Search for:

# Top Posts & Pages

* [Some thoughts about Anthropic's new cryptanalysis results](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/)
* [Let's talk about encrypted reasoning](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/)
* [Summary of the HAWK attack](https://blog.cryptographyengineering.com/summary-of-the-hawk-attack/)
* [The future of Siri, or: why private inference isn’t private enough](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)
* [Is Telegram really an encrypted messaging app?](https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/)
* [About Me](https://blog.cryptographyengineering.com/about-me/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [All Posts](https://blog.cryptographyengineering.com/all-posts/)
* [Useful Cryptography Resources](https://blog.cryptographyengineering.com/useful-cryptography-resources/)

*Banner image by Matt Blaze*

# Archives

Archives

Select Month
 July 2026  (1)
 June 2026  (1)
 May 2026  (1)
 April 2026  (1)
 March 2026  (1)
 February 2026  (1)
 September 2025  (1)
 June 2025  (1)
 March 2025  (1)
 February 2025  (5)
 January 2025  (1)
 August 2024  (1)
 April 2024  (1)
 January 2024  (1)
 November 2023  (1)
 October 2023  (1)
 August 2023  (1)
 May 2023  (2)
 April 2023  (1)
 March 2023  (1)
 December 2022  (1)
 October 2022  (1)
 June 2022  (1)
 January 2022  (1)
 August 2021  (1)
 July 2021  (1)
 March 2021  (1)
 November 2020  (1)
 August 2020  (1)
 July 2020  (1)
 April 2020  (1)
 March 2020  (1)
 January 2020  (1)
 December 2019  (1)
 October 2019  (1)
 September 2019  (1)
 June 2019  (1)
 February 2019  (1)
 December 2018  (1)
 October 2018  (1)
 September 2018  (1)
 July 2018  (2)
 May 2018  (1)
 April 2018  (3)
 February 2018  (1)
 January 2018  (2)
 December 2017  (1)
 November 2017  (1)
 October 2017  (2)
 September 2017  (1)
 July 2017  (1)
 March 2017  (1)
 February 2017  (1)
 January 2017  (1)
 November 2016  (1)
 August 2016  (2)
 July 2016  (1)
 June 2016  (1)
 March 2016  (2)
 December 2015  (1)
 November 2015  (1)
 October 2015  (1)
 September 2015  (1)
 August 2015  (1)
 July 2015  (1)
 May 2015  (1)
 April 2015  (2)
 March 2015  (1)
 February 2015  (3)
 January 2015  (1)
 December 2014  (1)
 November 2014  (1)
 October 2014  (3)
 September 2014  (1)
 August 2014  (1)
 July 2014  (1)
 April 2014  (2)
 March 2014  (1)
 February 2014  (1)
 January 2014  (1)
 December 2013  (4)
 October 2013  (1)
 September 2013  (4)
 August 2013  (1)
 July 2013  (1)
 June 2013  (2)
 May 2013  (1)
 April 2013  (2)
 March 2013  (2)
 February 2013  (3)
 January 2013  (2)
 December 2012  (1)
 November 2012  (1)
 October 2012  (4)
 September 2012  (3)
 August 2012  (4)
 July 2012  (2)
 June 2012  (3)
 May 2012  (5)
 April 2012  (6)
 March 2012  (4)
 February 2012  (7)
 January 2012  (8)
 December 2011  (11)
 November 2011  (13)
 October 2011  (7)
 September 2011  (8)

Yesterday Anthropic published two new [cryptanalysis](https://www-cdn.anthropic.com/e8d50c167ad47beeb03d6109a4a484be95cb38ea/hawk_key_recovery.pdf) [results](https://www-cdn.anthropic.com/c88771e1bf5ee8885349eed05e5484c0e5f7e02b/aes_mobius_bridge.pdf), both outputs of Claude Mythos, their (still) unreleased advanced model. The first of these results attacks a signature scheme called HAWK, while the second is an improved attack against reduced-round AES. Anthropic also [released a blog post](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) describing the research process that produced these results. A few people online have asked me what this all means. While I’m not sure I have all the answers, I figured it wouldn’t hurt to write a bit about my current understanding. These are *only my thoughts* and other folks will probably differ (including domain experts in the two areas at issue) so take them for what they are.

The two new results cover two very different areas, and are overall just very different in quality. Before we get to broad statements about the world, and whether you should sell all your cryptocurrency, let’s take a minute to talk about the substance.

**Hawk.** The first is a new key recovery algorithm against the non-standard signature scheme [HAWK](https://hawk-sign.info/). HAWK is a proposed post-quantum-safe signature scheme that’s based on the module Lattice Isomorphism Problem (module-LIP). For a brief Claude-written summary of the result itself, [see here](https://blog.cryptographyengineering.com/summary-of-the-hawk-attack/). There are five things you need to know about this result:

1. HAWK is not a deployed or standards-adopted algorithm, it’s a *proposed algorithm*. It is related to the [Falcon signature scheme](https://falcon-sign.info/), which is being standardized, but the attack does not transfer to that setting (which is based on a different hard problem.)
2. However, HAWK was somewhat far along in the process of being evaluated for a future standard.
3. The attack does not break “real deployed” HAWK in the sci-fi sense. The resulting attack is still exponential time, but roughly halves the number of “bits” of security in the algorithm. That means it could theoretically be fixed by doubling key sizes. The downside is that this makes the scheme less efficient, and, since HAWK is entirely motivated by being more efficient than alternatives, that makes the existence of the scheme much harder to justify.
4. The attack produced real code that runs in a few hours of wall-clock time *against a weakened “challenge instance” of HAWK that the authors provided for this purpose*. While this instance doesn’t use the parameters that were proposed for real deployment, it does demonstrate the cryptanalytic weakness well enough.
5. What’s particularly concerning (and so especially ripe for AI) is that the attack does not invent fundamentally new mathematics. It simply extends a bunch of tools that were lying around and well-known...
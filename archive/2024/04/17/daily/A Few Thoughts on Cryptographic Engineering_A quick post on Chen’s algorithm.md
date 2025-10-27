---
title: A quick post on Chen’s algorithm
url: https://blog.cryptographyengineering.com/2024/04/16/a-quick-post-on-chens-algorithm/
source: A Few Thoughts on Cryptographic Engineering
date: 2024-04-17
fetch_date: 2025-10-04T12:14:37.713191
---

# A quick post on Chen’s algorithm

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# A quick post on Chen’s algorithm

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/ "Posts by Matthew Green")
in [academics](https://blog.cryptographyengineering.com/category/academics/), [attacks](https://blog.cryptographyengineering.com/category/attacks/), [pqc](https://blog.cryptographyengineering.com/category/pqc/), [quantum](https://blog.cryptographyengineering.com/category/quantum/)
April 16, 2024April 19, 2024
807 Words

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

* [Kerberoasting](https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/)
* [Is Telegram really an encrypted messaging app?](https://blog.cryptographyengineering.com/2024/08/25/telegram-is-not-really-an-encrypted-messaging-app/)
* [A few thoughts on CSRankings.org](https://blog.cryptographyengineering.com/2017/11/08/a-few-thoughts-on-csrankings-org/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [Attack of the week: RC4 is kind of broken in TLS](https://blog.cryptographyengineering.com/2013/03/12/attack-of-week-rc4-is-kind-of-broken-in/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)
* [Let's talk about AI and end-to-end encryption](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)
* [Let's talk about PAKE](https://blog.cryptographyengineering.com/2018/10/19/lets-talk-about-pake/)
* [Attack of the week: 64-bit ciphers in TLS](https://blog.cryptographyengineering.com/2016/08/24/attack-of-week-64-bit-ciphers-in-tls/)
* [How to prove false statements? (Part 1)](https://blog.cryptographyengineering.com/2025/02/04/how-to-prove-false-statements-part-1/)

*Banner image by Matt Blaze*

# Archives

Archives

Select Month
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

**Update** **(April 19):** *Yilei Chen [announced the discovery of a bug](http://www.chenyilei.net/) in the algorithm, which he does not know how to fix. This was independently discovered by Hongxun Wu and Thomas Vidick. At present, the paper does not provide a polynomial-time algorithm for solving LWE.*

If you’re a normal person — that is, a person who doesn’t obsessively follow the latest cryptography news — you probably missed last week’s cryptography bombshell. That news comes in the form of a new e-print authored by Yilei Chen, “[Quantum Algorithms for Lattice Problems](https://eprint.iacr.org/2024/555)“, which has roiled the cryptography research community. The result is now being evaluated by experts in lattices and quantum algorithm design (*and to be clear, I am not one!*) but if it holds up, it’s going to be quite a bad day/week/month/year for the applied cryptography community.

Rather than elaborate at length, here’s quick set of five bullet-points giving the background.

(1) Cryptographers like to build modern public-key encryption schemes on top of mathematical problems that are believed to be “hard”. In practice, we need problems with a specific structure: we can construct *efficient* solutions for those who hold a secret key, or “trapdoor”, and yet also admit *no efficient solution* for folks who don’t. While many problems have been considered (and often discarded), most schemes we use today are based on three problems: [factoring](https://en.wikipedia.org/wiki/Integer_factorization) (the RSA cryptosystem), [discrete logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm) (Diffie-Hellman, DSA) and [elliptic curve discrete logarithm problem](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) (EC-Diffie-Hellman, ECDSA etc.)

(2) While we would like to believe our favorite problems are fundamentally “hard”, we know this isn’t really true. Researchers [have devised algorithms](https://en.wikipedia.org/wiki/Shor%27s_algorithm) that solve all of these problems quite efficiently (i.e., in polynomial time) — provided someone figures out how to build a quantum computer powerful enough to run the attack algorithms. *Fortunately such a computer has not yet been built!*

(3) Even though quantum computers are not yet powerful enough to break our public-key crypto, the mere threat of *future* quantum attacks has inspired industry, government and academia to join forces [Fellowship-of-the-Ring-style](https://csrc.nist.gov/projects/post-quantum-cryptography) in order to tackle the problem right now. This isn’t merely about future-proofing our systems: even if quantum computers take decades to build, future quantum computers could break encrypted messages we send *today*!

(4) One conspicuous outcome of this fellowship is [NIST’s Post-Quantum Cryptography (PQC) competition](https://www.nist.gov/news-events/news/2022/07/nist-announces-first-four-quantum-resistant-cryptographic-algorithms): this was an open competition designed to s...
---
title: How to prove false statements? (Part 1)
url: https://blog.cryptographyengineering.com/2025/02/04/how-to-prove-false-statements-part-1/
source: A Few Thoughts on Cryptographic Engineering
date: 2025-02-05
fetch_date: 2025-10-06T20:34:09.731459
---

# How to prove false statements? (Part 1)

[Skip to content](#content)

[Home](https://blog.cryptographyengineering.com/ "Home")
[Menu](#slide-menu)

# How to prove false statements? (Part 1)

[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/ "Posts by Matthew Green")
in [fundamentals](https://blog.cryptographyengineering.com/category/fundamentals/)
February 4, 2025February 6, 2025
3,846 Words

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
* [Let's talk about AI and end-to-end encryption](https://blog.cryptographyengineering.com/2025/01/17/lets-talk-about-ai-and-end-to-end-encryption/)
* [Zero Knowledge Proofs: An illustrated primer](https://blog.cryptographyengineering.com/2014/11/27/zero-knowledge-proofs-illustrated-primer/)
* [How to choose an Authenticated Encryption mode](https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/)
* [What is the Random Oracle Model and why should you care? (Part 1)](https://blog.cryptographyengineering.com/2011/09/29/what-is-random-oracle-model-and-why-3/)
* [Let's talk about PAKE](https://blog.cryptographyengineering.com/2018/10/19/lets-talk-about-pake/)
* [Dear Apple: add "Disappearing Messages" to iMessage right now](https://blog.cryptographyengineering.com/2025/03/01/dear-apple-add-disappearing-messages-to-imessage-right-now/)
* [Attack of the week: RC4 is kind of broken in TLS](https://blog.cryptographyengineering.com/2013/03/12/attack-of-week-rc4-is-kind-of-broken-in/)
* [EUF-CMA and SUF-CMA](https://blog.cryptographyengineering.com/euf-cma-and-suf-cma/)

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

*Trigger warning: incredibly wonky theoretical cryptography post (written by a non-theorist)!* *Also, this will be in two parts. I plan to be back with some more thoughts on practical stuff, like cloud backup, in the near future.*

If you’ve read my blog over the years, you should understand that I have basically two obsessions. One is my interest in building “practical” schemes that solve real problems that come up in the real world. The other is a weird fixation on the theoretical models that underpin (the security of) many of those same schemes. In particular, one of my favorite bugaboos is a particular model, or “heuristic”, called the [random oracle model](https://blog.cryptographyengineering.com/2011/09/29/what-is-random-oracle-model-and-why-3/) (ROM) — essentially a fancy way to think about [hash functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function).

Along those lines, my interest was recently piqued by a new theoretical result by Khovratovich, Rothblum and Soukhanov entitled “[How to Prove False Statements: Practical Attacks on Fiat-Shamir](https://eprint.iacr.org/2025/118).” This is a doozy of a paper! It touches nearly every sensitive part of my brain: it urges us towards a better understanding of our theoretical models for proving security of protocols. It includes the words “*practical*” and “*attacks*” in the title! And *most importantly* it demonstrates a real (albeit wildly contrived) attack on the kinds of “ZK” (note: not actually ZK, more on that later) “proving systems” that we are now using inside of real systems like blockchains.

I confess I am still struggling hard to figure out how I “feel” about this result. I understand how odd it seems that my feelings should even matter: this is *science* after all. *Shouldn’t the math speak for itself?* The worrying thing is that, in this case, I don’t think it does. In fact, this is what I find most fundamentally exciting about the result: *it really does matter how we think about it*. (Here I should add that we don’t all think the same say. My theory-focused PhD student [Aditya Hegde](https://adishegde.github.io/) has been vigorously debating me on my interpretation — and mostly winning on points. So anything non-stupid I say here is probably due to him.)

Oh yes, and I should also mention that there are [billions and billions of dollars riding on these questions](https://defillama.com/chains/Rollup)? I’m not being dramatic. This is really true.

I mentioned that this post is going to be long and wonky, that’s just unavoidable. But I promise it will be *fun*. (Ok, I can’t even promise that.) Screw it, let’s go.

### The shortest background ever (and it will still be really long)

If you’ve read this blog over the long term, you know that I’m obsessed with one particular “trick” we use in proving our schemes secure. This trick is known as the [random oracle model](https://blog.cryptographyengineering.com/2011/09/29/what-is-random-oracle-model-and-why-3/), and it’s one of the worst (or best) things to happen to cryptography.

Let me try to break this down as quickly as I can. In cryptography we have a tendency to use an ingredient called a *[cryptogra...
---
title: No, The Chinese Have Not Broken Modern Encryption Systems with a Quantum Computer
url: https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html
source: Schneier on Security
date: 2024-10-23
fetch_date: 2025-10-06T18:53:34.690675
---

# No, The Chinese Have Not Broken Modern Encryption Systems with a Quantum Computer

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

## No, the Chinese Have Not Broken Modern Encryption Systems with a Quantum Computer

The headline is pretty scary: “[China’s Quantum Computer Scientists Crack Military-Grade Encryption](https://www.newsweek.com/china-news-quantum-computer-scientists-crack-military-grade-encryption-1970760).”

No, it’s not true.

[This debunking](https://www.forbes.com/sites/craigsmith/2024/10/16/department-of-anti-hype-no-china-hasnt-broken-military-encryption-with-quantum-computers/) saved me the trouble of writing one. It all seems to have come from [this news article](https://www.scmp.com/news/china/science/article/3282051/chinese-scientists-hack-military-grade-encryption-quantum-computer-paper), which wasn’t bad but was taken wildly out of proportion.

Cryptography is safe, and [will be](https://www.schneier.com/blog/archives/2022/08/nists-post-quantum-cryptography-standards.html) for a [long time](https://www.schneier.com/essays/archives/2018/09/cryptography_after_t.html)

EDITED TO ADD (11/3): Really good [explainer](https://arstechnica.com/information-technology/2024/10/the-sad-bizarre-tale-of-hype-fueling-fears-that-modern-cryptography-is-dead/) from Dan Goodin.

Tags: [China](https://www.schneier.com/tag/china/), [encryption](https://www.schneier.com/tag/encryption/), [quantum computing](https://www.schneier.com/tag/quantum-computing/)

[Posted on October 22, 2024 at 7:03 AM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html) •
[11 Comments](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html#comments)

### Comments

LXE •
[October 22, 2024 8:02 AM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html/#comment-441259)

“computational difficulty of factoring large prime numbers”

Aaaaaaaaaah et tu Forbes!

Who? •
[October 22, 2024 9:48 AM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html/#comment-441262)

My background in theoretical physics (named “fundamental physics” at my University) makes it clear to me that, even if sending information a few microseconds to the past is possible following the rules of the quantum mechanics, turning into a possibility starting the next iteration of an algorithm before the previous one ends, each iteration consumes a certain amount of energy.

Even if quantum computers are able to run computations that would require thousands of years on a classical counterpart, the amount of energy required to fullfill this process will be prohibitively high.

I know, some people on this forum has talked about the possibility of running those quantum computers connected to their own nuclear power plants (something I do not doubt is a possibility for an intelligence agency), but even in this case we need to provide that huge amount of energy required to complete the decryption process on a short time period. No, it is not feasible with our current technology and, even if it were, breaking a single cryptographic secret will be incredibly expensive so, at best, we can expect highly targeted attacks using these quantum computers.

I agree with Bruce, we are far away of achieving this goal and, even in this case, we are doing research on quantum-resistant encryption algorithms right now. As this technology evolves, we will see how these quantum-resistant counterparts survive but right now it seems we have an answer to a problem that does not exist yet.

SevenKeys •
[October 22, 2024 10:21 AM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html/#comment-441263)

Unless they deliberately “leaked” this information to lull us into a false sense of security, that our RSA/AES are a long way from being broken.

Daniel Popescu •
[October 22, 2024 11:35 AM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html/#comment-441264)

Loved the 2018 essay, thanks!

iAPX •
[October 22, 2024 3:14 PM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html/#comment-441267)

From the debunking article:

> While factoring a 50-bit integer is an impressive technical achievement..

The worst case is 16 million division (24-bit) to factor a 50-bit integer (yes after 2 you don’t try any even number), and that its something that takes around a millisecond for mass-marketed modern 64-bit CPUs accounting for multicore and vector units.

Clive Robinson •
[October 23, 2024 4:22 AM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html/#comment-441273)

@ SevenKeys,

> “Unless they deliberately “leaked” this information to lull us into a false sense of security, that our RSA/AES are a long way from being broken.”

You are only thinking of time going in one direction, with information that has no mass or energy thus no forensic footprint it’s different.

Think of a digitally signed contract for like a land lease etc. That is a contract that could be valid for a thousand or more years (there is one in Ireland for longer with a well known brewery). Traditionally such contracts are protected by being registered and copies kept with an impartial agent (such as a Gov Land Registry). However impartial agents cost significant money to run and have all sorts of issues with “historic document preservation”. Modern neo-con arguments are that this is inefficient and should be replaced with something less expensive (even if one heck of a lot less secure).

As long as the “secret key” remains secret the contract should be not just “unalterable” but “verifiable” as well.

Now imagine that you can find the secret key from the public key in less than fifty years. This in effect puts an “end of life” on all contracts at between seven to fifty years.

After that you can nolonger trust the digital signed contract as being original thus accurate…

Traditional paper or velum contracts at least have forensics that can assist in authenticating their age and provenance, digital information does not.

It’s an argument “Blockchain” people like, but when you consider the power consumption of a blockchain then the cost can be a lot higher than expected and not even realistically secure either. Because what ails PubKey systems with QC also has an effect on anything else based on “One Way Functions”(OWFs).

Clive Robinson •
[October 23, 2024 8:06 AM](https://www.schneier.com/blog/archives/2024/10/no-the-chinese-have-not-broken-modern-encryption-systems-with-a-quantum-computer.html/#comment-441276)

@ LXE,

Re : F...
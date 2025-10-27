---
title: Side-Channel Attack against CRYSTALS-Kyber
url: https://www.schneier.com/blog/archives/2023/02/side-channel-attack-against-crystals-kyber.html
source: Schneier on Security
date: 2023-03-01
fetch_date: 2025-10-04T08:22:32.291592
---

# Side-Channel Attack against CRYSTALS-Kyber

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

## Side-Channel Attack against CRYSTALS-Kyber

[CRYSTALS-Kyber](https://pq-crystals.org/kyber/) is one of the public-key algorithms currently [recommended](https://csrc.nist.gov/News/2022/pqc-candidates-to-be-standardized-and-round-4) by NIST as part of its post-quantum cryptography [standardization process](https://csrc.nist.gov/projects/post-quantum-cryptography).

Researchers have [just published](https://eprint.iacr.org/2022/1713.pdf) a side-channel attack—using power consumption—against an implementation of the algorithm that was supposed to be resistant against that sort of attack.

The algorithm is not “broken” or “cracked”—despite [headlines](https://www-securityweek-com.cdn.ampproject.org/c/s/www.securityweek.com/ai-helps-crack-a-nist-recommended-post-quantum-encryption-algorithm/amp/) to the contrary—this is just a side-channel attack. What makes this work really interesting is that the researchers used a machine-learning model to train the system to exploit the side channel.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cryptography](https://www.schneier.com/tag/cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [machine learning](https://www.schneier.com/tag/machine-learning/), [quantum computing](https://www.schneier.com/tag/quantum-computing/), [quantum cryptography](https://www.schneier.com/tag/quantum-cryptography/), [side-channel attacks](https://www.schneier.com/tag/side-channel-attacks/)

[Posted on February 28, 2023 at 7:19 AM](https://www.schneier.com/blog/archives/2023/02/side-channel-attack-against-crystals-kyber.html) •
[8 Comments](https://www.schneier.com/blog/archives/2023/02/side-channel-attack-against-crystals-kyber.html#comments)

### Comments

Clive Robinson •
[February 28, 2023 11:08 AM](https://www.schneier.com/blog/archives/2023/02/side-channel-attack-against-crystals-kyber.html/#comment-418675)

@ Bruce, ALL,

> “The algorithm is not “broken” or “cracked”—despite headlines to the contrary—this is just a side-channel attack.”

The problem is not many understand the difference between,

1, Broken algorithm.

Or the implication of the latter.

As I’ve indicated in the past side channels appear in many ways, and they can leak many things.

What would be fair to say is that outside certain “Tripple Fence” organisations, not much research has been done.

Trying to deal with each type of side channel is not something many can do, and like “rolling your own crypto” is something where your success will be doubtful, without knowledge you may find difficult to aquire.

Thus the safe rule of thumb to mitigate side channels is not to use any crypto algorithm you need to rely on in an “On-Line” mode.

So encrypt your secrets on an “energy gapped” machine where neither side channeles or other communications can carry secret information out into the world for the third party ears of Eve and friends to pick up.

Ted •
[February 28, 2023 4:00 PM](https://www.schneier.com/blog/archives/2023/02/side-channel-attack-against-crystals-kyber.html/#comment-418680)

NIST’s Dustin Moody reports that he doesn’t see this research as being a fatal flaw for CRYSTALS-Kyber.

Although it demonstrates how a certain implementation can be broken, it doesn’t break the algorithm in general.

Moody adds that Kyber may be about twice as slow when lots of countermeasures are added to protect it from side channel attacks.

<https://www.scmagazine.com/analysis/policy/post-quantum-algorithm-attack>

Clive Robinson •
[February 28, 2023 5:46 PM](https://www.schneier.com/blog/archives/2023/02/side-channel-attack-against-crystals-kyber.html/#comment-418682)

@ Ted, ALL,

Re : Side channel protection gives slow algorithms.

> “Moody adds that Kyber may be about twice as slow when lots of countermeasures are added.”

And those measures will probably not be enough…

But before anyone goes “but but but.
..” The AES finalist suffers from this very issue quite badly as well. And the NSA darn well knew about side channel issues before they pursuaded NIST to rig the contest to not just ignore them but select for probably worat case algorithms… Which ment that the “fastness” of the AES finalist pushed out other better algorithms that did not have anywhere near as bad side channel leakage.

I’ve said for years on this blog, there is a trade off of “Security v Efficiency” in general the more efficient you make an algorithm or implementation the worse the side channel leakage will be in a practical implementation.

I’ve even said how you minimise some side channel issues.

One of those old English idioms os pertinent,

“There’s many a slip twixt the cup and lip”

As well as the more general,

“Don’t count your chickens till they’ve hatched”

That apply to information security.

The enemy of privacy and security when it comes to information has always been statistics, that lift apparent noise into being a signal.

When all is said and done about “Machine Learning”(ML), the reality is it’s in effect statistics on steroids. I’m only surprised that it’s taken so long for it to be shown as such against a “black box output”.

The flip side of this by the way, is it will enable us to get more information through a Shannon Channel, especially when time/distance precludes the use of feedback error correction.

So I expect to see some papers about ML applied to “Feedforward Error Correction”(FEC) to come out of this.

Which will actually be a better use of it from society and mankinds perspective, than cracking codes.

Clive Robinson •
[February 28, 2023 6:26 PM](https://www.schneier.com/blog/archives/2023/02/side-channel-attack-against-crystals-kyber.html/#comment-418684)

@ Bruce, ALL,

Re : NSA stich ups.

From the article @Ted points to from SC Magazine, towards the bottom you find,

> *“Their use will be mandatory for most civilian federal agencies per a White House national security memorandum, and many industries and international standards bodies rely on NIST standards when developing their own encryption policies.”*

We both know beyond reasonable doubt the NSA has previously “stiched up” the US Government not just US Civilisns and US Industry with their crypto gaming.

The classic was perhaps what Matt Blaze discovered about the “Law Enforcment Access Field”(LEAF) in the “Clipper chip” algorithm.

Basically the NSA made the LEAF too short, such that you could knowing how it worked provide a fake LEAF in realtime. Thus law enforcment or other Government Agency would be “locked out” of accessing the encrypted channel. This would benifit the NSA but no other US Gov Agency that would have to use clipper as specified with the NSA using their genuine LEAF to access the encrypted communications.

As far as I can tell every algorithm the NSA has either designed for others –not IC, Diplomatic– to use, or they have been involved with the selection process, has come up short in s...
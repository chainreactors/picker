---
title: NCSC Guidance on “Advanced Cryptography”
url: https://www.schneier.com/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html
source: Schneier on Security
date: 2025-05-03
fetch_date: 2025-10-06T22:29:38.580979
---

# NCSC Guidance on “Advanced Cryptography”

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

## NCSC Guidance on “Advanced Cryptography”

The UK’s National Cyber Security Centre just released its [white paper](https://www.ncsc.gov.uk/whitepaper/advanced-cryptography) on “Advanced Cryptography,” which it defines as “cryptographic techniques for processing encrypted data, providing enhanced functionality over and above that provided by traditional cryptography.” It includes things like homomorphic encryption, attribute-based encryption, zero-knowledge proofs, and secure multiparty computation.

It’s full of good advice. I especially appreciate this warning:

> When deciding whether to use Advanced Cryptography, start with a clear articulation of the problem, and use that to guide the development of an appropriate solution. That is, you should not start with an Advanced Cryptography technique, and then attempt to fit the functionality it provides to the problem.

And:

> In almost all cases, it is bad practice for users to design and/or implement their own cryptography; this applies to Advanced Cryptography even more than traditional cryptography because of the complexity of the algorithms. It also applies to writing your own application based on a cryptographic library that implements the Advanced Cryptography primitive operations, because subtle flaws in how they are used can lead to serious security weaknesses.

The conclusion:

> Advanced Cryptography covers a range of techniques for protecting sensitive data at rest, in transit and in use. These techniques enable novel applications with different trust relationships between the parties, as compared to traditional cryptographic methods for encryption and authentication.
>
> However, there are a number of factors to consider before deploying a solution based on Advanced Cryptography, including the relative immaturity of the techniques and their implementations, significant computational burdens and slow response times, and the risk of opening up additional cyber attack vectors.
>
> There are initiatives underway to standardise some forms of Advanced Cryptography, and the efficiency of implementations is continually improving. While many data processing problems can be solved with traditional cryptography (which will usually lead to a simpler, lower-cost and more mature solution) for those that cannot, Advanced Cryptography techniques could in the future enable innovative ways of deriving benefit from large shared datasets, without compromising individuals’ privacy.

NCSC [blog entry](https://www.ncsc.gov.uk/blog-post/advanced-cryptography-new-approaches-to-data-privacy).

Tags: [cryptography](https://www.schneier.com/tag/cryptography/), [homomorphic encryption](https://www.schneier.com/tag/homomorphic-encryption/), [reports](https://www.schneier.com/tag/reports/)

[Posted on May 2, 2025 at 7:03 AM](https://www.schneier.com/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html) •
[3 Comments](https://www.schneier.com/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html#comments)

### Comments

Clive Robinson •
[May 2, 2025 10:29 AM](https://www.schneier.com/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html/#comment-444965)

@ ALL,

The important point to understand for reading and use of this paper is that the UK “National Cyber Security Centre”(NCSC) defines Advanced Cryptography as,

> *“Cryptographic techniques for **processing encrypted data**, providing enhanced functionality over and above that provided by traditional cryptography.”*

As I’ve indicated in the past, “data” is in effect “intangible information” and as such has no physical form of matter or energy. But importantly it can be modulated or impressed on any matter or energy to form just about any type of “tangible object” advertently or inadvertently which is one of the reasons “containing or controling” to maintain confidentiality is so difficult.

Further there is actually only three basic things you can do with information,

1, Store it

Traditionally cryptography has only been used to maintain confidentiality for the first two types of operation.

And history is replete with examples of where the simplest of the three operations to do “store with confidentiality” fails.

The reason is that information as confidential data objects acquires attributes that are not immediately apparent such as Implicit-Data, Meta-Data, and consequently Meta-Meta-Data. That all in effect “leak information” that can enable or assist an adversary to strip back the confidentiality.

This issue gets significantly worse with communicating confidential data objects.

Whilst some form of information processing has always been possible on confidential information objects, it was rarely if ever done except in the form of counterfeiting information to carry out attacks against an opponent’s systems.

One such was “bit flipping” of data in known locations within a confidential information object produced by stream encryption. Which could enable forms of replay attack on systems that were not adequately “armoured” against it.

Now we are starting to be capable of “processing” with confidential information objects we have to be very mindful that all our existing armouring techniques are likely to be nolonger effective. Thus a whole new set of classes of attack has opened up, most of which we are currently oblivious to on the “unknown unknowns” principle.

One Giant Leap •
[May 2, 2025 4:22 PM](https://www.schneier.com/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html/#comment-444972)

@Bruce thanks. The problem isn’t recognizing “dont roll your own security”, its that nearly zero good methods enable avoiding encryption on the endgap, other than the likes of John Shearing’s tidy little github . com/johnshearing/PrivateKeyVault’

As you brought up in “US as a Surveillance State”, thats effectively the ONLY concern for any of us, until its addressed. All this guidance is pointless otherwise.

Thanks again. -4EHM

[Ian Brown](https://www.ianbrown.tech/about/) •
[May 5, 2025 1:55 PM](https://www.schneier.com/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html/#comment-445052)

Meanwhile, the UK government is doing its best to stop Apple and doubtless many other big tech firms’ users around the world from *using* these techniques, without inserting back doors first.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/05/ncsc-guidance-on-advanced-cryptography.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F05%2Fncsc-guidance-...
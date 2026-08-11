---
title: Python Now Has a Post-Quantum Encryption Library
url: https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html
source: Schneier on Security
date: 2026-08-10
fetch_date: 2026-08-11T03:31:50.576795
---

# Python Now Has a Post-Quantum Encryption Library

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

## Python Now Has a Post-Quantum Encryption Library

[This is good](https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/):

> Post-quantum cryptography is now one pip-install away for the entire Python ecosystem. With funding from the [Sovereign Tech Agency](https://www.sovereign.tech/), we implemented support for ML-KEM, the NIST-standard key-establishment primitive, and ML-DSA, the NIST-standard digital-signature primitive, in pyca/cryptography.

Remember, the reason to do this now is because there’s no emergency. And because you will make your systems crypto agile, which is always a good idea.

Tags: [cryptography](https://www.schneier.com/tag/cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [open source](https://www.schneier.com/tag/open-source/), [quantum computing](https://www.schneier.com/tag/quantum-computing/)

[Posted on August 10, 2026 at 7:02 AM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html) •
[9 Comments](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html#comments)

### Comments

someone •
[August 10, 2026 7:21 AM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456699)

why worry about this if aes-256 is uncrackable ?

Q •
[August 10, 2026 7:50 AM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456700)

Symmetric algorithms, like AES, are not affected by quantum algorithms (except for Grover’s algorithm, but it is too slow to be useful).

Post-quantum is for asymmetric algorithms, like RSA, and are affect by quantum algorithms. This is what post-quantum is needed for.

yet another bruce •
[August 10, 2026 9:02 AM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456702)

I had thought that another reason we are doing this now is to discourage Harvest Now, Decrypt Later (HNDL) attacks.

Between HNDL and AI data centers it is getting difficult to find an HDD at a reasonable price.

Clive Robinson •
[August 10, 2026 10:18 AM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456704)

@ someone, ALL,

With regards,

> “why worry about this if aes-256 is uncrackable ?”

Who told you that?

AES uses what at the time were a lot of new ideas, worse it has implementation issues.

The NSA knew about this but as NIST’s required Crypto Advisors they did not inform NIST.

The result was that the go faster stripes implementation used “loop unrolling” which whilst fast unfortunately was very very susceptable to Side Channel Leakage that could when put in “standard libraries –and it was– leak info loud and clear to the network easy enough to pick up several steps into the Internet, if not clear across it.

Now you may not know that the favourite hunting ground of the NSA and other similar level Nationsl SigInt Agencies is just inside the “cloud” on the other side of an “upstream router” where you as a leaf node can not see their presence but they can see not only all your traffic but very very precise timing that enabled that implimentation Side Channel leakage to “Sing Out”.

There are a number of people who strongly believe from what they saw that the NSA rigged the AES competition so that exactly this issue would arise.

More people have since come over to that view with the likes of the Dual Eliptic Curve Digital Random Bit generator”(Dual\_EC\_DRBG). The NSA well and truley stiched NIST up and then got caught out and thus truely embarrassed NIST who had to withdraw a FIPS document that are normally considered “Gold Standard” as far as International Standards are concerned.

Long prior to that I’d posted to this blog what I would be attacking if I was a Sigint Agency.

1, User File Standards
2, Protocol Standards
3, Implementation Standards

If as Microsoft does you dump between 4 and 16 Kbits of near static data at the front of a file then it makes “known plaintext” attacks oh so much easier.

If you cause “side channels” in protocol standards they almost always leak data that either assists or enables in leaking key or plaintext info.

Tamper with implementation standards and that becomes oh so much easier.

The NSA has been repeatedly caught out in various ways and it’s known that Microsoft has almost always gone along with it.

Now I don’t expect you to believe me, what I expect is for you to “go looking” to try to say “it isn’t so” which is where your education in this aspect of the NSA and other SigInt agencies will begin.

However a warning, you will find this subject is one of the deepest rabbit holes an average person can find themselves falling into.

KC •
[August 10, 2026 11:05 AM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456705)

@someone

From an [earlier post](https://blog.trailofbits.com/2024/07/01/quantum-is-unimportant-to-post-quantum/) it’s said the PQC standards are a step being taken with 40 years of lessons. Where current algorithms are subject to many subtle implementation errors, the newer designs make ‘footguns’ (aka shooting oneself in the foot) less easy.

Looks like pyca/cryptography is the eleventh ([now 10th?](https://pypistats.org/top)) most-downloaded package on PyPI.

[mark](https://mrw.5-cent.us) •
[August 10, 2026 12:55 PM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456707)

Ok, Bruce: who is Sovereign Tech, and who owns them?

Winter •
[August 10, 2026 1:37 PM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456709)

@mark

> who is Sovereign Tech, and who owns them?

Search engines are so useful:

<https://www.sovereign.tech/>

<https://en.wikipedia.org/wiki/Sovereign_Tech_Agency>

That is, a German Federal Agency

lurker •
[August 10, 2026 2:29 PM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456711)

@yet another bruce
“it is getting difficult to find an HDD at a reasonable price”

Amen, brother. But that might be part of the plan: If you can’t keep your stuff in your own briefcase, they want you to put it up on the Cloud, where …

wild eyes dying •
[August 10, 2026 8:11 PM](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html/#comment-456719)

When I was young
I used to dream
And the wind blows
And the owl sings
And dogs are driven wild
And dogs break their chains
And run through the lands
A prey to madness
With wild eyes dying
With wild eyes burning
They raise their heads
They swell their cold necks
Like a cat that’s ripped its guts
Like a hungr...
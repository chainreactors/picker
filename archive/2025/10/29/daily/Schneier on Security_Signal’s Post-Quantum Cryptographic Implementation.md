---
title: Signal’s Post-Quantum Cryptographic Implementation
url: https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html
source: Schneier on Security
date: 2025-10-29
fetch_date: 2025-10-30T03:13:00.860070
---

# Signal’s Post-Quantum Cryptographic Implementation

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

## Signal’s Post-Quantum Cryptographic Implementation

Signal has [just rolled out](https://signal.org/blog/spqr/) its quantum-safe cryptographic implementation.

*Ars Technica* has a [really good article](https://arstechnica.com/security/2025/10/why-signals-post-quantum-makeover-is-an-amazing-engineering-achievement/) with details:

> Ultimately, the architects settled on a creative solution. Rather than bolt KEM onto the existing double ratchet, they allowed it to remain more or less the same as it had been. Then they used the new quantum-safe ratchet to implement a parallel secure messaging system.
>
> Now, when the protocol encrypts a message, it sources encryption keys from both the classic Double Ratchet and the new ratchet. It then mixes the two keys together (using a cryptographic key derivation function) to get a new encryption key that has all of the security of the classical Double Ratchet but now has quantum security, too.
>
> The Signal engineers have given this third ratchet the formal name: Sparse Post Quantum Ratchet, or SPQR for short. The third ratchet was designed in collaboration with [PQShield](https://pqshield.com), [AIST](https://www.aist.go.jp/index_en.html), and New York University. The developers [presented](https://eprint.iacr.org/2025/078) the erasure-code-based chunking and the high-level Triple Ratchet design at the Eurocrypt 2025 conference. At the Usenix 25 conference, they [discussed](https://www.usenix.org/system/files/usenixsecurity25-auerbach.pdf) the six options they considered for adding quantum-safe forward secrecy and post-compromise security and why SPQR and one other stood out. Presentations at the [NIST PQC Standardization Conference](https://csrc.nist.gov/Presentations/2025/post-quantum-ratcheting-for-signal) and the [Cryptographic Applications Workshop](https://youtu.be/WhTLjKzkK9c) explain the details of chunking, the design challenges, and how the protocol had to be adapted to use the standardized ML-KEM.
>
> Jacomme further observed:
>
> > The final thing interesting for the triple ratchet is that it nicely combines the best of both worlds. Between two users, you have a classical DH-based ratchet going on one side, and fully independently, a KEM-based ratchet is going on. Then, whenever you need to encrypt something, you get a key from both, and mix it up to get the actual encryption key. So, even if one ratchet is fully broken, be it because there is now a quantum computer, or because somebody manages to break either elliptic curves or ML-KEM, or because the implementation of one is flawed, or…, the Signal message will still be protected by the second ratchet. In a sense, this update can be seen, of course simplifying, as doubling the security of the ratchet part of Signal, and is a cool thing even for people that don’t care about quantum computers.

Also read [this post](https://x.com/ianonymous3000/status/1976499827325202587?s=46) on X.

Tags: [cryptography](https://www.schneier.com/tag/cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [quantum computing](https://www.schneier.com/tag/quantum-computing/), [Signal](https://www.schneier.com/tag/signal/)

[Posted on October 29, 2025 at 7:09 AM](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html#comments)

### Comments

Rontea •
[October 29, 2025 9:06 AM](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html/#comment-449417)

The X link returns “rate limited”

kiwano •
[October 29, 2025 9:12 AM](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html/#comment-449418)

Am I the only one wondering if the choice of name “Sparse Post Quantum Ratchet” was influenced by ancient Rome?

finagle •
[October 29, 2025 10:01 AM](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html/#comment-449420)

Excellent.

finagle •
[October 29, 2025 10:03 AM](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html/#comment-449421)

@kiwano

Nope.

Let’s hope Signal don’t need to fear a modern day Hannibal.

HM •
[October 29, 2025 11:13 AM](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html/#comment-449423)

Just fyi, the twitter post appears to be largely written via an LLM. 🙁

Clive Robinson •
[October 29, 2025 11:29 AM](https://www.schneier.com/blog/archives/2025/10/signals-post-quantum-cryptographic-implementation.html/#comment-449424)

@ finagle, ALL,

With regards,

> “All of which worry me far more than the possibility of quantum computers being used in the (far?) future.”

That’s a mistake everyone makes…

The thing is the reason for Post Quantum Crypto is a problem of how to establish a “root of trust” from which you can then do “key generation”.

The root of trust has to be a secret between the two communicating parties. Thus the exchange of the secret prior to the 1970’s had to be “by hand” or some other “secure communications channel” which in the likes of OnLine Commerce did not exist so would have to be established. Hence the names used for such are,

1, Key Transfer Procedure
2, Key Establishment Protocols
3, Key Agreement Protocol

The first covers the older “by hand” systems as well as the newer mathematical systems and is part of the more general “Key Managment”(KeyMan) system. These usually require a secure “covert channel”.

The second covers the mathematical systems that don’t require even a secure channel. They are based on the notion that not only do “One Way Functions”(OWF) exist that also OWF’s with a “Back Door Function” exist.

The last is more about what happens after the initial root of trust is established and covers things like “ratchet functions”.

The problem you need to worry about more than Quantum Computers is the “assumption” that OWF’s exist…

There is of yet no “proof” in the mathematical sense that they do. Just the reassurance that despite many looking, no algorithm has yet been publicly demonstrated.

But if the assumption is invalid then you will not have to hang onto the “never never” idea that workable Quantum Computers will be developed in any of our life times, because existing computers will probably work just fine.

This then causes another question to arise which is what “Post Quantum Cryptography”(PQC) is all about.

Can there be the equivalent of a OWF in a way that is secure against Quantum Computing?

Again there is no proof that there is. In fact at least one serious attempt in the NIST Competition has failed already…

But the mathematicians, logicians and engineers are looking

And a couple of recent publications suggest that the OWF Assumption...
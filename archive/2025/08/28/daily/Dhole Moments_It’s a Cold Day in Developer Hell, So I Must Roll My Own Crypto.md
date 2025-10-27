---
title: It’s a Cold Day in Developer Hell, So I Must Roll My Own Crypto
url: https://soatok.blog/2025/08/27/its-a-cold-day-in-developer-hell-so-i-must-roll-my-own-crypto/
source: Dhole Moments
date: 2025-08-28
fetch_date: 2025-10-07T00:48:26.031888
---

# It’s a Cold Day in Developer Hell, So I Must Roll My Own Crypto

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

[Meta-blog](https://soatok.blog/category/meta/) [Open Source](https://soatok.blog/category/technology/open-source/)

# It’s a Cold Day in Developer Hell, So I Must Roll My Own Crypto

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [August 27, 2025](https://soatok.blog/2025/08/27/its-a-cold-day-in-developer-hell-so-i-must-roll-my-own-crypto/)

![It’s a Cold Day in Developer Hell, So I Must Roll My Own Crypto](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/08/BlogHeader-2025-ProjectUpdates.png?fit=1200%2C675&ssl=1)

I have several projects in-flight, and I wanted to write a quick status update for them so that folks can find it easier to follow along.

> Please bear in mind: This is in addition to, and totally separate from, my full-time employment.

## Hell Frozen Over

A while ago, annoyed by the single point of failure in digital signature algorithms, I decided to [build a tool](https://soatok.blog/2025/08/09/improving-geographical-resilience-for-distributed-open-source-teams-with-freeon/) to help developer teams use threshold cryptography.

The idea was: Wrap an existing implementation of [FROST (RFC 9591)](https://www.rfc-editor.org/rfc/rfc9591.html) with a command line tool (and provide a corresponding HTTP Server to fulfill the coordinator role). Then you can give it to DevSecOps folks and say, “Now you need 3 out of 5 keys to be turned in order for a valid Ed25519 signature to be emitted.”

Unfortunately, while writing integration tests for the tool, I ran into concurrency issues: The keygen ceremony worked fine, but signing would either never start or would get into an invalid state for arcane reasons.

After wrestling with this for 40 or so hours (with very little sleep), and being ignored by the maintainers of the FROST library I was building upon, I decided that this was a stupid problem to have.

So I decided to [roll my own FROST implementation](https://github.com/soatok/frost).

Of course, there are some complications.

### FROST Paper vs RFC 9591

The [original FROST paper](https://eprint.iacr.org/2020/852) was published in 2020 by Chelsea Komlo and Ian Goldberg. Section 2.3 of the FROST paper discussed **Distributed Key Generation** (“DKG” for short).

The FROST library I was originally using had implemented a version of the DKG mentioned by the FROST paper.

Unfortunately, RFC 9591 does not specify a DKG algorithm. Instead, it says this:

> This document does not specify how this information, including the signing key shares, are configured and distributed to participants. In general, two configuration mechanisms are possible: one that requires a single trusted dealer and one that requires performing a distributed key generation protocol. We highlight the key generation mechanism by a trusted dealer in [Appendix C](https://www.rfc-editor.org/rfc/rfc9591.html#dep-dealer) for reference.
>
> [RFC 9591: The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two‑Round Schnorr Signatures](https://www.rfc-editor.org/rfc/rfc9591.html#section-5)

![Disgusted Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-14.png?resize=512%2C512&ssl=1)

Wonderful.
Art by [CMYKat](https://cmykatgraphics.carrd.co/)

Since the thing I’m building is intended for creating threshold signatures in a geographically distributed manner **without ever reconstructing the secret key**, a trusted dealer is out of the question since that would require us to, at some point, have a reconstructed secret key in the first place.

### Enter, ChillDKG

After a bit of research (and talking with one of the FROST RFC authors), the direction the industry is moving towards is some kind of standardization of [ChillDKG, a distributed key generation algorithm for FROST](https://github.com/BlockstreamResearch/bip-frost-dkg).

ChillDKG has some nice benefits: It establishes a minimal trusted channel between participants without the need for a trusted coordinator or separate encrypted layer.

(The need for a separate encryption layer for transport wasn’t a game over issue for my tool, because it was always intended to run over a VPN, but not having to require additional setup for security is nice.)

Unfortunately, ChillDKG exists as a Bitcoin Improvement Proposal. Consequently, the reference code only supports [secp256k1](https://soatok.blog/2022/05/19/guidance-for-choosing-an-elliptic-curve-signature-algorithm-in-2022/#secp256k1).

Now, I have no love for cryptocurrency. Given that Ed25519 is in [a lot of things](https://ianix.com/pub/ed25519-deployment.html), including [FIPS 186-5](https://csrc.nist.gov/pubs/fips/186-5/final), I can meet a lot of developers where they already are if I support Ed25519.

Consequently, I’m going to be implementing an Ed25519-only variant of ChillDKG in my FROST implementation. Along the way, I plan on writing a [C2SP specification](https://github.com/C2SP/C2SP) so that others may implement a compatible feature. This specification will vend Ed25519 public keys and operate on the Ristretto255 prime-order group, and my implementation will do the same.

#### On Ed25519 and Ristretto255

Many cryptography protocols assume a prime-order group in their construction.

Ed25519 is a digital signature algorithm based on Schnorr, defined over the edwards25519 elliptic curve.

Edwards25519 is not prime-order; it has a cofactor of 8. This nuance introduced [a double-spend vulnerability](https://moderncrypto.org/mail-archive/curves/2017/000898.html) in CryptoNote-based currencies (most notably, Monero).

In response to this and related issues, cryptographers worked on [Ristretto](https://ristretto.group/ristretto.html), a prime-order group for Curve25519 and Curve448.

If you’re doing basic signatures, Ed25519 is fine.

But the moment you deviate from the `crypto_sign()` API for which Ed25519 was defined, you’re much better off using Ristretto255 and not having to worry about small torsion components.

My plan, therefore, is to define a ChillDKG variant over the Ristretto255 group and then convert the result to an Ed25519 public key.

You might be wondering, “What does that entail?”

#### Piercing the Ristretto255 Group Abstraction

Ristretto255 group elements do not necessarily map to a specific Edwards25519 point with a cleared cofactor. What you need to do is:

1. Multiply the Ristretto element by the cofactor (8).
2. Multiply by the modular inverse of the cofactor.

This will return a birationally equivalent point with a cleared cofactor.

In Go, an implementation of this algorithm might look like this:

```
import (
	"filippo.io/edwards25519"
	"github.com/gtank/ristretto255"
)

var eightInv, _ = edwards25519.NewScalar().SetCanonicalBytes([]byte{
	121, 47, 220, 226, 41, 229, 6, 97,
	208, 218, 28, 125, 179, 157, 211, 7,
	0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 6,
})

// Returns a birationally equivalent point on the edwards25519 curve.
//
// Since the element may not be of order 8, we cannot just return the bytes
// for the underlying point.
//
// However, [8^{-1}][8]P is guaranteed to have a cleared cofactor.
func ToEdwards25519Point(e *ristretto255.Element) *edwards25519.Point {
	p := edwards25519.NewIdentityPoint()
	// this is the byte representation of 8^{-1} mod q
	p.SetBytes(e.Bytes())
	p.MultByCofactor(p)
	p.ScalarMult(eightInv, p)
	return p
}
```

(I had previously offered this as [a built-in feature in the Go Ristretto255 implementation](https://github.com/gtank/ristretto255/pull/45), but...
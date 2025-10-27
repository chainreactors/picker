---
title: Cryptographic Innuendos
url: https://soatok.blog/2024/09/20/cryptographic-innuendos/
source: Dhole Moments
date: 2024-09-21
fetch_date: 2025-10-06T18:27:09.755828
---

# Cryptographic Innuendos

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

[Cryptography](https://soatok.blog/category/cryptography/)

# Cryptographic Innuendos

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [September 20, 2024](https://soatok.blog/2024/09/20/cryptographic-innuendos/)

![Cryptographic Innuendos](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/09/BlogHeader-2024-Innuendo.png?fit=1200%2C675&ssl=1)

Neil Madden recently wrote a blog post titled, [Digital Signatures and How to Avoid Them](https://neilmadden.blog/2024/09/18/digital-signatures-and-how-to-avoid-them/). One of the major points he raised is:

> Another way that signatures cause issues is that they are *too powerful* for the job they are used for. You just wanted to authenticate that an email came from a legitimate server, but now you are [providing irrefutable proof of the provenance of leaked private communications](https://blog.cryptographyengineering.com/2020/11/16/ok-google-please-publish-your-dkim-secret-keys/). Oops!
>
> Signatures are very much the hammer of cryptographic primitives. As well as authenticating a message, they also provide *third-party verifiability* and (part of) *non-repudiation*.
>
> Neil Madden

Later, he goes on to make recommendations for alternatives. Namely HMAC, possibly with a KEM. His recommendations are sensible and straightforward.

***Where’s the fun in that, though?***

![Fingerguns Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-07.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

Let’s design a type of digital signature algorithm that can only be verified by the intended recipients.

## Standard Crypto Disclaimer

Don’t use any of this.

I’m rolling my own crypto, which is almost always a bad idea, for my own amusement.

**Absolutely none of this has been peer-reviewed or audited.**

Even if there’s no immediately obvious fatal flaw in this design, it’s always possible that I screwed something up.

If anything **of value** ever comes of this post, it will be serious cryptographers writing their own protocol that accomplishes the goals set out in this furry blog post, but with a machine verifiable security proof.

## X3MAC

Let’s start with a somewhat simple building block (using libsodium), which I call [X3MAC](https://github.com/soatok/x3mac).

Why? Because it’s partly inspired by [X3DH](https://github.com/soatok/rawr-x3dh).

The idea is [pretty straightforward](https://github.com/soatok/x3mac?tab=readme-ov-file#how-it-works), and basically in line with what Neil recommended:

1. Generate an ephemeral keypair.
2. Do two ECDHs. One between the sender and the recipient, the other between the ephemeral keypair and the recipient.
3. Use a domain-separated hash with both ECDH outputs and all three public keys to obtain a symmetric key.
4. Calculate a MAC over the message, using the symmetric key.
5. Return the ephemeral public key and MAC.

Verification is basically deriving the same symmetric key from the recipient’s perspective, recalculating the MAC, and comparing the two in constant-time.

This should be pretty easy to understand.

### Why bother with ephemeral keypairs?

It doesn’t buy us much for the MAC use-case (since we aren’t encrypting so forward secrecy isn’t a consideration), but we will use it when we turn the X3MAC into X3SIG.

### What are people saying about X3MAC?

When I showed X3MAC to some friends, some recoiled in horror and others said, “Oh, I think I have a use case!”

I really hope they’re joking. But out of caution, this is where I will cease to provide sample code.

Sarah Jamie Lewis said, “[thank you i hate this](https://mastodon.social/%40sarahjamielewis/113167501810744698).” That’s probably the correct response.

## Turning X3MAC into a Signature

X3MAC isn’t actually very useful.

If Alice and Bob use X3MAC, it’s true that only the two of them can verify the authentication tag for a message… but both parties can also *create* authentication tags.

To turn this into a signature algorithm, we need to work with the [Ristretto group](https://ristretto.group/) and build [a non-interactive variant of Schnorr’s identification protocol](https://www.zkdocs.com/docs/zkdocs/zero-knowledge-protocols/schnorr/).

My modified protocol, **X3SIG**, uses Ristretto255 scalars and points instead of X25519 keypairs.

> “**What does any of that even mean?**“
>
> Ristretto255 is a prime-order group (imagine a clock, but instead of numbers going from 1 to 12, it’s between 0 and a very large prime number), built from Curve25519.
>
> Scalars are analogous to secret keys.
>
> Points are analogous to public keys.
>
> You can do point arithmetic. You can do scalar arithmetic. You don’t have to worry about the cofactor (like you would with Ed25519 or X25519).
>
> Schnorr’s identification protocol (explained above) is essentially the basis of elliptic curve signatures; i.e., you can construct EdDSA out of it with minor (yet important) tweaks.
>
> That’s exactly what we’re doing here: Turning X3MAC into a signature by building Schnorr out of it.

The protocol begins the same way as X3MAC: Generate a random scalar, multiply it by the base point to get a point. Do some point-scalar multiplications and a domain-separated hash to derive a symmetric key. Hash the message with the symmetric key.

But this time, we don’t stop there. We use the X3MAC-alike hash in place of the Hash() step in non-interactive Schnorr.

> Important: We can eschew some data from the hashing step because certain parameters are fixed by virtue of using Ristretto255.
>
> If anyone ever builds something on another group, especially one where these parameters can change, you MUST also include all of them in the hash.
>
> If you fail to do this, you will find yourself vulnerable to [weak Fiat-Shamir attacks](https://eprint.iacr.org/2023/691) (e.g., [Frozen Heart](https://blog.trailofbits.com/2022/04/18/the-frozen-heart-vulnerability-in-plonk/)). If you’re writing Rust, check out [Decree](https://github.com/trailofbits/decree) for transcript hashing.

(As stated before: No sample code will be provided, due to not wanting people to ship it to production.)

### What does this give us?

Alice can sign a message that only she and Bob can verify. Bob cannot generate a new signature. Third parties cannot perform either action.

Thus, we still have a digital signature, but not one that provides third-party verifiability.

## X3INU – Cryptographic Innuendos

If we had stopped the train at X3SIG, that’d be pretty neat.

However, X3SIG is limited to one sender and one recipient. This is kind of a bummer that doesn’t scale very well.

Fortunately, this is a solvable problem.

If you recall from [my idea for multicast support in Noise-based protocols](https://soatok.blog/2023/10/10/a-plan-for-multicast-support-in-noise-based-protocols/), I’m no stranger to reusing the TreeKEM abstraction from the MLS RFC to nerd-snipe my friends in the cryptography community.

So let’s do that here.

### X3INU.Pack

Inputs:

1. 1 keypair (sk, pk)
2. A finite number of other public keys (`pk_i` for many values of `i`)

Output:

* Group public key `gpk`

Here, we use a [Ratchet Tree](https://datatracker.ietf.org/doc/html/rfc9420#name-ratchet-tree-concepts) (per RFC 9420) where each step is a scalar multiplication over the Ristretto group (since that’s what everyone’s public key is) and a Key Derivation Function.

The important property is that each participant in the Pack can asynchronously derive the g...
---
title: Let’s All Agree to Use Seeds as ML-KEM Keys
url: https://words.filippo.io/dispatches/ml-kem-seeds/
source: Filippo Valsorda
date: 2024-08-22
fetch_date: 2025-10-06T18:03:19.453201
---

# Let’s All Agree to Use Seeds as ML-KEM Keys

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

21 Aug 2024

# Let’s All Agree to Use Seeds as ML-KEM Keys

Last week, NIST published the final version of the ML-KEM[1](#fn:mlkem) specification, [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final). One change from the draft is that the final document explicitly allows storing the private decapsulation key as a *seed*. This is a plea to the cryptography engineering community: let’s all agree to only use seeds as the storage format of ML-KEM keys, and forget that a serialized format for expanded decapsulation keys even exists.

Seeds have multiple advantages. The most obvious is size: a seed is 64 bytes, while an expanded decapsulation key is 1 632, 2 400, or 3 168 bytes depending on the ML-KEM parameter set.

More importantly, though, a 64-byte seed is always valid, while an expanded decapsulation key needs to be *validated*. FIPS 203, Section 7.3, requires the following check

```
H(dk[384𝑘 : 768𝑘 + 32])) == dk[768𝑘 + 32 : 768𝑘 + 64]
```

to ensure two parts of the input key are consistent: the pre-computed hash of the encapsulation key, and the encapsulation key itself.

That’s not all, though. The decapsulation key expanded format is

```
ByteEncode₁₂(s) || ByteEncode₁₂(t) || ρ || H(ekPKE) || z
```

where *s* and *t* are vectors of [NTT elements](https://words.filippo.io/dispatches/kyber-math/). An NTT element is in turn a vector of field elements, and a field element is a number between zero and 3 329, encoded as a 16-bit integer. What if an encoded field element is higher than 3 329? It’s invalid! What then? Well. If you find one in an *encapsulation key* you are required to reject it by FIPS 203, Section 7.2. But what if you find it in the encapsulation key that’s part of a decapsulation key (the *t* value)? And what if you find it in a different part of a decapsulation key (the *s* value)? The spec doesn’t say!

This whole can of worms just stays on the shelf with seeds, because it’s the implementation itself that derives *s*, *t*, and *H(ekPKE)*, so it can be certain they are valid.

Ok, so seeds are smaller and simpler, reducing the margin for error, but are they expensive? They are not, to the point that loading the expanded decapsulation key over a Gigabit link is almost as expensive as expanding a seed[2](#fn:vsnet), but most importantly it doesn’t matter!

Keys have implicitly two representations: one on the wire, one in memory. The latter can include precomputed values to enable faster operations and doesn’t need a fixed bytes format. The cost of going from one to the other—the cost of seed expansion—is not important for private keys: either keys are ephemeral, in which case they can go straight into the in-memory representation, or they are reused a lot, in which case the deserialization cost is amortized.

The ML-KEM expanded decapsulation key format is actually not even a good in-memory format, because it doesn’t include the full expanded matrix A but its seed ρ. It’s a weird in-between where some values are expanded (so you need to validate them) but some others are not (so you need to expand them).

Seeds have obvious advantages and are explicitly allowed by the specification, so we’ll definitely see them used in the wild. If we *also* support the expanded format, we’re going to see interoperability issues, and we’ll have to carry all the complexity of both code paths. Let’s just not.

Speaking of interoperability, FIPS 203 does a great job of specifying everything in terms of byte sequences[3](#fn:bytes)… *except* the seed, which is defined as *‌(d, z)*. I think every implementation I’ve seen just stores them by concatenating [4](#fn:invert) them as a 64-byte buffer, so hopefully we can all agree on that. If anyone suggests an ASN.1 SEQUENCE of BIT STRINGs or whatever I *will* quit.

~~To really put this to rest, we’re going to need (sooner rather than later!) a specification like [RFC 8410](https://www.rfc-editor.org/info/rfc8410) which specifies the key format and assigns OIDs for use in e.g. PKCS #8. Interestingly, the OID arc used by RFC 8410 for Ed25519, 1.3.101, is now [managed as an IANA registry](https://www.iana.org/assignments/smi-numbers/smi-numbers.xhtml#smi-numbers-1.3.101) with policy [Specification Required](https://datatracker.ietf.org/doc/html/rfc8126#section-4.6), *not* RFC Required. See [RFC 8411](https://www.rfc-editor.org/info/rfc8411). That means that anyone could make e.g. a [C2SP](https://c2sp.org) document referencing FIPS 203 and request OID assignments for ML-KEM. Unless work is already underway to assign OIDs, this might very well be the fastest path, and the longer we wait the more we risk ecosystem fractures.~~

**EDIT** (minutes after pressing send): Well, scratch all that, I was a day behind on my mailing lists inbox and I just saw that NIST has published [OIDs for all ML-KEM parameters](https://csrc.nist.gov/projects/computer-security-objects-register/algorithm-registration) and linked to [draft-ietf-lamps-kyber-certificates-03](https://www.ietf.org/archive/id/draft-ietf-lamps-kyber-certificates-03.html) for the key format specification. The “Private Key Format” section of that draft doesn’t say what the actual private key format is, and hopefully it will land on 64-byte seeds.

Concretely, for implementations, I am suggesting not implementing expanded key parsing and validation at all, or relegating it to an internal function like the [derandomized](https://words.filippo.io/dispatches/avoid-the-randomness-from-the-sky/) variants, not exposed in the public API. That’s [what I did for filippo.io/mlkem768](https://github.com/FiloSottile/mlkem768/compare/55afeac9504dbb4df06844821b0a33ad8c301879...859a9b3f2ff665591a5b659d55aaf0b4111dc171) and probably what we will do for the Go standard library. We will also ensure that the test vectors in [CCTV](https://c2sp.org/CCTV/ML-KEM) and [Wycheproof](https://github.com/C2SP/wycheproof) don’t require it (i.e. that they provide seeds as inputs). This will make it hard or impossible to test issues that require malformed decapsulation keys *but that’s the point*: if you don’t expose the API you don’t need to test its failure cases. All other vectors should be reproducible by bruteforcing seeds.[5](#fn:edge)

If you got this far, you might also want to follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo).

## The picture

In Madeira there is this incredible forest, [Fanal](https://visitmadeira.com/en/what-to-do/nature-seekers/laurissilva-forest/fanal/), full of centenary twisty trees in a mysterious eery atmosphere. One of a few places, along with Barcelona, that are best experienced with the fog. (I grew up in the Padan Plain, and was recently almost ran over by a pack of spooked cows in the thick fog driving a motorcycle up the Matese Apennines, don’t @ me about fog.)

![A group of gnarled, moss-covered trees with thick trunks and twisted branches standing on a foggy, green field, creating a mysterious and enchanting atmosphere.](https://assets.buttondown.email/images/dfd87150-2424-4ac1-a3ef-3e23c407c367.jpeg)

All this work is funded by the awesome [Geomys](https://geomys.org) clients: [Latacora](https://www.latacora.com/), [Interchain](https://interchain.io/), [Smallstep](https://smallstep.com/), [Ava Labs](https://www.avalabs.org/), [Teleport](https://goteleport.com/), [SandboxAQ](https://www.sandboxaq.com/), [Charm](https://charm.sh/), and [Tailscale](https://tailscale.com/). Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the [Geomys announcement](https://words.filippo.io/geomys).)

Here are a few words from some of them!

Latacora — [...
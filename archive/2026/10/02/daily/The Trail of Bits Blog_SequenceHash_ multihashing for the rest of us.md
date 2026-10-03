---
title: SequenceHash: multihashing for the rest of us
url: https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/
source: The Trail of Bits Blog
date: 2026-10-02
fetch_date: 2026-10-03T07:13:04.629112
---

# SequenceHash: multihashing for the rest of us

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# SequenceHash: multihashing for the rest of us

[Opal Wright](/authors/opal-wright/)

October 02, 2026

[cryptography](/categories/cryptography/), [zero-knowledge](/categories/zero-knowledge/), [open-source](/categories/open-source/)

Page content

* [Wait, “multihashing”?](#wait-multihashing)
* [Enter SequenceHash](#enter-sequencehash)
* [What does SequenceHash offer?](#what-does-sequencehash-offer)
  + [Unambiguous input encoding](#unambiguous-input-encoding)
  + [Length-extension prevention](#length-extension-prevention)
  + [Built-in customization strings](#built-in-customization-strings)
  + [MAC mode](#mac-mode)
* [How does SequenceHash work?](#how-does-sequencehash-work)
* [How do I use it?](#how-do-i-use-it)
* [Sounds cool. What about SequenceMAC?](#sounds-cool-what-about-sequencemac)
  + [Some notes on key size](#some-notes-on-key-size)
* [What about extensible output functions (XOFs)?](#what-about-extensible-output-functions-xofs)
* [What if I want to write my own implementation?](#what-if-i-want-to-write-my-own-implementation)
* [Some minor caveats](#some-minor-caveats)

Multihashing is one of those cryptographic tasks that’s easy not to think about too much. This is unfortunate, because multihashing is a [common stumbling point](/2024/08/21/yolo-is-not-a-valid-hash-construction/#yolomultihash) when cryptographers try to use hashes.

As part of our goal to “fix software, not bugs,” Trail of Bits is introducing [SequenceHash and its sister function SequenceMAC](https://github.com/C2SP/C2SP/blob/main/sequencehash.md), a pair of related hash constructions that bring secure multihashing to developers using hash functions other than Keccak. We hope SequenceHash and SequenceMAC will help cryptographers avoid attacks that take advantage of ambiguous input encodings. The specification is open source, and is now a [part](https://github.com/C2SP/C2SP/blob/main/sequencehash.md) of the Community Cryptography Specification Project (C2SP).

SequenceHash and SequenceMAC behave similarly to NIST’s [TupleHash](https://csrc.nist.gov/pubs/sp/800/185/final), but have the advantage of not being tied to a single hash function. They also don’t require developers to implement fiddly computations that aren’t byte-aligned. Instead, SequenceHash and SequenceMAC work out of the box with nearly any secure cryptographic hash function you care to use, including SHA256/384/512, BLAKE, and RIPEMD. SequenceMAC supports keys 32 bytes or longer (up to the ridiculous limit of ${2}^{128}-1$ bytes).

(It’s worth noting: SequenceHash and SequenceMAC rely on the security of the underlying hash for their own security. SequenceHash and SequenceMAC can’t magically make MD4 or SHA0 secure again. For the purposes of this document, it’s assumed that you have chosen a reasonable hash function like SHA256, not CRC32.)

To make SequenceHash and SequenceMAC easy to use, we’re releasing three initial implementations of SequenceHash and SequenceMAC: one each in Rust, Go, and Python. We’re also releasing a large set of test vectors that cover multiple hash functions and include intermediate values to help developers debug and verify their implementations.

## Wait, “multihashing”?

Yeah, it’s a weird term, but the idea is pretty simple. “Multihashing” means “hashing a bunch of values together.” If you’ve ever read a cryptography paper, and there’s a step that says something like “compute the shared authenticator `N=Hash(X, Y, Z, A, B)`,” that’s multihashing. You need to create a hash that incorporates the inputs `X, Y, Z, A`, and `B`. Unfortunately, the simple “solution” of concatenating the inputs and hashing the result can lead to serious security problems.

For example, consider what happens when you hash three inputs using “raw” SHA256:

```
import hashlib

hasher = hashlib.new('sha256')
hasher.update(b'Test 0')
hasher.update(b'Test 1')
hasher.update(b'Test 2')
print(hasher.hexdigest())
hasher = hashlib.new('sha256')
hasher.update(b'Test 0Test 1')
hasher.update(b'Test 2')
print(hasher.hexdigest())
hasher = hashlib.new('sha256')
hasher.update(b'Test 0')
hasher.update(b'')
hasher.update(b'Test 1Test 2')
print(hasher.hexdigest())
```

This produces the following output:

```
4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c
4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c
4fce0a9940a42b5c9d1bcbfc9a6ddd6de20d731d584a0acf5bda6de86483641c
```

Even though inputs are fed in through separate calls, they’re not separated from the perspective of the hash function—under the hood, the inputs are just concatenated.

As with many things in cryptography, multihashing is harder than you think. That’s a big problem because multihashing is a critical component of one of the most important tools in zero-knowledge proofs: the [Fiat-Shamir transform](/2021/02/19/serving-up-zero-knowledge-proofs/). When you get multihashing wrong, you introduce the risk of forgeries into your zero-knowledge proofs. Given that zero-knowledge proofs play a major role in cryptocurrency nowadays, that sort of mistake is sometimes measured in millions of dollars.

But Fiat-Shamir transforms aren’t the only place where you might want to use multihashing. It’s not uncommon to need to hash a collection of related objects, where both the objects *and* the collection are variable in size. Think of authenticating the files in an archive, grouping multiple cryptocurrency transactions into a single hash, or hashing something as [“simple” as somebody’s name](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/).

Multihashing is also used when generating cryptographic commitments to values. In some protocols, one party must perform calculations using secret values, only to reveal them to other parties for later verification. Often, this is done by hashing the secret value along with a random “blinding” value and broadcasting the result to other parties as the commitment. If the boundary between the secret value and the blinding value isn’t clear, a “commitment” can sometimes be opened several different ways.

Unfortunately, nobody seems to have landed on a consistent, standard solution to this problem. Instead, across the open-source ecosystem and in our private audits, we find developers solving the problem in wildly different ways. Some of these solutions are insecure, like using separator characters that can also appear in the inputs. Others encode their data in a way that makes their separators unambiguous, but the encoding is unnecessarily complex and introduces subtle timing risks. Think of stuff like Base64-encoding byte strings and separating the results with dollar signs. We often see situations where *some* hash inputs are length-encoded, but not *all*. It’s the wild west out there.

There are tools specific to Fiat-Shamir transforms, like [Merlin](https://merlin.cool/) and our own [decree](https://github.com/trailofbits/decree), but they don’t work so well for *general* multihashing.

The most widely known standard for multihashing is TupleHash, defined in [NIST SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final). To be clear, TupleHash is great. It solves the multihashing problem in a straightforward way (length-prefix encoding), and it handles inputs of *effectively* unlimited size (if you’re regularly hashing more than ${2}^{2040}-1$ bits of input, Trail of Bits wants to party with you and your disrespect for physics). As a bonus, it naturally operates as an XOF. If TupleHash is available for you, it’s a *great* tool.

TupleHash has a downside, though: it’s only defined to work with Keccak, the function that underpins SHA3. If you replace Keccak with another hash function, several of the important security features (like length-extension resistance) can go away. If you don’t have a Keccak implementation handy, you’re out of...
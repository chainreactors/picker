---
title: Invisible Salamanders Are Not What You Think
url: https://soatok.blog/2024/09/10/invisible-salamanders-are-not-what-you-think/
source: Dhole Moments
date: 2024-09-11
fetch_date: 2025-10-06T18:28:49.046294
---

# Invisible Salamanders Are Not What You Think

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

# Invisible Salamanders Are Not What You Think

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [September 10, 2024](https://soatok.blog/2024/09/10/invisible-salamanders-are-not-what-you-think/)

![Invisible Salamanders Are Not What You Think](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/09/BlogHeader-2024-InvisibleSalamanders.png?fit=1200%2C675&ssl=1)

Ever since the [*Invisible Salamanders* paper](https://eprint.iacr.org/2019/016) was published, there has been a quiet renaissance within my friends and colleagues in applied cryptography for studying systems that use Authenticated Encryption with Associated Data (AEAD) constructions, understanding what implicit assumptions these systems make about the guarantees of the AEAD mode they chose to build upon, and the consequences of those assumptions being false.

I’ve discussed Invisible Salamanders several times throughout this blog, from my criticisms of [AES-GCM](https://soatok.blog/2020/05/13/why-aes-gcm-sucks/) and [XMPP + OMEMO](https://soatok.blog/2024/08/04/against-xmppomemo/) to my vulnerability disclosures in [Threema](https://soatok.blog/2021/11/05/threema-three-strikes-youre-out/).

Five years after *Invisible Salamanders*, it’s become clear to me that many software developers do not fully appreciate the underlying problem discussed in the Invisible Salamanders paper, even when I share trivial [proof-of-concept exploits](https://github.com/soatok/gcm-exploit).

## Background

Fast AEAD constructions based on polynomial MACs, such as AES-GCM and ChaCha20-Poly1305, were designed to provide confidentiality and integrity for the plaintext data, and optionally integrity for some additional associated data, in systems where both parties already negotiated one shared symmetric key.

The integrity goals of the systems that adopted these AEAD constructions were often accompanied by performance goals–usually to prevent Denial of Service (DoS) attacks in networking protocols. Verification needed to be very fast and consume minimal resources.

In this sense, AEAD constructions were an incredible success. So successful, in fact, that most cryptographers urge application developers to use one of the fast AEAD modes as the *default* suggestion without looking deeper at the problem being solved. This is a good thing, because most developers will choose something stupid like [ECB mode](https://words.filippo.io/the-ecb-penguin/) in the absence of guidance from cryptographers, and AEAD modes are much, much safer than any hand-rolled block cipher modes.

The problem is, that *one* tiny little assumption that both parties (sender, recipient) for a communication have agreed on exactly one symmetric key for use in the protocol.

### Fast MACs Are Not Key-Committing

Cryptographers have concluded that AEAD constructions based on polynomial MACs–while great for performance and rejection of malformed packets without creating DoS risks–tend to make the same assumption. This is even true of [misuse-resistant modes like AES-GCM-SIV](https://keymaterial.net/2020/09/07/invisible-salamanders-in-aes-gcm-siv/) and extended-nonce constructions like XSalsa20-Poly1305.

When discussing this implicit assumption of *only one valid key* in the systems that use these AEAD modes, we say that the modes are not *key-committing*. This terminology is based on what happens when this assumption is false.

Consequently, you can take a single, specially crafted ciphertext (with an authentication tag) and decrypt it under multiple different keys. The authentication tags will be valid for all keys, and the plaintext will be different.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/robustness.png?resize=750%2C550&ssl=1)

Art: [Swizz](https://x.com/swizzlestixick)

### What does this look like in practice?

Consider [my GCM exploit](https://github.com/soatok/gcm-exploit), which was written to generate puzzle ciphertexts for the DEFCON Furs badge challenge a few years ago. How it works is conceptually simple (although the actual mechanics behind step 4 is a bit technical):

1. **Generate two keys.**

   There’s nothing special about these keys, or their relationship to each other, and can be totally random. They just can’t be identical or the exploit is kind of pointless.
2. Encrypt some blocks of plaintext with **key1**.
3. Encrypt some more blocks of plaintext with **key2**.
4. Calculate a collision block from the ciphertext in the previous two steps–which is [just a bit of polynomial arithmetic in GF(2^128)](https://github.com/soatok/gcm-exploit/blob/711e158a07c316bee9e2009b9de087dc0c48c0b8/src/Collider.php#L119-L182)
5. Return the ciphertext (steps 2, 3, 4) and authentication tag calculated over them (which will collide for both keys).

A system that decrypts the output of this exploit under key1 will see some plaintext, followed by some garbage, followed by 1 final block of garbage.

If the same system decrypts under key2, it will see some garbage, followed by some plaintext, followed by 1 final block of garbage.

For many file formats, this garbage isn’t really a problem. Additionally, a bit more precomputation allows you to choose garbage that will be more advantageous to ensuring both outputs are accepted as “valid” by the target system.

For example, choosing two keys and a targeted nonce may allow both the valid plaintext and garbage blocks to begin with a PDF file header.

If you’re familiar with [the file polyglot work of Ange Albertini](https://github.com/angea/pocorgtfo), you can use this to turn the Invisible Salamanders problem into an artform.

*And this is just the simple attack!*

The [Invisible Salamanders paper outlined](https://eprint.iacr.org/2019/016.pdf) a more advanced variant (with a proof of concept) in Section 3.2, which doesn’t suffer from nearly as much garbage data as the simple attack.

As Bruce Schneier [often says](https://www.schneier.com/blog/archives/2009/07/new_attack_on_a.html), “Attacks only get better, they never get worse.”

### Why is it called Invisible Salamanders?

The proof-of-concept used in the paper involved sending one picture (of a salamander) over an end-to-end encrypted messaging app, but when the recipient flagged it as abusive, the moderator saw a different picture.

[Real World Cryptography 2019 talk on Invisible Salamanders](https://www.youtube.com/watch?v=3M1jIO-jLHI)

Thus, the salamander was invisible to the moderators of the encrypted messaging app.

As for the choice of a “salamander”, I’ve been told by friends familiar with the research that was inspired by the original name of the Signal Protocol being “Axolotl”.

But, like, who cares about these details besides me? It’s a cute and memorable name.

### What are the consequences of violating the “one key” assumption?

That depends entirely on what your system does!

In *[Database Cryptography Fur the Rest of Us](https://soatok.blog/2023/03/01/database-cryptography-fur-the-rest-of-us/)*, I discussed the use of AEAD modes to prevent [confused deputy attacks](https://soatok.blog/2023/03/01/database-cryptography-fur-the-rest-of-us/#confused-deputies). This works great, but if you’re building an application that supports [multi-tenancy](https://soatok.blog/2023/03/01/database-cryptography-fur-the-rest-of-us/#multi-tenancy), you suddenly have to care about this issue again.

An earlier design for [OPAQUE](https://datatracker.ietf.org/doc/draft-i...
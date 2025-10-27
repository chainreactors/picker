---
title: Extending the AES-GCM Nonce Without Nightmare Fuel
url: https://soatok.blog/2022/12/21/extending-the-aes-gcm-nonce-without-nightmare-fuel/
source: Dhole Moments
date: 2022-12-22
fetch_date: 2025-10-04T02:13:55.021051
---

# Extending the AES-GCM Nonce Without Nightmare Fuel

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

# Extending the AES-GCM Nonce Without Nightmare Fuel

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [December 21, 2022](https://soatok.blog/2022/12/21/extending-the-aes-gcm-nonce-without-nightmare-fuel/)
* [1 Comment on Extending the AES-GCM Nonce Without Nightmare Fuel](https://soatok.blog/2022/12/21/extending-the-aes-gcm-nonce-without-nightmare-fuel/#comments)

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/12/BlogHeader-NonceExtension.png?fit=1200%2C675&ssl=1)

When it comes to AES-GCM, I am [not a fan](https://soatok.blog/2020/05/13/why-aes-gcm-sucks/). Most of my gripes fall into one of two categories:

1. Gripes with AES itself
2. Gripes with AES-GCM as a construction

However, one of my gripes technically belongs in both categories: The small nonce size, which is caused by AES’s block size, limits [the amount of data you can safely encrypt with a single symmetric key](https://soatok.blog/2020/12/24/cryptographic-wear-out-for-symmetric-encryption/).

While this problem is less significant for AES-GCM-SIV, I’ve been marinating on the problem of the short AES-GCM nonce for a while.

“Wouldn’t it be great if we could define an extended-nonce construction for AES-GCM?”

![Contemplating, Thinking Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-12.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

I’ve previously [written about extended-nonce constructions](https://soatok.blog/2021/03/12/understanding-extended-nonce-constructions/) with a focus on ChaCha.

## How ChaCha Became XChaCha

*If you’d like a deeper dive, check out [this section](https://soatok.blog/2021/03/12/understanding-extended-nonce-constructions/#xchacha) of my previous blog post on the topic of extended-nonce constructions.*

XChaCha is just ChaCha with a fast key derivation function. You feed in an additional 16 bytes (your extension to the nonce) and your key, and it outputs a subkey. You use this subkey with ChaCha as normal.

What makes XChaCha interesting is that the fast key derivation function, HChaCha, is a tweak of ChaCha (minus the final addition) that acts as a keyed hash function.

This means that the performance cost of this key derivation is roughly the same as extending your plaintext by 64 bytes (one internal ChaCha block), if slightly faster because the final addition is skipped.

If we wanted to propose a fast alternative to AES-GCM, we would need to have a similar performance story.

Most systems that have hardware-accelerated AES would not get the same performance if we opted for, say, HKDF-HMAC-SHA256 for such a construction.

For years, this was where my line of inquiry had stopped, because there didn’t seem like an obvious or elegant way to solve this problem.

![Coffee Sip Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-15.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Interlude: Meet AES-CCM

AES-GCM has a cousin in the world of AES-based and NIST-approved authenticated encryption modes. It’s called CCM (Counter with CBC-MAC).

AES-CTR isn’t particularly interesting (AES-GCM also uses Counter Mode under the hood), but CBC-MAC is a compelling construct (if one [that cryptographers have strong negative feelings about](https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/)).

> If you’re like most people, you don’t have a strong opinion about [CBC-MAC](http://en.wikipedia.org/wiki/CBC-MAC). In fact, if you’re like most people, you don’t have a strong opinion about *any* crypto primitive.
>
> This is healthy. Keep up the good work.
>
> Matthew Green

Notably, AES-CCM is the default mode of the [Stanford Javascript Crypto Library (SJCL)](http://bitwiseshiftleft.github.io/sjcl/). More things are using AES-CCM than you might suspect!

If AES-CCM is a secure construction for authenticated encryption, then we can reason about the security of CBC-MAC (when used correctly; see Matthew Green’s post).

## Introducing AES-XGCM

With these separate thoughts joined together, I’d like to propose a construction I like to call AES-XGCM (named in the spirit of XSalsa20 and XChaCha).

The security of AES-XGCM depends on two assumptions:

1. The overall security of AES-GCM (minus birthday attacks)
2. The PRF security of AES-CBC-MAC with fixed-length inputs

Additionally, the construction is morally equivalent to the incumbent extended-nonce designs: You have a novel fast key derivation step, but then you’re back in familiar territory.

## AES-XGCM Definition

### AES-DeriveSubKey

**Inputs**:

1. Nonce extension (E), 16 bytes
2. Key (K), 16 or 32 bytes

**Algorithm**:

1. If |K| = 32
   * Set b0 = AES-CBC-MAC over the following inputs:
     + Plaintext: E || 0x01
     + Key: K
   * Set b1 = AES-CBC-MAC over the following inputs:
     + Plaintext: E || 0x02
     + Key: K
   * Return b0 || b1
2. If |K| = 16
   * Return AES-CBC-MAC over the following inputs:
     + Plaintext: E || 0xFF
     + Key: K
3. If |K| is anything else, error.

**Output:**

16 or 32 byte subkey (same length as input key)

### AES-XGCM Encryption

**Inputs**:

1. Plaintext (P)
2. AAD (A)
3. Nonce (N), 28 bytes
4. Key (K), 16 or 32 bytes

**Algorithm**:

1. Derive a subkey (sk) using AES-DeriveSubKey with the first 16 bytes of N along with K
2. AES-GCM Encrypt with:
   * Plaintext (P)
   * AAD (A)
   * Nonce (remaining 12 bytes of N)
   * Subkey (sk)

**Outputs**:

* AES-GCM ciphertext (same length as P)
* Authentication tag (T)

### AES-XGCM Decryption

**Inputs**:

1. Ciphertext (C)
2. Authentication tag (T), 16 bytes
3. Nonce (N), 28 bytes
4. Key (K), 16 or 32 bytes

**Algorithm**:

1. Derive a subkey (sk) using AES-DeriveSubKey with the first 16 bytes of N along with K
2. AES-GCM Decrypt with:
   * Ciphertext (C)
   * Tag (T)
   * AAD (A)
   * Nonce (remaining 12 bytes of N)
   * Subkey (sk)

**Output**:

Either an error or the plaintext (same length as ciphertext).

## Design Rationale

This proposal supports both AES-128 and AES-256. To ensure domain separation, the suffix for AES-128 is `0xFF` (`-1` as an unsigned char) while the suffixes for AES-256 are `0x01` and `0x02`.

The output of AES-CBC-MAC is never revealed, since we’re using the algorithm for fast key derivation. Thus, we don’t need any of the CBC-MAC tweaks (length prefix, encrypt last block, etc.). Additionally, we use an all-zero IV.

XSalsa20 and XChaCha used a public computation for its key derivation: The same indices of the state after 20 rounds of HSalsa20 or HChaCha corresponding to publicly known inputs (constants and the nonce) are used to extract the key.

With AES-XGCM, the analogous version of a public computation is the output of the block cipher over a known plaintext (the nonce).

### Security Properties

The additional 16 bytes of randomness yields 128 extra bits of nonce misuse-resistance on top of AES-GCM. This changes the safety limit of vanilla AES-GCM.

Previously, AES-GCM would become unsafe after 2^32 messages encrypted under the same key. This nonce extension adds 2^128 different possible subkeys into the risk calculus. This implies a birthday bound such that:

* You have a 50% chance of nonce reuse after 2^112 messages
* You have a 1 in 2^32 chance of nonce reuse after 2^96 messages

### Performance Properties

The data being fed into AES-CBC-MAC is always a fixed length of 32 bytes...
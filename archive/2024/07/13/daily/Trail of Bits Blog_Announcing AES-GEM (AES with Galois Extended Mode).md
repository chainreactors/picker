---
title: Announcing AES-GEM (AES with Galois Extended Mode)
url: https://blog.trailofbits.com/2024/07/12/announcing-aes-gem-aes-with-galois-extended-mode/
source: Trail of Bits Blog
date: 2024-07-13
fetch_date: 2025-10-06T17:42:49.448236
---

# Announcing AES-GEM (AES with Galois Extended Mode)

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Announcing AES-GEM (AES with Galois Extended Mode)

Scott Arciszewski

July 12, 2024

[cryptography](/categories/cryptography/)

Today, AES-GCM is one of two cipher modes used by TLS 1.3 (the other being ChaCha20-Poly1305) and the preferred method for encrypting data in FIPS-validated modules. But despite its overwhelming success, AES-GCM has been the root cause of some catastrophic failures: for example, Hanno Böck and Sean Devlin exploited nonce misuse to [inject their Black Hat USA slide deck](https://www.blackhat.com/docs/us-16/materials/us-16-Devlin-Nonce-Disrespecting-Adversaries-Practical-Forgery-Attacks-On-GCM-In-TLS-wp.pdf) into the MI5 website.

Security researchers have been sounding the alarm about AES-GCM’s weaknesses for years. Nineteen years ago, Niels Ferguson [submitted a paper](https://csrc.nist.gov/csrc/media/projects/block-cipher-techniques/documents/bcm/comments/cwc-gcm/ferguson2.pdf) to a NIST project on block cipher modes outlining authentication weaknesses in AES-GCM (although NIST would ultimately standardize it). And earlier this year, Amazon published a paper that detailed [practical challenges with AES-GCM](https://csrc.nist.gov/csrc/media/Events/2023/third-workshop-on-block-cipher-modes-of-operation/documents/accepted-papers/Practical%20Challenges%20with%20AES-GCM.pdf) and posited that AES’ 128-bit block size is no longer sufficient, preferring a 256-bit block cipher (i.e., Rijndael-256).

To address these issues, I propose a new block cipher mode called Galois Extended Mode (GEM for short), which I presented last month at the [NIST workshop on the requirements for an accordion mode cipher](https://csrc.nist.gov/Events/2024/accordion-cipher-mode-workshop-2024). AES-GEM improves the security of GCM in every dimension with minimal performance overhead.

**Important:** The current design for AES-GEM is not ready for production use, as some details will likely change in the future. To understand the current design, let’s start by understanding where AES-GCM falls short, and then discuss how we can do better with GEM.

### How AES works

Before we dive in, it may be helpful for some readers to explain some of the terms and concepts used throughout this blog post.

**AES** (Advanced Encryption Standard) is a block cipher widely used to encrypt information. It supports multiple key sizes (128-, 192-, and 256-bit keys) but always operates on 128-bit blocks. AES is the standardized form of the Rijndael family of block ciphers. Rijndael supports other block sizes than 128-bit, but only the 128-bit blocks were standardized by NIST. Modern processors provide dedicated hardware instructions for accelerating AES operations, but the AES key schedule can still negatively impact performance.

**ECB** (Electronic Code Book) mode is the absence of a block cipher mode of operation. It involves computing the block cipher directly on a block of data. ECB mode is not semantically secure, as many cryptographers have [demonstrated](https://words.filippo.io/the-ecb-penguin/). For improved security, block ciphers like AES are typically used with a mode of operation. (If not, they almost certainly should be. Get in touch with our cryptography team if you think you’re using ECB to encrypt sensitive data.)

**CTR** (Counter Mode) is a mode of operation for block ciphers wherein an increasing sequence of values is encrypted with the block cipher to produce a pseudorandom keystream. To encrypt data, simply calculate the XOR of each plaintext byte with each corresponding keystream byte.

**GCM** (Galois/Counter Mode) is a block cipher mode of operation that provides authenticated encryption. It is what cryptographers call an AEAD mode: Authenticated Encryption with Additional Data. GCM can provide confidentiality for sensitive data and integrity for both sensitive and public data.

AEAD modes are important for designing cryptosystems that are resilient to attackers who attempt to mutate encrypted data in order to study the system’s behavior in hopes of learning something useful for cryptanalysis.

GCM is a composite of Counter Mode (CTR) for encrypting the plaintext and a Galois field Message Authentication Code (GMAC), which authenticates the ciphertext (and, if provided, additional associated data). GMAC is defined with a function called **GHASH**, which is a polynomial evaluated over the authenticated data. The output of GHASH is XORed with an encrypted block to produce the final authentication tag. The authentication key, called H, is calculated by encrypting a sequence of 128 zeroed bits.

**POLYVAL** is an alternative to GHASH that is used in AES-GCM-SIV. The irreducible polynomial used by POLYVAL is the reverse of GHASH’s irreducible polynomial.

Many cipher modes (including GCM and CTR) require a number that is used only once for each message. This public number that should never be repeated is called a **nonce**.

Finally, the **birthday bound** is a concept from probability theory that indicates the likelihood of collisions in a set of random values. In cryptography, it implies that if nonces are selected randomly, the probability of two nonces colliding increases significantly as more nonces are used. For AES-GCM with 96-bit nonces, after about 232 messages, there’s a 1 in 232 chance of a nonce collision, which can lead to security vulnerabilities such as the ability to forge messages.

### Practical challenges with AES-GCM today

The biggest challenge with AES-GCM, as others have pointed out, is that AES only has a 128-bit block size. This has two primary consequences:

1. The size of the public nonce and internal counter is constrained to a total of 128 bits. In practice, the nonce size is usually 96 bits, and the counter is 32 bits. If a larger nonce is selected, it is hashed down to an appropriate size, which has little improvement on security. If you ever reuse a nonce, you leak the authentication subkey and can, therefore, forge messages indefinitely.
2. Above a certain number of blocks encrypted under the same key, an attacker can distinguish between ciphertext and random bytes with significant probability.

When you understand that we’re dealing with powers of two, 96 bits of nonce space may sound like a lot, but if you’re selecting your nonces randomly, you can encrypt only 232 messages before you have a 2-32 probability of a collision. Using a cipher with a larger block size would alleviate this pain point, but it’s not the only way to fix it.

The AES block size is not the only problem with AES-GCM in practice. As [Niels Ferguson pointed out in 2005](https://csrc.nist.gov/csrc/media/projects/block-cipher-techniques/documents/bcm/comments/cwc-gcm/ferguson2.pdf), a successful forgery against short tags reveals the authentication subkey.

Further, we also learned that AES-GCM has an unexpected property where multiple keys can decrypt the same ciphertext + authentication tag. Its discoverers referred to this problem as [Invisible Salamanders](https://eprint.iacr.org/2019/016.pdf) because it allowed them to hide a picture of a salamander from an abuse-reporting tool in an encrypted messaging application. Mitigating against Invisible Salamanders in a protocol that uses AES-GCM requires some one-way commitment of the key used.

Finally, the maximum plaintext length for a single message in AES-GCM is relatively small: just below 64 GiB. In order to cope with this maximum length, software often decomposes larger messages into shorter frames that fit within this length constraint. This leads to the limited nonce space before the birthday bound being used up much more quickly than if longer messages were tolerable.

### Introducing AES-GEM

Our proposal, Galois Extended Mode, is a modification of GCM (Galois/Counter Mode) that currently addresses most of these weaknesses. However, there is still an open ques...
---
title: Best practices for key derivation
url: https://blog.trailofbits.com/2025/01/28/best-practices-for-key-derivation/
source: Trail of Bits Blog
date: 2025-01-29
fetch_date: 2025-10-06T20:07:17.171953
---

# Best practices for key derivation

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Best practices for key derivation

Marc Ilunga

January 28, 2025

[cryptography](/categories/cryptography/), [blockchain](/categories/blockchain/)

Key derivation is essential in many cryptographic applications, including key exchange, key management, secure communications, and building robust cryptographic primitives. But it’s also easy to get wrong: although standard tools exist for different key derivation needs, our audits often uncover improper uses of these tools that could compromise key security. [Flickr’s API signature forgery vulnerability](https://vnhacker.blogspot.com/2009/09/flickrs-api-signature-forgery.html) is a famous example of misusing a hash function during key derivation.

These misuses indicate potential misunderstandings about key derivation functions (KDFs). This post covers best practices for using KDFs, including specialized scenarios that require careful treatment of key derivation to achieve the desired security properties. Along the way, we offer advice for answering common questions, like:

* Do I need to add extra randomness to HKDF?
* Should I use salt with HKDF?
* Should I use different salts to derive multiple keys from HKDF?
* How do I combine multiple sources of keying material?

Before diving into key derivation best practices, we’ll recap some important concepts to help us better understand them.

### Sources of keying material

Keyed cryptographic primitives, such as AEADs, require keying material that satisfies certain requirements to guarantee security. In most cases, primitives require that the key is generated uniformly at random or cryptographically close to uniform random. We will distinguish four types of keying material:

* (Uniform) random, such as 32 bytes generated with the OS CSPRNG
* Non-uniform but high entropy, such as the output of key exchange
* Low-entropy, such as passwords and other easily guessable values
* Sets of several sources, such as pre- and post-quantum shared secrets

![](/img/wpdump/1198be6712f322c9ab630d25e515f363.png)

Figure 1: A diverse collection of keys (generated with AI)

The last category above is particularly relevant to the current development of quantum-resistant cryptography. Hybrid key exchange protocols combining classical and post-quantum key exchanges are designed to protect against [Store Now Decrypt Later](https://en.wikipedia.org/wiki/Harvest_now%2C_decrypt_later) attacks.

### How key derivation works

Key derivation is the process of generating acceptable keying material for cryptographic usage from some initial keying material (IKM). From a cryptographic perspective, “acceptable” usually means chosen uniformly at random from the set of all possible keys or indistinguishable from a truly random key. There are two main key derivation tasks related to the nature of the initial keying material.

* **Randomness extraction** extracts a cryptographic key from an IKM with “enough randomness.” Randomness extraction optionally uses a salt. Naturally, we can apply randomness extraction to a key that is already cryptographically appropriate.
* **Randomness expansion** derives subkeys from a cryptographic key. Expansion generally uses a “context” or “info” input unique to each subkey.

This categorization is heavily influenced by the widely used KDF algorithm [HKDF](https://datatracker.ietf.org/doc/html/rfc5869); other KDF designs do not necessarily follow the same principles. However, extraction and expansion are well reflected in most KDF applications. Additionally, we will consider an additional KDF task related to complex sources of keying material, such as a set of sources.

#### Extraction and expansion: a brief look into HKDF

*Tip: if you prefer a visual demonstration of HKDF, refer to the animations below.*

HKDF was designed to provide both extraction and expansion. HKDF is commonly accessible to applications with an API, such as `HKDF(ikm, salt, info, key_len)`. However, under the hood, the following happens: first, an extraction process generates a pseudo-random key (PRK) from the IKM and salt `prk = HKDF.Extract(ikm, salt) = HMAC(salt, ikm)`. Then, a subkey of length key\_len is generated: `sub_key = feedback[HMAC](prk, info)`. Here, `feedback[HMAC]` is a wrapper around `HMAC` that generates output as long as desired by repeatedly calling HMAC; in other words, it implements a variable-length pseudorandom function. For a given key, `feedback` will return a random bit string of the required length for every new `info` input; a fixed `info` value will always produce the same output. If `info` is kept constant but the length is variable, the smaller output will be a prefix of the longer output.

[
](/img/wpdump/2216e8524016ee7b84f190955fcea169.mp4)

Figure 2: Visualizing the extraction and expansion phases of a KDF

**Regarding the extraction salt:** the extraction stage of HKDF optionally takes a salt. The extraction salt is a *random, non-secret* value used to extract sufficient randomness from the keying material. Crucially, the salt cannot be attacker-controlled, since that could lead to catastrophic outcomes for KDFs in general. Hugo Krawczyk [provides a theoretical example](https://eprint.iacr.org/2010/264.pdf#page=10.33) of attacker-controlled salts breaking the independence between the salt and the IKM, leading to weak extractor construction. However, the consequences can also have practical relevance, as we discuss in the next section. A typical pain point for many applications (except, e.g., authenticated key exchange) is authenticating salts. Therefore, the [HKDF standard](https://datatracker.ietf.org/doc/html/rfc5869#section-2.2) recommends that most applications use a constant, such as an all-zero-byte string. The price to be paid for not using a salt is making somewhat stronger, albeit still reasonable, assumptions on HMAC.

### Addressing KDF misuses

Developers must consider several questions when choosing a KDF, but a misunderstanding of KDFs may lead to choices that introduce security issues. Below, we provide examples of misuse along with best practices to help avoid improper use of KDF.

#### Should I use different salts to derive multiple subkeys?

With the aforementioned KDF abstraction, subkey generation is better suited to randomness expansion. Given a pseudo-random key (perhaps obtained after an extraction step), subkeys can be obtained with randomness expansion using unique info inputs for each subkey. The salt is used for extraction. Furthermore, as discussed above, attacker-controlled salts can be detrimental to security. Consider a key management application that generates user keys on demand. One implementation might decide to derive a key from a master key using the username as salt. Besides freely choosing their usernames, users may provide a context string (e.g., `“file-encryption-key”`) that indicates the purpose of the key and ensure that different applications use independent keys. The core functionality is shown in the code snippet below:

```
# For each subkey
def generate_user_key(username, purpose, key_len):
    ikm = fetch_master_key_from_kms()
sub_key = hkdf(ikm=ikm, salt=username, info=purpose, key_len=key_len)
```

Figure 3: Key management application using a master key to derive keys on demand

This construction is bad: since the salt is used as an HMAC “key” for extraction, it is first preprocessed by a PAD-or-HASH scheme ([key padding](https://datatracker.ietf.org/doc/html/rfc2104#section-2), [key hashing](https://datatracker.ietf.org/doc/html/rfc2104#section-3)) to handle variable-length keys. In this implementation, if your username is `b”A”*65`, and I choose my username to be `sha256(b”A”*65)`, then I will get all your keys!

So what should we do instead? The first thing to avoid is potentially attacker-controlled salts. In the example above, the application could generate a ran...
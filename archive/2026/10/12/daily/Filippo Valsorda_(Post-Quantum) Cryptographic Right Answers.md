---
title: (Post-Quantum) Cryptographic Right Answers
url: https://words.filippo.io/right-answers/
source: Filippo Valsorda
date: 2026-10-12
fetch_date: 2026-10-13T08:37:05.152931
---

# (Post-Quantum) Cryptographic Right Answers

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

12 Oct 2026

# (Post-Quantum) Cryptographic Right Answers

Publishing “Cryptographic Right Answers” for developers is a tradition by now. [Colin Percival started in 2009](https://www.daemonology.net/blog/2009-06-11-cryptographic-right-answers.html), [Thomas Ptacek followed up in 2015](https://gist.github.com/tqbf/be58d2d39690c3b366ad), and then [Latacora carried on in 2018](https://www.latacora.com/blog/cryptographic-right-answers/) and [2024](https://www.latacora.com/blog/post-quantum-cryptographic-right-answers/#pqc-right-answers).

It might feel too soon for an update, but *so much has changed*. The timeline of the post-quantum transition [dramatically shifted in early 2026](https://words.filippo.io/crqc-timeline/), and there is now consensus that it needs to complete by 2029. 2029! We have three years!

The good news is that, despite what you might have heard, [symmetric cryptography is going to be fine, because Grover does not matter](https://words.filippo.io/128-bits/). The bad news is that all asymmetric answers changed compared to 2018 and most even compared to 2024.

The answers below assume you are not constrained by any specific compliance regime, although they are mostly compatible with FIPS 140.[1](#fn:fips140) If you need to follow something stricter like CNSA 2.0, you’ll know. Just substitute as appropriate.

Finally, remember the other big change of 2026: LLMs are very good at finding bugs now. “Get a review from the best model you can afford” is now firmly a Cryptographic Right Answer, along with the long-time classic “use a memory-safe language.”

If you’re in a rush, here’s the cheat sheet:

* **Encrypting data**: If you’re in the cloud, KMS. Otherwise, XAES-256-GCM or XChaCha20Poly1305 with random nonces. If you’re encrypting more than a few MB, use Cobblestone-128.
* **Symmetric key length**: Don’t stress it. 256-bit keys if you need to pick.
* **Symmetric “signatures”**: HMAC-SHA-256.
* **Hash algorithm**: SHA-2 is still fine, but use a real multihash (SequenceHash) if needed.
* **Random IDs**: 32 random bytes, a.k.a. 256-bit random numbers.
* **Password handling**: Argon2id or scrypt. But have you considered passkeys instead?
* **Key exchange**: X25519+ML-KEM-768 in a secure, standard protocol.
* **Asymmetric encryption**: HPKE with (MLKEM768-X25519 a.k.a. X-Wing, HKDF-SHA256, AES-128-GCM), or age with PQ keys.
* **Asymmetric signatures**: ML-DSA-44.
* **Website or client-server application security**: If you’re in the cloud, use its ALB/NLB. Otherwise, rustls, Go’s crypto/tls, BoringSSL, AWS-LC, or s2n-tls with a popular, updated ACME client.
* **Online backups**: restic with a long random password.

Now let’s dive in.

### Encrypting data

If you’re in the cloud, **KMS**. Otherwise, **XAES-256-GCM** or **XChaCha20Poly1305** with random nonces. If you’re encrypting more than a few MB, use [**Cobblestone-128**](https://c2sp.org/chunked-encryption).

*Percival, 2009*: AES-CTR with HMAC.
*Ptacek, 2015*: NaCl/libsodium default, or ChaCha20Poly1305, or AES-GCM.
*Latacora, 2018*: KMS, or XSalsa20+Poly1305.
*Latacora, 2024*: KMS, or NaCl’s secretbox, or XChaCha20Poly1305.

[Latacora’s reasoning for why and when you’d use your cloud’s KMS](https://www.latacora.com/blog/cryptographic-right-answers/#encrypting-data) is still solid, so start there.

If you’re encrypting locally, you want an AEAD where you can avoid worrying about tracking nonces or how many messages you encrypted, so you want random nonces of at least 128 bits.[2](#fn:gcm128)

NaCl/libsodium’s secretbox is just a [paper-thin wrapper](https://words.filippo.io/nacl-api/) around a less common AE construction (XSalsa20+Poly1305), so instead I recommend [XAES-256-GCM](https://words.filippo.io/xaes-256-gcm/) or XChaCha20Poly1305. The former is an efficient composition of a standard KDF and AES-GCM, packaged as an extended-nonce AEAD, so even if your library doesn’t provide it under that name you can assemble it from the KDF and AES-GCM APIs.[3](#fn:XAES-256-GCM)

Regular AES-GCM and ChaCha20Poly1305 with random nonces are only ok if you *know for certain* you won’t encrypt more than a billion messages with one key. AES-GCM-SIV is also a good AEAD choice if you happen to have it everywhere you need it, but that’s kinda unlikely. Some even newer options have nice properties like key commitment, but are not commonly available yet.

Since you have an AEAD, consider putting context in the additional data, like the user ID you’re encrypting for, or the version of the protocol. Anything not secret that you will definitely still know at decrypt time.

Very important is how you handle large messages, which KMS will not solve for you. *Do not* pass one large message to an AEAD, or you might be forced to process or store the plaintext before having authenticated it at decrypt time. *Absolutely do not* use unauthenticated stream ciphers. Instead, you should use STREAM (which is not a stream cipher but a way to use AEADs on a stream… I know, I know, terrible name). There are a lot of options—too many, in fact—and shamefully none are the consensus answer. [Tink has one](https://developers.google.com/tink/encrypt-large-files-or-data-streams#streaming_aead), [libsodium has one](https://libsodium.gitbook.io/doc/secret-key_cryptography/secretstream), [the AWS Encryption SDK has one](https://github.com/aws/aws-encryption-sdk-python/blob/a6c0413bb0ddc9bccdefad9f1d2c031e0bc4db29/examples/src/file_streaming_example.py), [FLOE is one](https://c2sp.org/FLOE), age has one, and the list goes on. I recommend [Cobblestone-128](https://c2sp.org/chunked-encryption), which is a STREAM variant derived from TLS, and is available in pyca/cryptography and soon in the Go standard library (and in the meantime at [filippo.io/cobblestone](https://filippo.io/cobblestone)).[4](#fn:Cobblestone)

*Avoid*: unauthenticated modes (CBC, CTR, raw stream ciphers), random 96-bit nonces unless you spent a lot of time thinking about how many messages you encrypt, rolling your own AEAD construction.

### Symmetric key length

**Don’t stress it.** 256-bit keys if you need to pick.

*Percival, 2009*: 256-bit AES keys.
*Ptacek, 2015*: 256-bit keys.
*Latacora, 2018*: 256-bit keys.
*Latacora, 2024*: 256-bit keys.

Remember that Grover doesn’t actually matter and 128-bit brute-force attacks don’t exist. Still, 256-bit keys rule out multi-target attacks, which is nice.

However, don’t make other decisions based on this. For example, the recommended Cobblestone suite uses 128-bit keys and that’s fine because it has a careful analysis of multi-target attacks. Likewise, don’t go changing the default cipher suite preferences of your TLS library to enforce 256-bit keys; there’s no need.

AES-256 is slower than AES-128 because unfortunately Rijndael ties the number of rounds to the key size, but this probably won’t matter in practice.

*Avoid*: anything other than 128 or 256 bits, worrying too much about size, keys that are not uniform (e.g. using a password or ASCII hex string directly as a key).

### Symmetric “signatures”

**HMAC-SHA-256**.

*Percival, 2009*: HMAC.
*Ptacek, 2015*: HMAC.
*Latacora, 2018*: HMAC.
*Latacora, 2024*: HMAC.

Yay for HMAC.

Just be careful to sidestep canonicalization and parser alignment bugs by always authenticating a verbatim string of bytes, not something you need to recompute.

*Good:*

```
{
    "inner": "{\"foo\":123}",
    "hmac": "MbPsZq7QGCllJgDnSSy/cyM10HjqiVu35UO7yyY5d3w="
}
```

Check the HMAC and then process or store or forward just `{"foo":123}`.

*Bad:*

```
{
    "foo": 123,
    "hmac": "MbPsZq7QGCllJgDnSSy/cyM10HjqiVu35UO7yyY5d3w="
}
```

You can use KMAC or keyed BLAKE3 if you already had a reason to use their underlying hashes. HMAC-SHA-512 is also fine.

Remember to compare tags with dedicated constant-time functions.

*Avoid*: rolling your own [YoloMAC](https://blog....
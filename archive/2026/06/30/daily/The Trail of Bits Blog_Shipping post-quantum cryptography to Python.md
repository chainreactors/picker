---
title: Shipping post-quantum cryptography to Python
url: https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/
source: The Trail of Bits Blog
date: 2026-06-30
fetch_date: 2026-07-01T06:23:20.599594
---

# Shipping post-quantum cryptography to Python

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Shipping post-quantum cryptography to Python

[Alexis Challande](/authors/alexis-challande/)

June 30, 2026

[cryptography](/categories/cryptography/), [open-source](/categories/open-source/), [post-quantum](/categories/post-quantum/)

Page content

* [Post-quantum support is now one pip install away](#post-quantum-support-is-now-one-pip-install-away)
* [PQ algorithm tradeoffs](#pq-algorithm-tradeoffs)
* [Using ML-DSA (FIPS 204): Quantum-resistant signatures](#using-ml-dsa-fips-204-quantum-resistant-signatures)
* [Using ML-KEM (FIPS 203): Key encapsulation for the post-quantum era](#using-ml-kem-fips-203-key-encapsulation-for-the-post-quantum-era)
* [The road ahead: SLH-DSA and protocol integration](#the-road-ahead-slh-dsa-and-protocol-integration)
  + [SLH-DSA](#slh-dsa)
  + [Post-quantum in protocols](#post-quantum-in-protocols)
* [Acknowledgments](#acknowledgments)

Post-quantum cryptography is now one `pip-install` away for the entire Python ecosystem. With funding from the [Sovereign Tech Agency](https://www.sovereign.tech/), we implemented support for ML-KEM, the NIST-standard key-establishment primitive, and ML-DSA, the NIST-standard digital-signature primitive, in `pyca/cryptography`.

On June 22, 2026, the White House [ordered](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) the U.S. government to accelerate its transition to post-quantum cryptography. The order says large-scale quantum computers, especially in adversarial hands, will threaten widely used cryptographic systems, and that attackers may already be collecting encrypted data now so they can decrypt it later. It also sets concrete migration deadlines: high-value and high-impact federal systems must use post-quantum key establishment by **December 31, 2030**, and post-quantum digital signatures by **December 31, 2031**. And even if you don’t care about quantum resistance, that’s not a problem because [quantum resistance isn’t the main benefit of post-quantum crypto.](https://blog.trailofbits.com/2024/07/01/quantum-is-unimportant-to-post-quantum/)

That transition cannot happen only at the policy layer. Every application that signs packages, validates certificates, establishes secure channels, or protects long-lived secrets depends on cryptographic libraries. If those libraries do not expose post-quantum algorithms, the software stack cannot migrate.

Almost every Python program that touches cryptography goes through `pyca/cryptography`. It’s currently the [eleventh most-downloaded package on PyPI](https://pypistats.org/top), pulling 1.2 billion downloads in the last month alone. The `pyca/cryptography` package handles the cryptographic operations of projects like Ansible, Certbot (the Let’s Encrypt client), Apache Airflow, paramiko (the Python-only SSH client), and [many others](https://deps.dev/pypi/cryptography/48.0.0/dependents). If `pyca/cryptography` doesn’t ship post-quantum primitives, the Python ecosystem can’t begin to migrate.

## Post-quantum support is now one pip install away

As of `cryptography>=48`, support for post quantum algorithms is just a `pip install` away. The version 48 release includes our Rust bindings for ML-KEM and ML-DSA, the cross binding API and tests, and support for AWS-LC as a cryptographic backend. It also includes work from pyca/cryptography’s maintainers to support the other cryptographic backends. Sadly, this is not enough for a post-quantum migration drop-in swap. These primitives have different size, performance, and integration tradeoffs than the classical algorithms they replace.

## PQ algorithm tradeoffs

Post-quantum primitives keep the same security strength, but they change the size of the data on the wire. Public keys, signatures, and ciphertexts are often 1–2 orders of magnitude larger than the classical values they replace. The operations are also more complex and therefore slower, but on modern hardware they are still imperceptible for regular use, and are likely to get faster with improved hardware and algorithms.

For **signatures**, here’s how the classical primitive (Ed25519) compares to its post-quantum equivalent (ML-DSA-65):

| Algorithm | Public key | Private key | Output |
| --- | --- | --- | --- |
| Ed25519 | 32 B | 32 B | 64 B sig |
| **ML-DSA-65** | **1,952 B** | **32 B** | **3,309 B sig** |

And for **key exchange and encryption**, here’s how X25519 compares to its post-quantum equivalent (ML-KEM-768):

| Algorithm | Public key | Private key | Output |
| --- | --- | --- | --- |
| X25519 | 32 B | 32 B | 32 B shared |
| **ML-KEM-768** | **1,184 B** | **64 B** | **1,088 B ciphertext** |

If you maintain a protocol or wire format that hardcodes Ed25519-sized signatures or X25519-sized public keys, the post-quantum migration involves more than a primitive swap. The surrounding fields, length prefixes, and chunking assumptions need to grow with it.

## Using ML-DSA ([FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)): Quantum-resistant signatures

ML-DSA is the lattice-based signature scheme that replaces RSA, ECDSA, and Ed25519. The Python API mirrors the existing asymmetric primitives:

```
from cryptography.hazmat.primitives.asymmetric import mldsa

private_key = mldsa.MLDSA65PrivateKey.generate()
public_key = private_key.public_key()

signature = private_key.sign(b"message")
public_key.verify(signature, b"message")  # raises InvalidSignature on failure
```

## Using ML-KEM ([FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)): Key encapsulation for the post-quantum era

ML-KEM is a key encapsulation mechanism (KEM) for establishing shared secrets. The construction is different, though. ML-KEM is a key encapsulation mechanism, not a Diffie-Hellman exchange. Instead of both parties combining key shares to derive a shared secret, one party encapsulates a fresh shared secret to the receiver’s public key, and the receiver decapsulates it with the matching private key. These operations allow both parties to exchange a secret but in a manner fundamentally different from Diffie-Hellman, and resistant to quantum factoring attacks.

```
from cryptography.hazmat.primitives.asymmetric import mlkem

# Receiver generates a keypair and publishes the public key.
private_key = mlkem.MLKEM768PrivateKey.generate()
public_key = private_key.public_key()

# Sender encapsulates a fresh shared secret to that public key.
shared_secret_sender, ciphertext = public_key.encapsulate()

# Receiver decapsulates the same shared secret from the ciphertext.
shared_secret_receiver = private_key.decapsulate(ciphertext)
assert shared_secret_sender == shared_secret_receiver
```

## The road ahead: SLH-DSA and protocol integration

Two areas are still in progress: a third NIST standard, and the work of integrating these primitives into real protocols.

### SLH-DSA

SLH-DSA ([FIPS 205](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.205.pdf)) is NIST’s hash-based digital signature standard. Like ML-DSA, it is meant to replace classical signature schemes such as RSA, ECDSA, and Ed25519. Its tradeoff is different: SLH-DSA has very large signatures and slow signing, but it relies only on the security properties of hash functions, which have been studied for decades. That makes it a conservative backstop if future cryptanalysis weakens lattice-based signatures. SLH-DSA is not supported in `pyca/cryptography` 48, but we’ve started working on it.

### Post-quantum in protocols

Primitives are the foundation, but the post-quantum migration will be complete only when protocols use the post-quantum resistant algorithms. You’re unlikely to use PQ algorithms directly in tools like Certbot or Ansible until common protocols add support for them. While well-designed to replace existing implementations, algorithm changes require c...
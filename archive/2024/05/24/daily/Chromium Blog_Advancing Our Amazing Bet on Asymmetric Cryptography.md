---
title: Advancing Our Amazing Bet on Asymmetric Cryptography
url: http://blog.chromium.org/2024/05/advancing-our-amazing-bet-on-asymmetric.html
source: Chromium Blog
date: 2024-05-24
fetch_date: 2025-10-06T16:49:02.477502
---

# Advancing Our Amazing Bet on Asymmetric Cryptography

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [Advancing Our Amazing Bet on Asymmetric Cryptography](https://blog.chromium.org/2024/05/advancing-our-amazing-bet-on-asymmetric.html "Advancing Our Amazing Bet on Asymmetric Cryptography")

Thursday, May 23, 2024

Google and many other organizations, such as [NIST](https://csrc.nist.gov/projects/post-quantum-cryptography), [IETF](https://datatracker.ietf.org/group/tls/about/), and [NSA](https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/3148990/nsa-releases-future-quantum-resistant-qr-algorithm-requirements-for-national-se/), believe that migrating to post-quantum cryptography is important due to the large risk posed by a [cryptographically-relevant quantum computer](https://media.defense.gov/2021/Aug/04/2002821837/-1/-1/1/Quantum_FAQs_20210804.PDF) (CRQC). In [August](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html), we posted about how Chrome Security is working to protect users from the risk of future quantum computers by leveraging a new form of [hybrid post-quantum cryptographic key](https://datatracker.ietf.org/doc/draft-tls-westerbaan-xyber768d00/) exchange, Kyber (ML-KEM)[1](#fn1). We’re happy to announce that we have enabled the latest Kyber draft specification by default for TLS 1.3 and QUIC on all desktop Chrome platforms as of Chrome 124.[2](#fn2) This rollout revealed a number of previously-existing bugs in several TLS middlebox products. To assist with the deployment of fixes, Chrome is offering a temporary [enterprise policy to opt-out](https://chromeenterprise.google/policies/#PostQuantumKeyAgreementEnabled).

Launching opportunistic quantum-resistant key exchange is part of [Google’s broader strategy](https://bughunters.google.com/blog/5108747984306176/google-s-threat-model-for-post-quantum-cryptography) to prioritize deploying post-quantum cryptography in systems *today* that are at risk if an adversary has access to a quantum computer *in the future*. We believe that it’s important to inform standards with real-world experience, by implementing drafts and iterating based on feedback from implementers and early adopters. This iterative approach was a key part of developing QUIC and TLS 1.3. It’s part of why we’re launching this draft version of Kyber, and it informs our future plans for post-quantum cryptography.

Chrome’s post-quantum strategy prioritizes quantum-resistant key exchange in HTTPS, and increased [agility](https://www.chromium.org/Home/chromium-security/root-ca-policy/moving-forward-together/) in certificates from the Web PKI. While PKI agility may appear somewhat unrelated, its absence has contributed to significant delays in past cryptographic transitions and will continue to do so until we find a viable solution in this space. A more agile Web PKI is required to enable a secure and reliable transition to post-quantum cryptography on the web.

To understand this, let’s take a look at HTTPS and the current state of post-quantum cryptography. In the context of HTTPS, cryptography is primarily used in three different ways:

* **Symmetric Encryption/Decryption.** HTTP is transmitted as data inside a TLS connection using an authenticated cipher (AEAD) such as AES-GCM. These algorithms are [broadly considered safe](https://words.filippo.io/dispatches/post-quantum-age/) against quantum cryptanalysis and can remain in place.
* **Key Exchange.** Symmetric cryptography requires a secret key. Key exchange is a form of asymmetric cryptography in which two parties can mutually generate a shared secret key over a public channel. This secret key can then be used for symmetric encryption and decryption. All current forms of asymmetric key exchange standardized for use in TLS are vulnerable to quantum cryptanalysis.
* **Authentication**. In HTTPS, authentication is achieved primarily through the use of digital signatures, which are used to convey server identity, handshake authentication, and transparency for certificate issuance. All of the digital signature and public key algorithms standardized for authentication in TLS are vulnerable to quantum cryptanalysis.

This results in two separate quantum threats to HTTPS.

The first is the threat to traffic being generated *today*. An adversary could store encrypted traffic now, wait for a CRQC to be practical, and then use it to decrypt the traffic after the fact. This is commonly known as a [store-now-decrypt-later](https://en.wikipedia.org/wiki/Harvest_now%2C_decrypt_later) attack. This threat is relatively urgent, since it doesn’t matter when a CRQC is practical—the threat comes from storing encrypted data *now*. Defending against this attack requires the key exchange to be quantum resistant. Launching Kyber in Chrome enables servers to mitigate store-now-decrypt-later attacks.

The second threat is that *future* traffic is vulnerable to impersonation by a quantum computer. Once a CRQC actually exists, it could be used to break the asymmetric cryptography used for authentication in HTTPS. To defend against impersonation from a CRQC, we need to migrate all of the asymmetric cryptography used for authentication to post-quantum variants. However, breaking authentication only affects traffic generated **after** the availability of CRQCs. This is because breaking authentication on a recorded transcript doesn’t help the attacker impersonate either party—the conversation has already finished.

In other words, there’s no store-now-decrypt-later equivalent for authentication, and so while migrating key exchange and authentication to post-quantum variants are both *important*, migrating authentication is less *urgent* than key exchange. This is good, because there are a [variety of challenges](https://dadrian.io/blog/posts/pqc-signatures-2024/) for migrating to post-quantum authentication. Specifically, size.

Post-quantum cryptography is big compared to the pre-quantum cryptographic algorithms used in HTTPS. A Kyber key exchange is ~1KB transmitted per peer, whereas an X25519 key exchange is only 32 bytes per peer, an over 30x increase. The actual key exchange operation in Kyber is quite fast. Transmitting Kyber keys is quite slow. The extra size from Kyber causes the TLS ClientHello to be split into two packets, resulting in a 4% median latency increase to all TLS handshakes in Chrome on desktop. On desktop platforms, this, with HTTP/2 and HTTP/3 connection reuse, is not large enough to be noticeable in [Core Web Vitals](https://web.dev/articles/vitals). Unfortunately, it is noticeable on Android, where Internet connections are often lower bandwidth and higher latency, and so we have not yet launched on Android.

The size issues are even worse for authentication. ML-DSA (Dilithium) keys and signatures are ~40X the size of ECDSA keys and signatures. A typical TLS connection today uses two public keys and five signatures to fulfill all of the authentication requirements. A naive swap to ML-DSA would add ~14KB to the TLS handshake. [Cloudflare anticipates](https://blog.cloudflare.com/pq-2024) it would increase latency by 20-40%, and we’ve seen that a single kilobyte was already impactful. Instead, we need alternate approaches to authentication in HTTPS that provide the desired properties and transmit fewer signatures and public keys.

We think the important next step for quantum-resistant authentication in HTTPS is to focus on enabling *trust anchor agility*. Historically, the public Web PKI could not deploy new algorithms quickly. This is because most site operators typically provision a single certificate for all supported clients and browsers. This certificate must both be issued from a trust hierarchy that is trusted by every browser or...
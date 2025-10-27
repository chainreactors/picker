---
title: Real World Cryptography Conference 2023 – Part II
url: https://buaq.net/go-175421.html
source: unSafe.sh - 不安全
date: 2023-08-26
fetch_date: 2025-10-04T11:59:31.095920
---

# Real World Cryptography Conference 2023 – Part II

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Real World Cryptography Conference 2023 – Part II

After a brief interlude, filled with several articles from the Cryptography
*2023-8-25 21:0:0
Author: [research.nccgroup.com(查看原文)](/jump-175421.htm)
阅读量:19
收藏*

---

After a brief interlude, filled with [several](https://research.nccgroup.com/2023/07/24/building-intuition-for-lattice-based-signatures-part-1-trapdoor-signatures/) [articles](https://research.nccgroup.com/2023/06/23/exploiting-noisy-oracles-with-bayesian-inference/) [from](https://research.nccgroup.com/2023/06/09/machine-learning-104-breaking-aes-with-power-side-channels/) [the](https://research.nccgroup.com/2023/06/02/how-to-spot-and-prevent-an-eclipse-attack/) [Cryptography](https://research.nccgroup.com/2023/06/01/eurocrypt-2023-death-of-a-kem/) [Services](https://research.nccgroup.com/2023/05/19/the-paillier-cryptosystem-with-applications-to-threshold-ecdsa/) [team](https://research.nccgroup.com/2023/05/18/rigging-the-vote-uniqueness-in-verifiable-random-functions/), we’re back with our final thoughts from this year’s Real World Cryptography Conference. In case you missed it, [check out Part I for more insights.](https://research.nccgroup.com/2023/05/10/real-world-cryptography-conference-2023-part-i/)

1. [Interoperability in E2EE Messaging](#Interoperability-in-E2EE-Messaging)
2. [Threshold ECDSA Towards Deployment](#Threshold-ECDSA-Towards-Deployment)
3. [The Path to Real World FHE: Navigating the Ciphertext Space](#The-Path-to-Real-World-FHE)
4. [High-Assurance Go Cryptography in Practice](#High-Assurance-Go-Cryptography)

A specter is haunting Europe – the specter of platform interoperability. The EU signed the Digital Market Acts (DMA) into law in September of last year, mandating chat platforms provide support for interoperable communications. This requirement will be in effect by March of 2024, an aggressive timeline requiring fast action from cryptographic (and regular) engineers. There are advantages to interoperability. It allows users to communicate with their friends and family across platforms, and it allows developers to build applications that work across platforms. There is the potential for this to partially mitigate the network effects associated with platform lock-in, which could lead to more competition and greater freedom of choice for end users. However, interoperability requires shared standards, and standards tend to imply compromise. This is a particularly severe challenge with secure chat apps which aim to provide their users with high levels of security. Introducing hastily designed, legislatively mandated components into these systems is a high-risk change which, in the worst case, could introduce weaknesses which, if introduced, would be difficult to fix (due to the effects of lock-in and the corresponding level of coordination and engineering effort required). This is further complicated by the heterogeneity of the field in regard to end-to-end encrypted chat: E2EE protocols vary by ciphersuite, level and form of authentication, personal identifier (email, phone number, username/password, etc.), and more. Any standardized design for interoperability would need to be able to manage all this complexity. This presentation on work by Ghosh, Grubbs, Len, and Rösler discussed one effort at introducing such a standard for interoperability between E2EE chat apps, focused on extending existing components of widely used E2EE apps. This is appropriate as these apps are most likely to be identified as “gatekeeper” apps to which the upcoming regulations apply in force. The proposed solution uses server-to-server interoperability, in which each end user is only required to directly communicate with their own messaging provider. Three main components of messaging affected by the DMA are identified: identity systems, E2EE protocols, and abuse prevention.

* For the first of these items, a system for running encrypted queries to remote providers’ identity systems is proposed; this allows user identities to be associated with keys in such a way that the actual identity data is abstracted and thus could be an email, a phone number, or an arbitrary string.
* For the second issue, E2EE encryption, a number of simple solutions are considered and rejected; the final proposal has several parts. Sender-anonymous wrappers are proposed, using a variant of the Secure Sender protocol from Signal, to hide sender metadata; for encryption in transit, non-gatekeeper apps can use an encapsulated implementation of a gatekeeper app’s E2EE through a *client bridge*. This provides both confidentiality and authenticity, while minimizing metadata leakage.
* For the third issue, abuse prevention, a number of options (including “doing nothing” are again considered and rejected). The final design is somewhat nonobvious, and consists of server-side spam filtering, user reporting (via asymmetric message franking, one of the more cryptographically fresh and interesting parts of the system), and blocklisting (which requires a small data leakage, in that the initiator would need to share the blocked party’s user ID with their own server).

Several open problems were also identified (these points are quoted directly from the slides):

* How do we improve the privacy of interoperable E2EE by reducing metadata leakage?
* How do we extend other protocols used in E2EE messaging, like key transparency, into the interoperability setting?
* How do we extend our framework and analyses to group chats and encrypted calls?

This is important and timely work on a topic which has the potential to result in big wins for user privacy and user experience; however, this best-case scenario will only play out if players in industry and academia can keep pace with the timeline set by the DMA. This requires quick work to design, implement, and review these protocols, and we look forward to seeing how these systems take shape in the months to come.

– *Eli Sohl*

A Threshold Signature Scheme (TSS) allows any sufficiently large subset of signers to cryptographically sign a message. There has been a flurry of research in this area in the last 10 years, driven partly by financial institutions’ needs to secure crypto wallets and partly by academic interest in the area from the Multiparty Computation (MPC) perspective. Some signature schemes are more amenable to “thresholding” than others. For example, due to linearity features of “classical” Schnorr signatures, Schnorr is more amenable to “thresholding” than ECDSA (see the FROST protocol in this context). As for thresholding ECDSA, there are tradeoffs as well; if one allows using cryptosystems such as Pallier’s, the overall protocol complexity drops, but speed and extraneous security model assumptions appear to suffer. The DKLS papers, listed below, aim for competitive speeds and minimizing necessary security assumptions:

* [DKLS18](https://eprint.iacr.org/2018/499): “Secure Two-party Threshold ECDSA from ECDSA Assumptions”, Jack Doerner, Yashvanth Kondi, Eysa Lee, abhi shelat
* [DKLS19](https://eprint.iacr.org/2019/523): “Secure Multi-party Threshold ECDSA from ECDSA Assumptions”, Jack Doerner, Yashvanth Kondi, Eysa Lee, abhi shelat

The first paper proposes a *2-out-of-n* ECDSA scheme, whereas the second paper extends it to the *t-out-of-n* case. The DKLS 2-party multiplication algorithm is based on Oblivious Transfer (OT) together with a number of optimization techniques. The OT is batched, then further sped up by an OT Extension (a way to reduce a large number of OTs to a smaller number of OTs using symmetric key cryptography) and finally used to multiply in a thresh...
---
title: Toward Quantum Resilient Security Keys
url: http://security.googleblog.com/2023/08/toward-quantum-resilient-security-keys.html
source: Google Online Security Blog
date: 2023-08-16
fetch_date: 2025-10-04T11:59:23.998115
---

# Toward Quantum Resilient Security Keys

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Toward Quantum Resilient Security Keys](https://security.googleblog.com/2023/08/toward-quantum-resilient-security-keys.html "Toward Quantum Resilient Security Keys")

August 15, 2023

Elie Bursztein, cybersecurity and AI research director, Fabian Kaczmarczyck, software engineer

As part of our effort to deploy quantum resistant cryptography, we are happy to announce the [release](https://github.com/google/OpenSK/releases/tag/hybrid-pqc) of the first quantum resilient FIDO2 security key implementation as part of OpenSK, our open source security key firmware. This open-source hardware optimized implementation uses a novel ECC/Dilithium hybrid signature schema that benefits from the security of ECC against standard attacks and Dilithium’s resilience against quantum attacks. This schema was co-developed in partnership with the [ETH Zürich](https://ee.ethz.ch/) and won the [ACNS secure cryptographic implementation workshop best paper](https://sulab-sever.u-aizu.ac.jp/ACNS2023/awards.html).

![Quantum processor](https://lh6.googleusercontent.com/3piifFuKJAHB9mH26mi2VrdNlwl_lKv3UVnZbA78aPAhINmYza4MnqXHhm_1jHJn010uk63tuhkUXfTHswzxQ3KWgp8iVwgHMLQ8jgQuJbbMzV1tkMt1N8rT4wiuwz3wSXfy0ZrTcF1xlwmwBFSZcM_va4gQCnnaIAq15jIFyN8eemoAFmJItWj1gI0OnDMVczT7xKdi5txnI9MDtN7qVU4pFatlQnRsLY7mjg)

Quantum processor

As [progress](https://blog.google/technology/research/an-important-step-towards-improved-quantum-computers/) toward practical quantum computers is accelerating, preparing for their advent is becoming a more pressing issue as time passes. In particular, standard public key cryptography which was designed to protect against traditional computers, will not be able to withstand quantum attacks. Fortunately, with the [recent standardization](https://csrc.nist.gov/News/2022/pqc-candidates-to-be-standardized-and-round-4) of public key quantum resilient cryptography including the [Dilithium algorithm](https://pq-crystals.org/dilithium/), we now have a clear path to secure security keys against quantum attacks.

While quantum attacks are still in the distant future, deploying cryptography at Internet scale is a massive undertaking which is why doing it as early as possible is vital. In particular, for security keys this process is expected to be gradual as users will have to acquire new ones once FIDO has standardized post quantum cryptography resilient cryptography and this new standard is supported by major browser vendors.

![Hybrid signature scheme](https://lh3.googleusercontent.com/lS1UVVErSSJ4ZdsrcStziLa1Ntl7PoHTq-ZrtvXNHo5nkg4WtQhFeyvKlU_kEX7VE2pRw2ZDob8Q-f0Pda8H9-jW8_N6NF8-8Wm-BDQbrtCcm4eExDzQ4kp9VA2bKyhjvrqrkkkN-5_i_jJc_gEP8SMO8C8aLpypyUz96oFzhTzcsBhRuRZWvMXnmLk4o1BZ-Jwv2f4mxhlcVbeCxj4NGVWLG_brFH6my7HZHg)

Hybrid signature: Strong nesting with classical and PQC scheme

Our proposed implementation relies on a hybrid approach that combines the battle tested ECDSA signature algorithm and the recently standardized quantum resistant signature algorithm, [Dilithium](https://pq-crystals.org/dilithium/index.shtml). In collaboration with ETH, we developed this novel hybrid signature schema that offers the best of both worlds. Relying on a hybrid signature is critical as the security of Dilithium and other recently standardized quantum resistant algorithms haven’t yet stood the test of time and recent [attacks on Rainbow](https://eprint.iacr.org/2020/1343) (another quantum resilient algorithm) demonstrate the need for caution. This cautiousness is particularly warranted for security keys as most can’t be upgraded – although we are working toward it for [OpenSK](https://github.com/google/OpenSK/blob/develop/docs/boards/nrf52840dk.md#upgradability). The hybrid approach is also used in other post-quantum efforts like [Chrome’s support for TLS](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html).

On the technical side, a large challenge was to create a Dilithium implementation small enough to run on security keys’ constrained hardware. Through careful optimization, we were able to develop a Rust memory optimized implementation that only required 20 KB of memory, which was sufficiently small enough. We also spent time ensuring that our implementation signature speed was well within the expected security keys specification. That said, we believe improving signature speed further by leveraging hardware acceleration would allow for keys to be more responsive.

Moving forward, we are hoping  to see this implementation (or a variant of it), being standardized as part of the FIDO2 key specification and supported by major web browsers so that users' credentials can be protected against quantum attacks. If you are interested in testing this algorithm or contributing to security key research, head to our open source implementation [OpenSK](https://github.com/google/OpenSK).

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://draft.blogger.com/comment/fullpage/post/1176949257541686127/490519433601899320)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/08/ai-powered-fuzzing-breaking-bug-hunting.html "Newer Post")

[**](https://security.googleblog.com/2023/08/making-chrome-more-secure-by-bringing.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security](https://security.googleblog.com/search/label/chrome%20security)
* [connected devices](https://security.googleblog.com/search/label/connected%20devices)
* [CTF](https://security.googleblog.com/search/label/CTF)
* [diversity](https://security.googleblog.com/search/label/diversity)
* [encryption](https://security.googleblog.com/search/label/encryption)
* [federated learning](https://security.googleblog.com/search/label/federated%20learning)
* [fuzzing](https://security.googleblog.com/search/label/fuzzing)
* [Gboard](https://security.googleblog.com/search/label/Gboard)
* [google play](https://security.googleblog.com/search/label/google%20play)
* [google play protect](https://security.googleblog.com/search/label/google%20play%20protect)
* [hacking](https://security.googleblog.com/search/label/hacking)
* [interoperability](https://security.googleblog.com/search/label/interoperability)
* [iot security](https://security.googleblog.com/search/label/iot%20security)
* [kubernetes](https://security.googleblog.com/search/label/kubernetes)
* [linux kernel](https://security.googleblog....
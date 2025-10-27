---
title: Google Chrome Switches to ML-KEM for Post-Quantum Cryptography Defense
url: https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html
source: The Hacker News
date: 2024-09-18
fetch_date: 2025-10-06T18:29:25.297891
---

# Google Chrome Switches to ML-KEM for Post-Quantum Cryptography Defense

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Google Chrome Switches to ML-KEM for Post-Quantum Cryptography Defense](https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html)

**Sep 17, 2024**Ravie LakshmananBrowser Security / Quantum Computing

[![Post-Quantum Cryptography Defense](data:image/png;base64... "Post-Quantum Cryptography Defense")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgozGxO5Xh0pP0FPDVw-eKlkSsrp9EjNB6oCpqsTBCVW8dEWV1GwpJK0oyqtUSrnPAj6SFYLDNk-3zgQDn1zirEkqQLmXFm-orQrGqI1TFL4nba_TvTDuMJKb2rNp5LTCNhEaFFjECNP9IEYVwL8m54A0_bGdzY8uKSn_DYFF4FSUldRnOgYCpXYrZEhs7n/s790-rw-e365/chrome.png)

Google has announced that it will be switching from KYBER to ML-KEM in its Chrome web browser as part of its ongoing efforts to defend against the risk posed by cryptographically relevant quantum computers ([CRQCs](https://security.googleblog.com/2024/08/post-quantum-cryptography-standards.html)).

"Chrome will offer a key share prediction for hybrid ML-KEM (codepoint 0x11EC)," David Adrian, David Benjamin, Bob Beck, and Devon O'Brien of the Chrome Team [said](https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html). "The PostQuantumKeyAgreementEnabled flag and [enterprise policy](https://chromeenterprise.google/policies/#PostQuantumKeyAgreementEnabled) will apply to both Kyber and ML-KEM."

The changes are expected to take effect in Chrome version 131, which is [on track for release](https://chromiumdash.appspot.com/schedule) in early November 2024. Google noted that the two hybrid post-quantum key exchange approaches are essentially incompatible with each other, prompting it to abandon KYBER.

"The changes to the final version of ML-KEM make it incompatible with the previously deployed version of Kyber," the company said. "As a result, the codepoint in TLS for hybrid post-quantum key exchange is changing from 0x6399 for Kyber768+X25519, to 0x11EC for ML-KEM768+X25519."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The development comes shortly after the U.S. National Institute of Standards and Technology (NIST) [published](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) the final versions of the [three new encryption algorithms](https://www.federalregister.gov/documents/2024/08/14/2024-17956/announcing-issuance-of-federal-information-processing-standards-fips-fips-203-module-lattice-based) to secure current systems against future attacks using quantum technologies, marking the culmination of an eight-year effort from the agency.

The algorithms in question are [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) (aka ML-KEM), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) (aka CRYSTALS-Dilithium or ML-DSA), and [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) (aka Sphincs+ or SLH-DSA), which allow for general encryption and protecting digital signatures. A fourth algorithm, [FN-DSA](https://csrc.nist.gov/presentations/2024/crclub-2024-08-07) (originally called FALCON), is slated for finalization later this year.

ML-KEM, short for Module-Lattice-based Key-Encapsulation Mechanism, is derived from the round-three version of the [CRYSTALS-KYBER](https://thehackernews.com/2022/07/nist-announces-first-four-quantum.html) KEM and can be used to establish a shared secret key between two parties communicating over a public channel.

Microsoft, for its part, is also readying for a post-quantum world by announcing an update to its [SymCrypt](https://github.com/microsoft/SymCrypt) cryptographic library with support for ML-KEM and eXtended Merkle Signature Scheme ([XMSS](https://www.rfc-editor.org/info/rfc8391)).

"Adding post-quantum algorithm support to the underlying crypto engine is the first step towards a quantum safe world," the Windows maker [said](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/microsoft-s-quantum-resistant-cryptography-is-here/ba-p/4238780), stating the [transition to post-quantum cryptography](https://engineering.fb.com/2024/05/22/security/post-quantum-readiness-tls-pqr-meta/) (PQC) is a "complex, multi-year and iterative process" that requires careful planning.

The disclosure also follows the discovery of a cryptographic flaw in the Infineon SLE78, Optiga Trust M, and Optiga TPM security microcontrollers that could allow for the extraction of Elliptic Curve Digital Signature Algorithm (ECDSA) private keys from YubiKey hardware authentication devices.

The cryptographic flaw within the Infineon-supplied library is believed to have remained unnoticed for 14 years and about 80 highest-level Common Criteria certification evaluations.

The side-channel attack, dubbed **EUCLEAK** (CVE-2024-45678, CVSS score: 4.9) by NinjaLab's Thomas Roche, affects all Infineon security microcontrollers embedding the cryptographic library and the following YubiKey devices -

* YubiKey 5 Series versions prior to 5.7
* YubiKey 5 FIPS Series prior to 5.7
* YubiKey 5 CSPN Series prior to 5.7
* YubiKey Bio Series versions prior to 5.7.2
* Security Key Series all versions prior to 5.7
* YubiHSM 2 versions prior to 2.4.0
* YubiHSM 2 FIPS versions prior to 2.4.0

"The attacker would need physical possession of the YubiKey, Security Key, or YubiHSM, knowledge of the accounts they want to target, and specialized equipment to perform the necessary attack," Yubico, the company behind YubiKey, [said](https://www.yubico.com/support/security-advisories/ysa-2024-03/) in a coordinated advisory.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Depending on the use case, the attacker may also require additional knowledge including username, PIN, account password, or [YubiHSM] authentication key."

But because existing YubiKey devices with vulnerable firmware versions can't be updated – an intentional design choice meant to maximize security and avoid introducing new vulnerabilities – they are permanently susceptible to EUCLEAK.

The company has since...
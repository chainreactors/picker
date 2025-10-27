---
title: Google Cloud KMS Adds Quantum-Safe Digital Signatures to Defend Against Future Threats
url: https://thehackernews.com/2025/02/google-cloud-kms-adds-quantum-safe.html
source: The Hacker News
date: 2025-02-25
fetch_date: 2025-10-06T20:55:44.981777
---

# Google Cloud KMS Adds Quantum-Safe Digital Signatures to Defend Against Future Threats

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

# [Google Cloud KMS Adds Quantum-Safe Digital Signatures to Defend Against Future Threats](https://thehackernews.com/2025/02/google-cloud-kms-adds-quantum-safe.html)

**Feb 24, 2025**Ravie LakshmananCloud Security / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7ozRguTOcW25S1mF3bx7y61U_i4K03Bx9MBTgrvhgqQSENc60Wy7qTusuvTJQyZ3rTGp-IJELumgXRy15lC5BJAuIGTwfdCzRLtzehklXBpkAPA8bMtM2fPVPfxSPTuVBM_s0IBPBeMyMULtI9Z6EUVPwI6jAkVHpT3k8zx56I2fRkbNcpsdRjgv70xzM/s790-rw-e365/google.png)

Google Cloud has announced quantum-safe digital signatures in Google Cloud Key Management Service ([Cloud KMS](https://cloud.google.com/kms/docs/)) for software-based keys as a way to bulletproof encryption systems against the threat posed by cryptographically-relevant quantum computers.

The feature, currently in preview, coexists with the National Institute of Standards and Technology's (NIST) post-quantum cryptography (PQC) standards, the final versions of which were [formalized](https://thehackernews.com/2024/09/google-chrome-switches-to-ml-kem-for.html) in August 2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Our Cloud KMS PQC roadmap includes support for the NIST post-quantum cryptography standards (FIPS 203, FIPS 204, FIPS 205, and future standards), in both software (Cloud KMS) and hardware (Cloud HSM)," the company's cloud division [noted](https://cloud.google.com/blog/products/identity-security/announcing-quantum-safe-digital-signatures-in-cloud-kms).

"This can help customers perform quantum-safe key import and key exchange, encryption and decryption operations, and digital signature creation."

The tech giant said its underlying software implementations of these standards – FIPS 203 (aka ML-KEM), FIPS 204 (aka CRYSTALS-Dilithium or ML-DSA), and FIPS 205 (aka Sphincs+ or SLH-DSA) – would be available as open-source software.

Furthermore, it's working with Hardware Security Module (HSM) vendors and Google Cloud External Key Manager (EKM) partners to enable quantum-safe cryptography across the platform.

By adopting PQC early on, the idea is to secure systems against a threat called Harvest Now, Decrypt Later ([HNDL](https://thehackernews.com/2024/05/zoom-adopts-nist-approved-post-quantum.html)) that involves threat actors harvesting encrypted sensitive data today with the goal of decrypting them at some point in the future when a quantum computer powerful enough to break existing key exchange protocols and algorithms become a reality.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"While that future may be years away, those deploying long-lived roots-of-trust or signing firmware for devices managing critical infrastructure should consider mitigation options against this threat vector now," Google Cloud's Jennifer Fernick and Andrew Foster said.

"The sooner we're able to secure these signatures, the more resilient the digital world's foundation of trust becomes."

Quantum-safe digital signatures in Cloud KMS is available in preview for both ML-DSA-65 (FIPS 204) and SLH-DSA-SHA2-128S (FIPS 205), with API support for hybridization schemes planned for future rollout if the cryptographic community arrives at a broader consensus.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[Digital Signatures](https://thehackernews.com/search/label/Digital%20Signatures)[encryption](https://thehackernews.com/search/label/encryption)[Google Cloud](https://thehackernews.com/search/label/Google%20Cloud)[Key Management](https://thehackernews.com/search/label/Key%20Management)[Post-Quantum Cryptography](https://thehackernews.com/search/label/Post-Quantum%20Cryptography)[Threat Mitigation](https://thehackernews.com/search/label/Threat%20Mitigation)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Pe...
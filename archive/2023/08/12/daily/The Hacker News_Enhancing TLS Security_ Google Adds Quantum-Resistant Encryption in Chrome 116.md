---
title: Enhancing TLS Security: Google Adds Quantum-Resistant Encryption in Chrome 116
url: https://thehackernews.com/2023/08/enhancing-tls-security-google-adds.html
source: The Hacker News
date: 2023-08-12
fetch_date: 2025-10-04T12:03:42.865693
---

# Enhancing TLS Security: Google Adds Quantum-Resistant Encryption in Chrome 116

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

# [Enhancing TLS Security: Google Adds Quantum-Resistant Encryption in Chrome 116](https://thehackernews.com/2023/08/enhancing-tls-security-google-adds.html)

**Aug 11, 2023**Ravie LakshmananEncryption / Browser Security

[![Quantum-Resistant Encryption](data:image/png;base64... "Quantum-Resistant Encryption")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ4fmBqTDrYWnhNBGw02TXV7n2bb9hPS8V8Rsx7VKh60N_vI_Crx0y4wCF__KlibJgMjlj6ldQRjbpkrrMtW8jrHUkQMoX1UAvhEGP1x8TTUYPY52md5CNfG4z3KvuqmpYDBPNLqX-l-l5IXypRvrKPg_0CRWlVUzkqVSy508u0gtlm4LBxbKX4LbT790z/s790-rw-e365/chrome.jpg)

Google has announced plans to add support for quantum-resistant encryption algorithms in its Chrome browser, starting with version 116.

"Chrome will begin supporting [X25519Kyber768](https://www.ietf.org/archive/id/draft-tls-westerbaan-xyber768d00-02.html) for establishing symmetric secrets in [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security), starting in Chrome 116, and available behind a flag in Chrome 115," Devon O'Brien [said](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html) in a post published Thursday.

Kyber was [chosen](https://thehackernews.com/2022/07/nist-announces-first-four-quantum.html) by the U.S. Department of Commerce's National Institute of Standards and Technology (NIST) as the candidate for general encryption in a bid to tackle future cyber attacks posed by the advent of quantum computing. [Kyber-768](https://pq-crystals.org/kyber/index.shtml) is roughly the security equivalent of [AES-192](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The encryption algorithm has already been adopted by [Cloudflare](https://blog.cloudflare.com/experiment-with-pq/), [Amazon Web Services](https://aws.amazon.com/blogs/security/round-2-post-quantum-tls-is-now-supported-in-aws-kms/), and IBM.

X25519Kyber768 is a hybrid algorithm that combines the output of [X25519](https://www.rfc-editor.org/rfc/rfc7748), an elliptic curve algorithm widely used for key agreement in TLS, and Kyber-768 to create a strong session key to encrypt TLS connections.

"Hybrid mechanisms such as X25519Kyber768 provide the flexibility to deploy and test new quantum-resistant algorithms while ensuring that connections are still protected by an existing secure algorithm," O'Brien explained.

While it's expected to take several years, possibly even decades, for quantum computers to pose severe risks, certain kinds of encryption are susceptible to an attack called "[harvest now, decrypt later](https://en.wikipedia.org/wiki/Harvest_now%2C_decrypt_later)" (aka retrospective decryption) in which data that's encrypted today is harvested by threat actors in hopes of decrypting it later when cryptanalysis becomes easier due to technological breakthroughs.

This is where quantum computers come in, as they are capable of efficiently performing certain computations in a manner that can trivially defeat existing cryptographic implementations.

"In TLS, even though the symmetric encryption algorithms that protect the data in transit are considered safe against quantum cryptanalysis, the way that the symmetric keys are created is not," O'Brien said.

"This means that in Chrome, the sooner we can update TLS to use quantum-resistant session keys, the sooner we can protect user network traffic against future quantum cryptanalysis."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Organizations that face network appliance incompatibility issues following the rollout are advised to disable X25519Kyber768 in Chrome using the [PostQuantumKeyAgreementEnabled](https://chromeenterprise.google/policies/#PostQuantumKeyAgreementEnabled) enterprise policy, which is available starting in Chrome 116, as a temporary measure.

The development comes as Google said it's changing the release cadence of Chrome security updates from bi-weekly to weekly to minimize the attack window and address the growing patch gap problem that allows threat actors more time to weaponize published n-day and zero-day flaws.

"Bad actors could possibly take advantage of the visibility into these fixes and develop exploits to apply against browser users who haven't yet received the fix," Amy Ressler from the Chrome Security Team [said](https://security.googleblog.com/2023/08/an-update-on-chrome-security-updates.html). "That's why we believe it's really important to ship security fixes as soon as possible, to minimize this 'patch gap.'"

It also follows the company's decision to enforce [key pinning](https://security.googleblog.com/2023/08/making-chrome-more-secure-by-bringing.html) by default in Chrome 106 for Android, released in September 2022, as a layer of defense to secure users against certificate authority (CA) compromise.

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

[browser security](https://thehackernews.com/search/label/browser%20security)[Chrome](https://thehackernews.com/search/label/Chrome)[encryption](https://thehackernews.com/search/label/encryption)[Google](https://thehackernews.com/search/label/Google)[network security](ht...
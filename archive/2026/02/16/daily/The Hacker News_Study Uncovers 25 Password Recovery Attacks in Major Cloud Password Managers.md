---
title: Study Uncovers 25 Password Recovery Attacks in Major Cloud Password Managers
url: https://thehackernews.com/2026/02/study-uncovers-25-password-recovery.html
source: The Hacker News
date: 2026-02-16
fetch_date: 2026-02-17T04:21:51.304746
---

# Study Uncovers 25 Password Recovery Attacks in Major Cloud Password Managers

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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Study Uncovers 25 Password Recovery Attacks in Major Cloud Password Managers](https://thehackernews.com/2026/02/study-uncovers-25-password-recovery.html)

**Ravie Lakshmanan**Feb 16, 2026Vulnerability / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBPbskdafjFepjzUnEOcPNFvk1UceqE9lVwhurVxvrqJ3_1VhbKg-XcZjTrVpt2aqk_uv6Sodg9NMcoTvkVEeoAhNUU9X_0ltI9oHpnTIA-a28iDGnudnxJklcADpfz5llcUEStKI7Nt7IjW3vhA_DyO7rKG03dgj8KTFfrpxamTqy7xEciFwLzeS-lXEb/s1700-e365/password-managers.jpg)

A new study has [found](https://ethz.ch/en/news-and-events/eth-news/news/2026/02/password-managers-less-secure-than-promised.html) that multiple cloud-based password managers, including Bitwarden, Dashlane, and LastPass, are susceptible to password recovery attacks under certain conditions.

"The attacks range in severity from integrity violations to the complete compromise of all vaults in an organization," researchers Matteo Scarlata, Giovanni Torrisi, Matilda Backendal, and Kenneth G. Paterson [said](https://zkae.io). "The majority of the attacks allow the recovery of passwords."

It's worth noting that the threat actor, per the study from ETH Zurich and Università della Svizzera italiana, supposes a malicious server and aims to examine the password manager's zero-knowledge encryption (ZKE) promises made by the three solutions. ZKE is a cryptographic technique that allows one party to prove knowledge of a secret to another party without actually revealing the secret itself.

ZKE is also a little different from end-to-end encryption (E2EE). While E2EE refers to a method of securing data in transit, ZKE is mainly about storing data in an encrypted format such that only the person with the key can access that information. Password manager vendors are known to implement ZKE to "enhance" user privacy and security by ensuring that the vault data cannot be tampered with.

However, the latest research has uncovered 12 distinct attacks against Bitwarden, seven against LastPass, and six against Dashlane, ranging from integrity violations of targeted user vaults to a total compromise of all the vaults associated with an organization. Collectively, these password management solutions serve over 60 million users and nearly 125,000 businesses.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"Despite vendors' attempts to achieve security in this setting, we uncover several common design anti-patterns and cryptographic misconceptions that resulted in vulnerabilities," the researchers said in an accompanying paper.

The attacks fall under four broad categories -

* Attacks that exploit the "Key Escrow" account recovery mechanism to compromise the confidentiality guarantees of Bitwarden and LastPass, resulting from vulnerabilities in their key escrow designs.
* Attacks that exploit flawed item-level encryption -- i.e., encrypting data items and sensitive user settings as separate objects and often combine with unencrypted or unauthenticated metadata, to result in integrity violations, metadata leakage, field swapping, and key derivation function ([KDF](https://en.wikipedia.org/wiki/Key_derivation_function)) downgrade.
* Attacks that exploit sharing features to compromise vault integrity and confidentiality.
* Attacks that exploit backwards compatibility with legacy code that result in downgrade attacks in Bitwarden and Dashlane.

The study also found that 1Password, another popular password manager, is vulnerable to both item-level vault encryption and sharing attacks. However, 1Password has opted to treat them as arising from already known architectural limitations.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaXS3vUuMd4jGNj1mDrOFc-Jo8_DsbYaQRaXCMl9t11C53ZmQ9WiSY6U5rs7ufndVsqh0BvV8XljNn-ZsGeUBpd7JZxFZzpMh_bPt4tgpmE80nIA5F7i-K4iw77n1IXIt-qzlS_nu5s3C7D0Zh5eUUypkv4Lk8xgMZrVykfhU1RCvwwdcby9Gnqw1EvZ3T/s1700-e365/password.jpg) |
| Summary of attacks (BW stands for Bitwarden, LP for LastPass, and DL for Dashlane) |

When reached for comment, Jacob DePriest, Chief Information Security Officer and Chief Information Officer at 1Password, told The Hacker News that the company's security reviewed the paper in detail and found no new attack vectors beyond those already documented in its publicly available [Security Design White Paper](https://agilebits.github.io/security-design/).

"We are committed to continually strengthening our [security architecture](https://support.1password.com/1password-security/) and evaluating it against advanced threat models, including malicious-server scenarios like those described in the research, and evolving it over time to maintain the protections our users rely on," DePriest added.

"For example, 1Password uses [Secure Remote Password](https://support.1password.com/secure-remote-password/) (SRP) to authenticate users without transmitting encryption keys to our servers, helping mitigate entire classes of server-side attacks. More recently, we introduced a [new capability](https://support.1password.com/cs/dns-record/) for enterprise-managed credentials, which from the start are created and secured to withstand sophisticated threats."

As for the rest, Bitwarden, Dashlane, and LastPass have all implemented countermeasures to mitigate the risks highlighted in the research, with LastPass also planning to harden its admin password reset and sharing workflows to counter the threat posed by a malicious intermediary. There is no evidence that any of these issues has been exploited in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

Specifically, Dashlane has patched an issue where a successful compromise of its servers could have allowed a downgrade of the encryption model used to generate encryption keys and protect user vaults. The issue was fixed by removing support for legacy cryptograph...
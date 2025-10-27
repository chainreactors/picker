---
title: Researchers Discover Severe Security Flaws in Major E2EE Cloud Storage Providers
url: https://thehackernews.com/2024/10/researchers-discover-severe-security.html
source: The Hacker News
date: 2024-10-22
fetch_date: 2025-10-06T18:56:02.137697
---

# Researchers Discover Severe Security Flaws in Major E2EE Cloud Storage Providers

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

# [Researchers Discover Severe Security Flaws in Major E2EE Cloud Storage Providers](https://thehackernews.com/2024/10/researchers-discover-severe-security.html)

**Oct 21, 2024**Ravie LakshmananEncryption / Data Protection

[![Major E2EE Cloud Storage Providers](data:image/png;base64... "Major E2EE Cloud Storage Providers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaY6R2rVsNFmbHbg9FJOHVDgZWEDjh5n8gFS0AVGlT1MgYYvO8Y_hx8DSgfcj2w0ru-ZGw4rdJNWcRkD5OqNtBEKrq3xTu6ahVVi8b77xoTHT92H5jqzFWiUBCwPPOl4MMudIreDKRlE_V_pg0uD9450Joei42LStBd_hR-qN_yJyy8Z2R3EeF7dVTZslC/s790-rw-e365/cloudkeys.png)

Cybersecurity researchers have discovered severe cryptographic issues in various end-to-end encrypted (E2EE) cloud storage platforms that could be exploited to leak sensitive data.

"The vulnerabilities range in severity: in many cases a malicious server can inject files, tamper with file data, and even gain direct access to plaintext," ETH Zurich researchers Jonas Hofmann and Kien Tuong Truong [said](https://brokencloudstorage.info/). "Remarkably, many of our attacks affect multiple providers in the same way, revealing common failure patterns in independent cryptographic designs."

The identified weaknesses are the result of an analysis of five major providers such as Sync, pCloud, Icedrive, Seafile, and Tresorit. The devised attack techniques hinge on a malicious server that's under an adversary's control, which could then be used to target the service providers' users.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A brief description of the flaws uncovered in the cloud storage systems is as follows -

* Sync, in which a malicious server could be used to break the confidentiality of uploaded files, as well as injecting files and tampering with their content

* pCloud, in which a malicious server could be used to break the confidentiality of uploaded files, as well as injecting files and tampering with their content

* Seafile, in which a malicious server could be used to speed-up brute-forcing of user passwords, as well as injecting files and tampering with their content

* Icedrive, in which a malicious server could be used to break the integrity of uploaded files, as well as injecting files and tampering with their content

* Tresorit, in which a malicious server could be used to present non-authentic keys when sharing files and to tamper with some metadata in the storage

[![Cloud Storage Providers](data:image/png;base64... "Cloud Storage Providers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif_FkMMRZRuYz5lQlHO4mOLSeJNem7dpudnLvnvdIm9kosyJwqAieKuj-M7lNmdCZDYAOTbfLjTfTdhFhwIv3_yRvOFSZIp1iNwZ24yfPcn0kxBSdTrLywat_TFgEcoKGcZ8yzCgtbEJVlehcP9PmMxTJCfQE4peFsTyPmQsEGwoMvnwt10vUR-74EwCIE/s790-rw-e365/Screenshot.png)

These attacks fall into one of the 10 broad classes that violate confidentiality, target file data and metadata, and allow for injection of arbitrary files -

* Lack of authentication of user key material (Sync and pCloud)
* Use of unauthenticated public keys (Sync and Tresorit)
* Encryption protocol downgrade (Seafile),
* Link-sharing pitfalls (Sync)
* Use of unauthenticated encryption modes such as CBC (Icedrive and Seafile)
* Unauthenticated chunking of files (Seafile and pCloud)
* Tampering with file names and location (Sync, pCloud, Seafile, and Icedrive)
* Tampering with file metadata (impacts all five providers)
* Injection of folders into a user's storage by combining the metadata-editing attack and exploiting a quirk in the sharing mechanism (Sync)
* Injection of rogue files into a user's storage (pCloud)

"Not all of our attacks are sophisticated in nature, which means that they are within reach of attackers who are not necessarily skilled in cryptography. Indeed, our attacks are highly practical and can be carried out without significant resources," the researchers said in an accompanying paper.

"Additionally, while some of these attacks are not novel from a cryptographic perspective, they emphasize that E2EE cloud storage as deployed in practice fails at a trivial level and often does not require more profound cryptanalysis to break."

While Icedrive has opted not to address the identified issues following responsible disclosure in late April 2024, Sync, Seafile, and Tresorit have acknowledged the report. The Hacker News has reached out to each of them for further comment, and we will update the story if we hear back.

The findings come a little over six months after a group of academics from King's College London and ETH Zurich detailed three distinct attacks against Nextcloud's E2EE feature that could be abused to break confidentiality and integrity guarantees.

"The vulnerabilities make it trivial for a malicious Nextcloud server to access and manipulate users' data," the researchers [said](https://eprint.iacr.org/2024/546) at the time, highlighting the need to treat all server actions and server-generated inputs as adversarial to address the problems.

Back in June 2022, ETH Zurich researchers also [demonstrated](https://thehackernews.com/2022/06/researchers-uncover-ways-to-break.html) a number of critical security issues in the MEGA cloud storage service that could be leveraged to break the confidentiality and integrity of user data.

### Responses from the companies

**Icedrive -** *We are aware of this research paper. The paper describes possible attacks within the "compromised server" threat model, where an adversary gains full control over a file server and can modify or delete files. The paper also mentions the use of a MITM server which must be able to decrypt HTTPS/SSL traffic.*

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

*We want to reassure our users that there is no real danger to the zero-knowledge encrypted data stored on our servers - it cannot be decrypted without knowing the passphrase. If someone gains full control over a file server (which in itself is not an easy task) an...
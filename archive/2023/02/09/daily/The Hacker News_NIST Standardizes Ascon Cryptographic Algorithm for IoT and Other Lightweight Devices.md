---
title: NIST Standardizes Ascon Cryptographic Algorithm for IoT and Other Lightweight Devices
url: https://thehackernews.com/2023/02/nist-standardizes-ascon-cryptographic.html
source: The Hacker News
date: 2023-02-09
fetch_date: 2025-10-04T06:10:09.963147
---

# NIST Standardizes Ascon Cryptographic Algorithm for IoT and Other Lightweight Devices

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

# [NIST Standardizes Ascon Cryptographic Algorithm for IoT and Other Lightweight Devices](https://thehackernews.com/2023/02/nist-standardizes-ascon-cryptographic.html)

**Feb 08, 2023**Ravie LakshmananEncryption / IoT Security

[![Ascon Cryptographic Algorithm for IoT](data:image/png;base64... "Ascon Cryptographic Algorithm for IoT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi42dS62dJPo0QuD2ENcasjCyih6i1o1y9uCEthdu6h2dRipDB7aeFX_lPvrarmCsHjkJBXrioHQdW1sGszdS93V-MUvgnTdQPM2uxpCWfWScJLTffJZKh4ZhdhVK-4PqyBy68tpZkVWExzLQizoA6TSAHfwYFgKsF1tclBXaQPEDndSekVCYVE3AFk/s790-rw-e365/iot.png)

The U.S. National Institute of Standards and Technology (NIST) has announced that a family of authenticated encryption and hashing algorithms known as Ascon will be standardized for [lightweight cryptography](https://csrc.nist.gov/Projects/lightweight-cryptography) applications.

"The chosen algorithms are designed to protect information created and transmitted by the Internet of Things (IoT), including its myriad tiny sensors and actuators," NIST [said](https://www.nist.gov/news-events/news/2023/02/nist-selects-lightweight-cryptography-algorithms-protect-small-devices). "They are also designed for other miniature technologies such as implanted medical devices, stress detectors inside roads and bridges, and keyless entry fobs for vehicles."

Put differently, the idea is to adopt security protections via lightweight cryptography in devices that have a "limited amount of electronic resources." That said, NIST still recommends the Advanced Encryption Standard ([AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)) and [SHA-256](https://en.wikipedia.org/wiki/SHA-2) for general use.

Ascon is [credited](https://ascon.iaik.tugraz.at/) to a team of cryptographers from the Graz University of Technology, Infineon Technologies, Lamarr Security Research, and Radboud University.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The suite comprises authenticated ciphers ASCON-128, ASCON-128a, and a variant called ASCON-80pq that comes with resistance against [quantum key-search](https://thehackernews.com/2022/08/single-core-cpu-cracked-post-quantum.html). It also offers a set of hash functions ASCON-HASH, ASCON-HASHA, ASCON-XOF, and ASCON-XOFA.

It's primarily aimed at constrained devices, and is said to be "easy to implement, even with added countermeasures against [side-channel attacks](https://en.wikipedia.org/wiki/Side-channel_attack)," according to its developers. This means that even if an adversary manages to glean sensitive information about the internal state during data processing, it cannot be leveraged to recover the secret key.

Ascon is also engineered to provide authenticated encryption with associated data (AEAD), which makes it possible to bind ciphertext to additional information, such as a device's IP address, to authenticate the ciphertext and prove its integrity.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The algorithm ensures that all of the protected data is authentic and has not changed in transit," NIST said. "AEAD can be used in vehicle-to-vehicle communications, and it also can help prevent counterfeiting of messages exchanged with the radio frequency identification (RFID) tags that often help track packages in warehouses."

Implementations of the [algorithm](https://ascon.iaik.tugraz.at/implementations.html) are [available](https://github.com/ascon/ascon_collection) in different programming languages, such as C, Java, Python, and Rust, in addition to hardware implementations that offer side-channel protections and energy efficiency.

When reached for comment, the Ascon team told The Hacker News that it's looking forward to the standardization process in the coming months.

"While we've already been working on Ascon for almost 10 years, this decision will trigger interesting new questions related to practical requirements and thus advance the research further," Maria Eichlseder, assistant professor of cryptography at Graz University of Technology, said.

"We also see this as a great opportunity for further research in secure implementations of Ascon and related designs, such as [ISAP](https://isap.iaik.tugraz.at/)."

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

[Authentication](https://thehackernews.com/search/label/Authentication)[cryptography](https://thehackernews.com/search/label/cryptography)[encryption](https://thehackernews.com/search/label/encryption)[IoT Device](https://thehackernews.com/search/label/IoT%20Device)[NIST](https://thehackernews.com/search/label/NIST)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Ten...
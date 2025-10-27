---
title: Goodbye SHA-1: NIST Retires 27-Year-Old Widely Used Cryptographic Algorithm
url: https://thehackernews.com/2022/12/goodbye-sha-1-nist-retires-27-year-old.html
source: The Hacker News
date: 2022-12-17
fetch_date: 2025-10-04T01:50:26.174934
---

# Goodbye SHA-1: NIST Retires 27-Year-Old Widely Used Cryptographic Algorithm

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

# [Goodbye SHA-1: NIST Retires 27-Year-Old Widely Used Cryptographic Algorithm](https://thehackernews.com/2022/12/goodbye-sha-1-nist-retires-27-year-old.html)

**Dec 16, 2022**Ravie LakshmananEncryption / Data Security

[![SHA-1 Cryptographic Algorithm](data:image/png;base64... "SHA-1 Cryptographic Algorithm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS63RPyCCmqTsrKDunKx8BK738LSTdA-q7VMtWWRPGysA2yZCCr2TsVPMlypAxCojp0_QXknUdNILTBEY5fT2kEHjKc7ykQMn5QtGoOssb5gVT1hRvWPgCuGHr-8fNmMIgpkT6Y0SJiK3UNT_5SmYbhEmgcvHA36Tky3m0eCT2b6vAUhuer9LpWUey/s790-rw-e365/sha1.png)

The U.S. National Institute of Standards and Technology (NIST), an agency within the Department of Commerce, [announced](https://www.nist.gov/news-events/news/2022/12/nist-retires-sha-1-cryptographic-algorithm) Thursday that it's formally retiring the SHA-1 cryptographic algorithm.

[SHA-1](https://en.wikipedia.org/wiki/SHA-1), short for Secure Hash Algorithm 1, is a 27-year-old [hash function](https://en.wikipedia.org/wiki/Hash_function) used in cryptography and has since been [deemed](https://www.schneier.com/blog/archives/2005/02/cryptanalysis_o.html) [broken](https://csrc.nist.gov/news/2006/nist-comments-on-cryptanalytic-attacks-on-sha-1) owing to the risk of [collision attacks](https://en.wikipedia.org/wiki/Collision_attack).

While hashes are designed to be irreversible – meaning it should be impossible to reconstruct the original message from the fixed-length enciphered text – the lack of collision resistance in SHA-1 made it possible to generate the same hash value for two different inputs.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In February 2017, a group of researchers from CWI Amsterdam and Google [disclosed](https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html) the first practical technique for producing collisions on SHA-1, effectively undermining the security of the algorithm.

"For example, by crafting the two colliding PDF files as two rental agreements with different rent, it is possible to trick someone to create a valid signature for a high-rent contract by having him or her sign a low-rent contract," the researchers [said](https://shattered.it/) at the time.

The cryptanalytic attacks on SHA-1 [prompted](https://csrc.nist.gov/Projects/Hash-Functions/NIST-Policy-on-Hash-Functions) NIST in 2015 to mandate federal agencies in the U.S. to stop using the algorithm for generating digital signatures, timestamps, and other applications that require collision resistance.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

According to NIST's Cryptographic Algorithm Validation Program ([CAVP](https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program)), which curates a list of approved cryptographic algorithms, as many as [2,272 libraries](https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program/validation-search?searchMode=validation&productType=-1&algorithm=129&dateFrom=01%2F01%2F2018&ipp=100) accredited since January 2018 still support SHA-1.

Besides urging users relying on the algorithm to migrate to SHA-2 or SHA-3 for securing electronic information, NIST is also recommending for SHA-1 be entirely phased out by December 31, 2030.

"Modules that still use SHA-1 after 2030 will not be [permitted for purchase](https://csrc.nist.gov/projects/cryptographic-module-validation-program) by the federal government," NIST computer scientist Chris Celi said. "Companies have eight years to submit updated modules that no longer use SHA-1."

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

[cryptographic hash](https://thehackernews.com/search/label/cryptographic%20hash)[Cryptographic hash collision](https://thehackernews.com/search/label/Cryptographic%20hash%20collision)[cryptography](https://thehackernews.com/search/label/cryptography)[NIST](https://thehackernews.com/search/label/NIST)[SHA-1 Hash Algorithm](https://thehackernews.com/search/label/SHA-1%20Hash%20Algorithm)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://the...
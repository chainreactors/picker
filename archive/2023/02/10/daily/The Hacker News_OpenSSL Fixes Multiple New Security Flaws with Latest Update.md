---
title: OpenSSL Fixes Multiple New Security Flaws with Latest Update
url: https://thehackernews.com/2023/02/openssl-fixes-multiple-new-security.html
source: The Hacker News
date: 2023-02-10
fetch_date: 2025-10-04T06:17:07.323899
---

# OpenSSL Fixes Multiple New Security Flaws with Latest Update

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

# [OpenSSL Fixes Multiple New Security Flaws with Latest Update](https://thehackernews.com/2023/02/openssl-fixes-multiple-new-security.html)

**Feb 09, 2023**Ravie LakshmananEncryption / Vulnerability

[![OpenSSL](data:image/png;base64... "OpenSSL")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2fd3OTmnadHxr-Z0uIYZhV_g6gmsKQIOAMfSKda0cfz_humOSvXRV2tgMqZOZwJdXm5Z-O6hlN9DktL8VPkAv3yMtCjJJVTOkXWLuwojB8MPvVuRUlhYeQORQ8amKIrPYKlYgjiXA7c_Zt_lNvnymOgbCTv_gxBZiNDfxkOtls3IuJUTVa3ZJwahK/s790-rw-e365/openssl.png)

The OpenSSL Project has released fixes to address several security flaws, including a high-severity bug in the open source encryption toolkit that could potentially expose users to malicious attacks.

Tracked as [**CVE-2023-0286**](https://nvd.nist.gov/vuln/detail/CVE-2023-0286), the issue relates to a case of type confusion that may permit an adversary to "read memory contents or enact a denial-of-service," the maintainers said in an advisory.

The vulnerability is rooted in the way the [popular cryptographic library](https://thehackernews.com/2022/11/just-in-openssl-releases-patch-for-2.html) handles X.509 certificates, and is likely to impact only those applications that have a custom implementation for retrieving a certificate revocation list ([CRL](https://en.wikipedia.org/wiki/Certificate_revocation_list)) over a network.

"In most cases, the attack requires the attacker to provide both the certificate chain and CRL, neither of which need to have a valid signature," OpenSSL [said](https://www.openssl.org/news/vulnerabilities.html). "If the attacker only controls one of these inputs, the other input must already contain an X.400 address as a CRL distribution point, which is uncommon."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Type confusion flaws could have [serious consequences](https://cwe.mitre.org/data/definitions/843.html), as they could be weaponized to deliberately force the program to behave in unintended ways, possibly causing a crash or code execution.

The issue has been patched in OpenSSL versions 3.0.8, 1.1.1t, and 1.0.2zg. Other security flaws [addressed](https://www.openssl.org/news/secadv/20230207.txt) as part of the latest updates include:

* **CVE-2022-4203** - X.509 Name Constraints Read Buffer Overflow
* **CVE-2022-4304** - Timing Oracle in RSA Decryption
* **CVE-2022-4450** - Double free after calling PEM\_read\_bio\_ex
* **CVE-2023-0215** - Use-after-free following BIO\_new\_NDEF
* **CVE-2023-0216** - Invalid pointer dereference in d2i\_PKCS7 functions
* **CVE-2023-0217** - NULL dereference validating DSA public key
* **CVE-2023-0401** - NULL dereference during PKCS7 data verification

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Successful exploitation of the above shortcomings could lead to an application crash, disclose memory contents, and even recover plaintext messages sent over a network by taking advantage of a [timing-based side-channel](https://nakedsecurity.sophos.com/2023/02/08/openssl-fixes-high-severity-data-stealing-bug-patch-now/) in what's a [Bleichenbacher-style attack](https://thehackernews.com/2022/06/researchers-uncover-ways-to-break.html).

The fixes arrive nearly two months after OpenSSL plugged a low-severity flaw ([CVE-2022-3996](https://nvd.nist.gov/vuln/detail/CVE-2022-3996)) that arises when processing an X.509 certificate, resulting in a denial-of-service condition.

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

[encryption](https://thehackernews.com/search/label/encryption)[OpenSSL](https://thehackernews.com/search/label/OpenSSL)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/202...
---
title: New TEE.Fail Side-Channel Attack Extracts Secrets from Intel and AMD DDR5 Secure Enclaves
url: https://thehackernews.com/2025/10/new-teefail-side-channel-attack.html
source: The Hacker News
date: 2025-10-28
fetch_date: 2025-10-29T03:16:26.104419
---

# New TEE.Fail Side-Channel Attack Extracts Secrets from Intel and AMD DDR5 Secure Enclaves

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

# [New TEE.Fail Side-Channel Attack Extracts Secrets from Intel and AMD DDR5 Secure Enclaves](https://thehackernews.com/2025/10/new-teefail-side-channel-attack.html)

**Oct 28, 2025**Ravie LakshmananEncryption / Hardware Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7WEENR9AjQZ-WdyQPD5itMbQHGgQu79Ykq0IYfq-vThOrYHX14a_kPBXDW39gvSaT8qQpGHJ9Xb73eCO18CfNSPLOHmnp40IAZ3HDHeCmgMLxaB7sGt8w37KQkuXoFelF4letd03UWYWcFfPYtfA6g-0P7z_qAMbQjI-2Mg4htAyB71nfu7CKlqVVw2Q2/s790-rw-e365/tee.jpg)

A group of academic researchers from Georgia Tech, Purdue University, and Synkhronix have developed a side-channel attack called **[TEE.Fail](https://tee.fail)** that allows for the extraction of secrets from the trusted execution environment (TEE) in a computer's main processor, including Intel's Software Guard eXtensions (SGX) and Trust Domain Extensions (TDX) and AMD's Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) and [Ciphertext Hiding](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3021.html).

The attack, at its core, involves the use of an interposition device built using off-the-shelf electronic equipment that costs under $1,000 and makes it possible to physically inspect all memory traffic inside a DDR5 server.

"This allows us for the first time to extract cryptographic keys from Intel TDX and AMD SEV-SNP with Ciphertext Hiding, including in some cases secret attestation keys from fully updated machines in trusted status," the researchers noted on an informational site.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Beyond breaking CPU-based TEEs, we also show how extracted attestation keys can be used to compromise Nvidia's GPU Confidential Computing, allowing attackers to run AI workloads without any TEE protections."

The findings come weeks after the release of two other attacks aimed at TEEs, such as [Battering RAM](https://thehackernews.com/2025/10/50-battering-ram-attack-breaks-intel.html) and [WireTap](https://thehackernews.com/2025/10/new-wiretap-attack-extracts-intel-sgx.html). Unlike these techniques that target systems using DDR4 memory, TEE.Fail is the first attack to be demonstrated against DDR5, meaning they can be used to undermine the latest hardware security protections from Intel and AMD.

The latest study has found that the AES-XTS encryption mode used by Intel and AMD is deterministic and, therefore, not sufficient to prevent physical memory interposition attacks. In a hypothetical attack scenario, a bad actor could leverage the custom equipment to record the memory traffic flowing between the computer and DRAM, and observe the memory contents during read and write operations, thereby opening the door to a side-channel attack.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipVRp6gyI5fhMu1VFWaFRtv7_p0nuCP1HH6BUJpR3JUuD_evTox-hZ1fdRj0r5M5eMttkcyhMWlxtNViU6azLQ9iry2hsbcKcDyjXUtT2Y-jG92jIqyBs1LQ-HJAgNJr5Y1Yg9s6Y5GM8YxgsyIh6Oe622BRHX48bwA-uASFeUhBARjc-c40BrYDut0COC/s790-rw-e365/data.png)

This could be ultimately exploited to extract data from confidential virtual machines (CVMs), including ECDSA attestation keys from Intel's Provisioning Certification Enclave (PCE), necessary in order to break SGX and TDX attestation.

"As attestation is the mechanism used to prove that data and code are actually executed in a CVM, this means that we can pretend that your data and code is running inside a CVM when in reality it is not," the researchers said. "We can read your data and even provide you with incorrect output, while still faking a successfully completed attestation process."

The study also pointed out that SEV-SNP with Ciphertext Hiding neither addresses issues with deterministic encryption nor prevents physical bus interposition. As a result, the attack facilitates the extraction of private signing keys from OpenSSL's ECDSA implementation.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Importantly, OpenSSL's cryptographic code is fully constant-time and our machine had Ciphertext Hiding enabled, thus showing these features are not sufficient to mitigate bus interposition attacks," they added.

While there is no evidence that the attack has been put to use in the wild, the researchers recommend using software countermeasures to mitigate the risks arising as a result of deterministic encryption. However, they are likely to be expensive.

In response to the disclosure, AMD [said](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3040.html) it has no plans to provide mitigations since physical vector attacks are out of scope for AMD SEV-SNP. Intel, in a similar alert, [noted](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2025-10-28-001.html) that TEE.fail does not change the company's previous out-of-scope statement for these types of physical attacks.

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

[AMD](https://thehackernews.com/search/label/AMD)[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https:/...
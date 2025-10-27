---
title: Researchers Say Microsoft Office 365 Uses Broken Email Encryption to Secure Messages
url: https://thehackernews.com/2022/10/researchers-claim-microsoft-office-365.html
source: The Hacker News
date: 2022-10-18
fetch_date: 2025-10-03T20:10:54.718603
---

# Researchers Say Microsoft Office 365 Uses Broken Email Encryption to Secure Messages

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

# [Researchers Say Microsoft Office 365 Uses Broken Email Encryption to Secure Messages](https://thehackernews.com/2022/10/researchers-claim-microsoft-office-365.html)

**Oct 17, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_w3nbJTFOqsK2RHm5cSJyf3QQjXne8E1kuRL7HaCED20pfpV6CQM5lrf7vD-qJiJ7-FTAkvko33UU3pnWpX4c-TCJyTzy36hHjPmh5CYWkpIpSH5OepCVmIwx5Df0tVOR7an34dFY-VKjJyk1WBHCZ3JSdR4YGO3fHXV9E-9oNT112liEei5slOnT/s790-rw-e365/crypto.jpg)

New research has disclosed what's being called a security vulnerability in Microsoft 365 that could be exploited to infer message contents due to the use of a broken cryptographic algorithm.

"The [Office 365 Message Encryption] messages are encrypted in insecure Electronic Codebook ([ECB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB))) mode of operation," Finnish cybersecurity company WithSecure [said](https://labs.withsecure.com/advisories/microsoft-office-365-message-encryption-insecure-mode-of-operation) in a report published last week.

Office 365 Message Encryption (OME) is a security mechanism used to send and receive encrypted email messages between users inside and outside an organization without revealing anything about the communications themselves.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A consequence of the newly disclosed issue is that rogue third-parties gaining access to the encrypted email messages may be able to decipher the messages, effectively breaking confidentiality protections.

Electronic Codebook is one of the simplest modes of encryption wherein each message block is encoded separately by a key, meaning identical plaintext blocks will be transposed into identical ciphertext blocks, making it [unsuitable](https://nvd.nist.gov/vuln/detail/CVE-2020-11500) as a cryptographic protocol.

Indeed, the U.S. National Institute of Standards and Technology (NIST) [pointed out](https://csrc.nist.gov/News/2022/proposal-to-revise-sp-800-38a) earlier this year that "ECB mode encrypts plaintext blocks independently, without randomization; therefore, the inspection of any two ciphertext blocks reveals whether or not the corresponding plaintext blocks are equal."

That said, the shortcoming identified by WithSecure doesn't relate to the decryption of a single message per se, but rather banks on analyzing a stash of encrypted stolen mails for such leaky patterns and subsequently decoding the contents.

"An attacker with a large database of messages may infer their content (or parts of it) by analyzing relative locations of repeated sections of the intercepted messages," the company said.

The findings add to growing concerns that encrypted information previously exfiltrated may be decrypted and exploited for attacks in the future, a threat called "hack now, decrypt later," fueling the need to switch to [quantum-resistant algorithms](https://thehackernews.com/2022/07/nist-announces-first-four-quantum.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Microsoft, for its part, considers OME as a [legacy system](https://learn.microsoft.com/en-us/microsoft-365/compliance/legacy-information-for-message-encryption), with the company [recommending customers](https://learn.microsoft.com/en-us/microsoft-365/compliance/ome-faq) to use a data governance platform called [Purview](https://learn.microsoft.com/en-us/azure/purview/) to secure emails and documents via encryption and access controls.

"Even though both versions can coexist, we highly recommend that you edit your old mail flow rules that use the rule action Apply the previous version of OME to use Microsoft Purview Message Encryption," Redmond [notes](https://learn.microsoft.com/en-us/microsoft-365/compliance/ome-version-comparison) in its documentation.

"Since Microsoft has no plans to fix this vulnerability the only mitigation is to avoid using Microsoft Office 365 Message Encryption," WithSecure said.

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

[encryption](https://thehackernews.com/search/label/encryption)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Microsoft 365](https://thehackernews.com/search/label/Microsoft%20365)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-criti...
---
title: Additional Supply Chain Vulnerabilities Uncovered in AMI MegaRAC BMC Software
url: https://thehackernews.com/2023/02/additional-supply-chain-vulnerabilities.html
source: The Hacker News
date: 2023-02-02
fetch_date: 2025-10-04T05:32:12.574251
---

# Additional Supply Chain Vulnerabilities Uncovered in AMI MegaRAC BMC Software

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

# [Additional Supply Chain Vulnerabilities Uncovered in AMI MegaRAC BMC Software](https://thehackernews.com/2023/02/additional-supply-chain-vulnerabilities.html)

**Feb 01, 2023**Ravie LakshmananServer and Cloud Security

[![BMC Supply Chain Vulnerabilities](data:image/png;base64... "BMC Supply Chain Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3PVTa1kltLpsnOdDNb2zOa39L0toek5kLvG7ZHCo17u-89Mg0ABdOrMuOEQnRGnp3T8M9mkZOCKCtUQs3X80tqNRs5lN_MyOkRQC_jYZ93ESxrzG36YGGKr4-nxjjVwF6yI7oA1OMEDk1vzGFDnNQEMJbCeDCQLbYAsnCjjmsaCubbV7xRKyRJPx2/s790-rw-e365/server.png)

Two more supply chain security flaws have been disclosed in AMI MegaRAC Baseboard Management Controller (BMC) software, nearly two months after [three security vulnerabilities](https://thehackernews.com/2022/12/new-bmc-supply-chain-vulnerabilities.html) were brought to light in the same product.

Firmware security firm Eclypsium [said](https://eclypsium.com/2022/12/05/supply-chain-vulnerabilities-put-server-ecosystem-at-risk/) the two shortcomings were held back until now to provide AMI additional time to engineer appropriate mitigations.

The issues, collectively tracked as **BMC&C**, could act as a springboard for cyber attacks, enabling threat actors to obtain remote code execution and unauthorized device access with superuser permissions.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The two new flaws in question are as follows -

* [**CVE-2022-26872**](https://nvd.nist.gov/vuln/detail/CVE-2022-26872) (CVSS score: 8.3) - ​​Password reset interception via API
* [**CVE-2022-40258**](https://nvd.nist.gov/vuln/detail/CVE-2022-40258) (CVSS score: 5.3) - Weak password hashes for Redfish and API

Specifically, MegaRAC has been found to use the MD5 hashing algorithm with a global salt for older devices, or [SHA-512 with per user salts](https://blog.mozilla.org/security/2011/05/10/sha-512-w-per-user-salts-is-not-enough/) on newer appliances, potentially allowing a threat actor to crack the passwords.

CVE-2022-26872, on the other hand, leverages an HTTP API to dupe a user into initiating a password reset by means of a social engineering attack, and set a password of the adversary's choice.

CVE-2022-26872 and CVE-2022-40258 add to three other vulnerabilities disclosed in December, including [CVE-2022-40259](https://nvd.nist.gov/vuln/detail/CVE-2022-40259) (CVSS score: 9.9), [CVE-2022-40242](https://nvd.nist.gov/vuln/detail/CVE-2022-40242) (CVSS score: 8.3), and [CVE-2022-2827](https://nvd.nist.gov/vuln/detail/CVE-2022-2827) (CVSS score: 7.5).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's worth pointing out that the weaknesses are exploitable only in scenarios where the BMCs are exposed to the internet or in cases where the threat actor has already gained initial access into a data center or administrative network by other methods.

The blast radius of BMC&C is currently unknown, but Eclypsium said it's working with AMI and other parties to determine the scope of impacted products and services.

Gigabyte, Hewlett Packard Enterprise, Intel, and Lenovo have all released updates to address the security defects in their devices. NVIDIA is [expected](https://nvidia.custhelp.com/app/answers/detail/a_id/5435) to ship a fix in May 2023.

"The impact of exploiting these vulnerabilities include remote control of compromised servers, remote deployment of malware, ransomware and firmware implants, and server physical damage (bricking)," Eclypsium noted.

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

[BMC Software](https://thehackernews.com/search/label/BMC%20Software)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Eclypsium](https://thehackernews.com/search/label/Eclypsium)[server security](https://thehackernews.com/search/label/server%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked Plu...
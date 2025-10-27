---
title: New Flaws in TPM 2.0 Library Pose Threat to Billions of IoT and Enterprise Devices
url: https://thehackernews.com/2023/03/new-flaws-in-tpm-20-library-pose-threat.html
source: The Hacker News
date: 2023-03-04
fetch_date: 2025-10-04T08:41:28.340592
---

# New Flaws in TPM 2.0 Library Pose Threat to Billions of IoT and Enterprise Devices

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

# [New Flaws in TPM 2.0 Library Pose Threat to Billions of IoT and Enterprise Devices](https://thehackernews.com/2023/03/new-flaws-in-tpm-20-library-pose-threat.html)

**Mar 03, 2023**Ravie LakshmananEnterprise Security / IoT

[![Enterprises and IoT Devices](data:image/png;base64... "Enterprises and IoT Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOyS_tkH5DQ3XqoOXKHGEKEsDIylUMip1tGAtAvhafX-nH4DIbbgUhGfAN6B7q_H_gsfN-hcDMqYpyTUaswzu57Y3VPFp10uABW3UYEfy4KULJMFlOT--Lo-tcO1SDph6hoGhuV-FwiaVNVEs5WIVyXl1wUx5QXa_w2c9wJpydf5oM_VDtG8dEDwIZ/s790-rw-e365/chip.png)

A pair of serious security defects has been disclosed in the Trusted Platform Module ([TPM](https://en.wikipedia.org/wiki/Trusted_Platform_Module)) 2.0 reference library specification that could potentially lead to information disclosure or privilege escalation.

One of the vulnerabilities, **CVE-2023-1017**, concerns an out-of-bounds write, while the other, **CVE-2023-1018**, is described as an out-of-bounds read. Credited with discovering and reporting the issues in November 2022 is cybersecurity company Quarkslab.

"These vulnerabilities can be triggered from user-mode applications by sending malicious commands to a TPM 2.0 whose firmware is based on an affected TCG reference implementation," the Trusted Computing Group (TCG) [said](https://trustedcomputinggroup.org/wp-content/uploads/TCGVRT0007-Advisory-FINAL.pdf) in an advisory.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Large tech vendors, organizations using enterprise computers, servers, IoT devices, and embedded systems that include a TPM can be impacted by the flaws, Quarkslab [noted](https://content.quarkslab.com/major-vulnerabilities-tpm20), adding they "could affect billions of devices."

TPM is a hardware-based solution (i.e., a crypto-processor) that's designed to provide secure cryptographic functions and physical security mechanisms to resist tampering efforts.

"The most common TPM functions are used for system integrity measurements and for key creation and use," Microsoft [says](https://learn.microsoft.com/en-us/windows/security/information-protection/tpm/trusted-platform-module-overview) in its documentation. "During the boot process of a system, the boot code that is loaded (including firmware and the operating system components) can be measured and recorded in the TPM."

"The integrity measurements can be used as evidence for how a system started and to make sure that a TPM-based key was used only when the correct software was used to boot the system."

The TCG consortium noted that the shortcomings are the result of a lack of necessary length checks, resulting in buffer overflows that could pave the way for local information disclosure or escalation of privileges.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Users are recommended to [apply the updates](https://trustedcomputinggroup.org/resource/errata-for-tpm-library-specification-2-0/) released by TCG as well as other vendors to address the flaws and mitigate supply chain risks.

"Users in high-assurance computing environments should consider using TPM Remote Attestation to detect any changes to devices and ensure their TPM is tamper proofed," the CERT Coordination Center (CERT/CC) [said](https://kb.cert.org/vuls/id/782720) in an alert.

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

[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[iot security](https://thehackernews.com/search/label/iot%20security)[Quarkslab](https://thehackernews.com/search/label/Quarkslab)[Trusted Platform Module](https://thehackernews.com/search/label/Trusted%20Platform%20Module)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm M...
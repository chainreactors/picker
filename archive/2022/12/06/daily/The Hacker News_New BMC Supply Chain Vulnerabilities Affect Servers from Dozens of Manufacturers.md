---
title: New BMC Supply Chain Vulnerabilities Affect Servers from Dozens of Manufacturers
url: https://thehackernews.com/2022/12/new-bmc-supply-chain-vulnerabilities.html
source: The Hacker News
date: 2022-12-06
fetch_date: 2025-10-04T00:37:15.815130
---

# New BMC Supply Chain Vulnerabilities Affect Servers from Dozens of Manufacturers

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

# [New BMC Supply Chain Vulnerabilities Affect Servers from Dozens of Manufacturers](https://thehackernews.com/2022/12/new-bmc-supply-chain-vulnerabilities.html)

**Dec 05, 2022**Ravie LakshmananServer Security / Cloud Technology

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiolCsXBH-kaR61fYu-jBJwv8qNy3L5XE48zgFzAOo0D8xZIhyZyPMESMC0L7Cy3993u4PbVASQyv9QyJAXwtP35mNPY_On_q3S9FJwsCvbkagdC6jHgRl1ax_y6XEyPDxf0fTYHuW_cCMTl-xFgPfF3kbFYIpWh6SZvssXaBGInRrJ21WvMEYJ1J4d/s790-rw-e365/server-hacking.png)

Three different security flaws have been disclosed in American Megatrends (AMI) [MegaRAC](https://www.ami.com/megarac/) Baseboard Management Controller (BMC) software that could lead to remote code execution on vulnerable servers.

"The impact of exploiting these vulnerabilities include remote control of compromised servers, remote deployment of malware, ransomware and firmware implants, and server physical damage (bricking)," firmware and hardware security company Eclypsium [said](https://eclypsium.com/2022/12/05/supply-chain-vulnerabilities-put-server-ecosystem-at-risk/) in a report shared with The Hacker News.

BMCs are privileged independent systems within servers that are used to control low-level hardware settings and manage the host operating system, even in scenarios when the machine is powered off.

These capabilities make BMCs an enticing target for threat actors looking to plant persistent malware on devices that can survive operating system reinstalls and hard drive replacements.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the major server manufacturers that are known to have used MegaRAC BMC include AMD, Ampere Computing, Arm, ASRock, Asus, Dell EMC, GIGABYTE, Hewlett Packard Enterprise, Huawei, Lenovo, Nvidia, Qualcomm, Quanta, and Tyan.

Collectively called **BMC&C**, the newly identified issues can be exploited by attackers having access to remote management interfaces ([IPMI](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface)) such as [Redfish](https://www.dmtf.org/standards/redfish), potentially enabling adversaries to gain control of the systems and put cloud infrastructures at risk.

The most severe among the issues is CVE-2022-40259 (CVSS score: 9.9), a case of arbitrary code execution via the Redfish API that requires the attacker to already have a minimum level of access on the device ([Callback privileges](https://docs.graphcore.ai/projects/bmc-user-guide/en/latest/user-management.html) or higher).

CVE-2022-40242 (CVSS score: 8.3) relates to a hash for a sysadmin user that can be cracked and abused to gain administrative shell access, while CVE-2022-2827 (CVSS score: 7.5) is a bug in the password reset feature that can be exploited to determine if an account with a specific username exists.

"[CVE-2022-2827] allows for pinpointing pre-existing users and does not lead into a shell but would provide an attacker a list of targets for brute-force or credential stuffing attacks," the researchers explained.

The findings once again underscore the importance of securing the firmware supply chain and ensuring that BMC systems are not directly exposed to the internet.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"As data centers tend to standardize on specific hardware platforms, any BMC-level vulnerability would most likely apply to large numbers of devices and could potentially affect an entire data center and the services that it delivers," the company said.

The findings come as Binarly disclosed [multiple](https://binarly.io/posts/Black_Hat_2022_The_Intel_PPAM_attack_story/index.html) [high-impact vulnerabilities](https://www.binarly.io/posts/Binarly_Discovers_Multiple_High_Severity_Vulnerabilities_in_AMI_based_Devices/index.html) in AMI-based devices that could result in memory corruption and arbitrary code execution during early boot phases (i.e., a pre-EFI environment).

Earlier this May, Eclypsium also uncovered what's called a "[Pantsdown](https://thehackernews.com/2022/05/critical-pantsdown-bmc-vulnerability.html)" BMC flaw impacting Quanta Cloud Technology (QCT) servers, a successful exploitation of which could grant attackers full control over the devices.

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

[Baseboard Management Controller](https://thehackernews.com/search/label/Baseboard%20Management%20Controller)[BMC Software](https://thehackernews.com/search/label/BMC%20Software)[hacking news](https://thehackernews.com/search/label/hacking%20news)[server security](https://thehackernews.com/search/label/server%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Imper...
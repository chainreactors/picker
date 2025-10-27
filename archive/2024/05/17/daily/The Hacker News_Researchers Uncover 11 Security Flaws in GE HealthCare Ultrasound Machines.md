---
title: Researchers Uncover 11 Security Flaws in GE HealthCare Ultrasound Machines
url: https://thehackernews.com/2024/05/researchers-uncover-11-security-flaws.html
source: The Hacker News
date: 2024-05-17
fetch_date: 2025-10-06T17:17:35.967178
---

# Researchers Uncover 11 Security Flaws in GE HealthCare Ultrasound Machines

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

# [Researchers Uncover 11 Security Flaws in GE HealthCare Ultrasound Machines](https://thehackernews.com/2024/05/researchers-uncover-11-security-flaws.html)

**May 16, 2024**Ravie LakshmananRansomware / Internet of Things

[![GE HealthCare Ultrasound Machines](data:image/png;base64... "GE HealthCare Ultrasound Machines")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0W6bvR9fzkycXkJJdcnbs_5eE6MI3KteW1cqK4EmjT9CtU3UeHZ9qrBsDt81R0i6Ihyphenhyphen9LKFhwPHDAoHdYzi_rLcg_FZC7x4ddV05oV0ybdTa8rd1Uu-lwxbQbHJeLL2X19HyElBjinJemsN7A8V5cenapqWtdFi0mJjbbAQroZFomNspkugGaARpukihf/s790-rw-e365/machine.png)

Security researchers have disclosed almost a dozen security flaws impacting the GE HealthCare Vivid Ultrasound product family that could be exploited by malicious actors to tamper with patient data and even install ransomware under certain circumstances.

"The impacts enabled by these flaws are manifold: from the implant of ransomware on the ultrasound machine to the access and manipulation of patient data stored on the vulnerable devices," operational technology (OT) security vendor Nozomi Networks [said](https://www.nozominetworks.com/blog/ge-healthcare-vivid-ultrasound-vulnerabilities) in a technical report.

The security issues impact the Vivid T9 ultrasound system and its pre-installed Common Service Desktop web application, which is exposed on the localhost interface of the device and allows users to perform administrative actions.

They also affect another software program called EchoPAC that's installed on a doctor's Windows workstation to help them access multi-dimensional echo, vascular, and abdominal ultrasound images.

That being said, successful exploitation of the flaws requires a threat actor to first gain access to the hospital environment and physically interact with the device, after which they can be exploited to achieve arbitrary code execution with administrative privileges.

In a hypothetical attack scenario, a malicious actor could lock out the Vivid T9 systems by implanting a ransomware payload and even exfiltrate or tamper with patient data.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The most severe of the vulnerabilities is CVE-2024-27107 (CVSS score: 9.6), which concerns the use of hard-coded credentials. Other identified shortcomings relate to command injection (CVE-2024-1628), execution with unnecessary privileges (CVE-2024-27110 and CVE-2020-6977), path traversal (CVE-2024-1630 and CVE-2024-1629), and protection mechanism failure (CVE-2020-6977).

The exploit chain devised by Nozomi Networks takes advantage of CVE-2020-6977 to get local access to the device and then weaponizes CVE-2024-1628 to attain code execution.

"However, to speed up the process, [...] an attacker may also abuse the exposed USB port and attach a malicious thumb drive that, by emulating the keyboard and mouse, automatically performs all necessary steps at faster-than-human speed," the company said.

Alternatively, an adversary could obtain access to a hospital's internal network using stolen VPN credentials gathered via other means (e.g., phishing or data leak), scan for vulnerable installations of EchoPAC, and then exploit CVE-2024-27107 to gain unfettered access to the patient's database, effectively compromising its confidentially, integrity, and availability.

[![GE HealthCare Ultrasound Machines](data:image/png;base64... "GE HealthCare Ultrasound Machines")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjy07tRvrDcZnAoAlAgbZ40aHfVK2IH03DQck9rhPrVr42fKM23NnU6wGjxw82EqDKXoarC_QK0JpUknrbsW5ApmbiUdmSV3eEMTmJJVt_Hw56armZWilWtxccAzAjz7s4MEn9lH6IR8QPIF9tELI4lmAkgLkSLRFGT63rAQfGP-mj9qmlZPraT5EQrPEZu/s790-rw-e365/ransomware.png)

GE HealthCare, in a set of advisories, said "existing mitigations and controls" reduce the risks posed by these flaws to acceptable levels.

"In the unlikely event a malicious actor with physical access could render the device unusable, there would be clear indicators of this to the intended user of the device," it [noted](https://www.gehealthcare.com/services/lifecycle-management/product-security-portal/security). "The vulnerability can only be exploited by someone with direct, physical access to the device."

The disclosure comes weeks after security flaws were also [uncovered](https://www.nozominetworks.com/blog/exploiting-healthcare-supply-chain-security-merge-dicom-toolkit) in the Merge DICOM Toolkit for Windows (CVE-2024-23912, CVE-2024-23913, and CVE-2024-23914) that could used to trigger a denial-of-service (DoS) condition on the DICOM service. The issues have been addressed in [version v5.18](https://www.merative.com/content/dam/merative/documents/technical/release-notes/merge-dicom-toolkit-5-18-0-release-notes.pdf) [PDF] of the library.

It also follows the discovery of a maximum-severity security flaw in the Siemens SIMATIC Energy Manager (EnMPro) product (CVE-2022-23450, CVSS score: 10.0) that could be exploited by a remote attacker to execute arbitrary code with SYSTEM privileges by sending maliciously crafted objects.

"An attacker successfully exploiting this vulnerability could remotely execute code and gain complete control over an EnMPro server," Claroty security researcher Noam Moshe [said](https://claroty.com/team82/research/exploiting-a-classic-deserialization-vulnerability-in-siemens-simatic-energy-manager).

Users are highly recommended to update to [version V7.3 Update 1](https://cert-portal.siemens.com/productcert/html/ssa-655554.html) or later as all versions prior to it contain the insecure deserialization vulnerability.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Security weaknesses have also been unearthed in the [ThroughTek Kalay Platform](https://www.throughtek.com/overview/) integrated within Internet of Things (IoT) devices (from CVE-2023-6321 through CVE-2023-6324) that allows an attacker to escalate privileges, execute commands as root, and establish a connec...
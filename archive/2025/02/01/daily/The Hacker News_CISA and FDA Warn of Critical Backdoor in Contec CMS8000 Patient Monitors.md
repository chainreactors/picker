---
title: CISA and FDA Warn of Critical Backdoor in Contec CMS8000 Patient Monitors
url: https://thehackernews.com/2025/01/cisa-and-fda-warn-of-critical-backdoor.html
source: The Hacker News
date: 2025-02-01
fetch_date: 2025-10-06T20:38:29.643272
---

# CISA and FDA Warn of Critical Backdoor in Contec CMS8000 Patient Monitors

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

# [CISA and FDA Warn of Critical Backdoor in Contec CMS8000 Patient Monitors](https://thehackernews.com/2025/01/cisa-and-fda-warn-of-critical-backdoor.html)

**Jan 31, 2025**Ravie LakshmananVulnerability / Healthcare

[![Critical Backdoor in Contec](data:image/png;base64... "Critical Backdoor in Contec")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTrvYDG-vuXO-u8vmIfOgMMGIBDS1zaCHCIs6Kflr_mUmGxGZyWMeMWB-16u9XmL1OiP8c-n7v7VaXhzaD18KlpH4XWcSYnn1MdPHkHgm74VbKkudrDcuz_PTJWRgfYw5yt2PvfEiYbcafLZUQ3kSbBcpifDbQfOytjeovtKaxhE4x5DhN-QRfJCghw44N/s790-rw-e365/cc.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) and the Food and Drug Administration (FDA) have issued alerts about the presence of hidden functionality in [Contec CMS8000 patient monitors](https://www.contecmed.com/productinfo/870649.html) and Epsimed MN-120 patient monitors.

The [vulnerability](https://www.cisa.gov/resources-tools/resources/contec-cms8000-contains-backdoor), tracked as **CVE-2025-0626**, carries a CVSS v4 score of 7.7 on a scale of 10.0. The flaw, alongside two other issues, was reported to CISA by an anonymous external researcher.

"The affected product sends out remote access requests to a hard-coded IP address, bypassing existing device network settings to do so," CISA [said](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-25-030-01) in an advisory. "This could serve as a backdoor and lead to a malicious actor being able to upload and overwrite files on the device."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The reverse backdoor provides automated connectivity to a hard-coded IP address from the Contec CMS8000 devices, allowing the device to download and execute unverified remote files. Publicly available records show that the IP address is not associated with a medical device manufacturer or medical facility but a third-party university."

Two other identified vulnerabilities in the devices are listed below -

* **CVE-2024-12248** (CVSS v4 score: 9.3) - An out-of-bounds write vulnerability that could allow an attacker to send specially formatted UDP requests in order to write arbitrary data, resulting in remote code execution
* **CVE-2025-0683** (CVSS v4 score: 8.2) - A privacy leakage vulnerability that causes plain-text patient data to be transmitted to a hard-coded public IP address when the patient is attached to the monitor

Successful exploitation of CVE-2025-0683 could allow the device with that unspecified IP address to gain access to confidential patient information or open the door to an adversary-in-the-middle (AitM) scenario.

The security holes affect the following products -

* CMS8000 Patient Monitor: Firmware version smart3250-2.6.27-wlan2.1.7.cramfs
* CMS8000 Patient Monitor: Firmware version CMS7.820.075.08/0.74(0.75)
* CMS8000 Patient Monitor: Firmware version CMS7.820.120.01/0.93(0.95)
* CMS8000 Patient Monitor: All versions (CVE-2025-0626 and CVE-2025-0683)

"These cybersecurity vulnerabilities can allow unauthorized actors to bypass cybersecurity controls, gaining access to and potentially manipulating the device," the FDA [said](https://www.fda.gov/medical-devices/safety-communications/cybersecurity-vulnerabilities-certain-patient-monitors-contec-and-epsimed-fda-safety-communication), adding it's "not aware of any cybersecurity incidents, injuries, or deaths related to these cybersecurity vulnerabilities at this time."

Given that these vulnerabilities remain unpatched, CISA is recommending that organizations unplug and remove any Contec CMS8000 devices from their networks. It's worth noting that the devices are also re-labeled and sold under the name Epsimed MN-120.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's also advised to check the patient monitors for any signs of unusual functioning, such as "inconsistencies between the displayed patient vitals and the patient's actual physical state."

CMS8000 Patient Monitor is manufactured by Contec Medical Systems, a developer of medical devices that are located in Qinhuangdao, China. On its website, the company [claims](https://www.contecmed.com/aboutus) its products are FDA-approved and distributed to over 130 countries and regions.

### Update

In a follow-up analysis, cybersecurity firm Claroty said that "it is most likely not a hidden backdoor, but instead an insecure/vulnerable design," and that the static IP addresses (202.114.4.119 and 202.114.4.120) in question are listed in their manuals.

"The CONTEC Operator Manual specifically mentions this "hard-coded" IP address as the Central Management System (CMS) IP address that organizations should use, so it is not hidden functionally as stated by CISA," Claroty's Team82 research team [said](https://claroty.com/team82/research/are-contec-cms8000-patient-monitors-infected-with-a-chinese-backdoor-the-reality-is-more-complicated).

"Absent additional threat intelligence, this nuance is important because it demonstrates a lack of malicious intent, and therefore changes the prioritization of remediation activities."

It's recommended that organizations using Contec CMS8000 block all access to the subnet 202.114.4.0/24 from their internal network. It's also advised to apply network segmentation and block all network traffic outbound to 202.114.4.120 to prevent leakage of information.

*(The story was updated after publication to include an analysis from Claroty.)*

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
[**Share on Twitter...
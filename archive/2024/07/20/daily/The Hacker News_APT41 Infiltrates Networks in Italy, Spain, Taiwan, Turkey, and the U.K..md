---
title: APT41 Infiltrates Networks in Italy, Spain, Taiwan, Turkey, and the U.K.
url: https://thehackernews.com/2024/07/apt41-infiltrates-networks-in-italy.html
source: The Hacker News
date: 2024-07-20
fetch_date: 2025-10-06T17:45:15.147621
---

# APT41 Infiltrates Networks in Italy, Spain, Taiwan, Turkey, and the U.K.

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

# [APT41 Infiltrates Networks in Italy, Spain, Taiwan, Turkey, and the U.K.](https://thehackernews.com/2024/07/apt41-infiltrates-networks-in-italy.html)

**Jul 19, 2024**Ravie LakshmananCyber Espionage / Threat Intelligence

[![APT41 Hackers](data:image/png;base64... "APT41 Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4MhmgNwEL6-gIJONG7CjrNFswX0ynkHfCA78zumQ1urK5-EJpktky4cGCtUJcPN5CxT5b-z_COFxPle8XBfG7J2n3V4w3l5waRgfgHDnNmjCfVllj6AXwIYSYMmVIp4FOpRJiCJEaStZXk8pybI4Dn3HdkvrSr_eTVL4u_jCXg0eJXmthAy3sOjvazyrd/s790-rw-e365/chinese-hackers.png)

Several organizations operating within global shipping and logistics, media and entertainment, technology, and automotive sectors in Italy, Spain, Taiwan, Thailand, Turkey, and the U.K. have become the target of a "sustained campaign" by the prolific China-based **APT41** hacking group.

"APT41 successfully infiltrated and maintained prolonged, unauthorized access to numerous victims' networks since 2023, enabling them to extract sensitive data over an extended period," Google-owned Mandiant [said](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust) in a new report published Thursday.

The threat intelligence firm described the adversarial collective as unique among China-nexus actors owing to its use of "non-public malware typically reserved for espionage operations in activities that appear to fall outside the scope of state-sponsored missions."

Attack chains involve the use of web shells (ANTSWORD and BLUEBEAM), custom droppers (DUSTPAN and DUSTTRAP), and publicly available tools (SQLULDR2 and PINEGROVE) to achieve persistence, deliver additional payloads, and exfiltrate data of interest.

The web shells act as a conduit to download the DUSTPAN (aka StealthVector) dropper that's responsible for loading Cobalt Strike Beacon for command-and-control (C2) communication, followed by the deployment of the DUSTTRAP dropper post lateral movement.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

DUSTTRAP, for its part, is configured to decrypt a malicious payload and execute it in memory, which, in turn, establishes contact with an attacker-controlled server or a compromised Google Workspace account in an attempt to conceal its malicious activities.

Google said the identified Workspace accounts have been remediated to prevent unauthorized access. It, however, did not reveal how many accounts were affected.

The intrusions are also characterized by the use of SQLULDR2 to export data from Oracle Databases to a local text-based file and PINEGROVE to transmit large volumes of sensitive data from compromised networks by abusing Microsoft OneDrive as an exfiltration vector.

It's worth noting here that the malware families that Mandiant tracks as DUSTPAN and DUSTTRAP share overlaps with those that have been codenamed [DodgeBox and MoonWalk](https://thehackernews.com/2024/07/chinese-apt41-upgrades-malware-arsenal.html), respectively, by Zscaler ThreatLabz.

[![APT41 Hackers](data:image/png;base64... "APT41 Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1gIMnuUfAqkOgoe1j8BGQY3mbE4Uiiv3t-_nv2R9iaF3y8n9FhqFGIQuwse-E0GcUR5S10HAT6DWH94qEhGrdETYqaK9lx2lO5GKasMVljhah2Y9aCeE3_AZ6Pm5Wz1GVaba3Ebb2zzUWWe-t603jShzXyH_xiq2WqoO_YuKdPm-uMOndrRFxsOOh9pE4/s790-rw-e365/apt41.jpg)

"DUSTTRAP is a multi-stage plugin framework with multiple components," Mandiant researchers said, adding it identified at least 15 plugins that are capable of executing shell commands, carrying out file system operations, enumerating and terminating processes, capturing keystrokes and screenshots, gathering system information, and modifying Windows Registry.

It's also engineered to probe remote hosts, perform domain name system (DNS) lookups, list remote desktop sessions, upload files, and conduct various manipulations to Microsoft Active Directory.

"The DUSTTRAP malware and its associated components that were observed during the intrusion were code signed with presumably stolen code signing certificates," the company said. "One of the code signing certificates seemed to be related to a South Korean company operating in the gaming industry sector."

### GhostEmperor Comes Back to Haunt

The disclosure comes as Israeli cybersecurity company Sygnia revealed details of a cyber attack campaign mounted by a sophisticated China-nexus threat group called [GhostEmperor](https://thehackernews.com/2021/10/chinese-hackers-used-new-rootkit-to-spy.html) to deliver a variant of the Demodex rootkit.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The exact method used to breach targets is currently not clear, although the group has been previously observed exploiting known flaws in internet-facing applications. The initial access facilitates the execution of a Windows batch script, which drops a Cabinet archive (CAB) file to ultimately launch a core implant module.

The implant is equipped to manage C2 communications and install the Demodex kernel rootkit by using an open-source project named [Cheat Engine](https://www.cheatengine.org/) to get around the Windows Driver Signature Enforcement ([DSE](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/driver-signing)) mechanism.

"GhostEmperor employs a multi-stage malware to achieve stealth execution and persistence and utilizes several methods to impede analysis process," Security researcher Dor Nizar [said](https://www.sygnia.co/blog/ghost-emperor-demodex-rootkit/).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Sha...
---
title: New Flaws in Sonos Smart Speakers Allow Hackers to Eavesdrop on Users
url: https://thehackernews.com/2024/08/new-flaws-in-sonos-smart-speakers-allow.html
source: The Hacker News
date: 2024-08-10
fetch_date: 2025-10-06T18:07:50.617027
---

# New Flaws in Sonos Smart Speakers Allow Hackers to Eavesdrop on Users

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

# [Sonos Speaker Flaws Could Have Let Remote Hackers Eavesdrop on Users](https://thehackernews.com/2024/08/new-flaws-in-sonos-smart-speakers-allow.html)

**Aug 09, 2024**Ravie LakshmananIoT Security / Wireless Security

[![Sonos Smart Speakers](data:image/png;base64... "Sonos Smart Speakers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmdkbexYeO2wiKQenDeECq78vwBXeXTT6AQNas1zLhCNEMLr8dUYuv4ICYny-whcNXzRgq89ccD-2ar9cRbJOFV2pnEiGPcEtrvmbJePerIzX2Xs_ZyPWoOFI9To7ooLHRSqami6J0C1GmSnq92P6EkdsMWGyhJ_IgLJvLhl5xwoIryHvUKcQpYsGe-WTh/s790-rw-e365/exploit.png)

Cybersecurity researchers have uncovered weaknesses in Sonos smart speakers that could be exploited by malicious actors to clandestinely eavesdrop on users.

The vulnerabilities "led to an entire break in the security of Sonos's secure boot process across a wide range of devices and remotely being able to compromise several devices over the air," NCC Group security researchers Alex Plaskett and Robert Herrera [said](https://www.nccgroup.com/us/research-blog/blackhat-usa-2024-listen-up-sonos-over-the-air-remote-kernel-exploitation-and-covert-wiretap/).

Successful exploitation of one of these flaws could allow a remote attacker to obtain covert audio capture from Sonos devices by means of an over-the-air attack. They [impact all versions](https://www.sonos.com/en-gb/security-advisory-2024-0001) prior to Sonos S2 release 15.9 and Sonos S1 release 11.12, which were shipped in October and November 2023.

The findings were presented at Black Hat USA 2024. A description of the two security defects is as follows -

* **CVE-2023-50809** - A vulnerability in the Sonos One Gen 2 Wi-Fi stack that does not properly validate an information element while negotiating a WPA2 four-way handshake, leading to remote code execution

* **CVE-2023-50810** - A vulnerability in the U-Boot component of the Sonos Era-100 firmware that would allow for persistent arbitrary code execution with Linux kernel privileges

NCC Group, which reverse-engineered the boot process to achieve remote code execution on Sonos Era-100 and the Sonos One devices, said CVE-2023-50809 is the result of a memory corruption vulnerability in the Sonos One's wireless driver, which is a third-party chipset manufactured by MediaTek.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"In wlan driver, there is a possible out of bounds write due to improper input validation," MediaTek [said](https://corp.mediatek.com/product-security-bulletin/March-2024) in an advisory for CVE-2024-20018. "This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation."

The initial access obtained in this manner paves the way for a series of post-exploitation steps that include obtaining a full shell on the device to gain complete control in the context of root followed by deploying a novel Rust implant capable of capturing audio from the microphone within close physical proximity to the speaker.

The other flaw, CVE-2023-50810, relates to a chain of vulnerabilities identified in the secure boot process to breach Era-100 devices, effectively making it possible to circumvent security controls to allow for unsigned code execution in the context of the kernel.

[![Sonos Smart Speakers](data:image/png;base64... "Sonos Smart Speakers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjycVHHJVIiXF3RnjTuzQYo3Ess7MKcuPspuF7oQXn_WcvRvFtbSpAXN0StLslnOdgAQ24IVymUQ1HkCjcot8idSQplKbT6BSorRqrp5Rbe8K9kr-tk_WE6GrPpPODjXENgZ_anwxv891PeVOHCLxDkLBMxL66wGkWwO3E0t5meKlCiRfUWL8HOniEUBN2s/s790-rw-e365/attack.png)

This could then be combined with an N-day privilege escalation flaw to facilitate [ARM EL3 level](https://developer.arm.com/documentation/100935/0100/Switching-betwen-the-Normal-and-Secure-worlds-) code execution and extract hardware-backed cryptographic secrets.

"Overall, there are two important conclusions to draw from this research," the researchers said. "The first is that OEM components need to be of the same security standard as in-house components. Vendors should also perform threat modeling of all the external attack surfaces of their products and ensure that all remote vectors have been subject to sufficient validation."

"In the case of the secure boot weaknesses, then it is important to validate and perform testing of the boot chain to ensure that these weaknesses are not introduced. Both hardware and software-based attack vectors should be considered."

The disclosure comes as firmware security company Binarly revealed that hundreds of UEFI products from nearly a dozen vendors are susceptible to a critical firmware supply chain issue known as PKfail, which allows attackers to bypass Secure Boot and install malware.

Specifically, it found that [hundreds of products](https://github.com/binarly-io/SupplyChainAttacks/blob/main/PKfail/ImpactedDevices.md) use a test Platform Key generated by American Megatrends International (AMI), which was likely included in their reference implementation in hopes that it would be replaced with another safely-generated key by downstream entities in the supply chain.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The problem arises from the Secure Boot 'master key,' known as the Platform Key (PK) in UEFI terminology, which is untrusted because it is generated by Independent BIOS Vendors (IBVs) and shared among different vendors," it [said](https://www.binarly.io/blog/pkfail-untrusted-platform-keys-undermine-secure-boot-on-uefi-ecosystem), describing it as a cross-silicon issue affecting both x86 and ARM architectures.

"This Platform Key [...] is often not replaced by OEMs or device vendors, resulting in devices shipping with untrusted keys. An attacker with access to the private part of the PK can easily bypass Secure Boot by manipulating the Key Exchange Key (KEK) database, the Signature Database (db), and the Forbidden Signat...
---
title: Cisco Patches 12 SD-WAN and IOS XE Flaws, Including Three 9.8 CVSS Score Bugs
url: https://thehackernews.com/2026/08/cisco-patches-12-sd-wan-and-ios-xe.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:24.626452
---

# Cisco Patches 12 SD-WAN and IOS XE Flaws, Including Three 9.8 CVSS Score Bugs

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

![cybersecurity](data:image/svg+xml;base64...)

# [Cisco Patches 12 SD-WAN and IOS XE Flaws, Including Three 9.8 CVSS Score Bugs](https://thehackernews.com/2026/08/cisco-patches-12-sd-wan-and-ios-xe.html)

**Ravie Lakshmanan**Aug 06, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzkSwdiUeH8rB-KgSkEXrT-oNL19IyghM7Ks8UDOedxPYB5czgwO8pXNf0YUt7OHqAbRRDJkRvJffzJ0lfpEdqfLn-w-Bc9pwOa_1FNJjJkrVbD-diaZu9HRFqAlOBWogXEsZ4sSFRDW-HYmsaUmVD98QGQoyq2rHep_dwDa5ueafTUO0Lh6zsA-Czd3he/s1700-e365/cisco-flaws.jpg)

Cisco has [rolled out updates](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-L4XfJg8S) to address multiple critical security vulnerabilities impacting [Catalyst SD-WAN](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-sdwan-faLcR3K) and [IOS XE Software](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ) as part of a comprehensive internal security review.

The security issues affect Cisco Catalyst SD-WAN Software, regardless of device configuration, and Cisco IOS XE Software when it is running in autonomous or controller mode.

"These vulnerabilities were found during internal security testing using existing testing processes as well as frontier AI models [...] and are not known to be actively exploited," Cisco said, urging customers to apply the necessary updates for optimal protection.

The vulnerabilities impacting Catalyst SD-WAN Software are listed below -

* **CVE-2026-20303** (CVSS score: 9.9) - An improper input validation vulnerability (which also covers path traversals)
* **CVE-2026-20304** (CVSS score: 9.9) - An improper access control vulnerability
* **CVE-2026-20310** (CVSS score: 9.9) - An improper link resolution before file access vulnerability
* **CVE-2026-20312** (CVSS score: 8.8) - A cleartext storage of sensitive information vulnerability
* **CVE-2026-20313** (CVSS score: 7.7) - An improper validation of specified quantity in input

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The issues have been addressed in the following versions of Cisco Catalyst SD-WAN Software -

* 20.9 (Fixed in 20.9.10)
* 20.10 (Fixed in 20.12.8.1)
* 20.111 (Fixed in 20.12.8.1)
* 20.12 (Fixed in 20.12.8.1)
* 20.131 (Fixed in 20.15.6)
* 20.141 (Fixed in 20.15.6)
* 20.15 (Fixed in 20.15.6)
* 20.161 (Fixed in 20.18.4)
* 20.18 (Fixed in 20.18.4)
* 26.1 (Fixed in 26.1.2)
* Earlier than 20.9 (Migrate to a fixed release)

The vulnerabilities impacting IOS XE Software relate to improper access control, command injection, and improper input validation -

* **CVE-2026-20267** (CVSS score: 9.0) - An improper access control vulnerability
* **CVE-2026-20268** (CVSS score: 8.6) - A set of buffer overflow and out-of-bounds write vulnerabilities
* **CVE-2026-20269** (CVSS score: 8.6) - An improper control of a resource through its lifetime vulnerability
* **CVE-2026-20270** (CVSS score: 8.6) - An incorrect calculation vulnerability (which also covers arithmetic or numeric conversion errors including integer overflow, underflow, and truncation)
* **CVE-2026-20271** (CVSS score: 8.6) - An insufficient control flow management vulnerability (which also covers infinite loops, uncontrolled recursion, and race conditions)
* **CVE-2026-20272** (CVSS score: 9.8) - An improper neutralization of special elements vulnerability (which also covers command, operating system, and argument injection)
* **CVE-2026-20273** (CVSS score: 8.6) - An improper input validation vulnerability (which also covers path traversals)

The set of seven flaws has been addressed in the following versions of Cisco IOS XE Software -

* 17.9 (Fixed in 17.9.10)
* 17.12 (Fixed in 17.12.8)
* 17.15 (Fixed in 17.15.6)
* 17.18 (Fixed in 17.18.4 and 17.18.4a)
* 26.1 (Fixed in 26.1.2)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Separately, Cisco also [shipped fixes](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-arg-inject-upSHdMfU) to address a high-severity security flaw in the web-based management interface of Integrated Management Controller (IMC) (CVE-2026-20200) for which it acknowledged a [proof-of-concept (PoC) exploit](https://github.com/NSIDE-ATTACK-LOGIC/CIMCown) is available.

* **CVE-2026-20200** (CVSS score: 8.8) - An improper validation of user-supplied input that could allow an authenticated, remote attacker with low privileges to execute arbitrary commands on the underlying operating system of an affected system and elevate privileges to root.
* **CVE-2026-20288** (CVSS score: 6.5) - An improper validation of user-supplied input that could allow an authenticated, remote attacker with Admin privileges to execute arbitrary commands on the underlying operating system of an affected system and elevate privileges to root.

"One should be clear about what a compromise of the IMC means: the controller sits in a position where it can influence the BIOS and SecureBoot and interact with the operating system above it," security researcher Christoph Peil, who discovered and reported CVE-2026-20200, [said](https://www.nsideattacklogic.de/en/cisco-imc-when-remote-management-becomes-a-backdoor-cve-2026-20200/).

"An attacker who gains root here can thereby nest themselves deeply and persistently in the system – far below what classic protective measures such as EDR solutions at the operating-system level can even see. The trust anchor of the entire server hardware is thus compromised."

The disclosure comes less than a week after the network equipment company [warned](https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html) of active exploitation of CVE-2026-20316 (CVSS score: 5.3), a vulnerability in Cisco Secure Firewall Management Center (FMC) Software that could allow a low-privilege account to access sensitive data within susceptible systems.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read...
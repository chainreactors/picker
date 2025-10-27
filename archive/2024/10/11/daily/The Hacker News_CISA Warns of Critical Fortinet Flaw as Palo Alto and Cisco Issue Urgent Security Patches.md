---
title: CISA Warns of Critical Fortinet Flaw as Palo Alto and Cisco Issue Urgent Security Patches
url: https://thehackernews.com/2024/10/cisa-warns-of-critical-fortinet-flaw-as.html
source: The Hacker News
date: 2024-10-11
fetch_date: 2025-10-06T19:01:14.037911
---

# CISA Warns of Critical Fortinet Flaw as Palo Alto and Cisco Issue Urgent Security Patches

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

# [CISA Warns of Critical Fortinet Flaw as Palo Alto and Cisco Issue Urgent Security Patches](https://thehackernews.com/2024/10/cisa-warns-of-critical-fortinet-flaw-as.html)

**Oct 10, 2024**Ravie LakshmananVulnerability / Network Security

[![Security Patch Update](data:image/png;base64... "Security Patch Update")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiAS8cfUsAeLIZLCqWDZHwcEaL8iNUDWhNJAwRkWlRfFj1pvzvRlRez9DEirJ63SEPM9B8FZ4aUrpP3F7r5i0Be7FdWxPgm7zJQ33Zn4pxa-3LgxjBM_rYD5Q9qgGK9omvDFk50u8hDKa9voEWtmJdod9bQDRJlD2L5ocYDtXkcWSWzYnBwDkIIw6XyF40/s790-rw-e365/update.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday [added](https://www.cisa.gov/news-events/alerts/2024/10/09/cisa-adds-three-known-exploited-vulnerabilities-catalog) a critical security flaw impacting Fortinet products to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, citing evidence of active exploitation.

The vulnerability, tracked as **CVE-2024-23113** (CVSS score: 9.8), relates to a case of remote code execution that affects FortiOS, FortiPAM, FortiProxy, and FortiWeb.

"A use of externally-controlled format string vulnerability [CWE-134] in FortiOS fgfmd daemon may allow a remote unauthenticated attacker to execute arbitrary code or commands via specially crafted requests," Fortinet [noted](https://www.fortiguard.com/psirt/FG-IR-24-029) in an advisory for the flaw back in February 2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As is typically the case, the bulletin is sparse on details related to how the shortcoming is being exploited in the wild, or who is weaponizing it and against whom.

In light of active exploitation, Federal Civilian Executive Branch (FCEB) agencies are mandated to apply the vendor-provided mitigations by October 30, 2024, for optimum protection.

## Palo Alto Networks Discloses Critical Bugs in Expedition

The development comes as Palo Alto Networks disclosed multiple security flaws in Expedition that could allow an attacker to read database contents and arbitrary files, in addition to writing arbitrary files to temporary storage locations on the system.

"Combined, these include information such as usernames, cleartext passwords, device configurations, and device API keys of PAN-OS firewalls," Palo Alto Networks [said](https://security.paloaltonetworks.com/PAN-SA-2024-0010) in a Wednesday alert.

[![Fortinet Flaw](data:image/png;base64... "Fortinet Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxMC9rdnwCAejOmxSY4P5DCibw-uqLJGP3EdLrlrQpCa47CK-Nrsj9qOsw6Pl_jhJ2YvgIr7o6fkjBwl9b8fJkwIJDA5hERPfOnLNHnSjaB3VXrhq6g9BY4QfVmY3B6u98a5BjUSKzlyZQjwDsOK-OotPlO5s8ALg5wC9B3Kfx9g0nCSKVweTrMrZEx4Uf/s790-rw-e365/forti.png)

The vulnerabilities, which affect all versions of Expedition prior to 1.2.96, are listed below -

* **CVE-2024-9463** (CVSS score: 9.9) - An operating system (OS) command injection vulnerability that allows an unauthenticated attacker to run arbitrary OS commands as root

* **CVE-2024-9464** (CVSS score: 9.3) - An OS command injection vulnerability that allows an authenticated attacker to run arbitrary OS commands as root

* **CVE-2024-9465** (CVSS score: 9.2) - An SQL injection vulnerability that allows an unauthenticated attacker to reveal Expedition database contents

* **CVE-2024-9466** (CVSS score: 8.2) - A cleartext storage of sensitive information vulnerability that allows an authenticated attacker to reveal firewall usernames, passwords, and API keys generated using those credentials

* **CVE-2024-9467** (CVSS score: 7.0) - A reflected cross-site scripting (XSS) vulnerability that enables execution of malicious JavaScript in the context of an authenticated Expedition user's browser if that user clicks on a malicious link, allowing phishing attacks that could lead to Expedition browser session theft

The company credited Zach Hanley of Horizon3.ai for discovering and reporting CVE-2024-9464, CVE-2024-9465, and CVE-2024-9466, and Enrique Castillo of Palo Alto Networks for CVE-2024-9463, CVE-2024-9464, CVE-2024-9465, and CVE-2024-9467.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOJ8jJscbnLmxJBiyctTSU1v99rYGQ3u5Vcm2GqdOsoMgXxURXRS8D_NJyBgv9lGZ3vS2r6qyJS_uCyFK4MaSOJUkyxlwz4_fDxYue-LOBbbzkFf66CFUQOWYoMgyVkYLHKjLQoXQPxA5XM2VPaSF4J2RDyz8Pbq8Ura0H-zG0G5X0RLL206BqkC2PIAMM/s790-rw-e365/2.png)

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjdMHDBqRqs5X1TCqymmBMNOrO6SiYnC88E-M6obrlZRbYzJanv4x2Br_YAAouGC-ehthuAHCZqTqUKyxT61G-nNXZXcKqRP1XVZVh06xItAARI2_SdkwunI1Ofh2jifnEnkT0GRuITPSVhTJZsc748JLnMYAA30vpAh98xCpkzV8wgerRaNrCOxz9Obnp/s790-rw-e365/1.png)

There is no evidence that the issues have ever been exploited in the wild, although it said steps to [reproduce the problem](https://github.com/horizon3ai/CVE-2024-9464) are already in the public domain, courtesy of Horizon3.ai.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

There are approximately 23 Expedition servers [exposed](https://www.horizon3.ai/attack-research/palo-alto-expedition-from-n-day-to-full-compromise/) to the internet, most of which are located in the U.S., Belgium, Germany, the Netherlands, and Australia. As mitigations, it's recommended to limit access to authorized users, hosts, or networks, and shut down the software when not in active use.

## Cisco Fixes Nexus Dashboard Fabric Controller Flaw

Last week, Cisco also released patches to remediate a critical command execution flaw in Nexus Dashboard Fabric Controller (NDFC) that it said stems from an improper user authorization and insufficient validation of command arguments.

Tracked as **CVE-2024-20432** (CVSS score: 9.9), it could permit an authenticated, low-privileged, remote attacker to perform a command injection attack against an affected device. The flaw has been addressed in NDFC vers...
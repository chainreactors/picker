---
title: High-Severity Flaws in Juniper Junos OS Affect Enterprise Networking Devices
url: https://thehackernews.com/2022/10/high-severity-flaws-in-juniper-junos-os.html
source: The Hacker News
date: 2022-10-29
fetch_date: 2025-10-03T21:16:33.006489
---

# High-Severity Flaws in Juniper Junos OS Affect Enterprise Networking Devices

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

# [High-Severity Flaws in Juniper Junos OS Affect Enterprise Networking Devices](https://thehackernews.com/2022/10/high-severity-flaws-in-juniper-junos-os.html)

**Oct 28, 2022**Ravie Lakshmanan

[![Juniper SSL VPN and Junos OS](data:image/png;base64... "Juniper SSL VPN and Junos OS")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3qOpsmiXDN_m0o3gko2KN2DqcD_rSEUEI33OP4ZlAVcu8COcXCnBpqdHuGZV_Act9SNlxkAUQD2aFo8RMDAZWfHaFDydBeXKtbMLSi-_QiS9m_z6PKKj-qdB7AyH8ztdKwZ_dB3ClyNpBzIZq0w0akPVP8ejm3FPGP1McBsE9rwnFeXgwrn64nqWr/s790-rw-e365/juniper.jpg)

Multiple high-severity security flaws have been disclosed as affecting Juniper Networks devices, some of which could be exploited to achieve code execution.

Chief among them is a remote pre-authenticated PHP archive file deserialization vulnerability (CVE-2022-22241, CVSS score: 8.1) in the J-Web component of Junos OS, according to Octagon Networks researcher Paulos Yibelo.

"This vulnerability can be exploited by an unauthenticated remote attacker to get remote phar files deserialized, leading to arbitrary file write, which leads to a remote code execution (RCE)," Yibelo [said](https://octagon.net/blog/2022/10/28/juniper-sslvpn-junos-rce-and-multiple-vulnerabilities/) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Also identified are five other issues, which are listed as follow -

* **CVE-2022-22242** (CVSS score: 6.1) - A pre-authenticated reflected [XSS](https://owasp.org/www-community/attacks/xss/) on the error page ("error.php"), allowing a remote adversary to siphon Junos OS admin session and chained with other flaws that require authentication.

* **CVE-2022-22243** (CVSS score: 4.3) & **CVE-2022-22244** (CVSS score: 5.3) - Two [XPATH injection](https://owasp.org/www-community/attacks/XPATH_Injection) flaws that exploited by a remote authenticated attacker to steal and manipulate Junos OS admin sessions

* **CVE-2022-22245** (CVSS score: 4.3) - A path traversal flaw that could permit a remote authenticated attacker to upload PHP files to any arbitrary location, in a manner similar to that of the recently disclosed RARlab UnRAR flaw ([CVE-2022-30333](https://thehackernews.com/2022/06/new-unrar-vulnerability-could-let.html)), and

* **CVE-2022-22246** (CVSS score: 7.5) - A local file inclusion vulnerability that could be weaponized to run untrusted PHP code.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This [CVE-2022-22246] allows an attacker the ability to include any PHP file stored on the server," Yibelo noted. "If this vulnerability is exploited alongside the file upload vulnerability, it can lead to remote code execution."

Users of Juniper Networks firewalls, routers, and switches are recommended to [apply the latest software patch](https://www.juniper.net/documentation/product/us/en/junos-os/#cat=release_notes) available for Junos OS to mitigate aforementioned threats.

"One or more of these issues could lead to unauthorized local file access, cross-site scripting attacks, path injection and traversal, or local file inclusion," Juniper Networks [disclosed](https://supportportal.juniper.net/s/article/2022-10-Security-Bulletin-Junos-OS-Multiple-vulnerabilities-in-J-Web?language=en_US) in an advisory released on October 12, 2022.

The issues have been addressed in Junos OS versions 19.1R3-S9, 19.2R3-S6, 19.3R3-S7, 19.4R3-S9, 20.1R3-S5, 20.2R3-S5, 20.3R3-S5, 20.4R3-S4, 21.1R3-S2, 21.3R3, 21.4R3, 22.1R2, 22.2R1, and later.

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

[hacking](https://thehackernews.com/search/label/hacking)[Juniper](https://thehackernews.com/search/label/Juniper)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware...
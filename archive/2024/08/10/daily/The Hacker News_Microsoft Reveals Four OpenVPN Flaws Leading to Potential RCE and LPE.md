---
title: Microsoft Reveals Four OpenVPN Flaws Leading to Potential RCE and LPE
url: https://thehackernews.com/2024/08/microsoft-reveals-four-openvpn-flaws.html
source: The Hacker News
date: 2024-08-10
fetch_date: 2025-10-06T18:07:48.887004
---

# Microsoft Reveals Four OpenVPN Flaws Leading to Potential RCE and LPE

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

# [Microsoft Reveals Four OpenVPN Flaws Leading to Potential RCE and LPE](https://thehackernews.com/2024/08/microsoft-reveals-four-openvpn-flaws.html)

**Aug 09, 2024**Ravie LakshmananVulnerability / Network Security

[![OpenVPN](data:image/png;base64... "OpenVPN")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXHEh5gX-v17cFCWBugUtv8FEhA8bvFdlxPjretKGfVszryQPXWO1P5gLPAYkos2ja_tEmA_W_i5vOfvoe8V1w2BMvMhWyYt4FQaLMkJHdvT5ewCeU2bYXNsbpMOOUkhUsRCOdbT19qxdlxtGqZciYuN0f87s8Q7Ev3b_hhBIXWPKdsF0bPwf6YsS1R0kt/s790-rw-e365/openvpn.png)

Microsoft on Thursday disclosed four medium-severity security flaws in the open-source OpenVPN software that could be chained to achieve remote code execution (RCE) and local privilege escalation (LPE).

"This attack chain could enable attackers to gain full control over targeted endpoints, potentially resulting in data breaches, system compromise, and unauthorized access to sensitive information," Vladimir Tokarev of the Microsoft Threat Intelligence Community [said](https://www.microsoft.com/en-us/security/blog/2024/08/08/chained-for-attack-openvpn-vulnerabilities-discovered-leading-to-rce-and-lpe/).

That said, the exploit, presented by Black Hat USA 2024, requires user authentication and an advanced understanding of OpenVPN's inner workings. The flaws affect all versions of OpenVPN prior to version 2.6.10 and 2.5.10.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The [list of vulnerabilities](https://forums-new.openvpn.net/forum/announcements/69-release-openvpn-version-2-6-10) is as follows -

* CVE-2024-27459 - A stack overflow vulnerability leading to a Denial-of-service (DoS) and LPE in Windows
* CVE-2024-24974 - Unauthorized access to the "\\openvpn\\service" named pipe in Windows, allowing an attacker to remotely interact with it and launch operations on it
* CVE-2024-27903 - A vulnerability in the plugin mechanism leading to RCE in Windows, and LPE and data manipulation in Android, iOS, macOS, and BSD
* CVE-2024-1305 - A memory overflow vulnerability leading to DoS in Windows

The first three of the four flaws are rooted in a component named openvpnserv, while the last one resides in the Windows Terminal Access Point (TAP) driver.

[![OpenVPN](data:image/png;base64... "OpenVPN")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdQIqsgF0K5IzNNkCozlrCE8nCdwelDodqhyphenhyphen9zyD1KziGq9WADFGqd84mIB97QQCsZeDpf7G7xs1qHYlte_-t6iF5ZliFM0be9byQZ7jc-p2aW_QnqWxEEPJCW_Iv4NTaoBlhBXvAm5E-nE8QzgI6QEci-aJjjBARLeGawERVnYBTui3uOq-dP1hLJPWQJ/s790-rw-e365/hacker.png)

All the vulnerabilities can be exploited once an attacker gains access to a user's OpenVPN credentials, which, in turn, could be obtained through various methods, including purchasing stolen credentials on the dark web, using stealer malware, or sniffing network traffic to capture NTLMv2 hashes and then using cracking tools like HashCat or John the Ripper to decode them.

An attacker could then chain these flaws in different combinations -- CVE-2024-24974 and CVE-2024-27903 or CVE-2024-27459 and CVE-2024-27903 -- to achieve RCE and LPE, respectively.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"An attacker could leverage at least three of the four discovered vulnerabilities to create exploits to facilitate RCE and LPE, which could then be chained together to create a powerful attack chain," Tokarev said, adding they could employ methods like [Bring Your Own Vulnerable Driver](https://techcommunity.microsoft.com/t5/microsoft-security-experts-blog/strategies-to-monitor-and-prevent-vulnerable-driver-attacks/ba-p/4103985) ([BYOVD](https://thehackernews.com/2024/05/ghostengine-exploits-vulnerable-drivers.html)) after achieving LPE.

"Through these techniques, the attacker can, for instance, disable Protect Process Light (PPL) for a critical process such as Microsoft Defender or bypass and meddle with other critical processes in the system. These actions enable attackers to bypass security products and manipulate the system's core functions, further entrenching their control and avoiding detection."

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

[Android](https://thehackernews.com/search/label/Android)[Denial-of-Service](https://thehackernews.com/search/label/Denial-of-Service)[iOS](https://thehackernews.com/search/label/iOS)[MacOS](https://thehackernews.com/search/label/MacOS)[Microsoft](https://thehackernews.com/search/label/Microsoft)[NTLMv2](https://thehackernews.com/search/label/NTLMv2)[OpenVPN](https://thehackernews.com/search/label/OpenVPN)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense t...
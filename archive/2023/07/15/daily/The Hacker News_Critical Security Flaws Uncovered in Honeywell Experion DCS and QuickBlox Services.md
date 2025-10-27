---
title: Critical Security Flaws Uncovered in Honeywell Experion DCS and QuickBlox Services
url: https://thehackernews.com/2023/07/critical-security-flaws-uncovered-in.html
source: The Hacker News
date: 2023-07-15
fetch_date: 2025-10-04T11:55:40.624257
---

# Critical Security Flaws Uncovered in Honeywell Experion DCS and QuickBlox Services

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

# [Critical Security Flaws Uncovered in Honeywell Experion DCS and QuickBlox Services](https://thehackernews.com/2023/07/critical-security-flaws-uncovered-in.html)

**Jul 14, 2023**Ravie LakshmananVulnerability/ Cyber Threat

[![Vulnerability](data:image/png;base64... "Vulnerability")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgm1-6zs8Kn8AjrlkQgInmquW4XeJ5Y8r4aJ2qiB2fu6cOeSz4fRW2YppjT9S8y6nAkmpCgplxe96yqWYWdFfOIOhFXZwfzQ_6D3QFZGxpCsp6cMmLaC2zXaUv9C2PCwHGQ6o6y9d8eqaA2sR0vIlFG3azYrb2uZhduRPD7DQABeqN8r2IA9f1bZXGfJ4f/s790-rw-e365/email.jpg)

Multiple security vulnerabilities have been discovered in various services, including Honeywell Experion distributed control system (DCS) and QuickBlox, that, if successfully exploited, could result in severe compromise of affected systems.

Dubbed Crit.IX, the nine flaws in the Honeywell Experion DCS platform allow for "unauthorized remote code execution, which means an attacker would have the power to take over the devices and alter the operation of the DCS controller, whilst also hiding the alterations from the engineering workstation that manages the controller," Armis said in a statement shared with The Hacker News.

Put differently, the issues relate to lack of encryption and adequate authentication mechanisms in a proprietary protocol called Control Data Access (CDA) that's used to communicate between Experion Servers and C300 controllers, effectively enabling a threat actor to take over the devices and alter the operation of the DCS controller.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"As a result, anyone with access to the network is able to impersonate both the controller and the server," Tom Gol, CTO for research at Armis, [said](https://www.armis.com/blog/critix-9-vulnerabilities-discovered-in-honeywells-experionplatforms-for-distributed-control-systems-dcs/). " In addition, there are design flaws in the CDA protocol which make it hard to control the boundaries of the data and can lead to buffer overflows."

The U.S. Cybersecurity and Infrastructure Security Agency (CISA), in an advisory of its own, said seven of the nine flaws carry a CVSS score of 9.8 out 10, while the two others have a severity rating of 7.5. "Successful exploitation of these vulnerabilities could cause a denial-of-service condition, allow privilege escalation or allow remote code execution," it [warned](https://www.cisa.gov/news-events/ics-advisories/icsa-23-194-06).

In a related development, Check Point and Claroty uncovered major flaws in a chat and video calling platform known as QuickBlox that's widely used in telemedicine, finance, and smart IoT devices. The vulnerabilities could allow attackers to leak the user database from many popular applications that incorporate QuickBlox SDK and API.

This includes Rozcom, an Israeli vendor that sells intercoms for residential and commercial use cases. A closer examination of its mobile app led to the discovery of additional bugs ([CVE-2023-31184](https://nvd.nist.gov/vuln/detail/CVE-2023-31184) and [CVE-2023-31185](https://nvd.nist.gov/vuln/detail/CVE-2023-31185)) that made it possible to download all user databases, impersonate any user, and perform full account takeover attacks.

"As a result, we were able to take over all Rozcom intercom devices, giving us full control and allowing us to access device cameras and microphones, wiretap into its feed, open doors managed by the devices, and more," the researchers [said](https://research.checkpoint.com/2023/major-security-flaws-in-popular-quickblox-chat-and-video-framework-expose-sensitive-data-of-millions/).

Also disclosed this week are remote code execution flaws impacting [Aerohive/Extreme Networks access points](https://research.aurainfosec.io/pentest/bee-yond-capacity/) running HiveOS/Extreme IQ Engine versions before 10.6r2 and the open-source Ghostscript library ([CVE-2023-36664](https://nvd.nist.gov/vuln/detail/CVE-2023-36664), CVSS score: 9.8) that could result in the execution of arbitrary commands.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Ghostscript is a widely used but not necessarily widely known package," Kroll researcher Dave Truman [said](https://www.kroll.com/en/insights/publications/cyber/ghostscript-cve-2023-36664-remote-code-execution-vulnerability). "It can be executed in many different ways, from opening a file in a vector image editor such as Inkscape to printing a file via CUPS. This means that an exploitation of a vulnerability in Ghostscript might not be limited to one application or be immediately obvious."

Security shortcomings have also been made public in two Golang-based open-source platforms Owncast ([CVE-2023-3188](https://nvd.nist.gov/vuln/detail/CVE-2023-3188), CVSS score: 6.5) and EaseProbe ([CVE-2023-33967](https://nvd.nist.gov/vuln/detail/CVE-2023-33967), CVSS score: 9.8) that could pave the way for Server-Side Request Forgery ([SSRF](https://cwe.mitre.org/data/definitions/918.html)) and [SQL injection](https://cwe.mitre.org/data/definitions/89.html) attacks, respectively.

Rounding off the list is the discovery of hard-coded credentials in Technicolor TG670 DSL gateway routers that could be weaponized by an authenticated user to gain full administrative control of the devices.

"A remote attacker can use the default username and password to login as the administrator to the router device," CERT/CC [said](https://kb.cert.org/vuls/id/913565) in an advisory. "This allows the attacker to modify any of the administrative settings of the router and use it in unexpected ways."

Users are advised to disable remote administration on their devices to prevent potential exploitation attempts and check with the service providers to determine if appropriate patches and updates are available.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter]...
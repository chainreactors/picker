---
title: SolarWinds Patches 4 Critical Serv-U 15.5 Flaws Allowing Root Code Execution
url: https://thehackernews.com/2026/02/solarwinds-patches-4-critical-serv-u.html
source: The Hacker News
date: 2026-02-25
fetch_date: 2026-02-26T04:12:08.924278
---

# SolarWinds Patches 4 Critical Serv-U 15.5 Flaws Allowing Root Code Execution

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [SolarWinds Patches 4 Critical Serv-U 15.5 Flaws Allowing Root Code Execution](https://thehackernews.com/2026/02/solarwinds-patches-4-critical-serv-u.html)

**Ravie Lakshmanan**Feb 25, 2026Vulnerability / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJsxWsiu7fwprSIRxMv2GeyDwgjXKWppIf60pJICGIbw87BvlIEuh4P_8cWt1GXCcChC7u521YqP5RVa-3vV-Hs2djakl0xfjcRe5YAQPnrekGJBVrrdC8MKMcGKsG0YxOXZF15XUTTLXiEWhJViXZUnI2Rl2S9QLe3lUuautotpE8OhS1D6g2HfmAEI86/s1700-e365/solarwinds-serv-u.jpg)

SolarWinds has [released updates](https://documentation.solarwinds.com/en/success_center/servu/content/release_notes/servu_15-5-4_release_notes.htm) to address four critical security flaws in its Serv-U file transfer software that, if successfully exploited, could result in remote code execution.

The vulnerabilities, all rated 9.1 on the CVSS scoring system, are listed below -

* **[CVE-2025-40538](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40538)** - A broken access control vulnerability that allows an attacker to create a system admin user and execute arbitrary code as root via domain admin or group admin privileges.
* **[CVE-2025-40539](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40539)** - A type confusion vulnerability that allows an attacker to execute arbitrary native code as root.
* **[CVE-2025-40540](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40540)** - A type confusion vulnerability that allows an attacker to execute arbitrary native code as root.
* **[CVE-2025-40541](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40541)** - An insecure direct object reference (IDOR) vulnerability that allows an attacker to execute native code as root.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

SolarWinds noted that the vulnerabilities require administrative privileges for successful exploitation. It also said that they carry a medium security risk on Windows deployments as the services "frequently run under less-privileged service accounts by default."

The four shortcomings affect SolarWinds Serv-U version 15.5. They have been addressed in SolarWinds Serv-U version 15.5.4.

While SolarWinds makes no mention of the security flaws being exploited in the wild, prior vulnerabilities in the software ([CVE-2021-35211](https://thehackernews.com/2021/09/microsoft-says-chinese-hackers-were.html), [CVE-2021-35247](https://thehackernews.com/2022/01/microsoft-hackers-exploiting-new.html), and [CVE-2024-28995](https://thehackernews.com/2024/06/solarwinds-serv-u-vulnerability-under.html)) have been exploited by malicious actors, including by a China-based hacking group tracked as Storm-0322 (formerly DEV-0322).

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Serv-U](https://thehackernews.com/search/label/Serv-U), [SolarWinds](https://thehackernews.com/search/label/SolarWinds), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [windows security](https://thehackernews.com/search/label/windows%20security)

Trending News

[![OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond](data:image/svg+xml;base64... "OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond")

OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond](https://thehackernews.com/expert-insights/2026/01/ot-security-in-practice-4-crossindustry.html)

[![Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools](data:image/svg+xml;base64... "Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools")

Reynolds Ransomware Embeds BYOVD Driver to Disable EDR Security Tools](https://thehackernews.com/2026/02/reynolds-ransomware-embeds-byovd-driver.html)

[![Microsoft Patches 59 Vulnerabilities Including Six Actively Exploited Zero-Days](data:image/svg+xml;base64... "Microsoft Patches 59 Vulnerabilities Including Six Actively Exploited Zero-Days")

Microsoft Patches 59 Vulnerabilities Including Six Actively Exploited Zero-Days](https://thehackernews.com/2026/02/microsoft-patches-59-vulnerabilities.html)

[![SSHStalker Botnet Uses IRC C2 to Control Linux Systems via Legacy Kernel Exploits](data:image/svg+xml;base64... "SSHStalker Botnet Uses IRC C2 to Control Linux Systems via Legacy Kernel Exploits")

SSHStalker Botnet Uses IRC C2 to Control Linux Systems via Legacy Kernel Exploits](https://thehackernews.com/2026/02/sshstalker-botnet-uses-irc-c2-to.html)

[![First Malicious Outlook Add-In Found Stealing 4,000+ Microsoft Credentials](data:image/svg+xml;base64... "First Malicious Outlook Add-In Found Stealing 4,000+ Microsoft Credentials")

First Malicious Outlook Add-In Found Stealing 4,000+ Microsoft Credentials](https://thehackernews.com/2026/02/first-malicious-outlook-add-in-found.html)

[![ThreatsDay Bulletin: AI P...
---
title: Juniper Warns of Mirai Botnet Targeting SSR Devices with Default Passwords
url: https://thehackernews.com/2024/12/juniper-warns-of-mirai-botnet-targeting.html
source: The Hacker News
date: 2024-12-20
fetch_date: 2025-10-06T19:58:31.998023
---

# Juniper Warns of Mirai Botnet Targeting SSR Devices with Default Passwords

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

# [Juniper Warns of Mirai Botnet Targeting SSR Devices with Default Passwords](https://thehackernews.com/2024/12/juniper-warns-of-mirai-botnet-targeting.html)

**Dec 19, 2024**Ravie LakshmananMalware / Botnet

[![Mirai Botnet](data:image/png;base64... "Mirai Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXGS4s-l4PzLiM4vfSusTBptUPFvDdcmRGiBSagRLz22d0ccXUGNlVdCZTIMsGUR-IVvs_cOO-wKMR321GRA-lR5ME3fzIdg3XX9Pin-xzKLV8YpJ6ZATm_tUp5GUNj0nFve_DHrXnf5akUd_DJq15-j34oDS4g4YBupTnjgjUyo_Iy0OWuoW9GGlpMxt4/s790-rw-e365/ddos.png)

Juniper Networks is warning that Session Smart Router (SSR) products with default passwords are being targeted as part of a malicious campaign that deploys the Mirai botnet malware.

The company said it's issuing the advisory after "several customers" reported anomalous behavior on their Session Smart Network (SSN) platforms on December 11, 2024.

"These systems have been infected with the Mirai malware and were subsequently used as a DDoS attack source to other devices accessible by their network," it [said](https://supportportal.juniper.net/s/article/2024-12-Reference-Advisory-Session-Smart-Router-Mirai-malware-found-on-systems-when-the-default-password-remains-unchanged?language=en_US). "The impacted systems were all using default passwords."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Mirai](https://thehackernews.com/2024/10/new-gorilla-botnet-launches-over-300000.html), which has had its source code leaked in 2016, has spawned several variants over the years. The malware is capable of scanning for known vulnerabilities as well as default credentials to infiltrate devices and enlist them into a botnet for mounting distributed denial-of-service (DDoS) attacks.

To mitigate such threats, organizations are recommended to change their passwords with immediate effect to strong, unique ones (if not already), periodically audit access logs for signs of suspicious activity, use firewalls to block unauthorized access, and keep software up-to-date.

Some of the indicators associated with Mirai attacks include unusual port scanning, frequent SSH login attempts indicating brute-force attacks, increased outbound traffic volume to unexpected IP addresses, random reboots, and connections from known malicious IP addresses.

"If a system is found to be infected, the only certain way of stopping the threat is by reimaging the system as it cannot be determined exactly what might have been changed or obtained from the device," the company said.

The development comes as the AhnLab Security Intelligence Center (ASEC) revealed that poorly managed Linux servers, particularly publicly exposed SSH services, are being targeted by a previously undocumented DDoS malware family dubbed cShell.

"cShell is developed in the Go language and is characterized by exploiting Linux tools called screen and [hping3](https://www.kali.org/tools/hping3/) to perform DDoS attacks," ASEC [said](https://asec.ahnlab.com/en/85165/).

### DigiEver Flaw Exploited to Distribute Mirai Botnet Variant

In a new report published on December 19, 2024, Akamai revealed that a remote code execution vulnerability in DigiEver DS-2105 Pro DVRs (no CVE) is being exploited by attackers to spread a variant of the Mirai botnet dubbed "[Hail Cock](https://ducklingstudio.blog.fc2.com/blog-entry-394.html)" since at least October 2024. The botnet is estimated to have been active a month prior to the activity.

The vulnerability in question has been described as a post-auth arbitrary file write that works in combination with DVRs that have weak passwords. The malware installed on the devices subsequently proceeds to carry out Telnet and SSH brute-force attacks to broaden the size of the botnet.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Akamai told The Hacker News that it has not heard from the vendor yet to know if the DigiEver vulnerability has been patched. In addition to the code execution exploit, the campaign has been observed targeting other known vulnerabilities -

* [**CVE-2023-1389**](https://nvd.nist.gov/vuln/detail/cve-2023-1389) (CVSS score: 8.8), a command injection vulnerability affecting TP-Link routers
* [**CVE-2018-17532**](https://nvd.nist.gov/vuln/detail/cve-2018-17532) (CVSS score: 9.8), multiple unauthenticated operating system command injection vulnerabilities in Teltonika RUT9XX routers

"Cybercriminals have consistently leveraged the legacy of the Mirai malware to perpetuate botnet campaigns for years, and the new Hail Cock botnet is no exception," Akamai researchers Kyle Lefton, Daniel Messing, and Larry Cashdollar [said](https://www.akamai.com/blog/security-research/digiever-fix-that-iot-thing). "One of the easiest methods for threat actors to compromise new hosts is to target outdated firmware or retired hardware."

"The DigiEver DS-2105 Pro, which is approximately 10 years old now, is an example. Hardware manufacturers do not always issue patches for retired devices, and the manufacturer itself may sometimes be defunct."

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

[botnet](https://thehackernews.com/search/label/botnet)[cybersecur...
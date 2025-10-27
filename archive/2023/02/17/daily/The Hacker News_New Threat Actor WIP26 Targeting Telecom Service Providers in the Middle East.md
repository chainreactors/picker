---
title: New Threat Actor WIP26 Targeting Telecom Service Providers in the Middle East
url: https://thehackernews.com/2023/02/new-threat-actor-wip26-targeting.html
source: The Hacker News
date: 2023-02-17
fetch_date: 2025-10-04T07:17:16.895583
---

# New Threat Actor WIP26 Targeting Telecom Service Providers in the Middle East

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

# [New Threat Actor WIP26 Targeting Telecom Service Providers in the Middle East](https://thehackernews.com/2023/02/new-threat-actor-wip26-targeting.html)

**Feb 16, 2023**Ravie LakshmananCloud Security / Cyber Threat

[![cyber espionage](data:image/png;base64... "cyber espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuczo9JHqukyt8JvJzy6NILaYLF_jyBnScNLxmMIXxrXz628-BBbUzP40ILiu4IIIMT4EAf9lOt04DkYuVV4Wk_W_KiNQobAS1SwN4QabNuDPVhv3u2e0-h9A9A_K5NdakHHeT-x_cgKD_ESGfJmS8EUL4y4HHFA9BL3ct-x3Ct_E8eZjHzwO3YSgs/s790-rw-e365/mappp.png)

Telecommunication service providers in the Middle East are being targeted by a previously undocumented threat actor as part of a suspected intelligence gathering mission.

Cybersecurity firms SentinelOne and QGroup are tracking the activity cluster under the former's work-in-progress moniker **WIP26**.

"WIP26 relies heavily on public cloud infrastructure in an attempt to evade detection by making malicious traffic look legitimate," researchers Aleksandar Milenkoski, Collin Farr, and Joey Chen [said](https://www.sentinelone.com/labs/wip26-espionage-threat-actors-abuse-cloud-infrastructure-in-targeted-telco-attacks/) in a report shared with The Hacker News.

This includes the misuse of Microsoft 365 Mail, Azure, Google Firebase, and Dropbox for malware delivery, data exfiltration, and command-and-control (C2) purposes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The initial intrusion vector used in the attacks entails "precision targeting" of employees via WhatsApp messages that contain links to Dropbox links to supposedly benign archive files.

The files, in reality, harbor a malware loader whose core feature is to deploy custom .NET-based backdoors such as CMD365 or CMDEmber that leverage Microsoft 365 Mail and Google Firebase for C2.

[![cyber espionage](data:image/png;base64... "cyber espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXM4ixSDUldFcvOQVJ5j9WxTpvK3Ub9pu0wIECnhHZNJ8O1lccO0GPwyRsFDq9rlY93xHkT2KhheIfBMb7k1OPW7wyGkHOdV6y3lqp4u4FwEWMz0AcVJ0nOSqnGDC9Uf5dXhaVMAylnRQ411VMpS7LZFnjPzPek640ltfV07BLTo9gT-Zq-t-Bc8-h/s790-rw-e365/apps.png)

"The main functionality of CMD365 and CMDEmber is to execute attacker-provided system commands using the Windows command interpreter," the researchers said. "This capability was used to conduct a variety of activities, such as reconnaissance, privilege escalation, staging of additional malware, and data exfiltration."

CMD365, for its part, works by scanning the inbox folder for specific emails that begin with the subject line "input" to extract the C2 commands for execution on the infected hosts. CMDEmber, on the other hand, sends and receives data from the C2 server by issuing HTTP requests.

Transmitting the data – which comprises users' private web browser information and details about high-value hosts in the victim's network – to actor-controlled Azure instances is orchestrated by means of PowerShell commands.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The [abuse](https://thehackernews.com/2022/07/russian-hackers-using-dropbox-and.html) of [cloud services](https://thehackernews.com/2023/02/chinese-hackers-targeting-south.html) for nefarious ends is not unheard of, and the latest campaign from WIP26 indicates continued attempts on the part of threat actors to evade detection.

This is not the first time telecom providers in the Middle East have come under the radar of espionage groups. In December 2022, Bitdefender [disclosed](https://thehackernews.com/2022/12/chinese-hackers-target-middle-east.html) details of an operation dubbed **BackdoorDiplomacy** aimed at a telecom company in the region to siphon valuable data.

Then earlier this month, Trend Micro disclosed a set of targeted phishing attacks mounted by a group called [Earth Zhulong](https://www.trendmicro.com/en_us/research/23/b/earth-zhulong-familiar-patterns-target-southeast-asian-firms.html) aimed at telecom, technology, and media sectors in Southeast Asia since 2020 to deploy a shellcode loader known as ShellFang and a backdoor named MACAMAX.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hacking news](https://thehackernews.com/search/label/hacking%20news)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critica...
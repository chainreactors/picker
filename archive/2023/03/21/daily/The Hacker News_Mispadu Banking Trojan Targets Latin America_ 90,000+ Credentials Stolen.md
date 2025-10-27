---
title: Mispadu Banking Trojan Targets Latin America: 90,000+ Credentials Stolen
url: https://thehackernews.com/2023/03/mispadu-banking-trojan-targets-latin.html
source: The Hacker News
date: 2023-03-21
fetch_date: 2025-10-04T10:11:52.856206
---

# Mispadu Banking Trojan Targets Latin America: 90,000+ Credentials Stolen

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

# [Mispadu Banking Trojan Targets Latin America: 90,000+ Credentials Stolen](https://thehackernews.com/2023/03/mispadu-banking-trojan-targets-latin.html)

**Mar 20, 2023**Ravie LakshmananCyber Threat / Malware

[![Mispadu](data:image/png;base64... "Mispadu")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7--lSsudjeN4rSAwQ4LX_bbwU79y7qy-aI9Rd8m0o8XtD0P6Dwh41ZapIVMhrcm2eQ3RFhsNBHW-SRME2hsbw4g3r0ZuqWSyIOPPjl7bz_qXc93tv3bGhX7jvNqDexwKI5LbPZxZcYhDf3clhs9GX17sLOhbliHip72dm1jjwv_0-I7HSPVc4Aze4/s790-rw-e365/pc.png)

A banking trojan dubbed **Mispadu** has been linked to multiple spam campaigns targeting countries like Bolivia, Chile, Mexico, Peru, and Portugal with the goal of stealing credentials and delivering other payloads.

The activity, which commenced in August 2022, is currently ongoing, the Ocelot Team from Latin American cybersecurity firm Metabase Q said in a [report](https://www.metabaseq.com/mispadu-banking-trojan/) shared with The Hacker News.

[Mispadu](https://csirt.gob.cl/alertas/2cmv23-00398-01/) (aka URSA) was [first documented](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/) by ESET in November 2019, describing its ability to perpetrate monetary and credential theft and act as a backdoor by taking screenshots and capturing keystrokes.

"One of their main strategies is to compromise legitimate websites, searching for vulnerable versions of WordPress, to turn them into their command-and-control server to spread malware from there, filtering out countries they do not wish to infect, dropping different type of malware based on the country being infected," researchers Fernando García and Dan Regalado said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's also said to [share similarities](https://seguranca-informatica.pt/ursa-trojan-is-back-with-a-new-dance/) with other banking trojans targeting the region, like [Grandoreiro](https://thehackernews.com/2022/08/new-grandoreiro-banking-malware.html), [Javali](https://seguranca-informatica.pt/latin-american-javali-trojan-weaponizing-avira-antivirus-legitimate-injector-to-implant-malware/), and [Lampion](https://seguranca-informatica.pt/new-release-of-lampion-trojan-spreads-in-portugal-with-some-improvements-on-the-vbs-downloader/). Attack chains involving the Delphi malware leverage email messages urging recipients to open fake overdue invoices, thereby triggering a multi-stage infection process.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSS-VZpEpuJWPJEYR-Y1wTZPaW0PYRPf4uRLkQSgDlkBLP_AcpT56TXTit4gRNvIME-xs_zb1fFeBT4pIZfOcnNE3Z3tV85OW6wLeu60YBXtRpOLK4qYw3_Y6FxYgirYyavf25Y_ODX9K_GcE1MzpWwIRVFH-8LKIqAUjO7jPzYCq4c70MT5ZQozWV/s790-rw-e365/ndfs.png)

Should a victim open the HTML attachment sent via the spam email, it verifies that the file was opened from a desktop device and then redirects to a remote server to fetch the first-stage malware.

The RAR or ZIP archive, when launched, is designed to make use of rogue digital certificates – one which is the Mispadu malware and the other, an AutoIT installer – to decode and execute the trojan by abusing the legitimate [certutil command-line utility](https://attack.mitre.org/techniques/T1140/).

Mispadu is equipped to gather the list of antivirus solutions installed on the compromised host, siphon credentials from Google Chrome and Microsoft Outlook, and facilitate the retrieval of additional malware.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This includes an obfuscated Visual Basic Script dropper that serves to download another payload from a hard-coded domain, a .NET-based remote access tool that can run commands issued by an actor-controlled server, and a loader written in Rust that, in turn, executes a PowerShell loader to run files directly from memory.

What's more, the malware utilizes malicious overlay screens to obtain credentials associated with online banking portals and other sensitive information.

Metabase Q noted that the certutil approach has allowed Mispadu to bypass detection by a wide range of security software and harvest over 90,000 bank account credentials from over 17,500 unique websites.

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

[Android](https://thehackernews.com/search/label/Android)[Banking Trojan](https://thehackernews.com/search/label/Banking%20%20Trojan)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Cr...
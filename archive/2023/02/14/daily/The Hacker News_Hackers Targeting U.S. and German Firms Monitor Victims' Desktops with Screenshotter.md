---
title: Hackers Targeting U.S. and German Firms Monitor Victims' Desktops with Screenshotter
url: https://thehackernews.com/2023/02/hackers-targeting-us-and-german-firms.html
source: The Hacker News
date: 2023-02-14
fetch_date: 2025-10-04T06:33:42.771594
---

# Hackers Targeting U.S. and German Firms Monitor Victims' Desktops with Screenshotter

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

# [Hackers Targeting U.S. and German Firms Monitor Victims' Desktops with Screenshotter](https://thehackernews.com/2023/02/hackers-targeting-us-and-german-firms.html)

**Feb 13, 2023**Ravie LakshmananCyber Attack / Cyber Risk

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-t65CPCdOmL4W0GO4ZUeWynZscuox8dEL-_B0ROxpF0Dblk545dxLea1ej68BFNKzJYJFE9WdSwfWrxqLcXAVT4z-K1PtBaPlbh8LbMRs5bqWG0L5XcnCxoqPEhBjSpMLTsJ7SPYycaC91gOKw1pQrpzORxQS3V7ufhq2OjyCN9w6xAUeSyFMxufT/s790-rw-e365/malwareee.jpg)

A previously unknown threat actor has been targeting companies in the U.S. and Germany with bespoke malware designed to steal confidential information.

Enterprise security company Proofpoint, which is tracking the activity cluster under the name **Screentime**, said the group, dubbed **TA866**, is likely financially motivated.

"TA866 is an organized actor able to perform well thought-out attacks at scale based on their availability of custom tools; ability and connections to purchase tools and services from other vendors; and increasing activity volumes," the company [assessed](https://www.proofpoint.com/us/blog/threat-insight/screentime-sometimes-it-feels-like-somebodys-watching-me).

Campaigns mounted by the adversary are said to have commenced around October 3, 2022, with the attacks launched via emails containing a booby-trapped attachment or URL that leads to malware. The attachments range from macro-laced Microsoft Publisher files to PDFs with URLs pointing to JavaScript files.

The intrusions have also leveraged conversation hijacking to entice recipients into clicking on seemingly innocuous URLs that initiate a multi-step attack chain.

Irrespective of the method used, executing the downloaded JavaScript file leads to an MSI installer that unpacks a VBScript dubbed WasabiSeed, which functions as a tool to fetch next-stage malware from a remote server.

One of the payloads downloaded by WasabiSeed is Screenshotter, a utility that's tasked with taking screenshots of the victim's desktop periodically and transmitting that information back to a command-and-control (C2) server.

"This is helpful to the threat actor during the reconnaissance and victim profiling stage," Proofpoint researcher Axel F said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A successful reconnaissance phase is followed by the distribution of more malware for post-exploitation, with select attacks deploying an AutoHotKey (AHK)-based bot to drop an information stealer named [Rhadamanthys](https://threatmon.io/rhadamanthys-stealer-analysis-threatmon/).

Proofpoint said the URLs used in the campaign involved a traffic direction system ([TDS](https://thehackernews.com/2022/06/researchers-uncover-malware-controlling.html)) called 404 TDS, enabling the adversary to serve malware only in scenarios where the victims meet a specific set of criteria, such as geography, browser application, and operating system.

The [origins](https://thehackernews.com/2022/03/hackers-try-to-hack-european-officials.html) of TA866 remain unclear as yet, although Russian language variable names and comments have been identified in the source code of AHK Bot, a 2020 variant of which was employed in attacks aimed at [Canadian and U.S. banks](https://thehackernews.com/2020/12/autohotkey-based-password-stealer.html). The malware is also suspected to have been put to use [as far back as](https://www.trendmicro.com/en_us/research/19/d/potential-targeted-attack-uses-autohotkey-and-malicious-script-embedded-in-excel-file-to-avoid-detection.html) [April 2019](https://research.checkpoint.com/2019/finteam-trojanized-teamviewer-against-government-targets/).

"The use of Screenshotter to gather information on a compromised host before deploying additional payloads indicates the threat actor is manually reviewing infections to identify high-value targets," Proofpoint said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiixCLHkLHcD5sRFniVqf9JcoHVMWiOssWRUQcWlkI6_QwSWcgln-KkHgEFtSxGxX2JG7jFEyBdT3PItYoO_gwThLuAAKhkcqmBVgNcyIpe9W6bvDNFBxfOSKyHfb0TQI3ECxiwrFuaonPtSrjOplWMZmOaKR-apRLLIKzV-1J1Ooe5lQ-v2_wcsBaj/s790-rw-e365/flow.png)

"It is important to note that in order for a compromise to be successful, a user has to click on a malicious link and, if successfully filtered, interact with a JavaScript file to download and run additional payloads."

The findings come amid a spike in threat actors [trying](https://www.silentpush.com/blog/silent-push-uncovers-a-russian-ursnifgozi-banking-trojan-operation-targeting-global-anydesk-users) [out](https://www.silentpush.com/blog/threat-actors-continue-to-exploit-malvertising-and-brand-spoofing-to-deploy-infostealers-and-propagate-crypto-fraud) [new ways](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/crypto-inspired-magecart-skimmer-surfaces-via-digital-crime-haven) to execute code on targets' devices after [Microsoft blocked macros](https://thehackernews.com/2022/07/hackers-opting-new-attack-methods-after.html) by default in Office files downloaded from the internet.

This includes the use of search engine optimization (SEO) poisoning, malvertising, and brand spoofing to distribute malware by packaging the payloads as popular software such as remote desktop apps and online meeting platforms.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Furthermore, [rogue ads](https://thehackernews.com/2023/02/formbook-malware-spreads-via.html) on Google search results are being used to redirect unsuspecting users to fraudulent credential phishing websites that are designed to steal Amazon Web Services (AWS) logins, according to a new campaign documented by SentinelOne.

"The proliferation of malicious Google Ads leading to AWS phishing websites represents a serious threat to not just average users, but network and cloud administrators," the cybersecurity company [said](https://www.sentinelone...
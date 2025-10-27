---
title: YoroTrooper Stealing Credentials and Information from Government and Energy Organizations
url: https://thehackernews.com/2023/03/yorotrooper-stealing-credentials-and.html
source: The Hacker News
date: 2023-03-16
fetch_date: 2025-10-04T09:46:13.965962
---

# YoroTrooper Stealing Credentials and Information from Government and Energy Organizations

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

# [YoroTrooper Stealing Credentials and Information from Government and Energy Organizations](https://thehackernews.com/2023/03/yorotrooper-stealing-credentials-and.html)

**Mar 15, 2023**Ravie LakshmananCyber Espionage / Data Security

[![YoroTrooper](data:image/png;base64... "YoroTrooper")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrvAHCeUCjHtoZwQfrdV_OzrNHEU1Ip34dT3Ly5LsGLZNRw1PJ4--ZpU-WrxBD5aMr0LxEm6iHnDPoHcZDwjrwu8FrIF-2Zr8tkPpFcHsoM0Eep6bpyAiJZmFbxwWzmiFNyVuysxcJxygQY5oZea4srH1cvzW9DtNPobMTXjC3VIe5RcvbAloct02_/s790-rw-e365/python.png)

A previously undocumented threat actor dubbed **YoroTrooper** has been targeting government, energy, and international organizations across Europe as part of a cyber espionage campaign that has been active since at least June 2022.

"Information stolen from successful compromises include credentials from multiple applications, browser histories and cookies, system information and screenshots," Cisco Talos researchers Asheer Malhotra and Vitor Ventura [said](https://blog.talosintelligence.com/yorotrooper-espionage-campaign-cis-turkey-europe/) in a Tuesday analysis.

Prominent countries targeted include Azerbaijan, Tajikistan, Kyrgyzstan, Turkmenistan, and other Commonwealth of Independent States (CIS) nations.

The threat actor is believed to be Russian-speaking owing to the victimology patterns and the presence of Cyrillic snippets in some of the implants.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

That said, the YoroTrooper intrusion set has been found to exhibit tactical overlaps with the [PoetRAT team](https://blog.talosintelligence.com/poetrat-update/) that was [documented](https://thehackernews.com/2020/04/coronavirus-scada-malware.html) in 2020 as leveraging coronavirus-themed baits to strike government and energy sectors in Azerbaijan.

YoroTrooper's data gathering goals are realized through a combination of commodity and open source stealer malware such as [Ave Maria](https://www.huntress.com/blog/ave-maria-and-the-chambers-of-warzone-rat) (aka Warzone RAT), [LodaRAT](https://thehackernews.com/2022/11/lodarat-malware-resurfaces-with-new.html), Meterpreter, and [Stink](https://github.com/FallenAstaroth/stink), with the infection chains using malicious shortcut files (LNKs) and decoy documents wrapped in ZIP or RAR archives that are propagated via spear-phishing.

[![YoroTrooper](data:image/png;base64... "YoroTrooper")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_dykgzNdD6Yic9Mc1ib_JMBom9ZB-eMvTnKAkkipwuKYJMqL2ChQXUNTL_sNrSfrPBm0Ph6R_UMXBiVaxBvt9oQ_iRk04xNJJpMAPwZlh1D57q7doPk-ykeycotiUfSYdZQe9IyodHu29W94CO6cNIw57pAeSYKWaSHibfYvIOr3421i0-5Fxkjji/s790-rw-e365/talos.png)

The LNK files function as simple downloaders to execute an [HTA file](https://en.wikipedia.org/wiki/HTML_Application) retrieved from a remote server, which is then used to display a lure PDF document, while stealthily launching a dropper to deliver a custom stealer that uses Telegram as an exfiltration channel.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The use of LodaRAT is notable as it indicates that the malware is being employed by multiple operators despite its attribution to another group called Kasablanka, which has also been observed [distributing Ave Maria](https://ti.qianxin.com/blog/articles/Kasablanka-Group-Probably-Conducted-Compaigns-Targeting-Russia/) in recent campaigns targeting Russia.

Other auxiliary tools deployed by YoroTrooper consist of reverse shells and a C-based custom keylogger that's capable of recording keystrokes and saving them to a file on disk.

"It is worth noting that while this campaign began with the distribution of commodity malware such as Ave Maria and LodaRAT, it has evolved significantly to include Python-based malware," the researchers said.

"This highlights an increase in the efforts the threat actor is putting in, likely derived from successful breaches during the course of the campaign."

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

[Cisco Talos](https://thehackernews.com/search/label/Cisco%20Talos)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exp...
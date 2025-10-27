---
title: UNG0002 Group Hits China, Hong Kong, Pakistan Using LNK Files and RATs in Twin Campaigns
url: https://thehackernews.com/2025/07/ung0002-group-hits-china-hong-kong.html
source: The Hacker News
date: 2025-07-19
fetch_date: 2025-10-06T23:54:47.999839
---

# UNG0002 Group Hits China, Hong Kong, Pakistan Using LNK Files and RATs in Twin Campaigns

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

# [UNG0002 Group Hits China, Hong Kong, Pakistan Using LNK Files and RATs in Twin Campaigns](https://thehackernews.com/2025/07/ung0002-group-hits-china-hong-kong.html)

**Jul 18, 2025**Ravie LakshmananCyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUyRvWULXBF5SvL3X7Q6HpcHWAngP_fGmfVyBHHmP-7vORPmjm3EbTqVxKyEtgJ7OyAn7TFtXwaAcBM_gf8VgR0UO4mmsvC9RimrYDyOaPJgMc2Nycpjf2VCXe7fbv2szL97qDGKpWTi9iFgXbdMyrDe93MYiL6r9Zy2_4okww9ua4YluKqdzV_gw3lOjK/s790-rw-e365/cyber.jpg)

Multiple sectors in China, Hong Kong, and Pakistan have become the target of a threat activity cluster tracked as UNG0002 (aka Unknown Group 0002) as part of a broader cyber espionage campaign.

"This threat entity demonstrates a strong preference for using shortcut files (LNK), VBScript, and post-exploitation tools such as Cobalt Strike and Metasploit, while consistently deploying CV-themed decoy documents to lure victims," Seqrite Labs researcher Subhajeet Singha [said](https://www.seqrite.com/blog/ung0002-espionage-campaigns-south-asia/) in a report published this week.

The activity encompasses two major campaigns, one called Operation Cobalt Whisper which took place between May and September 2024, and Operation AmberMist that occurred between January and May 2025.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Targets of these campaigns include defense, electrotechnical engineering, energy, civil aviation, academia, medical institutions, cybersecurity, gaming, and software development sectors.

Operation Cobalt Whisper was [first documented](https://thehackernews.com/2025/04/weekly-recap-critical-sap-exploit-ai.html#:~:text=Lotus%20Panda%20Targets%20Southeast%20Asia%20With%20Sagerunex) by Seqrite Labs in late October 2024, detailing the use of ZIP archives propagated via spear-phishing attacks to deliver Cobalt Strike beacons, a post-exploitation framework, using LNK and Visual Basic Scripts as interim payloads.

"The scope and complexity of the campaign, coupled with the tailored lures, strongly suggest a targeted effort by an APT group to compromise sensitive research and intellectual property in these industries," the company noted at the time.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOCWDJBfHetbJMJGyNPDSPm2T_CL3LiAWoqviygJpIF6M5x7co4dYaxkrB_nlS_Re8YYw6tDEjK-Spnb6fuApGdTOtHgLJkiF2r8jOdqrvEguGUZPgRk4LAG85CzIF9HfpyfH6rxvMMZXJgyvvlF3O0qzSEeOBAaJ48g-azfXu7uIUDb2F45c5VXI5WJcK/s790-rw-e365/map.png)

The AmberMist attack chains have been found to leverage spear-phishing emails as a starting point to deliver LNK files masquerading as curriculum vitae and resumes to unleash a multi-stage infection process that results in the deployment of INET RAT and Blister DLL loader.

Alternate attack sequences detected in January 2025 have been found to redirect email recipients to fake landing pages spoofing Pakistan's Ministry of Maritime Affairs (MoMA) website to serve fake CAPTCHA verification checks that employ ClickFix tactics to launch PowerShell commands, which are used to execute Shadow RAT.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Shadow RAT, launched via DLL side-loading, is capable of establishing contact with a remote server to await further commands. INET RAT is assessed to be a modified version of Shadow RAT, whereas the Blister DLL implant functions as a shellcode loader, eventually paving the way for a reverse-shell based implant.

The exact origins of the threat actor remain unclear, but evidence points to it being an espionage-focused group from Southeast Asia.

"UNG0002 represents a sophisticated and persistent threat entity from South Asia that has maintained consistent operations targeting multiple Asian jurisdictions since at least May 2024," Singha said. "The group demonstrates high adaptability and technical proficiency, continuously evolving their toolset while maintaining consistent tactics, techniques, and procedures."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat)[china](https://thehackernews.com/search/label/china)[Cobalt Strike](https://thehackernews.com/search/label/Cobalt%20Strike)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Hong Kong](https://thehackernews.com/search/label/Hong%20Kong)[Malware](https://thehackernews.com/search/label/Malware)[pakistan](https://thehackernews.com/search/label/pakistan)[Seqrite Labs](https://thehackernews.com/search/label/Seqrite%20Labs)[Shadow RAT](https://thehackernews.com/search/label/Shadow%20RAT)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Resp...
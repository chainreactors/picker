---
title: New Cyber Threat Targets Azerbaijan and Israel Diplomats, Stealing Sensitive Data
url: https://thehackernews.com/2024/08/new-cyber-threat-targets-azerbaijan-and.html
source: The Hacker News
date: 2024-08-16
fetch_date: 2025-10-06T18:07:16.744397
---

# New Cyber Threat Targets Azerbaijan and Israel Diplomats, Stealing Sensitive Data

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

# [New Cyber Threat Targets Azerbaijan and Israel Diplomats, Stealing Sensitive Data](https://thehackernews.com/2024/08/new-cyber-threat-targets-azerbaijan-and.html)

**Aug 15, 2024**Ravie LakshmananCyber Espionage / Data Theft

[![Azerbaijan and Israel Diplomats](data:image/png;base64... "Azerbaijan and Israel Diplomats")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiv8fPALFIlsVGUSdQqvKBUBgCT-svByqAzkZRllTvEi4Ddq5ksxC3SA3SzN1ErP3Eqjeg8OQUa9jQSxrcQPg-yGg3NWbmWg-NHlxOM7jhUKM9g4vwnfEfM523oMWAFEWbdgHU2r0C79llWKxCI36kFYzOzeBAzhxc3FHYl_eHI4_lh1WHtDXP7xXMErNN/s790-rw-e365/cyber-threat.png)

A previously unknown threat actor has been attributed to a spate of attacks targeting Azerbaijan and Israel with an aim to steal sensitive data.

The attack campaign, detected by NSFOCUS on July 1, 2024, leveraged spear-phishing emails to single out Azerbaijani and Israeli diplomats. The activity is being tracked under the moniker **Actor240524**.

"Actor240524 possesses the ability to steal secrets and modify file data, using a variety of countermeasures to avoid overexposure of attack tactics and techniques," the cybersecurity company [said](https://nsfocusglobal.com/new-apt-group-actor240524-a-closer-look-at-its-cyber-tactics-against-azerbaijan-and-israel/) in an analysis published last week.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack chains commence with the use of phishing emails bearing Microsoft Word documents that, upon opening, urge the recipients to "[Enable Content](https://thehackernews.com/2024/06/hackers-use-ms-excel-macro-to-launch.html)" and run a malicious macro responsible for executing an intermediate loader payload codenamed ABCloader ("MicrosoftWordUpdater.log").

In the next step, ABCloader acts as a conduit to decrypt and load a DLL malware called ABCsync ("synchronize.dll"), which then establishes contact with a remote server ("185.23.253[.]143") to receive and run commands.

[![Azerbaijan and Israel Diplomats](data:image/png;base64... "Azerbaijan and Israel Diplomats")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiOdjzEZ0dJV1jYMcUsaHvsLqAT6Y8prz6zxz60yx8jBSwP9Zmm1V_lwBWSlAQaqYxXf5YDQMUjAvdx24yUN3_P6JJYjykZ1QqHZUb7aERbHll2QN1V2l0XAL4No9a278D9npisbx6LnOttR6oezcl3ibvtclGr7qGp3Jxtc1Hh3T77kxlIv1akxUHlUKz/s790-rw-e365/exe.png)

"Its main function is to determine the running environment, decrypt the program, and load the subsequent DLL (ABCsync)," NSFOCUS said. "It then performs various anti-sandbox and anti-analysis techniques for environmental detection."

Some of the prominent functions of ABCsync are to execute remote shells, run commands using cmd.exe, and exfiltrate system information and other data.

Both ABCloader and ABCsync have been observed employing techniques like string encryption to cloak important file paths, file names, keys, error messages, and command-and-control (C2) addresses. They also carry out several checks to determine if the processes are being debugged or executed in a virtual machine or sandbox by validating the display resolution.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Another crucial step taken by Actor240524 is that it inspects if the number of processes running in the compromised system is less than 200, and if so, it exits the malicious process.

ABCloader is also designed to launch a similar loader called "synchronize.exe" and a DLL file named "vcruntime190.dll" or "vcruntime220.dll," which are capable of setting up persistence on the host.

"Azerbaijan and Israel are allied countries with close economic and political exchanges," NSFOCUS said. "Actor240524's operation this time is likely aimed at the cooperative relationship between the two countries, targeting phishing attacks on diplomatic personnel of both countries."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[data theft](https://thehackernews.com/search/label/data%20theft)[Malware](https://thehackernews.com/search/label/Malware)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Maliciou...
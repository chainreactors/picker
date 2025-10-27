---
title: New Golang-Based Backdoor Uses Telegram Bot API for Evasive C2 Operations
url: https://thehackernews.com/2025/02/new-golang-based-backdoor-uses-telegram.html
source: The Hacker News
date: 2025-02-18
fetch_date: 2025-10-06T20:49:21.649495
---

# New Golang-Based Backdoor Uses Telegram Bot API for Evasive C2 Operations

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

# [New Golang-Based Backdoor Uses Telegram Bot API for Evasive C2 Operations](https://thehackernews.com/2025/02/new-golang-based-backdoor-uses-telegram.html)

**Feb 17, 2025**Ravie LakshmananThreat Intelligence / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiq0khCMfCXQk11NSKiQqxNDhGDhmNxovCmsYhkol67j_MlG40lVqQJnlkLyxEXGvj7Z1gFlN82JNgOT5WdqRy9wn2b9kU2drvBWzrxoNEv_nE718udyMQ8NwvXhs1g5SSEPAWRSQdx6oR3W-_0_nWtCt9Gd46VI9xmo6kNwWfd4q69Z-fd5h48kL82YSVi/s790-rw-e365/malware.png)

Cybersecurity researchers have shed light on a new Golang-based backdoor that uses Telegram as a mechanism for command-and-control (C2) communications.

Netskope Threat Labs, which detailed the functions of the malware, described it as possibly of Russian origin.

"The malware is compiled in Golang and once executed it acts like a backdoor," security researcher Leandro Fróes [said](https://www.netskope.com/blog/telegram-abused-as-c2-channel-for-new-golang-backdoor) in an analysis published last week. "Although the malware seems to still be under development it is completely functional."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Once launched, the backdoor is designed to check if it's running under a specific location and using a specific name – "C:\Windows\Temp\svchost.exe" – and if not, it reads its own contents, writes them to that location, and creates a new process to launch the copied version and terminate itself.

A notable aspect of the malware is that it uses an [open-source library](https://github.com/go-telegram-bot-api/telegram-bot-api) that offers Golang bindings for the Telegram Bot API for C2 purposes.

This involves interacting with the Telegram Bot API to receive new commands originating from an actor-controlled chat. It supports four different commands, although only three of them are currently implemented -

* /cmd - Execute commands via PowerShell
* /persist - Relaunch itself under "C:\Windows\Temp\svchost.exe"
* /screenshot - Not implemented
* /selfdestruct - Delete the "C:\Windows\Temp\svchost.exe" file and terminate itself

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The output of these commands is sent back to the Telegram channel. Netskope said that the "/screenshot" command sends the message "Screenshot captured" despite it not being fully fleshed out.

The Russian roots of the malware are explained by the fact that the "/cmd" instruction sends the message "Enter the command:" in Russian to the chat.

"The use of cloud apps presents a complex challenge to defenders and attackers are aware of it," Fróes said. "Other aspects such as how easy it is to set and start the use of the app are examples of why attackers use applications like that in different phases of an attack."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Golang](https://thehackernews.com/search/label/Golang)[Malware](https://thehackernews.com/search/label/Malware)[powershell](https://thehackernews.com/search/label/powershell)[Telegram](https://thehackernews.com/search/label/Telegram)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](https://thehackernews.com/2025/10/scanning-activity-on-palo-alto-networks.html)

[![Researchers Warn of ...
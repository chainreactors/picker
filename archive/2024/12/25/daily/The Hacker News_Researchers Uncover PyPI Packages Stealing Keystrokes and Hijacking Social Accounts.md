---
title: Researchers Uncover PyPI Packages Stealing Keystrokes and Hijacking Social Accounts
url: https://thehackernews.com/2024/12/researchers-uncover-pypi-packages.html
source: The Hacker News
date: 2024-12-25
fetch_date: 2025-10-06T19:40:54.036689
---

# Researchers Uncover PyPI Packages Stealing Keystrokes and Hijacking Social Accounts

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

# [Researchers Uncover PyPI Packages Stealing Keystrokes and Hijacking Social Accounts](https://thehackernews.com/2024/12/researchers-uncover-pypi-packages.html)

**Dec 24, 2024**Ravie LakshmananMalware / Data Exfiltration

[![PyPI Packages](data:image/png;base64... "PyPI Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2fpo1l85L1KFPzg1xsX7LOMv0yGyuPjr_CZGmz6JPr0T4AwIdbvqMHFIXz4fTfgat9o0FQ6K53jXkoWIesU3UgJ0fa753fWob-zGCIw69p3j32uH3m4pBXklan3VgjvK_9qC4x0H5jVPwEEPelXrWQA3ErKKKEb638OoiWbr9siessmHh3buKZQq6CM6D/s790-rw-e365/python.png)

Cybersecurity researchers have flagged two malicious packages that were uploaded to the Python Package Index (PyPI) repository and came fitted with capabilities to exfiltrate sensitive information from compromised hosts, according to [new findings](https://www.fortinet.com/blog/threat-research/analyzing-malicious-intent-in-python-code) from Fortinet FortiGuard Labs.

The packages, named [zebo](https://secure.software/pypi/packages/zebo) and [cometlogger](https://secure.software/pypi/packages/cometlogger), attracted 118 and 164 downloads each, prior to them being taken down. According to ClickPy statistics, a [majority](https://clickpy.clickhouse.com/dashboard/zebo) of these [downloads](https://clickpy.clickhouse.com/dashboard/cometlogger) came from the United States, China, Russia, and India.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Zebo is a "typical example of malware, with functions designed for surveillance, data exfiltration, and unauthorized control," security researcher Jenna Wang said, adding cometlogger "also shows signs of malicious behavior, including dynamic file manipulation, webhook injection, stealing information, and anti-[virtual machine] checks."

The first of the two packages, zebo, uses obfuscation techniques, such as hex-encoded strings, to conceal the URL of the command-and-control (C2) server it communicates with over HTTP requests.

It also packs in a slew of features to harvest data, including leveraging the pynput library to capture keystrokes and ImageGrab to periodically grab screenshots every hour and save them to a local folder, prior to uploading them to the free image hosting service ImgBB using an API key retrieved from the C2 server.

In addition to exfiltrating sensitive data, the malware sets up persistence on the machine by creating a batch script that launches the Python code and adds it to the Windows Startup folder so that it's automatically executed upon every reboot.

Cometlogger, on the other hand, is a lot of feature-packed, siphoning a wide range of information, including cookies, passwords, tokens, and account-related data from apps such as Discord, Steam, Instagram, X, TikTok, Reddit, Twitch, Spotify, and Roblox.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's also capable of harvesting system metadata, network and Wi-Fi information, a list of running processes, and clipboard content. Furthermore, it incorporates checks to avoid running in virtualized environments and terminates web browser-related processes to ensure unrestricted file access.

"By asynchronously executing tasks, the script maximizes efficiency, stealing large amounts of data in a short time," Wang said.

"While some features could be part of a legitimate tool, the lack of transparency and suspicious functionality make it unsafe to execute. Always scrutinize code before running it and avoid interacting with scripts from unverified sources."

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

[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[Fortinet](https://thehackernews.com/search/label/Fortinet)[Malware](https://thehackernews.com/search/label/Malware)[Obfuscation](https://thehackernews.com/search/label/Obfuscation)[PyPI](https://thehackernews.com/search/label/PyPI)[Python Package](https://thehackernews.com/search/label/Python%20Package)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[!...
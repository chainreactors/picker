---
title: Expired Domains Allowed Control Over 4,000 Backdoors on Compromised Systems
url: https://thehackernews.com/2025/01/expired-domains-allowed-control-over.html
source: The Hacker News
date: 2025-01-14
fetch_date: 2025-10-06T20:14:16.204419
---

# Expired Domains Allowed Control Over 4,000 Backdoors on Compromised Systems

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

# [Expired Domains Allowed Control Over 4,000 Backdoors on Compromised Systems](https://thehackernews.com/2025/01/expired-domains-allowed-control-over.html)

**Jan 13, 2025**Ravie LakshmananMalware / Domain Security

[![Expired Domains](data:image/png;base64... "Expired Domains")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqLUiUiInn2mO8M0WOIZ8jwlrCg2zFmKV5XBg6KfJkLa7R-Lai0s72hvaHzohEzjdVcybkEaNvZYcP85tR_2iU3rGwnccp-B-ldrCxrVh6TCNbbFVGltG2_jP0H6EZaE5M3Vx77h6duy5H49OraDYNihwLr7qk6QVWsIZSzF8HwU35fAL8g4iPTvh1ta-x/s790-rw-e365/domain.png)

No less than 4,000 unique web backdoors previously deployed by various threat actors have been hijacked by taking control of abandoned and expired infrastructure for as little as $20 per domain.

Cybersecurity company watchTowr Labs said it pulled off the operation by registering over 40 domain names that the backdoors had been designed to use for command-and-control (C2). In partnership with the Shadowserver Foundation, the domains implicated in the research have been sinkholed.

"We have been hijacking backdoors (that were reliant on now abandoned infrastructure and/or expired domains) that themselves existed inside backdoors, and have since been watching the results flood in," watchTowr Labs CEO Benjamin Harris and researcher Aliz Hammond [said](https://labs.watchtowr.com/more-governments-backdoors-in-your-backdoors/) in a technical write-up last week.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This hijacking allowed us to track compromised hosts as they 'reported in,' and theoretically gave us the power to commandeer and control these compromised hosts."

Among the compromised targets identified by means of the beaconing activity included government entities from Bangladesh, China, and Nigeria; and academic institutions across China, South Korea, and Thailand, among others.

The backdoors, which are nothing but web shells designed to offer persistent remote access to target networks for follow-on exploitation, vary in scope and functionality -

* Simple web shells that are capable of executing an attacker-provided command by means of a PHP code
* [c99shell](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:PHP/C99Shell.RR&ThreatID=2147761267)
* [r57shell](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:PHP/R57Shell.A)
* [China Chopper](https://thehackernews.com/2022/06/chinese-gallium-hackers-using-new.html), a web shell prominently shared by China-nexus advanced persistent threat (APT) groups

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCUBSZwgld9uwFkV6XtuW0UQoaIdoOfAusYDe5iPhF1nHzLqfITa0gvFXZdxrdK58ludXqSjKDYAXEA0ri8aPf4SJuT6OZbywcLskFjSYyeOgVHTNTwvEQsdSBfKXdcALta9OCVON2zZ1QfXEFvKqMx-mtYk8baeXgj5pybkTwFbUfWwU9ZdKczBmvUtJN/s790-rw-e365/c.png)

Both c99shell and r57shell are fully-featured web shells with features to execute arbitrary code or commands, perform file operations, deploy additional payloads, brute-force FTP servers, and remove themselves from compromised hosts.

WatchTowr Labs said it observed instances where some of the web shells were backdoored by the script maintainers to leak the locations where they were deployed, thereby inadvertently handing over the reins to other threat actors as well.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes a couple of months after the company [revealed](https://thehackernews.com/2024/09/thn-cybersecurity-recap-last-weeks-top.html) it spent a mere $20 to acquire a legacy WHOIS server domain ("whois.dotmobiregistry[.]net") associated with the .mobi top-level domain (TLD), identifying more than 135,000 unique systems that were still communicating with the server even after it had migrated to "whois.nic[.]mobi."

These comprised various private companies, like VirusTotal, as well as mail servers for countless government, military, and university entities. The .gov addresses belonged to Argentina, Bangladesh, Bhutan, Ethiopia, India, Indonesia, Israel, Pakistan, The Philippines, Ukraine, and the U.S.

"It is somewhat encouraging to see that attackers make the same mistakes as defenders," watchTowr Labs said. "It's easy to slip into the mindset that attackers never slip up, but we saw evidence to the contrary – boxes with open web shells, expired domains, and the use of software that has been backdoored."

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

[Backdoor](https://thehackernews.com/search/label/Backdoor)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Domain Security](https://thehackernews.com/search/label/Domain%20Security)[Malware](https://thehackernews.com/search/label/Malware)[Web Shell](https://thehackernews.com/search/label/Web%20Shell)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incid...
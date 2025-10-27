---
title: Hackers Found Using CrossC2 to Expand Cobalt Strike Beacon’s Reach to Linux and macOS
url: https://thehackernews.com/2025/08/researchers-warn-crossc2-expands-cobalt.html
source: The Hacker News
date: 2025-08-15
fetch_date: 2025-10-07T00:50:20.542269
---

# Hackers Found Using CrossC2 to Expand Cobalt Strike Beacon’s Reach to Linux and macOS

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

# [Hackers Found Using CrossC2 to Expand Cobalt Strike Beacon's Reach to Linux and macOS](https://thehackernews.com/2025/08/researchers-warn-crossc2-expands-cobalt.html)

**Aug 14, 2025**Ravie LakshmananThreat Intelligence / Linux

[![CrossC2 Expands Cobalt Strike](data:image/png;base64... "CrossC2 Expands Cobalt Strike")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHJUrGWkx7DZ_vwVDxSwsYdwTwiQAY1dHz5vTRTQ8GKyJm3-CmLP8-Gbep5JI5TxDjGUMwgQNBxnlaJw-HUG6fI0-MRKpJVnO2jcZcgx_mjGsqnTeGP0xFOgc41Htpv1VY8yBZ0ENh3lgIqbROROcQudBxHLznsSGAByoAds357VLwmdt9Iq4E70m4WxU7/s790-rw-e365/malware-cross.png)

Japan's CERT coordination center (JPCERT/CC) on Thursday revealed it observed incidents that involved the use of a command-and-control (C2) framework called [CrossC2](https://github.com/gloxec/CrossC2), which is designed to extend the functionality of Cobalt Strike to other platforms like Linux and Apple macOS for cross-platform system control.

The agency said the activity was detected between September and December 2024, targeting multiple countries, including Japan, based on an analysis of VirusTotal artifacts.

"The attacker employed CrossC2 as well as other tools such as PsExec, Plink, and Cobalt Strike in attempts to penetrate AD. Further investigation revealed that the attacker used custom malware as a loader for Cobalt Strike," JPCERT/CC researcher Yuma Masubuchi [said](https://blogs.jpcert.or.jp/en/2025/08/crossc2.html) in a report published today.

The bespoke Cobalt Strike Beacon loader has been codenamed ReadNimeLoader. CrossC2, an unofficial Beacon and builder, is capable of executing various Cobalt Strike commands after establishing communication with a remote server specified in the configuration.

In the attacks documented by JPCERT/CC, a scheduled task set up by the threat actor on the compromised machine is used to launch the legitimate java.exe binary, which is then abused to sideload ReadNimeLoader ("jli.dll").

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Written in the Nim programming language, the loader extracts the content of a text file and executes it directly in memory so as to avoid leaving traces on disk. This loaded content is an open-source shellcode loader dubbed [OdinLdr](https://github.com/emdnaia/OdinLdr), which ultimately decodes the embedded Cobalt Strike Beacon and runs it, also in memory.

ReadNimeLoader also incorporates various anti-debugging and anti-analysis techniques that are designed to prevent OdinLdr from being decoded unless the route is clear.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioXnCU7TeYdTaArZ7j9KGUOkfarJyiWWspViMDk59PmcYFtqecid9aOrmSYFlWN3bVOONvF5dNrerg9904mhT5AB7NV4QHNrq9sSJehmmSoAejWpW0Uhmafk3HdTa7eJl0sZYTEhmjps6N4Rj99pL11BXUVys08zyAQsi-S9zkOaLRBAIcmuU0Ks_S_tqk/s790-rw-e365/cobalt.png)

JPCERT/CC said the attack campaign shares some level of overlap with BlackSuit/Black Basta ransomware activity [reported](https://thehackernews.com/2025/06/former-black-basta-members-use.html) by Rapid7 back in June 2025, citing overlaps in the command-and-control (C2) domain used and similarly-named files.

Another notable aspect is the presence of several [ELF versions](https://x.com/anyrun_app/status/1884207667058463188) of [SystemBC](https://thehackernews.com/2024/01/systembc-malwares-c2-server-analysis.html), a backdoor that often acts as a precursor to the deployment of Cobalt Strike and ransomware.

"While there are numerous incidents involving Cobalt Strike, this article focused on the particular case in which CrossC2, a tool that extends Cobalt Strike Beacon functionality to multiple platforms, was used in attacks, compromising Linux servers within an internal network," Masubuchi said.

"Many Linux servers do not have EDR or similar systems installed, making them potential entry points for further compromise, and thus, more attention is required."

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

[Cobalt Strike](https://thehackernews.com/search/label/Cobalt%20Strike)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Incident response](https://thehackernews.com/search/label/Incident%20response)[Japan CERT](https://thehackernews.com/search/label/Japan%20CERT)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[ransomware](https://thehackernews.com/search/label/ransomware)[SystemBC](https://thehackernews.com/search/label/SystemBC)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise De...
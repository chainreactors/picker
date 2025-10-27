---
title: Kimsuky APT Deploying Linux Backdoor Gomir in South Korean Cyber Attacks
url: https://thehackernews.com/2024/05/kimsuky-apt-deploying-linux-backdoor.html
source: The Hacker News
date: 2024-05-18
fetch_date: 2025-10-06T16:52:54.895683
---

# Kimsuky APT Deploying Linux Backdoor Gomir in South Korean Cyber Attacks

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

# [Kimsuky APT Deploying Linux Backdoor Gomir in South Korean Cyber Attacks](https://thehackernews.com/2024/05/kimsuky-apt-deploying-linux-backdoor.html)

**May 17, 2024**Ravie LakshmananLinux / Malware

[![Linux Backdoor](data:image/png;base64... "Linux Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKkkd9TlpBH69SJ2A5la8Bres_d4l53vzANAK7W2RVh3HJoJjX9PuIhhtiYhO5YlDnu8RuFrT8bAyj_0DwcjPB4tSIcLglj7N2PGus3G1cYnF29ytBkUvgf_DuGCsD5wc7c9NZ-Y5WoSifZzg5ZcNs2nbhRgepHlfcURgaVUvEu_6OQwZktjWfr-did40B/s790-rw-e365/linux.png)

The [Kimsuky](https://thehackernews.com/2024/05/north-korean-hackers-exploit-facebook.html) (aka Springtail) advanced persistent threat (APT) group, which is linked to North Korea's Reconnaissance General Bureau (RGB), has been observed deploying a Linux version of its GoBear backdoor as part of a campaign targeting South Korean organizations.

The backdoor, codenamed **Gomir**, is "structurally almost identical to GoBear, with extensive sharing of code between malware variants," the Symantec Threat Hunter Team, part of Broadcom, [said](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/springtail-kimsuky-backdoor-espionage) in a new report. "Any functionality from GoBear that is operating system-dependent is either missing or reimplemented in Gomir."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

GoBear was [first documented](https://thehackernews.com/2024/02/kimsukys-new-golang-stealer-troll-and.html) by South Korean security firm S2W in early February 2024 in connection with a campaign that delivered a malware called Troll Stealer (aka TrollAgent), which overlaps with known Kimsuky malware families like AppleSeed and AlphaSeed.

A subsequent analysis by the AhnLab Security Intelligence Center (ASEC) revealed that the malware is distributed via trojanized security programs downloaded from an unspecified South Korean construction-related association's website.

This includes nProtect Online Security, NX\_PRNMAN, TrustPKI, UbiReport, and WIZVERA VeraPort, the last of which was previously subjected to a [software supply chain attack](https://thehackernews.com/2020/11/trojanized-security-software-hits-south.html) by the Lazarus Group in 2020.

Symantec said that it also observed the Troll Stealer malware being delivered via rogue installers for Wizvera VeraPort, although the exact distribution mechanism by which the installation packages get delivered is presently unknown.

"GoBear also contains similar function names to an older Springtail backdoor known as BetaSeed, which was written in C++, suggesting that both threats have a common origin," the company noted.

The malware, which supports capabilities to execute commands received from a remote server, is also said to be propagated through droppers that masquerade as a fake installer for an app for a Korean transport organization.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Its Linux counterpart, Gomir, supports as many as 17 commands, allowing its operators to perform file operations, start a reverse proxy, pause command-and-control (C2) communications for a specified time duration, run shell commands, and terminate its own process.

"This latest Springtail campaign provides further evidence that software installation packages and updates are now among the most favored infection vectors for North Korean espionage actors," Symantec said.

"The software targeted appears to have been carefully chosen to maximize the chances of infecting its intended South Korean-based targets."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hacking news](https://thehackernews.com/search/label/hacking%20news)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[reverse proxy](https://thehackernews.com/search/label/reverse%20proxy)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-mal...
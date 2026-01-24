---
title: Phishing Attack Uses Stolen Credentials to Install LogMeIn RMM for Persistent Access
url: https://thehackernews.com/2026/01/phishing-attack-uses-stolen-credentials.html
source: The Hacker News
date: 2026-01-23
fetch_date: 2026-01-24T03:32:39.688895
---

# Phishing Attack Uses Stolen Credentials to Install LogMeIn RMM for Persistent Access

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

# [Phishing Attack Uses Stolen Credentials to Install LogMeIn RMM for Persistent Access](https://thehackernews.com/2026/01/phishing-attack-uses-stolen-credentials.html)

**Ravie Lakshmanan**Jan 23, 2026Email Security / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicydHIzxQzKCM6IJLuGPOYTskBFZhVxh6XYXItKSN91mAqv0xzZfIRmI1XXeyGE8yJ-gORNbdNwXBdCSJ9uEV9CnSE814erkLz4HKjN-eYPERE-7CWfE-UER9iumjTABTzv6j05jubb0hND2LJs9SNJyIBBd7PFkkzv0wNvlDfZFtsYqrxZgR5a0VLaNAI/s1600-e365/logmein.jpg)

Cybersecurity researchers have disclosed details of a new dual-vector campaign that leverages stolen credentials to deploy legitimate Remote Monitoring and Management (RMM) software for persistent remote access to compromised hosts.

"Instead of deploying custom viruses, attackers are bypassing security perimeters by weaponizing the necessary IT tools that administrators trust," KnowBe4 Threat Labs researchers Jeewan Singh Jalal, Prabhakaran Ravichandhiran, and Anand Bodke [said](https://blog.knowbe4.com/the-skeleton-key-how-attackers-weaponize-trusted-rmm-tools-for-backdoor-access). "By stealing a 'skeleton key' to the system, they turn legitimate Remote Monitoring and Management (RMM) software into a persistent backdoor."

The attack unfolds in two distinct waves, where the threat actors leverage fake invitation notifications to steal victim credentials, and then leverage those pilfered credentials to deploy RMM tools to establish persistent access.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The bogus emails are disguised as an invitation from a legitimate platform called Greenvelope, and aim to trick recipients into clicking on a phishing URL that's designed to harvest their Microsoft Outlook, Yahoo!, AOL.com login information. Once this information is obtained, the attack moves to the next phase.

Specifically, this involves the threat actor registering with LogMeIn using the compromised email to generate RMM access tokens, which are then deployed in a follow-on attack through an executable named "GreenVelopeCard.exe" to establish persistent remote access to victim systems.

The binary, signed with a valid certificate, contains a JSON configuration that acts as a conduit to silently install LogMeIn Resolve (formerly GoTo Resolve) and connect to an attacker-controlled URL without the victim's knowledge.

With the RMM tool now deployed, the threat actors weaponize the remote access to alter its service settings so that it runs with unrestricted access on Windows. The attack also establishes hidden scheduled tasks to automatically launch the RMM program even if it's manually terminated by the user.

To counter the threat, it's advised that organizations monitor for unauthorized RMM installations and usage patterns.

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

[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[email security](https://thehackernews.com/search/label/email%20security)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Malware](https://thehackernews.com/search/label/Malware)[Phishing](https://thehackernews.com/search/label/Phishing)[Remote Access](https://thehackernews.com/search/label/Remote%20Access)[windows security](https://thehackernews.com/search/label/windows%20security)

Trending News

[![⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More")

⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](https://thehackernews.com/2026/01/weekly-recap-fortinet-exploits-redline.html)

[![n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](data:image/svg+xml;base64... "n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens")

n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](https://thehackernews.com/2026/01/n8n-supply-chain-attack-abuses.html)

[![New Advanced Linux VoidLink Malware Targets Cloud and container Environments](data:image/svg+xml;base64... "New Advanced Linux VoidLink Malware Targets Cloud and container Environments")

New Advanced Linux VoidLink Malware Targets Cloud and container Environments](https://thehackernews.com/2026/01/new-advanced-linux-voidlink-malware.html)

[![Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow](data:image/svg+xml;base64... "Critical Node.js Vulnerability Can Cause Server Crashes via async_hooks Stack Overflow")

Critical Node.js Vulnerability Can Cause Server Crashes via async\_hooks Stack Overflow](https://thehackernews.com/2026/01/critical-nodejs-vulnerability-can-cause.html)

[![Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution](data:image/svg+xml;base64... "Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution")

Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution](https://thehackernews.com/2026/01/fortinet-fixes-critical-fortisiem-flaw.html)

[![Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login](data:image/svg+xml;base64... "Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login")

Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login](https://thehackernews.com/2026/01/palo...
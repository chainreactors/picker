---
title: Harvester Deploys Linux GoGra Backdoor in South Asia Using Microsoft Graph API
url: https://thehackernews.com/2026/04/harvester-deploys-linux-gogra-backdoor.html
source: The Hacker News
date: 2026-04-22
fetch_date: 2026-04-23T04:45:14.463513
---

# Harvester Deploys Linux GoGra Backdoor in South Asia Using Microsoft Graph API

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

# [Harvester Deploys Linux GoGra Backdoor in South Asia Using Microsoft Graph API](https://thehackernews.com/2026/04/harvester-deploys-linux-gogra-backdoor.html)

**Ravie Lakshmanan**Apr 22, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiptXaD_Im0Bee0znCFTtBnOBEGGfeP-lS85crmRfAsd5-sMOsHstg9jATLVQOSJF2tiQQ6qkQ2ZWK98foU4WIQU_tHja8H882jF-_oiA5UGh-iG0-ByeaGfBbjDGid-FkfsNfKQUljfBsgejRsHBiBeX1DXRbjf1ohM1uhZiKdsjpBaH_0lYylOWSA9itt/s1700-e365/linux.jpg)

The threat actor known as **Harvester** has been attributed to a new Linux version of its **GoGra** backdoor deployed as part of attacks likely targeting entities in South Asia.

"The malware uses the legitimate Microsoft Graph API and Outlook mailboxes as a covert command-and-control (C2) channel, allowing it to bypass traditional perimeter network defenses," the Symantec and Carbon Black Threat Hunter Team [said](https://www.security.com/threat-intelligence/harvester-new-linux-backdoor-gogra) in a report shared with The Hacker News.

The cybersecurity company said it identified artifacts uploaded to the VirusTotal platform from India and Afghanistan, suggesting that the two countries may be the target of the espionage activity.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

Harvester was first [publicly documented](https://thehackernews.com/2021/10/lightbasin-hackers-breach-at-least-13.html) by Symantec in late 2021, linking it to an information-stealing campaign aimed at telecommunications, government, and information technology sectors in South Asia since June 2021, using a bespoke implant called Graphon that used the Microsoft Graph API for C2.

Subsequent activity flagged in August 2024 [connected](https://thehackernews.com/2024/08/new-go-based-backdoor-gogra-targets.html) the hacking group to an attack targeting an unnamed media organization in South Asia with a never-before-seen Go-based backdoor called GoGra. The latest findings suggest that the adversary is continuing to expand its toolset beyond Windows and infecting Linux machines with a new variant of the same backdoor.

The attacks employ social engineering to trick victims into opening ELF binaries disguised as PDF documents. The dropper then proceeds to display a lure document while stealthily running the backdoor.

Like its Windows counterpart, the Linux version of GoGra abuses Microsoft's cloud infrastructure to contact a specific Outlook mailbox folder named "Zomato Pizza" every two seconds using Open Data Protocol (OData) queries. The backdoor scans the inbox for incoming email messages with a subject line starting with the word "Input."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

Once an email matching the criteria is received, it decrypts the Base64-encoded message body and executes it as shell commands using "/bin/bash." The results of the execution are sent back to the operator in an email message with the subject line "Output." After the exfiltration step is complete, the implant wipes the original tasking message to cover up the tracks.

"Despite using different deployment architectures and operating systems, the underlying C2 logic remains unchanged," Symantec and Carbon Black said, adding the teams "also identified several matching, hard-coded spelling errors across both platforms, which points towards the same developer being behind both tools."

"The use of a new Linux backdoor shows that Harvester is continuing to expand its toolset and actively develop new tooling in order to go after a wider range of victims and machines."

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data exfiltration](https://thehackernews.com/search/label/data%20exfiltration), [linux](https://thehackernews.com/search/label/linux), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Outlook](https://thehackernews.com/search/label/Outlook), [social engineering](https://thehackernews.com/search/label/social%20engineering), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

[![Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](data:image/svg+xml;base64... "Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads")

Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html)

[![New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released](data:image/svg+xml;base64... "New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released")

New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released](https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html)

[![OpenAI Launches GPT-5.4-Cyber with Exp...
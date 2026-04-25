---
title: Tropic Trooper Uses Trojanized SumatraPDF and GitHub to Deploy AdaptixC2
url: https://thehackernews.com/2026/04/tropic-trooper-uses-trojanized.html
source: The Hacker News
date: 2026-04-24
fetch_date: 2026-04-25T04:38:42.782908
---

# Tropic Trooper Uses Trojanized SumatraPDF and GitHub to Deploy AdaptixC2

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

# [Tropic Trooper Uses Trojanized SumatraPDF and GitHub to Deploy AdaptixC2](https://thehackernews.com/2026/04/tropic-trooper-uses-trojanized.html)

**Ravie Lakshmanan**Apr 24, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheXZWhV-F6JpyIS7BshxCI158lslIFwx6XU9K15AoGDti8DVknLSrhAEc9HybQjSHfjfuKpGJ5by4EJamG4RV_7v8_SzlmhmSlxcfIBRaYX913E8f6-z0NQyMJ9g0VkszTUY726Csg6xWhwY16ygTe_JySvgj-JkaMyX4ZdM7yCuxRT_98lv22nywvy6r5/s1700-e365/cyberattack.jpg)

Chinese-speaking individuals are the target of a new campaign that uses a trojanized version of SumatraPDF reader to deploy the [AdaptixC2](https://unit42.paloaltonetworks.com/adaptixc2-post-exploitation-framework/) Beacon post-exploitation agent and ultimately facilitate the abuse of Microsoft Visual Studio Code (VS Code) tunnels for remote access.

Zscaler ThreatLabz, which discovered the campaign last month, has attributed it with high confidence to **[Tropic Trooper](https://thehackernews.com/2024/09/chinese-speaking-hacker-group-targets.html)** (aka APT23, Earth Centaur, KeyBoy, and Pirate Panda), a hacking group known for its targeting of various entities in Taiwan, Hong Kong, and the Philippines. It's assessed to be active since at least 2011.

"The threat actors created a custom AdaptixC2 Beacon listener, leveraging GitHub as their command-and-control (C2) platform," security researcher Yin Hong Chang [said](https://www.zscaler.com/blogs/security-research/tropic-trooper-pivots-adaptixc2-and-custom-beacon-listener) in an analysis.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d-1)

It's believed that Chinese-speaking individuals in Taiwan, and individuals in South Korea and Japan, are the targets of the campaign. The starting point of the attack is a ZIP archive containing military-themed document lures to launch the rogue version of SumatraPDF, which is then used to display a decoy PDF document, while simultaneously retrieving encrypted shellcode from a staging server to launch AdaptixC2 Beacon.

To accomplish this, the backdoored SumatraPDF executable launches a slightly modified version of a loader codenamed [TOSHIS](https://thehackernews.com/2025/08/abandoned-sogou-zhuyin-update-server.html), which is a variant of Xiangoop, a malware linked to Tropic Trooper, and has been used in the past to fetch next-stage payloads like Cobalt Strike Beacon or Merlin agent for the Mythic framework.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg21UOEYsyDAlO4-FqgPfxdudr_S4GOyGRQnr4hvFWOk4A4wBPfcIoIp055IkqauWRSdcNWJtLOu_7bE-ytxZoosbHAM_5x0cQJWHXABEN0v0nZev0LZJz2Qj0k3azb-XUnDx9BBbw4ofhCBbxynZtxRNahjnJKUyu8yIK-ft7nKIYR_fVgYK80oSRmr0QC/s1700-e365/zz.jpg)

The loader is responsible for activating the multi-stage attack, dropping both the lure document as a distraction mechanism and the AdaptixC2 Beacon agent in the background.The agent employs GitHub for C2, beaconing out to the attacker-controlled infrastructure to fetch tasks to be executed on the compromised host.

The attack moves to the next stage only when the victim is deemed valuable, at which point the threat actor deploys VS Code and sets up [VS Code tunnels](https://thehackernews.com/2024/12/hackers-weaponize-visual-studio-code.html) for remote access. On select machines, the threat actor has been found to install alternative, trojanized applications, likely in an attemptto better camouflage their actions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

What's more, the staging server involved in the intrusion ("158.247.193[.]100") has been observed hosting a Cobalt Strike Beacon and a custom backdoor called [EntryShell](https://hitcon.org/2024/CMT/slides/Pirates_of_The_Nang_Hai_Follow_the_Artifacts_of_Tropic_Trooper%2C_No_One_Knows.pdf), both of which have been put to use by Tropic Trooper in the past.

"Similar to the [TAOTH campaign](https://thehackernews.com/2025/08/abandoned-sogou-zhuyin-update-server.html), publicly available backdoors are used as payloads," Zscaler said. "While Cobalt Strike Beacon and Mythic Merlin were previously used, the threat actor has now shifted to AdaptixC2."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [GitHub](https://thehackernews.com/search/label/GitHub), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft Visual Studio Code](https://thehackernews.com/search/label/Microsoft%20Visual%20Studio%20Code), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

[![Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](data:image/svg+xml;base64... "Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads")

Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](https://thehackernews.com/2026/04/mirax-a...
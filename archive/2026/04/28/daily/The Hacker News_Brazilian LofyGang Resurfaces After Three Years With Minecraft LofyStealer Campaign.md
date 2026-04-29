---
title: Brazilian LofyGang Resurfaces After Three Years With Minecraft LofyStealer Campaign
url: https://thehackernews.com/2026/04/brazilian-lofygang-resurfaces-after.html
source: The Hacker News
date: 2026-04-28
fetch_date: 2026-04-29T05:13:05.164736
---

# Brazilian LofyGang Resurfaces After Three Years With Minecraft LofyStealer Campaign

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

# [Brazilian LofyGang Resurfaces After Three Years With Minecraft LofyStealer Campaign](https://thehackernews.com/2026/04/brazilian-lofygang-resurfaces-after.html)

**Ravie Lakshmanan**Apr 28, 2026Malware / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQf8Wzg1Ms0KVsO546uQuwlR3w_8qW1MQZExs5TgKCGHSNNS1UEnOITq-_y8HIrA_3n_gfq7Hm0IMb-XSRJSsGL1ncRPlPoyDX7cf_wFbEGAJCPkv6ZDBzjN1Nswe9-CMR3Tmn1F5KuVyWGdOkGEIbeI9R7zGKplJPofRFBx-Ru20JOGfAFEpiZOAlDBXh/s1700-e365/hackers.jpg)

A cybercrime group of Brazilian origin has resurfaced after more than three years to orchestrate a campaign that targets Minecraft players with a new stealer called **LofyStealer** (aka GrabBot).

"The malware disguises itself as a Minecraft hack called 'Slinky,'" Brazil-based cybersecurity company ZenoX [said](https://zenox.ai/en/lofystealer-malware-mirando-jogadores-de-minecraft/) in a technical report. "It uses the official game icon to induce voluntary execution, exploiting the trust of young users in the gaming scene."

The activity has been attributed with high confidence to a threat actor known as [LofyGang](https://thehackernews.com/2022/10/lofygang-distributed-200-malicious-npm.html), which was [observed](https://thehackernews.com/2022/08/10-credential-stealing-python-libraries.html#malicious-npm-packages-steal-discord-tokens-and-bank-card-data) leveraging typosquatted packages on the npm registry to push stealer malware in 2022, specifically with an intent to siphon credit card data and user accounts associated with Discord Nitro, gaming, and streaming services.

The group, believed to be active since late 2021, advertises their tools and services on platforms like GitHub and YouTube, while also contributing to an underground hacking community under the alias DyPolarLofy to leak thousands of Disney+ and  Minecraft accounts.

"Minecraft has been a LofyGang target since 2022," Acassio Silva, co-founder and head of threat intelligence at ZenoX, told The Hacker News. "They leaked thousands of Minecraft accounts under the DyPolarLofy alias on Cracked.io. The current campaign goes after Minecraft players directly through a fake 'Slinky' hack."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agentic-guide-d-3)

The attack begins with a Minecraft hack that, when launched, triggers the execution of a JavaScript loader that's ultimately responsible for the deployment of LofyStealer ("chromelevator.exe") on compromised hosts and execute it directly in memory with an aim to harvest a wide range of sensitive data spanning multiple web browsers, including Google Chrome, Chrome Beta, Microsoft Edge, Brave, Opera, Opera GX, Mozilla Firefox, and Avast Browser.

The captured data, which includes cookies, passwords, tokens, cards, and International Bank Account Numbers (IBANs), is exfiltrated to a command-and-control (C2) server located at 24.152.36[.]241.

"Historically, the group's primary vector was the JavaScript supply chain: NPM package typosquatting, starjacking (fraudulent references to legitimate GitHub repositories to inflate credibility), and payloads embedded in sub-dependencies to evade detection," ZenoX said.

"The focus was on Discord token theft, Discord client modification for credit card interception, and exfiltration via webhooks abusing legitimate services (Discord, Repl.it, Glitch, GitHub, and Heroku) as C2."

The latest development marks a departure from previously observed tradecraft and a shift towards a malware-as-a-service (MaaS) model with free and premium tiers, along with a bespoke builder called Slinky Cracked that's used as a delivery vehicle for the stealer malware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbAr1NKRR65f1kQCoig_Pv6wnWUX6226X-sXLNLhJf6IAtYg5lzVYkN9ghMzcI_lO9q0G8uGKVYNIVI1TWRk0B_6TNCAyzKuSDkM52lFRwg7TLA2fB6J4hX0mAIgEhJrbEZhk1Ifkl2tmTnUKPinoz_2eV934v7Vct_xc9cXlXLEn73tQZrcoqqqdGWmDk/s1700-e365/cc.jpg)

The disclosure comes as threat actors are increasingly abusing the trust associated with a platform like GitHub to [host bogus repositories](https://hexastrike.com/resources/blog/threat-intelligence/cloned-loaded-and-stolen-how-109-fake-github-repositories-delivered-smartloader-and-stealc/) that act as lures for [malware families](https://blog.intellibron.io/lua-jit-smartloader-analyzing-the-github-campaign-delivering-stealer/) like [SmartLoader, StealC Stealer](https://thehackernews.com/2026/02/smartloader-attack-uses-trojanized-oura.html), and Vidar Stealer. Unsuspecting users are directed to these repositories through techniques like SEO poisoning.

In some cases, attackers have been found to spread Vidar 2.0 through Reddit posts advertising fake Counter-Strike 2 game cheats, redirecting victims to a malicious website that delivers a ZIP archive containing the malware.

"This infostealer campaign highlights an ongoing security challenge where widely trusted platforms are abused to distribute malicious payloads," Acronis [said](https://www.acronis.com/en/tru/posts/vidar-stealer-20-distributed-via-fake-game-cheats-on-github-and-reddit/) in an analysis published last month. "By taking advantage of social trust and common download channels, threat actors are often able to bypass traditional security solutions."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The findings add to a growing list of campaigns that have leveraged GitHub in recent months -

* Targeting developers directly inside GitHub, using fake Microsoft Visual Studio Code (VS Code) security alerts posted through Discussions to trick users into installing malware by clicking on a link. "Because GitHub Discussions trigger email notifications for participants and watchers, these posts are also delivered directly to developers' inboxes," Socket [said](https://socket.dev/blog/widespread-github-campaign-uses-fake-vs-code-security-alerts-to-deliver-malware). "This extends the reach of the campaign beyond GitHub itself and makes the alerts appear more legitimate."
* Targeting Argentina's judicial systems [using spear‑phishing emails](https://www.pointwild.com/threat-intelligence/covert-rat-phishing-campaign/) to distribute a compressed ZIP archive that uses an intermediate batc...
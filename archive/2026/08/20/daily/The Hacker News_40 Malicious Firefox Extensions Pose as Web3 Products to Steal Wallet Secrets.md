---
title: 40 Malicious Firefox Extensions Pose as Web3 Products to Steal Wallet Secrets
url: https://thehackernews.com/2026/08/40-malicious-firefox-extensions-pose-as.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:10.222511
---

# 40 Malicious Firefox Extensions Pose as Web3 Products to Steal Wallet Secrets

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [40 Malicious Firefox Extensions Pose as Web3 Products to Steal Wallet Secrets](https://thehackernews.com/2026/08/40-malicious-firefox-extensions-pose-as.html)

**Ravie Lakshmanan**Aug 20, 2026Browser Security / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhA5ySurVDL2oPvG7l78G22fbZEDplybrP5KX79GCEuhHybqkIgDGWDY_iHNfSLhKMt4sxn51CF33lRNwyjQy-l4Zajbkl9qUFxsjHEIoVsFhWBcGoHavMzOnmbWAI-8VHreBmZhuoCPs_N5KAKLFccr-bFLhzvJq12bvhvp5upRSkZulRN4tUDUTkfTRqo/s1700-e365/firefox.png)

A set of 40 Mozilla Firefox extensions has been found to engage in cryptocurrency wallet theft by masquerading as OKX, Rabby Wallet, TronLink, and other Web3 products.

According to the Socket Threat Research team, the extensions are part of a broader set of 77 browser add-ons that share source code and infrastructure overlaps. The campaign, dubbed **Offside Wallet Theft Factory**, is believed to have been active since March 2026. The activity has not been attributed to any known threat actor or group.

"Extension-level analysis confirms 40 as malicious," security researcher Kirill Boychenko [said](https://socket.dev/blog/firefox-crypto-wallet-theft#Counterfeit-Wallets-Collect-Secrets-Directly). "Another 37 form a coordinated multi-sport score-shell operation. Their analyzed builds contain no confirmed credential- or wallet-stealing payloads, but their deceptive functionality, shared publishing artifacts, and version histories indicate malicious intent."

Among those 40 extensions, seven use threat actor-controlled Supabase projects as remote switches to server phishing or decoy content dynamically; 15 capture recovery phrases, private keys, and other wallet secrets, and exfiltrate them through Cloudflare Workers; 13 modified Rabby Wallet builds exfiltrate serialized keyrings before local encryption; and the remaining five capture credentials and clipboard data through hard-coded command and control (C2) infrastructure.

The wallet secrets are stolen using two methods: either remotely loading a fake wallet page or baking the functionality into the extension itself. In some cases, the add-ons first appeared on the official Firefox extensions marketplace as sports score or utility shells, before they were turned into wallet-stealing malware under the same Firefox ID.

The 37 extensions related to the sports score operation contain deceptive implementations spanning football, basketball, NBA, and hockey, and share a hard-coded credential for legitimate [API-Sports](https://api-sports.io/), a legitimate service that delivers real-time sports data, while marketing unrelated functions such as password generation, dark mode, VPN access, currency conversion, screenshot capture, and note-taking.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"Historical versions of nine confirmed malicious identities also used sports-score shells spanning football, basketball, NBA, and American football before later versions under the same Firefox IDs were repurposed into wallet-stealing extensions," Socket said.

"The other 31 confirmed malicious identities lack the sports API integration but contain confirmed malicious wallet- or credential-stealing functionality."

The names of some of the malicious extensions are below -

* Safe-Themes - Browser Extension (bliss-heaven@webbrol.com)
* Rabbit For Desktop (bright-save-feed@tabtools.org)
* ℞ab␢y Wa❘Iet (flex-clock-dash@extrakits.com)
* Rabb-Walӏet CryptoPortfolio (free-note-bolt@webtools.co)
* RABB-Walӏet Web3 & EVM (safe-stat-pure@proaddons.net)
* Rabbit/WALLET - EVM (sharp-stat-gear@netplugs.net)

"A single successful installation can expose a recovery phrase, private key, or wallet state worth far more than the cost of repeatedly publishing disposable extensions," Boychenko said.

"That economics helps explain the threat actors’ persistence in targeting the Firefox Add-ons ecosystem even when individual extensions are short-lived and ultimately removed. Rotating names and IDs, repurposing existing extension identities, cloning code, and separating malicious functionality across extensions, remote pages, and cloud infrastructure make repeated publication cheap and scalable."

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

[browser security](https://thehackernews.com/search/label/browser%20security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [cryptocurrency](https://thehackernews.com/search/label/cryptocurrency), [Cybercrime](https://thehackernews.com/search/label/Cybercrime), [data theft](https://thehackernews.com/search/label/data%20theft), [Firefox](https://thehackernews.com/search/label/Firefox), [Malware](https://thehackernews.com/search/label/Malware), [Phishing](https://thehackernews.com/search/label/Phishing), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](data:image/svg+xml;base64... "Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database")

Az...
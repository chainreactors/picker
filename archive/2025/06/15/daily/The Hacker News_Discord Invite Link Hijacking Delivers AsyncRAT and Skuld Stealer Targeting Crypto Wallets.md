---
title: Discord Invite Link Hijacking Delivers AsyncRAT and Skuld Stealer Targeting Crypto Wallets
url: https://thehackernews.com/2025/06/discord-invite-link-hijacking-delivers.html
source: The Hacker News
date: 2025-06-15
fetch_date: 2025-10-06T22:55:32.282250
---

# Discord Invite Link Hijacking Delivers AsyncRAT and Skuld Stealer Targeting Crypto Wallets

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

# [Discord Invite Link Hijacking Delivers AsyncRAT and Skuld Stealer Targeting Crypto Wallets](https://thehackernews.com/2025/06/discord-invite-link-hijacking-delivers.html)

**Jun 14, 2025**Ravie LakshmananMalware / Threat Intelligence

[![AsyncRAT and Skuld Stealer](data:image/png;base64... "AsyncRAT and Skuld Stealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi96L2cuGtbxiIZlMnLTlrdLrFfuLnu2GxEusOULWFIR9rstf31tuJIBGncdb-kwEAL0Fuxdbw-FhRJ4GH1SgQv61zi9yUwRZQRnJhrS7uXDHXLA9H_9mEenDlhI_HiRNXzyWszamB2vq3wV51P9GoRVdmq9cX_kUs4xfV167Tj4QbB0QwTgejeZ4INERqe/s790-rw-e365/Discord.jpg)

A new malware campaign is exploiting a weakness in Discord's invitation system to deliver an information stealer called [Skuld](https://thehackernews.com/2023/06/new-golang-based-skuld-malware-stealing.html) and the [AsyncRAT](https://thehackernews.com/2025/02/asyncrat-campaign-uses-python-payloads.html) remote access trojan.

"Attackers hijacked the links through vanity link registration, allowing them to silently redirect users from trusted sources to malicious servers," Check Point [said](https://research.checkpoint.com/2025/from-trust-to-threat-hijacked-discord-invites-used-for-multi-stage-malware-delivery/) in a technical report. "The attackers combined the ClickFix phishing technique, multi-stage loaders, and time-based evasions to stealthily deliver AsyncRAT, and a customized Skuld Stealer targeting crypto wallets."

The issue with Discord's invite mechanism is that it allows attackers to hijack expired or deleted invite links and secretly redirect unsuspecting users to malicious servers under their control. This also means that a Discord invite link that was once trusted and shared on forums or social media platforms could unwittingly lead users to malicious sites.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Details of the campaign come a little over a month after the cybersecurity company [revealed](https://thehackernews.com/2025/05/38000-freedrain-subdomains-found.html) another sophisticated phishing campaign that hijacked expired vanity invite links to entice users into joining a Discord server and instruct them to visit a phishing site to verify ownership, only to have their digital assets drained upon connecting their wallets.

While users can create temporary, permanent, or [custom](https://support.discord.com/hc/en-us/articles/115001542132-Custom-Invite-Link) (vanity) invite links on Discord, the platform prevents other legitimate servers from reclaiming a previously expired or deleted invite. However, Check Point found that creating custom invite links allows the reuse of expired invite codes and even deleted permanent invite codes in some cases.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxjLgvnmt8E9HWX3sgytwu5_z1h-YnINYUBqf_e0nFEADOZf-bTJ5D3OpKi3NQPBPwo8ER8CnLz5EREzLNXQA7dEQqThFMyIC1yKfVI-VGEvlvCqnvNdv2R3qFcUGFqmkyhEWKzRHVf3dFG-ilL1kp_6kxvRbson-cMI8zTjbibHiJxZjeft03sv48Pkmh/s790-rw-e365/cp-flow.jpg)

This ability to reuse Discord expired or deleted codes when creating custom vanity invite links opens the door to abuse, allowing attackers to claim it for their malicious server.

"This creates a serious risk: Users who follow previously trusted invite links (e.g., on websites, blogs, or forums) can unknowingly be redirected to fake Discord servers created by threat actors," Check Point said.

The Discord invite-link hijacking, in a nutshell, involves taking control of invite links originally shared by legitimate communities and then using them to redirect users to the malicious server. Users who fall prey to the scheme and join the server are asked to complete a verification step in order to gain full server access by authorizing a bot, which then leads them to a fake website with a prominent "Verify" button.

This is where the attackers take the attack to the next level by incorporating the infamous [ClickFix](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html) social engineering tactic to trick users into infecting their systems under the pretext of verification.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJleGypTpPeuABlMDyPu4FhAlpae98FQRLA9YouP6nQt3GnX7P58fPyroo8mx6tx8DfsM8trf0Mp-fWyUiMV_mzlqjncuk0lRcKq9AkULJE3K5_3sTk6gGycyX0PkvaAFJ_59TSu5FTSWeZsCYIxFCZderB9PPy2rR3nUZb7HxeDg0Tzbs_K08-AvI4cCB/s790-rw-e365/cp-main.jpg)

Specifically, clicking the "Verify" button surreptitiously executes JavaScript that copies a PowerShell command to the machine's clipboard, after which the users are urged to launch the Windows Run dialog, paste the already copied "verification string" (i.e., the PowerShell command), and press Enter to authenticate their accounts.

But in reality, performing these steps triggers the download of a PowerShell script hosted on Pastebin that subsequently retrieves and executes a first-stage downloader, which is ultimately used to drop AsyncRAT and Skuld Stealer from a remote server and execute them.

At the heart of this attack lies a meticulously engineered, multi-stage infection process designed for both precision and stealth, while also taking steps to subvert security protections through sandbox security checks.

AsyncRAT, which offers comprehensive remote control capabilities over infected systems, has been found to employ a technique called [dead drop resolver](https://thehackernews.com/2025/02/new-malware-campaign-uses-cracked.html) to access the actual command-and-control (C2) server by reading a Pastebin file.

The other payload is a Golang information stealer that's downloaded from Bitbucket. It's equipped to steal sensitive user data from Discord, various browsers, crypto wallets, and gaming platforms.

Skuld is also capable of harvesting crypto wallet seed phrases and passwords from the Exodus and Atomic crypto wallets. It accomplishes this using an approach called wallet injection that replaces legitimate application files w...
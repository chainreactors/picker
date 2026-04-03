---
title: Researchers Uncover Mining Operation Using ISO Lures to Spread RATs and Crypto Miners
url: https://thehackernews.com/2026/04/researchers-uncover-mining-operation.html
source: The Hacker News
date: 2026-04-02
fetch_date: 2026-04-03T04:29:26.822982
---

# Researchers Uncover Mining Operation Using ISO Lures to Spread RATs and Crypto Miners

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Researchers Uncover Mining Operation Using ISO Lures to Spread RATs and Crypto Miners](https://thehackernews.com/2026/04/researchers-uncover-mining-operation.html)

**Ravie Lakshmanan**Apr 02, 2026Cryptomining / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpKoZinOy6MS9s0nTi1TV12H46KUmgkxu0kGinPE7yyq7Vpo9lmmcz30e5ve0yCk2T0ETCedeV6aXs0iEjI1rOykcXwBPa2a11yb75bjgjad7WKkKgsUAv0lO1tuZ8vVnYZtuiUHKqwM6Z6bxGtheJIhuWW5W6lKjo0FaHZf7ewPO_SFuKAjPKMh_sqDB2/s1700-e365/monero.jpg)

A financially motivated operation codenamed **REF1695** has been observed leveraging fake installers to deploy remote access trojans (RATs) and cryptocurrency miners since November 2023.

"Beyond cryptomining, the threat actor monetizes infections through CPA (Cost Per Action) fraud, directing victims to content locker pages under the guise of software registration," Elastic Security Labs researchers Jia Yu Chan, Cyril François, and Remco Sprooten [said](https://www.elastic.co/security-labs/fake-installers-to-monero) in an analysis published this week.

Recent iterations of the campaign have also been found to deliver a previously undocumented .NET implant codenamed CNB Bot. These attacks leverage an ISO file as the infection vector to deliver a .NET Reactor-protected loader and a text file with explicit instructions to the user to bypass Microsoft Defender SmartScreen protections against running unrecognized applications by clicking on "More info" and "Run anyway."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

The loader is designed to invoke PowerShell, which is responsible for configuring broad Microsoft Defender Antivirus exclusions to fly under the radar and launch CNB Bot in the background. At the same time, the user is displayed an error message: "Unable to launch the application. Your system may not meet the required specifications. Please contact support."

CNB Bot functions as a loader with capabilities to download and execute additional payloads, update itself, and uninstall and perform cleanup actions to cover up the tracks. It communicates with a command-and-control (C2) server using HTTP POST requests.

Other campaigns mounted by the threat actor have leveraged similar ISO lures to deploy [PureRAT](https://thehackernews.com/2025/05/purerat-malware-spikes-4x-in-2025.html), [PureMiner](https://thehackernews.com/2025/09/researchers-expose-svg-and-purerat.html), and a bespoke .NET-based XMRig loader, the last of which reaches out to a hard-coded URL to extract the mining configuration and launch the miner payload.

As recently observed in the [FAUX#ELEVATE](https://thehackernews.com/2026/03/hackers-use-fake-resumes-to-steal.html) campaign, "WinRing0x64.sys," a legitimate, signed, and vulnerable Windows kernel driver, is abused to obtain kernel-level hardware access and modify CPU settings to boost hash rates, thereby enabling performance improvement. The [use of the driver](https://www.sophos.com/en-us/blog/mrbminer-cryptojacking-to-bypass-international-sanctions) has been [observed](https://www.morphisec.com/blog/proxyshellminer-campaign/) in many [cryptojacking campaigns](https://www.trellix.com/blogs/research/technical-deep-dive-the-monero-mining-campaign/) over the years. The functionality was [added to XMRig miners](https://github.com/xmrig/xmrig/blob/master/bin/WinRing0/WinRing0x64.sys) in December 2019.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

Elastic said it also identified another campaign that leads to the deployment of [SilentCryptoMiner](https://thehackernews.com/2025/03/silentcryptominer-infects-2000-russian.html). The miner, besides using direct system calls to evade detection, takes steps to disable Windows Sleep and Hibernate modes, set up persistence via a scheduled task, and uses the "Winring0.sys" driver to fine-tune the CPU for mining operations.

Another notable component of the attack is a watchdog process that ensures the malicious artifacts and persistence mechanisms are restored in the event they are deleted. The campaign is estimated to have accrued 27.88 XMR ($9,392) across four tracked wallets, indicating that the operation is yielding consistent financial returns to the attacker.

"Beyond the C2 infrastructure, the threat actor abuses GitHub as a payload delivery CDN, hosting staged binaries across two identified accounts," Elastic said. "This technique shifts the download-and-execute step away from operator-controlled infrastructure to a trusted platform, reducing detection friction."

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

[Cryptomining](https://thehackernews.com/search/label/Cryptomining), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [GitHub](https://thehackernews.com/search/label/GitHub), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft Defender](https://thehackernews.com/search/label/Microsoft%20Defender), [powershell](https://thehackernews.com/search/label/powershell), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)...
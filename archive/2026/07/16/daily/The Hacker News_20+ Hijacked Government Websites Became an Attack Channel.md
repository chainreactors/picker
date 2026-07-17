---
title: 20+ Hijacked Government Websites Became an Attack Channel
url: https://thehackernews.com/2026/07/20-hijacked-government-websites.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:24.246526
---

# 20+ Hijacked Government Websites Became an Attack Channel

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [20+ Hijacked Government Websites Became an Attack Channel](https://thehackernews.com/2026/07/20-hijacked-government-websites.html)

**The Hacker News**Jul 16, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs_Ix6AmdT0f-NuPj2BLNRcSaOhWHf5pPdDuwR0eykvHCnOmoHUhq5Z2axM2GJX9gX5A3FlesfKuynGTsj012HNIJZURuZ8S7uCfa7_cSXIZDWC1donHjiQbkNr3jNLSq8B2PGpUG24fddwOaG2POjEQuvlrVEnp3yPa1F3tV2fpYDVQHEsaIHbnShUuQ/s1700-e365/hacked.jpg)

More than 20 Brazilian government websites were hijacked and turned into malware delivery channels in an active **PhantomEnigma** campaign uncovered by [ANY.RUN](https://any.run/?utm_source=the+hacker+news&utm_medium=article&utm_campaign=hijacked+websites&utm_content=landing&utm_term=160726), a leading provider of interactive malware analysis and threat intelligence solutions.

The investigation revealed previously undocumented backdoor behavior, hidden infrastructure relationships, and multiple attack arms behind a campaign putting banks and public agencies at risk.

By connecting hundreds of seemingly unrelated sandbox sessions, ANY.RUN researchers exposed the operation’s broader scope and showed how trusted .gov.br links and authenticated emails helped the activity remain hidden.

*For the complete technical analysis, infrastructure details, indicators, and detection guidance, read the [full PhantomEnigma investigation report](https://any.run/cybersecurity-blog/phantomenigma-research/?utm_source=the+hacker+news&utm_medium=article&utm_campaign=hijacked+websites&utm_content=blog&utm_term=160726)*

## Trusted Government Infrastructure Became the Lure

The attack began with fake police-themed documents presented as official “Ofício Polícia Civil” or “Procuração Digital” notices. Some contained QR codes, while others directed recipients to links designed to look like legitimate government resources.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS6yDw8gAJEfaIhWbCPAicAqgEu0BMZ_dXO6KAhaAoPus4eg87j0-FjoqBr3n20oH9sce5VgJtGQe1M9sk0B7dA2tB_K3SlK7ac6_UaIxeqqkmtNcSywtCMYGVUSDE1xfxU8r8hpQdrWGc4vxwGRJjWZON7heiYE-wVS8nC6NTHskmSw-50Duag1wgbX0/s1700-e365/1.png) |
| Fake police-themed document analyzed inside ANY.RUN sandbox for full visibility into PhantomEnigma attack |

In several cases, the emails were sent through compromised mailboxes and passed SPF, DKIM, and DMARC checks. That gave the messages a stronger appearance of legitimacy than ordinary spoofed phishing emails.

Victims were then redirected through compromised .gov.br hosts or police-themed lookalike domains before reaching the malicious installer. The government systems were used as trusted delivery infrastructure, not necessarily as the final targets of the campaign.

### Observed Government Hosts

Among the compromised systems observed during the investigation were timon.ma.gov[.]br, loginam.sesp.es.gov[.]br (state public security), aplicacao.cbm.mt.gov[.]br (fire department), prodoc.ap.gov[.]br, and others.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCs8KTadxz4wegYdQURkJ09ChGrFmzV7p9auvDn_MfyxhGMexgFLJy6x3jYBbdL00JahpVc9OQ_1mfL9OAMUMYKmc_4aN_Yd6TdqaXip8GdD5otdre9iS8IuObqRAjHL-7nWIMCfuGTPCyTgFhyphenhyphenRrCsYsCC9VQPU6DiWxZ0ljthfU3O_oFeCcj4ThI8eg/s1700-e365/2.png) |
| TI Lookup query that involves compromised government hosts |

These legitimate municipal, public-security, and judicial portals were used at different stages of the delivery chain. Several also appeared across more than one PhantomEnigma attack arm, helping researchers connect activity that initially looked unrelated.

## PhantomEnigma’s Evolution: Two Paths to Harder Detection

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicxDrh4bHJFBURe-TomnpaBKByXGZDKIrU5Lu1h_nnL0LTRfohZdedMNLMo8fgF_kb3mqffPjKJDWTWQhx1EqME5HRE2ovjNxBbrFULqCp-_PuaLG2fSPmb42IP4DXQrUDge1ZjRGJgojbPkimlQxb2E5QikOX-Reny9pMBUanDz2ZBJhcnKB7ncWtM1w/s1700-e365/3.png) |
| Timeline of PhantomEnigma’s malisious activity |

The timeline shows one operation evolving along two main paths:

**Delivery:** PhantomEnigma moved from banking-focused activity in 2025 to abusing compromised .gov.br websites and email accounts in 2026. This gave the campaign a more trusted route to victims without confirming a new target group.

**Arsenal:** The malware evolved from a browser-extension banker into a modular Inno/Node.js backdoor capable of executing JavaScript and delivering additional payloads.

For security teams, this combination creates a serious visibility gap. Trusted infrastructure reduces suspicion, modular payloads can change after infection, and rotating C2 domains quickly make static blocklists outdated. Behavioral analysis and continuous threat hunting provide more reliable coverage as the campaign evolves.

## From Trusted Email to Full Compromise: The PhantomEnigma Attack Chain

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHwkvJsUjNfQrYdKLS0i-zDBL_xwpHHt0jSsyUBopBJG0YwlqGvq8RGr379QebkgEYGo2tYHUfotTRwXaDgJauUn9W-Vufevfhut3ARrce8rZNpEO1-NCHP3PsActy_RiBi4Mk5nuUR4PiDu6OBICrJgOZ6h61uTP0yHxWKXFrHj90W0tGyvNTGYH3DNc/s1700-e365/4.png) |
| The analysis process of PhantomEnigma inside interactive sandbox |

Once a victim engaged with the lure, the campaign moved through a multi-stage infection chain:

1. **Phishing email:** A fake police-themed or official-document lure reaches the victim.
2. **Trusted infrastructure:** The link redirects through a compromised government host or police-themed lookalike domain.
3. **Malicious installer:** An Inno Setup, MSI, or another installer starts the infection.
4. **Patched Electron application:** Legitimate software loads a malicious index.js backdoor.
5. **Backdoor activation:** The malware collects system data, establishes persistence, and connects to rotati...
---
title: Rust-based Realst Infostealer Targeting Apple macOS Users' Cryptocurrency Wallets
url: https://thehackernews.com/2023/07/rust-based-realst-infostealer-targeting.html
source: The Hacker News
date: 2023-07-27
fetch_date: 2025-10-04T11:57:03.291237
---

# Rust-based Realst Infostealer Targeting Apple macOS Users' Cryptocurrency Wallets

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

# [Rust-based Realst Infostealer Targeting Apple macOS Users' Cryptocurrency Wallets](https://thehackernews.com/2023/07/rust-based-realst-infostealer-targeting.html)

**Jul 26, 2023**Ravie LakshmananCryptocurrency / Endpoint Security

[![Infostealer](data:image/png;base64... "Infostealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRUIM0cr9J2r5k-upwug5_sdosxlOfIJzzT8i4QHH1spE7OnBGnnkeh7ErUxD-mpeo3WBSijk4vp4EoOkmQQ_3fC6qmXXZV85a9HPw974MwfE8K3fUFKPAhklouIwjK5oQ2h6GU3dgyNMfLwE_3OPokNItWtyx1JSqlXUIgplC1zq9jOnDgYD3dnQGeLX0/s790-rw-e365/macos-malware.jpg)

A new malware family called **Realst** has become the latest to target Apple macOS systems, with a third of the samples already designed to infect macOS 14 Sonoma, the upcoming major release of the operating system.

Written in the Rust programming language, the malware is distributed in the form of bogus blockchain games and is capable of "emptying crypto wallets and stealing stored password and browser data" from both Windows and macOS machines. Realst was first discovered in the wild by security researcher [iamdeadlyz](https://iamdeadlyz.gitbook.io/malware-research/july-2023/fake-blockchain-games-deliver-redline-stealer-and-realst-stealer-a-new-macos-infostealer-malware).

"Realst Infostealer is distributed via malicious websites advertising fake blockchain games with names such as Brawl Earth, WildWorld, Dawnland, Destruction, Evolion, Pearl, Olymp of Reptiles, and SaintLegend," SentinelOne security researcher Phil Stokes [said](https://www.sentinelone.com/blog/apple-crimeware-massive-rust-infostealer-campaign-aiming-for-macos-sonoma-ahead-of-public-release/) in a report. "Each version of the fake blockchain game is hosted on its own website complete with associated Twitter and Discord accounts."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity firm, which identified 16 variants across 59 samples, said the activity likely has links to another information stealer campaign called [Pureland](https://www.sentinelone.com/blog/session-cookies-keychains-ssh-keys-and-more-7-kinds-of-data-malware-steals-from-macos-users/), which came to light earlier this March. Windows machines, on the other hand, are infected with RedLine Stealer.

"Despite the cross-platform capabilities of Rust, we haven't observed Realst variants on other platforms to date," Stokes told The Hacker News via an email statement.

"The Realst malware is clearly developed by devs with a good knowledge of the macOS environment and isn't just a simple port of something written on another platform. It's likely that the development team behind RedLine Stealer is entirely different from that behind Realst as there are few overlaps between developing for Windows and developing for macOS."

The attack chains begin with threat actors approaching potential victims through direct messages on social media, convincing them to test a game as part of a paid collaboration, only to drain their cryptocurrency wallets and steal sensitive information upon execution.

The web browsers targeted for harvesting include Brave, Google Chrome, Mozilla Firefox, Opera, and Vivaldi. Apple Safari is a notable exception. The malware is also capable of gathering information from Telegram and capturing screenshots.

"Most variants attempt to grab the user's password via osascript and AppleScript spoofing and perform rudimentary checking that the host device is not a virtual machine via sysctl -n hw.model," Stokes explained.

"The number of Realst samples and their variation shows that the threat actor has invested serious effort in order to target macOS users for data and crypto wallet theft."

News of the Realst stealer follows the discovery of [SophosEncrypt](https://news.sophos.com/en-us/2023/07/18/sophos-discovers-ransomware-abusing-sophos-name/), which has been found impersonating cybersecurity firm Sophos and described as a "general-purpose remote access trojan (RAT) with the capacity to encrypt files and generate these ransom notes."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The developments come as data captured via commercial information stealers are being packaged and sold for profit on dark web marketplaces and Telegram channels, with over 200,000 OpenAI credentials [leaked via stealer logs](https://thehackernews.com/2023/06/over-100000-stolen-chatgpt-account.html) in 2022 and 2023, according to multiple reports from [Bitdefender](https://www.bitdefender.com/blog/hotforsecurity/dark-net-sounds-mysterious-lets-see-whats-really-available-for-sale/) and [Flare](https://flare.io/learn/resources/stealer-logs-and-corporate-access).

Stolen enterprise credentials, in particular, can act as a channel for initial access brokers to breach organizations, which can then be auctioned off to other actors looking to exploit the foothold for follow-on activities such as ransomware deployment.

According to IBM's [Cost of a Data Breach Report 2023](https://www.ibm.com/reports/data-breach), which examined data breaches experienced by 553 organizations across 16 countries between March 2022 and March 2023, the global average cost of a data breach in 2023 stands at $4.45 million, a 15.3% increase from $3.86 million in 2020.

The study also found that "data breaches led to an increase in the pricing of their business offerings, passing on costs to consumers," a trend observed in 2022 as well.

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
[...
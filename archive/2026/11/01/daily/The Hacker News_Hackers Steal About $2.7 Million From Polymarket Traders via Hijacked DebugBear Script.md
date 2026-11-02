---
title: Hackers Steal About $2.7 Million From Polymarket Traders via Hijacked DebugBear Script
url: https://thehackernews.com/2026/11/hackers-steal-about-27-million-from.html
source: The Hacker News
date: 2026-11-01
fetch_date: 2026-11-02T08:33:34.629910
---

# Hackers Steal About $2.7 Million From Polymarket Traders via Hijacked DebugBear Script

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Hackers Steal About $2.7 Million From Polymarket Traders via Hijacked DebugBear Script](https://thehackernews.com/2026/11/hackers-steal-about-27-million-from.html)

**Swati Khandelwal**Nov 01, 2026Cryptocurrency / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe0B28qLAtUMfqN29_phxZJVJORICkj_98MZFwDiXAxFTABw8G9qbsVyD98pg7T_Rvgv83NXyR5tNGYH4dRwlxs3QFTUZxDPHQs2BgFsnmGcOuVW1HkFVCfiCR3Y05kPQrfFx4S7A8DiFXXAAgdc5SiEKx0-0xrW5rNlNSyN3jZJcyXasdpCr5AG7KM3s/s1700-nu-rw-lo-l85-e365/Polymarket.jpg)

Malicious code on the website of prediction market Polymarket sold some signed-in traders' positions and moved their funds to the hackers on October 29. The code had replaced a page-speed script that the site loaded from an outside company.

[Polymarket says](https://x.com/PolymarketTrade/status/2116177566553764137) it is refunding about $2.7 million to 726 affected wallets. [Blockchain records](https://polygonscan.com/address/0x3F99139F1C5854bb628c2e576Aaf638e99dFfc18) show crypto worth about $2.64 million reached the hackers' wallet in under an hour.

The replaced script came from DebugBear, whose real user monitoring (RUM) tool measures how fast web pages load for real visitors.

Researchers at [Hudson Rock](https://www.infostealers.com/article/polymarket-breach-alert-wallet-draining-code-found-in-a-third-party-script/) downloaded the malicious file on October 29 from the address Polymarket's site used to load the DebugBear script. They also found a change in Polymarket's site code that removed the DebugBear script.

DebugBear's DNS records were compromised through its domain registrar, the company said on X. Its early findings indicate the attack targeted one customer's website. It has seen no sign of a break-in to its own systems, though it is still looking.

[Researchers at Ohey](https://ohey.ca/research/polymarket-debugbear-wallet-drainer/) found a different server answering for DebugBear's web addresses at 18:13 UTC, when the malicious file was still online. Earlier that day, the normal script had been served from Google Cloud Storage. Each DebugBear customer loads its own copy of the script, and the file that was swapped was Polymarket's.

### How the Script Took the Money

The code reuses the access a signed-in trader already has in an open Polymarket page, Hudson Rock found after reviewing the file without running it. It reads account details that Polymarket keeps in the browser, including a set of trading API keys.

Those API keys alone cannot place an order on Polymarket, because orders also need a wallet signature. Hudson Rock found no part of the code that sends the keys, a password, a seed phrase, or a private key to the server it reports to.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Instead, the code searches the page for the part of Polymarket's site that places orders, and for the signer that approves the account's transactions.

It then takes one of two paths. For accounts that sign in with their own crypto wallet, it moves the trader's positions straight to the hackers' wallet. For accounts that sign in via email, it sells positions at ever-worse prices and then moves the money out.

In both paths, the code asks the account's own signer to sign its requests and hands them to Polymarket's relayer, which submits them. Hudson Rock said a signing request alone does not prove a trader signed without seeing a prompt. The wallet provider may still ask the trader, refuse, or apply its own rules for the session.

The wallet written into the code received its first funds at 17:10 UTC and its last at 18:02 UTC, according to Ohey's blockchain trace. In that time, it collected 28.6 million POL tokens and positions from 33 wallets.

At 18:19 UTC, those 28.6 million POL were worth about $2.64 million at DefiLlama's price of $0.0922, [DefiPrime](https://defiprime.com/polymarket-debugbear-frontend-drain) calculated. The figure covers only the POL, not the positions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhz4J4PPBzNIoHOiPwAsiPV_If7AV3IC9tgAJRXK8AvNX-EYL9yCqpLmWOfMoe1MEnBazwLzN9widQtJZ74v6zYx0iWdQdfeRoR48ahRMuz-FkeBxNTimjeIu2LmXWC2zfZuNnADpiW8gMlAyZAgrf-TWBUE60QTDx6UnHpvtcyhs0G2_KW0aq59QYev0/s1700-nu-rw-lo-l85-e365/funds.png)

The wallet sent all 28.6 million POL on to three other addresses between 18:28 and 18:38 UTC, its transaction history shows.

### Polymarket's Response and Refunds

Polymarket posted its first status update about unauthorized activity in user wallets at 17:38 UTC. At 18:05 UTC, it [said its exchange was in cancel-only mode](https://status.polymarket.com/history), with relayer actions paused.

The company said it removed the script "within the hour." It also cleared every cache, reset all active login sessions and paused trading until the site was clean. It has referred the case to law enforcement.

By October 30, 689 of the 726 affected wallets had been refunded in full, and the remaining 37 were being paid as they were checked. Polymarket is also paying $1.19 million to about 5,500 wallets that lost money during the trading pause or had positions taken. In all, it is returning $3.9 million to traders.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Traders do not need to file a claim. Polymarket's [status page](https://status.polymarket.com/cmvvek1i90eme14ruga1z6tuj) links a form for anyone who thinks their amount is wrong or that they should have received a payment.

### What Sites and Traders Can Do

DebugBear has told customers of its RUM product to remove its embed code from their websites. The address that served the malicious file, cdn.debugbear[.]com, had no DNS record when The Hacker News checked on November 1.

Polymarket said it is putting third-party scripts back in place with extra checks, such as a stronger Content Security Policy (CSP), pinned versions, and sandboxing...
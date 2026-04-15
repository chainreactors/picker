---
title: 108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users
url: https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html
source: The Hacker News
date: 2026-04-14
fetch_date: 2026-04-15T04:44:12.660413
---

# 108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users

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

# [108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

**Ravie Lakshmanan**Apr 14, 2026Data Theft / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEOmjr311c0yBDI593joFXQLaRdpm6DY67lbFv83YcYlRHaJkpocwXjDZDsV9F9DM-SavZwCOZ-fg10ncUJyW3ODlfBjqG6aK_ytdBfvXFGLswxeJ69oiZXfhGKdCgVO0Angg_qlYB6oAZYo-JQRKn4toBGWcS7OTDwPV0rkus7eNw-9BllIGJa2nkeKXn/s1700-e365/chrome-telegram.jpg)

Cybersecurity researchers have discovered a new campaign in which a cluster of 108 Google Chrome extensions has been found to communicate with the same command-and-control (C2) infrastructure with the goal of collecting user data and enabling browser-level abuse by injecting ads and arbitrary JavaScript code into every web page visited.

According to Socket, the extensions (complete list [here](https://socket.dev/blog/108-chrome-ext-linked-to-data-exfil-session-theft-shared-c2#:~:text=Chrome%20Extension%20IDs)) are published under five distinct publisher identities – Yana Project, GameGen, SideGames, Rodeo Games, and InterAlt – and have collectively amassed about 20,000 installs in the Chrome Web Store.

"All 108 route stolen credentials, user identities, and browsing data to servers controlled by the same operator," security researcher Kush Pandya [said](https://socket.dev/blog/108-chrome-ext-linked-to-data-exfil-session-theft-shared-c2) in an analysis.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Of these, 54 add-ons steal Google account identity via OAuth2, 45 extensions contain a universal backdoor that opens arbitrary URLs as soon as the browser is started, and the remaining ones engage in a variety of malicious behaviors -

* Exfiltrate Telegram Web sessions every 15 seconds
* Strip YouTube and TikTok security headers (i.e., Content Security Policy, X-Frame-Options, and CORS) and inject gambling overlays and ads
* Inject content scripts into every page the user visits
* Proxy all translation requests through the threat actor's server

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCID6WdCf6NahLEXNxG3NBdHR_nMToGiNP1RUeIAFXerxXS2XzGKaoloqKKTd99YEZPnsRSoyE3wzEs3NTO_Q-cfGclNOO76hxbLwVvbeQTP2MD0Gf1TFEKEfKecz2VOuYOSz5bBIbyZ11d_Cql_a6VY90d9lQVxwnDjE4P4JGZu-snpVRd4KJw9Job0bS/s1700-e365/tele.jpg)

In an attempt to lend a veneer of legitimacy, the identified extensions masquerade as Telegram sidebar clients, slot machine and Keno games, YouTube and TikTok enhancers, text translation tools, and page utilities. The advertised functionality is diverse, aiming to cast a wide net, while sharing the same backend.

Unbeknownst to the users, however, malicious code running in the background captures session information, injects arbitrary scripts, and opens URLs of the attacker's choosing.

Some of the identified extensions are listed below -

* Telegram Multi-account (ID: obifanppcpchlehkjipahhphbcbjekfa), which extracts the user\_auth token used by Telegram Web and exfiltrates the data to a remote server. It can also overwrite localStorage with threat actor-supplied session data and force-load the messaging application, effectively replacing the victim's active Telegram session with the threat actor's chosen session.
* Web Client for Telegram - Teleside (ID: mdcfennpfgkngnibjbpnpaafcjnhcjno), which strips Telegram's security headers and injects scripts to steal Telegram sessions.
* Formula Rush Racing Game (ID: akebbllmckjphjiojeioooidhnddnplj), which steals the user's Google account identity the first time the victim clicks the sign-in button. This includes details like email, full name, profile picture URL, and Google account identifier.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"Five extensions use Chrome's declarativeNetRequest API to strip security headers from target sites before the page loads," Socket said. "All 108 malicious extensions share the same backend, hosted at 144.126.135[.]238."

It's currently not known who is behind the policy-violating extensions. However, an analysis of source code has uncovered Russian language comments across several add-ons.

Users who have installed any of the extensions are advised to remove them with immediate effect and log out of all Telegram Web sessions from the Telegram mobile app.

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

[browser security](https://thehackernews.com/search/label/browser%20security), [Command and Control](https://thehackernews.com/search/label/Command%20and%20Control), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data theft](https://thehackernews.com/search/label/data%20theft), [Google Chrome](https://thehackernews.com/search/label/Google%20Chrome), [OAuth2](https://thehackernews.com/search/label/OAuth2), [Telegram](https://thehackernews.com/search/label/Telegram)

Trending News

[![Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](data:image/svg+xml;base64... "Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass")

Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](https://thehackernews.com/2026/04/microsoft-warns-of-whatsapp-delivered.html)

[![New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](data:image/svg+xml;bas...
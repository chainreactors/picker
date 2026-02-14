---
title: Malicious Chrome Extensions Caught Stealing Business Data, Emails, and Browsing History
url: https://thehackernews.com/2026/02/malicious-chrome-extensions-caught.html
source: The Hacker News
date: 2026-02-13
fetch_date: 2026-02-14T04:08:49.018938
---

# Malicious Chrome Extensions Caught Stealing Business Data, Emails, and Browsing History

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Malicious Chrome Extensions Caught Stealing Business Data, Emails, and Browsing History](https://thehackernews.com/2026/02/malicious-chrome-extensions-caught.html)

**Ravie Lakshmanan**Feb 13, 2026Browser Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuDcg8kBvyrdu22dNN8lKs3vJ_Nhk_nEuuZtq0Q-EcpvUKlRbXSHVssro3qio1_12lWV-dcFQ_O94jO4KAzh_mbdS0MKJ7REEcNSrPr5hon0iUNDcP91cFAqcNUl3EwPIVqhgOTss5ntc4x1BpfXldEBmCm1BzRNsPQMxqMsqTtNc6jZm4hN0vS3T9K3yj/s1700-e365/chrome-hacks.jpg)

Cybersecurity researchers have discovered a malicious Google Chrome extension that's designed to steal data associated with Meta Business Suite and Facebook Business Manager.

The extension, named CL Suite by @CLMasters (ID: jkphinfhmfkckkcnifhjiplhfoiefffl), is marketed as a way to scrape Meta Business Suite data, remove verification pop-ups, and generate two-factor authentication (2FA) codes. The extension has 33 users as of writing. It was first uploaded to the Chrome Web Store on March 1, 2025.

However, the browser add-on also exfiltrates TOTP codes for Facebook and Meta Business accounts, Business Manager contact lists, and analytics data to infrastructure controlled by the threat actor, Socket said.

"The extension requests broad access to meta.com and facebook.com and claims in its privacy policy that 2FA secrets and Business Manager data remain local," security researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-chrome-extension-steals-meta-business-manager-exports-and-totp-2fa-seeds).

"In practice, the code transmits TOTP seeds and current one-time security codes, Meta Business 'People' CSV exports, and Business Manager analytics data to a backend at getauth[.]pro, with an option to forward the same payloads to a Telegram channel controlled by the threat actor."

By targeting users of Meta Business Suite and Facebook Business Manager, the threat actor behind the operation has leveraged the extension to conduct data collection and exfiltration without users' knowledge or consent.

While the extension does not have capabilities to steal password-related information, the attacker could obtain such information beforehand from other sources, such as infostealer logs or credential dumps, and then use the stolen codes to gain unauthorized access to victims' accounts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The full scope of the malicious add-on's capabilities is listed below -

* Steal TOTP seed (a unique, alphanumeric code that's used to generate time-based one-time passwords) and 2FA code
* Target Business Manager "People" view by navigating to facebook[.]com and meta[.]com and build a CSV file with names, email addresses, roles and permissions, and their status and access details.
* Enumerate Business Manager-level entities and their linked assets and build a CSV file of Business Manager IDs and names, attached ad accounts, connected pages and assets, and billing and payment configuration details.

Socket warned that despite the low number of installs, the extension gives the threat actor enough information to identify high-value targets and mount follow-on attacks.

"CL Suite by @CLMasters shows how a narrow browser extension can repackage data scraping as a 'tool' for Meta Business Suite and Facebook Business Manager," Boychenko said.

"Its people extraction, Business Manager analytics, popup suppression, and in-browser 2FA generation are not neutral productivity features, they are purpose-built scrapers for high-value Meta surfaces that collect contact lists, access metadata, and 2FA material straight from authenticated pages."

## Chrome Extensions Hijack VKontakte Accounts

The disclosure comes as Koi Security [found](https://www.koi.ai/blog/vk-styles-500k-users-infected-by-chrome-extensions-that-hijack-vkontakte-accounts) that about 500,000 VKontakte users have had their accounts silently hijacked through Chrome extensions masquerading as VK customization tools. The large-scale campaign has been codenamed **VK Styles**.

The malware embedded in the extensions is designed to engage in active account manipulation by automatically subscribing users to the attacker's VK groups, resetting account settings every 30 days to override user preferences, manipulating Cross-Site Request Forgery (CSRF) tokens to bypass VK's security protections, and maintaining persistent control.

The activity has been traced to a threat actor operating under the GitHub username 2vk, who has relied on VK's own social network to distribute malicious payloads and build a follower base through forced subscriptions. The names of the extensions are listed below -

* VK Styles - Themes for vk.com (ID: ceibjdigmfbbgcpkkdpmjokkokklodmc)
* VK Music - audio saver (ID: mflibpdjoodmoppignjhciadahapkoch)
* Music Downloader - VKsaver (ID: lgakkahjfibfgmacigibnhcgepajgfdb)
* vksaver - music saver vk (ID: bndkfmmbidllaiccmpnbdonijmicaafn)
* VKfeed - Download Music and Video from VK (ID: pcdgkgbadeggbnodegejccjffnoakcoh)

One of the defining traits of the campaign is the use of a VK profile's ("vk[.]com/m0nda") HTML metadata tags as a dead drop resolver to conceal the next-stage payload URLs and, therefore, evade detection. The next-stage payload is hosted in a public repository named "-" that's associated with 2vk. Present in the payload is obfuscated JavaScript that's injected into every VK page the victim visits.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPzipGiz_wnh86iilk2y_D2pYOpO0hyv9VzW2QlRQxKN2vvbRueOl0hygV6T9LvPgiFE3RtW_tsnr_zCzd4o71RGYz8fHHjyF2RjwyWjodAAoXYxU03T4b_JvEpSYksgsSnff0tnHcQJp-z8U4-_Swdv57K7nqk0ajFeGbKIxPvnsmB9ck5fgHwe7BwhMg/s1700-e365/vk.png)

The repository is still accessible as of writing, with the file, simply named "C," receiving a total of 17 commits between June 2025 and January 2026, as the operator refined an...
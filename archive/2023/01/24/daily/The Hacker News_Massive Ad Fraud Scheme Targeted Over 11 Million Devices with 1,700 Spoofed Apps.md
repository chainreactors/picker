---
title: Massive Ad Fraud Scheme Targeted Over 11 Million Devices with 1,700 Spoofed Apps
url: https://thehackernews.com/2023/01/massive-ad-fraud-scheme-targeted-over.html
source: The Hacker News
date: 2023-01-24
fetch_date: 2025-10-04T04:40:55.536622
---

# Massive Ad Fraud Scheme Targeted Over 11 Million Devices with 1,700 Spoofed Apps

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

# [Massive Ad Fraud Scheme Targeted Over 11 Million Devices with 1,700 Spoofed Apps](https://thehackernews.com/2023/01/massive-ad-fraud-scheme-targeted-over.html)

**Jan 23, 2023**Ravie LakshmananMobile Security / Malvertising

[![Massive Ad Fraud Scheme](data:image/png;base64... "Massive Ad Fraud Scheme")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-aXXZ4ZhMnxWjWAK1ON1hdUiGzwXdIYm3-1DJnXHjgQxpyqWz_0e60cA3kF0x5otQzKkrPAKeXa_92r6BUEH4Cgs5mV52f3p_mLaa0gBlfwT0Mx9qne5QObc8MiY_0Bl0-HcDgqzEV_DgFroeUqI_ArNwTETkhugXomFggxKcC-yH6U0zCEVi92ev/s790-rw-e365/ads.png)

Researchers have shut down an "expansive" ad fraud scheme that spoofed more than 1,700 applications from 120 publishers and impacted roughly 11 million devices.

"VASTFLUX was a malvertising attack that injected malicious JavaScript code into digital ad creatives, allowing the fraudsters to stack numerous invisible video ad players behind one another and register ad views," fraud prevention firm HUMAN [said](https://www.humansecurity.com/learn/blog/traffic-signals-the-vastflux-takedown).

The operation gets its name from the use of a DNS evasion technique called [Fast Flux](https://en.wikipedia.org/wiki/Fast_flux) and [VAST](https://www.iab.com/guidelines/vast/), a Digital Video Ad Serving Template that's employed to serve ads to video players.

The sophisticated operation particularly exploited the restricted in-app environments that run ads on iOS to place bids for displaying ad banners. Should the auction be won, the hijacked ad slot is leveraged to inject rogue JavaScript that establishes contact with a remote server to retrieve the list of apps to be targeted.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This includes the [bundle IDs](https://support.apple.com/en-in/guide/deployment/depece748c41/web) that belong to legitimate apps so as to conduct what's called as an [app spoofing attack](https://www.humansecurity.com/learn/blog/show-me-the-app-spoofing), in which a fraudulent app passes off as a highly-regarded app in an attempt to trick advertisers into bidding for the ad space.

[![Ad Fraud Scheme](data:image/png;base64... "Ad Fraud Scheme")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3vBSHguCOrts-f7Ir4rX7gWOHaLYkNxeeB9hpgjgaSV2YVcXJwblAOrzCXtu8Y_L1L_zSw9_LLbqyxhHIm9WdAF7Jae6ILMB-LiiqzNYWSB7pQwrXQ4NHMd6C3OuJgoQfjtSxkKcaCTslN_5EhZppdm649XKZDlkddn7GPJkGEmxA8E07XQ2Yv_j8/s790-rw-e365/fraud.png)

The ultimate objective, per HUMAN, was to register views for as many as 25 video ads by layering them atop one another in a manner that's completely invisible to the users and generate illicit revenue.

"It doesn't stop with the stacked ads, though," the company said. "For as many of those as might be rendering on a user's device at once, they keep loading new ads until the ad slot with the malicious ad code is closed."

[![Ad Fraud Scheme](data:image/png;base64... "Ad Fraud Scheme")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_Z1EQqt83SKOvBGOPGYVLkFguphlnEY7NlTO5i-uvjgs1FQzDCmoeJW0vqooQLGqGG0g0FV5Ge1DNR0hk7SfY1yM7uueK0oAgrSS925rkN4roj88Q76pbsV0-5SEEM32MjTN8fDJGVk8gLjYau-Nuv47U_jmusv15jmXd16O3nWlLGbdKZQZB8TSP/s790-rw-e365/ads.png)

"The actors behind the VASTFLUX scheme clearly have an intimate understanding of the digital advertising ecosystem," it further added, stating the campaign also rendered an endless "playlist" of ads to defraud both the advertising companies and the apps that show ads.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The takedown of VASTFLUX arrives three months after the disruption of [Scylla](https://thehackernews.com/2022/09/experts-uncover-85-apps-with-13-million.html), a fraud operation targeting advertising software development kits (SDKs) within 80 Android apps and 9 iOS apps published on the official storefronts.

VASTFLUX, which generated over 12 billion bid requests per day at its peak, is also the latest in a stretch of ad fraud botnets that have been shuttered in recent years, after [3ve](https://www.humansecurity.com/learn/blog/3ve/foreword), [PARETO](https://www.humansecurity.com/learn/blog/disrupting-pareto), and [Methbot](https://www.humansecurity.com/learn/blog/the-sentencing-of-the-king-of-fraud-and-the-birth-of-collective-protection).

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

[hacking news](https://thehackernews.com/search/label/hacking%20news)[malvertising](https://thehackernews.com/search/label/malvertising)[mobile hacking](https://thehackernews.com/search/label/mobile%20hacking)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra I...
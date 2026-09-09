---
title: BengalSEO Poisons Bing Search Results to Deliver MayaBot and Tech Support Scams
url: https://thehackernews.com/2026/09/bengalseo-poisons-bing-search-results.html
source: The Hacker News
date: 2026-09-08
fetch_date: 2026-09-09T06:56:59.071884
---

# BengalSEO Poisons Bing Search Results to Deliver MayaBot and Tech Support Scams

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [BengalSEO Poisons Bing Search Results to Deliver MayaBot and Tech Support Scams](https://thehackernews.com/2026/09/bengalseo-poisons-bing-search-results.html)

**Ravie Lakshmanan**Sep 08, 2026Web Security / Phishing

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_rKrsCwJpZOS1Cu2htzFszKn4OgjK2p5A43OUaQJsmlbjsaLfGHtgyqQPfOu3IFWqRBoj2J6hIiqv6CVr56ZLyyf73-E71iaDRB2nrO9qaGOg92EbOcutMu8M8i1uimwkC-GPcc9oGDgFNNLB4kkgfDB3MbcjPuAn_gsml3FyThlEyI3Pg8E-udYq175m/s1700-nu-rw-lo-l85-e365/bing.jpg)

Cybersecurity researchers have disclosed details of a sprawling search engine optimization (SEO) poisoning campaign that paves the way for malware deployment and tech support scams.

The campaign, discovered by the DFIR Report in March 2026, has been codenamed **BengalSEO**. It has operated out of the Indian state of Rajasthan since at least 2015, driven by two IT service providers named WeConnect Solutions LLC (previously iConnect Soft Solutions LLC) and Garage2Global.

Although Garage2Global claims to be a website design, SEO, and digital marketing services provider, the cyber threat intelligence platform said it unearthed evidence indicating the company develops malicious web infrastructure used in SEO poisoning campaigns as part of the BengalSEO scam cluster.

"This group utilizes its extensive SEO and web development capabilities to create and promote lure pages with multiple Black Hat SEO techniques," the DFIR Report said in a [technical analysis](https://thedfirreport.com/2026/08/24/bengalseo-part-1-anatomy-of-the-operation/) published late last month. "These lure pages then tie into a sophisticated traffic distribution system to direct, track, and filter traffic to payloads and tech support scams."

One of the payloads is a custom malware dubbed MayaBot, which is responsible for enabling command-and-control (C2), system monitoring, and delivering an XMRig cryptocurrency miner. BengalSEO is said to have leveraged MayaBot since 2022 to carry out the group's operations.

The financially motivated threat actor has been described as possessing extensive knowledge of black hat SEO techniques and web development to create and promote a cluster of rogue lure pages to deliver MayaBot malware or dupe victims into calling their scam call centers. It also integrates a sophisticated traffic distribution system (TDS) to handle traffic flow, campaign performance, and cloaking.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Specifically, the TDS acts as a gating mechanism to lead victims to payload delivery domains through a redirector chain, while employing a legitimate privacy-first analytics service called Matomo for victim tracking and fingerprinting.

The starting point of the operation is a network of malicious lure pages that are promoted via SEO poisoning techniques so that they appear at the top of search results on Microsoft Bing. The decoy pages impersonate legitimate technical support and service activation portals for streaming services. They also claim to offer downloads for antivirus tools, gaming software, and taxation utilities, as well as activate credit, healthcare, and gift cards.

One such example hijacks searches for "bitdefender central how to login" to serve a fraudulent link hosted on readthedocs[.]io. The page features a prominent "Get Started" button that initiates the infection chain and routes unsuspecting users through a series of redirector domains to fingerprint their web browser before taking them to the appropriate final landing page.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijJYxuwyjJ0sTWA1ZFFEZSlJWTwWS1M1Jr4vrP35EIFSjinVdS9EtRe9ceDCnuOlTte0wpaH9JHunTQxNHRCi2Sj9jU3kKjq9tgVGMbgC58Mh_ryzY5yc5d04C25vi4iKeFVFdWVxZkNCm4yEuUxdIHAaFZfkCSBBzueNmY0OtUdLxfwyCyhjLWkuQIlx1/s1700-nu-rw-lo-l85-e365/cloaking.png)

"BengalSEO used backlinks, DOM injection, DOM shuffling, and keyword stuffing to enable their operation through Black Hat SEO techniques," the DFIR Report noted. "BengalSEO uses aggressive user-generated content (UGC) spam to generate backlinks at scale."

This involves flooding forums and comment sections with hyperlinks to the lure pages (e.g., "viziocomsetupentercode.github[.]io"), urging readers to set up their smart TV "easily" by following "simple on-screen instructions." The Vizio decoy page, for instance, has [2,000 backlinks and 167 unique external domains](https://ahrefs.com/backlink-checker/?input=viziocomsetupentercode.github.io&mode=subdomains) that link to the site.

This suggests that BengalSEO is heavily relying on a high volume of backlinks to manipulate search engine ranking algorithms and artificially boost the visibility of the lure pages on search engine results.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzlopnV5VTEciiVkegp1Qk0BXZB3ek7t2B-AUdiRAs2tdKH3sxlNwPojjPZc9ymSzzHK7GSYGXRP6s506YvVo3kydOU14xLbCQiRV7xgE33R2fUPX3AoSAgUsUmLSBEwq1uC0M9GwTIEz87XaCN7-R7TIIUA8cCSim9KZwAkMpPqvb6CV0KFMUiY6-pgei/s1700-nu-rw-lo-l85-e365/cloaking-1.png)

DOM Shuffling, on the other hand, refers to the practice of dynamically reordering HTML elements using embedded JavaScript code with the goal of randomizing the Document Object Model (DOM) structure. This, in turn, allows identical setup guides deployed across hundreds of domains to appear unique to web crawlers and bypass spam filters.

Before being served the main payload page, the TDS-based redirector domains display a Cloudflare Turnstile or hCaptcha challenge to screen automated scanners, crawlers, bots, and other unwanted visitors. The lure and landing pages come embedded with a Matomo tracking script to profile the browser on the client-side and send the information to the domain "stats.us3[.]org." A search for the domain "stats.us3[.]org" on urlscan.io [yields 1,112 results](https://urlscan.io/search/#domain%3Astats.us3.org) as of wr...
---
title: Researchers Uncover Chrome Extensions Abusing Affiliate Links and Stealing ChatGPT Access
url: https://thehackernews.com/2026/01/researchers-uncover-chrome-extensions.html
source: The Hacker News
date: 2026-01-30
fetch_date: 2026-01-31T04:05:14.570756
---

# Researchers Uncover Chrome Extensions Abusing Affiliate Links and Stealing ChatGPT Access

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

# [Researchers Uncover Chrome Extensions Abusing Affiliate Links and Stealing ChatGPT Access](https://thehackernews.com/2026/01/researchers-uncover-chrome-extensions.html)

**Ravie Lakshmanan**Jan 30, 2026Malware / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4xLoFpuzf6DbHF4Fy9WnEv4INmkiXkLiWxb9Pc7eqWDphv3Wcp57B38zLriR2xberjGDP_Xll60j1q8KmqpFTu9yfBIuyWilyHA97sm4-2CD_yqTOJubfYUKDp_-gkGHS-f-tcZYMk4N3sjwNzcy3GomBw-yVigT-MqY3J77PiGLVQyGK8JKHla5vykAd/s1700-e365/chrome.jpg)

Cybersecurity researchers have discovered malicious Google Chrome extensions that come with capabilities to hijack affiliate links, steal data, and collect OpenAI ChatGPT authentication tokens.

One of the extensions in question is Amazon Ads Blocker (ID: pnpchphmplpdimbllknjoiopmfphellj), which claims to be a tool to browse Amazon without any sponsored content. It was uploaded to the Chrome Web Store by a publisher named "10Xprofit" on January 19, 2026.

"The extension does block ads as advertised, but its primary function is hidden: it automatically injects the developer's affiliate tag (10xprofit-20) into every Amazon product link and replaces existing affiliate codes from content creators," Socket security researcher Kush Pandya [said](https://socket.dev/blog/malicious-chrome-extension-performs-hidden-affiliate-hijacking).

Further analysis has determined that Amazon Ads Blocker is part of a larger cluster of 29 browser add-ons that target several e-commerce platforms like AliExpress, Amazon, Best Buy, Shein, Shopify, and Walmart. The complete list is as follows -

* AliExpress Invoice Generator (FREE) - AliInvoice™️ (10+ Templates) (ID: mabbblhhnmlckjbfppkopnccllieeocp)
* AliExpress Price Tracker - Price History & Alerts (ID: loiofaagnefbonjdjklhacdhfkolcfgi)
* AliExpress Quick Currency & Price Converter (ID: mcaglpclodnaiimhicpjemhcinjfnjce)
* AliExpress Deals Countdown - Flash Sale Timer (ID: jmlgkeaofknfmnbpmlmadnfnfajdlehn)
* 10Xprofit - Amazon Seller Tools (FBA & FBM) (ID: ahlnchhkedmjbdocaamkbmhppnligmoh)
* Amazon Ads Blocker (ID: pnpchphmplpdimbllknjoiopmfphellj)
* Amazon ASIN Lookup 10xprofit (ID: ljcgnobemekghgobhlplpehijemdgcgo)
* Amazon Search Suggestion (ID: dnmfcojgjchpjcmjgpgonmhccibjopnb)
* Amazon Product Scraper 10xprofit (ID: mnacfoefejolpobogooghoclppjcgfcm)
* Amazon Quick Brand Search (ID: nigamacoibifjohkmepefofohfedblgg)
* Amazon Stock Checker 999 (ID: johobikccpnmifjjpephegmfpipfbfme)
* Amazon Price History Saver (ID: kppfbknppimnoociaomjcdgkebdmenkh)
* Amazon ASIN Copy (ID: aohfjaadlbiifnnajpobdhokecjokhab)
* Amazon Keyword Cloud Generator (ID: gfdbbmngalhmegpkejhidhgdpmehlmnd)
* Amazon Image Downloader (ID: cpcojeeblggnjjgnpiicndnahfhjdobd)
* Amazon Negative Review Hider (ID: hkkkipfcdagiocekjdhobgmlkhejjfoj)
* Amazon Listing Score Checker (ID: jaojpdijbaolkhkifpgbjnhfbmckoojh)
* Amazon Keyword Density Searcher (ID: ekomkpgkmieaaekmaldmaljljahehkoi)
* Amazon Sticky Notes (ID: hkhmodcdjhcidbcncgmnknjppphcpgmh)
* Amazon Result Numbering (ID: nipfdfkjnidadibpbflijepbllfkokac)
* Amazon Profit Calculator Lite (ID: behckapcoohededfbgjgkgefgkpodeho)
* Amazon Weight Converter (ID: dfnannaibdndmkienngjahldiofjbkmj)
* Amazon BSR Fast View (ID: nhilffccdbcjcnoopblecppbhalagpaf)
* Amazon Character Count & Seller Tools (ID: goikoilmhcgfidolicnbgggdpckdcoam)
* Amazon Global Price Checker (ID: mjcgfimemamogfmekphcfdehfkkbmldn)
* BestBuy Search By Image (ID: nppjmiadmakeigiagilkfffplihgjlec)
* SHEIN Search By Image (ID: mpgaodghdhmeljgogbeagpbhgdbfofgb)
* Shopify Search By Image (ID: gjlbbcimkbncedhofeknicfkhgaocohl)
* Walmart Search By Image (ID: mcaihdkeijgfhnlfcdehniplmaapadgb)

While "Amazon Ads Blocker" offers the advertised functionality, it also embeds malicious code that scans all Amazon product URL patterns for any affiliate tag without requiring any user interaction, and replaces it with "10xprofit-20" (or "\_c3pFXV63" for AliExpress). In cases where there are no tags, the attacker's tag is appended to each URL.

Socket also noted that the extension listing page on the Chrome Web Store makes misleading disclosures, claiming that the developers earn a "small commission" every time a user makes use of a coupon code to make a purchase.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Affiliate links are widely used across social media and websites. They refer to URLs containing a specific ID that enables tracking of traffic and sales to a particular marketer. When a user clicks this link to buy the product, the affiliate earns a cut of the sale.

Due to the extensions searching for existing tags and replacing them, social media content creators who share Amazon product links with their own affiliate tags lose commissions when users who have installed the add-on click those links.

This amounts to a violation of [Chrome Web Store policies](https://developer.chrome.com/docs/webstore/program-policies/affiliate-ads), as they require extensions using affiliate links to accurately divulge how the program works, require user action before each injection, and never replace existing affiliate codes.

"The disclosure describes a coupon/deal extension with user-triggered reveals. The actual product is an ad blocker with automatic link modification," Pandya explained. "This mismatch between disclosure and implementation creates false consent."

"The extension also violates the [Single Purpose policy](https://developer.chrome.com/docs/webstore/program-policies/policies) by combining two unrelated functions (ad blocking and affiliate injection) that should be separate extensions."

The identified extensions have also been found to scrape product data and exfiltrate it to "app.10xprofit[.]io," with those focusing on AliExpress serving bogus "LIMITED TIME DEAL" countdown timers on product pages to create a false sense of urgency and rush them into making purchases so as to earn commissions on affiliate links.

"Extensions that combine unrelated functionality (ad blocking, price comparison, coupon finding) with affiliate injection should be treated as high-risk, particularly those with disclosures that don't match the actual code behavior," Socket said.

The disclosure comes as Broadcom-owned Symantec flagged four different extensions that have a combined user base exceeding 100,000 users and are designed to steal d...
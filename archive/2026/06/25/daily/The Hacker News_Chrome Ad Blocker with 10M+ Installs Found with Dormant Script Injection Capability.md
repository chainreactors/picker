---
title: Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability
url: https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html
source: The Hacker News
date: 2026-06-25
fetch_date: 2026-06-26T06:09:43.487864
---

# Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html)

**Ravie Lakshmanan**Jun 25, 2026Browser Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqtdBDQ0Y38i0JZmDwU6XKiZ1R6HJ0KHe59012E0krnPubG5pJgiTg6IUg4fHEzoW5jm7QyEk8fXOL9swj7FlpXdMcjyn0ltziMhQJD2pYPtzjXimsntV8DFg-c1erOgWkLl8du8eBvJYlukTCDDycp5jSmWNfwmv5WwGKlJRJvZt1GvUZZl24dP2HVDkn/s1700-e365/adblocker.jpg)

An analysis of a popular Google Chrome ad block extension for YouTube has uncovered the ability to execute arbitrary JavaScript code.

According to Island, the extension, named **[Adblock for YouTube](https://chromewebstore.google.com/detail/adblock-for-youtube/cmedhionkhpnakcndndgjdbohmhepckk?hl=en)** (ID: cmedhionkhpnakcndndgjdbohmhepckk), has more than 10 million installs and carries a Featured badge on the Chrome Web Store.

The extension description states that it allows users to prevent web page elements like ads, including preroll ads, from being displayed on the video sharing platform, as well as on external sites that load YouTube. While the add-on offers the promised functionality, it also features capabilities to run arbitrary JavaScript code.

"It also contains the architectural ingredients for arbitrary JavaScript execution on any website, activated by a single server-side configuration change, without an extension update, without a store review, and without any visible sign that something has changed," researchers Oleg Zaytsev and Shachar Gritzman [said](https://www.island.io/blog/badblocker-11-million-users-one-server-call-away-from-compromise) in a report shared with The Hacker News.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"In practical terms, that could mean reading pages, stealing data, and acting as the user inside personal accounts, work apps, admin panels, and other sensitive browser sessions."

It's worth emphasizing here that there is no evidence malicious payload has been distributed to users in this manner, but the mere presence of the capability, coupled with ties to other ad-blocking extensions that have since been removed from the storefront for malware, raises privacy and security risks, Island added.

The list of related extensions that have been taken down is listed below -

* Adblock for Chrome (ID: onomjaelhagjjojbkcafidnepbfkpnee)
* Adblock for You (ID: ogcaehilgakehloljjmajoempaflmdci)
* AdBlock Suite (ID: gekoepiplklhniacchbbgbhilidiojmb)

Adblock for YouTube has been on the Chrome Web Store since 2014, starting off as a basic YouTube ad blocker before it changed ownership four years later. Early iterations of the extension were found to ship with an ad-injection software development kit (SDK) named Unistream SDK, although it was removed in June 2024.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuD0n65nmg8U1KqemSILCQI1hsrVBu_Q0jgmz-TEMpOhZCKz06-dwNUZyHRrZIIF5hmAOxn6Zn9JJyREGpAJI01nX2dJnPqU1JfEAVXfaKjrKNdaYDfiLP95N4R946LarfR9bPqb1RUKqfuvJLZetTRg_VxYlr2t5t_f6ebHiIOkIMjtrwmbhq8G2DKnHc/s1700-e365/adblock.jpg)

What's been constant is the presence of remote-controlled script injection paths since February 2025, opening the door to the creation of arbitrary "<script> elements using a bespoke scriptlet rule ("trusted-create-element") defined by the extension author that can, in turn, access sensitive data.

"At the time of our analysis, trusted-create-element was not active in the server response," the researchers explained. "The capability is dormant, not absent. Activating it requires a single server-side change, no extension update, no store review."

Compounding the risk further is the fact that ad blocker extensions typically request extensive permissions to inspect requests, alter pages, hide elements, and adjust their behavior as ad systems evolve.

Specifically, it's been found that contrary to its name, the extension runs on every website a user visits on the browser, while adding a check that activates only when the current URL contains "youtube.com." However, in reality, the check only verifies if the string corresponding to "youtube.com" appears anywhere in the URL, and does not validate the hostname, frame origin, or embedded player context.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

This means that the check can be trivially bypassed by putting youtube.com anywhere in the URL, as depicted in the following URL patterns -

* www.facebook.com/page?ref=youtube.com
* bank.example.com/search?q=youtube.com
* internal.corp.com/redirect?from=youtube.com

"The concern is not a single suspicious line of code," Island said. "It is the combination: a high-install extension with all-site access, a remote-controlled injection path, prior ad-injection infrastructure, a major ownership and codebase change, and related extensions that were removed from the Chrome Web Store for malware."

The Hacker News has contacted the developer of the extension for comment, and we will update the story if we hear back.

The disclosure comes as Palo Alto Networks Unit 42 said it detected 18 browser extensions impersonating consumer brands with an aim to monetize through affiliate marketing.

"Upon installation, all extensions open the .shop domain in a new tab," Unit 42 [said](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-06-24-affiliate-marketing-fraud-via-brand-impersonation-extension-farm.txt). "The .shop domain redirects to another domain. The domain presents a page citing that further action is required. The page cites incompatibility issues and asks users to install a gaming-oriented browser."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/the...
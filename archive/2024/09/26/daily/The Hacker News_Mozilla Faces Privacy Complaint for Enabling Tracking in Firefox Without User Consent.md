---
title: Mozilla Faces Privacy Complaint for Enabling Tracking in Firefox Without User Consent
url: https://thehackernews.com/2024/09/mozilla-faces-privacy-complaint-for.html
source: The Hacker News
date: 2024-09-26
fetch_date: 2025-10-06T18:30:42.004250
---

# Mozilla Faces Privacy Complaint for Enabling Tracking in Firefox Without User Consent

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

# [Mozilla Faces Privacy Complaint for Enabling Tracking in Firefox Without User Consent](https://thehackernews.com/2024/09/mozilla-faces-privacy-complaint-for.html)

**Sep 25, 2024**Ravie LakshmananData Protection / Online Tracking

[![Tracking in Firefox](data:image/png;base64... "Tracking in Firefox")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiurnd2U_6yaK4uRg8AZlMyHa5ud3MwqyWpEysZ44qJ_4bmoAtzbx8NVFk2x5IDZpOImY2sMAUan0aaKnbb5_5Wopk723MB0y6EovaKLLVO961cdea-Q-0kTNgct_0SgKZbW4nwW0pVawBE9ibGxSIBogBtVs9ijhFfVDMf3qKYwIEOXZqenpOe1Dyftp4G/s790-rw-e365/firefox.png)

Vienna-based privacy non-profit noyb (short for None Of Your Business) has filed a complaint with the Austrian data protection authority (DPA) against Firefox maker Mozilla for enabling a new feature called Privacy-Preserving Attribution (PPA) without explicitly seeking users' consent.

"Contrary to its reassuring name, this technology allows Firefox to track user behavior on websites," noyb [said](https://noyb.eu/en/firefox-tracks-you-privacy-preserving-feature). "In essence, the browser is now controlling the tracking, rather than individual websites."

Noyb also called out Mozilla for allegedly taking a leaf out of Google's playbook by "secretly" enabling the feature by default without informing users.

PPA, which is [currently enabled](https://support.mozilla.org/en-US/kb/privacy-preserving-attribution) in Firefox version 128 as an experimental feature, has its parallels in Google's [Privacy Sandbox](https://thehackernews.com/2024/06/googles-privacy-sandbox-accused-of-user.html) project in Chrome.

The initiative, now [abandoned by Google](https://thehackernews.com/2024/07/google-abandons-plan-to-phase-out-third.html), sought to replace third-party tracking cookies with a set of APIs baked into the web browser that advertisers can talk to in order to determine users' interests and serve targeted ads.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Put differently, the web browser acts as a middleman that stores information about the different categories that users can be slotted into based on their internet browsing patterns.

PPA, per Mozilla, is a way for sites to "understand how their ads perform without collecting data about individual people," describing it as a "non-invasive alternative to cross-site tracking."

It's also similar to Apple's [Privacy Preserving Ad Click Attribution](https://thenextweb.com/news/google-and-facebook-are-gonna-hate-apples-new-privacy-preserving-online-ads), which allows advertisers to measure the effectiveness of their ad campaigns on the web without compromising on user privacy.

The way PPA works is as follows: Websites that serve ads can ask Firefox to remember the ads in the form of an impression that includes details about the ads themselves, such as the destination website.

If a Firefox user ends up visiting the destination website and performs an action that's deemed valuable by the business – e.g., making an online purchase by clicking on the ad, also called "conversion" – that website can prompt the browser to generate a report.

The generated report is encrypted and submitted anonymously using the Distributed Aggregation Protocol ([DAP](https://blog.cloudflare.com/have-your-data-and-hide-it-too-an-introduction-to-differential-privacy/)) to an "aggregation service," after which the results are combined with other similar reports to create a summary such that it makes it impossible to learn too much about any individual.

This, in turn, is made possible by a mathematical framework called [differential privacy](https://thehackernews.com/2022/03/privid-privacy-preserving-surveillance.html) that enables the sharing of aggregate information about users in a privacy-preserving manner by adding random noise to the results to prevent re-identification attacks.

"PPA is enabled in Firefox starting in version 128," Mozilla notes in a support document. "A small number of sites are going to test this and provide feedback to inform our standardization plans, and help us understand if this is likely to gain traction."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"PPA does not involve sending information about your browsing activities to anyone. Advertisers only receive aggregate information that answers basic questions about the effectiveness of their advertising."

It's this aspect that noyb has found fault with, as it's in violation of the European Union's (E.U.) stringent data protection regulations by enabling PPA by default without seeking users' permissions.

"While this may be less invasive than unlimited tracking, which is still the norm in the US, it still interferes with user rights under the E.U.'s GDPR," the advocacy group said. "In reality, this tracking option doesn't replace cookies either, but is simply an alternative - additional - way for websites to target advertising."

It further noted that a Mozilla developer [justified](https://mastodon.social/%40Schouten_B/112784434152717689) the move by claiming that users cannot make an informed decision and that "explaining a system like PPA would be a difficult task."

"It's a shame that an organization like Mozilla believes that users are too dumb to say yes or no," Felix Mikolasch, data protection lawyer at noyb, said. "Users should be able to make a choice and the feature should have been turned off by default."

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
[**Share on L...
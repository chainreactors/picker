---
title: Over 4,500 WordPress Sites Hacked to Redirect Visitors to Sketchy Ad Pages
url: https://thehackernews.com/2023/01/over-4500-wordpress-sites-hacked-to.html
source: The Hacker News
date: 2023-01-26
fetch_date: 2025-10-04T04:54:39.761457
---

# Over 4,500 WordPress Sites Hacked to Redirect Visitors to Sketchy Ad Pages

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

# [Over 4,500 WordPress Sites Hacked to Redirect Visitors to Sketchy Ad Pages](https://thehackernews.com/2023/01/over-4500-wordpress-sites-hacked-to.html)

**Jan 25, 2023**Ravie LakshmananWebsite Security / WordPress

[![WordPress Hacking](data:image/png;base64... "WordPress Hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6fbefyc6Sxt_01sChOycIIV18-08HOOFB8_JIHP7sKJ8nK45QvCXJotwyz-8DQdSzHQ7wrTzVf594F_W9yYz6F62qNlkluPPEKAY0jwhx_Eik068Vc-XAm9mbJsTKBrRZXnC6ZCbSg1VBTsuZ1VtNfgNTpAOsxb_C9BC3p4LdqLhFiBjNSSboA-k0/s790-rw-e365/wordpress.png)

A massive campaign has infected over 4,500 WordPress websites as part of a long-running operation that's been believed to be active since at least 2017.

According to GoDaddy-owned Sucuri, the infections involve the injection of obfuscated JavaScript hosted on a malicious domain named "track[.]violetlovelines[.]com" that's designed to redirect visitors to undesirable sites.

The latest [operation](https://publicwww.com/websites/%22violetlovelines.com%22/) is said to have been under way since December 26, 2022, according to [data](https://urlscan.io/search/#%22violetlovelines.com%22) from urlscan.io. A prior wave seen in [early December 2022](https://publicwww.com/websites/%22specialblueitems.com%22/) impacted more than 3,600 sites, while another set of attacks recorded in [September 2022](https://publicwww.com/websites/%22weatherplllatform.com%22/) ensnared more than 7,000 sites.

The rogue code is inserted in the WordPress index.php file, with Sucuri noting that it has removed such changes from more than 33,000 files on the compromised sites in the past 60 days.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"In recent months, this malware campaign has gradually switched from the notorious fake CAPTCHA push notification scam pages to black hat 'ad networks' that alternate between redirects to legitimate, sketchy, and purely malicious websites," Sucuri researcher Denis Sinegubko [said](https://blog.sucuri.net/2023/01/massive-campaign-uses-hacked-wordpress-sites-as-platform-for-black-hat-ad-network.html).

Thus when unsuspecting users land on one of the hacked WordPress sites, a redirect chain is triggered by means of a traffic direction system, landing the victims on pages serving sketchy ads about products that ironically block unwanted ads.

[![WordPress Hacking](data:image/png;base64... "WordPress Hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSg0d7jlrfuB2tQAJo_e-GqZ0BsP7xR2xHxRb6ndO0Ffe-dfNp4qwc-ad6MiTBiKtesCdzoRFAg2E8plHLT0Ontu5bPm42nowphIJwBnLPpVKBufwq1ZY-UOW71at--l_mCwf0WU9YILuDwB6Kd-qZwRlySBFnVcXgfUwplRqXIc5lTEQQsCoDhnk1/s790-rw-e365/website-hacking.png)

Even more troublingly, the website for one such ad blocker named Crystal Blocker is engineered to display misleading browser update alerts to trick the users into installing its extension depending on the web browser used.

The browser extension is used by nearly 110,000 users spanning [Google Chrome](https://chrome.google.com/webstore/detail/crystalblocker/ehhgaobakclpaachikjhcpelknghhbfh) (60,000+), [Microsoft Edge](https://microsoftedge.microsoft.com/addons/detail/crystalblocker/lneokhajjamkcciipddlogdbiegmcaim) (40,000+), and [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/crystalblocker/) (8,635).

"And while the extensions indeed have ad blocking functionality, there is no guarantee that they are safe to use — and may contain undisclosed functions in the current version or in future updates," Sinegubko explained.

Some of the redirects also fall into the outright nefarious category, wherein the infected websites act as a conduit for initiating drive-by downloads.

[![WordPress Hacking](data:image/png;base64... "WordPress Hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKzGBWTAJsG2hGDYvrhQYhEHJbstBINJljxqo3xhsOldnfKcyIR2sGCQt9BelkEFzFG7n8GgJ6UrkSpuhmzApLqx3EH15xLrrzU3Bf47IYnyrb65UH8lal-LE85T8UE8PHYxYtUD56__y2-K4QjhpTn-Zv3s6BpqiZIHpoN5lKKMt1uahiVGtxGa4h/s790-rw-e365/malware.png)

This also includes retrieving from Discord CDN an information-stealing malware known as Raccoon Stealer, which is capable of plundering sensitive data such as passwords, cookies, autofill data from browsers, and crypto wallets.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings come as threat actors are [setting up](https://thehackernews.com/2022/12/new-malvertising-campaign-via-google.html) [lookalike](https://thehackernews.com/2023/01/the-evolving-tactics-of-vidar-stealer.html) [websites](https://thehackernews.com/2023/01/raccoon-and-vidar-stealers-spreading.html) for a variety of legitimate software to [distribute stealers and trojans](https://thehackernews.com/2023/01/new-research-delves-into-world-of.html) through malicious ads in Google search results.

Google has since stepped in to block [one of the rogue domains](https://transparencyreport.google.com/safe-browsing/search?url=wholegrady.com) involved in the redirect scheme, classifying it as an unsafe site that installs "unwanted or malicious software on visitors' computers."

To mitigate such threats, WordPress site owners are advised to change passwords and update [installed](https://thehackernews.com/2023/01/wordpress-security-alert-new-linux.html) [themes and plugins](https://patchstack.com/category/security-advisories/) as well as remove those that are unused or abandoned by their developers.

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
[**Share on Twit...
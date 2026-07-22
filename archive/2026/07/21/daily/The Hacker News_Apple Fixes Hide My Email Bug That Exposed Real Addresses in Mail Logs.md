---
title: Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs
url: https://thehackernews.com/2026/07/apple-fixes-hide-my-email-bug-that.html
source: The Hacker News
date: 2026-07-21
fetch_date: 2026-07-22T05:04:26.141040
---

# Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Apple Fixes Hide My Email Bug That Exposed Real Addresses in Mail Logs](https://thehackernews.com/2026/07/apple-fixes-hide-my-email-bug-that.html)

**Ravie Lakshmanan**Jul 21, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiIg3Sasyz94bt9uOMqOnkEhZ4APzMbVwOObUmNzIGuYtxHO0wYNBu1LXTGi0Q5mTT6SI_CgqPwCWgejCc7BnclxwtLvDKiUlJR80nzE6dniSdomYMVcQU8Z1BQECtTvevKArxtEsJjB8Zeh2ouEgblz0vOiTDKcXUzpMzW70C56-Xbj-LT1gLp0Mbw99p/s1700-e365/apple-email.jpg)

Apple has moved to address a security flaw in its Hide My Email service that enabled users' real email addresses to be unmasked, effectively undermining the feature's privacy guarantees.

404 Media [reported](https://www.404media.co/apple-fixes-hide-my-email-vulnerability-after-404-media-coverage/) Tuesday that a fix for the issue was deployed by Apple on July 3, 2026, after more than a year, when it was [disclosed](https://easyoptouts.com/guides/apple-hide-my-email-is-leaking-email-addresses) to the company by Tyler Murphy, co-founder of EasyOptOuts.

Hide My Email [generates](https://support.apple.com/105078) unique, random email addresses that forward messages to a user's personal email inbox automatically. By creating disposable email addresses, the idea is to safeguard user privacy and tackle unwanted spam. The feature requires a paid subscription to iCloud+ and was [announced](https://thehackernews.com/2021/06/top-10-privacy-and-security-features.html) by Apple in June 2021.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

However, at the start of the month, details [emerged](https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html#email-privacy-flaw) of a flaw that made it possible to unmask a user's real email address hidden behind a Hide My Email address. The issue was first reported to Apple on June 13, 2025, with Cupertino unsuccessfully attempting to patch it earlier this March and again on June 30, 2026.

Although specifics about the issue were withheld at that time to avoid potential exploitation, more details have now been published given it has been finally plugged.

The crux of the problem was that simply sending a targeted Hide My Email user a message that got rejected as spam caused the person's real email address to appear in email logs.

"We don't know how often hidden email addresses were leaked in email logs. For many major email hosts, the leak was triggered simply by an email being automatically rejected as spam, even if it was a legitimate message. Such emails probably didn't make it to your inbox, so you can't review your spam folder to learn whether you were affected," Murphy and EasyOptOuts co-founder Ben Weiner told 404 Media.

It bears noting that while the bug has been resolved, it's possible that a real email address linked to a Hide My Email address created before July 7, 2026, may have been captured in mail transfer logs when non-malicious emails get bounced.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

The development comes as Apple is [facing](https://www.courtlistener.com/docket/73624685/alvarez-v-apple-inc/) a [class action lawsuit](https://www.pacermonitor.com/public/case/65717401/Alvarez_v_Apple_Inc), accusing it of misleading customers about the privacy of its Hide My Email feature while charging for it.

"Apple promised Hide My Email as a privacy feature customers paid for, whether directly through iCloud+ or indirectly through Apple's product-wide privacy representations, and failed to deliver it," according to the complaint. "Worse, Apple has been fully aware of this problem for over a year and has not fixed it."

"At no point during this period did Apple disable or pause Hide My Email, warn its customers of the flaw, or correct its privacy representations."

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

[Apple](https://thehackernews.com/search/label/Apple), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Consumer Security](https://thehackernews.com/search/label/Consumer%20Security), [Data Exposure](https://thehackernews.com/search/label/Data%20Exposure), [Digital Identity](https://thehackernews.com/search/label/Digital%20Identity), [email security](https://thehackernews.com/search/label/email%20security), [icloud](https://thehackernews.com/search/label/icloud), [Privacy](https://thehackernews.com/search/label/Privacy), [security update](https://thehackernews.com/search/label/security%20update), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat](data:image/svg+xml;base64... "URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat")

URGENT - Progress Tells Share...
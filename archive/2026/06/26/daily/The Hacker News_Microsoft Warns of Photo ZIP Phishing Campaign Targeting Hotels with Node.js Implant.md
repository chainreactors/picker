---
title: Microsoft Warns of Photo ZIP Phishing Campaign Targeting Hotels with Node.js Implant
url: https://thehackernews.com/2026/06/microsoft-warns-of-photo-zip-phishing.html
source: The Hacker News
date: 2026-06-26
fetch_date: 2026-06-27T05:52:31.426459
---

# Microsoft Warns of Photo ZIP Phishing Campaign Targeting Hotels with Node.js Implant

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

# [Microsoft Warns of Photo ZIP Phishing Campaign Targeting Hotels with Node.js Implant](https://thehackernews.com/2026/06/microsoft-warns-of-photo-zip-phishing.html)

**Swati Khandelwal**Jun 26, 2026Phishing / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWYWOSDRBtv65eOzqdHSuOxXN7BWyBo1EAltLLUTTKGt68GYJ67zn9ixdKIQjTPCgE3P1o09UzrwXzvbopRZIhjN0LxYAZR06WaXOd116NQutGo1zLaceeob3nkuIHCeP6ZhlVp1yVOfc7dt-YZKFhEJJiPF8H5P03bc1ny0E3mi7jbIhqh7wqodC_zKE/s1700-e365/hotel-photo-zip.jpg)

An active phishing campaign has been targeting hotel and other hospitality organizations across Europe and Asia since April 2026, using photo-themed ZIP files to drop a Node.js implant and dig into front-desk machines, Microsoft says.

The company has not attributed the activity to a known threat actor, and the operators' end goal is still unclear.

The lure plays to how hotels work. Phishing emails carry the display name "Booking Manager (via Calendly)" and reference guest complaints, bedbug infestations, room inquiries, health inspections, and stay reviews.

The lures came in Japanese, Danish, and Dutch, with Japanese the most common. The subject line names no recipient or property, which points to high-volume, list-driven sending rather than tailored spear phishing. The pressure is reputational: complaints, final warnings, threatened inspections.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The delivery is the interesting part. The operators route messages through Calendly's email notification system and Google's URL redirect service, a trick Microsoft calls **authentication laundering**. Emails sent through the direct Calendly path pass SPF, DKIM, and DMARC, because they really are sent from authorized infrastructure.

The checks confirm the sender is allowed to send. They say nothing about what the message is for. A multi-hop chain then walks the victim from a Calendly link through share.google and a Google redirect to a freshly registered, Cloudflare-fronted .cfd domain. That domain sits behind a Turnstile challenge that doubles as anti-analysis.

Click through, and the target downloads a file named photo-<numbers>.zip. Inside is a shortcut posing as an image: IMG-<numbers>.png.lnk in the first wave, PHOTO-<numbers>.png.lnk in the second.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCvpIw74RMjaGm8NbOn37t48gXsif-Ne68XQ2e1QXR9pHgjR8x-J61k5rgw9sqC3Ay4w1eDG4ocmjYog9MRzyle-2gve5_mrO_NzSvRLAI7dHxnlcUNYX7zhxpaV0IH7pnktbBV9vkl7lN0QPMMwn-IY0p9lGK67C5xpSxmBn_eFBrJfVbu2w44VHwQRs/s1700-e365/zip.jpg)

Opening it fires PowerShell. The script uses BigInt arithmetic to decode a hidden download URL, pulls a .ps1 to %TEMP%, and drops a legitimate Node.js v24.13.0 runtime from nodejs.org into user space, which then runs the JavaScript implant. No system-wide Node install is needed.

The implant is tracked as **TonRAT**. It resolves its C2 domains through the TON blockchain API, then opens an encrypted WebSocket channel, per [SOC Prime](https://socprime.com/active-threats/technical-analysis-of-suspicious-emails-targeting-the-hotel-industry/). Fetching domains on the fly makes static blocklists less useful.

After the compromise, the implant beaconed to fixed IPs over non-standard ports: 8443, 8445, 8453, 5555, and 56001 to 56003. Some hosts also showed headless browser automation (--headless --no-sandbox), an ip-api.com geolocation check, and a forced shutdown via cmd /c shutdown -s -t 0. [Microsoft has not reported](https://www.microsoft.com/en-us/security/blog/2026/06/25/photo-zip-campaign-targeting-hospitality-industry-delivers-node-js-implant-persistent-access/) confirmed data theft, ransomware, or named victims.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Full remediation has to hit both persistence paths: the RunOnce entry pointing into ProgramData and the Node.js Run key, plus the runtime and .js files under AppData\Local\Nodejs. Pulling one leaves the other alive. Reception, reservations, and front office systems are the first places to look.

The campaign is not brand new. SOC Prime and [ITOCHU](https://blog.itochuci.co.jp/entry/2026/06/11/110000) documented the same hotel phishing and the LNK-to-PowerShell-to-Node.js chain about two weeks earlier, and Microsoft says its findings line up with that reporting.

Booking-themed phishing aimed at hotel staff has been a recurring pattern, including [ClickFix campaigns that dropped PureRAT](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html) to steal Booking.com logins.

What none of the reports can answer yet is what these operators want. The access is durable, the cleanup is easy to get wrong, and the final payload has not been pinned down. That is enough to treat this as more than another booking-themed phish.

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

[Calendly](https://thehackernews.com/search/label/Calendly), [CloudFlare](https://thehackernews.com/search/label/CloudFlare), [Google](https://thehackernews.com/search/label/Google), [Malware](https://thehackernews.com/search...
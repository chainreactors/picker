---
title: Calendar Invites and Live Proxies: Inside a Google Session Hijacking Campaign
url: https://thehackernews.com/2026/11/calendar-invites-and-live-proxies.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:45.694928
---

# Calendar Invites and Live Proxies: Inside a Google Session Hijacking Campaign

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Calendar Invites and Live Proxies: Inside a Google Session Hijacking Campaign](https://thehackernews.com/2026/11/calendar-invites-and-live-proxies.html)

**The Hacker News**Nov 12, 2026Cloud Security / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhf8YVgw9hIWEYN0_qgaD6MVIZad0fOCu_J5Z4Cn2CDuMzcV7HOQ9Xt4E08l1nOo7uMjAyYqYP-bUy5zHisRW8cfeSVmJcCKYgCTI2y1MpRUwsM1I2cs0MsuoAy7VSGLyTPzonhKITzWPU1hTADZnFt5VTZhlt4eJohVas2tzhl47AOV3Cp53LC_uhlpVY/s1700-nu-rw-lo-l85-e365/mt.jpg)

Since mid-August 2026, a phishing operation has been stealing live Google sessions from corporate users. Every check defenders normally lean on to judge a link came back clean, and the operator designed it that way on purpose.

The Threat Research team at [Material Security](https://material.security/lp-cloud-office-security?utm_campaign=Email-Security&utm_source=the-hacker-news&utm_medium=Third%20Party) spotted the campaign and has since taken down hundreds of attacker domains in an effort the team calls Operation CloudFire. Here’s what the researchers found.

## The lure: Google Calendar invites

The messages show up as Google Calendar invites. Some arrive by BCC, and many come from an organization the recipient has already traded email with. The pretexts are deliberately boring: voicemail notifications, RFP and RFI requests, court summonses, and missed payment notices. Nothing about them stands out in a busy inbox.

Most of the links point to Google itself. The usual pattern runs through Google’s own /url redirector, with the real destination tucked into a query parameter. Other waves used share.google and Drive file links the same way, and one variant leaned on Intuit transaction notification links. Whenever a message gets scored, the domain, certificate, and reputation on display are all legitimate.

## The capture: a reverse proxy in front of Google sign-in

Once a victim clicks through, the attacker runs a live reverse proxy in front of the real Google sign-in page. The victim types a password, gets a genuine prompt, and approves it while the operator watches in real time. The server passes each second factor along to Google as it comes in, whether that’s an SMS code, an authenticator code, Google’s Tap-Yes number matching, or phone-based account recovery. None of those controls stop the session from being captured.

The framework behind it, known as Nyasher, has been publicly documented since February, after researchers found a hardcoded key in its JavaScript.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXW-lyHb6PkdIP7stwUVa8u-YYSudtINtjph52QKo7leBna-g3ORMiaAtfMLieoB0jL0Yp7rQXaNSjqmNt2WEsbSGVtHTvhLB1nnbvIWOlMHHv5i3CBiNtIeKkLaL4whjB3VLBFSAigfKEwhQgGDkF3BQXcN3ObOZBFRcPDVln2JKqUI78PfmI8rNPrr4/s1700-nu-rw-lo-l85-e365/1.png)

## Why the usual controls stay quiet

Reputation systems answer questions about ownership. They ask who registered a domain, what else it has hosted, and whether anyone has complained about it. This campaign was built so every one of those answers came back harmless.

It works in three layers. The first is Google’s redirector, which gives the initial hop a trusted Google URL. The second is a Cloudflare Turnstile challenge, and in some builds it’s the real widget served from Cloudflare’s own infrastructure. The third is the password capture page, and that’s where things get tricky for defenders. There’s no static site to scan. JavaScript builds the page in the browser after the visitor clears the challenge, so a crawler has nothing to fetch and a proxy log has nothing to record. As far as the researchers know, nobody had scanned those pages before the campaign was documented.

The infrastructure is also meant to be thrown away. Early waves used many lure domains spread across several registrars, and most were registered just days before use. Receiving endpoints went live one to twenty days ahead of the wave they served. One wildcard certificate was issued 46 minutes before the domain it covers was even registered. Blocking any single piece costs the operator a few dollars and an afternoon.

## What stopping it took

Researchers tracked the campaign from the start, following each variant as lures, gates, and endpoints rotated. Once detections were in place, they caught more than 99% of the malicious messages, with a reclassification rate of 0.01%. It’s been steady work, since the attacker kept changing tactics, themes, and lure text to slip past static, machine learning, and agentic detections.

What worked was refusing to let any one signal make the call. Reputation alone wouldn’t have caught this. Neither would link analysis, since the first hop is a Google URL and the final page doesn’t exist until a browser builds it. Instead, the detection approach weighs technical indicators alongside the apparent intent of the message, where its links actually end up, and the sending relationship behind it. Any one of those can be enough to act on. A detection built around a single signal inherits that signal’s blind spots, and this operator has put real effort into mapping them.

Where the analysis happens matters too. Gateways built to inspect mail in transit aren’t a great fit for calendar invites, and much of this campaign arrives as invites. Calendar invites need to be treated as a threat surface of their own, with the account’s full history used as context next to the technical signals.

## Where the damage lands

A hijacked session leaves its trail in Google Workspace audit logs. A live session reaches mail, Drive, and the ability to grant OAuth access in the victim’s name, so the blast radius goes well past the inbox.

That raises a couple of hard questions for security teams. Who’s actually reviewing those audit logs, and how fast can they act on what they find? Could the team revoke sessions, contain OAuth grants, and reset the affected account within an hour? Plenty of programs can’t, and an attacker holding a...
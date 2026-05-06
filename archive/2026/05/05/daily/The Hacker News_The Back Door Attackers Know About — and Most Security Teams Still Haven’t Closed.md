---
title: The Back Door Attackers Know About — and Most Security Teams Still Haven’t Closed
url: https://thehackernews.com/2026/05/the-back-door-attackers-know-about-and.html
source: The Hacker News
date: 2026-05-05
fetch_date: 2026-05-06T05:09:54.738561
---

# The Back Door Attackers Know About — and Most Security Teams Still Haven’t Closed

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [The Back Door Attackers Know About — and Most Security Teams Still Haven’t Closed](https://thehackernews.com/2026/05/the-back-door-attackers-know-about-and.html)

**The Hacker News**May 05, 2026SaaS Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMhaEkMCxALglRWDFwTHVYgZ0KrRmAuzdwfh0zbL5Ml163rakQSv8yRVQ8yTQ4xIAtcwdqvGyVXeZXgXGNYKoyStckJv2xzjH3f1O7oICND5cWbnIBGYkSVJbpDRYHH9XqNfFQNk1qWIVwd43UuJv2vozhpndzCMS789h026IKgX1t7pgp01AtI6i9wKE/s1700-e365/material.jpg)

Every AI tool, workflow automation, and productivity app your employees connected to Google or Microsoft this year left something behind: a persistent OAuth token with no expiration date, no automatic cleanup, and in most organizations, no one watching it. Your perimeter controls don't see it. Your MFA doesn't stop it. And when an attacker gets hold of one, they don't need a password.

OAuth grants don't expire when employees leave. They don't reset when passwords change. And in most organizations, nobody is watching them.

The model made sense when a handful of IT-approved apps needed calendar access. It doesn't hold up when every employee is independently wiring AI tools, workflow automations, and productivity apps directly into their Google or Microsoft environment — each one receiving a persistent, scoped token with no automatic expiration and no centralized visibility.

That's not a misconfiguration. It's how OAuth is designed to work. The gap is that most security programs weren't built to account for it at scale.

## CISOs know it's a problem. Most aren't solving it.

[New research from Material Security](https://material.security/resources/automating-oauth-grant-management-materials-research-shows-the-growing-gap-between-awareness-and-action?utm_source=third-party&utm_medium=blog&utm_campaign=20260505-the-hacker-news) quantifies the gap between awareness and action. 80% of security leaders consider unmanaged OAuth grants a critical or significant risk. Most have said as much for years.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsTygaceWrxyWhXfbcDkmZV9JeY4kSvXnGbuNlNtMqxU9w_p4WgNXOoy2wJ2YizDvkUOkbwAlw_Lywl_dKme8ZfxFGg7ebcB0WJbUgGgTmFB_zWBRzlhZtPWFwg_m5yfq-JENhTwGWV5m0IoWB8OvcdqwEKOWMRWyWvYDwiSUU5DeB29KIl_Iq5PkEf_8/s1700-e365/fig1.png)

But awareness doesn't translate directly into capability.  A substantial portion of organizations (45%) are doing nothing to monitor OAuth grants at scale. Many of the rest (33%) are running manual processes — tracking grants in spreadsheets, reviewing permissions on an ad hoc basis, relying on employees to flag unusual app behavior.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3OO8pv_ZKMiVIdT3Y62U8v9wOjV4rgRcxjofWLosXeRDVDVnYS7iZMNDGVPHDEAVCqblnAuGkI0tP_Svk3H0AuG1c534ItZP3HfElLdnAABGiRNRvn4dpQiumE_wQ-cAnij6xVRHgvBLJ_QWIgM49-vGnDfQzMG8xuoFo1M1mEItg527bzDIx1sSEm8I/s1700-e365/fig2.png)

Spreadsheets are not a threat response capability. They're a record of how much exposure an organization doesn't know it has.

## It's not theoreticalrisk

The argument for OAuth visibility often gets framed as employees piping sensitive information into third-party tools without IT visibility. That's a real problem, but it's the smaller one. The more pressing issue is that OAuth grants are an active attack vector. The [Drift incident](https://material.security/resources/the-supply-chain-is-the-new-watering-hole?utm_source=third-party&utm_medium=blog&utm_campaign=20260505-the-hacker-news) makes that concrete.

Drift, a sales engagement platform acquired by Salesloft, maintained OAuth integrations with Salesforce instances across hundreds of customer organizations. A threat actor tracked by Palo Alto Unit 42 as UNC6395 obtained valid OAuth refresh tokens — likely through prior phishing campaigns — and used them to access Salesforce environments belonging to more than 700 organizations.

The attack's structure is a warning: the tokens were legitimate, the integration was legitimate. From the perspective of any perimeter control, nothing was wrong. MFA was bypassed entirely because the attacker wasn't logging in — they were presenting a token that Drift had already been granted permission to use. Once inside, UNC6395 systematically exported data and combed through it for credentials: AWS access keys, Snowflake tokens, passwords.

Cloudflare, PagerDuty, and dozens of others were affected. The full scope is still being assessed.

The Drift incident wasn't an attack from a suspicious, unknown app. It was an attack *through* a trusted one. The lesson isn't that organizations should restrict OAuth integrations — it's that trusting an app at the time of installation doesn't mean it stays trustworthy, and that OAuth grants need active, continuous monitoring rather than passive acceptance.

## What monitoring actually needs to look like

The current generation of OAuth security tools addresses OAuth risk at the point of installation. They check whether a requested permission scope is excessive. They may flag apps from vendors with poor reputations. That's useful — but it's not sufficient. For the Drift scenario, a legitimate app whose credentials were later stolen and weaponized — it catches nothing.

To begin with, vendor trust levels and app scopes are important, but it only tells part of the story. Monitoring the actual behavior of the app–the API calls it makes, the actions it takes–is critical to understanding what the app is *actually* doing, not just what it could do. And even then, without deep visibility into the account(s) the app is linked to, you’re still operating half-blind. A risky app tied to an intern’s account is one thing–the same app being used by a VIP with access to countless sensitive emails, files, and systems is something else entirely.

The Drift attack didn't involve a suspicious app requesting unusual permissions at installation. It involved a le...
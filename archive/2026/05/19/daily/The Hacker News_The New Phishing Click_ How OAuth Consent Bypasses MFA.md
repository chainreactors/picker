---
title: The New Phishing Click: How OAuth Consent Bypasses MFA
url: https://thehackernews.com/2026/05/the-new-phishing-click-how-oauth.html
source: The Hacker News
date: 2026-05-19
fetch_date: 2026-05-20T06:05:28.076854
---

# The New Phishing Click: How OAuth Consent Bypasses MFA

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

# [The New Phishing Click: How OAuth Consent Bypasses MFA](https://thehackernews.com/2026/05/the-new-phishing-click-how-oauth.html)

**The Hacker News**May 19, 2026Identity Security / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLnnvBvl0Gs5pfpUcrlJ_Ni62CyGs5UpoGCmpUAjReyBpExj5FzhuxSwuUcfQiyxDqeeoy6jSAHq4tA2KUnO5CRfbpfd_jN1ndeXgC0MiG0TrAfAyW67eybZeHMY-t6_kICQdPPKqK-1n9Ngkrj7UJrZZa1KQWqN9WjaTaDuHA_t6RW9Stul6tb82OS_4/s1700-e365/reco1.jpg)

In February 2026, a phishing-as-a-service (PhaaS) platform called [EvilTokens](https://labs.cloudsecurityalliance.org/research/csa-research-note-oauth-device-code-phishing-m365-20260325-c/) went live. Within five weeks, it had compromised more than 340 Microsoft 365 organizations across five countries.

The targets of the platform received a message asking them to enter a short code at microsoft.com/devicelogin and complete their normal MFA challenge, then walked away believing they had verified a routine sign-in. They had actually handed the operator a valid refresh token scoped to their mailbox, drive, calendar, and contacts, with the lifespan of a tenant policy rather than a session.

The operator never needed a password, never tripped an MFA prompt, and never produced a sign-in event that looked like an intrusion. The attack succeeded because the OAuth consent screen has become an instinctive click, and the controls built to stop credential phishing do not look at the consent layer.

Security researchers call the resulting condition consent phishing or OAuth grant abuse. The phishing click that mattered last decade handed over a password. The phishing click that matters now hands over a refresh token, and it sits structurally below the identity controls most organizations still treat as the perimeter.

## **Why MFA Cannot See an OAuth Grant**

A credential phish hands over a username and password that has to be replayed somewhere, and most identity stacks now demand a second factor at the replay. Even adversary-in-the-middle (AiTM) kits produce a session cookie tied to a sign-in event that the SIEM correlates against geography, device, and travel patterns.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5JIwDvfaKyGcj0TqarIPHXTums0vw-XcwuChUdiQcUW97w0O89OsC_vqeE-8_rUvzVaTw6zv2e1PKsCnHvn7AgmrvnxCh40mfyS_1rI7OcMRfJNQEAGdlVK41X9XxErLxOvsChlctDX2yxSE4ZfSCmQE-mAZk_a9p1vdiCgMgWNqMaDHNP9jCtaR2ToE/s1700-e365/1.png) |
| Figure 1: Credential phishing leaves a sign-in trail the SIEM can correlate. |

An OAuth grant produces no replayed credentials. The user authenticates on the legitimate identity provider, finishes the MFA challenge on the legitimate domain, and clicks Accept. The token the attacker walks away with is the system working as designed. It is signed by the identity provider, scoped to whatever the user agreed to, and refreshable. MFA cannot block it because MFA has already happened.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVF6GgTbkaDquC76Rf4ki6La-i0vin7TFrtzKOsbFDRuIv4RdyeJosUaSkX-6JPJal90jzb7sIQtxlflX1a540Es_jZEoe4IK87wYwmcBomfUCDwXyPSuNR1RCcdmm5ti8GxURJM5aCPLlALJ5LlN6LnL6nm8OJQXXlSabpAcLd0Bd0ZUq3h-YaOEh4gs/s1700-e365/2.png) |
| Figure 2: An OAuth grant leaves no replay, just a refreshable token. |

The other problem is that refresh tokens then extend the window. The tokens EvilTokens issued survived password resets and remained valid for weeks or months, depending on the tenant configuration. Rotating the password did not invalidate the grant. Only explicit revocation, or a conditional access policy that demanded re-consent, closed it.

## **How Consent Got Normalized**

This attack vector has existed since OAuth became standard. What changed is the environment it operates in. Users have been trained to click through consent screens at the rate they once clicked through cookie banners. Every AI agent installs Surface One. Every productivity integration surfaces one. Every browser extension that touches a SaaS account surfaces one. The volume of legitimate consent that a knowledge worker sees in a month exceeds anything that existed when the original OAuth threat models were written.

The scopes themselves use language that does not map cleanly to risk. A scope called "Read your mail" sounds limited, but in practice it covers every message, attachment, and shared thread the user can access. A scope called "Access files when you're not present" means a long-lived token issued without the user being in front of a screen to revoke it. The gap between consent language and operational reach is exactly where attackers operate.

## **Toxic Combinations Form Below the Application Owner**

A single OAuth consent gives an attacker a scoped foothold inside one application. The deeper risk forms when those footholds bridge.

A finance user grants an AI meeting summarizer access to their calendar and mailbox. The same user later grants a productivity assistant access to the company's shared drive. A third grant connects a CRM enrichment tool to the customer database. Each was approved one at a time. No application owner sanctioned the combination. The risk surface is now three scopes intersecting through one human identity, where the meeting summarizer's compromise can reach contract drafts and customer records through the same person.

This is called a [toxic combination](https://thehackernews.com/2026/04/toxic-combinations-when-cross-app.html). It consists of a permission breakdown across applications, bridged by an OAuth grant, an integration, or an AI agent, that no single application owner ever authorized as its own risk surface. It cannot be seen by any one application's audit log because the bridge exists outside of all of them.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwqOKiXRSvHrfI9sbERjIxze4jIqEPzkJEGTQea3FOjd_bzUY9o0mGa_Fl...
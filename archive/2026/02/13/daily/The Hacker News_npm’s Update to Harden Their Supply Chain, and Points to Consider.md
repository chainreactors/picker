---
title: npm’s Update to Harden Their Supply Chain, and Points to Consider
url: https://thehackernews.com/2026/02/npms-update-to-harden-their-supply.html
source: The Hacker News
date: 2026-02-13
fetch_date: 2026-02-14T04:08:49.171262
---

# npm’s Update to Harden Their Supply Chain, and Points to Consider

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [npm’s Update to Harden Their Supply Chain, and Points to Consider](https://thehackernews.com/2026/02/npms-update-to-harden-their-supply.html)

**The Hacker News**Feb 13, 2026Supply Chain Security / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2f7TicFSKUe4LQJy82mhhepyMplbLHU-VNYpY_gxLvTILbFCviVqGKP4thBHnPvHWaw1EdFBuqDcDePYX1Z76KaB2j0pC8rWGM4eyu8tNLDcy0HChASJSx2zZufWVktAvzIR2yAJGDC0eIpVPV5u5OaAJsYohGS77dRTUcm_q3kl3D-N5hhCJ6XWxz-w/s1700-e365/npm-security.jpg)

In December 2025, in response to the Sha1-Hulud incident, npm completed a [major authentication overhaul](https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/#if-you-were-still-using-npm-classic-tokens) intended to reduce supply-chain attacks. While the overhaul is a solid step forward, the changes don’t make npm projects immune from supply-chain attacks. npm is still susceptible to malware attacks – here’s what you need to know for a safer Node community.

## **Let’s start with the original problem**

Historically, npm relied on classic tokens: long-lived, broadly scoped credentials that could persist indefinitely. If stolen, attackers could directly publish malicious versions to the author’s packages (no publicly verifiable source code needed). This made npm a prime vector for supply-chain attacks. Over time, numerous real-world incidents demonstrated this point. Shai-Hulud, Sha1-Hulud, and chalk/debug are examples of recent, notable attacks.

## **npm’s solution**

To address this, npm made the following changes:

1. npm revoked all classic tokens and defaulted to session-based tokens instead. The npm team also improved token management. Interactive workflows now use short-lived session tokens (typically two hours) obtained via npm login, which *defaults* to MFA for publishing.
2. The npm team also encourages OIDC Trusted Publishing, in which CI systems obtain short-lived, per-run credentials rather than storing secrets at rest.

In combination, these practices improve security. They ensure credentials expire quickly and require a second factor during sensitive operations.

## **Two important issues remain**

First, people need to remember that the original attack on tools like ChalkJS was a successful MFA phishing attempt on npm’s console. If you look at the original email attached below, you can see it was an MFA-focused phishing email (nothing like trying to do the right thing and still getting burned). The campaign tricked the maintainer into sharing both the user login and one-time password. This means in the future, similar emails could get short-lived tokens, which still give attackers enough time to upload malware (since that would only take minutes).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXFQSKG-LeBnnzMYojU9iWdG9dZ0E8eMhNOsR_lxwGOtJmUjU3dirzJq18nER5-x3lXbz38lSKks6VnmauJvvJuDCC4MP6wxWtmVaN5nh2iIei-gqAt8R8BgDUv-oMneR-oRw1r47iH8fdzNi_V7V8lKjg941WGR_XqXlKuQPkuplFLmTTMDGOQshN7XA/s1700-e365/npm.png)

Second, MFA on publish is optional. Developers can still create 90-day tokens with MFA bypass enabled in the console, which are extremely similar to the classic tokens from before.

These tokens allow you to read and write to a token author’s maintained packages. This means that if bad actors gain access to a maintainer’s console with these token settings, they can publish new, malicious packages (and versions) on that author’s behalf. This circles us back to the original issue with npm before they adjusted their credential policies.

To be clear, more developers using MFA on publish is good news, and future attacks should be fewer and smaller. However, making OIDC and MFA on-publish *optional* still leaves the core issue unresolved.

In conclusion, if (1) MFA phishing attempts to npm’s console still work and (2) access to the console equals access to publish new packages/versions, then developers need to be aware of the supply-chain risks that still exist.

## **Recommendations**

In the spirit of open source security, here are three recommendations that we hope GitHub and npm will consider in the future.

1. Ideally, they continue to push for the ubiquity of OIDC in the long term. OIDC is very hard to compromise and would almost completely erase the issues surrounding supply-chain attacks.
2. More realistically, enforcing MFA for local package uploads (either via an email code or a one-time password) would further reduce the blast radius of worms like Shai-Hulud. In other words, it would be an improvement to *not allow* custom tokens that bypass MFA.
3. At a minimum, it would be nice to add metadata to package releases, so developers can take precautions and avoid packages (or maintainers) who do not take supply chain security measures.

In short, npm has taken an important step forward by eliminating permanent tokens and improving defaults. Until short-lived, identity-bound credentials become the norm — and MFA bypass is no longer required for automation — supply-chain risk from compromised build systems remains materially present.

## **A new way to do it**

This entire time, we’ve been talking about supply-chain attacks by uploading packages to npm on a maintainer’s behalf. If we could build every npm package from verifiable upstream source code rather than downloading the artifact from npm, we’d be better off. That’s exactly what Chainguard does for its customers with Chainguard Libraries for JavaScript.

[We’ve looked at the public database for compromised packages across npm](https://www.chainguard.dev/unchained/mitigating-malware-in-the-npm-ecosystem-with-chainguard-libraries) and discovered that for 98.5% of malicious packages, the malware was not present in the upstream source code (just the published artifact). This means an approach of building from source would reduce your attack surface by some 98.5%, based on past ...
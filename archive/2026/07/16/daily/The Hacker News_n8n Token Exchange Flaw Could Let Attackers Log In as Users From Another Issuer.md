---
title: n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer
url: https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:23.808642
---

# n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer

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

# [n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer](https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html)

**Swati Khandelwal**Jul 16, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1Pvezsft8WXzYy1Lw3zKDZrkf0TNZfj95rzTnuQgzbJuztRDNDFK35ahO9UfhNJOicjjuzyZGFCtC_idBl8vgNdw4kzfeYFo6LwUur66S5qUTO2Bl3WVLwCDWoDTnw4dlZdj_ZQ1T2JcG1dWfJeoO3WDZs94EVm9z0hZ8VPL36KDpaAmw7fH9hSWSSaw/s1700-e365/n8n-main.jpg)

[n8n](https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html), the workflow automation platform, handed out the wrong accounts at login. On Enterprise instances configured to trust more than one external token issuer, it matched an incoming JWT to a local user on the `sub` claim alone and ignored `iss`.

A valid token from issuer A carrying a `sub` that belongs to someone under issuer B logged you in as them. Their password never came into it. n8n shipped the fix on June 24.

The flaw is tracked as [`CVE-2026-59208`](https://nvd.nist.gov/vuln/detail/CVE-2026-59208). The CVE record did not go public until July 9. n8n [credits the report](https://github.com/n8n-io/n8n/security/advisories/GHSA-mq3m-f8x3-579w) to the GitHub account [bearsyankees](https://github.com/bearsyankees), whose profile lists Strix, which makes an AI penetration testing agent.

Strix [says](https://www.strix.ai/blog/n8n-cross-issuer-account-takeover) it pointed out that the agent at the token-exchange flow and found the identity-binding bug there.

## Two issuers, one account

Token exchange is n8n's Enterprise route for [OEM partners who embed the product](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration), an [RFC 8693 implementation](https://docs.n8n.io/release-notes) that spares their users a second login screen.

The partner signs a short-lived JWT with its own key, n8n verifies it against a configured public key, matches the claims to a local account, and the user is in. Trusted keys go in `N8N_TOKEN_EXCHANGE_TRUSTED_KEYS`, and the [deployment docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment) still tag the feature as preview.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The token itself checks out. The matching is the bug. A `sub` value is only guaranteed to be unique inside the issuer that minted it. [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519.html) asks that it be "scoped to be locally unique in the context of the issuer" or else globally unique. The identifier for a user is therefore [the pair, `iss` plus `sub`](https://thehackernews.com/2025/06/noauth-vulnerability-still-affects-9-of.html).

n8n keyed on half of it. Nothing stops two issuers from emitting the same subject string, and when they do, both land on one n8n account.

## How big a deal is this

The flaw reaches an instance only if token exchange is switched on and the config trusts at least two external issuers. [n8n says](https://github.com/n8n-io/n8n/security/advisories/GHSA-mq3m-f8x3-579w) nothing else is affected. Token exchange is Enterprise-only and still flagged as a preview, so the exposed set is small and specific: OEM deployments, where trusting a second issuer is a supported configuration.

What the advisory does not pin down is how an attacker gets the token. It says only that they can obtain one. The practical question is whether an ordinary user at a trusted issuer can influence the `sub` they receive. The public record does not answer it. GitHub's CVSS 4.0 vector marks attack requirements as present and stops there.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5_A0dukdP3uSsRE-4hAiRENYYs2QhsO2JXXFdgoU0KOFApL9CBqhjYFmJ0_PVBC7xBoUl6qm98VXYB7mH6r4UJUU2H3I4wS3Y8Tr7kPgka2Cj5jvJqQtpFqU8gTYXor0bC4_evYFTNz_YthZ4Go7xsOs_9wBASZ5o2Gtb9x83E53B2j5HPGvIYdUWBt0/s1700-e365/n8n.jpg)

GitHub assigned that vector. As the CNA here, it puts `CVE-2026-59208` at 7.6 on CVSS 4.0, high. NVD puts the same bug at 6.8 on CVSS 3.1, medium, and has not issued a 4.0 assessment at all; its record carries `CWE-287` and `CWE-346`. CISA's July 13 SSVC assessment records exploitation as none, and The Hacker News found no public proof-of-concept in searches on July 16.

Two weeks before the June 24 fix, the maintainers patched [`CVE-2026-54305`](https://github.com/n8n-io/n8n/security/advisories/GHSA-2j5h-858j-5mpf), another Enterprise-only flaw. It lets any authenticated user overwrite or revoke another user's stored OAuth tokens through the Dynamic Credentials endpoints. That one was a missing ownership check, not an identity binding. Different bug, same surface.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The Hacker News has reached out to n8n for confirmation on the scope and impact of `CVE-2026-59208` and will update this story with any response.

## Patch or cut the issuer list

`CVE-2026-59208` affects every n8n release below 2.27.4 and version 2.28.0. The fix first landed in 2.27.4 and 2.28.1. Those are the floor. On July 16, n8n's npm package carried 2.30.6 on both its `latest` and `stable` tags. It ships a new minor most weeks by its own account, so check the tag and take the newest stable build your deployment supports.

If patching has to wait, work out what you are running: `N8N_TOKEN_EXCHANGE_TRUSTED_KEYS` holds the trusted signing keys, and a separate preview flag controls whether token exchange is on at all. Cut back to a single trusted issuer, or turn the feature off.

The advisory calls both short-term measures and says neither fully remediates the risk. ...
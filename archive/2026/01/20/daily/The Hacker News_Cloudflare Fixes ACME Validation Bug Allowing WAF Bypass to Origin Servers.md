---
title: Cloudflare Fixes ACME Validation Bug Allowing WAF Bypass to Origin Servers
url: https://thehackernews.com/2026/01/cloudflare-fixes-acme-validation-bug.html
source: The Hacker News
date: 2026-01-20
fetch_date: 2026-01-21T03:33:18.870281
---

# Cloudflare Fixes ACME Validation Bug Allowing WAF Bypass to Origin Servers

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

# [Cloudflare Fixes ACME Validation Bug Allowing WAF Bypass to Origin Servers](https://thehackernews.com/2026/01/cloudflare-fixes-acme-validation-bug.html)

**Ravie Lakshmanan**Jan 20, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFMNWyLouRnOIXsad4n8lgA97dY7GEYeVjCrVWqYokwEg-es4kDCyjPCwEKZ_q0LCOCjcufDbeBu-O_aJIuKYu6IY2g9ZMoMMxhkYgCWlsjeIA0ByqwBVJX-HaF_G3oNlBuUWsTk5b4K35K60lUrjrWQ-dhMtEymdsWX84cuPUERd5balmQJMZQqsfKhnu/s1600-e365/acme.jpg)

Cloudflare has [addressed](https://blog.cloudflare.com/acme-path-vulnerability/) a security vulnerability impacting its Automatic Certificate Management Environment ([ACME](https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment)) validation logic that made it possible to bypass security controls and access [origin servers](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/).

"The vulnerability was rooted in how our edge network processed requests destined for the ACME HTTP-01 challenge path (/.well-known/acme-challenge/\*)," the web infrastructure company's Hrushikesh Deshpande, Andrew Mitchell, and Leland Garofalo said.

The web infrastructure company said it found no evidence that the vulnerability was ever exploited in a malicious context.

ACME is a communications protocol ([RFC 8555](https://www.rfc-editor.org/rfc/rfc8555)) that facilitates automatic issuance, renewal, and revocation of SSL/TLS certificates. Every certificate provisioned to a website by a certificate authority (CA) is validated using challenges to prove domain ownership.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

This process is typically achieved using an ACME client like [Certbot](https://letsencrypt.org/docs/client-options/) that proves domain ownership via an [HTTP-01](https://letsencrypt.org/docs/challenge-types/) (or DNS-01) challenge and manages the certificate lifecycle. The HTTP-01 challenge checks for a validation token and a key fingerprint located in the web server at "https://<YOUR\_DOMAIN>/.well-known/acme-challenge/<TOKEN>" over HTTP port 80.

The CA's server makes an HTTP GET request to that exact URL to retrieve the file. Once the verification succeeds, the certificate is issued and the CA marks the ACME account (i.e., the registered entity on its server) as authorized to manage that specific domain.

In the event the challenge is used by a certificate order managed by Cloudflare, then Cloudflare will respond on the aforementioned path and provide the token provided by the CA to the caller. But if it does not correlate to a Cloudflare-managed order, the request is routed to the customer origin, which may be using a different system for domain validation.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX4Xwq3no3Rl4H2B7PE2zJJFc61ZZq5WHIUkzEigx2fp9JORe-xXxsMwSRn4Rb_LIdnTblNL2xnkXt5CV0h879BHUbOBz3VR9oEReIi2YPevhI5BF8tPSs2Iu2mhE3CDCDOgCPkU4DC7rjltwCpeZVmAYzdC__YhiTPq2iFgvArEaajpiBxQxWm3mN7Pt0/s1600-e365/flaw.jpg)

The vulnerability, [discovered and reported](https://fearsoff.org/research/cloudflare-acme) by FearsOff in October 2025, has to do with a flawed implementation of the ACME validation process that causes certain challenge requests to the URL to disable web application firewall (WAF) rules and allow it to reach the origin server when it should have been ideally blocked.

In other words, the logic failed to verify whether the token in the request actually matched an active challenge for that specific hostname, effectively permitting an attacker to send arbitrary requests to the ACME path and circumvent WAF protections entirely, granting them the ability to reach the origin server.

"Previously, when Cloudflare was serving an HTTP-01 challenge token, if the path requested by the caller matched a token for an active challenge in our system, the logic serving an ACME challenge token would disable WAF features, since Cloudflare would be directly serving the response," the company explained.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

"This is done because those features can interfere with the CA's ability to validate the token values and would cause failures with automated certificate orders and renewals. However, in the scenario that the token used was associated with a different zone and not directly managed by Cloudflare, the request would be allowed to proceed onto the customer origin without further processing by WAF rulesets."

Kirill Firsov, founder and CEO of FearsOff, said the vulnerability could be exploited by a malicious user to obtain a deterministic, long‑lived token and access sensitive files on the origin server across all Cloudflare hosts, opening the door to reconnaissance.

The vulnerability was addressed by Cloudflare on October 27, 2025, with a code change that serves the response and disables WAF features only when the request matches a valid ACME HTTP-01 challenge token for that hostname.

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

[ACME Protocol](https://thehackernews.com/search/label/ACME%20Protocol)[Certificate Authority](https://thehackernews.com/search/label/Certificate%20Authority)[CloudFlare](https://thehackernews.com/search/label/CloudFlare)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Web Application Firewall](https://thehackernews.com/search/label/Web%20Applicati...
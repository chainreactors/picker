---
title: RabbitMQ Flaws Could Leak OAuth Secrets and Expose Cross-Tenant Queue Metadata
url: https://thehackernews.com/2026/07/rabbitmq-flaws-could-leak-oauth-secrets.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:49:59.543000
---

# RabbitMQ Flaws Could Leak OAuth Secrets and Expose Cross-Tenant Queue Metadata

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

# [RabbitMQ Flaws Could Leak OAuth Secrets and Expose Cross-Tenant Queue Metadata](https://thehackernews.com/2026/07/rabbitmq-flaws-could-leak-oauth-secrets.html)

**Ravie Lakshmanan**Jul 14, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhhRQ9rN4_5eYqXiJ7svWKwWY0dcPiiALZ6EkDG05ruFzTANJtwyw_w2Ht29dON1oFiLAkQkE0M75FYExbXmvFSr4jU0K0sNlwRxG3Q1rU51ouVIt3UtnrazRwhCer3coTHbU3So1dXx_8Frh1KhJKKXc7Lq2h5DZTGkBq35Y2ngnGVg6wAGubf8cVRx0F/s1700-e365/rebbitmq.jpg)

Cybersecurity researchers have disclosed details of two access control-related flaws impacting the RabbitMQ message broker service that could allow attackers to leak OAuth client secrets, expose enterprise messaging infrastructure to takeover risks, and bypass tenant boundaries.

Miggo's security team, which [discovered](https://www.miggo.io/post/full-broker-takeover-no-login-required-miggo-discovers-critical-rabbitmq-vulnerabilities-putting-application-data-at-risk) and reported the flaws, said one "leaks the broker's confidential OAuth secret to an unauthenticated attacker in a single request, a direct path to full broker takeover in the configurations that use that secret." The second vulnerability allows any logged-in user to silently read other tenants' data.

Both shortcomings are said to have been present in the codebase since early 2024, impacting RabbitMQ release lines from 3.13.0 and later. They have been addressed in versions 4.3.0, 4.2.6, 4.1.11, 4.0.20, and 3.13.15. There is no evidence of active exploitation of either of the vulnerabilities prior to the public disclosure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

A brief description of the two flaws is below -

* **[CVE-2026-57219](https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-pj24-8j6m-vq9q)** (CVSS score: 8.7) - An obsolete HTTP API endpoint ("GET /api/auth") that reveals client secret on RabbitMQ installations that had OAuth 2 configured to use the management.oauth\_client\_secret configuration key, allowing an attacker to exchange it for an administrator token and obtain full control of every message, queue, user, and broker setting.
* **[CVE-2026-57221](https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-9q2j-2hq8-22r2)** (CVSS score: 5.3) - A missing authorization that allows any authenticated user who can connect to a virtual host to enumerate all queue and exchange names in that virtual host and read queue message counts and consumer counts, regardless of their actual permissions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg84d6nm_Z80hggjGZ80-AAZNuwThj5k9k5eyJNQ3sJLmMlXNEYkhMos96htxSxn5TtCc9DyxhZHU_Clh1yXDNOXvnvRZR5XZheQ3SiWrFqNYaGj0_ar4MKYWe8SVCvpO_UKc2LBVoLZZ51RrCkl6i2PrD1C1WLzHfQGe6q80auHugozayL8BzeQu9VubkB/s1700-e365/RabbitMQ.jpg)

"The endpoint's authorization check was hard-coded to always allow the request, unlike every other sensitive management endpoint," Miggo said about CVE-2026-57219. "The risk is sharpest wherever the management port is reachable by an untrusted network: cloud or multi-tenant setups, or a management UI accidentally exposed to the internet."

Besides patching to the latest versions, it's advised to rotate the OAuth client secret if the management interface is reachable over the internet, limit access to port 15672 to prevent the management interface from being reachable over the network, separate tenants by virtual host, and implement firewall rules to block access to the vulnerable endpoint on unpatched instances.

The disclosure comes as RabbitMQ maintainers addressed two critical-severity flaws that could result in a [TLS client-authentication bypass](https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-cw8c-4m83-9c6w) (CVSS score: 9.1) and allow an attacker in an adversary-in-the-middle (AitM) position to [forge JSON Web Key Set (JWKS) responses](https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-37wx-r6q9-6fhj) and cause the broker to accept arbitrary JWTs (CVSS score: 9.2).

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

[API Security](https://thehackernews.com/search/label/API%20Security), [Application Security](https://thehackernews.com/search/label/Application%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [Identity and Access Management](https://thehackernews.com/search/label/Identity%20and%20Access%20Management), [network security](https://thehackernews.com/search/label/network%20security), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](data:image/svg+xml;base64... "16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems")

16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](htt...
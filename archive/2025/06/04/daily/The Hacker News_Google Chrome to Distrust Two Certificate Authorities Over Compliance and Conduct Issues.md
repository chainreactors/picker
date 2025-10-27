---
title: Google Chrome to Distrust Two Certificate Authorities Over Compliance and Conduct Issues
url: https://thehackernews.com/2025/06/google-chrome-to-distrust-two.html
source: The Hacker News
date: 2025-06-04
fetch_date: 2025-10-06T22:56:45.847038
---

# Google Chrome to Distrust Two Certificate Authorities Over Compliance and Conduct Issues

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

# [Google Chrome to Distrust Two Certificate Authorities Over Compliance and Conduct Issues](https://thehackernews.com/2025/06/google-chrome-to-distrust-two.html)

**Jun 03, 2025**Ravie LakshmananWeb Security / Digital Identity

[![Certificate Authorities](data:image/png;base64... "Certificate Authorities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh_48johKFC7YPzw28rfrEogqVFntJg71bh1VOHlVs577leNUQMznUGhkdVHiAulT88o9jEuUKoz9uRiYbswcGG9XrIPGv62FFvDvgAU2dQCiHLIQjtzicH5Qf6kB4Ftv9VlTf83wJbGI3w-diiS7bu8p2RNYTE1Tq8kKFPoIZsVD2eO8Zagv1n8x2zVfa/s790-rw-e365/chrome-root-certs.jpg)

Google has revealed that it will no longer trust digital certificates issued by Chunghwa Telecom and Netlock citing "patterns of concerning behavior observed over the past year."

The changes are expected to be introduced in Chrome 139, which is [scheduled](https://chromiumdash.appspot.com/schedule) for public release in early August 2025. The current major version is 137.

The update will affect all Transport Layer Security (TLS) server authentication certificates issued by the two Certificate Authorities (CAs) after July 31, 2025, 11:59:59 p.m. UTC. Certificates issued before that date will not be impacted.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Chunghwa Telecom is Taiwan's largest integrated telecom service provider and Netlock is a Hungarian company that offers digital identity, electronic signature, time stamping, and authentication solutions.

"Over the past several months and years, we have observed a pattern of compliance failures, unmet improvement commitments, and the absence of tangible, measurable progress in response to publicly disclosed incident reports," Google's Chrome Root Program and the Chrome Security Team [said](https://security.googleblog.com/2025/05/sustaining-digital-certificate-security-chrome-root-store-changes.html).

"When these factors are considered in the aggregate and considered against the inherent risk each publicly-trusted CA poses to the internet, continued public trust is no longer justified."

As a result of this change, Chrome browser users on Windows, macOS, ChromeOS, Android, and Linux who navigate to a site serving a certificate issued by either of the two CAs after July 31, will be served a full-screen security warning.

Website operators who rely on the two CAs are recommended to use the Chrome Certificate Viewer to check the validity of their site's certificates and transition to a new publicly-trusted CA as soon as "reasonably possible" to avoid any user disruption.

Enterprises, however, can override these [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/faq.md#What-is-the-Chrome-Root-Store) constraints by installing the corresponding root CA certificate as a [locally-trusted root](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/faq.md#How-does-the-Chrome-Certificate-Verifier-integrate-with-platform-trust-stores-for-local-trust-decisions) on the platform Chrome is running. It's worth noting that Apple has [distrusted](https://support.apple.com/en-us/121668) the root CA certificate "NetLock Arany (Class Gold) Főtanúsítvány" effective November 15, 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes after Google Chrome, Apple, and Mozilla [decided](https://thehackernews.com/2024/06/google-to-block-entrust-certificates-in.html) to no longer trust root CA certificates signed by [Entrust](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/LhTIUMFGHNw/m/uKzergzqAAAJ) as of November 2024. Entrust has since sold off its certificate business to Sectigo.

Earlier this March, Google also [revealed](https://security.googleblog.com/2025/03/new-security-requirements-adopted-by.html) that the CA/Browser Forum adopted Multi-Perspective Issuance Corroboration (MPIC) and Linting as required practices in the [Baseline Requirements](https://cabforum.org/working-groups/server/baseline-requirements/requirements/) (BRs) to enhance domain control validation and flag insecure practices in X.509 certificates.

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

[Apple](https://thehackernews.com/search/label/Apple)[browser security](https://thehackernews.com/search/label/browser%20security)[Certificate Authority](https://thehackernews.com/search/label/Certificate%20Authority)[Certificate Management](https://thehackernews.com/search/label/Certificate%20Management)[Compliance](https://thehackernews.com/search/label/Compliance)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DevOps](https://thehackernews.com/search/label/DevOps)[Digital Identity](https://thehackernews.com/search/label/Digital%20Identity)[Google Chrome](https://thehackernews.com/search/label/Google%20Chrome)[Mozilla](https://thehackernews.com/search/label/Mozilla)[network security](https://thehackernews.com/search/label/network%20security)[web security](https://thehackernews.com/search/label/web%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert C...
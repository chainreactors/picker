---
title: GitLab Patches Critical SAML Authentication Bypass Flaw in CE and EE Editions
url: https://thehackernews.com/2024/09/gitlab-patches-critical-saml.html
source: The Hacker News
date: 2024-09-20
fetch_date: 2025-10-06T18:31:20.755797
---

# GitLab Patches Critical SAML Authentication Bypass Flaw in CE and EE Editions

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

# [GitLab Patches Critical SAML Authentication Bypass Flaw in CE and EE Editions](https://thehackernews.com/2024/09/gitlab-patches-critical-saml.html)

**Sep 19, 2024**Ravie LakshmananEnterprise Security / DevOps

[![Authentication Bypass](data:image/png;base64... "Authentication Bypass")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiH6m5pM1NPMMHNVkcJKEqLCHOEnt-BVymJmR1nFbrIxNSgOC-Q4e-GBp-pTXrJdhFThJjfar295vwO-BiPcXbHUac81BIMedhlsNNyUUn3Tvu4CugG0X-W7XUtD5s_vXaBgv0dcgj1oKMy2pp1drjCkLrX1HbWx5HyoKcrZeyr_e3_NMhiQmjpKxroxVDf/s790-rw-e365/git.png)

GitLab has [released](https://about.gitlab.com/releases/2024/09/17/patch-release-gitlab-17-3-3-released/) patches to address a critical flaw impacting Community Edition (CE) and Enterprise Edition (EE) that could result in an authentication bypass.

The vulnerability is rooted in the ruby-saml library (CVE-2024-45409, CVSS score: 10.0), which could allow an attacker to log in as an arbitrary user within the vulnerable system. It was addressed by the maintainers last week.

The problem as a result of the library not properly verifying the signature of the SAML Response. SAML, short for Security Assertion Markup Language, is a protocol that enables single sign-on (SSO) and exchange of authentication and authorization data across multiple apps and websites.

"An unauthenticated attacker with access to any signed SAML document (by the IdP) can thus forge a SAML Response/Assertion with arbitrary contents, according to a [security advisory](https://github.com/SAML-Toolkits/ruby-saml/security/advisories/GHSA-jw9c-mfg7-9rx2). "This would allow the attacker to log in as arbitrary user within the vulnerable system."

It's worth noting the flaw also impacts omniauth-saml, which [shipped](https://github.com/omniauth/omniauth-saml/security/advisories/GHSA-cvp8-5r8g-fhvq) an update of its own (version 2.2.1) to upgrade ruby-saml to version 1.17.

The latest patch from GitLab is designed to update the dependencies omniauth-saml to version 2.2.1 and ruby-saml to 1.17.0. This includes versions 17.3.3, 17.2.7, 17.1.8, 17.0.8, and 16.11.10.

As mitigations, GitLab is urging users of self-managed installations to enable two-factor authentication (2FA) for all accounts and disallow the [SAML two-factor bypass](https://docs.gitlab.com/ee/integration/saml.html#bypass-two-factor-authentication) option.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

GitLab makes no mention of the flaw being exploited in the wild, but it has provided indicators of attempted or successful exploitation, suggesting that threat actors may be actively trying to capitalize on the shortcomings to gain access to susceptible GitLab instances.

"Successful exploitation attempts will trigger SAML related log events," it said. "A successful exploitation attempt will log whatever extern\_id value is set by the attacker attempting exploitation."

"Unsuccessful exploitation attempts may generate a ValidationError from the RubySaml library. This could be for a variety of reasons related to the complexity of crafting a working exploit."

The development comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://www.cisa.gov/news-events/alerts/2024/09/18/cisa-adds-five-known-exploited-vulnerabilities-catalog) five security flaws to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, including a recently disclosed critical bug impacting Apache HugeGraph-Server ([CVE-2024-27348](https://thehackernews.com/2024/07/critical-apache-hugegraph-vulnerability.html), CVSS score: 9.8), based on evidence of active exploitation.

Federal Civilian Executive Branch (FCEB) agencies have been recommended to remediate the identified vulnerabilities by October 9, 2024, to protect their networks against active threats.

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

[Authentication](https://thehackernews.com/search/label/Authentication)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[DevOps](https://thehackernews.com/search/label/DevOps)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Identity Management](https://thehackernews.com/search/label/Identity%20Management)[Open Source](https://thehackernews.com/search/label/Open%20Source)[software security](https://thehackernews.com/search/label/software%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to...
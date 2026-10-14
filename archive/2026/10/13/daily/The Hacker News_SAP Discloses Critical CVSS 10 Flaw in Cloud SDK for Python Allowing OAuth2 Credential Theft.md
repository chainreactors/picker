---
title: SAP Discloses Critical CVSS 10 Flaw in Cloud SDK for Python Allowing OAuth2 Credential Theft
url: https://thehackernews.com/2026/10/sap-discloses-critical-cvss-10-flaw-in.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:24.417131
---

# SAP Discloses Critical CVSS 10 Flaw in Cloud SDK for Python Allowing OAuth2 Credential Theft

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [SAP Discloses Critical CVSS 10 Flaw in Cloud SDK for Python Allowing OAuth2 Credential Theft](https://thehackernews.com/2026/10/sap-discloses-critical-cvss-10-flaw-in.html)

**Swati Khandelwal**Oct 13, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKBZR5elkBVKRcFO6lyde7XYDVO73IBxDvnx9-UkLst3GhVFuK8Yz3QBVIIEJABDjZuJMn8tyf7RLLPIRV8J8qe-OUULjnQRaQNyWricSsOjlKJoyYu8WOvs5PxBWQpzuiq8hlDlOY7zY-qIYDgQ6NFuifS5GbHbnLBET0OTfmsMC8797Mo5un9_ECyg8/s1700-nu-rw-lo-l85-e365/sap-hacker.jpg)

A flaw in SAP's [Cloud SDK for Python](https://github.com/SAP/cloud-sdk-python) can send an application's OAuth2 client credentials to a server an attacker controls, SAP said in a [security advisory](https://github.com/SAP/cloud-sdk-python/security/advisories/GHSA-4mv3-jxxm-9cx2) on October 13. The flaw affects multi-tenant applications on SAP Business Technology Platform (BTP) that use the SDK, SAP's official Python client for BTP services. An attacker must be able to control the tenant subdomain, the name such an application passes to the SDK to say which tenant a request is for.

The flaw is tracked as CVE-2026-89111 and carries SAP's CVSS score of 10.0 out of 10. The advisory names [version 0.45.2](https://github.com/SAP/cloud-sdk-python/releases/tag/v0.45.2), released on August 21, as the fix.

The SDK handles authentication for those services with the application's client credentials, a client ID and a client secret. Version 0.45.2 added a check that rejects any tenant subdomain that is not a simple name.

Six later releases do not apply that check in every case, The Hacker News found. Versions 0.53.0 through 0.55.0, published between September 10 and September 18, skip it when an application calls the SDK's Destination service module.

Version 0.53.0 moved that module onto new shared code for requesting tokens, and that code did not include the check. Version 0.55.1 added it there on September 18.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

Passing a tenant subdomain that contains URL delimiters "now raises ValueError immediately instead of silently routing credentials to an attacker-controlled endpoint," the 0.55.1 [release notes](https://github.com/SAP/cloud-sdk-python/releases/tag/v0.55.1) say.

The Hacker News ran SAP's own tests for the check on October 13, against the source code of every release from 0.45.1 to 0.58.4 and of the three 0.36 releases. The six releases failed 9 of the 11 tests SAP added with version 0.55.1. That version and the 11 releases after it passed all 11.

As of October 13, the advisory lists no version above 0.45.2 as affected. Neither it nor the release notes say whether the six releases fall under CVE-2026-89111.

Two releases on the older 0.36 line also lack the check. Versions 0.36.1 and [0.36.2](https://github.com/SAP/cloud-sdk-python/releases/tag/v0.36.2) were published on September 4 and September 10, after the August fix, and failed the tests SAP wrote for it. Both fall inside the advisory's range of versions below 0.45.2.

| Releases | Tenant subdomain check | Basis |
| --- | --- | --- |
| Below 0.45.2, including 0.36.1 and 0.36.2 | Missing | SAP advisory. The Hacker News test of 0.36.0, 0.36.1, 0.36.2 and 0.45.1. |
| 0.45.2 to 0.52.2 | Present | The Hacker News test of all 18 releases. |
| 0.53.0 to 0.55.0 | Missing for Destination calls. Also missing for Document Management Service calls in 0.55.0. | SAP's 0.55.1 release notes. The Hacker News test of all 6 releases. |
| 0.55.1 to 0.58.4 | Present | The Hacker News test of all 12 releases. |

### What to Do

Versions 0.45.2 through 0.52.2 and 0.55.1 through 0.58.4 contain the check. Version 0.58.4 was the [newest release](https://pypi.org/project/sap-cloud-sdk/0.58.4/) on PyPI, the Python package index, on October 13.

Upgrading within the 0.36 line does not add the check. None of its three releases contains it.

Applications that cannot upgrade yet can compare each tenant subdomain with a list of their registered tenants before passing it to the SDK, SAP says in the advisory.

The flaw matters only where an application passes a tenant subdomain to the SDK. The August fix covered three modules: Agent Gateway, Destination and Document Management Service.

The advisory does not say whether applications that ran a release without the check should replace their client credentials.

### How the Flaw Works

When an application passes a tenant subdomain, the SDK requests an access token for that tenant. To do that, it takes the token URL from the application's configuration and replaces part of it with the tenant subdomain.

Releases without the check used whatever value they were given. The SDK then sent the application's client ID and client secret to the resulting URL to request the token.

An attacker who controls the tenant subdomain can point that request at their own server, according to SAP.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The check accepts only a single name made of letters, digits and hyphens, up to 63 characters long. Any other value stops the request with an error.

SAP labels the flaw server-side request forgery (SSRF), a weakness in which a server can be made to send a request to a destination it did not intend.

What an attacker could do with the credentials depends on what the application's client is allowed to do. The advisory does not say.

### Fixed in August, Disclosed in October

The unchecked code was in the SDK from its first release on PyPI, on March 16.

The August release notes list the fix under "Bug Fixes" and do not mention security. "Previously, invalid values were silently used to construct a malformed URL," the notes say.

The advisory followed 53 days later. It credits a GitHub user named [SunandM](https://github.com/SunandM) with reporting the flaw and does not report any attacks....
---
title: SkyW4lker Exposed: A Growing Microsoft 365 Phishing Threat to American Enterprises
url: https://any.run/cybersecurity-blog/skyw4lker-phishing-kit-analysis/
source: Over Security
date: 2026-10-27
fetch_date: 2026-10-28T07:49:27.080223
---

# SkyW4lker Exposed: A Growing Microsoft 365 Phishing Threat to American Enterprises

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [SOC & MSSP Strategy](https://any.run/cybersecurity-blog/category/soc-mssp-strategy/)
  + [Customer Success Story](https://any.run/cybersecurity-blog/category/customer-success/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![SkyW4lker Exposed: A Growing Microsoft 365 Phishing Threat to American Enterprises](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/Skyw4lker-scaled.png)

[Threat Landscape](https://any.run/cybersecurity-blog/category/threat-landscape/)

# SkyW4lker Exposed: A Growing Microsoft 365 Phishing Threat to American Enterprises

October 27, 2026

[Add comment](#comments-24071)
3306 views
12 min read

[Home](https://any.run/cybersecurity-blog/)[Threat Landscape](https://any.run/cybersecurity-blog/category/threat-landscape/)

SkyW4lker Exposed: A Growing Microsoft 365 Phishing Threat to American Enterprises

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/Skyw4lker-1024x497.png)

  #### SkyW4lker Exposed: A Growing Microsoft 365 Phishing Threat to American Enterprises

  3306
  0](https://any.run/cybersecurity-blog/skyw4lker-phishing-kit-analysis/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/Early_SOC_Response-1024x497.png)

  #### Cyber Threat Context for Early Response: Enriching SOC Telemetry with Real-Time Intel from 16K Organizations

  10466
  0](https://any.run/cybersecurity-blog/cyber-threat-context-for-early-soc-triage-response/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/10/Related_analyses_new_cover-1024x497.png)

  #### Your New MTTR Shortcut — Introducing Related Threat Context: Cut Time-to-Triage with Actionable IOC Context

  12679
  0](https://any.run/cybersecurity-blog/related-threat-context-release/)

[Home](https://any.run/cybersecurity-blog/)[Threat Landscape](https://any.run/cybersecurity-blog/category/threat-landscape/)

SkyW4lker Exposed: A Growing Microsoft 365 Phishing Threat to American Enterprises

**SkyW4lker** (SkyW4lker x365 Sentinel) is an active device-code phishing kit targeting Microsoft 365 users in the United States, Europe, and other regions. By abusing Microsoft’s legitimate authentication process, the kit can give attackers access to corporate accounts without stealing passwords or bypassing MFA. This puts business emails, sensitive documents, and other Microsoft 365 resources at risk of unauthorized access.

The [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=skyw4lker-phishing-kit-analysis&utm_term=271026&utm_content=linktolanding) team identified **618 sandbox analyses** related to SkyW4lker between June and October 21, 2026, with **46% of submissions coming from the United States**. Activity increased from 20 analyses in June to 200 in September, highlighting the growing exposure of organizations relying on Microsoft 365.

## Key Takeaways

* SkyW4lker is distributed through phishing emails with a password-protected malicious attachment; the password is provided in the email body. After a chain of decoy pages, the victim reaches a page that asks for a Microsoft device code.
* The kit consists of a PHP backend and obfuscated JavaScript. Its main features are IP-based geolocation of visitors and periodic polling of the backend to check whether the victim has completed authentication.
* ANY.RUN’s powerful new capability, [Related Threat Context](https://any.run/cybersecurity-blog/related-threat-context-release/), helped analysts accelerate the SkyW4lker investigation by instantly surfacing connections to previous sandbox analyses. This reduced manual correlation work, enabled faster expansion of the campaign cluster, and ultimately helped uncover the phishing kit’s administration panel.
* As a result, 618 analyses were identified over the past six months (as of October 21, 2026), with monthly submissions growing from 20 in June to 200 in September. They were submitted mainly by organizations in the technology, manufacturing, and government sectors, most often from the United States, India, Canada, and the United Kingdom.
* SkyW4lker shares its JavaScript modules, landing-URL format, and part of its hosting infrastructure with Gabagool, a credential phishing kit active since April 2026. We assess with high confidence that both kits were built by the same developer.
* SkyW4lker exploits routine business workflows, using contracts, invoices, and service proposals as phishing lures. By directing employees through familiar platforms and legitimate Microsoft authentication pages, attackers make malicious requests harder to distinguish from normal business activity.

## SkyW4lker Threat Overview

| Threat Type | Phishing Kit |
| --- | --- |
|  |  |
| --- | --- |
| Objective | Microsoft 365 / OAuth credentials |
| Capabilities | JavaScript obfuscation (obfuscator.io), Device-Code phishing, Geolocation detection, IP-address detection, CAPTCHA verification |
| Delivery | Email attachments (.pdf, .docx, .xls/xlsx and others), redirection links and lure pages (including Google Maps, Google Images, Miro, Zoom and others) |
| Motivation | Possible financial |
| Operator / brand | SkyW4lker (SkyW4lker x365 Sentinel) |
| Known links | URL patterns: /session\_public.php?action= /endpoints/confirm\_visit.php /js/url\_helper.js /js/endpoint.js /js/client\_geo.js |
| Activity window | 2026-06 – now |

## SkyW4lker Activity Across US Organizations

The United States accounts for 47% of SkyW4lker-related sandbox submissions, more than twice the share of any other country. With the campaign exploiting legitimate Microsoft authentication processes and routine business communications, these findings raise concerns for US enterprises about how effectively existing security controls can identify suspici...
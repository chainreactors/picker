---
title: A Single Canadian Tax Lure Spread into a 46-Country, US-First RMM Campaign
url: https://any.run/cybersecurity-blog/us-campaign-malware-analysis/
source: Over Security
date: 2026-08-28
fetch_date: 2026-08-29T08:32:50.672349
---

# A Single Canadian Tax Lure Spread into a 46-Country, US-First RMM Campaign

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
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
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![A Single Canadian Tax Lure Spread into a 46-Country, US-First RMM Campaign](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Malware-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# A Single Canadian Tax Lure Spread into a 46-Country, US-First RMM Campaign

August 25, 2026

[Add comment](#comments-22827)
8785 views
13 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

A Single Canadian Tax Lure Spread into a 46-Country, US-First RMM Campaign

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Cyber-Threats-to-US-Finance-1024x497.png)

  #### US Finance Under Phishing Pressure: What the SOC Data Reveals?

  3343
  0](https://any.run/cybersecurity-blog/phishing-us-finance/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Malware-1024x497.png)

  #### A Single Canadian Tax Lure Spread into a 46-Country, US-First RMM Campaign

  8785
  0](https://any.run/cybersecurity-blog/us-campaign-malware-analysis/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/dprk_workers-1024x497.png)

  #### North Korean IT Workers Scheme: Detection IOCs and Tactics for Government and Corporate SOCs

  11496
  0](https://any.run/cybersecurity-blog/how-to-protect-organization-against-north-korean-it-workers/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

A Single Canadian Tax Lure Spread into a 46-Country, US-First RMM Campaign

As [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=us-campaign-malware-analysi&utm_term=250826&utm_content=linktolanding) analysis shows, a campaign that initially appears to target Canadians with fake Canada Revenue Agency (CRA) T4 tax documents is actually part of a much broader remote-access campaign spanning 46 countries, with 45% of observed activity associated with the [United States.](https://any.run/cybersecurity-blog/usa-top-30-threats-2026/)

The attackers impersonate trusted [organizations](https://any.run/cybersecurity-blog/soc-business-success-cases-anyrun/) and document types to trick victims into installing legitimate remote management software, giving them remote access to compromised systems.

## Part I. Campaign Scope, Impact, and Defense

### Threat Overview

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Vercel_Campaign_in-Brief-1024x772.png)

Campaign overview based on ANY.RUN research

This phishing operation’s final goal is the remote control of the victim’s machine. A reusable fake-document kit delivers interchangeable, legitimate [RMM](https://any.run/cybersecurity-blog/rmm-blind-spot-for-cisos/) software installer, which the attacker then abuses for hands-on access.

Because the payload is signed commercial software, ordinary signature-based antivirus cannot flag it. Its activity resembles ordinary remote administration.

[View this malware analysis in TI Reports](https://intelligence.any.run/reports/08-24-2026-cra-t4-rmm/?utm_source=anyrunblog&utm_medium=article&utm_campaign=us-campaign-malware-analysi&utm_term=250826&utm_content=linktotireports)

The campaign uses multiple lures, including the US Social Security Administration, Adobe PDF documents, invoices, VAT notices, and shipping communications, allowing the same attack model to target victims across different regions and business contexts.

**Campaign Profile**

| Attribute | Assessment |
| --- | --- |
|  |  |
| --- | --- |
| Threat type | Phishing delivering RMM-as-RAT for living-off-the-land remote access |
| Family | Fake-document-to-RMM kit; the CRA/T4 Word lure is one arm of a broader fmtt font-linked family |
| Severity | High — hands-on-keyboard remote access |
| Sophistication | Capable — kit-based delivery, LOLBin RMM abuse, password-protected archive, Telegram-based victim filtering; built entirely on legitimate signed tooling |
| Payload | Signed RMM installers abused as remote-access trojans; productsare interchangeable and include GoTo Resolve, LogMeIn Rescue, ITarian in this arm; ScreenConnect, ConnectWise in sibling arms |
| Impersonated brands | Canada Revenue Agency / 2025 T4 Form, SSA, VAT/ATO, DocuSign, Adobe PDF, overdue invoices, shipping documents |
| Attribution | Campaign-level based on shareddelivery-kit handwriting; no named threat actor. Whether this is one operator or a shared phishing-as-a-service kit remains unknown |
| Activity window | January 2026 to present; steady 17–33 kit cases per month |

### Statistics and Victimology

Two scopes are important here: the CRA/T4 Word arm, with 137 observed cases, and the broader fake-document family, covering 425 kit URLs across 240 hosts and 601 cases with geographic and industry context.

Activity grew from a single observed case in January 2026 to a steady 17–33 cases per month. Because the final payload is legitimate signed RMM software, cases are tracked through shared kit assets rather than malware-family verdicts, which would significantly undercount the campaign.

![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Kit-Cases-Per-Month.png)

Kit cases per month graph by ANY.RUN

Geographically, the broader family is US-first, while the CRA/T4 arm is Canada-first. North America accounts for 61% of family cases, but activity ...
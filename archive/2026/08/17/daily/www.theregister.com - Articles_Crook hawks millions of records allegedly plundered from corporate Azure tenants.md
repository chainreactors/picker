---
title: Crook hawks millions of records allegedly plundered from corporate Azure tenants
url: https://www.theregister.com/security/2026/08/17/crook-hawks-millions-of-records-allegedly-plundered-from-corporate-azure-tenants/5288305
source: www.theregister.com - Articles
date: 2026-08-17
fetch_date: 2026-08-18T02:54:05.157378
---

# Crook hawks millions of records allegedly plundered from corporate Azure tenants

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

SECURITY

# Crook hawks millions of records allegedly plundered from corporate Azure tenants

McDonald's, Vodafone, TCS, Kyndryl, and others named as researchers point to compromised credentials

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
mon 17 Aug 2026 // 12:43 UTC

A cybercrook claims to have siphoned millions of employee records from the Microsoft Azure environments of major companies including McDonald's, Vodafone, Kyndryl, and Tata Consultancy Services.

The alleged haul spans nine organizations and is being advertised for sale by a threat actor using the name "TheHatman," according to [research published by Hudson Rock](https://www.infostealers.com/article/massive-azure-exfiltration-campaign-exposes-millions-of-enterprise-records-via-compromised-credentials-mcdonalds-vodafone-kyndryl-others/).

McDonald's accounts for the largest alleged dataset on TheHatman's shopping list, with 1.7 million records purportedly up for grabs. Another 800,000 records supposedly come from Tata Consultancy Services, 425,000 from Vodafone, and 250,000 from HCL Technologies, with IHG Hotels & Resorts, Kyndryl, Gap, Hexaware Technologies, and Wyndham Hotels & Resorts rounding out the haul.

REG AD

Hudson Rock assessed the data as "highly likely authentic," citing corporate email addresses and structures consistent with exports from Microsoft Azure directory services.

REG AD

The records allegedly contain considerably more than names and work email addresses. Samples reviewed by the security shop reportedly include phone numbers, physical addresses, employee IDs, job titles, departments, office locations, reporting structures, group memberships, and service account details.

Some records also reportedly identify accounts with Global Administrator privileges, potentially handing attackers a useful map of whom to target next. Even if the passwords aren't included, knowing who holds the keys to the kingdom makes for a handy phishing shortlist.

How TheHatman allegedly obtained the information remains unclear. The attacker claims to have used compromised credentials, but Hudson Rock could not independently establish the initial access vector. It floated several possibilities, including credentials or session cookies stolen by infostealer malware, phishing, weak or absent multifactor authentication, and overly permissive third-party applications.

## MORE CONTEXT

* [### Black Hat and DEF CON are AI conferences now, too](/security/2026/08/17/black-hat-and-def-con-are-ai-conferences-now-too/5288076)
* [### Chinese AI company Zhipu claims its new model is a better bug-finder than Anthropic, OpenAI](/security/2026/08/17/chinese-ai-company-zhipu-claims-its-new-model-is-a-better-bug-finder-than-anthropic-openai/5288203)
* [### Stopping a cyberattack while walking your dog - defensive AI security CEO says it's not ruff to do](/security/2026/08/16/stopping-a-cyberattack-while-walking-your-dog-defensive-ai-security-ceo-says-its-not-ruff-to-do/5288126)
* [### ChainDrop worm crawls into npm supply chain, evades standard defenses](/security/2026/08/15/chaindrop-worm-crawls-into-npm-supply-chain-evades-standard-defenses/5287958)

Hudson Rock said its infostealer database contained compromised Microsoft cloud credentials associated with most of the named companies, although it could not link those credentials to TheHatman's alleged access.

"Judging by the massive size of the organizations impacted, it appears highly likely that this campaign originates from targeted exploitation of Infostealer infections rather than a systemic zero-day vulnerability in Azure," said Hudson Rock. "If this were a widespread vulnerability, we would likely see a much broader spectrum of organizations impacted, including smaller businesses, rather than just these massive Fortune 500-level enterprises."

The Register contacted all the organizations named by Hudson Rock to ask whether they were breached, whether the advertised data is authentic, and how any unauthorized access occurred. We've also asked Microsoft whether it is aware of a wider campaign targeting Azure or Entra customers.

Tata Services sent The Register the statement it made to [India's stock exchange](https://www.bseindia.com/xml-data/corpfiling/AttachLive/ac9edbea-ea43-4...
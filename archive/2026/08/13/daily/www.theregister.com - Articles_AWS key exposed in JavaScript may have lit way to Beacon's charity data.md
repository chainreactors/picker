---
title: AWS key exposed in JavaScript may have lit way to Beacon's charity data
url: https://www.theregister.com/security/2026/08/13/aws-key-exposed-in-javascript-may-have-lit-way-to-beacons-charity-data/5287303
source: www.theregister.com - Articles
date: 2026-08-13
fetch_date: 2026-08-14T04:01:08.495904
---

# AWS key exposed in JavaScript may have lit way to Beacon's charity data

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

Security

# AWS key exposed in JavaScript may have lit way to Beacon's charity data

CRM provider confirms customer database was copied and probably downloaded in readable form

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
thu 13 Aug 2026 // 12:34 UTC

Beacon, a CRM provider for charities and nonprofits, says an AWS access key "potentially exposed in public JavaScript build artifacts" is the leading suspect in its July breach.

The revelation came in the company's first update on the attack in more than a week. If the access key was exposed in public build artifacts, it raises questions about why Beacon's development pipeline and code review controls failed to catch it.

Beacon used stronger wording about the potential data loss, confirming that a copy of the database was made and assessing that it was probably downloaded in readable form.

REG AD

"This update confirms… that a copy of the database which holds all Beacon customer data, including attachment files, was made and likely downloaded in a readable format by the threat actor," [wrote](https://www.beaconcrm.org/incident) CTO David Simpson.

REG AD

"Analysis of the AWS Cost & Usage reports across May-July 2026 has been conducted. This data showed a significant increase in data transfer on 27-28 July 2026. This timing correlates with the malicious activity, which supports an assessment that substantial downloads occurred."

Beacon's logs cannot reveal which specific records left its systems, although the company has confirmed that a copy of the database containing all customer data and attachments was made.

In an FAQ accompanying the update, Beacon advises customers to assess the likely exposure by reviewing what they stored in their CRM instance.

Many of the charities that have confirmed they are affected have said the data mainly pertains to personal information and details about donations.

Simpson said Beacon's AWS data was encrypted at rest, but the compromised access key may have allowed the attacker to retrieve it in readable form.

The malicious activity began in the early hours of July 27, according to Beacon's root cause analysis, matching its initial estimate of the incident timeline. The company has more than 1,500 customers, although it has not established how many had data taken.

The malicious activity lasted one hour and 27 minutes, Beacon said, and the attacker established no persistence mechanisms in [AWS](https://www.theregister.com/devops/2026/06/23/aws-hypes-continuous-agentic-devops-puts-kiro-in-your-pocket/5260186).

Simpson warned customers that "there are things we may never be able to find out about this incident," and that other details won't be shared to protect Beacon's security position.

REG AD

He promised to provide customers with a summary when the investigation concludes in a few weeks, but warned that "the level of detail contained in this next and final update may not be any more than" Beacon published on Wednesday.

"I recognise this is frustrating, but unfortunately it is the reality of [complex incidents](https://www.theregister.com/special-features/2025/03/10/how-not-to-f-up-your-security-incident-response/773217) like this. With this in mind, we would recommend making your own risk assessments now regarding onward notification to impacted data subjects using your knowledge of the data you process and store with Beacon."

## MORE CONTEXT

* [### UK charities count the cost of Beacon CRM cyberattack](/security/2026/08/05/uk-charities-count-the-cost-of-beacon-crm-cyberattack/5283305)
* [### Exposed: Woeful security at UK criminal records office that led to sensitive data leak](/security/2026/08/12/exposed-woeful-security-at-uk-criminal-records-office-that-led-to-sensitive-data-leak/5286736)
* [### Scot NHS trust probes access to medical records of 9-year-old girl after man arrested on suspicion of murder](/security/2026/08/07/nhs-tayside-investigates-breach-concerning-data-of-dead-girl/5284815)
* [### Police National Legal Database confirms data theft after dark web leak](/cyber-crime/2026/08/03/police-national-legal-database-confirms-data-theft-after-dark-web-leak/5282332)

Since Beacon [disclosed the attack on August 4](https://www.theregister.com/security/...
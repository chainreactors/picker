---
title: Framework loses customer data in Metabase zero-day attack
url: https://www.theregister.com/personal-tech/2026/08/10/framework-loses-customer-data-in-metabase-zero-day-attack/5285302
source: www.theregister.com - Articles
date: 2026-08-10
fetch_date: 2026-08-11T03:31:56.853396
---

# Framework loses customer data in Metabase zero-day attack

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

PERSONAL TECH

# Framework loses customer data in Metabase zero-day attack

Repairable hardware is little comfort when personal details escape

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
mon 10 Aug 2026 // 12:21 UTC

Modular laptop maker Framework has warned customers that an attacker exploited a zero-day at analytics provider Metabase to access names, email addresses, phone numbers, physical addresses, and login IP addresses, according to an email [shared on Reddit](https://www.reddit.com/r/framework/comments/1vhic7k/framework_data_breach/).

For business customers, the exposed information may also include company names, phone numbers, VAT or Employer Identification Numbers (EINs), and billing email addresses. Framework said order and payment details were not affected.

"We are deeply sorry for this breach of information, and are reviewing and improving our methodology for data storage in external database vendors," Framework said, adding that it's notifying regulators where required, though it noted that names, email addresses, phone numbers, and physical addresses don't cross the mandatory reporting threshold in many regions. Customers are getting the heads-up regardless.

REG AD

Framework didn't immediately reply to The Register's questions, but told[TechCrunch](https://techcrunch.com/2026/08/07/computer-maker-framework-notifies-all-customers-of-a-data-breach/) that the breach had affected "all customers."

REG AD

The intrusion began with a zero-day vulnerability in Metabase, the business intelligence platform Framework uses to analyze its data.

![The Framework Laptop 13 Pro](https://image.theregister.com/5225977.webp?imageId=5225977&width=960&height=548&format=jpg)

Framework's latest laptop, the 13 Pro

Pic courtesy Framework

In its [own blog post,](https://www.metabase.com/blog/security-update) Metabase said an attacker targeted its cloud service using a previously unknown vulnerability affecting versions 1.58 and later. The company blocked the endpoints used in the attack, patched the bug, and deployed the fix across its cloud service.

Framework's account provides a timeline for the break-in. Metabase discovered the attack on August 3 and notified Framework at 9am Pacific Time on August 6, telling the laptop maker that its instance had been vulnerable and that the attacker had successfully gained access to it.

Framework said it then rotated credentials for every database connected to its Metabase instance and found no changes to admin access or evidence that systems outside Metabase had been accessed. The company has also brought in a third-party forensics firm to investigate, and cautioned that its findings so far are preliminary.

According to Metabase, exploitation can allow an attacker to inject arbitrary SQL against the application's database and potentially gain administrator access. From there, they could alter configuration settings, steal credentials for databases connected to Metabase, query data those connections can access, and export the results.

## MORE CONTEXT

* [### Right to repair champ Framework punts modular 13in laptop with Core Ultra Series 3](/on-prem/2026/04/22/framework-punts-modular-13in-laptop-with-core-ultra-series-3/5225673)
* [### A lot of product makers snub Right to Repair laws](/offbeat/2025/07/01/despite-right-to-repair-laws-some-manufacturers-fall-short/101372)
* [### Tariff-ied Framework pulls laptops, Keyboardio warns of keystroke sticker shock](/on-prem/2025/04/08/framework-pauses-sales-on-laptops-it-will-make-a-loss-on/1050587)
* [### Framework Desktop wows iFixit – even with the soldered RAM](/on-prem/2025/02/27/framework-desktop-wows-ifixit-even-with-the-soldered-ram/786928)

Metabase told anyone running their own instance to patch immediately. If the vulnerable password-reset endpoint was exposed to the internet, admins have more work ahead of them: killing active sessions, checking for rogue API keys or admin accounts, rotating database credentials, and digging through logs for anything suspicious.

Framework is reviewing how customer information is made available through external analytics services, but hasn't yet said what changes that review might produce.

The breach lands during an already bumpy spell for Framework and i...
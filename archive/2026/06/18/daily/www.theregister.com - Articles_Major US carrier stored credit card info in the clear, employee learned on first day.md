---
title: Major US carrier stored credit card info in the clear, employee learned on first day
url: https://www.theregister.com/security/2026/06/18/major-us-carrier-stored-credit-card-info-in-the-clear-employee-learned-on-first-day/5257932
source: www.theregister.com - Articles
date: 2026-06-18
fetch_date: 2026-06-19T07:09:18.350819
---

# Major US carrier stored credit card info in the clear, employee learned on first day

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
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
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
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

SECURITY

# Major US carrier stored credit card info in the clear, employee learned on first day

It happened at a major US telco in the early 2000s

Avram Piltch
[Avram
Piltch](https://www.theregister.com/author/avram-piltch)
US editor

Published
thu 18 Jun 2026 // 08:00 UTC

PWNED Welcome back to PWNED, the weekly column where we register some of the worst tech security mistakes our readers have ever seen. Our goal: to help you not do the same.

Have a story about someone leaving a gaping hole in their network? Share it with us at pwned@sitpub.com. Anonymity is available upon request.

This week's tale of code carelessness comes courtesy of a database administrator we'll Regomize as Joker. Back in the first decade of the 21st century, she went for a job interview at one of the USA's leading national cellular carriers.

REG AD

What she saw would make you want to swap your SIM.

REG AD

After a successful meeting with a hiring manager, Joker was hired on the spot.

Within hours the company granted her sudo-level access to a database server, then instructed her to "take a look" at some of the databases.

Joker soon realized the carrier's security was no laughing matter as she found herself accessing the main production server for the company's data services division, overseeing all services for the mobile web. This story took place in a time before the iPhone, so she was looking at nasty little versions of websites comressed for viewing on their BlackBerries or flip phones.

After peeking around some more, Joker discovered that she had access to the master customer table. It contained nightmarish quantities of personally identifiable information: names, addresses, Social Security numbers, billing info, and even full 16-digit credit card numbers. All of this info was stored in the clear, with no encryption or obfuscation. The CVVs were missing from some credit card info, but many were present.

"There was a central billing system upstream on Amdocs servers, but this database also had billing details so they didn't have to reach back upstream to Amdocs if users asked to provision new services," Joker said.

After Joker informed management about the mess, they deleted the offending info and forced the developers to go upstream again for billing information, just like they should have been doing in the first place.

Joker, like any reasonable DBA, assumed access to this information would be tightly controlled - not made available to new staff with full access rights on their first day.

## MORE CONTEXT

* [### Every employee’s password was stored in a single Excel file](/security/2026/06/11/every-employees-password-was-stored-in-a-single-excel-file/5253784)
* [### All the passwords were stored in Active Directory description fields](/security/2026/06/04/all-the-passwords-were-stored-in-active-directory-description-fields/5250820)
* [### Company CEO flooded file share with smut, called for help after he deleted it](/security/2026/05/28/company-ceo-flooded-file-share-with-smut-called-for-help-after-he-deleted-it/5247502)
* [### Zombie user account let hackers control the city’s water](/security/2026/05/21/zombie-user-account-let-hackers-control-the-citys-water/5243724)

She also assumed her new employer would tokenize key pieces of data because that technique means certain info – say credit card and Social Security numbers – would not be visible in the same table as a customer's name and address. Instead, there would be tokens linking back to the actual numbers stored in a secure token vault. This is common in payment systems.

REG AD

If Joker were less ethical or someone else had gained admin access, they could have exfiltrated large amounts of sensitive data. Permissions should start from a zero-trust assumption and provide only what someone needs to do their job.

Joker said that when she later moved on to work for a major online retailer, security was front and center, proving that some people did get it, even back in the George W. Bush era. ®

[data breach](/tag/data%20breach)
[pwned](/tag/pwned)
[pii](/tag/pii)
[security](/tag/security)
[telco](/tag/telco)

REG AD

[![](https://image.theregister.com/240961.jpg?imageId=240961&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Personal tech

## Users claimed they’d never seen a spell checker and panicked at the sight of red squiggles

Techie couldn’t help but be a little blunt when the support call came in – but has no regrets!](https://www.theregister.com/personal-tech/2026/06/19/users-claimed-theyd-never-seen-a-spell-checker-and-panicked-at-the-sight-of-red-squiggles/5257476)

[On-PREM

## 2,000 retired Google...
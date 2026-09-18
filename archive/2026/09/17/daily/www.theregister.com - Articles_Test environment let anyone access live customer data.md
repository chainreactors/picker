---
title: Test environment let anyone access live customer data
url: https://www.theregister.com/security/2026/09/17/test-environment-let-anyone-access-live-customer-data/5296977
source: www.theregister.com - Articles
date: 2026-09-17
fetch_date: 2026-09-18T06:53:43.510709
---

# Test environment let anyone access live customer data

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
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
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
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Science](/science)

REG AD

[security](/tag/security)

# Test environment let anyone access live customer data

[pwned](https://www.theregister.com/tag/Pwned/)

Even a temporary staging server needs to be locked down.

Avram Piltch
[Avram
Piltch](https://www.theregister.com/author/avram-piltch)
US EDITOR
US editor

Published
thu 17 Sep 2026 // 12:28 UTC

### READ MORE

* [#### Dental contractor set up secret account with access to 4,000 patient records then left the company

  7 days ago](/security/2026/09/10/dental-contractor-set-up-secret-account-with-access-to-4000-patient-records-then-left-the-company/5295361)
* [#### Terminated employee cost company hundreds of thousands of dollars because nobody revoked access

  14 days ago](/security/2026/09/03/terminated-employee-cost-company-hundreds-of-thousands-of-dollars-because-nobody-revoked-access/5292763)
* [#### AI girlfriend review site's secrets were exposed to the world for three weeks

  21 days ago](/security/2026/08/27/ai-girlfriend-review-sites-secrets-were-exposed-to-the-world-for-three-weeks/5293064)
* [#### AI agent suggested installing a malware package. Engineer almost took its advice

  28 days ago](/security/2026/08/20/ai-agent-suggested-installing-a-malware-package-engineer-almost-took-its-advice/5289849)
* [#### Passwords stored in public Google Doc then showed up in search results

  August 13, 2026](/security/2026/08/13/passwords-stored-in-public-google-doc-then-showed-up-in-search-results/5287028)

Welcome back to PWNED, the weekly column where we learn important life lessons about how we let cybercrims access our data through carelessness. Hopefully, others’ mistakes provide an example of what not to do.

Today’s tales of woe comes courtesy of Richard Schut, Managing Director & AI Software Researcher at [SmartRepl](https://smartrepl.com/), a company that offers business AI services such as AI receptionists and sales automation. In a past job, Schut was working for what he describes as a mid-size company during a security audit whose purpose was to identify any potential problems ahead of moving some local systems to the cloud.

Schut and his team discovered that there was a test environment that was accessible outside the network and connected to a database which had live customer information in it. This was a gaping hole that a miscreant could have used to grab valuable information from the business.

REG AD

“What made the situation particularly concerning was that the environment had originally been created for what the development team considered a short-term purpose,” he told The Register. “They needed somewhere to demonstrate the application and test the migration, so a staging instance was spun up quickly. It was never intended to become part of the company's permanent infrastructure.”

REG AD

Unfortunately, the test environment was still running months after it was initially set up. And because those who created it did not expect unauthorized people to access it, they didn’t use the same authentication and access control methods that they would in production.

## Tell us your story

Have a story about someone leaving a gaping hole in their network? Share it with us at
pwned@sitpub.com. Anonymity is available upon request.

The SQL file containing the database was appropriately named master\_test\_final.sql, just in case there was any question about what it contained.

“It was a classic example of how security problems don't always come from sophisticated attacks or exotic vulnerabilities,” Schut said. “Sometimes the biggest risk is simply something that was supposed to exist for a few hours, but was still sitting there six months later.”

After Schut and his colleagues discovered the security vulnerability, he immediately restricted access to the staging environment. Then he and his team started a review of other development and test environments in the company to make sure none of them was open to exploitation.

The takeaway here is as accessible as that SQL file: Don't get lax with security simply because an environment is made for testing. Even if the test server was live for only a day, that’s a day where it could be exploited.

“The incident completely changed how I look at staging environments. If an ...
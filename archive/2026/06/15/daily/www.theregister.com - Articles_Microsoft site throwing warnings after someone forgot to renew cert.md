---
title: Microsoft site throwing warnings after someone forgot to renew cert
url: https://www.theregister.com/security/2026/06/15/microsoft-site-throwing-warnings-after-someone-forgot-to-renew-cert/5255597
source: www.theregister.com - Articles
date: 2026-06-15
fetch_date: 2026-06-16T07:17:06.166265
---

# Microsoft site throwing warnings after someone forgot to renew cert

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

Security

# Microsoft site throwing warnings after someone forgot to renew cert

Connectivity checker trips browser alarms thanks to lapsed security paperwork

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
mon 15 Jun 2026 // 16:33 UTC

Microsoft appears to have dropped the ball with its certificate management after a domain used by sysadmins worldwide to test connectivity to Microsoft 365 started throwing untrusted connection warnings in browsers.

The [connectivity.office.com](http://connectivity.office.com) domain is used by IT pros to test their network's connectivity to Microsoft 365 and ensure their firewalls aren't blocking anything that could affect an organization's access to Microsoft servers.

An [SSL server report](https://www.ssllabs.com/ssltest/analyze.html?d=connectivity.office.com&s=13.107.6.202) retrieved on Monday showed that the certificate expired on June 14 after last being renewed on December 16, 2025.

REG AD

At the time of writing, 35 hours have passed since the certificate expired, and Microsoft has still not renewed it, despite many in the IT community making [their opinions on the matter](https://www.reddit.com/r/sysadmin/comments/1u63hb0/ms_forgot_to_renew_their_cert_for/) known.

REG AD

Certificate renewals are often automated in this day and age, but in organizations still relying on manual processes, those responsible for renewals would almost certainly have received multiple alerts warning of the impending expiration.

It suggests that something, or someone, involved in the certificate-renewal process at Microsoft has messed up.

The Register contacted Redmond for a response. The company's publicists acknowledged the request for comment but did not return one in time for publication.

## MORE CONTEXT

* [### New SSL/TLS certs to each live no longer than 47 days by 2029](/security/2025/04/14/ssl/tls-certificates-will-last-47-days-max-by-2029/463450)
* [### Microsoft Teams starts February with a good, old-fashioned TITSUP\*](/software/2020/02/03/microsoft-teams-starts-february-with-a-good-old-fashioned-titsup/1500974)
* [### Typhoon-like gang slinging TLS certificate 'signed' by the Los Angeles Police Department](/security/2025/06/24/typhoon-like-gang-slinging-tls-certificate-signed-by-lapd/1209911)
* [### DigiCert gives unlucky folks 24 hours to replace doomed certificates after code blunder](/security/2024/07/31/digicert-revokes-certificates-issued-in-error-by-software/541382)

The fallout could have been much worse. Browser warnings on a network diagnostic tool are irritating, but hardly catastrophic compared with the same thing happening to [login.microsoft.com](http://login.microsoft.com) or another critical service.

Teams users may remember the collaboration platform abruptly [deciding to take Monday off](https://www.theregister.com/software/2020/02/03/microsoft-teams-starts-february-with-a-good-old-fashioned-titsup/1500974) in 2020, after an authentication certificate expired, for example.

Whatever went wrong here, Microsoft will have to tighten its processes before [shorter certificate lifespans](https://www.theregister.com/security/2025/04/14/ssl/tls-certificates-will-last-47-days-max-by-2029/463450) arrive in the coming years.

As of March 26, new SSL/TLS certs will have a maximum lifespan of 200 days. This is set to decrease to 100 days by March 15, 2027, and then to 47 days two years later. ®

[microsoft](/tag/microsoft)
[certificate expiration](/tag/certificate%20expiration)
[microsoft 365](/tag/microsoft%20365)
[security](/tag/security)
[tls certificate](/tag/tls%20certificate)

REG AD

[![](https://image.theregister.com/5255961.jpg?imageId=5255961&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

AI + ML

## A modest proposal: Reformat everything to make documents more palatable to AI

What's up, DocLang?](https://www.theregister.com/ai-and-ml/2026/06/16/a-modest-proposal-reformat-everything-to-make-documents-more-palatable-to-ai/5255938)

[PATCHES

## Cisco SD-WAN make-me-root bug under attack

Second Catalyst SD-WAN Manager flaw exploited as an 0-day this month](https://www.theregister.com/patches/2026/06/15/cisco-sd-wan-make-me-root-bug-under-attack/5255916)

[## Europe's AI paralysis has a solution - and it starts with a semantic twin

PARTNER CONTENT: Onix's Wingspan platform promises to move enterprises from pilot purgatory to governed, enterprise-wide AI deployment in weeks, not years](https://www.theregister.com/ai-and-ml/2026/06/15/europes-ai-paralysis-has-a-solution-and-it-starts-with-a-semantic-twin/5255303)

[security

## Feds freaked ov...
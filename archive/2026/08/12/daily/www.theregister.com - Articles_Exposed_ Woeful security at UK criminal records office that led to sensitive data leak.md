---
title: Exposed: Woeful security at UK criminal records office that led to sensitive data leak
url: https://www.theregister.com/security/2026/08/12/exposed-woeful-security-at-uk-criminal-records-office-that-led-to-sensitive-data-leak/5286736
source: www.theregister.com - Articles
date: 2026-08-12
fetch_date: 2026-08-13T04:05:23.082853
---

# Exposed: Woeful security at UK criminal records office that led to sensitive data leak

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

# Exposed: Woeful security at UK criminal records office that led to sensitive data leak

Nobody patched the CMS or read the alerts, and ACRO still cannot tell whether info was exfiltrated

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 12 Aug 2026 // 14:40 UTC

The UK's criminal records office, ACRO, has escaped a fine and received a regulatory reprimand after security failings potentially exposed highly sensitive data belonging to nearly 11,000 people.

ACRO disclosed the "cybersecurity incident" in April 2023, and said at the time that it had no evidence to suggest that any data was compromised.

However, it has now emerged that attackers maintained persistent access to ACRO's website and content management system for more than seven months, and staged sensitive data for possible exfiltration.

REG AD

According to the Information Commissioner's Office (ICO), which reprimanded ACRO rather than imposing a financial penalty, [the breach was uncovered in March 2023](https://www.theregister.com/security/2023/04/06/uk-criminal-records-portal-offline-amid-security-incident/1203257) only because ACRO was investigating a separate intrusion.

REG AD

## Busting ICO enforcement jargon

The ICO has a few enforcement tools in its belt when it comes to data protection offenders.

Monetary penalties are pretty self-explanatory, but are reserved only for the very worst and most flagrant [UK GDPR](https://www.theregister.com/on-prem/2024/10/24/yet-another-uk-government-seeks-to-reform-gdpr/1253659) offenses. These can reach up to £17.5 million ($23.6 million), or 4 percent of the organization's total worldwide annual turnover, whichever is higher.

Lesser powers include enforcement notices, which can be served to offenders and are essentially a list of mandatory corrective actions an offender must take to make the regulator leave it alone.

And then the lesser of the three is a reprimand, which serves as a formal warning not to be naughty again. These are often used for public sector organizations to avoid draining public funds.

The watchdog said that while investigating an SQL injection attack that compromised 15 sets of credentials, most belonging to ACRO staff, investigators found evidence of separate intrusions dating back to July 8, 2021.

The incidents fell into three categories, the ICO said. Some did not affect personal data, while others exposed only a small number of account credentials.

The most serious involved ACRO's website and its Kentico content management system. The intrusion began on August 5, 2022, and the attackers maintained persistent access, without being detected, until March 14, 2023.

The ICO found that ACRO ran version 12.0.0 of Kentico CMS from September 2019 until March 2023 without applying the patches and hotfixes released during that period, leaving known vulnerabilities unresolved.

The ICO blamed poor communication between ACRO and its managed service provider. The supplier did not learn that patching was its responsibility until February 2020 and continued to assume that it was not required to monitor actively for security updates.

"The ambiguity around who was accountable for identifying necessary Kentico CMS patches created a gap where patches and hotfixes were missed, which ultimately left ACRO's website vulnerable," the ICO said.

Further, ACRO did not have a documented policy that covered patching Kentico CMS, nor could it demonstrate how vulnerabilities were identified or prioritized.

ACRO's Trend Micro antivirus generated alerts, but nobody appears to have been minding them. The records office told the ICO that, for reasons redacted from the postmortem, it was "unable to establish what business processes existed for the assessment or handling of security alerts at the relevant time."

REG AD

## MORE CONTEXT

* [### Criminal records office yanks web portal offline amid 'cyber security incident'](/security/2023/04/06/uk-criminal-records-portal-offline-amid-security-incident/1203257)
* [### ICO chief John Edwards steps back as workplace probe quietly unfolds](/on-prem/2026/04/27/ico-boss-edwards-steps-back-amid-workplace-investigation/5222705)
* [### UK data watchdog fines Reddit £14.47M for letting kids slip pas...
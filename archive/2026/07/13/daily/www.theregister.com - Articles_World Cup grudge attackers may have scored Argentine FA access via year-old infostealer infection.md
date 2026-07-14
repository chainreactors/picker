---
title: World Cup grudge attackers may have scored Argentine FA access via year-old infostealer infection
url: https://www.theregister.com/security/2026/07/13/world-cup-grudge-attackers-may-have-scored-argentine-fa-access-via-year-old-infostealer-infection/5270302
source: www.theregister.com - Articles
date: 2026-07-13
fetch_date: 2026-07-14T04:48:22.610551
---

# World Cup grudge attackers may have scored Argentine FA access via year-old infostealer infection

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
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
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

# World Cup grudge attackers may have scored Argentine FA access via year-old infostealer infection

Footie fans? Overreacting? There's a first time for everything

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
mon 13 Jul 2026 // 13:02 UTC

Cybersecurity shop Hudson Rock says the suspected compromise of the Argentine Football Association (AFA) may be linked to an infostealer infection nearly a year earlier.

The incident appears to be the work of an aggrieved football fan, or group of them, after Argentina eliminated Egypt from the World Cup round of 16.

Egypt's coach and football association complained about several refereeing and VAR decisions, which they said contributed to the result.

REG AD

The compromise of AFA's systems was spotted after mass emails were sent from legitimate domains stating that Argentina "stole" the win from Egypt and that "the robbery will not go unnoticed."

REG AD

Hudson Rock said it found evidence of an [infostealer](https://www.theregister.com/security/2026/01/12/block-red-teamed-its-own-ai-agent-to-run-an-infostealer/4134767) infection dating back to September 8, 2025, on a device belonging to an AFA software developer who had been employed at the governing body for nearly a decade.

The security shop operates a database of known infostealer victims, and noted that the compromised machine was added to its database the following day.

Whoever was behind the attack, which was claimed by "All Egyptian Cyber Warriors," they either sat on the credentials for nearly a year, or sought them out after Egypt were controversially eliminated from the [World Cup](https://www.theregister.com/offbeat/2026/06/13/world-cup-ai-predictor-now-lets-users-ask-daft-what-ifs/5254853).

Once they procured the credentials and authenticated themselves into the AFA's systems, Hudson Rock said they "likely had profound administrative control."

This would have included direct access to phpMyAdmin database management panels, root access to certain AFA databases, access to the management portal of AFA's training HQ, the AFA media portal, and its competition management system.

After looking at the stolen credentials in their database, the researchers said that weak, easily guessable [passwords](https://www.theregister.com/security/2025/11/06/what-are-the-most-common-passwords-no-surprises-here/954667) were reused across several internal systems.

In addition to the compromised emails sent from AFA's management and admin portal (afasistemas.com.ar), Hudson Rock spotted a number of posts made to cybercrime forums advertising the body's data for sale.

## MORE CONTEXT

* [### Crooks compromise WordPress sites to push infostealers via fake CAPTCHA prompts](/security/2026/03/10/crooks-compromise-wordpress-sites-spread-infostealers/5222045)
* [### One criminal, 50 hacked organizations, and all because MFA wasn't turned on](/security/2026/01/06/one-criminal-stole-info-from-50-orgs-thanks-to-no-mfa/2812092)
* [### Rhadamanthys malware admin rattled as cops seize a thousand-plus servers](/security/2025/11/13/cops-take-down-rhadamanthys-infostealer-venomrat/2731204)
* [### World Cup AI predictor now lets users ask daft what-ifs](/offbeat/2026/06/13/world-cup-ai-predictor-now-lets-users-ask-daft-what-ifs/5254853)

According to the advertisements, the data related to staff, professional clubs, and the AFA's external media partners.

REG AD

The samples appeared to include internal email addresses, phone numbers, user roles, and registration timestamps, as well as listings for access to AFA subdomains.

Passwords were also among the data, although much of them were securely hashed. However, a small portion were in plaintext, which Hudson Rock said suggests "a significant security oversight."

"The AFA breach is a textbook example of how devastating a single, unmitigated infostealer infection can be," the security outfit [said](https://www.infostealers.com/article/infostealer-malware-triggers-major-database-breach-at-the-argentine-football-association/). "A compromised machine belonging to a developer with high-level access highly likely handed a threat actor direct database administration rights and the ability to send authenticated internal emails.

"Because the stolen credentials sat dormant for months, the organization was lulled into a false sense of security, completely unaware of the ticking time bomb in their network infrastructure."

The AFA told reporters on Friday that it was investigating the compromise with its IT...
---
title: Suspected Chinese snoops caught breaking into universities' Roundcube mailservers
url: https://www.theregister.com/security/2026/07/08/suspected-chinese-snoops-caught-breaking-into-universities-roundcube-mailservers/5268778
source: www.theregister.com - Articles
date: 2026-07-08
fetch_date: 2026-07-09T06:03:37.104429
---

# Suspected Chinese snoops caught breaking into universities' Roundcube mailservers

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

# Suspected Chinese snoops caught breaking into universities' Roundcube mailservers

Proofpoint researcher tells The Reg: 'We estimate the total volume of targets would be a few dozen'

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
wed 8 Jul 2026 // 22:35 UTC

Suspected Chinese spies have been breaking into major US and Canadian universities since May, exploiting vulns in Roundcube mailservers to steal data belonging to physics and engineering administrators and professors, according to Proofpoint threat researchers.

Proofpoint directly observed “less than 10” universities targeted in these intrusions, Greg Lesnewich, principal threat research engineer at Proofpoint, told The Register. “We estimate the total volume of targets would be a few dozen universities, but stress that this is at best a guess, not substantiated by our data.”

While the most recent sighting occurred in early June, “we believe it is likely that the campaign is ongoing,” Lesnewich said.

REG AD

The email security shop tracks the crew as UNK\_MassTraction, and says that it focuses on individuals in departments with national security ties or in astrophysics and particle physics - all topics that support Beijing’s intelligence-gathering goals and, as such, are [frequently targeted](https://www.theregister.com/research/2026/06/15/google-says-prc-linked-spies-hid-in-medical-research-networks-for-more-than-a-year/5254547) by [government-backed cyber goons](https://www.theregister.com/security/2026/02/02/notepad-hijacking-linked-to-chinese-lotus-blossom-crew/4829043).

REG AD

To gain initial access, the intruders exploit [CVE-2024-42009](https://nvd.nist.gov/vuln/detail/cve-2024-42009), a cross-site scripting vulnerability in Roundcube that only requires that the email is opened in the mail client to achieve access to the server.

“The targeted departments were likely specifically chosen because they were all running [vulnerable] versions of Roundcube … indicating that UNK\_MassTraction had conducted reconnaissance into the targets prior to conducting the campaign,” the threat hunters [wrote](https://www.proofpoint.com/us/blog/threat-insight/one-email-closer-edge-unkmasstraction-physics-exploitation) in a Tuesday blog.

While the espionage activity is similar to an earlier campaign [disclosed by Trellix](https://www.trellix.com/blogs/research/the-silent-fileless-threat-of-vshell/) that used a filename parsing vulnerability to deliver VShell malware, a Go-based backdoor used primarily by Chinese APT groups for remote access, file operations, and post-exploitation control, Proofpoint says it cannot definitely link this earlier activity to UNK\_MassTraction.

### It all starts with a generic phishing email

The UNK\_MassTraction attack chain begins with a phishing email sent to university departments from both compromised legitimate senders and abused domains vulnerable to spoofing.

According to the threat hunters, the lures are generic, sometimes purporting to be a university marketing message, and this could imply “a larger targeting swath” than Proofpoint observed. It could also indicate “an attempt to resemble marketing or spam content because targets may open the email but ultimately overlook it (and not investigate it), which is still sufficient for the actor to gain access,” they wrote.

Opening the email triggers CVE-2024-42009. The bug abuses a desanitization issue, and can allow remote attackers to steal and send messages.

Once the user opens the email in the webmail client of a vulnerable Roundcube instance, a JavaScript loader stored in the message body executes, and allows the attacker to remotely deliver a fully functioning stealer called IceCube.

REG AD

IceCube first escapes Roundcube's iFrame instantiation via [DOM traversal](https://medium.com/%40mohanapriyanpriyan4/dom-traversal-165061ab7254), which gives the stealer access to the entire Document Object Model (DOM) in the browser and Roundcube authentication session.

Then it sets to work stealing usernames, passwords, session tokens, and cookies, and it also conducts reconnaissance against the browser, collecting info on the language in use, screen size, and form field values.

The stealer sends this initial data to the attacker’s command-and-control servers via HTTP POST, and then uses the session’s CSRF token to set up gadgets to exploit another Roundcube vulnerability. This one, a deserialization exploit tracked as [CVE-2025-49113](https://nvd.nist.gov/vuln/detail/cve-2025-491...
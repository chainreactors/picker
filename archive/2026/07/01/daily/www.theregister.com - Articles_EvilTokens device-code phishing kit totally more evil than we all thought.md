---
title: EvilTokens device-code phishing kit totally more evil than we all thought
url: https://www.theregister.com/cyber-crime/2026/07/01/eviltokens-device-code-phishing-kit-totally-more-evil-than-we-all-thought/5265409
source: www.theregister.com - Articles
date: 2026-07-01
fetch_date: 2026-07-02T05:58:28.953242
---

# EvilTokens device-code phishing kit totally more evil than we all thought

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

cyber-crime

# EvilTokens device-code phishing kit totally more evil than we all thought

It's a 'complete BEC operations environment,' Talos researcher says

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 1 Jul 2026 // 22:50 UTC

EvilTokens, the device-code phishing kit that can allow criminals to bypass multi-factor authentication (MFA) and silently authenticate as the victim to the organization's Microsoft 365 applications, appears to be even more insidious than we all thought.

Cisco Talos incident responders on Wednesday described how the lure reaches a victim's inbox, and revealed new capabilities alongside a “more sophisticated evasion approach” than documented in earlier EvilTokens research.

Talos uncovered a phishing-as-a-service (PhaaS) operator panel, branded “ARToken,” that appears to be an EvilTokens customer, according to security research engineer Michael Kelley, who noted the phishing operation shares infrastructure, API contracts, and operational patterns with the EvilTokens platform.

REG AD

REG AD

EvilTokens was [first documented](https://www.sekoia.com/blog/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1) by French cybersecurity firm Sekoia in March, and in April Microsoft said the device-code phishing campaign was compromising hundreds of organizations daily.

"Since March 15, 2026, we have observed 10 to 15 distinct campaigns launching every 24 hours," Microsoft VP of security research Tanmay Ganacharya told El Reg [at the time](https://www.theregister.com/security/2026/04/07/hundreds-compromised-daily-in-microsoft-device-code-phishes/5222742). “Each campaign is distributed at scale, targeting hundreds of organizations with highly varied and unique payloads, making pattern-based detection more challenging.”

While most subsequent analysis has covered EvilTokens’ panel and phishing kit, “what it has not shown is how an ARToken lure actually reaches an inbox,” Kelley [said](https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/) on Wednesday. “Talos recovered two near-identical messages, sent roughly four minutes apart on April 20, 2026, that initiate the chain. The tradecraft is targeted, not spray-and-pray.”

Specifically, the email lure abused a real vendor relationship between a US life-sciences company and a legitimate plumbing and fire-protection contractor. The email uses an outstanding-invoice lure, telling the life-sciences company that “the following invoices appear to still be outstanding,” and the “from” header presents the contractor’s real domain. The reply-to, however, redirects replies to an unrelated domain.

Even the visible anchor text in the body of the email reads as the vendor's genuine SharePoint tenant, we’re told. The actual href, however, points to a near-identical copycat tenant under a different, attacker-controlled Microsoft 365 workspace. But because the destination is still a legitimate sharepoint.com host, the email is less likely to be flagged as a phish.

## MORE CONTEXT

* [### FBI warns Kali365 phishing kit is stealing Microsoft OAuth tokens at scale](/cyber-crime/2026/05/22/fbi-warns-of-kali365-as-device-code-phishing-soars/5245024)
* [### Hundreds of orgs compromised daily in Microsoft device code phishing attacks](/security/2026/04/07/hundreds-compromised-daily-in-microsoft-device-code-phishes/5222742)
* [### Health board apologizes for phishing staff with with bogus vacation day](/security/2026/06/22/canadian-health-board-sorry-after-tasteless-phishing-test/5259320)
* [### Somebody told DeepSeek to build in-browser ransomware and it gleefully complied](/security/2026/07/01/somebody-told-deepseek-to-build-in-browser-ransomware-and-it-gleefully-complied/5265311)

During its investigation into the ARToken phishing infrastructure, Cisco uncovered the connections to EvilTokens – including an identical API contract to the one originally documented by Sekoia and matching deployment and operational models – as well as “notably more sophisticated” anti-analysis and evasion capabilities.

ARToken’s panel also revealed a very comprehensive post-exploitation toolkit that provides token management and persistence mechanisms, and a built-in business email compromise (BEC) tool with full Microsoft Outlook inbox read access, email sending capabilities as the victim, inbox rule creation for forwarding and deleting messages, and keyword-based monitoring across all compromised accounts.

“These features indicate the platform is more mature than a simple device code phishing kit - it is a complete BEC operation...
---
title: WeChat worm could pwn a friend before they even answered the call
url: https://www.theregister.com/security/2026/09/09/wechat-worm-could-pwn-a-friend-before-they-even-answered-the-call/5295234
source: www.theregister.com - Articles
date: 2026-09-09
fetch_date: 2026-09-10T06:52:45.393662
---

# WeChat worm could pwn a friend before they even answered the call

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

Security

# WeChat worm could pwn a friend before they even answered the call

Calif says AI helped turn a VoIP memory bug into cross-platform RCE before Tencent shut it down

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 9 Sep 2026 // 13:45 UTC

### READ MORE

* [#### Laptop-slinger Framework refunding customers who paid top dollar for RAM

  20 minutes ago](/personal-tech/2026/09/10/laptop-slinger-framework-refunding-customers-who-paid-top-dollar-for-ram/5295439)
* [#### Microsoft goes after Salesforce and ERP users with AI-powered converter

  1 hour ago](/software/2026/09/10/microsoft-goes-after-salesforce-and-erp-users-with-ai-powered-converter/5295428)
* [#### VMware defends ending downloads of SDK that helps VM backups– or migrations to rivals

  4 hours ago](/virtualization/2026/09/10/vmware-defends-ending-downloads-of-sdk-that-helps-vm-backups-or-migrations-to-rivals/5295421)
* [#### Anthropic reveals fourth likely crime committed by its AI

  7 hours ago](/ai-and-ml/2026/09/10/anthropic-reveals-fourth-likely-crime-committed-by-its-ai/5295412)
* [#### Novel Blue Moon kit targeting Chrome and Windows reflects new reality of AI-driven exploits

  8 hours ago](/research/2026/09/09/novel-blue-moon-kit-targeting-chrome-and-windows-reflects-new-reality-of-ai-driven-exploits/5295399)

Tencent has patched up a zero-click vulnerability that security researchers used to create a worm capable of spreading through calls on WeChat.

With more than 1.4 billion monthly active users, WeChat is among the most popular apps in the world. According to researchers at Calif, its VoIP stack contained a memory corruption bug that could enable a trusted contact to take control of a user's account simply by calling them.

Calif called the flaw WeWorm, describing it as the first zero-click worm capable of spreading through WeChat calls on both iOS and Android.

REG AD

Calif released a demo of the vulnerability in action this week, and although Tencent has pushed fixes to address the attack on August 21, the team that found it is still withholding key details.

REG AD

In Calif's demonstration, the exploit took control of a victim's WeChat account within seconds, without the recipient answering the call. The compromised account then called another contact and repeated the process without user interaction.

Declining the call stopped infection, but answering it or allowing it to continue ringing did not. An attacker could also try again when the recipient was away from the phone, the researchers said.

"Exploitation takes only seconds, and gives us full control of the WeChat account," Calif [said](https://calif.io/research/weworm). "We can read and send messages, make calls, and act on the victim's behalf."

The exploit requires the attacker to be on the victim's friends list. Calif argued that this offered limited protection because a compromised account could be used to target its trusted contacts.

Calif said the WeWorm exploit could be chained with other vulnerabilities to compromise an entire device rather than only a [WeChat](https://www.theregister.com/security/2025/07/11/chinese-censorship-busters-say-tencent-behind-shutdown-bid/747332) account. It did not disclose the full attack chain.

"Chained with other Android and iOS bugs we've reported and are helping fix, it can lead to full control of the device," the researchers said.

"[Attackers] could exploit another app, gain root access using techniques like those in [OEMpocalypse](https://calif.io/research/oempocalypse), take over the victim's WeChat app, and use it to attack you."

Calif said it used AI to find the vulnerability and develop its first remote code execution (RCE) exploit in about two days. Tencent later confirmed the researchers' findings.

REG AD

The researchers said they published their high-level findings to highlight how AI could make such capabilities available beyond "well-funded, sophisticated actors."

Calif plans to present the full analysis of WeWorm "at an upcoming conference."

Ryan Fedasiuk, an adjunct assistant professor in Georgetown University's Security Studies Program, [described](https://x.com/ryanfedasiuk/status/209...
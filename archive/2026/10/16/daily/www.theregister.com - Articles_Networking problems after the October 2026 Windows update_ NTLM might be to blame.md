---
title: Networking problems after the October 2026 Windows update? NTLM might be to blame
url: https://www.theregister.com/security/2026/10/16/networking-problems-after-the-october-2026-windows-update-ntlm-might-be-to-blame/5303503
source: www.theregister.com - Articles
date: 2026-10-16
fetch_date: 2026-10-17T06:39:12.414837
---

# Networking problems after the October 2026 Windows update? NTLM might be to blame

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
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
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

# Networking problems after the October 2026 Windows update? NTLM might be to blame

Legacy protocol is going to be axed, and enforcement by default will highlight how migration is going

Richard Speed
[Richard
Speed](https://www.theregister.com/author/richard-speed)
MICROSOFT ECOSYSTEM REPORTER

Published
fri 16 Oct 2026 // 16:30 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### Uncle Scam Wants You … to cough up your cash and personal data, FBI warns ahead of midterms

  15 hours ago](/cyber-crime/2026/10/16/uncle-scam-wants-you-to-cough-up-your-cash-and-personal-data-fbi-warns-ahead-of-midterms/5303512)
* [#### Attack on BAE-managed system disrupts US bankruptcy courts

  17 hours ago](/security/2026/10/16/attack-on-bae-managed-system-disrupts-us-bankruptcy-courts/5303487)
* [#### Thief snatches school snapper's SD cards in smash & grab

  21 hours ago](/security/2026/10/16/thief-snatches-school-snappers-sd-cards-in-smash-grab/5303379)
* [#### User refused to change her password because everyone already knew it

  23 hours ago](/security/2026/10/16/user-refused-to-change-her-password-because-everyone-already-knew-it/5301864)
* [#### Researchers warned attackers could 'defrost the food' months before French supermarkets got hit

  1 day ago](/security/2026/10/15/researchers-warned-attackers-could-defrost-the-food-months-before-french-supermarkets-got-hit/5303425)

The October 2026 Windows security update may break networking for some customers who are still clinging to long-deprecated NTLMv1 security.

A seemingly minor change in the update could have [major implications](https://support.microsoft.com/en-gb/servicing/os/windows/docs/2025/08/upcoming-changes-to-ntlmv1-in-windows-11-version-24h2-and-windows-server-2025#rollout-of-changes) for administrators and enterprises that haven't fully moved away from the legacy technology.

Before the October 2026 update, Windows permitted NTLMv1-derived credentials for Single Sign-On and generated warning events. After the update, requests to use NTLMv1-derived credentials are blocked.

REG AD

It comes down to the BlockNtlmSSO registry value. If it hasn't been set, Windows will now use Enforce mode (1) instead of Audit mode (0), thus blocking requests and potentially impacting Wi-Fi, Ethernet, and VPN authentication, and therefore connections.

REG AD

The update does not set the value of BlockNtlmSSO, and administrators can set it to 0 to temporarily allow NTLMv1-derived Single Sign-On credentials. However, Microsoft noted, "Using Audit mode reduces the protection provided by Enforce mode and should only be considered as a scoped, temporary security exception."

To be clear, this is not a bug and is by design. The addition of NTLM to the deprecation list [occurred in 2024](https://www.theregister.com/security/2024/06/06/microsoft-adds-ntlm-to-the-deprecated-features-list/1123954), and Microsoft added audit logs for NTLMv1 usage in late August 2025. The Windows giant has made no secret of its desire to ditch the legacy technology, [stating in 2023](https://techcommunity.microsoft.com/blog/windows-itpro-blog/the-evolution-of-windows-authentication/3926848), "Our end goal is eliminating the need to use NTLM at all."

The problem is NTLM's longevity. It appeared in 1993 with Windows NT 3.1, and removing it from enterprise environments has proven tricky, even though it is somewhat insecure by modern standards. Microsoft [removed](https://learn.microsoft.com/en-gb/windows/whats-new/removed-features#removed-features-and-functionality) it from Windows 11 24H2 and Windows Server 2025, but some remnants can still be found, notably when using MS-CHAPv2-based connections, including PEAP-MSCHAPv2, and EAP-MSCHAPv2, in a domain-joined environment.

[![A close-up thumb in front of a digital fingerprint recognition overlay.](https://image.theregister.com/5235229.webp?imageId=5235229&width=960&height=432&format=jpg)

## NTLM authentication: still broken after all these years

FROM THE ARCHIVES](/se...
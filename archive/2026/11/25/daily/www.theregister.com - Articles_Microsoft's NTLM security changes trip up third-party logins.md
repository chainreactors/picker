---
title: Microsoft's NTLM security changes trip up third-party logins
url: https://www.theregister.com/security/2026/11/25/microsofts-ntlm-security-changes-trip-up-third-party-logins/5312085
source: www.theregister.com - Articles
date: 2026-11-25
fetch_date: 2026-11-26T10:15:16.437883
---

# Microsoft's NTLM security changes trip up third-party logins

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
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [SC 26](/special_features/sc26)
  + [Supercomputing Month 2026](/special_features/supercomputing_month_2026)
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
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
* [Security](/tag/security)
* [Software](/tag/software)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Outages](/tag/outage)

REG AD

[security](/tag/security)

# Microsoft's NTLM security changes trip up third-party logins

It's not our fault if you've implemented it wrong

Richard Speed
[Richard
Speed](https://www.theregister.com/author/richard-speed)
MICROSOFT ECOSYSTEM REPORTER

Published
wed 25 Nov 2026 // 17:01 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### Microsoft fixes Office dialog that had nothing to say and wouldn't go away

  19 hours ago](/software/2026/11/25/microsoft-fixes-office-dialog-that-had-nothing-to-say-and-wouldnt-go-away/5312057)
* [#### Microsoft 365 Backup stretches recovery window to ten years

  21 hours ago](/saas/2026/11/25/microsoft-365-backup-stretches-recovery-window-to-ten-years/5312043)
* [#### Microsoft refreshes Copilot app search for users without an AI subscription

  1 day ago](/personal-tech/2026/11/24/microsoft-refreshes-copilot-app-search-for-users-without-an-ai-subscription/5311895)
* [#### Microsoft mega outage: Report reveals testing gaps and emails that never arrived

  2 days ago](/saas/2026/11/23/microsoft-mega-outage-report-reveals-testing-gaps-and-emails-that-never-arrived/5311656)
* [#### Everything going down at once wasn't evidence of a conspiracy – but the truth may be scarier

  2 days ago](/off-prem/2026/11/23/everything-going-down-at-once-wasnt-evidence-of-a-conspiracy-but-the-truth-may-be-scarier/5311458)

Microsoft's November security updates can break authentication in some third-party applications and devices following changes to NTLM message signing.

Affected systems include authentication proxy servers, single sign-on (SSO) products, and application packaging tools, the company's [support notice](https://support.microsoft.com/en-gb/servicing/os/windows/docs/2026/11/kb5135557-ntlm-signing-security-improvements) says.

The failures stem from products that claim to supply required information during NTLM authentication but return incomplete or empty data, Microsoft said: "An affected device might set the NTLMSSP\_NEGOTIATE\_TARGET\_INFO flag in its CHALLENGE\_MESSAGE but provide an empty or incomplete TargetInfo field."

REG AD

Administrators can use the notice's network trace and event log examples to identify affected products. For confirmed cases, the temporary workaround is to set the ClientAllowUnsignedNtlm Registry value to 1 on affected clients. This stops the client offering signing, backing out the new default rather than fixing the incompatible product. The recommended long-term options are a vendor update or Kerberos authentication, where supported.

REG AD

The value sits under HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\MSV1\_0 and defaults to 0, enabling clients to offer signing on non-anonymous connections.

The NTLM changes arrived in the November 10 update as phase 1 in a 2-phase process. In phase 1, "Windows client devices begin offering NTLM signing on all connections by default. Servers accept both signed and unsigned clients. Auditing events identify clients not using signing."

Phase 2, scheduled for May 2027, will make Windows servers require NTLM signing by default. "Clients that do not offer signing will be rejected by secure servers," Microsoft stated.

Ominously, Microsoft warned that it "might remove the registry keys at a future date," so the company is not kidding about the temporary workaround thing.

The additional protections were added to address [CVE-2026-118737](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118737), a vulnerability in which "improper verification of cryptographic signature in Windows Remote Procedure Call Runtime allows an unauthorized attacker to execute code over a network."

NTLM is on Microsoft's hit list, having [joined the Deprecated Features list](https://www.theregister.com/security/2024/06/06/microsoft-adds-ntlm-to-the-deprecated-features-list/1123954) in 2024. It dates back to the era of Windows NT, and Microsoft [has made clear](https://techcommunity.microsoft.com/blog/windows-itpro-blog/the-ev...
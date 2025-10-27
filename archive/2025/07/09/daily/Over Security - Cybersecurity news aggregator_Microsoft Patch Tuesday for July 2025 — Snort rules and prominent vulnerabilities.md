---
title: Microsoft Patch Tuesday for July 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-july-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-09
fetch_date: 2025-10-06T23:53:17.029307
---

# Microsoft Patch Tuesday for July 2025 — Snort rules and prominent vulnerabilities

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2025/07/patch-tues.jpg)

# Microsoft Patch Tuesday for July 2025 — Snort rules and prominent vulnerabilities

By
[Tiago Pereira](https://blog.talosintelligence.com/author/tiago-pereira/)

Tuesday, July 8, 2025 16:29

[Patch Tuesday](/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for July 2025, which includes 132 vulnerabilities affecting a range of products, including 14 that Microsoft marked as “critical.”

In this month's release, Microsoft observed none of the included vulnerabilities being actively exploited in the wild. Out of 14 "critical" entries, 11 are remote code execution (RCE) vulnerabilities in Microsoft Windows services and applications including KDC Proxy service, Microsoft Office and SharePoint server.

[CVE-2025-49735](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49735) is an RCE vulnerability in Windows KDC Proxy Service (KPSSVC) given a CVSS 3.1 score of 8.1. To successfully exploit this vulnerability, an unauthenticated attacker could use a specially-crafted application to leverage a cryptographic protocol vulnerability in KPSSVC to perform RCE against the target. Microsoft has noted that this vulnerability only affects Windows servers that are configured as a Kerberos key Distribution Center (KDC) Proxy Protocol server, and domain controllers are not affected. Microsoft assessed that the attack complexity is “high,” and exploitation is "more likely."

[CVE-2025-49704](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49704) is an RCE vulnerability in Microsoft SharePoint server given a CVSS 3.1 score of 7.7. Microsoft noted that this vulnerability in Microsoft Office SharePoint is due to improper control of generation of code (“code injection”) which would allow an authenticated attacker to execute code over a network. To exploit this vulnerability, an authenticated attacker in a network-based attack, with a minimum of Site Member permission, could execute arbitrary code remotely on the SharePoint server. Microsoft assessed that the attack complexity is “low,” and exploitation is “more likely."

[CVE-2025-49695](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49695), [CVE-2025-49696](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49696), [CVE-2025-49697](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49697), [CVE-2025-49698](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49698), [CVE-2025-49702](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49702) and [CVE-2025-49703](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49703) are RCE vulnerabilities in Microsoft Office and Microsoft Word. The vulnerabilities [CVE-2025-49695](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49695) and [CVE-2025-49698](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49698) are "use after free” (UAF) vulnerabilities that occur when Microsoft Office tries to access memory that has already been freed. [CVE-2025-49696](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49696) is an out-of-bounds read in Microsoft Office. Microsoft assessed that for [CVE-2025-49695](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49695) and [CVE-2025-49696](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49696), the attack complexity is "low," and exploitation is "more likely." For [CVE-2025-49697](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49697), [CVE-2025-49698](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49698), [CVE-2025-49702](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49702) and [CVE-2025-49703](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49703), the attack complexity is "low," and exploitation is "less likely."

[CVE-2025-48822](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-48822) is an RCE vulnerability in Windows Hyper-V Discrete Device Assignment (DDA) given a CVSS 3.1 score of 8.6. This vulnerability is an out-of-bounds read in Hyper-V that could allow an unauthorized attacker to execute code locally. Microsoft assessed that the attack complexity is “low,” and exploitation is “less likely.”

[CVE-2025-47981](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-47981)is an RCE vulnerability in SPNEGO Extended Negotiation (NEGOEX) Security Mechanism given a CVSS 3.1 score of 9.8. This vulnerability is a heap-based buffer overflow that could allow an unauthorized attacker to execute code over a network. According to Microsoft, this vulnerability affects Windows client machines running Windows 10, version 1607 and above, due to the following GPO being enabled by default on these operating systems: "Network security: Allow PKU2U authentication requests to this computer to use online identities." Microsoft has assessed that the attack complexity is “low,” and exploitation is “more likely.”

[CVE-2025-49717](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-49717) is an RCE vulnerability in Microsoft SQL Server, given a CVSS 3.1 score of 8.5. This vulnerability is a heap-based buffer overflow that could allow an unauthorized attacker to execute code over a network. However, Microsoft has assessed “exploitation unlikely”.

The last critical vulnerability listed ([CVE-2025-47980](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-47980)) is an information disclosure in Windows Imaging Component that, if exploited, could allow an attacker to read small portions of heap memory. Microsoft has assessed that the attack complexity is “low,” and exploitation ...
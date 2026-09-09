---
title: Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-september-2026/
source: Over Security
date: 2026-09-08
fetch_date: 2026-09-09T06:56:31.940067
---

# Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities

[Blog](/)

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

# Microsoft Patch Tuesday for September 2026 — Snort rules and prominent vulnerabilities

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Tuesday, September 8, 2026 18:16

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for September 2026, which includes 973 vulnerabilities affecting a range of products, including 113 that Microsoft marked as "critical."

**Microsoft notes that 2 of the vulnerabilities disclosed this month have been exploited in the wild:**

[*CVE-2026-81963*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963) affects Windows Update Stack. [*CVE-2026-81963*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963) is a elevation of privilege vulnerability associated with Improper Link Resolution Before File Access ('Link Following') and Improper Access Control and has a CVSS base score of 7.8.

[*CVE-2026-85880*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880) affects Windows Advanced Local Procedure Call (ALPC). [*CVE-2026-85880*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880) is a elevation of privilege vulnerability associated with Heap-based Buffer Overflow and Use of Uninitialized Resource and has a CVSS base score of 7.8.

Out of 113 "critical" vulnerabilities, 82 are remote code execution (RCE) vulnerabilities.

---

**Microsoft considers exploitation of the following vulnerabilities more likely:**

[*CVE-2026-69676*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69676) affects Windows Kerberos. [*CVE-2026-69676*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69676) is a remote code execution vulnerability associated with Authentication Bypass by Capture-replay and has a CVSS base score of 8.8.

[*CVE-2026-69852*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69852) affects Windows Routing and Remote Access Service (RRAS). [*CVE-2026-69852*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69852) is a remote code execution vulnerability associated with Heap-based Buffer Overflow and has a CVSS base score of 7.5.

[*CVE-2026-72957*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72957) affects Windows Deployment Services. [*CVE-2026-72957*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72957) is a remote code execution vulnerability associated with Heap-based Buffer Overflow and has a CVSS base score of 7.8.

[*CVE-2026-69854*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69854) affects Spring Cloud Azure. [*CVE-2026-69854*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69854) is a elevation of privilege vulnerability associated with Improper Authentication and has a CVSS base score of 9.0.

[*CVE-2026-83501*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83501) affects Windows Virtualization-Based Security (VBS). [*CVE-2026-83501*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83501) is a information disclosure vulnerability associated with Out-of-bounds Read and has a CVSS base score of 5.5.

[*CVE-2026-70585*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70585) affects Windows Services for NFS ONCRPC XDR Driver. [*CVE-2026-70585*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70585) is a remote code execution vulnerability associated with Use After Free and has a CVSS base score of 7.0.

[*CVE-2026-69730*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69730) affects Windows DNS Server. [*CVE-2026-69730*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69730) is a remote code execution vulnerability associated with Use After Free and has a CVSS base score of 9.8.

[*CVE-2026-69857*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69857) affects Azure Cosmos DB. [*CVE-2026-69857*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69857) is a spoofing vulnerability associated with Authorization Bypass Through User-Controlled Key and has a CVSS base score of 8.5.

---

**Microsoft considers exploitation of the following vulnerabilities less likely:**

[*CVE-2026-69845*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69845) and [*CVE-2026-72979*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72979) affect Windows DHCP Server. [*CVE-2026-69845*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69845) is a remote code execution vulnerability associated with Heap-based Buffer Overflow and Improper Input Validation and has a CVSS base score of 9.8. [*CVE-2026-72979*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72979) is a remote code execution vulnerability associated with Use After Free and has a CVSS base score of 9.8.

[*CVE-2026-58599*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-58599) affects HEVC Video Extensions. [*CVE-2026-58599*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-58599) is a remote code execution vulnerability associated with Heap-based Buffer Overflow and has a CVSS base score of 7.8.

[*CVE-2026-65772*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65772) affects Microsoft Dynamics 365 On-Premises. [*CVE-2026-65772*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65772) is a remote code execution vulnerability associated with Deserialization of Untrusted Data and has a CVSS base score of 8.8.

[*CVE-2026-66302*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-66302) affects Skype for Business. [*CVE-2026-66302*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-66302) is a remote code execution vulnerabi...
---
title: Microsoft Patch Tuesday for November 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/
source: Over Security
date: 2026-11-11
fetch_date: 2026-11-12T09:02:43.046406
---

# Microsoft Patch Tuesday for November 2026 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for November 2026 — Snort rules and prominent vulnerabilities

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Tuesday, November 10, 2026 20:41

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for November 2026, which includes 1095 vulnerabilities affecting a range of products, including 64 that Microsoft marked as "critical."

Microsoft notes that 1 of the vulnerabilities disclosed this month have been exploited in the wild

[CVE-2026-124194](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-124194) affects Microsoft Office Outlook. [CVE-2026-124194](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-124194) is a spoofing vulnerability involving Product UI does not Warn User of Unsafe Actions and has a CVSS base score of 6.5.

Out of 64 "critical" vulnerabilities, 48 are remote code execution (RCE) vulnerabilities.

---

**Microsoft considers exploitation of the following vulnerabilities more likely:**

[CVE-2026-113862](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-113862) affects Windows Network Address Translation (NAT). [CVE-2026-113862](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-113862) is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.1.

[CVE-2026-118146](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118146) and [CVE-2026-118148](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118148) affect Active Directory Domain Services. [CVE-2026-118146](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118146) is a remote code execution vulnerability involving Incorrect Authorization and has a CVSS base score of 8.8. [CVE-2026-118148](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118148) is an elevation of privilege vulnerability involving Incorrect Authorization and has a CVSS base score of 7.5.

[CVE-2026-118207](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118207) affects Microsoft Exchange Server. [CVE-2026-118207](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118207) is a remote code execution vulnerability involving Use of Incorrectly-Resolved Name or Reference and has a CVSS base score of 8.8.

[CVE-2026-119952](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-119952) affects Windows Schannel. [CVE-2026-119952](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-119952) is a remote code execution vulnerability involving Observable Timing Discrepancy and has a CVSS base score of 8.1.

**Microsoft considers exploitation of the following vulnerabilities less likely:**

[CVE-2026-109459](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109459) and [CVE-2026-119967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-119967) affect Windows Message Queuing Queue Manager. [CVE-2026-109459](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109459) is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 8.1. [CVE-2026-119967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-119967) is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.1.

[CVE-2026-110043](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110043), [CVE-2026-110068](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110068) and [CVE-2026-111309](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111309) affect Microsoft Office Outlook. [CVE-2026-110043](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110043) is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 8.8. [CVE-2026-110068](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110068) is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.8. [CVE-2026-111309](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111309) is a remote code execution vulnerability involving Release of Invalid Pointer or Reference and has a CVSS base score of 8.8.

[CVE-2026-110047](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110047), [CVE-2026-110067](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110067), [CVE-2026-111285](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111285) and [CVE-2026-124185](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-124185) affect Microsoft Office Word. [CVE-2026-110047](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110047) is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.8. [CVE-2026-110067](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-110067) is a remote code execution vulnerability involving Use After Free and has a CVSS base score of 8.8. [CVE-2026-111285](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111285) is a remote code execution vulnerability involving Heap-based Buffer Overflow and has a CVSS base score of 8.8. [CVE-2026-124185](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-124185) is a remote code execution vulnerability involving Use of Uninitialized Resource and has a CVSS base score of 7.5.

[CVE-2026-111289](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111289) and [CVE-2026-120003](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-120003) affect Microsoft Office. [CVE-2026-111289](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111289) is a remote code execution vulnerability involving Use After Free and has...
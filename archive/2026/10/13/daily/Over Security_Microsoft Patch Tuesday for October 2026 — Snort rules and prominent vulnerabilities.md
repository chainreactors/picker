---
title: Microsoft Patch Tuesday for October 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-october-2026/
source: Over Security
date: 2026-10-13
fetch_date: 2026-10-14T06:53:02.467440
---

# Microsoft Patch Tuesday for October 2026 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for October 2026 — Snort rules and prominent vulnerabilities

By
[Nick Biasini](https://blog.talosintelligence.com/author/nick-biasini/)

Tuesday, October 13, 2026 16:37

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for October 2026, which includes 1415 vulnerabilities affecting a range of products, including 85 that Microsoft marked as "critical."

Microsoft notes that 1 of the vulnerabilities disclosed this month have been exploited in the wild

[*CVE-2026-96951*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-96951) is a security feature bypass vulnerability that affects Windows Shell. The shared weakness is Improper Neutralization of Special Elements used in a Command ('Command Injection'). The vulnerability has a CVSS base score of 8.8.

Out of 85 "critical" vulnerabilities, 67 are remote code execution (RCE) vulnerabilities.

Microsoft considers exploitation of the following vulnerabilities more likely.

[*CVE-2026-70229*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70229) is a remote code execution vulnerability that affects Windows Active Directory Domain Services. The shared weakness is Incorrect Authorization. The vulnerability has a CVSS base score of 8.1.

[*CVE-2026-70571*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70571) is a remote code execution vulnerability that affects Microsoft Exchange Server. The shared weakness is Stack-based Buffer Overflow. The vulnerability has a CVSS base score of 8.1.

Microsoft considers exploitation of the following vulnerabilities less likely.

[*CVE-2026-105733*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-105733), [*CVE-2026-102214*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-102214), and [*CVE-2026-108399*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-108399) affect Windows Hyper-V. [*CVE-2026-105733*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-105733) has an impact of remote code execution; involves Incorrect Initialization of Resource; has a CVSS base score of 8.8. [*CVE-2026-102214*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-102214) has an impact of remote code execution; involves Use After Free; has a CVSS base score of 8.8. [*CVE-2026-108399*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-108399) has an impact of elevation of privilege; involves Heap-based Buffer Overflow; has a CVSS base score of 7.2.

[*CVE-2026-100202*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-100202) is a remote code execution vulnerability that affects Windows Message Queuing Queue Manager. The shared weakness is Use After Free. The vulnerability has a CVSS base score of 9.8.

[*CVE-2026-100209*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-100209), [*CVE-2026-100210*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-100210), [*CVE-2026-100211*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-100211), [*CVE-2026-97739*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97739), [*CVE-2026-97745*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97745), [*CVE-2026-97755*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97755), [*CVE-2026-97759*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97759), [*CVE-2026-97765*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97765), [*CVE-2026-97778*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97778), [*CVE-2026-97741*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97741), [*CVE-2026-97742*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97742), [*CVE-2026-97753*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97753), [*CVE-2026-97756*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97756), [*CVE-2026-97758*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97758), [*CVE-2026-97761*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97761), [*CVE-2026-97767*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97767), [*CVE-2026-97776*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97776), and [*CVE-2026-97780*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97780) are remote code execution vulnerabilities that affect Microsoft Office Excel. Each has a CVSS base score of 8.8. [*CVE-2026-100209*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-100209), [*CVE-2026-100211*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-100211), [*CVE-2026-97745*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97745), and [*CVE-2026-97759*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97759) involve Use After Free. [*CVE-2026-100210*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-100210), [*CVE-2026-97765*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97765) , [*CVE-2026-97756*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97756),  [*CVE-2026-97758*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97758), [*CVE-2026-97776*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97776), and [*CVE-2026-97780*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97780) involve Heap-based Buffer Overflow. [*CVE-2026-97739*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97739) involves Heap-based Buffer Overflow and Integer Underflow (Wrap or Wraparound). [*CVE-2026-97755*](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97755) involves Out-of-bou...
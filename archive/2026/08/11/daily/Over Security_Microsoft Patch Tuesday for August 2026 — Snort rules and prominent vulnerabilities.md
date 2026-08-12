---
title: Microsoft Patch Tuesday for August 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/
source: Over Security
date: 2026-08-11
fetch_date: 2026-08-12T04:02:29.058140
---

# Microsoft Patch Tuesday for August 2026 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for August 2026 — Snort rules and prominent vulnerabilities

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Tuesday, August 11, 2026 18:21

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for August 2026, which includes 421 vulnerabilities affecting a range of products, including 62 that Microsoft marked as "critical."

Microsoft notes that 1 of the vulnerabilities disclosed this month have been exploited in the wild

[CVE-2026-68820](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820) is an elevation of privilege vulnerability affecting Windows Ancillary Function Driver for WinSock. A Use After Free vulnerability could allow an authorized attacker to elevate privileges locally. This vulnerability has a CVSS base score of 7.0.

Out of 62 "critical" vulnerabilities, 40 are remote code execution (RCE) vulnerabilities.

Microsoft considers exploitation of the following vulnerabilities more likely.

[CVE-2026-62893](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62893) is a remote code execution vulnerability affecting Windows Deployment Services TFTP Server. A Use After Free could allow an unauthorized attacker to execute code over a network. This vulnerability has a CVSS base score of 9.8.

[CVE-2026-65665](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65665) is a remote code execution vulnerability affecting Microsoft SharePoint Server. Deserialization of Untrusted Data could allow an authorized attacker to execute code over a network. This vulnerability has a CVSS base score of 8.8.

[CVE-2026-62823](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62823) is a remote code execution vulnerability affecting Windows DHCP Server. A Heap-based Buffer Overflow could allow an unauthorized attacker to execute code over an adjacent network. This vulnerability has a CVSS base score of 8.8.

Microsoft considers exploitation of the following vulnerabilities less likely.

[CVE-2026-62830](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62830) is an elevation of privilege vulnerability affecting Azure SRE Agent. Missing Authorization could allow an authorized attacker to elevate privileges over a network. This vulnerability has a CVSS base score of 9.9.

[CVE-2026-50516](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50516) is an elevation of privilege vulnerability affecting Microsoft Azure Kubernetes Service. Missing Authentication for Critical Function could allow an unauthorized attacker to elevate privileges over a network. This vulnerability has a CVSS base score of 9.4.

Three remote code execution vulnerabilities, [CVE-2026-68794](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68794), [CVE-2026-68816](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68816) and [CVE-2026-68804](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68804), affect Microsoft Excel and have a CVSS base score of 7.8. An unauthorized attacker could execute code locally. [CVE-2026-68794](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68794) is a Heap-based Buffer Overflow. [CVE-2026-68816](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68816) is a Stack-based Buffer Overflow. [CVE-2026-68804](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68804) involves a Numeric Truncation Error and a Heap-based Buffer Overflow.

[CVE-2026-62911](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62911) is an elevation of privilege vulnerability affecting Microsoft Exchange Server. Authentication Bypass by Capture-replay could allow an authorized attacker to elevate privileges over a network. This vulnerability has a CVSS base score of 8.0.

Nine remote code execution vulnerabilities, [CVE-2026-63515](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-63515), [CVE-2026-65657](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65657), [CVE-2026-63532](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-63532), [CVE-2026-64898](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64898), [CVE-2026-64903](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64903), [CVE-2026-64909](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64909), [CVE-2026-64910](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64910), [CVE-2026-64911](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64911) and [CVE-2026-70130](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70130), affect Microsoft Office and could allow an unauthorized attacker to execute code locally. [CVE-2026-63515](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-63515) involves an Out-of-bounds Read and an Integer Underflow (Wrap or Wraparound) and has a CVSS base score of 7.8. [CVE-2026-65657](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65657) is a Use After Free and has a CVSS base score of 7.8. [CVE-2026-63532](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-63532) involves an Integer Overflow or Wraparound and a Heap-based Buffer Overflow and has a CVSS base score of 7.8. [CVE-2026-64898](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64898) involves a Heap-based Buffer Overflow and an Integer Overflow or Wraparound and has a CVSS base score of 7.8. [CVE-2026-64903](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64903) involves an Integer Overflow or Wraparound and a Heap-based Buffer Overflow and has a CVSS base score of 7.8. [CVE-2026-64909](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-64909) involves an In...
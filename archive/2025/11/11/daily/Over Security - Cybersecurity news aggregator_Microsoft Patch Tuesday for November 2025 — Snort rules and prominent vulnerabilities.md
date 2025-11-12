---
title: Microsoft Patch Tuesday for November 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-november-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-11
fetch_date: 2025-11-12T03:12:38.166478
---

# Microsoft Patch Tuesday for November 2025 — Snort rules and prominent vulnerabilities

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

![](/content/images/2025/11/patch-tuesday.jpg)

# Microsoft Patch Tuesday for November 2025 — Snort rules and prominent vulnerabilities

By
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/)

Tuesday, November 11, 2025 13:19

[Patch Tuesday](/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for November 2025, which includes 63 vulnerabilities affecting a range of products, including 5 that Microsoft marked as “critical.” Current intelligence shows that one of the important vulnerabilities, CVE-2025-62215, has already been detected in the wild.

Out of five "Critical" entries, three are remote code execution (RCE) vulnerabilities in Microsoft Windows components including GDI+, Microsoft Office, and Visual Studio. One is an elevation of privilege vulnerability affecting the DirectX Graphics Kernel.

In the following sections we give a concise overview of the critical and important entries that are most relevant for defenders. The full catalogue of all reported issues can be found on Microsoft’s official [update page](https://msrc.microsoft.com/update-guide/releaseNote/2025-Nov).

# Exploited in the Wild

One “important” vulnerability was confirmed to have been exploited in the wild.

[CVE-2025-62215](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62215) is a Windows Kernel elevation of privilege vulnerability, given a CVSS 3.1 score of 7.8, where a race condition in Windows Kernel allows an authorized attacker to elevate privileges locally. Microsoft assessed that the attack complexity is “low”.

# Critical Vulnerabilities

Among all the critical vulnerabilities, none of them were labelled as exploitation more likely. Five are considered exploitation less likely. Below we describe each of those five entries.

[CVE-2025-60724](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-60724) is a RCE vulnerability in GDI+, given a CVSS 3.1 score of 9.8, where a heap-based buffer overflow in Microsoft Graphics Component allows an unauthorized attacker to execute code over a network. The vulnerability can be triggered by convincing a victim to download and open a document that contains a specially crafted metafile. In the worst-case scenario, an attacker could trigger this vulnerability on web services by uploading documents containing a specially crafted metafile without user interaction. An attacker doesn't require any privileges on the systems hosting the web services. Successful exploitation of this vulnerability could cause RCE or Information Disclosure on web services that are parsing documents that contain a specially crafted metafile, without the involvement of a victim user. Microsoft assessed that the attack complexity is “low”, and that exploitation is “less likely”.

[CVE‑2025‑30398](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-30398) is a Nuance PowerScribe 360 information disclosure vulnerability, given a CVSS 3.1 score of 8.1, where missing authorization in Nuance PowerScribe allows an unauthorized attacker to disclose information over a network. An unauthenticated attacker could exploit this vulnerability by making an API call to a specific endpoint. The attacker could then use the data to gain access to sensitive information (including PII data) on the server. Microsoft assessed that the attack complexity is “low”, and that exploitation is “less likely”.

[CVE‑2025‑62199](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62199) is a RCE vulnerability in Microsoft Office applications, given a CVSS 3.1 score of 7.8, where a use‑after‑free flaw in Microsoft Office allows an unauthenticated attacker to execute code locally on a vulnerable workstation. To exploit this vulnerability, an attacker must send the user a malicious file and convince them to open it. Microsoft assessed that the attack complexity is “low”, and that exploitation is “less likely”.

[CVE‑2025‑60716](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-60716) is a DirectX Graphics kernel elevation of privilege vulnerability, given a CVSS 3.1 score of 7, where a use‑after‑free flaw in Windows DirectX allows an authorized attacker to elevate privileges locally. Successful exploitation of this vulnerability requires an attacker to win a race condition. Microsoft assessed that the attack complexity is “high”, and that exploitation is “less likely”.

[CVE‑2025‑62214](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62214) is a RCE vulnerability in Visual Studio, given a CVSS 3.1 score of 6.7, where AI command injection in Visual Studio allows an authorized attacker to execute code locally. Exploitation is not trivial for this vulnerability as it requires multiple steps: prompt injection, Copilot Agent interaction, and triggering a build. Microsoft assessed that the attack complexity is “high”, and that exploitation is “less likely”.

# Important Vulnerabilities

Talos would also like to highlight the following "important" vulnerabilities as Microsoft has determined that their exploitation is "more likely":

[CVE‑2025‑59512](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-59512) – Customer Experience Improvement Program (CEIP) Elevation of Privilege Vulnerability.

[CVE‑2025‑60705](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-60705) – Windows CSC Service Elevation of Privilege Vulnerability

[CVE-2025-60719](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-60719) - Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability

[CVE-2025-62217](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-62217) - Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability

[CVE-2025-62213](https://m...
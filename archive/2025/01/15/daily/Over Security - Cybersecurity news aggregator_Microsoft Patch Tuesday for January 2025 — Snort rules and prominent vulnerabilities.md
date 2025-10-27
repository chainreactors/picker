---
title: Microsoft Patch Tuesday for January 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/january-patch-tuesday-release/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-15
fetch_date: 2025-10-06T20:12:18.676911
---

# Microsoft Patch Tuesday for January 2025 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for January 2025 — Snort rules and prominent vulnerabilities

By
[Edmund Brumaghin](https://blog.talosintelligence.com/author/edmund-brumaghin/)

Tuesday, January 14, 2025 16:15

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for January of 2025 which includes 159 vulnerabilities, including 12 that Microsoft marked as “critical.” The remaining vulnerabilities listed are classified as “important.”

One notable critically rated vulnerability that has been patched this month is [CVE-2025-21309](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21309), which is a remote code execution vulnerability affecting Windows Remote Desktop Services. Exploitation of this vulnerability could lead to arbitrary code execution on systems where the Remote Desktop Gateway role has been enabled. This vulnerability has been assigned a CVSS 3.1 score of 8.1 and is considered “more likely to be exploited” by Microsoft.

Another notable remote code execution vulnerability in Window Object Linking and Embedding (OLE) was also patched this month. This vulnerability, [CVE-2025-21298](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21298), is a critical remotely exploitable vulnerability that can be triggered by sending a malicious email to a victim running a vulnerable version of Microsoft Outlook. Successful exploitation of this vulnerability could allow an attacker to execute arbitrary code on vulnerable systems and can be triggered when the victim previews the malicious email. This vulnerability has been assigned a CVSS 3.1 score of 9.8. Microsoft recommends disabling RTF as mitigation for this vulnerability.

[CVE-2025-21294](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21294) is a critical vulnerability in Microsoft Digest Authentication that affects multiple versions of Windows and Windows Server. Successful exploitation of this vulnerability could allow an attacker to execute arbitrary code on vulnerable systems. To exploit this vulnerability, an attacker would need to win a race condition.

[CVE-2025-21295](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21295) is a critical remote code execution vulnerability in SPNEGO Extended Negotiation (NEGOEX) Security Mechanism. This vulnerability could allow an attacker to execute arbitrary code on vulnerable systems and does not require user interaction for successful exploitation.

[CVE-2025-21296](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21296) is a critical remote code execution vulnerability in BranchCache. This vulnerability could allow an attacker to execute arbitrary code on vulnerable systems. Microsoft assesses that an attacker would need to be on the same network to successfully exploit this vulnerability.

[CVE-2025-21297](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21297) is another critical remote code execution vulnerability in Windows Remote Desktop Services. Microsoft has assessed that this vulnerability is “less likely to be exploited” and that it would require an attacker to win a race condition for exploitation to be successful. This vulnerability affects multiple versions of Windows Server.

[CVE-2025-21298](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21298) is a critical remote code execution vulnerability in Windows Object Linking and Embedding (OLE). It could allow an attacker to execute arbitrary code on vulnerable systems. Microsoft recommends disabling RTF as a mitigation for this vulnerability.

[CVE-2025-21307](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21307) is a critical remote code execution vulnerability in Windows Reliable Multicast Transport Driver (RMCAST). This vulnerability, if successfully exploited, could enable an unauthenticated attacker to execute arbitrary code by sending a specially crafted packet to vulnerable systems.

[CVE-2025-21311](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21311) is a critical privilege escalation vulnerability in NTLMv1. This vulnerability can be exploited remotely and could allow an attacker to increase their level of access to vulnerable systems. Microsoft recommends disabling the use of NTLMv1 as a mitigation for this vulnerability.

[CVE-2025-21362](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21362) - is a critical remote code execution vulnerability in Microsoft Excel. This vulnerability could allow an attacker to execute arbitrary code on vulnerable systems. This vulnerability can also be triggered via the preview pane.

[CVE-2025-21380](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21380) is a critical information disclosure vulnerability affecting Azure Marketplace SaaS Resources. According to Microsoft this vulnerability, which could enable an attacker to disclose information, has been mitigated.

[CVE-2025-21385](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21385) is a critical information disclosure vulnerability affecting Microsoft Purview. This vulnerability is due to a Server-Side Request Forgery (SSRF) vulnerability that Microsoft reports has been mitigated.

Talos would also like to highlight the following important vulnerabilities that Microsoft considers to be “more likely” to be exploited:

* [CVE-2025-21189](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21189) - MapUrlToZone Security Feature Bypass Vulnerability
* [CVE-2025-21210](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21210) - Windows BitLocker Information Disclosure Vulnerability
* [CVE-2025-21219](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21219) - MapUrlToZone Security Feature Bypass V...
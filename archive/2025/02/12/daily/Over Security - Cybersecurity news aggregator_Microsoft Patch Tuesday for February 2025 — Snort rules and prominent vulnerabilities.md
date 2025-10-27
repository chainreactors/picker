---
title: Microsoft Patch Tuesday for February 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/february-patch-tuesday-release/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-12
fetch_date: 2025-10-06T20:38:01.559007
---

# Microsoft Patch Tuesday for February 2025 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for February 2025 — Snort rules and prominent vulnerabilities

By
[Holger Unterbrink](https://blog.talosintelligence.com/author/holger-unterbrink/)

Tuesday, February 11, 2025 14:24

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for February of 2025 which includes 63 vulnerabilities affecting a range of products, including 4 that Microsoft marked as “critical” and one marked as "moderate."

There are two notable "critical" vulnerabilities. The first is [CVE-2025-21376](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21376), which is a remote code execution (RCE) vulnerability affecting the Windows Lightweight Directory Access Protocol (LDAP). This vulnerability is a remote unauthenticated [Out-of-bounds Write (OOBW)](https://cwe.mitre.org/data/definitions/787.html) caused by a race condition in LDAP and could potentially result in arbitrary code execution in the Local Security Authority Subsystem Service (lsass.exe). This is a process in the Microsoft Windows operating systems that is responsible for enforcing the security policy on the system. Successful exploitation of this vulnerability requires an attacker to win a race condition. [CVE-2025-21376](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21376) has been assigned a CVSS 3.1 score of 8.1 and is considered “more likely to be exploited” by Microsoft.

[CVE-2025-21379](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21379) is another notable critical remote code execution vulnerability. It was found in the DHCP Client Service and was also patched this month. Successful exploitation of this vulnerability could allow an attacker to execute arbitrary code on vulnerable systems. The attacker must inject themselves into the logical network path between the target and the resource requested by the victim to read or modify network communications. This vulnerability has been assigned a CVSS 3.1 score of 7.1 and is considered "less likely to be exploited” by Microsoft.

[CVE-2025-21177](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21177) is a critical privilege escalation vulnerability in the Microsoft Dynamics 365 Sales customer relationship management (CRM) software. A Server-Side Request Forgery (SSRF) allows an authorized attacker to elevate privileges over a network.

[CVE-2025-21381](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21381) is a critical remote code execution vulnerability affecting Microsoft Excel and could enable an attacker to execute arbitrary code on vulnerable systems. This vulnerability could be triggered via the preview pane in affected applications. This vulnerability has been listed "less likely to be exploited" by Microsoft.

[CVE-2025-21368](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21368) and [CVE-2025-21369](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21369) are RCE vulnerabilities flagged "important" by Microsoft. They have a CVS 3.1 score of 8.8. To successfully exploit one of these remote code execution vulnerability, an attacker could send a malicious logon request to the target domain controller. Any authenticated attacker could trigger these vulnerabilities. It does not require admin or other elevated privileges.

[CVE-2025-21400](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21400) is also an RCE vulnerability flagged "important" by Microsoft, affecting the Microsoft SharePoint Server. Successful exploitation of this vulnerability could allow an attacker to execute arbitrary code on vulnerable systems. This attack requires a client to connect to a malicious server and could allow an attacker to gain code execution on the client. Microsoft considers this vulnerability as "more likely to be exploited".

[CVE-2025-21391](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21391) and [CVE-2025-21418](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21418) are the only vulnerabilities this month which are known to be exploited in the wild. Both are privilege elevation vulnerabilities. An attacker can use [CVE-2025-21391](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21391) to delete critical system files. [CVE-2025-21418](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21418), nestled within the Ancillary Function Driver (AFD), exposes a pathway to local privilege escalation through the Winsock API. An attacker who successfully exploits this vulnerability could gain SYSTEM privileges.

Talos would also like to highlight the following vulnerabilities that Microsoft considers to be “important”:

* [CVE-2025-21190](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21190) Windows Telephony Service Remote Code Execution Vulnerability
* [CVE-2025-21198](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21198) Microsoft High Performance Compute (HPC) Pack Remote Code Execution Vulnerability
* [CVE-2025-21200](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21200) Windows Telephony Service Remote Code Execution Vulnerability
* [CVE-2025-21201](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21201) Windows Telephony Server Remote Code Execution Vulnerability
* [CVE-2025-21208](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21208) Windows Routing and Remote Access Service (RRAS) Remote Code Execution Vulnerability
* [CVE-2025-21371](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21371) Windows Telephony Service Remote Code Execution Vulnerability
* [CVE-2025-21406](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21406) Windows Telephony Service Remote Code E...
---
title: Microsoft Patch Tuesday for April 2026 - Snort Rule and Prominent Vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-april-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-14
fetch_date: 2026-04-15T04:43:49.217028
---

# Microsoft Patch Tuesday for April 2026 - Snort Rule and Prominent Vulnerabilities

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

# Microsoft Patch Tuesday for April 2026 - Snort Rule and Prominent Vulnerabilities

By
[Nick Biasini](https://blog.talosintelligence.com/author/nick-biasini/)

Tuesday, April 14, 2026 16:27

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for April 2026, which includes 165 vulnerabilities affecting a wide range of products, including eight Microsoft marked as “critical.”

[CVE-2026-23666](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-23666) is a critical Denial of Service (DoS) vulnerability that affects the .NET framework. Successful exploitation could allow the attacker to deny service over the network.

[CVE-2026-32157](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32157) is a critical use after free vulnerability in the Remote Desktop Client that results in code execution. Attack requires an authorized user on the client to connect to a malicious server, which could result in code execution on the client.

[CVE-2026-32190](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32190) is a critical user after free vulnerability in Microsoft Office that can result in local code execution. Attacker is remote but attack is carried out locally.  Code from the local machine needs to be executed to exploit the vulnerability.

[CVE-2026-33114](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33114) is a critical untrusted pointer deference vulnerability in Microsoft Office Word that could allow the attacker to execute code locally. Code from the local machine needs to be executed to exploit this vulnerability.

[CVE-2026-33115](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33115) is a critical use after free vulnerability in Microsoft Office word that can result in local code execution. Similar to CVE-2026-33114 and CVE-2026-32190 the attacker is remote, but code needs to be executed from the local machine to exploit the vulnerability.

[CVE-2026-33824](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33824) is a critical double free vulnerability in the Widows Internet Key Exchange (IKE) extension, allowing remote code execution. An unauthenticated attacker can send specially crafted packets to a Windows machine with IKE version 2 enabled to potentially enable remote code execution. Additional mitigations can include blocking inbound traffic on UDP ports 500 and 4500 if IKE is not in use.

[CVE-2026-33826](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33826) is a critical improper input validation in Windows Active Directory that can result in code execution over an adjacent network. Requires an authenticated attacker to send specially crafted RPC calls to an RPC host. Can result in remote code execution. Note that successful exploitation requires the attacker be in the same restricted Active Directory domain as the target system.

[CVE-2026-33827](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33827) is a critical race condition vulnerability in Windows TCP/IP that can result in remote code execution. Successful exploitation requires the attacker to win a race condition along with additional actions prior to exploitation to prepare the target environment. An unauthenticated actor can send specially crafted IPv6 packets to a Windows node where IPSec is enabled to potentially achieve remote code execution.

[CVE-2026-32201](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32201) is an important improper input validation vulnerability in Microsoft Office SharePoint that can allow an unauthorized user to perform spoofing. An attacker that successfully exploits this vulnerability could view some sensitive information and make changes to disclosed information. This vulnerability has already been detected as being exploited in the wild.

The majority of the remaining vulnerabilities are labeled as important with a two moderate and one low vulnerability also being patched.  Talos would like to highlight the several additional  important vulnerabilities that Microsoft has deemed as “more likely” to be exploited.

·      [CVE-2026-0390](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-0390) - UEFI Secure Boot Security Feature Bypass Vulnerability

·      [CVE-2026-26151](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26151) - Remote Desktop Spoofing Vulnerability

·      [CVE-2026-26169](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26169) - Windows Kernel Memory Information Disclosure Vulnerability

·      [CVE-2026-26173](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26173) - Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability

·      [CVE-2026-26177](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26177) - Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability

·      [CVE-2026-26182](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26182) - Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability

·      [CVE-2026-27906](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-27906) - Windows Hello Security Feature Bypass Vulnerability

·      [CVE-2026-27908](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-27908) - Windows TDI Translation Driver (tdx.sys) Elevation of Privilege Vulnerability

·      [CVE-2026-27909](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-27909) - Windows Search Service Elevation of Privilege Vulnerability

·      [CVE-2026-27913](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-27913) - Windows BitLocker Security Feature Bypass Vulnerability

·      [CVE-2026-27914](https://msrc.m...
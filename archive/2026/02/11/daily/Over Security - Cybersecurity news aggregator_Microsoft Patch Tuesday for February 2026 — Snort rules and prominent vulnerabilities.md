---
title: Microsoft Patch Tuesday for February 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-february-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-11
fetch_date: 2026-02-12T04:23:07.859374
---

# Microsoft Patch Tuesday for February 2026 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for February 2026 — Snort rules and prominent vulnerabilities

By
[Holger Unterbrink](https://blog.talosintelligence.com/author/holger-unterbrink/)

Tuesday, February 10, 2026 18:54

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for February 2026, which includes 59 vulnerabilities affecting a range of products, including two that Microsoft marked as “Critical”.

[CVE-2026-21522](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21522) is a critical elevation of privilege vulnerability affecting Microsoft ACI Confidential Containers. Successful exploitation of this vulnerability could enable an authorized attacker to escalate privileges on affected systems. This vulnerability is not listed as publicly disclosed and received a CVSS 3.1 score of 6.7.

[CVE-2026-23655](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-23655) is a critical information disclosure vulnerability affecting Microsoft ACI Confidential Containers. This vulnerability could enable an authorized attacker to disclose sensitive information including secret tokens and keys if successfully exploited. This vulnerability is not listed as publicly disclosed and received a CVSS 3.1 score of 6.5.

In this month’s release, Microsoft reported active exploitation of five vulnerabilities rated as "Important". Additionally, one "Moderate" vulnerability, [CVE-2026-21525](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21525), was also listed as being actively exploited. [CVE-2026-21510](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21510), [CVE-2026-21513](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21513), and [CVE-2026-21514](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21514) have also been publicly disclosed.

[CVE-2026-21510](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21510) is a security feature bypass vulnerability affecting Windows Shell. Successful exploitation of this vulnerability could allow an unauthenticated attacker to bypass a security feature on affected systems. This vulnerability could be exploited by convincing a user to open a malicious shortcut or link file, enabling them to bypass Windows SmartScreen and Windows Shell security prompts.

[CVE-2026-21513](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21513) is a security feature bypass vulnerability affecting MSHTML Framework. This vulnerability could be exploited by convincing a user to open a specially crafted HTML or LNK file, allowing an attacker to bypass security features and achieve code execution. This vulnerability received a CVSS 3.1 score of 8.8.

[CVE-2026-21514](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21514) affects Microsoft Office Word and results from reliance on untrusted input, enabling an unauthorized attacker to bypass security protections locally. Exploitation requires user interaction, typically by persuading a user to open a malicious Office document, and may bypass OLE mitigation mechanisms designed to protect against vulnerable COM/OLE controls.

[CVE-2026-21519](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21519) is a type confusion vulnerability in the Desktop Window Manager that allows an authenticated attacker to elevate privileges locally, potentially gaining full SYSTEM-level access.

[CVE-2026-21533](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21533) is an elevation of privilege vulnerability affecting Windows Remote Desktop Services. This vulnerability is due to improper privilege management and could enable an attacker to escalate privileges on affected systems. Successful exploitation of this vulnerability could grant an attacker SYSTEM level privileges on the system.

[CVE-2026-21525](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21525) is a moderate denial-of-service vulnerability affecting Windows Remote Access Connection Manager. This vulnerability is due to a null pointer dereference that could allow an unauthorized attacker to create a denial-of-service condition on affected systems. This vulnerability has not been publicly disclosed and received a CVSS 3.1 rating of 6.2.

Talos would also like to highlight the following "important" vulnerabilities affecting Microsoft Azure, Notepad, various GitHub Copilot components, and Hyper-V.

[CVE-2026-21228](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21228) is an improper certificate validation issue in Azure Local that allows an unauthorized attacker to execute code over the network; successful exploitation may result in a scope change, enabling interaction with other tenants’ applications and data. An attacker could exploit this flaw by intercepting unsecured communication between the configurator application and target systems, tampering with responses to trigger command injection with administrative privileges, and subsequently extracting Azure tokens from application logs to facilitate lateral movement within the cloud environment.

[CVE-2026-20841](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20841) addresses an RCE vulnerability in Microsoft Notepad. This issue could allow an attacker to entice a user into clicking a malicious link within a Markdown file opened in Notepad, resulting in the launch of untrusted protocols that download and execute remote content.

[CVE-2026-21244](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21244) and [CVE-2026-21248](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21248) affect Windows Hyper-V and enable unauthorized attackers ...
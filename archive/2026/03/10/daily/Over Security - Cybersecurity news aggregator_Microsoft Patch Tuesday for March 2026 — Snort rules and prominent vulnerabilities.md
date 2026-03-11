---
title: Microsoft Patch Tuesday for March 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-march-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-10
fetch_date: 2026-03-11T04:05:05.734861
---

# Microsoft Patch Tuesday for March 2026 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for March 2026 — Snort rules and prominent vulnerabilities

By
[Takahiro Takeda](https://blog.talosintelligence.com/author/takahiro/)

Tuesday, March 10, 2026 18:23

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for March 2026 which includes 79 vulnerabilities, including three that Microsoft marked as “critical.” The remaining vulnerabilities listed are classified as “important.” Microsoft assessed that exploitation of the three “critical” vulnerabilities is “less likely.”

[CVE-2026-26110](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26110) and [CVE-2026-26113](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26113) are “critical” Microsoft Office Remote Code Execution Vulnerabilities that could allow an unauthorized attacker to execute code locally; the former is a type confusion issue caused by access to a resource using an incompatible type, and the latter is an untrusted pointer dereference.

[CVE-2026-26144](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26144) is a “critical” information disclosure vulnerability affecting Microsoft Excel. This vulnerability is due to improper neutralization of input in Microsoft Excel which could enable an unauthorized attacker to disclose information on affected systems. This vulnerability has not been previously publicly disclosed or exploited, and Microsoft has rated it as “exploitation unlikely.”

[CVE-2026-26109](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26109) is an “important” vulnerability in Microsoft Office Excel that allows an unauthorized attacker to execute code locally due to an out-of-bounds read. This issue could enable an attacker to compromise the affected system. vulnerability in Microsoft Office Excel that allows an unauthorized attacker to execute code locally due to an out-of-bounds read. This issue could enable an attacker to compromise the affected system.

[CVE-2026-26106](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26106) and [CVE-2026-26114](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26114) are “important” remote code execution vulnerabilities affecting Microsoft SharePoint Server. CVE-2026-26106 is caused by improper input validation in Microsoft Office SharePoint, while CVE-2026-26114 results from deserialization of untrusted data. In both cases, an authenticated attacker with at least Site Member permissions (PR:L) can execute code remotely over a network on the SharePoint Server.

[CVE-2026-26115](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26115), [CVE-2026-26116](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26116), and [CVE-2026-21262](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21262) are “important” elevation of privilege vulnerabilities in SQL Server, each with a CVSS v3.1 highest base score of 8.8. [CVE-2026-26115](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26115) is caused by improper input validation in SQL Server, while [CVE-2026-26116](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26116) is due to improper neutralization of special elements used in a SQL command ('sqlinjection'). [CVE-2026-21262](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21262) results from improper access control in SQL Server. In each case, an authorized attacker could exploit the vulnerability over a network to elevate privileges, potentially gaining administrator privileges. [CVE-2026-21262](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21262) has also been publicly disclosed.

[CVE-2026-26118](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26118) is an elevation of privilege vulnerability in Azure MCP Server Tools with a CVSS v3.1 highest base score of 8.8. It has been rated “important” by Microsoft. This vulnerability is caused by server-side request forgery (SSRF) in Azure MCP Server, which allows an authorized attacker to elevate privileges over a network. An attacker could exploit this issue by sending specially crafted input to an Azure Model Context Protocol (MCP) Server tool that accepts user-provided parameters. If the attacker can interact with the MCP-backed agent, they may submit a malicious URL instead of a standard Azure resource identifier. The MCP Server then sends an outbound request to that URL, possibly includingits managed identity token. The attacker can capture this token without requiring administrative access. A successful attacker could obtain the permissions associated with the MCP Server’s managed identity, enabling access or actions on any resources authorized for that identity. However, the attacker does not gain broader tenant-level or administrator permissions—only those linked to the compromised managed identity.

[CVE-2026-26128](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26128) is an elevation of privilege vulnerability in Windows SMB Server that has been rated “important” by Microsoft. This vulnerability is caused by improper authentication in Windows SMB Server, allowing an authorized attacker to elevate privileges over a network. An attacker who successfully exploits this vulnerability could gain SYSTEM privileges.

Cisco Talos would also like to highlight several vulnerabilities that are only rated as “important,” but Microsoft lists as “more likely” to be exploited:

* [CVE-2026-23668](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-23668) - Windows Graphics Component Elevation of Privilege Vulnerability
* [CVE-2026-24289](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-24289) - Windows Kernel Elevation of Privilege Vulnerability
* [CVE-202...
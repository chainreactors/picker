---
title: Microsoft Patch Tuesday for April 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-april-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-09
fetch_date: 2025-10-06T22:07:14.400195
---

# Microsoft Patch Tuesday for April 2025 — Snort rules and prominent vulnerabilities

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

![](/content/images/2025/04/11_41_27.jpg)

# Microsoft Patch Tuesday for April 2025 — Snort rules and prominent vulnerabilities

By
[Chris Neal](https://blog.talosintelligence.com/author/chris-neal/)

Tuesday, April 8, 2025 14:53

[Patch Tuesday](/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for April of 2025 which includes 126 vulnerabilities affecting a range of products, including 11 that Microsoft marked as “critical”.

In this month's release, none of the included vulnerabilities have been observed by Microsoft to be exploited in the wild. The eleven "critical” entries are all remote code execution (RCE) vulnerabilities, four of which have been marked as "Exploitation more likely".

Two of the “critical” vulnerabilities listed affect components of the Windows Remote Desktop Services.

[CVE-2025-27480](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27480) and [CVE-2025-27482](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27482) are RCE vulnerabilities in components of the Remote Desktop Gateway Service. Both vulnerabilities were given a CVSS 3.1 score of 8.1. To successfully exploit these an attacker could connect to a system with the Remote Desktop Gateway role and trigger a race condition to create a use-after-free scenario, potentially allowing arbitrary code to be executed. Microsoft has assessed that the attack complexity is “high”, and exploitation is “More likely”.

[CVE-2025-26663](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26663) is an RCE vulnerability in the Windows Lightweight Directory Access Protocol (LDAP) and has been given a CVSS 3.1 score of 8.1. This could be exploited by an attacker by sending a specially crafted LDAP call to trigger a use-after-free vulnerability, allowing arbitrary code to be executed in the context of the LDAP service. An attacker could initiate this by sending a victim an email or message containing a malicious link. Microsoft has assessed that exploitation is “more likely” and that the attack complexity is “high”.

[CVE-2025-26670](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26670) is a RCE vulnerability in the Lightweight Directory Access Protocol (LDAP) Client and has been given a CVSS 3.1 base score of 8.1. An attacker could exploit this vulnerability by sending sequential specially crafted LDAP requests to a vulnerable LDAP server. Successful exploitation would require an attacker to win a race condition, which could result in a use-after-free that would allow for arbitrary code execution. Microsoft states that exploitation of this vulnerability is “More likely” and that the attack complexity is “high”.

[CVE-2025-26686](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26686) is an RCE vulnerability in Windows TCP/IP and has been given a CVSS 3.1 base score of 7.5. Due to improperly locked memory in Windows TCP/IP, this vulnerability could allow an attacker to execute arbitrary code over a network. To exploit this an attacker must wait for a user to initiate a connection and send a DHCPv6, to which the attacker would reply with a DHCPv6 response containing a fake IPv6 address. Successful exploitation requires the attacker to win a race condition and make several preparations in the target environment beforehand. Due to this complexity Microsoft has determined that exploitation is "Less likely".

[CVE-2025-27491](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27491) is an RCE vulnerability in Windows Hyper-V and has a CVSS 3.1 base score of 7.1. An attacker with guest privileges on a network could exploit this by convincing a victim to click a link to a malicious site.  Microsoft has determined that exploitation of this vulnerability is “Less likely” and that the attack complexity is “high”.

[CVE-2025-29791](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29791) is an RCE vulnerability in Microsoft Excel and has a CVSS 3.1 base score of 7.8. An attacker could exploit this by sending a specially crafted document to a victim that triggers a type confusion when opened. Once triggered, the type confusion could lead to arbitrary code execution. Microsoft has assessed that exploitation of this vulnerability is "Less likely".

[CVE-2025-27752](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27752) is another RCE vulnerability in Microsoft Excel and has a CVSS 3.1 score of 7.8. This is a heap overflow vulnerability and can be exploited by an attacker to locally execute arbitrary code. It has been assessed that exploitation of this vulnerability is considered "Less likely".

[CVE-2025-27745](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27745), [CVE-2025-27748](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27748) and [CVE-2025-27749](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27749) are RCE vulnerabilities in Microsoft Office and all have a CVSS 3.1 base score of 7.8. These could be exploited by an attacker by triggering a use-after-free scenario, allowing for the execution of arbitrary code. Microsoft has determined that exploitation for each is considered "Less likely".

Talos would also like to highlight the following "important" vulnerabilities as Microsoft has determined that exploitation is "More likely":

* [CVE-2025-27472](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27472) - Windows Mark of the Web Security Feature Bypass Vulnerability
* [CVE-2025-27727](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-27727) - Windows Installer Elevation of Privilege Vulnerability
* [CVE-2025-29792](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29792) - Microsoft Office Elevation of Privilege Vulnerability
* [CVE-2025-29793](https...
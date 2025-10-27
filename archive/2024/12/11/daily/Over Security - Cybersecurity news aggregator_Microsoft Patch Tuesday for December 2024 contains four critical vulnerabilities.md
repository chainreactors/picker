---
title: Microsoft Patch Tuesday for December 2024 contains four critical vulnerabilities
url: https://blog.talosintelligence.com/december-patch-tuesday-release/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-11
fetch_date: 2025-10-06T19:49:24.637160
---

# Microsoft Patch Tuesday for December 2024 contains four critical vulnerabilities

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

# Microsoft Patch Tuesday for December 2024 contains four critical vulnerabilities

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Tuesday, December 10, 2024 15:52

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

The Patch Tuesday for December of 2024 includes 72 vulnerabilities, including four that Microsoft marked as “critical.” The remaining vulnerabilities listed are classified as “important.”

Microsoft assessed that exploitation of the four “critical” vulnerabilities is “less likely.”

[CVE-2024-49112](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49112) is the most serious of this bunch, with a CVSS severity score of 9.8 out of 10. An attacker could exploit this vulnerability in Windows Lightweight Directory Access Protocol (LDAP) calls to execute arbitrary code within the context of the LDAP service. Additionally, [CVE-2024-49124](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49124) and [CVE-2024-49127](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49127) permit an unauthenticated attacker to send a specially crafted request to a vulnerable LDAP server, potentially executing the attacker's code if they succeed in a "race condition." Although the above vulnerabilities are marked as "critical" and with high CVSS, Microsoft has determined that exploitation is "less likely."

[CVE-2024-49126](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49126) - Windows Local Security Authority Subsystem Service (LSASS) remote code execution vulnerability. An attacker with no privileges could target the server accounts and execute malicious code on the server's account through a network call. Despite being considered “critical”, the successful exploitation of this vulnerability requires an attacker to win a “race condition” which complexity is high, Microsoft has determined that exploitation is "less likely."

[CVE-2024-49105](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49105) is a "critical" remote code execution vulnerability in a remote desktop client. Microsoft has assessed exploitation of this vulnerability as "less likely". An authenticated attacker could exploit by triggering remote code execution on the server via a remote desktop connection using Microsoft Management Console (MMC). It has not been detected in the wild.

[CVE-2024-49117](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49117) is a remote code execution vulnerability in Windows Hyper-V. Although marked as "critical," Microsoft has determined that exploitation is "less likely." The exploit needs an authenticated attacker and locally on a guest VM to send specially crafted file operation requests on the VM to hardware resources on the VM and trigger remote code execution on the host server. Microsoft has not detected active exploitation of this vulnerability in the wild.

[CVE-2024-49106](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49106), [CVE-2024-49108](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49108), [CVE-2024-49115](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49115), [CVE-2024-49119](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49119) and [CVE-2024-49120](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49120), [CVE-2024-49123](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49123), [CVE-2024-49132](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49132), [CVE-2024-49116](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49116), [CVE-2024-49128](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49128) are remote code execution vulnerabilities in Windows Remote Desktop Gateway (RD Gateway) Service. An attacker could exploit this by connecting to a system with the Remote Desktop Gateway role, triggering the “race condition” to create a “use-after-free” scenario, and then leveraging the execute arbitrary code. Although marked as "critical," Microsoft has determined that exploitations are "less likely" and the attack complexity considered “high.” Microsoft has not detected active exploitation of these vulnerabilities in the wild.

[CVE-2024-49122](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49122) and [CVE-2024-49118](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49118) are remote code execution vulnerabilities in Microsoft Message Queuing (MSMQ) which is a queue manager in Microsoft Windows system. An attacker would need to send a specially crafted malicious MSMQ packet to a MSMQ server and win the “race condition” that is able to exploit on the server side which also means the attack complexity is “high”. While considered “critical” those were determined that exploitation is “less likely” and not been detected in the wild.

[CVE-2024-49138](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49138) is an elevation of privilege vulnerability in Windows Common Log File System Driver, and while it only has a 7.8 out of 10 CVSS score, it has been actively exploited in the wild.

Cisco Talos would also like to highlight several vulnerabilities that are only rated as “important,” but Microsoft lists as “more likely” to be exploited:

* [CVE-2024-49070](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49070) - Microsoft SharePoint Remote Code Execution Vulnerability
* [CVE-2024-49093](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-49093) - Windows Resilient File System (ReFS) Elevation of Privilege Vulnerability
* [CVE-2024-49088](https://msrc.microsoft.com/update-guide/en-US/vulnerab...
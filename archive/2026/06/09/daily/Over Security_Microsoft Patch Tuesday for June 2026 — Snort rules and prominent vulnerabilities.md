---
title: Microsoft Patch Tuesday for June 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-june-2026-snort-rules-and-prominent-vulnerabilities/
source: Over Security
date: 2026-06-09
fetch_date: 2026-06-10T06:16:50.192621
---

# Microsoft Patch Tuesday for June 2026 — Snort rules and prominent vulnerabilities

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/patch_tuesday.png)

# Microsoft Patch Tuesday for June 2026 — Snort rules and prominent vulnerabilities

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Tuesday, June 9, 2026 17:21

[Patch Tuesday](/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for June 2026, which includes 206 vulnerabilities affecting a range of products, including 32 that Microsoft marked as “critical”.

Out of 32 "critical" entries, 28 are remote code execution (RCE) vulnerabilities in Microsoft Windows services and applications including Windows Active Directory, Windows Kerberos Key Distribution Centre (KDC), Windows Graphics component, Windows Remote Desktop client, Windows Deployment Services (WDS), DHCP Client service, Windows Hyper-V, Windows Kernel and Media, Azure Kubernetes Service (AKS), Microsoft Office, Microsoft Outlook, Microsoft Word, Microsoft SQL server and Windows HTTP Protocol Stack.

Talos highlights 4 critical vulnerabilities as Microsoft has determined that their exploitation is “more likely:”

[CVE-2026-42985](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42985) is a critical Remote Code Execution Vulnerability due to Heap-based buffer overflow in Remote Desktop Client which allows an unauthorized attacker to execute code over a network.

[CVE-2026-47291](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47291) is a critical Remote Code Execution Vulnerability due to Integer overflow or wraparound in Windows HTTP Protocol Stack (http.sys). An unauthenticated attacker could exploit this vulnerability by sending a specially crafted packet to a targeted server utilizing the HTTP Protocol Stack (http.sys) to process packets.

[CVE-2026-44803](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44803) and [CVE-2026-44812](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44812) are critical Remote Code Execution Vulnerability in the Windows Graphics component. This vulnerability is due to Integer overflow or wraparound in Windows Win32K – GRFX subsystem (graphics component). An unauthorized attacker, exploiting this vulnerability can execute malicious code locally.

Talos highlights 23 critical vulnerabilities as Microsoft has determined that their exploitation is “less likely:”

[CVE-2026-42992](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42992), [CVE-2026-44799](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44799), [CVE-2026-44801](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44801), [CVE-2026-47289](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47289) and [CVE-2026-48563](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-48563) are critical Remote Code Execution Vulnerability due to Heap-based buffer overflow in Windows Remote Desktop Client allows an unauthorized attacker to execute code over a network. Successful exploitation of this vulnerability necessitates that an attacker takes additional steps to prepare the target environment before exploitation. In the case of a Remote Desktop connection, an attacker who controls a Remote Desktop Server could initiate a remote code execution (RCE) on the machine when a victim connects to the attacking server using the vulnerable Remote Desktop Client.

[CVE-2026-45607](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45607), [CVE-2026-45641](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45641) and [CVE-2026-47652](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47652) are critical Remote Code Execution vulnerabilities in Windows Hyper-V that arise from Out-of-bounds reads, which enable an unauthorized attacker to execute code locally. This vulnerability necessitates that an authenticated attacker on a guest virtual machine (VM) sends specially crafted file operation requests to hardware resources within the VM which could result in remote code execution on the host server.

[CVE-2026-45657](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45657) is a critical use after free vulnerability in Windows Kernel which allows an unauthorized attacker to execute malicious code over a network. An attacker could exploit this vulnerability by sending specially crafted network traffic to a vulnerable Windows system. With the successful exploitation attempt, the malicious network packets could trigger a flaw in how the Windows kernel processes certain TCP/IP data, potentially allowing the attacker to run code with system-level privileges without needing to sign in or interact with a user.

[CVE-2026-48574](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-48574) is a critical Remote Code Execution vulnerability in Windows Media due to Heap-based buffer overflow which allows an unauthorized attacker to execute the malicious code locally.

[CVE-2026-42987](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42987) is a critical Remote Code Execution vulnerability in Windows Deployment Services (WDS). This vulnerability is due to the use after free flaw in Windows Deployment Services and an unauthorized attacker, exploiting this vulnerability, can execute malicious code over a network.

[CVE-2026-44815](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44815) is a critical Remote Code Execution vulnerability due to the Stack-based buffer overflow in Windows DHCP Client which allows an unauthorized attacker to execute code over a network. An authenticated user could exploit this vulnerability by sending specially crafted network traffic to a server configured for use as a Dynamic Host Configuration Protocol (DHCP) Server.

[CVE-2026-4...
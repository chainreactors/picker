---
title: Microsoft Patch Tuesday for August 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-august-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-13
fetch_date: 2025-10-07T00:48:26.629789
---

# Microsoft Patch Tuesday for August 2025 — Snort rules and prominent vulnerabilities

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

![](/content/images/2025/08/patch-tues.jpg)

# Microsoft Patch Tuesday for August 2025 — Snort rules and prominent vulnerabilities

By
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/)

Tuesday, August 12, 2025 15:39

[Patch Tuesday](/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for August 2025, which includes 111 vulnerabilities affecting a range of products, including 13 that Microsoft marked as “critical”.

In this month's release, Microsoft observed none of the included vulnerabilities being actively exploited in the wild. Out of 13 "critical" entries, 9 are remote code execution (RCE) vulnerabilities in Microsoft Windows services and applications including the Windows kernel, Microsoft Message Queuing (MSMQ), Windows Hyper-V, Microsoft Office and GDI+.

[CVE-2025-50176](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-50176) is an RCE vulnerability in DirectX Graphics Kernel given a CVSS 3.1 score of 7.8, where access of resource using incompatible type ('type confusion') in Graphics Kernel allows an authorized attacker to execute code locally. Microsoft has noted that this vulnerability affects different versions of Windows 11, Windows Server 2022 and Windows Server 2025. Microsoft assessed that the attack complexity is “low”, and that exploitation is "more likely".

[CVE-2025-50177](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-50177) is an RCE vulnerability in Microsoft Message Queuing (MSMQ) service, given a CVSS score of 8.1, where use after free vulnerability allows an unauthorized attacker to execute code over a network. To exploit this vulnerability, an attacker would need to send a series of specially crafted MSMQ packets in arapid sequence over HTTP to a MSMQ server. Microsoft assessed that the attack complexity is “high”, and that exploitation is “more likely”.

[CVE-2025-53778](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-53778) is a Windows NTLM elevation of privilege vulnerability given a CVSS 3.1 base score of 8.8, where improper authentication in Windows NTLM allows an authorized attacker to elevate privileges over a network, with an attacker successfully exploiting this vulnerability gaining SYSTEM privileges. Microsoft has noted that this vulnerability affects different versions of Windows 10, Windows 11, Windows server 2008, Windows Server 2012, Windows Server 2026, Windows Server 2019, Windows Server 2022 and Windows Server 2025. Microsoft assessed that the attack complexity is “low”, and that exploitation is “more likely”.

[CVE-2025-53781](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-53781) is an information disclosure vulnerability in Windows Hyper-V given a CVSS 3.1 base score of 7.7, where an authorized attacker may be able to disclose sensitive information over a network. Microsoft has noted that this vulnerability affects Windows Server 2025 with the attack complexity assessed as “low” and that exploitation as “less likely”.

[CVE-2025-53733](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-53733) is a remote code execution vulnerability in Microsoft Word given a CVSS 3.1 base score of 8.4 where an incorrect conversion between numeric types in Microsoft Office Word allows an unauthorized attacker to execute code locally. Microsoft has noted that this vulnerability affects Word 2016, Microsoft SharePoint Server 2019, Microsoft SharePoint Enterprise Server 2016, Microsoft Office LTSC 2024, Microsoft Office LTSC 2021, Microsoft Office LTSC 2019 and Microsoft 365 Apps for Enterprise. Microsoft assessed that the attack complexity is “low”, and that exploitation is “less likely”.

[CVE-2025-53740](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-53740) is a remote code execution vulnerability in Microsoft Office, given a CVSS 3.1 base score of 8.4 where a use after free condition allows an unauthorized attacker to execute code locally using a Preview Pane as the attack vector. Microsoft has noted that this vulnerability affects Microsoft Office LTSC for Mac 2024, Microsoft Office LTSC for Mac 2021, Microsoft Office LTSC 2024, Microsoft Office LTSC 2021, Microsoft Office LTSC 2019, Microsoft Office LTSC 2016 and Microsoft 365 Apps for Enterprise. Microsoft assessed that the attack complexity is “low”, and that exploitation is “less likely”.

[CVE-2025-53766](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-53766) is a remote code execution vulnerability in GDI+, a graphics Windows subsystem providing a set of features for rendering 2D graphics, images, and text, given a CVSS 3.1 base score of 9.8 where a heap-based buffer overflow allows an unauthorized attacker to execute code over a network. An attacker could trigger this vulnerability by convincing a victim to download and open a document that contains a specially crafted metafile. Microsoft has noted that this vulnerability affects various versions of Windows 10, Windows 11 and Windows Server 2008. Microsoft assessed that the attack complexity is “low”, and that exploitation is “less likely”.

[CVE-2025-50165](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-50165) is another remote code execution vulnerability in the Windows graphics component. It was also given a CVSS 3.1 base score of 9.8 where an untrusted pointer dereference allows an unauthorized attacker to execute code over a network without any user intervention. An attacker can use an uninitialized function pointer being called when decoding a JPEG image. This can be embedded in Office and 3rd party documents/files. This vulnerability affects Windows 11 24H2 and Windows Server 2025. Microsoft assessed that the attack complexity is “low”, and that exploitation is “less li...
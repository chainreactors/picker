---
title: ToolShell: Details of CVEs Affecting SharePoint Servers
url: https://blog.talosintelligence.com/toolshell-affecting-sharepoint-servers/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-22
fetch_date: 2025-10-06T23:49:27.018079
---

# ToolShell: Details of CVEs Affecting SharePoint Servers

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

![](/content/images/2025/07/threat-advisory-1.jpg)

# ToolShell: Details of CVEs affecting SharePoint servers

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Monday, July 21, 2025 16:33

[Threat Advisory](/category/threat-advisory/)

*Update 2025/07/22: Microsoft has released a security update for Sharepoint Enterprise Server 2016. The update, with the ID KB5002760, is available in the following* [*link*](https://www.microsoft.com/en-us/download/details.aspx?id=108288)*.*

Cisco Talos is aware of the ongoing exploitation of [CVE-2025-53770](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53770) and [CVE-2025-53771](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53771) in the wild. These are path traversal vulnerabilities affecting SharePoint Server Subscription Edition, SharePoint Server 2016, and SharePoint Server 2019. According to Microsoft, these vulnerabilities do not affect SharePoint Online in Microsoft 365 and only apply to on-premises SharePoint servers.

Microsoft has also [released](https://msrc.microsoft.com/blog/2025/07/customer-guidance-for-sharepoint-vulnerability-cve-2025-53770/) security updates and mitigation guidance for multiple affected products. The update for Sharepoint Server 2016 has also been [released](https://www.microsoft.com/en-us/download/details.aspx?id=108288).

These two vulnerabilities, [CVE-2025-53770](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53770) / [CVE-2025-53771](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53771), are related to [CVE-2025-49704](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49704) and [CVE-2025-49706](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49706), which were featured in the July Microsoft Patch Tuesday updates. The new updates that Microsoft has published provide more comprehensive protection against exploitation attempts targeting these vulnerabilities. In addition to installing the updates provided by Microsoft, they are also recommending users rotate the SharePoint Server ASP.NET machine keys to ensure data integrity. The Cybersecurity Infrastructure Security Agency (CISA) has also [released](https://www.cisa.gov/news-events/alerts/2025/07/20/microsoft-releases-guidance-exploitation-sharepoint-vulnerability-cve-2025-53770) additional details and technical indicators associated with ongoing exploitation attempts targeting unprotected SharePoint servers between July 18 – 19, 2025.

## Vulnerability details

These are both unauthenticated remote code execution vulnerabilities related to [CVE-2025-49704](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49704) and [CVE-2025-49706](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49706). One of the key features of the previous vulnerabilities is that the user needed to be authenticated to obtain a valid signature by extracting the ValidationKey from memory or configuration. In the case of [CVE-2025-53770](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53770) and [CVE-2025-53771](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53771), attackers have managed to eliminate the need to be authenticated to obtain a valid signature, resulting in unauthenticated remote code execution.

Patches have already been provided by Microsoft for most versions of SharePoint Server. As an alternative option, Microsoft has recommended that the Antimalware Scan Interface (AMSI) is turned on and configured correctly with the associated antivirus solution.

Once patches are applied, Microsoft also recommends that users rotate their SharePoint Server ASP.NET machine keys in case the signing keys were compromised in the attack. This can be done both manually [via Powershell and via Central Admin](https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/improved-asp-net-view-state-security-key-management).

## Coverage

As part of our coverage of the July Microsoft Patch Tuesday release on July 8, 2025, Talos previously published Snort SID 65092 to provide detection for exploitation attempts targeting CVE-2025-49704. We have investigated the new details provided by Microsoft as well as open-source information related to ongoing reports of exploitation activity targeting these vulnerabilities and have confirmed that the existing coverage remains effective at this time. Additionally Talos has published Snort SID 65183 to provide detection for the webshell being deployed in the current campaigns.

ClamAV detections: Asp.Webshell.SharpyShell-10056352-3

The Splunk Threat Research Team has developed detection analytics targeting CVE-2025-53770 exploitation attempts and post-compromise activities. The security content includes rules to detect suspicious SharePoint requests to the vulnerable ToolPane endpoint and the characteristic authentication bypass patterns observed in ToolShell campaigns.

Additionally, the detection content covers post-exploitation behaviors including malicious PowerShell execution, suspicious child processes spawned by w3wp.exe (SharePoint worker processes), and SharePoint-specific indicators like the creation of spinstall0.aspx web shells. These analytics provide security teams with comprehensive visibility into both initial exploitation attempts and subsequent attacker activities, enabling faster detection and response to ToolShell compromises. The analytics can be found at <https://research.splunk.com/>

### Related existing BP Rules:

Malicious Process Creation By Microsoft Exchange Server lIS triggers on creation of the webshell payload

![A screenshot of a computer  Description automatically generated, Picture](https://blog.talosintelligence.com/content/images/2025/07/data-src-image-3e06ba30-ad0b-498e-ab83-a721c49917c4.jpeg)
...
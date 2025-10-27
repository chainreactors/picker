---
title: Microsoft Patch Tuesday for May 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-may-2025-snort-rules-and-prominent-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-14
fetch_date: 2025-10-06T22:29:45.356531
---

# Microsoft Patch Tuesday for May 2025 — Snort rules and prominent vulnerabilities

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

![](/content/images/2025/05/patch-tues.jpg)

# Microsoft Patch Tuesday for May 2025 — Snort rules and prominent vulnerabilities

By
[Jaeson Schultz](https://blog.talosintelligence.com/author/jaeson-schultz/)

Tuesday, May 13, 2025 16:38

[Patch Tuesday](/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for May of 2025 which includes 78 vulnerabilities affecting a range of products, including 11 that Microsoft marked as “critical”.

Microsoft noted five vulnerabilities that have been observed to be exploited in the wild. [CVE-2025-30397](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30397) is a remote code execution vulnerability in the Microsoft Scripting Engine. There were also four elevation of privilege vulnerabilities being actively exploited, [CVE-2025-32709](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-32709), [CVE-2025-30400](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30400), [CVE-2025-32701](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32701) and [CVE-2025-32706](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-32706) affecting the Ancillary Function Driver for WinSock, the DWM Core Library and the Windows Common Log File System Driver.

The eleven "critical” entries consist of five remote code execution (RCE) vulnerabilities, four elevation of privilege vulnerabilities, one information disclosure vulnerability and one spoofing vulnerability. Three of the critical vulnerabilities have been marked as "Exploitation more likely": [CVE-2025-30386](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30386) --a Microsoft Office RCE vulnerability, [CVE-2025-30390](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30390) --an Azure ML Compute elevation of privilege vulnerability, and [CVE-2025-30398](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30398) – a Nuance PowerScribe 360 information disclosure vulnerability.

The most notable of the “critical” vulnerabilities listed affect Microsoft Office. [CVE-2025-30386](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30386) is a RCE vulnerability with base CVSS 3.1 score of 8.3. To successfully exploit CVE-2025-30386, an attacker could send a victim an email, and without the victim clicking the link, viewing or interacting with the email, trigger a use-after-free scenario, allowing arbitrary code to be executed. Microsoft has assessed that the attack complexity is “Low”, and exploitation is “More likely”. Another RCE vulnerability affecting Microsoft Office, [CVE-2025-30377](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-30377), has a CVSS 3.1 base score of 8.4, and has been assessed an attack complexity of “Low”, but exploitation is considered “Less Likely”.

Two RCE vulnerabilities affect the Remote Desktop Client. [CVE-2025-29966](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29966) and [CVE-2025-29967](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29967) are both Heap-cased Buffer Overflow vulnerabilities with CVSS 3.1 base scores of 8.8 with “Low” attack complexity and exploitation “Less Likely”. An attacker controlling a Remote Desktop Server could trigger the buffer overflow in a vulnerable when a vulnerable Remote Desktop Client connects to the server.

[CVE-2025-29833](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29833) is a RCE affecting the Virtual Machine Bus. This is a Time-of-check Time-of-use (TOCTOU) Race Condition which has been assessed an attack complexity of “High” and exploitation is “Less Likely”.

Talos would also like to highlight the following "important" vulnerabilities as Microsoft has determined that exploitation is "More likely":

* CVE-2025-24063 - Kernel Streaming Service Driver Elevation of Privilege Vulnerability
* CVE-2025-29841 - Universal Print Management Service Elevation of Privilege Vulnerability
* CVE-2025-29971 - Web Threat Defense (WTD.sys) Denial of Service Vulnerability
* CVE-2025-29976 - Microsoft SharePoint Server Elevation of Privilege Vulnerability
* CVE-2025-30382 - Microsoft SharePoint Server Remote Code Execution Vulnerability
* CVE-2025-30385 - Windows Common Log File System Driver Elevation of Privilege Vulnerability
* CVE-2025-30388 - Windows Graphics Component Remote Code Execution Vulnerability

A complete list of all the other vulnerabilities Microsoft disclosed this month is available on its [update page](https://msrc.microsoft.com/update-guide/).

In response to these vulnerability disclosures, Talos is releasing a new Snort rule set that detects attempts to exploit some of them. Please note that additional rules may be released at a future date and current rules are subject to change pending additional information. Cisco Security Firewall customers should use the latest update to their ruleset by updating their SRU. Open-source Snort Subscriber Rule Set customers can stay up to date by downloading the latest rule pack available for purchase on [Snort.org.](https://snort.org/)

The rules included in this release that protect against the exploitation of many of these vulnerabilities are 64848-64867. There are also these Snort 3 rules: 64852-64853, 301192-301200, and 301203

##### Share this post

#### Related Content

[### Microsoft Patch Tuesday for September 2025 – Snort rules and prominent vulnerabilities

September 9, 2025 15:12

Microsoft has released its monthly security update for September 2025, which includes 86 vulnerabilities affecting a range of products.](/microsoft-patch-tuesday-september-2025/)

[### Microsoft Patch Tuesday for August 2025 — Snort rules and prominent vulnerabilities

August 12, 2025 15:39

Microsoft has released its monthly security update ...
---
title: Four zero-days included in group of 79 vulnerabilities Microsoft discloses, including one with 9.8 severity score
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-september-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-11
fetch_date: 2025-10-06T18:32:17.165585
---

# Four zero-days included in group of 79 vulnerabilities Microsoft discloses, including one with 9.8 severity score

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

# Four zero-days included in group of 79 vulnerabilities Microsoft discloses, including one with 9.8 severity score

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Tuesday, September 10, 2024 15:30

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft disclosed four vulnerabilities that are actively being exploited in the wild as part of its regular Patch Tuesday security update this week in what’s become a regular occurrence for the company’s patches in 2024.

Two of the zero-day vulnerabilities, [CVE-2024-38226](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38226) and [CVE-2024-38014,](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38014) exist in the Microsoft Publisher software and Windows Installer, respectively. Last month, Microsoft [disclosed six vulnerabilities](https://blog.talosintelligence.com/microsoft-patch-tuesday-august-2024/) in its Patch Tuesday that were already being exploited in the wild.

In all, September’s monthly round of patches from Microsoft included 79 vulnerabilities, seven of which are considered critical. In addition to the zero-days disclosed Tuesday, Microsoft also fixed a security issue that had already been publicly disclosed: [CVE-2024-38217](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38217), a vulnerability in Windows Mark of the Web that could allow an adversary to bypass usual MOTW detection techniques.

Cisco Talos’ Vulnerability Research team also discovered [an information disclosure vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38257) in the AllJoyn API that could allow an adversary to access uninitialized memory. [CVE-2024-38257](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38257) is considered “less likely” to be exploited, though it does not require any user interaction or user privileges.

The most serious of the issues included in September’s Patch Tuesday is [CVE-2024-43491,](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43491) which has a severity score of 9.8 out of 10. CVE-2024-43491, a remote code execution issue in Windows Update, is considered “more likely” to be exploited, though Microsoft disclosed few details about the nature of this vulnerability.

There are also four remote code execution vulnerabilities in SharePoint Server that are also considered “more likely” to be exploited: [CVE-2024-38018](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38018), [CVE-2024-38227](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38227), [CVE-2024-38228](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38228) and [CVE-2024-43464](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43464).

In the case of the latter three vulnerabilities, an authenticated attacker with Site Owner permissions can inject arbitrary code and execute code in the context of SharePoint Server. However, an attacker only needs to have Site Member permissions to exploit CVE-2024-38018.

CVE-2024-38226, one of the zero-days disclosed this week, is a security feature bypass vulnerability in Microsoft Publisher that could allow an attacker to bypass the default Microsoft Office macro policies used to block untrusted or malicious files. An adversary could exploit this vulnerability by tricking a user into opening a specially crafted, malicious file in Microsoft Publisher, which could lead to a local attack on the victim’s machine. Macros have been [blocked by default on Office](https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked) software to prevent attackers from hiding malicious code in them.

Another vulnerability being actively exploited in the wild, CVE-2024-38014, is an issue in Windows Installer that could allow an adversary to gain SYTEM-level privileges. This issue affects Windows 11, version 24H2, which is currently only available on certain Microsoft Copilot+ devices, among other older versions of Windows 10 and 11.

A complete list of all the other vulnerabilities Microsoft disclosed this month is available on its [update page](https://portal.msrc.microsoft.com/en-us/security-guidance).

In response to these vulnerability disclosures, Talos is releasing a new Snort rule set that detects attempts to exploit some of them. Please note that additional rules may be released at a future date and current rules are subject to change pending additional information. Cisco Security Firewall customers should use the latest update to their ruleset by updating their SRU. Open-source Snort Subscriber Rule Set customers can stay up to date by downloading the latest rule pack available for purchase on [Snort.org](https://snort.org/advisories/talos-rules-2024-08-13).

The rules included in this release that protect against the exploitation of many of these vulnerabilities are 63979 - 63984 and 63987 - 63994. There are also Snort 3 rules 301008 - 301013.

##### Share this post

#### Related Content

[### Microsoft Patch Tuesday for September 2025 – Snort rules and prominent vulnerabilities

September 9, 2025 15:12

Microsoft has released its monthly security update for September 2025, which includes 86 vulnerabilities affecting a range of products.](/microsoft-patch-tuesday-september-2025/)

[### Microsoft Patch Tuesday for August 2025 — Snort rules and prominent vulnerabilities

August 12, 2025 15:39

Microsoft has released its monthly security update for August 2025, which includes 111 vulnerabilities affecting a range of products, including 13 that Microsoft marked as “critical”.](/microsoft-patch-tuesday-august-2025/)

[### Microsoft Patch Tuesday for July 2025 — Snort rules and prominent vulnerabilities

July 8, 2025 16:29

Microsoft has released ...
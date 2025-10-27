---
title: Talos discovers Microsoft kernel mode driver vulnerabilities that could lead to SYSTEM privileges; Seven other critical issues disclosed
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-august-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-14
fetch_date: 2025-10-06T18:04:42.019995
---

# Talos discovers Microsoft kernel mode driver vulnerabilities that could lead to SYSTEM privileges; Seven other critical issues disclosed

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

# Talos discovers Microsoft kernel mode driver vulnerabilities that could lead to SYSTEM privileges; Seven other critical issues disclosed

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/),
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/)

Tuesday, August 13, 2024 15:12

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft disclosed six security vulnerabilities that are actively being exploited across its products as part of the company’s regular Patch Tuesday security update.

In all, August’s monthly round of patches from Microsoft included 87 vulnerabilities, seven of which are considered critical. In addition to the zero-days disclosed Tuesday, Microsoft also fixed a security issue that had already been publicly disclosed: [CVE-2024-21302](https://nvd.nist.gov/vuln/detail/CVE-2024-21302), a vulnerability in Microsoft Office that could result in unauthorized disclosure of sensitive information to malicious actors. Microsoft initially warned about the possibility that [attackers could exploit this vulnerability](https://www.helpnetsecurity.com/2024/08/08/windows-downgrade-attack/) in the wild last week, including being able to reverse older software patches that could re-open them to past vulnerabilities.

Cisco Talos’ Vulnerability Research team discovered four of the vulnerabilities Microsoft patched this week: [CVE-2024-38184](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38184), [CVE-2024-38185](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38185), [CVE-2024-38186](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38186) and [CVE-2024-38187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38187). These are elevation of privilege vulnerabilities in the Microsoft Windows kernel-mode driver that could allow an attacker to gain SYSTEM-level privileges.

The most serious of the issues included in August’s Patch Tuesday is [CVE-2024-38063](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38063), a remote code execution vulnerability in Windows TCP/IP. An unauthenticated attacker could exploit this vulnerability by repeatedly sending specially crafted IPv6 packets to a targeted Windows machine that could enable remote code execution. Systems that have IPv6 disabled are not susceptible to this vulnerability.

CVE-2024-38063 has a severity score of 9.8 out of 10 and is listed as “more likely” to be exploited.

Two other remote code execution vulnerabilities, [CVE-2024-38159](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38159) and [CVE-2024-38160](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38160), exist in Windows Network Virtualization, and another, [CVE-2024-38140,](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38140) exists in the Windows Reliable Multicast Transport Driver. All three are considered critical.

Two of the vulnerabilities already being exploited in the wild are [CVE-2024-38178](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38178), a memory corruption vulnerability in the Microsoft Scripting Engine, and [CVE-2024-38193](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38193), an elevation of privilege vulnerability in the Windows Ancillary Function Driver. Though they are both zero-days, Microsoft only lists them as being “important.”

Lastly, we’d also like to highlight two vulnerabilities in the Secure Boot security feature, [CVE-2024-38090](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38090) and [CVE-2024-28918](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-28918), which are rated critical and important, respectively.

A complete list of all the other vulnerabilities Microsoft disclosed this month is available on its [update page](https://portal.msrc.microsoft.com/en-us/security-guidance).

In response to these vulnerability disclosures, Talos is releasing a new Snort rule set that detects attempts to exploit some of them. Please note that additional rules may be released at a future date and current rules are subject to change pending additional information. Cisco Security Firewall customers should use the latest update to their ruleset by updating their SRU. Open-source Snort Subscriber Rule Set customers can stay up to date by downloading the latest rule pack available for purchase on [Snort.org](https://snort.org/advisories/talos-rules-2024-08-13).

The rules included in this release that protect against the exploitation of many of these vulnerabilities are 63858 – 63861 and 63864 - 63878. There are also Snort 3 rules 300980 – 300988.

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

Microsoft has released its monthly security update for July 2025, which includes 132 vulnerabilities affecting a range of products, including 14 that Microsoft marked as “critical.”](/microsoft-patch-tuesday-july-2025/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](http...
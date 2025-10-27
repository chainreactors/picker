---
title: Largest Patch Tuesday in 3 months includes 5 critical vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-july-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-10
fetch_date: 2025-10-06T17:47:01.934877
---

# Largest Patch Tuesday in 3 months includes 5 critical vulnerabilities

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

# Largest Patch Tuesday in 3 months includes 5 critical vulnerabilities

By
[Tiago Pereira](https://blog.talosintelligence.com/author/tiago-pereira/)

Tuesday, July 9, 2024 14:01

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft released its monthly security update on Tuesday, disclosing 142 vulnerabilities across its suite of products and software. Of those, there are five critical vulnerabilities, and every other security issue disclosed this month is considered "important."

This is the largest Patch Tuesday [since April](https://blog.talosintelligence.com/patch-tuesday-april-2024/) when Microsoft patched 150 vulnerabilities.

Of the critical vulnerabilities, two are considered more likely to be exploited:

[CVE-2024-38023](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38023), a remote code execution vulnerability in Microsoft SharePoint server, where an authenticated attacker with Site Owner permissions can use the vulnerability to execute arbitrary code in the context of SharePoint server.

[CVE-2024-38060](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38060), a remote code execution vulnerability in Microsoft Windows Codecs Library that can be exploited by an authenticated attacker who uploads a specially crafted malicious TIFF file.

There are three other critical vulnerabilities listed in this advisory. All three ([CVE-2024-38074](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38074), [CVE-2024-38076](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38076) and [CVE-2024-38077](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38077)) are remote code execution vulnerabilities in Windows Remote Desktop Licensing Service. In all of them, an attacker could send a specially crafted network packet which could cause remote code execution. In the case of CVE-2024-38077, the adversary does not need to be authenticated.

All the remaining vulnerabilities are considered important. Of these, [CVE-2024-38080](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38080) is particularly relevant because Microsoft has acknowledged that it’s already being exploited in the wild. An adversary could exploit this elevation of privilege vulnerability in Windows Hyper-V to gain System privileges.

Cisco Talos' Vulnerability Research team discovered another elevation of privilege vulnerability, [CVE-2024-38062](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38062), in the kernel-mode driver. An adversary could also exploit this vulnerability to gain System privileges. Microsoft considers the complexity of this attack to be "low," though it's "less likely" to be exploited.

Several other “important” vulnerabilities could lead to remote code execution and are identified by Microsoft as being “more likely” to be exploited.

[CVE-2024-38021](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38021) is a remote code execution vulnerability in Microsoft Office. An attacker could craft a malicious link that bypasses the Protected View Protocol, leading to the leaking of local NTLM credentials and remote code execution.

[CVE-2024-38024](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38024) is a remote code execution vulnerability in Microsoft SharePoint Server. An adversary could exploit this issue by uploading a specially crafted file to the targeted SharePoint Server and crafting specialized API requests to trigger the deserialization of a file's parameters, leading to arbitrary code execution in the context of the SharePoint server. However, this attacker would need to have Site Owner permissions or higher.

[CVE-2024-38094](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38094) is another vulnerability in SharePoint servers. Adversaries with Site Owner permissions can use this vulnerability to inject arbitrary code and execute code in the context of a SharePoint server.

A complete list of all the vulnerabilities Microsoft disclosed this month is available on its [update page](https://msrc.microsoft.com/update-guide/).

In response to these vulnerability disclosures, Talos is releasing a new Snort rule set that detects attempts to exploit some of them. Please note that additional rules may be released at a future date, and current rules are subject to change pending additional information. Cisco Secure Firewall customers should use the latest update to their rule set by updating their SRU. Open-source Snort Subscriber Rule Set customers can stay up-to-date by downloading the latest rule pack available for purchase on Snort.org.

The rules included in this release that protect against the exploitation of many of these vulnerabilities are 63687 - 63690, 63693, 63694 and 63697 - 63700. There are also Snort 3 rules 300958 - 300961.

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

Microsoft has released its monthly security update for July 2025, which includes 132 vulnerabilities affecting a range of products, including 14 that Microsoft marke...
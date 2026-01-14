---
title: Microsoft Patch Tuesday for January 2026 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-january-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-13
fetch_date: 2026-01-14T03:35:43.530752
---

# Microsoft Patch Tuesday for January 2026 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for January 2026 — Snort rules and prominent vulnerabilities

By
[Edmund Brumaghin](https://blog.talosintelligence.com/author/edmund-brumaghin/)

Tuesday, January 13, 2026 13:29

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for January 2026, which includes 112 vulnerabilities affecting a range of products, including 8 that Microsoft marked as “critical”.

In this month's release, Microsoft observed one of the included “important” vulnerabilities, [CVE-2026-20805](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20805), as being exploited in the wild. Out of 8 "critical" entries, 6 are remote code execution (RCE) vulnerabilities in Microsoft Windows services and applications including Windows Local Security Authority Subsystem Service (LSASS), Microsoft Word, Microsoft Excel, and Microsoft Office. The two remaining “critical” entries are elevation of privilege (EoP) vulnerabilities affecting Windows Graphic Component and Windows Virtualization-Based Security (VBS) Enclave.

[CVE-2026-20822](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20822) is a critical elevation of privilege vulnerability affecting Windows Graphic Component. This vulnerability is due to a use-after-free (UAF) bug that could enable an attacker to obtain SYSTEM privileges on affected systems if exploited. This vulnerability was issued a CVSS 3.1 base score of 7.8 and would require an attacker to successfully win a race condition to achieve successful exploitation. Microsoft has assessed that exploitation of this vulnerability is “less likely” and that it has not been publicly disclosed.

[CVE-2026-20854](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20854) is a critical remote code execution vulnerability affecting Windows Local Security Authority Subsystem Service (LSASS). This vulnerability was issued a CVSS 3.1 base score of 7.5 and could enable an authorized attacker the ability to execute code on affected systems over a network. Successful exploitation of this vulnerability does not require elevated privileges. Microsoft has assessed that this vulnerability is “less likely” to be exploited and that it has not been publicly disclosed.

[CVE-2026-20876](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20876) is a critical elevation of privilege vulnerability affecting Windows Virtualization-Based Security (VBS) Enclave. This vulnerability is due to a heap-based buffer overflow that could enable local privilege elevation if successfully exploited by an authorized attacker. Successful exploitation of this vulnerability could grant an attacker Virtual Trust Level 2 (VTL2) privileges on affected systems. This vulnerability was issued a CVSS 3.1 base score of 6.7 and has been assessed by Microsoft to be “less likely” to be exploited and has not been publicly disclosed.

[CVE-2026-20944](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20944) is a critical remote code execution vulnerability affecting Microsoft Word. This vulnerability is due to an out-of-bounds read and could enable an attacker to execute arbitrary code on affected systems. To exploit this vulnerability, an attacker would need to convince victims to open a specially crafted malicious file on a vulnerable system. This vulnerability was issued a CVSS 3.1 base score of 7.8. Microsoft has assessed that this vulnerability is “less likely” to be exploited and has not been publicly disclosed.

[CVE-2026-20952](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20952) and [CVE-2026-20953](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20953) are critical remote code execution vulnerabilities affecting Microsoft Office. These vulnerabilities are due to user-after-free conditions and could enable an unauthorized attacker to execute arbitrary code on affected systems. To successfully exploit either of these vulnerabilities, an attacker would need to log on and run a specially crafted application or convince a victim to open a malicious file on affected systems. Both vulnerabilities were issued a CVSS 3.1 base score of 8.4. Microsoft has assessed that these vulnerabilities are “less likely” to be exploited and neither were publicly disclosed.

[CVE-2026-20955](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20955) is a critical remote code execution vulnerability affecting Microsoft Excel. This vulnerability is due to an untrusted pointer reference and could be leveraged by an unauthorized attacker to execute arbitrary code on affected systems. To successfully exploit this vulnerability, an attacker would need to convince a victim to open a specially crafted malicious file. This vulnerability was issued a CVSS 3.1 base score of 7.8 and was assessed by Microsoft to be “less likely” to be exploited. Microsoft has also noted that this vulnerability has not been publicly disclosed.

[CVE-2026-20957](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20957) is a critical remote code execution vulnerability affecting Microsoft Excel. This vulnerability is due to an integer underflow that could be leveraged by an unauthorized attacker to execute arbitrary code on affected systems. To successfully exploit this vulnerability, an attacker would need to convince a victim to open a specially crafted malicious file. This vulnerability was issued a CVSS 3.1 base score of 7.8 and was assessed by Microsoft to be “less likely” to be exploited. Microsoft has also noted that this vulnerability has not been publicly disclosed.

[CVE-2026-20805](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-20805) is an important informatio...
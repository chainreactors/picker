---
title: Microsoft Patch Tuesday for December 2025 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-december-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-09
fetch_date: 2025-12-10T03:22:40.509224
---

# Microsoft Patch Tuesday for December 2025 — Snort rules and prominent vulnerabilities

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

![](/content/images/2025/12/patch-tuesday.jpg)

# Microsoft Patch Tuesday for December 2025 — Snort rules and prominent vulnerabilities

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Tuesday, December 9, 2025 18:29

[Patch Tuesday](/category/microsoft-patch-tuesday/)

The Patch Tuesday for December of 2025 includes 57 vulnerabilities, including two that Microsoft marked as “critical.” The remaining vulnerabilities listed are classified as “important.” Microsoft assessed that exploitation of the two “critical” vulnerabilities is “less likely.”

[CVE‑2025‑62562](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62562) is a Microsoft Outlook remote code execution vulnerability. Although it involves a use after free in Microsoft Office Outlook to allow an unauthorized attacker to execute code locally, an attacker would still need to send a malicious email and persuade the user to reply to it for the exploit to work.

[CVE-2025-62553](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62553), [CVE-2025-62554](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62554), [CVE-2025-62556](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62556) and [CVE-2025-62557](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62557) are Microsoft Office Remote Code Execution Vulnerability. An attacker can access resources using incompatible type ('type confusion') or use after free or untrusted pointer dereference in Microsoft Office allows an unauthorized attacker to execute code locally. Despite some of them being considered “critical”, the successful exploitation of this vulnerability requires an attacker to execute exploit code from the local machine to exploit the vulnerability.

[CVE-2025-62456](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62456) is a Remote Code Execution Vulnerability in Windows Resilient File System (ReFS). The vulnerability is based on heap-based buffer overflow in Windows Resilient File System (ReFS) that allows an authorized attacker to execute code over a network. Although the vulnerability has high CVSS scores, Microsoft has assessed that this exploitation in the wild is unlikely.

[CVE-2025-62549](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62549) - Windows Routing and Remote Access Service (RRAS) Remote Code Execution Vulnerability. An attacker could exploit this vulnerability by deceiving a user to send a request to a malicious server. The malicious server could then respond with crafted data that may lead to arbitrary code execution on the user's system. However, exploitation of this vulnerability requires user interaction, meaning the attacker must wait for the user to initiate a connection to the malicious server set up by the attacker before the exploit can occur. This dependency on user action increases the complexity of a successful attack.

[CVE‑2025‑62565](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62565) and [CVE‑2025‑64661](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-64661) are Windows Shell elevation‑of‑privilege vulnerabilities. They involve issues such as use after free or concurrent execution using shared resources with improper synchronization ('race condition') in Windows Shell which could allow a local authorized attacker to gain higher privileges on the system.

Cisco Talos would also like to highlight several vulnerabilities that are only rated as “important,” but Microsoft lists as “more likely” to be exploited:

* [CVE-2025-62454](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62454) - Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability
* [CVE-2025-62458](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62458) - Win32k Elevation of Privilege Vulnerability
* [CVE-2025-62470](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62470) - Windows Common Log File System Driver Elevation of Privilege Vulnerability
* [CVE-2025-62472](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62472) - Windows Remote Access Connection Manager Elevation of Privilege Vulnerability
* [CVE-2025-59516](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-59516) and [CVE-2025-59517](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-59517)- Windows Storage VSP Driver Elevation of Privilege Vulnerability
* [CVE-2025-62221](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-62221) - Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability

A complete list of all the other vulnerabilities Microsoft disclosed this month is available on its [update page](https://msrc.microsoft.com/update-guide/). In response to these vulnerability disclosures, Talos is releasing a new Snort rule set that detects attempts to exploit some of them. Please note that additional rules may be released at a future date and current rules are subject to change pending additional information. Cisco Security Firewall customers should use the latest update to their ruleset by updating their SRU. Open-source Snort Subscriber Rule Set customers can stay up to date by downloading the latest rule pack available for purchase on [Snort.org](http://snort.org/).

The rules included in this release that protect against the exploitation of many of these vulnerabilities are: 62486, 62487, 65555-65562, 65571-65574. There are also these Snort 3 rules: 300719, 301351-301354, 301356, 301357.

##### Share this post

#### Related Content

[### Microsoft Patch Tuesday for November 2025 — Snort rules and prominent vulnerabilities

November 11, 2025 13:19

Microsoft has released its monthly security update for November 2025, which includes 63 vulnerabilities affecting a range of products, including 5 that M...
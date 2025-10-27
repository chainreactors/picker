---
title: Microsoft Patch Tuesday for September 2025 – Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-september-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-10
fetch_date: 2025-10-02T19:54:54.613919
---

# Microsoft Patch Tuesday for September 2025 – Snort rules and prominent vulnerabilities

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

![](/content/images/2025/09/patch-tuesday.jpg)

# Microsoft Patch Tuesday for September 2025 – Snort rules and prominent vulnerabilities

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Tuesday, September 9, 2025 15:12

[Patch Tuesday](/category/microsoft-patch-tuesday/)

Microsoft has released its monthly security update for September 2025, which includes 86 vulnerabilities affecting a range of products.

In this month’s release, Microsoft observed none of the included vulnerabilities being exploited in the wild. However, there are eight vulnerabilities where exploitation may be likely. Five consist of elevation of privileges, two may result in information disclosure and only one, CVE-2025-54916, is a remote code execution (RCE) vulnerability.

[CVE-2025-54916](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54916) is an RCE vulnerability caused by a stack-buffer overflow in Windows NTFS that allows an authorized attacker to execute code over the network. Microsoft has noted that this vulnerability affects different versions of Windows 10, 11, Server 2008, 2012, 2016, 2019, 2022 and 2025.

[CVE-2025-54910](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54910) is an RCE vulnerability caused by a heap-based buffer overflow in Microsoft Office that allows an unauthorized attacker to execute code locally. This type of vulnerability is also known as Arbitrary Code Execution (ACE). Microsoft clarifies that the attack itself is carried out locally, and that the location of the attacker can be remote, but the vulnerability must be exploited locally. This vulnerability affects Microsoft 365 Apps, Office 2016, 2019 and LTSC 2021 and 2024.

[CVE-2025-54918](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54918) is an elevation of privilege (EoP) vulnerability caused by improper authentication in Windows NTLM that allows an authorized attacker to elevate privileges over a network to gain SYSTEM privileges. This vulnerability affects various versions of Windows including Windows 10, 11, Server 2008, 2012, 2016, 2019, 2022 and 2025.

[CVE-2025-54101](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54101) is an RCE vulnerability caused by a use-after-free in Windows SMB v3 Client/Server that allows an authorized attacker to execute code over a network. Successful exploitation requires the attacker to win a race condition. This vulnerability affects various versions of Windows including Windows 10, 11, Server 2008, 2012, 2016, 2019 and 2022.

Two RCE vulnerabilities in DirectX Graphics kernel may result in remote code execution: [CVE-2025-55226](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55226) and [CVE-2025-55236](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55236). [CVE-2025-55226](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55226) is caused by concurrent execution using a shared resource and improper synchronization in the Graphics Kernel allowing an authorized attacker to execute code locally. Microsoft also notes that this vulnerability requires an attacker to prepare the target environment to improve exploit reliability. This vulnerability affects various versions of Windows including Windows 10, 11, Server 2008, 2012, 2016, 2019, 2022 and 2025.

[CVE-2025-55236](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-55236) is a time-of-check time-of-use (toctou) race condition in the Graphics Kernel allowing an authorized attacker to execute locally. This vulnerability affects various versions of Windows including Windows 10, 11, Server 2019, 2022 and 2025.

Talos would also like to highlight the following important vulnerabilities as Microsoft has assessed that their exploitation is more likely:

[CVE-2025-53803](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53803): Windows Kernel Memory Information Disclosure Vulnerability.

[CVE-2025-53804](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53804): Windows Kernel-Mode Driver Information Disclosure Vulnerability.

[CVE-2025-54093](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54093): Windows TCP/IP Driver Elevation of Privilege Vulnerability.

[CVE-2025-54098](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54098): Windows Hyper-V Elevation of Privilege Vulnerability.

[CVE-2025-54110](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-54110): Windows Kernel Elevation of Privilege Vulnerability.

A complete list of all the other vulnerabilities Microsoft disclosed this month is available on its [update page](https://msrc.microsoft.com/update-guide/releaseNote/2025-Sep).

In response to these vulnerability disclosures, Talos is releasing a new Snort ruleset that detects attempts to exploit some of them. Please note that additional rules may be released at a future date, and current rules are subject to change pending additional information. Cisco Security Firewall customers should use the latest update to their ruleset by updating their SRU. Open-source Snort Subscriber Ruleset customers can stay up to date by downloading the latest rule pack available for purchase on [Snort.org](https://snort.org/).

Snort2 rules included in this release that protect against the exploitation of many of these vulnerabilities are: 65327 – 65334.

The following Snort3 rules are also available: 301310 – 301313.

##### Share this post

#### Related Content

[### Microsoft Patch Tuesday for August 2025 — Snort rules and prominent vulnerabilities

August 12, 2025 15:39

Microsoft has released its monthly security update for August 2025, which includes 111 vulnerabilities affecting a range of products, including 13 that Microsoft marked as “critical”.](/microsoft-patch-tuesday-august-2025/)

[### Micr...
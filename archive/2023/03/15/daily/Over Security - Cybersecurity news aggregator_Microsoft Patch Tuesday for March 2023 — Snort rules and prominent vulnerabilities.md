---
title: Microsoft Patch Tuesday for March 2023 — Snort rules and prominent vulnerabilities
url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-march-2023-snort-rules-and-prominent-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-15
fetch_date: 2025-10-04T09:40:37.892236
---

# Microsoft Patch Tuesday for March 2023 — Snort rules and prominent vulnerabilities

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

# Microsoft Patch Tuesday for March 2023 — Snort rules and prominent vulnerabilities

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Tuesday, March 14, 2023 16:08

[Patch Tuesday](https://blog.talosintelligence.com/category/microsoft-patch-tuesday/)

Microsoft released its monthly security update Tuesday, disclosing 83 vulnerabilities across the company’s hardware and software line, including two issues that are actively being exploited in the wild, [continuing a trend](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-february-2023-snort-rules-and-prominent-vulnerabilities/) of [zero-days appearing](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-december-2022/) in Patch Tuesdays over the past few months.

Two of the vulnerabilities included in March’s security update have been exploited in the wild, according to Microsoft, including one critical issue.

In all, eight of the issues disclosed this month are critical, while the remainder — outside of one — is “important.”

A moderate-severity vulnerability that’s already being exploited in the wild is [CVE-2023-24880](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24880), a security feature bypass vulnerability in Windows SmartScreen, a cloud-based anti-phishing and anti-malware feature included in several Microsoft products. An attacker could exploit this vulnerability to craft a malicious file that would evade Mark of the Web (MOTW) defenses, resulting in a limited loss of integrity and availability of security features such as Protected View in Microsoft Office, which rely on MOTW tagging. This, in theory, could allow the attacker to pass a malicious file through without it being detected.

The other zero-day included this month is [CVE-2023-23397](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-23397), a privilege escalation vulnerability in Microsoft Outlook that could force a targeted device to connect to a remote URL and transmit the Windows account's Net-NTLMv2 hash to an adversary.

To trigger this vulnerability, a user doesn’t even need to open the email or preview it, the vulnerability is triggered as soon as the email is retrieved by the targeted email server.

Three of the other critical vulnerabilities Microsoft is patching have a CVSS severity score of 9.8 out of 10: [CVE-2023-21708](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21708), [CVE-2023-23392](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23392) and [CVE-2023-23415.](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23415)

CVE-2023-21708 is a remote code execution vulnerability in Microsoft Remote Call Procedure (RCP). To exploit this vulnerability, an unauthenticated attacker could send a specially crafted RPC call to an RPC host. This could result in remote code execution on the server side with the same permissions as the RPC service.

The attacker would need to have access to TCP port 135 on the remote host, so Microsoft considers this vulnerability “less likely” to be exploited, especially from an outside network perimeter. But an attacker who already have a foothold on an internal network could use this vulnerability to compromise other machines in the same domain if the target doesn’t block this port.

Another remote code execution vulnerability exists on the HTTP protocol stack on Windows 11 and Windows Server 2022. An attacker could exploit CVE-2023-23392 by sending a specially crafted packet to a targeted server that utilizes the HTTP Protocol Stack to process packets. For a server to be vulnerable, it must already have HTTP/3 enabled and use buffered I/O. HTTP/3 support for services is a new feature of Windows Server 2022. Another escalation of privilege vulnerability in the same component ([CVE-2023-23410](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23410)) may allow an attacker to elevate privileges to SYSTEM.

CVE-2023-23415 is the only vulnerability among the three with 9.8 CVSS scores that is “more likely” to be exploited, according to Microsoft. An attacker could exploit this vulnerability in the Internet Control Message Protocol (ICMP) to gain the ability to execute remote code with SYSTEM-level privileges.

An attacker could send fragmented ICMP error messages to a remote target and cause a read past the fragment buffer end. This could cause a BSOD if the read crosses a page boundary or give the attacker remote code execution abilities.

The other critical vulnerabilities are:

* [CVE-2023-23404](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23404), a remote code execution vulnerability in Windows point-to-point tunneling protocol
* [CVE-2023-23411](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23411), a denial-of-service vulnerability in Windows Hyper-V
* [CVE-2023-23416](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23416), a remote code execution vulnerability in Windows cryptographic services

A complete list of all the vulnerabilities Microsoft disclosed this month is available on its [update page](https://portal.msrc.microsoft.com/en-us/security-guidance).

In response to these vulnerability disclosures, Talos is releasing a new Snort rule set that detects attempts to exploit some of them. Please note that additional rules may be released at a future date and current rules are subject to change pending additional information. Cisco Secure Firewall customers should use the latest update to their ruleset by updating their SRU. Open-source Snort Subscriber Rule Set customers can stay up to date by downloading the latest rule pack available for purchase on Snort.org.

The rules included in this release that protect against the exploitation of many of these vulnerabilities are 61464 -...
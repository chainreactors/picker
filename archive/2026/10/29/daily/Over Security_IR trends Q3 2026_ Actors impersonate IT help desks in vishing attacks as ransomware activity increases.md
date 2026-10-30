---
title: IR trends Q3 2026: Actors impersonate IT help desks in vishing attacks as ransomware activity increases
url: https://blog.talosintelligence.com/ir-trends-q3-2026/
source: Over Security
date: 2026-10-29
fetch_date: 2026-10-30T07:56:06.542570
---

# IR trends Q3 2026: Actors impersonate IT help desks in vishing attacks as ransomware activity increases

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

# IR trends Q3 2026: Actors impersonate IT help desks in vishing attacks as ransomware activity increases

By
[Aliza Johnson](https://blog.talosintelligence.com/author/aliza/)

Thursday, October 29, 2026 10:00

[Talos IR trends](https://blog.talosintelligence.com/category/ctir-trends/)
[Cisco Talos Incident Response](https://blog.talosintelligence.com/category/cisco-talos-incident-response/)
[CTIR trends](https://blog.talosintelligence.com/category/ctir-trends-2/)

Phishing remained the leading initial access technique, appearing in slightly over one-third of all Cisco Talos Incident Response (Talos IR) engagements — a decrease from over 50 percent last quarter. In addition to traditional phishing links and attachments, we observed numerous threat actors conducting voice phishing (vishing) in tandem with IT desk impersonation to socially engineer the victim into allowing remote access via a legitimate remote monitoring and management (RMM) tool. Exploitation of public-facing applications was the next most common vector, accounting for one-third of Talos IR engagements. Threat actors predominantly targeted edge devices such as security gateways and remote network management interfaces. These are critical components within enterprise environments, often responsible for managing authentication, network traffic, or sensitive data. Compromising them can provide broad access to internal networks or user credentials.

Ransomware and pre-ransomware incidents made up 27 percent of engagements in Q3 2026, an increase from a maximum of 20 percent seen in the previous four quarters. Talos responded to attacks involving prolific, technologically advanced, and well-established ransomware-as-a-service (RaaS) variants such as The Gentlemen, Qilin, and Rhysida, as well as Interlock, which operates as a closed group. Threat actors predominantly chose to disable endpoint detection and response (EDR) systems, often by exploiting vulnerable drivers or using Windows Defender Application Control (WDAC). Additionally, we observed the emerging ransomware variant VYPR, whose operator(s) tested a range of tactics, techniques, and procedures (TTPs) instead of following a standard attack method or affiliate playbook.

## Salt Typhoon-affiliated threat actors exploit public-facing application vulnerabilities for cyber espionage

Talos IR continues to see prolonged cyber espionage intrusions targeting the telecommunications sector. Talos attributed most of these intrusions with high confidence to China state-sponsored threat actors, including Salt Typhoon. The attackers in these intrusions routinely gain initial access by leveraging valid credentials and exploiting a known vulnerability (CVE-2023-20198) in publicly accessible web-based management interfaces—two of the most frequently observed initial access vectors this quarter. In one campaign, the threat actor deployed [BadCandy,](https://blog.talosintelligence.com/active-exploitation-of-cisco-ios-xe-software/) a malicious web shell implant known to be leveraged by Salt Typhoon, to maintain persistent and stealthy remote access.

The adversaries continue to employ living-off-the-land (LOTL) tactics, leveraging legitimate network infrastructure features — such as VPN access, traffic mirroring, and management protocols — to establish backdoors, exfiltrate data, and conduct reconnaissance. Exploiting a vulnerability in the web-based management interface, they created privileged accounts, disabled logging to conceal their activity, and altered configurations to maintain persistence, blending their actions with normal administrative operations to evade detection.

These intrusions revealed several security weaknesses in the victim environment, including reliance on password-only authentication without evidence of multi-factor authentication (MFA), use of legacy and weak management protocols (such as plaintext SNMP and outdated VPN encryption), and inadequate credential management practices. Attackers were able to create and abuse privileged accounts, disable logging, and manipulate configuration settings without encountering effective security barriers, enabling persistent and stealthy access. The absence of strong MFA and robust credential management are two of the most frequently observed security weaknesses this quarter.

## AI exploited as a weapon and a target

Recent Talos IR investigations highlight the growing role of artificial intelligence (AI) in cybercriminal activity, both as a tool and a target. In one case, an internal threat actor who was hired under false credentials abused their privileged access to install AI-powered development tools, such as GitHub Copilot CLI and Anthropic Claude Code. While the investigation did not find evidence of malicious activity or data theft, the employee’s developer-level access — including cloning repositories, configuring plugins, and connecting to databases — could have enabled them to use AI tools to automate malicious actions within the organization.

A second investigation revealed an attack chain in which a compromised macOS endpoint, infected via a trojanized application, was scripted to scrape credentials from the macOS keychain specifically associated with the Anthropic Claude Code AI assistant. This direct targeting of AI-related secrets highlights an emerging threat, where attackers seek to compromise not only traditional user and system credentials but also those tied to AI platforms, which may grant access to additional sensitive data and advanced automation capabilities.

These incidents highlight the critical need for organizations to implement strong MFA and robust credential management practices, especially for AI platforms and development tools.

## Ransomware trends

Ransomware and pre-ransomware incidents increased from a little over 20 percent last quarter to...
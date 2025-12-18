---
title: UAT-9686 actively targets Cisco Secure Email Gateway and Secure Email and Web Manager
url: https://blog.talosintelligence.com/uat-9686/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-17
fetch_date: 2025-12-18T03:20:46.940301
---

# UAT-9686 actively targets Cisco Secure Email Gateway and Secure Email and Web Manager

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

![](/content/images/2025/12/threat-advisory.jpg)

# UAT-9686 actively targets Cisco Secure Email Gateway and Secure Email and Web Manager

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Wednesday, December 17, 2025 11:55

[APT](/category/apt/)
[Threat Advisory](/category/threat-advisory/)

* Cisco Talos recently discovered a campaign targeting Cisco AsyncOS Software for Cisco Secure Email Gateway, formerly known as Cisco Email Security Appliance (ESA), and Cisco Secure Email and Web Manager, formerly known as Cisco Content Security Management Appliance (SMA).
* We assess with moderate confidence that the adversary, who we are tracking as UAT-9686, is a Chinese-nexus advanced persistent threat (APT) actor whose tool use and infrastructure are consistent with other Chinese threat groups.
* As part of this activity, UAT-9686 deploys a custom persistence mechanism we track as “AquaShell” accompanied by additional tooling meant for reverse tunneling and purging logs.
* Our analysis indicates that appliances with non-standard configurations, [as described in Cisco's advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sma-attack-N9bf4), are what we have observed as being compromised by the attack.

---

Cisco Talos is tracking the active targeting of Cisco AsyncOS Software for Cisco Secure Email Gateway, formerly known as Cisco Email Security Appliance (ESA), and Cisco Secure Email and Web Manager, formerly known as Cisco Content Security Management Appliance (SMA), enabling attackers to execute system-level commands and deploy a persistent Python-based backdoor, AquaShell. Cisco became aware of this activity on December 10, which has been ongoing since at least late November 2025. Additional tools observed include AquaTunnel (reverse SSH tunnel), chisel (another tunneling tool), and AquaPurge (log-clearing utility). Talos' analysis indicates that appliances with non-standard configurations, as described in Cisco's advisory, are what we have observed as being compromised by the attack.

The Cisco Secure Email and Web Manager centralizes management and reporting functions across multiple Cisco Email Security Appliances (ESAs) and Web Security Appliances (WSAs), offering centralized services such as spam quarantine, policy management, reporting, tracking, and configuration management to simplify administration and enhance security enforcement.

Customers are strongly advised to follow the guidance published in the security advisories discussed below. Additional recommendations specific to Cisco are [available here](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sma-attack-N9bf4).

Talos assesses with moderate confidence that this activity is being conducted by a Chinese-nexus threat actor, which we track as UAT-9686. We have observed overlaps in tactics, techniques and procedures (TTPs), infrastructure, and victimology between UAT-9686 and other Chinese-nexus threat actors Talos tracks. Tooling used by UAT-9686, such as AquaTunnel (aka ReverseSSH), also aligns with previously disclosed Chinese-nexus APT groups such as [APT41](https://www.security.com/threat-intelligence/china-southeast-asia-espionage) and [UNC5174](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2025-CTI-009.pdf). Additionally, the tactic of using a custom-made web-based implant such as AquaShell is increasingly being adopted by highly sophisticated Chinese-nexus APTs.

## AquaShell

AquaShell is a lightweight Python backdoor that is embedded into an existing file within a Python-based web server. The backdoor is capable of receiving encoded commands and executing them in the system shell. It listens passively for unauthenticated HTTP POST requests containing specially crafted data. If such a request is identified, the backdoor will then attempt to parse the contents using a custom decoding routine and execute them in the system shell.

AquaShell is delivered as an encoded data blob that is decoded and ultimately placed in “/data/web/euq\_webui/htdocs/index.py”.

The result of decoding the data blob is the Python code that constitutes the AquaShell backdoor. AquaShell parses the HTTP POST request, decodes it using a combination custom algorithm and Base64 decoding and executes the resulting commands on the appliance.

## AquaPurge

AquaPurge removes lines containing specific keywords from the log files specified. It uses the “egrep” command  to filter out (invert search) all content that doesn’t contain the keywords and then simply commits them to the log files:

![](https://blog.talosintelligence.com/content/images/2025/12/AquaPurge.png)

## AquaTunnel

AquaTunnel is a compiled GoLang ELF binary based on the open-source “[ReverseSSH](https://github.com/Fahrj/reverse-ssh)” backdoor. AquaTunnel creates a reverse SSH connection from the compromised system back to an attacker‑controlled server, enabling unauthorized remote access even when the system is behind firewalls or NAT.

## Chisel

Chisel is an open‑source tunneling tool that supports creating TCP/UDP tunnels over a single‑port HTTP‑based connection. Chisel allows an attacker to proxy traffic through a compromised edge device, allowing them to easily pivot through that device into the internal environment.

## Coverage and remediation

Recommendations for Cisco customers are [available here](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sma-attack-N9bf4). If your organization does find connections to the provided actor indicators of compromise (IOCs), [please open a case with Cisco TAC](https://mycase.cloudapps.cisco.com/create/start).

All IOCs, including IPs and file hashes determined to be associated with this campaign have been blocked across the Cisco portfolio.

## IOCs

The IOCs can a...
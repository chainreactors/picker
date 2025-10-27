---
title: BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks
url: https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-29
fetch_date: 2025-10-06T18:07:53.517049
---

# BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks

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

![](/content/images/2024/08/blackbyteheader.jpg)

# BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks

By
[James Nutland](https://blog.talosintelligence.com/author/james/),
[Craig Jackson](https://blog.talosintelligence.com/author/craig/),
[Terryn Valikodath](https://blog.talosintelligence.com/author/terryn/),
[Brennan Evans](https://blog.talosintelligence.com/author/brennan-evans/)

Wednesday, August 28, 2024 06:00

[Threat Spotlight](/category/threat-spotlight/)
[Cisco Talos Incident Response](/category/cisco-talos-incident-response/)

* The BlackByte ransomware group continues to leverage tactics, techniques and procedures (TTPs) that have formed the foundation of its tradecraft since its inception, continuously iterating its use of vulnerable drivers to bypass security protections and deploying a self-propagating, wormable ransomware encryptor.
* In recent investigations, Talos IR has also observed BlackByte using techniques that depart from their established tradecraft, such as exploiting CVE-2024-37085 – an authentication bypass vulnerability in VMware ESXi – shortly after it was disclosed and using a victim’s authorized remote access mechanism rather than deploying a commercial remote administration tool like AnyDesk.
* Talos IR observed a new iteration of the BlackByte encryptor that appends the file extension “blackbytent\_h” to encrypted files, drops four vulnerable driver files compared to the previously observed three, and uses victim Active Directory credentials to self-propagate.
* Talos also assesses that the BlackByte group is more active than its data leak site may imply, where only 20 to 30 percent of successful attacks result in an extortion post.

BlackByte is a ransomware-as-a-service (RaaS) group believed to be an offshoot of the infamous Conti ransomware group. First observed in mid- to late-2021, their tradecraft includes the use of vulnerable drivers to bypass security controls, deployment of self-propagating ransomware with worm-like capabilities, and the use of known-good system binaries (LoLBins) and other legitimate commercial tools as part of their attack chain.

BlackByte has reengineered its ransomware binary over time, with versions written in [Go, .NET, C++, or a combination of these languages](https://blog.talosintelligence.com/talos-ir-trends-q3-2023/). The group’s apparent efforts to continuously improve its tooling, operations and even its data leak site is well-documented.

During investigation of a recent BlackByte attack, Cisco Talos Incident Response (Talos IR) and Talos threat intelligence personnel noted close similarities between indicators of compromise (IOCs) discovered during the investigation and other events flagged in Talos’ global telemetry. Further investigation of these similarities provided additional insights into BlackByte’s current tradecraft and revealed that the group has been significantly more active than would appear from the number of victims published on its data leak site.

## Technical details

### Initial access

During Talos IR’s investigation into a recent BlackByte ransomware attack, the threat actor gained initial access using valid credentials to access the victim organization’s VPN. Limits in telemetry and loss of evidence following the ransomware encryption event prevented Talos IR from determining whether the credentials were obtained through brute-forcing of the VPN interface or had already been known by the adversary prior to the attack. However, Talos IR has moderate confidence that brute-force authentication facilitated via internet scanning was the initial access vector based on the following observations:

* The initial account compromised by the adversary had a basic naming convention and, reportedly, a weak password.
* The VPN interface may have allowed a domain account to authenticate without multi-factor authentication (MFA) if the target account had a specific Active Directory configuration.
* BlackByte has a history of scanning for and exploiting public-facing vulnerabilities, [such as the ProxyShell vulnerability in Microsoft Exchange server](https://redcanary.com/blog/threat-intelligence/blackbyte-ransomware/).

Given BlackByte’s history of exploiting public-facing vulnerabilities for initial access, the use of VPN for remote access may represent a slight shift in technique or could represent opportunism. The use of the victim’s VPN for remote access also affords the adversary other advantages, including reduced visibility from the organization’s EDR.

### Reconnaissance and enumeration

After gaining initial access to the environment, the adversary managed to escalate privileges by compromising two Domain Admin-level accounts. One of these accounts was used to access the organization’s VMware vCenter server and, shortly after, create Active Directory domain objects for individual VMware ESXi hypervisors, effectively joining those hosts to the domain. The same account was then used to create and add several other accounts to an Active Directory group called "ESX Admins." Talos IR assesses that this user group was created to exploit [CVE-2024-37085](https://nvd.nist.gov/vuln/detail/CVE-2024-37085), an authentication bypass vulnerability in VMware ESXi [known to be used by multiple ransomware groups](https://www.microsoft.com/en-us/security/blog/2024/07/29/ransomware-operators-exploit-esxi-hypervisor-vulnerability-for-mass-encryption/). Successful exploitation of this vulnerability grants members of a specific Active Directory group elevated privileges on an ESXi host, allowing for control over virtual machines (VMs), the ability to modify the host server’s configuration, and access to system logs, diagnostics and performance monitoring tools.

Talos IR observed the threat actor leveraging thi...
---
title: Akira ransomware continues to evolve
url: https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-22
fetch_date: 2025-10-06T18:54:24.709922
---

# Akira ransomware continues to evolve

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

# Akira ransomware continues to evolve

By
[James Nutland](https://blog.talosintelligence.com/author/james/),
[Michael Szeliga](https://blog.talosintelligence.com/author/michael/)

Monday, October 21, 2024 12:50

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[ransomware](https://blog.talosintelligence.com/category/ransomware/)

Akira continues to cement its position as [one of the most prevalent](https://blog.talosintelligence.com/common-ransomware-actor-ttps-playbooks/) ransomware operations in the threat landscape, according to Cisco Talos’ findings and analysis.

Their success is partly due to the fact that they are constantly evolving. For example, after Akira already developed a new version of their ransomware encryptor earlier in the year, we just recently observed another novel iteration of the encryptor targeting Windows and Linux hosts alike.

Previously, Akria typically employed a double-extortion tactic in which critical data is exfiltrated prior to the compromised victim systems becoming encrypted. Beginning in early 2024, Akira appeared to be sidelining the encryption tactics, focusing on data exfiltration only. We assess with low to moderate confidence that this shift was due in part to the developers taking time to further retool their encryptor.

During this period, we began to see Akira ransomware-as-a-service (RaaS) operators developing a Rust variant of their ESXi encryptor, iteratively building on the payload’s functions while moving away from C++ and experimenting with different programming techniques.

Most recently, we have observed a potential shift back to previous encryption methods, in conjunction with data theft extortion tactics.

Returning to this approach leverages the reliability of tested encryption techniques, while simultaneously capitalizing on data theft for additional leverage. Pivoting to a previously effective strategy post-language reimplementation with v2 indicates a refocus on stability and efficiency in affiliate operations.

We anticipate Akira will continue refining its tactics, techniques, and procedures (TTPs), developing its attack chain, adapting to shifts in the threat landscape, and striving for greater effectiveness in its RaaS operations, targeting both Windows and Linux-based enterprise environments.

Members of our team will be delving into this prickly threat actor presenting at the upcoming MITRE ATT&CKCon 5.0 in [‘GoGo Ransom Rangers: Diving into Akira’s Linux Variant with ATT&CK'](https://na.eventscloud.com/website/76470/#Agenda). Join us as we uncover findings about the TTPs employed by this developing threat actor, dissect their attack chain, and actionable intelligence is vital in the threat protection pipeline.

> "The future is not a straight line. It is filled with many crossroads" Kiyoko

### 2024 attack chain: Leveraging exposed network appliances and vulnerable systems for rapid compromise

As Akira continuously refines its ransomware, affiliates are equally proactive in selecting and exploiting new vulnerabilities for initial access, adapting their tactics in tandem. They leverage newly disclosed CVEs, not only to breach networks but also to escalate privileges and move laterally within compromised environments. This allows them to establish a greater foothold to swiftly deploy encryption and exfiltrate victim data for extortion.

Akira ransomware operators have utilized a variety of common infection vectors to gain initial access to targeted networks, often favoring the use of compromised VPN credentials.

Most recently, Akira ransomware affiliates have been observed targeting network appliances vulnerable to [CVE-2024-40766](https://nvd.nist.gov/vuln/detail/CVE-2024-40766), an exploit in the SonicWall SonicOS facilitating remote code execution on the vulnerable device. Security researchers found that software on the affected systems was vulnerable to this exploit, suggesting affiliates’ swift capitalization on exposed systems.

Additional vulnerabilities leveraged by affiliates throughout 2024 include:

* [CVE-2020-3259](https://nvd.nist.gov/vuln/detail/CVE-2020-3259) and [CVE-2023-20263](https://nvd.nist.gov/vuln/detail/CVE-2023-20263): In similar Cisco security appliance exploits leveraged in early 2024, Akira was observed abusing a flaw in [Cisco Adaptive Security Appliance](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-asaftd-info-disclose-9eJtycMB.html) (ASA) with CVE-2020-3259 and CVE-2023-20263 via Firepower Threat Defense (FTD) software that allowed attackers to execute arbitrary code, after initial access was established post Cisco AnyConnect SSL VPN compromise.
* [CVE-2023-48788](https://nvd.nist.gov/vuln/detail/CVE-2023-48788): Exposed and vulnerable FortiClientEMS software abuse by Akira was observed for initial access, enabling lateral movement and privilege escalation.

Once initial access is established, Akira operators utilize PowerShell scripts to conduct credential harvesting and privilege escalation, such as extracting Veeam backup credentials and dumping Kerberos authentication credentials. Additionally, we often see affiliates delete system shadow copies to obstruct file recovery via Windows Management Instrumentation (WMI): “Get-WmiObject Win32\_Shadowcopy | Remove-WmiObject”.

Operators typically utilize RDP connections and lateral tool transfers to move through the network and employ a variety of defense evasion techniques, such as binary padding, matching legitimate name or location taxonomy, and disabling or modifying security tools.

In an attack targeting a Latin American airline in June 2024, RaaS operators were able to exploit key vulnerable services and deploy the ransomware payload in a manner that drastically reduced the time to exfiltrate data. Initially gaining access via Secure Shell ...
---
title: Russian state-sponsored espionage group Static Tundra compromises unpatched end-of-life network devices
url: https://blog.talosintelligence.com/static-tundra/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-21
fetch_date: 2025-10-07T00:49:42.288774
---

# Russian state-sponsored espionage group Static Tundra compromises unpatched end-of-life network devices

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

![](/content/images/2025/08/static-tundra-header.jpg)

# Russian state-sponsored espionage group Static Tundra compromises unpatched end-of-life network devices

By
[Sara McBroom](https://blog.talosintelligence.com/author/sara/),
[Brandon White](https://blog.talosintelligence.com/author/brandon/)

Wednesday, August 20, 2025 09:00

[Threats](/category/threats/)
[Threat Advisory](/category/threat-advisory/)

* **Static Tundra is a Russian state-sponsored cyber espionage group** linked to the FSB's Center 16 unit that has been operating for over a decade, specializing in compromising network devices for long-term intelligence gathering operations.
* **The group actively exploits a seven-year-old vulnerability (CVE-2018-0171),** which was patched at the time of the vulnerability publications, in Cisco IOS software's Smart Install feature, targeting unpatched and end-of-life network devices to steal configuration data and establish persistent access.
* **Primary targets include organizations in telecommunications, higher education and manufacturing sectors** across North America, Asia, Africa and Europe, with victims selected based on their strategic interest to the Russian government.
* **Static Tundra employs sophisticated persistence techniques** including the historic SYNful Knock firmware implant (first reported in 2015) and bespoke SNMP tooling to maintain undetected access for multiple years.
* **The threat extends beyond Russia's operations** — other state-sponsored actors are likely conducting similar network device compromise campaigns, making comprehensive patching and security hardening critical for all organizations.
* **Threat actors will continue** to abuse devices which remain unpatched and have Smart Install enabled.
* Customers are urged to apply the [patch for CVE-2018-0171](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180328-smi2) or to disable Smart Install as indicated [in the advisory](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180328-smi2.html) if patching is not an option. Customer support is available if needed by initiating a [TAC request](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#gsrq).

---

Since 2015, Cisco Talos has observed the compromise of unpatched and often end-of-life Cisco networking devices by a highly sophisticated threat actor. Based on sufficient recent activity observed through our ongoing analysis, we have designated this threat cluster “Static Tundra.” This blog highlights our observations regarding this threat actor and provides recommendations for detecting and preventing activities associated with Static Tundra.

## Threat actor and campaign overview

Talos assesses with high confidence that Static Tundra is a Russian state-sponsored cyber espionage group specializing in network device exploitation to support long-term intrusion campaigns into organizations that are of strategic interest to the Russian government. Static Tundra is likely a sub-cluster of another group, “[Energetic Bear](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-296a)” (aka BERSERK BEAR), based on an overlap in tactics, techniques and procedures (TTPs) and victimology, which has been [corroborated by the FBI](https://www.ic3.gov/PSA/2025/PSA250820). Energetic Bear was linked to the Russian Federal Security Service’s (FSB) Center 16 unit in a 2022 [U.S. Department of Justice indictment](https://www.justice.gov/archives/opa/pr/four-russian-government-employees-charged-two-historical-hacking-campaigns-targeting-critical). Talos also assesses with moderate confidence that Static Tundra is associated with the historic use of “SYNful Knock,” a malicious implant installed on compromised Cisco devices [publicly reported](https://cloud.google.com/blog/topics/threat-intelligence/synful-knock-acis) in 2015.

Static Tundra is assessed to be a highly sophisticated cyber threat actor that has operated for over a decade, conducting long-term espionage operations. Static Tundra specializes in network intrusions, demonstrated by the group's advanced knowledge of network devices and use of bespoke tooling, possibly including the novel, but now decade-old, [SYNful Knock router implant](https://blogs.cisco.com/security/synful-knock).

Static Tundra targets unpatched, and often end-of-life, network devices to establish access on primary targets and support secondary operations against related targets of interest. Once they establish initial access to a network device, Static Tundra will pivot further into the target environment, compromising additional network devices and establishing channels for long-term persistence and information gathering. This is demonstrated by the group’s ability to maintain access in target environments for multiple years without being detected.

For years, Static Tundra has been compromising Cisco devices by exploiting a [previously disclosed vulnerability](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180328-smi2.html) in the Smart Install feature of Cisco IOS software and Cisco IOS XE software ([CVE-2018-0171](https://nvd.nist.gov/vuln/detail/cve-2018-0171)) that has been left unpatched, often after those devices are end-of-life. We assess that the purpose of this campaign is to compromise and extract device configuration information en masse, which can later be leveraged as needed based on then-current strategic goals and interests of the Russian government. This is demonstrated by Static Tundra’s adaptation and shifts in operational focus as Russia’s priorities have changed over time.

Since Static Tundra was first observed in 2015, the group has targeted organizations in the telecommunications, higher education and manufacturing sectors. Victims are primarily based in Ukrain...
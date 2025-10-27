---
title: State-sponsored campaigns target global network infrastructure
url: https://blog.talosintelligence.com/state-sponsored-campaigns-target-global-network-infrastructure/
source: Over Security - Cybersecurity news aggregator
date: 2023-04-19
fetch_date: 2025-10-04T11:36:04.198830
---

# State-sponsored campaigns target global network infrastructure

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

![](/content/images/2023/04/image1.jpg)

# State-sponsored campaigns target global network infrastructure

By
[Matt Olney](https://blog.talosintelligence.com/author/matt-olney/)

Tuesday, April 18, 2023 11:02

[Threats](/category/threats/)
[SecureX](/category/securex-3/)
[Threat Advisory](/category/threat-advisory/)

Cisco is deeply concerned by an increase in the rate of high-sophistication attacks on network infrastructure — that we have observed and have seen corroborated by numerous reports issued by various intelligence organizations — indicating state-sponsored actors are targeting routers and firewalls globally. We have [spoken about infrastructure security](https://blogs.cisco.com/security/the-time-is-now-for-organizations-to-address-their-aging-infrastructure) for a long time. However, while working with network infrastructure in various parts of the world, we have observed both espionage and obvious targeting to support future destructive attacks. While working with our partners, we have experienced the operational barriers that slow and sometimes stop security teams from properly securing network infrastructure. In this report, we are sharing both our observations of top-tier attackers and their activities on network devices, and recommendations and resources to help you improve your network infrastructure resilience.

## Background

Recently, the UK’s National Cyber Security Centre (NCSC) [released a report on a sustained campaign](https://www.ncsc.gov.uk/news/apt28-exploits-known-vulnerability-to-carry-out-reconnaissance-and-deploy-malware-on-cisco-routers) by a Russian intelligence agency targeting a vulnerability in routers that [Cisco had published a patch for in 2017](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170629-snmp). This campaign, dubbed "Jaguar Tooth," is an example of a much broader trend of sophisticated adversaries targeting networking infrastructure to advance espionage objectives or pre-position for future destructive activity. While infrastructure of all types has been observed under attack, attackers have been particularly successful in compromising infrastructure with out-of-date software.

Because of the large presence of Cisco network infrastructure around the world, any sustained attack against network infrastructure would likely target Cisco equipment, but attacks are by no means limited to Cisco hardware. [In reporting on Russian intelligence contracting documents](https://www.washingtonpost.com/national-security/2023/03/30/russian-cyberwarfare-documents-vulkan-files/), samples of which were recently shared with Cisco Talos, it was shown that any infrastructure brand would be targeted, with one scanning component targeting almost 20 different router and switch manufacturers (see the image below). Looking at past research, in 2018 Talos looked into the [VPNFilter threat](https://blog.talosintelligence.com/vpnfilter/), also believed to be of Russian origin, which showed a well-developed capability targeting Asus, Huawei, Linksys, MikroTik, Netgear, QNAP, TP-LINK, Ubiquiti, and Upvel devices.

![](https://blog.talosintelligence.com/content/images/2023/04/Picture1.png)

Russia is not alone in its actions. [CISA has reported on Chinese adversaries](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-158a) targeting network equipment from a similarly broad set of manufacturers. These are certainly not the only campaigns targeting network equipment, nor the only actors. It is reasonable to conclude that [any sufficiently capable national intelligence operation](https://blogs.cisco.com/security/shadow-brokers) would develop and use the capability to compromise the communications infrastructure of their preferred targets.

Talos investigations are consistent with these findings. We have observed traffic manipulation, traffic copying, hidden configurations, router malware, infrastructure reconnaissance and active weakening of defenses by adversaries operating on networking equipment. Given the variety of activities we have seen adversaries engage in, they have shown a very high level of comfort and expertise working within the confines of compromised networking equipment.

Our assessment is clear, that national intelligence agencies and state-sponsored actors across the globe have attacked network infrastructure as a target of primary preference. Route/switch devices are stable, infrequently examined from a security perspective, are often poorly patched and provide deep network visibility. They are the perfect target for an adversary looking to be both quiet and have access to important intelligence capability as well as a foothold in a preferred network.

## Campaign observations

We’d like to share a non-exhaustive list of the sorts of activities we have observed actors take on various infrastructure devices. Our analysis for this set of actors is that they were (depending on the incident) either engaging in espionage or establishing a foothold for follow-on actions in support of any number of strategic goals, which may include destructive attacks. While these activities span several different incidents and campaigns, they demonstrate the technical capability of the actor. So, in brief, we have seen the following actor behaviors across different infrastructure platforms at critical infrastructure facilities:

* The creation of Generic Router Encapsulation (GRE) tunnels and the hijacking of DNS traffic, giving the actor the ability to observe and control DNS resolution
* Modifying memory to reintroduce vulnerabilities that had been patched so the actor has a secondary path to access
* Modification of configurations to move the compromised device into a compromised state to allow the actor to execute additional exploits to further access
* Installatio...
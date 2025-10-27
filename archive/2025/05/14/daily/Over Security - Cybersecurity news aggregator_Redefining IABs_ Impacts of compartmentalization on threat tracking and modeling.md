---
title: Redefining IABs: Impacts of compartmentalization on threat tracking and modeling
url: https://blog.talosintelligence.com/redefining-initial-access-brokers/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-14
fetch_date: 2025-10-06T22:30:51.429061
---

# Redefining IABs: Impacts of compartmentalization on threat tracking and modeling

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

![](/content/images/2025/05/IABs-header.jpg)

# Redefining IABs: Impacts of compartmentalization on threat tracking and modeling

By
[Edmund Brumaghin](https://blog.talosintelligence.com/author/edmund-brumaghin/),
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/)

Tuesday, May 13, 2025 06:00

[initial access broker](/category/initial-access-broker/)

* Cisco Talos has observed a growing trend of attack kill chains being split into two stages — initial compromise and subsequent exploitation — executed by separate threat actors. This compartmentalization increases the complexity and difficulty of performing threat modeling and actor profiling.
* Initial access groups now include both traditional initial access brokers (IABs) as well as opportunistic and state-sponsored threat actors, whose characteristics, motivations and objectives differ significantly.
* In response to these evolving threats, we have refined the definitions of initial access groups to include subcategories such as financially-motivated initial access (FIA), state-sponsored initial access (SIA), and opportunistic initial access (OIA).
* We provide several examples of publicly-known threat groups to explain our methodology and the differentiation between them. Understanding the motivations of initial access groups is crucial for analyzing compartmentalized threats. In the forthcoming [blog](https://blog.talosintelligence.com/compartmentalized-threat-modeling), we will explain how to model attack kill chains that involve multiple attackers.

---

## What is initial access?

The term "initial access" refers to the initial foothold or entry point that threat actors establish within a target network or system. It is the stage in the cyber attack kill chain in which an attacker has the opportunity to begin working towards their longer-term mission objectives, whatever those may be. Initial access can be gained through a variety of methods, including exploitation of software or hardware vulnerabilities, employment of social engineering tactics to obtain credentials, or delivery of malicious components that, if opened or executed by victims, grant this ability automatically.

In recent years, we have observed the emergence of threat actors who specialize in gaining initial access to computer networks. These threat actors, also referred to as initial access brokers (IABs), traditionally monetize the access they gain by selling it to other threat actors, who may then utilize the provided access for espionage or financial purposes. In short, IABs play a pivotal role in the overall cybercrime ecosystem, as they enable other malicious actors to quickly and efficiently execute their attacks without requiring them to obtain access themselves.

This distinction between IABs and the threat actors they may transfer network/system access to is extremely important. It directly impacts organizational risk assessment and threat modeling activities, as well as how incident response may be conducted if an intrusion occurs. It also complicates intrusion analysis, as it is often difficult to determine when a potential “handoff” of access occurs between threat actors when analyzing log data collected during an active intrusion.

Additionally, the term "initial access" is sometimes misused to refer to infrastructure leveraged by threat actors, such as operational relay box (ORB) networks and those offered as Infrastructure as a Service (IaaS). In this context, "initial access" specifically refers to access to the target's network, not a network leveraged by threat actors merely as infrastructure for their campaign.

## What are the challenges?

One of the primary challenges in modern intrusion analysis is the ability to correctly identify whether an observed adversary is an IAB. This distinction is operationally critical: when the actor responsible for the intrusion focuses solely on initial access, defenders must anticipate and prepare for the likely involvement of secondary actors who may carry out the core objectives of the attack. However, distinguishing IABs from full-spectrum threat actors has become increasingly difficult, as many initial access operations now exhibit the same level of sophistication, targeting and tooling as those conducted by targeted attackers or advanced persistent threats (APT). This overlap in tradecraft significantly complicates attribution, especially in cases where multiple actors interact across different phases of the intrusion.

Another challenge stems from the fact that compartmentalization is no longer exclusive to financially-motivated cybercriminals. In recent years, state-sponsored threat actors have adopted similar operational models, performing initial access and subsequently handing off to other state-sponsored groups within the same state apparatus (e.g., between military or intelligence units). In some [cases](https://unit42.paloaltonetworks.com/north-korean-threat-group-play-ransomware/), state-sponsored initial access groups even transfer access to financially-motivated ransomware operators. These handoffs may be strategic or opportunistic in nature, but they introduce a key problem for defenders: the appropriate preventative, detective and responsive strategies employed must consider not only the threat actor who obtains initial access, but also any other threat actors that may operate during later stages of an intrusion. Likewise, the hunting and containment strategies employed to defend against financially-motivated IABs may not be suitable against state-sponsored initial access groups, whose access operations are typically more stealthy, targeted, and persistent.

Given this evolu...
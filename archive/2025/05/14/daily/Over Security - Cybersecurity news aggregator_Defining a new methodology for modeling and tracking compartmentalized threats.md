---
title: Defining a new methodology for modeling and tracking compartmentalized threats
url: https://blog.talosintelligence.com/compartmentalized-threat-modeling/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-14
fetch_date: 2025-10-06T22:30:51.925349
---

# Defining a new methodology for modeling and tracking compartmentalized threats

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

![](/content/images/2025/05/attack-chain-header.jpg)

# Defining a new methodology for modeling and tracking compartmentalized threats

By
[Edmund Brumaghin](https://blog.talosintelligence.com/author/edmund-brumaghin/),
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/)

Tuesday, May 13, 2025 06:00

[initial access broker](/category/initial-access-broker/)

* In the evolving cyberthreat landscape, Cisco Talos is witnessing a significant shift towards compartmentalized attack kill chains, where distinct stages — such as initial compromise and subsequent exploitation — are executed by multiple threat actors. This trend complicates traditional threat modeling and actor profiling, as it requires understanding the intricate relationships and interactions between various groups, explained in [the previous blog](https://blog.talosintelligence.com/redefining-initial-access-brokers).
* The traditional Diamond Model of Intrusion Analysis’ feature-centered approach (adversary, capability, infrastructure and victim) to pivoting can lead to inaccuracies when analyzing "compartmentalized" attack kill chains that involve multiple distinct threat actors. Without incorporating context of relationships, the model faces challenges in accurately profiling actors and constructing comprehensive threat models.
* We have identified several methods for analyzing compartmentalized attacks and propose an extended Diamond Model, which adds a “Relationship Layer” to enrich the context of the relationships between the four features.
* In a collaboration between Cisco Talos and [The Vertex Project](https://vertex.link), a Synapse model update has just been [published](https://synapse.docs.vertex.link/en/latest/synapse/changelog.html#v2-210-0-2025-05-12) which introduces the *entity:relationship* providing modeling support to this methodology.
* We illustrate our investigative approach and application of the extended Diamond Model for effective pivoting by examining the [ToyMaker](https://blog.talosintelligence.com/introducing-toymaker-an-initial-access-broker/) campaign, where ToyMaker functioned as a financially-motivated initial access (FIA) group, handing over access to the Cactus ransomware group.

---

## Impacts on defenders

The convergence of multiple threat actors operating within the same overall intrusion creates additional layers of obfuscation, making it difficult to differentiate the activities of one threat actor from another, or to identify when access has been handed off from one to the next. At each point where outsourcing occurs or access is handed off, the Diamond Model of the adversary changes. Likewise, the ability to leverage the output of kill chain analysis for the purpose of pivoting, clustering, and attribution becomes significantly more difficult as analysts may be forced to operate under the assumption that multiple actors are involved unless they can prove otherwise, where historically the opposite assumption was likely made.

Additionally, misattributing attacks due to tactics, techniques and procedures (TTPs) present in earlier stages of the intrusion may impact the way in which incident response or investigative activities are conducted post-compromise. They may also create uncertainty around the motivation(s) behind an attack or why an organization is being targeted in some cases.

Analysis processes and analytical models must be updated to reflect these new changes in the way that adversaries conduct intrusions, as existing methodologies often create more confusion than clarity.

## Introduction to threat modeling

[NIST SP 800-53 (Rev. 5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)) defines threat modeling as “a form of risk assessment that models aspects of the attack and defense sides of a logical entity, such as a piece of data, an application, a host, a system, or an environment.”

For many organizations, this involves evaluating their preventative, detective and corrective security controls from an adversarial perspective to identify deficiencies in their ability to prevent, detect or respond to threats based on specific tactics, techniques, and procedures (TTPs). For example, adversary emulation simulates an attack scenario and demonstrates how an organization could reasonably expect their security program to respond if a specific threat is encountered.

Intrusion analysis is the process of analyzing computer intrusion activity. This involves reconstructing intrusion attack timelines, analyzing forensic artifacts and identifying the scope and impact of activity. Intrusion analysis typically results in a better understanding of an attack or adversary, and may also result in the development of a model to reflect what is known about the threat. This model can then be used to support more effective detection content development and threat modeling activities in the future. The symbiotic relationship between intrusion analysis and threat modeling allows organizations to effectively incorporate new knowledge and information about threats and threat actors into their security programs to ensure continued effectiveness.

Over the past several years, different analytical models have been developed to assist with intrusion analysis and threat modeling that provide logical ways to organize contextual details about threats and threat actors so that they can be communicated and incorporated more effectively. Two of the most popular models are the [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf) and the [Kill Chain Model](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html).

![]...
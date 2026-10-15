---
title: Break the silence: Kazakhstan-nexus UAT-6275 targets CIS government organizations
url: https://blog.talosintelligence.com/break-the-silence-kazakhstan-nexus-uat-6275-targets-cis-government-organizations/
source: Over Security
date: 2026-10-14
fetch_date: 2026-10-15T06:45:10.597571
---

# Break the silence: Kazakhstan-nexus UAT-6275 targets CIS government organizations

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/UAT-6275-Header.jpg)

# Break the silence: Kazakhstan-nexus UAT-6275 targets CIS government organizations

By
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/)

Wednesday, October 14, 2026 10:00

[Threat Spotlight](/category/threat-spotlight/)
[APT](/category/apt/)

*This research was conducted jointly with Julian-Ferdinand Vögele of Recorded Future’s Insikt Group. Details of the joint research and presentation are available* [*here*](https://www.virusbulletin.com/uploads/pdf/conference/vb2026/papers/Break-the-silence-tracking-Silent-Lynx-through-exposed-infrastructure.pdf)*.*

* Cisco Talos identified UAT-6275 ([TAG-193](http://www.recordedfuture.com/blog/tag193-regional-espionage-operations) by Recorded Future) activity targeting government organizations across the Commonwealth of Independent States (CIS). Recovered artifacts show additional interest in water resources and energy. This focus is consistent with intelligence collection and may reflect the regional effects of the Russia–Ukraine war.
* In activity observed from June 2025 through August 2026, Talos identified four infection-chain types that use macro-enabled documents, PS2EXE downloaders, GitHub-hosted PowerShell, and a crafted WinRAR archive exploiting CVE-2025-8088. The recovered payloads include several custom reverse shells that provide interactive remote access.
* Three publicly accessible staging directories and GitHub repository history exposed payload builds, tool inventories, and changes to command-and-control (C2) infrastructure. These operational security lapses gave us direct visibility into the group's recent activity.
* The files recovered from the exposed infrastructure suggest preparation for post-compromise operations and potential activity against Linux hosts and internet-facing appliances.
* Talos assesses with medium confidence that UAT-6275 has a Kazakhstan nexus, based on infrastructure access, language artifacts, sample submissions, working hours analysis, and regional targeting interests.

---

## Background

Cisco Talos and Recorded Future Insikt Group jointly investigated UAT-6275 activity targeting government organizations across the Commonwealth of Independent States (CIS). The investigation uncovered three publicly accessible staging directories and a previously unreported GitHub repository used to host malicious scripts and payloads. These exposed assets provided visibility into the threat actor's malware development, infrastructure changes and preparations for additional intrusion activity.

Talos tracks this activity as UAT-6275, while Recorded Future tracks it as TAG-193. It overlaps with [Silent Lynx (first reported by Seqrite)](https://www.seqrite.com/blog/silent-lynx-apt-targeting-central-asian-entities/) and sits within a broader set of campaigns connected to [YoroTrooper](https://blog.talosintelligence.com/yorotrooper-espionage-campaign-cis-turkey-europe/), which we first reported in 2023.Subsequent research on [Tomiris (Kaspersky)](https://securelist.com/tomiris-called-they-want-their-turla-malware-back/109552/), [ShadowSilk (Group-IB)](https://www.group-ib.com/blog/shadowsilk/), [Cavalry Werewolf (BI.ZONE)](https://bi-zone.medium.com/cavalry-werewolf-raids-russias-public-sector-with-trusted-relationship-attacks-e19f7a5c83ef), and [Hydra Saiga (VMRay)](https://www.vmray.com/hydra-saiga-covert-espionage-and-infiltration-of-critical-utilities/) identified overlapping indicators across these reported clusters. We assess that UAT-6275 and YoroTrooper likely belong to the same broader activity cluster. However, we continue to track them separately because we have not observed direct indicator or toolset overlap between the two.

This post summarizes our joint Virus Bulletin 2026 white paper, “[Break the silence:](https://www.virusbulletin.com/uploads/pdf/conference/vb2026/papers/Break-the-silence-tracking-Silent-Lynx-through-exposed-infrastructure.pdf) [tracking](https://www.virusbulletin.com/uploads/pdf/conference/vb2026/papers/Break-the-silence-tracking-Silent-Lynx-through-exposed-infrastructure.pdf) [Silent Lynx through exposed infrastructure](https://www.virusbulletin.com/uploads/pdf/conference/vb2026/papers/Break-the-silence-tracking-Silent-Lynx-through-exposed-infrastructure.pdf)” which contains the full technical analysis and indicators of compromise (IOCs).

## Victimology

UAT-6275's targeting is concentrated in Central Asia and the wider CIS region. Across the reviewed campaigns, observed victims and lure themes span nine countries: Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan, Armenia, Azerbaijan, Russia, and Belarus.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/UAT-6275-6.jpg)

Figure 1. Regional targeting.

### Government and diplomatic affairs

UAT-6275 targets government institutions responsible for diplomacy, economic development, agriculture, and environmental management. These organizations hold information that can inform bilateral negotiations, economic planning, and regional security decisions.

Our network flow analysis identified activity involving a Tajik government entity shortly after [treaty](https://qazinform.com/news/majilis-ratifies-kazakhstan-tajikistan-treaty-on-allied-relations-87a9f5) discussions with Kazakhstan in March 2026 and a Belarusian government entity ahead of [a bilateral meeting](https://www.aa.com.tr/en/eurasia/kazakh-president-receives-belarusian-foreign-minister-to-discuss-bilateral-cooperation/3905389) in April. This timing may indicate an interest in regional diplomatic developments.

The decoy documents we recovered also suggest an interest in diplomatic relations, international trade, and aviation. Examples include a d...
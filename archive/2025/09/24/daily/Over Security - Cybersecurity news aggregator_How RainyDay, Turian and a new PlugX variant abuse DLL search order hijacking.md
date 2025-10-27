---
title: How RainyDay, Turian and a new PlugX variant abuse DLL search order hijacking
url: https://blog.talosintelligence.com/how-rainyday-turian-and-a-new-plugx-variant-abuse-dll-search-order-hijacking/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-24
fetch_date: 2025-10-02T20:34:58.236127
---

# How RainyDay, Turian and a new PlugX variant abuse DLL search order hijacking

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

![](/content/images/2025/09/Rainyday-DLL-header.jpg)

# How RainyDay, Turian and a new PlugX variant abuse DLL search order hijacking

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/),
[Takahiro Takeda](https://blog.talosintelligence.com/author/takahiro/)

Tuesday, September 23, 2025 14:00

[APT](/category/apt/)
[Threats](/category/threats/)

* Cisco Talos discovered a new campaign active since 2022, targeting the telecommunications and manufacturing sectors in Central and South Asian countries, delivering a new variant of [PlugX](https://malpedia.caad.fkie.fraunhofer.de/details/win.plugx).
* Talos discovered that the new variant’s features overlap with both the [RainyDay](https://attack.mitre.org/software/S0629/) and [Turian](https://malpedia.caad.fkie.fraunhofer.de/details/win.turian) backdoors, including abuse of the same legitimate applications for DLL sideloading, the XOR-RC4-RtlDecompressBuffer algorithm used to encrypt/decrypt payloads and the RC4 keys used.
* The configuration associated with this new variant of PlugX differs significantly from the standard PlugX configuration format. Instead, it adopts the same structure as RainyDay, enabling us to assess with medium confidence that this variant of PlugX can be attributed to [Naikon](https://attack.mitre.org/groups/G0019/).
* Although these malware families have historically been associated with campaigns attributed to Naikon or [BackdoorDiplomacy](https://www.bitdefender.com/files/News/CaseStudies/study/426/Bitdefender-PR-Whitepaper-BackdoorDiplomacy-creat6507-en-EN.pdf), our analysis of the victimology and technical malware implementation has uncovered evidence that indicates a potential connection between the two threat actors and suggests that they are the same group or that both are sourcing their tools from the same vendor.

---

## Overview

Cisco Talos has identified an ongoing campaign targeting the telecommunications and manufacturing sectors in Central and South Asian countries. Based on our analysis of collected evidence, we assess with medium confidence that this campaign can be attributed to [Naikon](https://attack.mitre.org/groups/G0019/), an active Chinese-speaking threat actor that has been operating since 2010. This assessment is based on analysis of the PlugX configuration format used during this campaign as well as the malware infection chain involved, which was very similar to their previous malware, RainyDay.

During the investigation and hunting efforts for RainyDay backdoors, Talos uncovered two significant findings. First, we found that several instances of the Turian backdoor and newly identified variants of the PlugX backdoor were abusing the same legitimate Mobile Popup Application as RainyDay to load themselves into memory. Second, we observed that the three malware families leverage loaders which not only have a similar XOR decryption function but also use the same RC4 key to decrypt the encrypted payload. Although we did not observe any activity associated with RainyDay or Turian during this campaign, this finding enables us to make assessments regarding attribution.

## Attribution

### Naikon

[Naikon](https://securelist.com/analysis/publications/69953/the-naikon-apt/) is a well-known [Chinese-speaking](https://threatconnect.com/wp-content/uploads/ThreatConnect-Project-Camera-Shy-Report.pdf) cyber [espionage](https://attack.mitre.org/groups/G0019/) group that has been active since at least 2010. This threat group has primarily targeted government, military, and civil organizations across Southeast Asia.

Naikon employs a variety of backdoors, including [Aira-body](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/), [Nebulae](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf) and RainyDay, along with numerous [customized hacking tools](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf) to maintain persistence and exfiltrate data from victims' network environments. Notably, [Symantec](https://www.security.com/threat-intelligence/telecoms-espionage-asia) reported the group has been using the RainyDay backdoor to target telecom operators in several Asian countries as part of a prolonged espionage campaign, which they traced back to 2020.

### BackdoorDiplomacy

[BackdoorDiplomacy](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/) is a threat group that has been active since at least 2017. The group has primarily targeted Ministries of Foreign Affairs and telecommunication companies across Africa, Europe, the Middle East and Asia.

Their primary tool of choice is [Turian](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/#reconnaissance-and-lateral-movement), believed to be an upgraded version of [Quarian](https://blog.talosintelligence.com/quarian/). ESET has noted similarities in the network encryption methods of Turian and a backdoor known as [Backdoor.Whitebird.1](https://vms.drweb.com/virus/?i=21512303). Bitdefender has suggested that Quarian, Turian and Whitebird may be different versions of the same backdoor. Bitdefender has also published a [blog](https://www.bitdefender.com/files/News/CaseStudies/study/426/Bitdefender-PR-Whitepaper-BackdoorDiplomacy-creat6507-en-EN.pdf) on attacks against telecommunication companies in the Middle East, which began in February 2022.

Talos compares Naikon and BackdoorDiplomacy using the diamond model in Figure 1.

![](https://blog.talosintelligence.com/content/images/2025/09/Rainyday-DLL-graphics_comparison.jpg)

Figure 1. Comparison between the Naikon and the BackdoorDiplomacy by using the diamond model.

## Relations in recent campaigns

While investigating the DLL search order ...
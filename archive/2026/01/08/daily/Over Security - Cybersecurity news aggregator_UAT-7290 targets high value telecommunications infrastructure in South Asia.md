---
title: UAT-7290 targets high value telecommunications infrastructure in South Asia
url: https://blog.talosintelligence.com/uat-7290/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-08
fetch_date: 2026-01-09T03:31:52.811514
---

# UAT-7290 targets high value telecommunications infrastructure in South Asia

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

# UAT-7290 targets high value telecommunications infrastructure in South Asia

By
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/),
[Brandon White](https://blog.talosintelligence.com/author/brandon/)

Thursday, January 8, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[APT](https://blog.talosintelligence.com/category/apt/)
[malware](https://blog.talosintelligence.com/category/malware/)

* Cisco Talos is disclosing a sophisticated threat actor we track as UAT-7290, who has been active since at least 2022.
* UAT-7290 is tasked with gaining initial access as well as conducting espionage focused intrusions against critical infrastructure entities in South Asia.
* UAT-7290's arsenal includes a malware family consisting of implants we call RushDrop, DriveSwitch, and SilentRaid.
* Our findings indicate that UAT-7290 conducts extensive technical reconnaissance of target organizations before carrying out intrusions.

---

Talos assesses with high confidence that UAT-7290 is a sophisticated threat actor falling under the China-nexus of Advanced Persistent Threat actors (APTs). UAT-7290 primarily targets telecommunications providers in South Asia. However, in recent months we have also seen UAT-7290 expand their targeting into Southeastern Europe.

In addition to conducting espionage focused attacks where UAT-7290 burrows deep inside a victim enterprise’s network infrastructure, their tactics, techniques and procedures (TTPs) and tooling suggests that this actor also establishes Operational Relay Box (ORBs) nodes. The ORB infrastructure may then be used by other China-nexus actors in their malicious operations, signifying UAT-7290's dual role as an espionage motivated threat actor as well as an initial access group.

Active since at least 2022, UAT-7290 has an expansive arsenal of tooling, including open-source malware, custom developed malware, and payloads for 1-day vulnerabilities in popular edge networking products. UAT-7290 primarily leverages a Linux based malware suite but may also utilize Windows based bespoke implants such as [RedLeaves](https://malpedia.caad.fkie.fraunhofer.de/details/win.redleaves) or [Shadowpad](https://malpedia.caad.fkie.fraunhofer.de/details/win.shadowpad) commonly linked to China-nexus threat actors.

Our findings suggest that the threat actor conducts extensive reconnaissance of target organizations before carrying out intrusions. UAT-7290 leverages one-day exploits and target-specific SSH brute force to compromise public facing edge devices to gain initial access and escalate privileges on compromised systems. The actor appears to rely on publicly available proof-of-concept exploit code as opposed to developing their own.

UAT-7290 shares overlapping TTPs with known China-nexus adversaries, including the exploitation of high-profile vulnerabilities in networking devices, use of open-source web shells for persistence, leveraging UDP listeners, and using compromised infrastructure to facilitate operations.

Specifically, we have observed technical indicators that overlap with [RedLeaves](https://malpedia.caad.fkie.fraunhofer.de/details/win.redleaves), a malware family attributed to [APT10](https://malpedia.caad.fkie.fraunhofer.de/actor/apt10) (a.k.a. MenuPass, POTASSIUM and Purple Typhoon), as well as infrastructure associated with [ShadowPad](https://malpedia.caad.fkie.fraunhofer.de/details/win.shadowpad), a malware family used by a variety of China-nexus adversaries.

Additionally, UAT-7290 shares a significant amount of overlap in victimology, infrastructure, and tooling with a group publicly reported by Recorded Future as Red Foxtrot. In a 2021 [report](https://go.recordedfuture.com/hubfs/reports/cta-2021-0616.pdf), Recorded Future linked Red Foxtrot to Chinese People’s Liberation Army (PLA) Unit 69010.

## UAT-7290's malware arsenal for edge devices

Talos currently tracks the Linux-based malware families associated with UAT-7290 in this intrusion as:

* RushDrop – The dropper that kickstarts the infection chain. RushDrop is also known as [ChronosRAT](https://unit42.paloaltonetworks.com/infiltration-of-global-telecom-networks/).
* DriveSwitch – A peripheral malware used to execute the main implant on the infected system.
* SilentRaid – The main implant in the intrusion meant to establish persistent access to compromised endpoints. It communicates with its command-and-control server (C2) and carries out tasks defined in the malware. SilentRaid is also known as [MystRodX](https://blog.xlab.qianxin.com/mystrodx_covert_dual-mode_backdoor_en/).

Another malware implanted on compromised devices by UAT-7290 is Bulbature. Bulbature, first disclosed by [Sekoia in late 2024](https://blog.sekoia.io/bulbature-beneath-the-waves-of-gobrat/), is an implant that is used to convert compromised devices into ORBs.

### RushDrop and DriveSwitch

RushDrop is a malware dropper that consists of three binaries encoded and embedded within it. RushDrop first makes rudimentary checks to ensure it is running on a legitimate system instead of a sandbox.

![](https://blog.talosintelligence.com/content/images/2026/01/data-src-image-3aed5baf-cb90-48bd-8808-0f86d96a810f.png)

Figure 1. RushDrop deleting itself if VM checks fail.

Then it either checks for the existence of, or creates a folder called “.pkgdb” in the current working directory of the dropper. RushDrop then decodes and drops three binaries to the “.pkgdb” folder:

* “daytime” - A malware family that simply executes a file called “chargen” from the current working directory. This executor is being tracked as DriveSwitch.
* “chargen” - The central implant of the infection chain, tracked as SilentRaid. SilentRaid communicates with its C2 serve...
---
title: Threat Roundup for April 28 to May 5
url: https://blog.talosintelligence.com/threat-roundup-0428-0505/
source: Over Security - Cybersecurity news aggregator
date: 2023-05-06
fetch_date: 2025-10-04T11:41:31.446515
---

# Threat Roundup for April 28 to May 5

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

# Threat Roundup for April 28 to May 5

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Friday, May 5, 2023 17:25

[Threat Roundup](https://blog.talosintelligence.com/category/threat-roundup/)

Today, Talos is publishing a glimpse into the most prevalent threats we've observed between April 28 and May 5. As with previous roundups, this post isn't meant to be an in-depth analysis. Instead, this post will summarize the threats we've observed by highlighting key behavioral characteristics, indicators of compromise, and discussing how our customers are automatically protected from these threats.

As a reminder, the information provided for the following threats in this post is non-exhaustive and current as of the date of publication. Additionally, please keep in mind that IOC searching is only one part of threat hunting. Spotting a single IOC does not necessarily indicate maliciousness. Detection and coverage for the following threats is subject to updates, pending additional threat or vulnerability analysis. For the most current information, please refer to your Firepower Management Center, [Snort.org](https://www.snort.org/), or [ClamAV.net](https://www.clamav.net/).

For each threat described below, this blog post only lists 25 of the associated file hashes and up to 25 IOCs for each category. An accompanying JSON file can be found [here](https://raw.githubusercontent.com/Cisco-Talos/Threat-Round-Up/master/2023/0505.json) that includes the complete list of file hashes, as well as all other IOCs from this post. A visual depiction of the MITRE ATT&CK techniques associated with each threat is also shown. In these images, the brightness of the technique indicates how prevalent it is across all threat files where dynamic analysis was conducted. There are five distinct shades that are used, with the darkest indicating that no files exhibited technique behavior and the brightest indicating that technique behavior was observed from 75 percent or more of the files.

The most prevalent threats highlighted in this roundup are:

| Threat Name | Type | Description |
| --- | --- | --- |
| Win.Packed.njRAT-9999411-0 | Packed | njRAT, also known as Bladabindi, is a remote access trojan (RAT) that allows attackers to execute commands on the infected host, log keystrokes and remotely turn on the victim's webcam and microphone. njRAT was developed by the Sparclyheason group. Some of the largest attacks using this malware date back to 2014. |
| Win.Dropper.Bifrost-9999421-0 | Dropper | Bifrost is a backdoor with more than 10 variants. Bifrost uses the typical server, server builder and client backdoor program configuration to allow a remote attacker who uses the client to execute arbitrary code on the compromised machine. The malware contains standard RAT features including a file manager, screen capture utility, keylogging, video recording, microphone and camera monitoring, and a process manager. To mark its presence in the system, Bifrost uses a mutex that may be named "Bif1234" or "Tr0gBot." |
| Win.Ransomware.Cerber-9999985-0 | Ransomware | Cerber is ransomware that encrypts documents, photos, databases and other important files. Historically, this malware would replace files with encrypted versions and add the file extension ".cerber," although in more recent campaigns, other file extensions are used. |
| Win.Dropper.Kuluoz-9999994-0 | Dropper | Kuluoz, sometimes known as "Asprox," is a modular remote access trojan that is also known to download and execute follow-on malware, such as fake antivirus software. Kuluoz is often delivered via spam emails pretending to be shipment delivery notifications or flight booking confirmations. |
| Win.Dropper.XtremeRAT-10000002-0 | Dropper | XtremeRAT is a remote access trojan active since 2010 that allows the attacker to eavesdrop on users and modify the running system. The source code for XtremeRAT, written in Delphi, was leaked online and has since been used by similar RATs. |
| Win.Dropper.Tofsee-10000005-0 | Dropper | Tofsee is multi-purpose malware that features several modules to carry out various activities such as sending spam messages, conducting click fraud, mining cryptocurrency and more. Infected systems become part of the Tofsee spam botnet and send large volumes of spam messages to infect additional systems and increase the size of the botnet under the operator's control. |
| Win.Trojan.Ramnit-10000021-1 | Trojan | Ramnit is a banking trojan that monitors web browser activity on an infected machine and collects login information from financial websites. It can also steal browser cookies and hide from popular anti-virus software. |

---

## Threat Breakdown

### Win.Packed.njRAT-9999411-0

#### Indicators of Compromise

* IOCs collected from dynamic analysis of 12 samples

| Registry Keys | Occurrences |
| --- | --- |
| `<HKCU>\ENVIRONMENT  Value Name: SEE_MASK_NOZONECHECKS` | 8 |
| `<HKCU>\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN  Value Name: 23556fb1360f366337f97c924e76ead3` | 3 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN  Value Name: 23556fb1360f366337f97c924e76ead3` | 3 |
| `<HKCU>\SOFTWARE\23556FB1360F366337F97C924E76EAD3` | 3 |
| `<HKCU>\SOFTWARE\23556FB1360F366337F97C924E76EAD3  Value Name: US` | 3 |
| `<HKCU>\SOFTWARE\BA4C12BEE3027D94DA5C81DB2D196BFD  Value Name: US` | 2 |
| `<HKCU>\SOFTWARE\BA4C12BEE3027D94DA5C81DB2D196BFD` | 2 |
| `<HKCU>\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN  Value Name: 5cd8f17f4086744065eb0992a09e05a2` | 1 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN  Value Name: 5cd8f17f4086744065eb0992a09e05a2` | 1 |
| `<HKCU>\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN  Value Name: ba4c12bee3027d94da5c81db2d196bfd` | 1 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN...
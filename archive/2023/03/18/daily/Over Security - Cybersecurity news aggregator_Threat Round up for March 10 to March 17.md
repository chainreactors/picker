---
title: Threat Round up for March 10 to March 17
url: https://blog.talosintelligence.com/threat-roundup-0310-0317/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-18
fetch_date: 2025-10-04T09:59:00.100116
---

# Threat Round up for March 10 to March 17

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

# Threat Roundup for March 10 to March 17

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Friday, March 17, 2023 15:52

[Threat Roundup](https://blog.talosintelligence.com/category/threat-roundup/)

Today, Talos is publishing a glimpse into the most prevalent threats we've observed between March 10 and March 17. As with previous roundups, this post isn't meant to be an in-depth analysis. Instead, this post will summarize the threats we've observed by highlighting key behavioral characteristics, indicators of compromise, and discussing how our customers are automatically protected from these threats.

As a reminder, the information provided for the following threats in this post is non-exhaustive and current as of the date of publication. Additionally, please keep in mind that IOC searching is only one part of threat hunting. Spotting a single IOC does not necessarily indicate maliciousness. Detection and coverage for the following threats is subject to updates, pending additional threat or vulnerability analysis. For the most current information, please refer to your Firepower Management Center, [Snort.org](https://www.snort.org/), or [ClamAV.net](https://www.clamav.net/).

For each threat described below, this blog post only lists 25 of the associated file hashes and up to 25 IOCs for each category. An accompanying JSON file can be found [here](https://raw.githubusercontent.com/Cisco-Talos/Threat-Round-Up/master/2023/0317.json) that includes the complete list of file hashes, as well as all other IOCs from this post. A visual depiction of the MITRE ATT&CK techniques associated with each threat is also shown. In these images, the brightness of the technique indicates how prevalent it is across all threat files where dynamic analysis was conducted. There are five distinct shades that are used, with the darkest indicating that no files exhibited technique behavior and the brightest indicating that technique behavior was observed from 75 percent or more of the files.

The most prevalent threats highlighted in this roundup are:

| Threat Name | Type | Description |
| --- | --- | --- |
| Win.Dropper.Locky-9992697-0 | Dropper | Locky is ransomware typically distributed via spam emails containing a maliciously crafted Microsoft Word document crafted to trick targets into enabling malicious macros. This family was originally released in 2016 and updated over the years with additional functionality. |
| Win.Dropper.LokiBot-9992313-0 | Dropper | Lokibot is an information-stealing malware designed to siphon off sensitive information stored on an infected device. It is modular in nature, supporting the ability to steal sensitive information from a number of popular applications. It is commonly pushed via malicious documents attached to spam emails. |
| Win.Dropper.Tofsee-9992775-0 | Dropper | Tofsee is multi-purpose malware that features a number of modules used to carry out various activities such as sending spam messages, conducting click fraud, mining cryptocurrency, and more. Infected systems become part of the Tofsee spam botnet and are used to send large volumes of spam messages in an effort to infect additional systems and increase the overall size of the botnet under the operator's control. |
| Win.Dropper.TrickBot-9992835-0 | Dropper | TrickBot is a banking trojan targeting sensitive information for certain financial institutions. This malware is frequently distributed through malicious spam campaigns. Many of these campaigns rely on downloaders for distribution, such as VB scripts. |
| Win.Dropper.Zeus-9992851-0 | Dropper | Zeus is a trojan that steals information such as banking credentials using methods such as key-logging and form-grabbing. |
| Win.Ransomware.Cerber-9992849-0 | Ransomware | Cerber is ransomware that encrypts documents, photos, databases and other important files. Historically, this malware would replace files with encrypted versions and add the file extension ".cerber," although in more recent campaigns, other file extensions are used. |
| Win.Virus.Expiro-9992651-0 | Virus | Expiro is a known file infector and information-stealer that hinders analysis with anti-debugging and anti-analysis tricks. |
| Win.Malware.Ursu-9993206-0 | Malware | Ursu is a generic malware that has numerous functions. It contacts a C2 server and performs code injection in the address space of legitimate processes, after which it achieves persistence and collects confidential data. Ursu is usually spread via email. |
| Win.Dropper.njRAT-9993044-0 | Dropper | njRAT, also known as Bladabindi, is a RAT that allows attackers to execute commands on the infected host, log keystrokes and remotely turn on the victim's webcam and microphone. njRAT was developed by the Sparclyheason group. Some of the largest attacks using this malware date back to 2014. |
| Win.Dropper.DarkKomet-9992898-0 | Dropper | DarkKomet is a freeware remote access trojan that was released by an independent software developer. It provides the same functionality as expected from a remote access tool, such as keylogging, webcam access, microphone access, remote desktop, URL download and program execution. |

---

## Threat Breakdown

### Win.Dropper.Locky-9992697-0

#### Indicators of Compromise

* IOCs collected from dynamic analysis of 18 samples

| Registry Keys | Occurrences |
| --- | --- |
| `<HKCU>\SOFTWARE\LOCAL APPWIZARD-GENERATED APPLICATIONS` | 17 |
| `<HKCU>\Software\Microsoft\<random, matching '[A-Z][a-z]{3,11}'>` | 7 |
| `<HKLM>\SYSTEM\CONTROLSET001\SERVICES\VSS\DIAG\VSSAPIPUBLISHER` | 6 |
| `<HKCU>\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\EXT\STATS\{761497BB-D6F0-462C-B6EB-D4DAF1D92D43}` | 5 |
| `<HKCU>\SOFTWARE\MICROSOFT\INTERNET EXPLORER\SEARCHSCOPES\{0633EE93-D776-472F-A0FF-E1416B8B2E3A}  Value Name: FaviconPath` | 4 |
| `<HKCU>\S...
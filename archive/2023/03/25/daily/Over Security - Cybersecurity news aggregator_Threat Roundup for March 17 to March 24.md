---
title: Threat Roundup for March 17 to March 24
url: https://blog.talosintelligence.com/threat-roundup-0317-0324/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-25
fetch_date: 2025-10-04T10:38:53.559836
---

# Threat Roundup for March 17 to March 24

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

# Threat Roundup for March 17 to March 24

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Friday, March 24, 2023 13:42

[Threat Roundup](https://blog.talosintelligence.com/category/threat-roundup/)

Today, Talos is publishing a glimpse into the most prevalent threats we've observed between March 17 and March 24. As with previous roundups, this post isn't meant to be an in-depth analysis. Instead, this post will summarize the threats we've observed by highlighting key behavioral characteristics, indicators of compromise, and discussing how our customers are automatically protected from these threats.

As a reminder, the information provided for the following threats in this post is non-exhaustive and current as of the date of publication. Additionally, please keep in mind that IOC searching is only one part of threat hunting. Spotting a single IOC does not necessarily indicate maliciousness. Detection and coverage for the following threats is subject to updates, pending additional threat or vulnerability analysis. For the most current information, please refer to your Firepower Management Center, [Snort.org](https://www.snort.org/), or [ClamAV.net](https://www.clamav.net/).

For each threat described below, this blog post only lists 25 of the associated file hashes and up to 25 IOCs for each category. An accompanying JSON file can be found [here](https://raw.githubusercontent.com/Cisco-Talos/Threat-Round-Up/master/2023/0324.json) that includes the complete list of file hashes, as well as all other IOCs from this post. A visual depiction of the MITRE ATT&CK techniques associated with each threat is also shown. In these images, the brightness of the technique indicates how prevalent it is across all threat files where dynamic analysis was conducted. There are five distinct shades that are used, with the darkest indicating that no files exhibited technique behavior and the brightest indicating that technique behavior was observed from 75 percent or more of the files.

The most prevalent threats highlighted in this roundup are:

| Threat Name | Type | Description |
| --- | --- | --- |
| Win.Dropper.Bifrost-9993163-0 | Dropper | Bifrost is a backdoor with more than 10 variants. Bifrost uses the typical server, server builder and client backdoor program configuration to allow a remote attacker who uses the client to execute arbitrary code on the compromised machine. Bifrost contains standard RAT features such as a file manager, screen capture utility, keylogging, video recording, microphone and camera monitoring, and a process manager. To mark its presence in the system, Bifrost uses a mutex that may be named "Bif1234" or "Tr0gBot." |
| Win.Dropper.Tofsee-9993367-0 | Dropper | Tofsee is multi-purpose malware that features several modules used to carry out various activities such as sending spam messages, conducting click fraud, mining cryptocurrency, and more. Infected systems become part of the Tofsee spam botnet and are used to send large volumes of spam messages to infect additional systems and increase the size of the botnet. |
| Win.Dropper.Cerber-9993689-0 | Dropper | Cerber is ransomware that encrypts documents, photos, databases and other important files. Historically, this malware would replace files with encrypted versions and add the file extension ".cerber," although in more recent campaigns, other file extensions are used. |
| Win.Trojan.DarkComet-9993855-1 | Trojan | DarkComet and related variants are a family of remote access trojans designed to provide an attacker with control over an infected system. Capabilities of this malware include the ability to download files from a user's machine, mechanisms for persistence and hiding, and the ability to send back usernames and passwords from the infected system. |
| Win.Packed.Zusy-9993358-0 | Packed | Zusy, also known as TinyBanker or Tinba, is a trojan that uses man-in-the-middle attacks to steal banking information. When executed, it injects itself into legitimate Windows processes such as "explorer.exe" and "winver.exe." When the user accesses a banking website, it displays a form to trick the user into submitting personal information. |
| Win.Packed.Upatre-9993687-0 | Packed | Upatre is a malicious downloader often used by exploit kits and phishing campaigns. Upatre downloads and executes malicious executables such as banking malware. |
| Win.Dropper.LokiBot-9993959-0 | Dropper | Lokibot is an information-stealing malware designed to siphon sensitive information stored on an infected device. It is modular in nature, supporting the ability to steal sensitive information from several popular applications. It is commonly pushed via malicious documents delivered via spam emails. |
| Win.Virus.Ramnit-9993699-0 | Virus | Ramnit is a banking trojan that monitors web browser activity on an infected machine and collects login information from financial websites. It also can steal browser cookies and attempts to hide from popular antivirus software. |

---

## Threat Breakdown

### Win.Dropper.Bifrost-9993163-0

#### Indicators of Compromise

* IOCs collected from dynamic analysis of 21 samples

| Registry Keys | Occurrences |
| --- | --- |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUNONCE  Value Name: wextract_cleanup0` | 18 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\ACTIVE SETUP\INSTALLED COMPONENTS\{3G4L2686-J4L1-X5MV-12RE-JFH5V38F5030}  Value Name: StubPath` | 2 |
| `<HKCU>\SOFTWARE\COFFIN OF EVIL  Value Name: FileName` | 2 |
| `<HKLM>\SYSTEM\CONTROLSET001\SERVICES\DFMIRAGE  Value Name: Type` | 2 |
| `<HKLM>\SYSTEM\CONTROLSET001\SERVICES\DFMIRAGE  Value Name: ErrorControl` | 2 |
| `<HKLM>\SYSTEM\CONTROLSET001\SERVICES\DFMIRAGE  Value Name: Tag` | 2 |
| `<HKLM>\SYSTEM\CONTROLSET001\SERVICES\DFMIRAGE  Value Name: ImagePath` | 2 |
...
---
title: Threat Roundup for March 24 to March 31
url: https://blog.talosintelligence.com/threat-roundup-0324-0331-2/
source: Over Security - Cybersecurity news aggregator
date: 2023-04-01
fetch_date: 2025-10-04T11:23:33.302655
---

# Threat Roundup for March 24 to March 31

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

# Threat Roundup for March 24 to March 31

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Friday, March 31, 2023 13:41

[Threat Roundup](https://blog.talosintelligence.com/category/threat-roundup/)

Today, Talos is publishing a glimpse into the most prevalent threats we've observed between March 24 and March 31. As with previous roundups, this post isn't meant to be an in-depth analysis. Instead, this post will summarize the threats we've observed by highlighting key behavioral characteristics, indicators of compromise, and discussing how our customers are automatically protected from these threats.

As a reminder, the information provided for the following threats in this post is non-exhaustive and current as of the date of publication. Additionally, please keep in mind that IOC searching is only one part of threat hunting. Spotting a single IOC does not necessarily indicate maliciousness. Detection and coverage for the following threats is subject to updates, pending additional threat or vulnerability analysis. For the most current information, please refer to your Firepower Management Center, [Snort.org](https://www.snort.org/), or [ClamAV.net](https://www.clamav.net/).

For each threat described below, this blog post only lists 25 of the associated file hashes and up to 25 IOCs for each category. An accompanying JSON file can be found [here](https://raw.githubusercontent.com/Cisco-Talos/Threat-Round-Up/master/2023/0331.json) that includes the complete list of file hashes, as well as all other IOCs from this post. A visual depiction of the MITRE ATT&CK techniques associated with each threat is also shown. In these images, the brightness of the technique indicates how prevalent it is across all threat files where dynamic analysis was conducted. There are five distinct shades that are used, with the darkest indicating that no files exhibited technique behavior and the brightest indicating that technique behavior was observed from 75 percent or more of the files.

The most prevalent threats highlighted in this roundup are:

| Threat Name | Type | Description |
| --- | --- | --- |
| Win.Ransomware.TeslaCrypt-9994144-1 | Ransomware | TeslaCrypt is a well-known ransomware family that encrypts a user's files with strong encryption and demands Bitcoin in exchange for a file decryption service. A flaw in the encryption algorithm was discovered that allowed files to be decrypted without paying the ransomware, and eventually, the malware developers released the master key allowing all encrypted files to be recovered easily. |
| Win.Ransomware.Cerber-9994145-0 | Ransomware | Cerber is ransomware that encrypts documents, photos, databases and other important files. Historically, this malware would replace files with encrypted versions and add the file extension ".cerber," although in more recent campaigns, other file extensions are used. |
| Win.Dropper.Tofsee-9994178-0 | Dropper | Tofsee is multi-purpose malware that features a number of modules used to carry out various activities such as sending spam messages, conducting click fraud, mining cryptocurrency and more. Infected systems become part of the botnet and send large volumes of spam messages to infect additional systems and increase the size of the botnet under the operator's control. |
| Win.Dropper.Formbook-9994385-0 | Dropper | Formbook is an information stealer that attempts to collect sensitive information from an infected machine by logging keystrokes, stealing saved web browser credentials, and monitoring information copied to the clipboard. |
| Win.Dropper.Kovter-9994588-1 | Dropper | Kovter is known for its fileless persistence mechanism. This family of malware creates several malicious registry entries that store its malicious code. Kovter can reinfect a system, even if the file system has been cleaned of the infection. The malware traditionally spreads ransomware and click-fraud malware. |
| Win.Dropper.TinyBanker-9994341-1 | Dropper | TinyBanker, also known as Zusy or Tinba, is a trojan that uses man-in-the-middle attacks to steal banking information. When executed, it injects itself into legitimate Windows processes such as "explorer.exe" and "winver.exe." When the user accesses a banking website, it displays a form to trick the user into submitting personal information. |
| Win.Dropper.Emotet-9994401-0 | Dropper | Emotet is one of the most widely distributed and active malware families today. It is a highly modular threat that can deliver a wide variety of payloads. Emotet is commonly delivered via Microsoft Office documents with macros, sent as attachments on malicious emails. |
| Win.Dropper.Fareit-9994421-1 | Dropper | The Fareit trojan is an information stealer with the functionality to download and install other malware. |
| Win.Dropper.DarkComet-9994524-1 | Dropper | DarkComet and related variants are a family of remote access trojans designed to provide an attacker with control over an infected system. This malware can download files from a user's machine and contains mechanisms for persistence and hiding, along with the ability to send back usernames and passwords from the infected system. |

---

## Threat Breakdown

### Win.Ransomware.TeslaCrypt-9994144-1

#### Indicators of Compromise

* IOCs collected from dynamic analysis of 17 samples

| Registry Keys | Occurrences |
| --- | --- |
| `<HKCU>\SOFTWARE\XXXSYS` | 17 |
| `<HKCU>\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN  Value Name: v23-deadbeef` | 17 |
| `<HKCU>\SOFTWARE\XXXSYS  Value Name: ID` | 17 |
| `<HKCU>\Software\<random, matching '[A-Z0-9]{14,16}'>` | 17 |
| `<HKCU>\Software\<random, matching '[A-Z0-9]{14,16}'>  Value Name: data` | 17 |

| Mutexes | Occurrences |
| --- | --- |
| `z_a_skh495ldfsgjl2935345` | 17 |

| IP Addresses contacted by malware. Does not indicate ...
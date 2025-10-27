---
title: Threat Roundup (Feb. 24 - March 3)
url: https://blog.talosintelligence.com/threat-roundup-feb-24-march-3-2023/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-04
fetch_date: 2025-10-04T08:40:04.176532
---

# Threat Roundup (Feb. 24 - March 3)

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

# Threat Roundup (Feb. 24 - March 3)

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Friday, March 3, 2023 15:00

[Threat Roundup](https://blog.talosintelligence.com/category/threat-roundup/)

Today, Talos is publishing a glimpse into the most prevalent threats we've observed between Feb. 24 and March 3. As with previous roundups, this post isn't meant to be an in-depth analysis. Instead, this post will summarize the threats we've observed by highlighting key behavioral characteristics, indicators of compromise, and discussing how our customers are automatically protected from these threats.

As a reminder, the information provided for the following threats in this post is non-exhaustive and current as of the date of publication. Additionally, please keep in mind that IOC searching is only one part of threat hunting. Spotting a single IOC does not necessarily indicate maliciousness. Detection and coverage for the following threats is subject to updates, pending additional threat or vulnerability analysis. For the most current information, please refer to your Firepower Management Center, [Snort.org](https://www.snort.org), or [ClamAV.net](https://www.clamav.net).

For each threat described below, this blog post only lists 25 of the associated file hashes and up to 25 IOCs for each category. An accompanying JSON file can be found here that includes the complete list of file hashes, as well as all other IOCs from this post. A visual depiction of the MITRE ATT&CK techniques associated with each threat is also shown. In these images, the brightness of the technique indicates how prevalent it is across all threat files where dynamic analysis was conducted. There are five distinct shades that are used, with the darkest indicating that no files exhibited technique behavior and the brightest indicating that technique behavior was observed from 75 percent or more of the files.

The most prevalent threats highlighted in this roundup are:

| Threat Name | Type | Description |
| --- | --- | --- |
| Win.Dropper.Nanocore-9988753-1 | Dropper | Nanocore is a .NET remote access trojan. Its source code has been leaked several times, making it widely available. Like other RATs, it allows full control of the system, including recording video and audio, stealing passwords, downloading files and recording keystrokes. |
| Win.Dropper.NetWire-9988754-0 | Dropper | NetWire is a remote access trojan (RAT) that allows attackers to execute commands on the infected host, log keystrokes, interact with a webcam, remote desktop, and read data from connected USB devices. NetWire is commonly delivered through Microsoft Office documents with macros, sent as attachments on malicious emails. |
| Win.Dropper.Raccoon-9988770-0 | Dropper | Raccoon is an information-stealer written in C++. It collects system information and a list of installed applications, then steals cookies and autofill form details from various browsers (Chrome, Internet Explorer, Firefox, Waterfox, SeaMonkey and Pale Moon). The malware can also steal credentials from email clients like Outlook, Thunderbird and Foxmail, then scans the infected device for information about valid cryptocurrency wallets. |
| Win.Dropper.LokiBot-9988785-0 | Dropper | Lokibot is an information-stealing malware designed to siphon sensitive information stored on an infected device. It is modular in nature, supporting the ability to steal sensitive information from several popular applications. It is commonly pushed via malicious documents delivered via spam emails. |
| Win.Trojan.Tofsee-9989403-0 | Trojan | Tofsee is multi-purpose malware that features a number of modules used to carry out various activities such as sending spam messages, conducting click fraud, mining cryptocurrency, and more. Infected systems become part of the Tofsee spam botnet and send large volumes of spam messages to infect additional systems and increase the size of the botnet under the operator's control. |
| Win.Dropper.Glupteba-9988873-0 | Dropper | Glupteba is a multi-purpose trojan that is known to use the infected machine to mine cryptocurrency and steals sensitive information like usernames and passwords, spreads over the network using exploits like EternalBlue, and leverages a rootkit component to remain hidden. Glupteba has also been observed using the bitcoin blockchain to store configuration information. |
| Win.Virus.Ramnit-9988782-0 | Virus | Ramnit is a banking trojan that monitors web browser activity on an infected machine and collects login information from financial websites. It also has the ability to steal browser cookies and attempts to hide from popular antivirus software. |
| Win.Dropper.Zeus-9988750-0 | Dropper | Zeus is a trojan that steals information such as banking credentials using methods such as key-logging and form-grabbing. |

---

## Threat Breakdown

### Win.Dropper.Nanocore-9988753-1

#### Indicators of Compromise

* IOCs collected from dynamic analysis of 20 samples

| Registry Keys | Occurrences |
| --- | --- |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN Value Name: AutoUpdate` | 14 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN Value Name: AGP Manager` | 12 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN Value Name: WindowsUpdate` | 10 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN Value Name: Chrome` | 7 |
| `<HKCU>\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\POLICIES\SYSTEM Value Name: DisableTaskMgr` | 5 |
| `<HKCU>\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\POLICIES\SYSTEM` | 5 |
| `<HKLM>\SOFTWARE\MICROSOFT\WINDOWS NT\CURRENTVERSION\SCHEDULE\TASKCACHE\TASKS Value Name: Path` | 1 |
| `<HKLM>\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN Value Name: Explorere` | 1 |
| `<HKCU>\SOFTWARE\...
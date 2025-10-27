---
title: N-IOCs to Rule Them All
url: https://dfir.ch/posts/n-iocs/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:07:45.429383
---

# N-IOCs to Rule Them All

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# N-IOCs to Rule Them All

31 Dec 2023

**Table of Contents**

* [Introduction](#pintroductionp)
* [IOC #1: Defender Exclusions](#pioc-1-defender-exclusionsp)
* [IOC #2: Powershell Logs](#pioc-2-powershell-logsp)
* [IOC #3: Scheduled Tasks](#pioc-3-scheduled-tasksp)
* [IOC #4: Run Keys](#pioc-4-run-keysp)
* [IOC #5: Startup Folder](#pioc-5-startup-folderp)
* [IOC #6: Appdata](#pioc-6-appdatap)
* [IOC #7: Dynamic DNS (DynDNS)](#pioc-7-dynamic-dns-dyndnsp)
* [IOC #8: High-Port || IP-Only](#pioc-8-high-port--ip-onlyp)
* [Conclusion](#pconclusionp)
* [References](#preferencesp)
* [Samples](#psamplesp)

## Introduction

We analyzed the top ten malware families in Switzerland (according to govcert.ch) during the period April - December 2022 to find patterns and overlaps in the forensic artifacts that a successful infection leaves on an endpoint.

We explicitly did not analyze the infection chain (how the infection happens â macros, wscript, hta, etc.), but rather the traces left by the second stage, i.e., the final malware executed on the endpoint.

This analysis resulted in eight artifacts that a SOC analyst or an incident responder can leverage to find infections of these malware families (and probably other malware strains) with a reasonably high probability. These artifacts can also be leveraged for monitoring purposes or threat hunting on the network.

We analyzed the following malware families in more detail:
![Malware families](/images/n-iocs/1.png "Malware families")

As this research was done for my talk at the FIRST Conference 2023 in Montreal, the original slides are available [here](https://www.first.org/resources/papers/conf2023/FIRSTCON23-TLP-CLEAR-Berger-N-IOCs-To-Rule-Them-All.pdf). A huge thank you goes to my two proofreaders [Kostas](https://twitter.com/Kostastsale), and my team colleague [Asger](https://twitter.com/hackerkartellet).

## IOC #1: Defender Exclusions

![Nanocore RAT](/images/n-iocs/2.png "Nanocore RAT")

Figure 1: Excluding a file (or a folder path) from Windows Defender scans

During the analysis, it was found that in many cases, the malware sets up an exception for Windows Defender so that a directory or file is not scanned, as depicted in Figure 1 by Nanocore RAT. However, the creation of such an exception is recorded in an event log (ID 5007, Windows Defender, Figure 2). If (event-)logs are already collected centrally in a SIEM, collecting and monitoring the Windows Defender event log is also recommended to monitor for newly created exclusions specifically.

Monitoring the ID 5007 event log has an additional advantage. Apart from detecting malware infections, it can also identify misconfigurations, like overly broad exclusion rules that cover entire drives or directories.

![Windows Defender Event Log](/images/n-iocs/3.png "Windows Defender Event Log")

Figure 2: Windows Defender Event Log

An alternative way to find these exceptions on endpoints is to extract the exceptions directly from the registry (HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths). This approach is feasible if code execution is possible on all endpoints in the network (for example, via an EDR or the req query command).

[@DebugPrivilege](https://twitter.com/DebugPrivilege) covered Windows Defender AV logs extensively. [1]

## IOC #2: Powershell Logs

![Ave Maria RAT](/images/n-iocs/5.png "Ave Maria RAT")

Figure 3: Malware sets up persistency in the Registry with PowerShell

Interestingly, various malware families used PowerShell code to set up persistency on the endpoint within our analysis timeframe. There is an example of the Ave Maria RAT depicted in Figure 3. We suspect that the malware uses PowerShell instead of the Windows API to fool or circumvent the logging mechanism by some EDR products and also because PowerShell Script Block logging is not an enabled by default. When PowerShell Script Block Logging has been enabled, executed PowerShell code is stored inside the Microsoft-Windows-PowerShell event log (Figure 4).

![Scriptblock](/images/n-iocs/7.png "Scriptblock")

Figure 4: PowerShell Event Log (Scriptblock)

Enable PowerShell Script Block Logging via Group Policy on all endpoints in the network. These logs are a goldmine for finding adversaries inside the network and for forensics during an incident response investigation. [2]

**Extra Mile:** When working on an IR case or conducting a compromise assessment, always check the PowerShell logs, even if logging is not enabled globally. You might be surprised by what you will find :)

![Suspicious keywords](/images/n-iocs/8.png "Suspicious keywords")

Figure 5: Suspicious keywords

## IOC #3: Scheduled Tasks

![QakBot](/images/n-iocs/9.png "QakBot")

Figure 6: Malware creates a new Scheduled Task

Creating scheduled tasks for the periodic execution of malware is a classic (Figure 6). With the open-source tool Velociraptor (Velociraptor is an advanced digital forensic and incident response tool that enhances your visibility into your endpoints [3]) and the built-in Velociraptor hunt “Windows.System.TaskScheduler”, we can collect all tasks from the endpoints where Velociraptor is running. The example above was tweaked for my FIRST presentation, but apart from the DLL file and location, the same command line was used by QakBot in the past.

![TaskScheduler](/images/n-iocs/10.png "TaskScheduler")

Figure 7: Collecting all Scheduled Tasks with Velociraptor

Velociraptor offers a range of pre-made searches, known as *hunts* [4,5], and a query language called *Velociraptor Query Language* (VQL). This allows for convenient processing of data in notebooks built into the Velociraptor interface. [9] As a result, searches like finding DLL files or other files in user directories are relatively simple. (Figure 8).

![Velociraptor Notebook](/images/n-iocs/11.png "Velociraptor Notebook")

Figure 8: Examination of the collected Tasks with Velociraptor

In addition to the live data (the Tasks file) on the endpoints, various traces can also be found in the security event logs (task creation, evidence of file execution, deletion, etc.). There is even a separate event log for TaskScheduler, which could contain further traces about the executed tasks.

**Security.evtx**

* 4698: A scheduled task was created
* 4699: A scheduled task was deleted
* 4700: A scheduled task was enabled
* 4701: A scheduled task was disabled
* 4702: A scheduled task was updated

**Microsoft-Windows-TaskScheduler%4Operational.evtx**

* 140: User  updated Task Scheduler task
* 141: User  deleted Task Scheduler task

## IOC #4: Run Keys

![404 Keylogger](/images/n-iocs/12.png "404 Keylogger")

Figure 9: Creating a new run key in the registry

With the help of the Run-Key within the registry, malware will automatically start when a login occurs under the user account where the Run-Key is created.

With the open-source software Sysmon [6], we can monitor the creation of registry keys (ID 13).

![Monitoring registry keys](/images/n-iocs/13.png "Monitoring registry keys")

Figure 10: Monitoring registry keys with Sysmon

Or we can use Velociraptor (again) to read all run keys from the user and system hives.

![Collecting run keys](/images/n-iocs/14.png "Collecting run keys")

Figure 11: Collecting run keys from the registry keys with Velociraptor

Data collected in this way can, in turn, be easily searched using Velociraptor’s query language (VQL). In the following example, we searched for files in the AppData directory.

![Velociraptor Notebook](/images/n-iocs/15.png "Velociraptor Notebook")

Figure 12: Filtering the collected data with Velociraptor

## IOC #5: Startup Folder

![Persistence in the Startup Folder](/images/n-iocs/16.png "Persistence in the Startup Folder")

Figure 13: Persistence in the Startup Folder

Another classic persistence technique is to use the Startup folder. Files in this directory...
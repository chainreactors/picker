---
title: Trawler - PowerShell Script To Help Incident Responders Discover Adversary Persistence Mechanisms
url: https://buaq.net/go-174512.html
source: unSafe.sh - 不安全
date: 2023-08-16
fetch_date: 2025-10-04T11:59:17.905549
---

# Trawler - PowerShell Script To Help Incident Responders Discover Adversary Persistence Mechanisms

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ab93958420f366f012f66cb60f53ca1c.jpg)

Trawler - PowerShell Script To Help Incident Responders Discover Adversary Persistence Mechanisms

What is it?Trawler is a PowerShell script designed to help Incident Responders discover pot
*2023-8-15 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-174512.htm)
阅读量:36
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiY9kq-VlmQ2IPwPbzUkWZkGRpKdmY0KHmM-OqvdIxCG5crNfC_iXNOeHyun8_ZtH2NaDqCfSd5kXcvUquqVBo88fJrRimXs3Jzj4KtynCFeV1x0RoApBDhAXFlpnt7HlS4muwO0R63pfdwuB62qCkarMamWPqJHR2Kj3lYSAGc8zL0Scs3dzhXnGT-nqSv/w400-h334/Trawler_1_logo.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiY9kq-VlmQ2IPwPbzUkWZkGRpKdmY0KHmM-OqvdIxCG5crNfC_iXNOeHyun8_ZtH2NaDqCfSd5kXcvUquqVBo88fJrRimXs3Jzj4KtynCFeV1x0RoApBDhAXFlpnt7HlS4muwO0R63pfdwuB62qCkarMamWPqJHR2Kj3lYSAGc8zL0Scs3dzhXnGT-nqSv/s2000/Trawler_1_logo.png)

## What is it?

Trawler is a PowerShell script designed to help Incident Responders discover potential [indicators of compromise](https://www.kitploit.com/search/label/Indicators%20of%20Compromise "indicators of compromise") on Windows hosts, primarily focused on persistence mechanisms including Scheduled Tasks, Services, Registry Modifications, Startup Items, Binary Modifications and more.

Currently, trawler can detect most of the persistence techniques specifically called out by MITRE and Atomic Red Team with more detections being added on a regular basis.

## Main Features

* Scanning Windows OS for a variety of persistence techniques (Listed below)
* CSV Output with MITRE Technique and Investigation Jumpstart Metadata
* Analysis and Remediation Guidance Documentation ([https://github.com/joeavanzato/Trawler/wiki/Analysis-and-Remediation-Guidance](https://github.com/joeavanzato/Trawler/wiki/Analysis-and-Remediation-Guidance "https://github.com/joeavanzato/Trawler/wiki/Analysis-and-Remediation-Guidance"))
* Dynamic Risk Assignment for each detection
* Built-in Allow Lists for common Windows configurations spanning Windows 10/Server 2012|2016|2019|2022 to reduce noise
* Capture persistence metadata from 'golden' enterprise image for use as a dynamic allow-list at runtime
* Analyze mounted disk images via drive re-targeting

## How do I use it?

Just download and run trawler.ps1 from an Administrative PowerShell/cmd prompt - any detections will be displayed in the console as well as written to a CSV ('detections.csv') in the current working directory. The generated CSV will contain Detection Name, Source, Risk, Metadata and the relevant MITRE Technique.

Or use this one-liner from an Administrative PowerShell terminal:

```
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/joeavanzato/Trawler/main/trawler.ps1'))
```

Certain detections have allow-lists built-in to help remove noise from default Windows configurations (10/2016/2019/2022) - expected Scheduled Tasks, Services, etc. Of course, it is always possible for attackers to hijack these directly and masquerade with great detail as a default OS process - take care to use multiple forms of analysis and detection when dealing with skillful adversaries.

If you have examples or ideas for additional detections, please feel free to submit an Issue or PR with relevant technical details/references - the code-base is a little messy right now and will be cleaned up over time.

Additionally, if you identify obvious false positives, please let me know by opening an issue or PR on GitHub! The obvious culprits for this will be non-standard COMs, Services or Tasks.

### CLI Parameters

```
-scanoptions : Tab-through possible detections and select a sub-set using comma-delimited terms (eg. .\trawler.ps1 -scanoptions Services,Processes)
-hide : Suppress Detection output to console
-snapshot : Capture a "persistence snapshot" of the current system, defaulting to "$PSScriptRoot\snapshot.csv"
-snapshotpath : Define a custom file-path for saving snapshot output to.
-outpath : Define a custom file-path for saving detection output to (defaults to "$PSScriptRoot\detections.csv")
-loadsnapshot : Define the path for an existing snapshot file to load as an allow-list reference
-drivetarget : Define the variable for a mounted target drive (eg. .\trawler.ps1 -targetdrive "D:") - using this alone leads to an 'assumed homedrive' variable of C: for analysis purposes
```

## What separates this from PersistenceSniper?

PersistenceSniper is an awesome tool - I've used it heavily in the past - but there are a few key points that differentiate these utilities

* trawler is (currently) a local utility - it would be pretty straight-forward to wrap it in a loop and use WinRM/PowerShell Sessions to execute it on remote hosts though
* trawler implements allow-listing for many 'noisy' detections to help remove expected detections from default configurations of Windows (10/2016/2019/2022) and these are constantly being updated
  + PersistenceSniper (for the most part) does not contain any type of allow-listing - therefore, there is more noise generated when considering items such as Services, Scheduled Tasks, general COM DLL scanning, etc.
* trawler's output is much more simplified - Name, Risk, Source, MITRE Technique and Metadata are the only items provided for each detection to help analysts jump-start their persistence hunting efforts
* Regex is used in many checks to help detect 'suspicious' keywords or patterns in various critical areas including scanned file contents, registry values, etc.
* trawler supports 'snapshotting' a system (for example, an enterprise golden image) then using the generated snapshot as an allow-list to reduce noise.
* trawler supports 'drive-retargeting' to check dead-boxes mounted to an analysis machine.

Overall, these tools are extremely similar but approach the problem from slightly different angles - [PersistenceSniper](https://www.kitploit.com/search/label/PersistenceSniper "PersistenceSniper") provides all information back to the analyst for review while Trawler tries to limit what is returned to only results that are likely to be potential adversary persistence mechanisms. As such, there is a possibility for false-negatives with trawler if an adversary completely mimics an allow-listed item.

## Tuning to your environment

Trawler supports loading an allow-list from a 'snapshot' - to do this requires two steps.

1. Run '.\trawler.ps1 -snapshot' on a "Golden Image" representing the servers in your environment - once complete, in addition to the standard 'detections.csv' a file named 'snapshots.csv' will be generated
2. This file can then be used as input to trawler when running on other hosts and the data will be loaded dynamically as an allow-list for each appropriate detection
   1. '.\trawler.ps1' -loadsnapshot "path\to\snapshot.csv"

That's it - all relevant detections will then draw from the snapshot file as an allow-list to reduce noise and identify any potential changes to the base image that may have occurred.

(Allow-listing is implemented for most of the checks but not all - still being actively implemented)

## Drive ReTargeting

Often during an investigation, analysts may end up mounting a new drive that represents an imaged Windows device - Trawler now partially supports scanning these mounted drives through the use of the '-drivetarget' parameter.

At runtime, Trawler will re-target temporary script-level variables for use in checking file-based artifacts and also will attempt to load relevant Registry Hives (HKLM\SOFTWARE, HKLM\SYSTEM, NTUSER.DATs, USRCLASS.DATs) underneath HKLM/HKU and prefixed by 'ANAL...
---
title: When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Three
url: https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to_029886864.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-03-22
fetch_date: 2026-03-23T04:23:21.865590
---

# When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Three

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Sunday, March 22, 2026

### When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Three

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEkitV4IXvhCrD8b468es9XysjNO5fAITKnqv6RQGB4p-gUArgh2A_1afD-3VZpqbWBSu2uC8F51x2veTelrFUOKn2XnfQomnuf9oT8WbrHtyFtenWJfvVEDS-1sjVoep3x3vVLRYTdQGghbyhyphenhyphen_BOHf4lIYX3CQB2MjQht_nXLmRTFhWf9nt-/s320/Misc_3700.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEkitV4IXvhCrD8b468es9XysjNO5fAITKnqv6RQGB4p-gUArgh2A_1afD-3VZpqbWBSu2uC8F51x2veTelrFUOKn2XnfQomnuf9oT8WbrHtyFtenWJfvVEDS-1sjVoep3x3vVLRYTdQGghbyhyphenhyphen_BOHf4lIYX3CQB2MjQht_nXLmRTFhWf9nt-/s792/Misc_3700.png)

Dear blog readers,

 Continuing the "[When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Two](https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to.html)" blog post series in this post I'll continue analyzing the next [malicious software](https://ddanchev.blogspot.com/2022/06/a-compilation-of-known-conti-ransomware_21.html) binary which I obtained by [data mining](https://ddanchev.blogspot.com/search?q=conti) [Conti Leaks](https://archive.org/details/rewards-for-justice-01) with a lot of success.

**The actual malicious software binary location URL:**

hxxp://shighil.com/dl2.exe

MD5: c2055b7fbaa041d9f68b9d5df9b45edd
SHA-1: e4bd443bd4ce9029290dcd4bb47cb1a01f3b1b06
SHA-256: 342f04c4720590c40d24078d46d9b19d8175565f0af460598171d58f5ffc48f3

Here's the actual analysis.

Executive Summary

dl2.exe is a Windows x86\_64 PE executable (849.5 KB) exhibiting characteristics consistent with malicious software. The binary demonstrates sophisticated capabilities including registry manipulation, dynamic API resolution, file system operations, and system information gathering. Analysis identified multiple high-risk behaviors typical of malware, particularly around persistence mechanisms and anti-analysis techniques.

## Key Findings

### Critical Capabilities (High Severity)

1. Registry Manipulation

* Functions: sub\_419118, sub\_419228, sub\_419198, sub\_4192e8, sub\_4193c4, sub\_40da8c, sub\_422ef4, sub\_418ffc
* APIs Used: RegOpenKeyA, RegSetValue, RegCreateKey, RegQueryValue
* Registry Keys Accessed:
  + Software\Microsoft\Windows\CurrentVersion
  + RestrictRun and NoRun keys (policy restriction keys)
* Risk: High - Can modify system configuration and establish persistence

2. Dynamic API Resolution

* Function: sub\_40b868 (0x40b868)
* APIs Used: GetProcAddress, LoadLibrary, GetModuleHandle
* Risk: High - Common evasion technique to bypass static analysis and API monitoring
* Details: Dynamically resolves function addresses at runtime, making static detection more difficult

### Medium Severity Capabilities

3. File System Operations

* Functions: sub\_423718, sub\_4228a4, sub\_423360, sub\_41aeec
* APIs Used: CreateFile, DeleteFile, MoveFile, CopyFile, FindFirstFile, FindNextFile, GetFileAttributes
* Risk: Medium - Can manipulate files on the system

4. System Information Gathering

* Functions: sub\_4542b0, sub\_40f0ac, sub\_46df44, sub\_46d3bc
* APIs Used: GetVersionExA, GetSystemInfo, GetComputerName, GetUserName
* Risk: Medium - Fingerprints the system, likely for profiling or anti-VM checks

5. Memory Manipulation

* Functions: sub\_4540e0, sub\_453df0, sub\_453d10, sub\_453b50
* APIs Used: VirtualAlloc, VirtualProtect, HeapAlloc, HeapFree
* Risk: Medium - Can change memory protection flags, potentially indicating code injection or unpacking behavior

6. Mutex Creation

* Function: sub\_46be50 (0x46be50)
* API Used: CreateMutex
* Risk: Medium - Commonly used for single-instance enforcement in malware

### Security Features (Informational)

7. Stack Protection Mechanisms

* Stack Cookie Initialization (sub\_45ca90 at 0x45ca90): Uses multiple entropy sources (GetSystemTimeAsFileTime, GetCurrentProcessId, GetCurrentThreadId, GetTickCount, QueryPerformanceCounter) to generate stack cookies
* Stack Guard Pages (sub\_4540e0 at 0x4540e0): Implements guard pages using VirtualQuery, VirtualAlloc, and VirtualProtect

### Notable Observations

* Entry Point: 0x4545a0 (\_start)
* Main Function: 0x46d9f4 (jumps to 0x46da1c)
* Imported Libraries: ADVAPI32.dll, GDI32.dll, KERNEL32.dll, OLEAUT32.dll, SHELL32.dll, SHLWAPI.dll, USER32.dll, WINSPOOL.DRV, comdlg32.dll, ole32.dll, oledlg.dll
* Total Functions Identified: 2,616
* No Network APIs Detected: No direct socket, HTTP, or network communication APIs were found in the analyzed functions (analysis incomplete)
* No Obvious Encryption Strings: No strings matching common encryption algorithm names were found

## Malware Classification

Based on identified capabilities, this binary exhibits behaviors consistent with:

* System modification malware (registry manipulation, file operations)
* Information stealer (system information gathering)
* Potentially a dropper/loader (dynamic API resolution, memory manipulation)

Critical Malicious Capabilities Identified

### 1. Windows Policy Restriction Manipulation (HIGH SEVERITY)

The binary targets multiple Windows policy registry keys designed to restrict user actions:

Registry Keys Targeted:

* Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
  + NoRun - Prevents running programs via Run dialog
  + RestrictRun - Restricts which programs can execute
  + NoDrives - Hides/restricts drive access
  + NoNetConnectDisconnect - Prevents network connections/disconnections
  + NoRecentDocsHistory - Disables recent documents
  + NoClose - Prevents closing windows
* Software\Microsoft\Windows\CurrentVersion\Policies\Network
  + NoEntireNetwork - Restricts network browsing
* Software\Microsoft\Windows\CurrentVersion\Policies\Comdlg32
  + Common dialog restrictions

Functions Involved:

* sub\_419228 (0x419228) - Writes DWORD registry values
* sub\_4192e8 (0x4192e8) - Writes/deletes registry string values and keys
* sub\_419198 (0x419198) - Reads registry integer values
* sub\_4193c4 (0x4193c4) - Reads registry string values
* sub\_419118 (0x419118) - Opens registry keys
* sub\_40b0d4 (0x40b0d4) - Saves settings to registry
* sub\_432610 (0x432610) - Batch registry operations

### 2. Console Output Manipulation

* sub\_46be50 (0x46be50) - Opens CONOUT$ device handle, likely for output redirection or hiding console output

### 3. Persistence & Configuration

The binary uses both registry and INI file storage for configuration, with registry taking precedence. This dual-storage approach suggests:

* Fallback mechanisms for different environments
* Ability to persist settings across system changes

Summary of Malicious Findings

This binary is highly malicious with the following critical behaviors:

### Primary Threat: System Restriction Malware

The binary manipulates Windows Group Policy registry keys to:

* Disable the Run dialog (NoRun)
* Restrict program execution (RestrictRun)
* Hide/disable drives (NoDrives)
* Prevent network operations (NoNetConnectDisconnect, NoEntireNetwork)
* Disable system features (NoClose, NoRecentDocsHistory)

This behavior is characteristic of ransomware preparation, system lockers, or destructive malware that prevents users from:

* Running recovery tools
* Accessing safe mode
* Using system utilities
* Connecting to networks for help

### Additional Malicious Capabilities:

1. Dynamic API resolution - Evades static analysis
2. Dual persisten...
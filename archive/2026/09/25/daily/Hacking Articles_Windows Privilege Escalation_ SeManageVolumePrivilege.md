---
title: Windows Privilege Escalation: SeManageVolumePrivilege
url: https://www.hackingarticles.in/windows-privilege-escalation-semanagevolumeprivilege/
source: Hacking Articles
date: 2026-09-25
fetch_date: 2026-09-26T06:50:23.898882
---

# Windows Privilege Escalation: SeManageVolumePrivilege

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel's Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)
»* [Windows Privilege Escalation: SeManageVolumePrivilege](https://www.hackingarticles.in/windows-privilege-escalation-semanagevolumeprivilege/)
»

[Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)

# Windows Privilege Escalation: SeManageVolumePrivilege

[September 25, 2026](https://www.hackingarticles.in/windows-privilege-escalation-semanagevolumeprivilege/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

This article demonstrates how attackers abuse the SeManageVolumePrivilege Windows token right to escalate from a standard user to SYSTEM on a Windows 10 target. The technique exploits direct API access to NTFS volumes — a capability normally restricted to administrators — to rewrite directory ACLs across C:\Windows. With write control over the Windows directory, attackers plant malicious DLLs into system paths and trigger high-privileged processes to load them. The walkthrough covers three distinct exploitation paths: Print Spooler DLL hijacking, WBEM tzres.dll substitution, and Windows Error Reporting abuse via WerTrigger.

### **Table of Contents:**

* Introduction to SeManageVolumePrivilege
* Lab Environment
* Confirming the Target User
* Assigning SeManageVolumePrivilege via Local Security Policy
  + Opening secpol.msc
  + Navigating to User Rights Assignment
  + Adding the Target User
* Establishing the Initial Reverse Shell
* Enabling the Privilege with EnableAllTokenPrivs
  + Staging the Script on the Attacker Machine
  + Fetching and Executing the Script on the Target
* Abusing SeManageVolumePrivilege to Rewrite C:\Windows ACLs
  + Auditing the Initial ACL
  + Running SeManageVolumeExploit
* Exploitation 1: Print Spooler DLL Hijacking → SYSTEM
  + Generating the Printconfig.dll Payload
  + Deploying the DLL and Triggering the Spooler
  + Receiving the SYSTEM Shell
* Exploitation 2: WBEM tzres.dll Hijacking → NT AUTHORITY\NETWORK SERVICE
  + Generating the tzres.dll Payload
  + Deploying tzres.dll and Triggering WMI
  + Landing as NT AUTHORITY\NETWORK SERVICE
* Exploitation 3: Windows Error Reporting (WerTrigger) → SYSTEM
  + Generating the phoneinfo.dll Payload
  + Downloading WerTrigger Components
  + Deploying and Executing WerTrigger
  + Receiving the SYSTEM Shell via WerTrigger
* Mitigation Strategies
  + Audit and Restrict User Rights Assignments
  + Apply the Principle of Least Privilege
  + Monitor Privilege Activation Events
  + Detect ACL Modification on Protected Directories
  + Control DLL Hijacking Vectors
  + Restrict Print Spooler and Limit WER Exposure
  + Enforce Endpoint Detection and Response (EDR) Coverage
* Conclusion

### **Introduction to SeManageVolumePrivilege**

SeManageVolumePrivilege is a Windows token privilege that allows a process to call the SetFileValidData() API — a function that lets an application write valid data to an allocated file region without zero-padding. While this privilege exists primarily for database and backup software that must initialise large files quickly, granting it to an ordinary user account opens a severe privilege escalation vector.

The privilege maps to the “Perform volume maintenance tasks” user right in the Local Security Policy. When assigned to a non-administrator, the token carries the right but leaves it in a Disabled state; Windows does not activate optional privileges automatically. An attacker who holds this disabled privilege can enable it programmatically using token manipulation tools, then wield it to call Windows kernel APIs that modify NTFS directory security descriptors — effectively granting arbitrary write access to the Windows directory tree.

Once BUILTIN\Users holds Modify (M) and Full Control (F) permissions on C:\Windows, the entire attack surface changes. Any DLL that a SYSTEM-level process loads from a writable path becomes a hijacking target. This article chains that write primitive into three separate SYSTEM shells, demonstrating the breadth of post-exploitation options the privilege unlocks.

### **Lab Environment**

* Attacker: Kali Linux — IP 192.168.1.8
* Target: Windows 10 (MSEDGEWIN10, build 10.0.17763.379) — IP 192.168.1.12
* Target user: raj — standard local account with no administrative privileges![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvkPf0O_3SPTN4MtKficmVDkN32zMU8rJOTbpFTGJZFcKAu7kZzd3bWAESZ_z6_6WHedy1FIv4b6KTDJktf8caEhaOLJxhnKnVuzSAL8nPTnkYQqrYHBque2lG_AuC9ewFdyihQJuV_HmL4m8ZAJquHrW6wZkly-D7dLZT5WPZSCtw21OU9vL80OS-zFEZ/s1600/0.png)

### **Confirming the Target User**

Before assigning any privilege, the attacker enumerates the target user with following command to confirm the account is a standard, non-privileged user.

```
net user raj
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjER_EqXPT2-rt6OTQmyQQhhgkMX09btiwfIFTirU-wr9ATODPlmqw1D6EtQc5S3eiQx-t6szXYRSdi8uaJfvsQdO33vqihVJZXuHKHufIWQYPSdDUd6kNLTf0gcjBhjKTtKoeo5XStQfeiYtWjUNM2CbtIOXBZ8muWoDnUKQD0jioo1wjNepylfuYlHgFI/s1600/1.png)

The output shows that raj belongs only to the Remote Desktop Users, Remote Management Use, and Users local groups, with no Global Group memberships. The account is active and has a valid logon history — a realistic foothold scenario.

### **Assigning SeManageVolumePrivilege via Local Security Policy**

The attacker (or a misconfiguring administrator) grants raj the “Perform volume maintenance tasks” right through the Local Security Policy editor. This simulates a real-world misconfiguration — for example, a DBA or backup operator account granted this right by an administrator who underestimates its security implications.

### **Opening secpol.msc**

The administrator presses Win+R and types secpol.msc to launch the Local Security Policy MMC snap-in with elevated privileges.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDUxd5P2DXgb98oOb3SWp8H-usEVDl2fqIjci5OznynssNBN34sNgsUmEiq823aQO7treHxes-3LYsnXqh5cvNr4lD3NtqW07eui2tnhRHSmcL5St73dEHGOU6bTHcAt9mW-b9Cp8Q1K9W35jpaaEaMOSyrI4Bz_YNX9u_lxiAHwKBLozIsGkHPOOApLx3/s1600/3.png)

### **Navigating to User Rights Assignment**

Inside the snap-in, the administrator goes to Local Policies > User Rights Assignment. The right pane lists all user rights. The administrator locates “Perform volume maintenance tasks,” which currently assigns only to Administrators, and double-clicks the entry.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmtpJ29SpAdadH60vpfIIj3GO0J3YHyxzdOtyH0hiR6ShaZqMk1_Y52UIJwBFXJbKAAMZzgWR7rvfzOhnQQrL8uPovRXrYmnqyjaOfAhTCjkaXViLfLRLDfI-pJUjWftzHEk-W5uuR-l54uSJ-Iixse1bKPtveX_2dnCygRMat1zhf1ydIQMjxrNWCXdNj/s1600/4.png)

### **Adding the Target User**

The Properties dialog reveals that only the Administrators group currently holds this right. The administrator clicks Add User or Group to expand access.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhYio-AHFwMOoEeFJWzOcufrbWRq_h_oROvDMchZDaJxbgoBE9zjoTEodoenj4Yvkg76TOtHnzXxC9E0vZX9YqVwivOYAJcdLZ1bI14z9EBuPf9NVwyo4qavkq7mcWHBOlOKZJzDumIsnPjWDKB0LrXi5DzdMNbwFJX82MxWZXQXAzfg4AANzOwmc2-ntS/s1600/5.png)

After clicking Add User or Group, the administrator types MSEDGEWIN10\raj and confirms. The policy now lists both Administrators and MSEDGEWIN10\raj as holders of SeManageVolumePrivilege — a dangerous misconfiguration that an attacker can exploit t...
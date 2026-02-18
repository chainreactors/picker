---
title: Windows Event Log Analysis - Investigating Kerberos & AD Attacks
url: https://www.hackingdream.net/2026/02/windows-event-log-analysis-investigating-kerberos-ad-attacks.html
source: Hacking Dream
date: 2026-02-17
fetch_date: 2026-02-18T04:15:09.593146
---

# Windows Event Log Analysis - Investigating Kerberos & AD Attacks

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

### Windows Event Log Analysis - Investigating Kerberos & AD Attacks

[February 18, 2026](https://www.hackingdream.net/2026/02/windows-event-log-analysis-investigating-kerberos-ad-attacks.html "permanent link")

Windows Event Log Analysis: Red Team Guide to Kerberos & AD Attacks

# Windows Event Log Analysis: Investigating Kerberos & AD Attacks

*Updated on February 18, 2026*

**Table of Contents**

* [Prerequisites](#prerequisites)
* [1. Initial Triage & Investigation Workflow](#initial-triage)
* [2. Deep Technical Breakdown – Event IDs & Attack Mapping](#deep-technical-breakdown)
* [3. Practical Log Analysis Techniques & Tooling](#practical-analysis)
* [4. SIEM-Based Detection & Correlation](#siem-detection)
* [5. Red Team Insight (The Adversary Perspective)](#red-team-insight)
* [Conclusion](#conclusion)

You've got the call. The Domain Controller (DC) is acting strange, a high-privilege user just logged in from a subnet that doesn't exist, and the CISO is breathing down your neck. You've been handed a zip file full of `.evtx` files and asked to find the bleeding.

Now, I've spent years on the offensive side executing these exact attacks. I know exactly what artifacts I leave behind when I'm sloppy, and I know what I try to hide when I'm being careful. But here's the reality: on a Windows domain, **everything is a transaction**. Even the stealthiest Golden Ticket leaves a footprint if you know where to look.

[![Windows Event Log Analysis - Investigating Kerberos & AD Attacks](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy1Xif8WmJipUKpPsucuNMQ7AutXbPSa25pbMb732Eg6AF0DQtvu1g5Qa3MOxBTAo8gfRLgibqEGxKer2SvgX9zriTGB7Eba6IjSxNZkuKTWszQVpIHCapyNm7agjaxLxGBkxtfskN6drNqBsvgBJrrR1H4flsQuGzO3Wl2UFVYjGzu1BiFIZV9UxonyBa/w640-h358/Windows-Event-Log-Analysis---Investigating-Kerberos-&-AD-Attacks.jpg "Windows Event Log Analysis - Investigating Kerberos & AD Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy1Xif8WmJipUKpPsucuNMQ7AutXbPSa25pbMb732Eg6AF0DQtvu1g5Qa3MOxBTAo8gfRLgibqEGxKer2SvgX9zriTGB7Eba6IjSxNZkuKTWszQVpIHCapyNm7agjaxLxGBkxtfskN6drNqBsvgBJrrR1H4flsQuGzO3Wl2UFVYjGzu1BiFIZV9UxonyBa/s1024/Windows-Event-Log-Analysis---Investigating-Kerberos-%26-AD-Attacks.jpg)

In this guide, we're going to break down how to perform **Windows Event Log Analysis** for Kerberos-based attacks and Active Directory abuse. We aren't just looking for "bad" events; we are reconstructing the crime scene using the exact methodology I use to evade you.  if you need more info on how the Kerberos authentication and attacks work in detail - you can check out our article on [Understanding Kerberos Authentication and its Attacks](https://www.hackingdream.net/2025/03/understanding-kerberos-authentication-and-its-attacks.html)

## Prerequisites

To follow along effectively, you need a forensic workstation set up to parse these logs without modifying them.

* **Target Logs:** `Security.evtx` (Authentication), `System.evtx` (Services/Reboots), `Directory Service.evtx` (AD Object Access).
* **Access:** You don't need Domain Admin to analyze logs, just a workstation with the right tools.
* **Tools:**
  + **Chainsaw** (Rapid artifact parsing)
  + **Hayabusa** (Threat hunting tool)
  + **EvtxECmd & Timeline Explorer** (Eric Zimmerman's suite)
  + **PowerShell** (Native filtering)

```
# Install Hayabusa (Windows via Scoop)
scoop bucket add extras
scoop install hayabusa

# Chainsaw setup
# Download binary, no install needed
chainsaw.exe --help
```

## 1. Initial Triage & Investigation Workflow

When you first open a 20GB `Security.evtx` file, it's easy to get overwhelmed. Don't just start `grep`-ing for "Error". You need a workflow that mirrors how an attacker moves.

### Prioritization Strategy

1. **Security.evtx:** This is your primary source of truth. It holds the "Who, What, Where" of authentication.
2. **System.evtx:** Look here for service installations (PSEXEC leaves traces here) and specific lateral movement indicators like Service Control Manager events (Event ID 7045).
3. **Directory Service.evtx:** Critical for detecting DCSync, Shadow Credentials, and AdminSDHolder abuse.

### Building the Timeline (The Anchor Event)

Find an **Anchor Event**. This is a confirmed bad event - maybe the time the ransomware note dropped or the time a specific user reported a lockout.

* **Work Backward:** How did they get the privileges to execute the anchor event?
* **Work Forward:** What did they do after they got those privileges?

### The Forensic Pivot

You must pivot to track lateral movement. Here is the operational loop:

1. **Identify Suspicious User:** Find a compromised account (e.g., `backup_admin`).
2. **Filter by UserID (SID):** See every logon event for that user.
3. **Identify Source IP:** In Event 4624, look at the "Source Network Address."
4. **Pivot to IP:** Filter for that IP address to see *who else* logged in from that compromised machine. This reveals the attacker's pivot point.

**Operational Check:** If you see a Domain Admin logging in from a workstation that typically only houses marketing interns, you have a confirmed compromise. For more on domain controller attack patterns, see our red teamer guide on [Penetration Testing Domain Controllers](https://www.hackingdream.net/2024/02/pentesting-domain-controllers-cheatsheet.html) - this can be very helpful in figuring out how the attacker infiltrated the network.

## 2. Deep Technical Breakdown – Event IDs & Attack Mapping

Let's map specific Red Team attacks to their Blue Team artifacts using advanced **Windows Event Log Analysis**.

### 2.1 Credential Access: Roasting Attacks

Attacking offline material is my favorite way to get passwords without touching LSASS.

#### Kerberoasting

**The Attack:** I request a TGS (Service Ticket) for a service account (SQL, IIS). I take the ticket offline and crack the RC4-HMAC hash.

**The Artifact:** Event **4769** (Kerberos Service Ticket Requested).

**Red Flags:**

* **Encryption Type:** `0x17` (RC4). Modern domains use AES (`0x11` or `0x12`). If I force RC4, I'm likely cracking it.
* **Ticket Options:** `0x40810000` (Forwardable, Renewable, Canonicalize).
* **Service Name:** Not `krbtgt` or `$` machine accounts.

#### AS-REP Roasting

**The Attack:** I find a user with "Do not require Kerberos preauthentication" enabled. I ask the DC for a TGT. It gives it to me, encrypted with the user's password. I crack it.

...
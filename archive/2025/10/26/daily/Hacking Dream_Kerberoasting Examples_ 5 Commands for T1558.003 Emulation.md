---
title: Kerberoasting Examples: 5 Commands for T1558.003 Emulation
url: https://www.hackingdream.net/2025/10/kerberoasting-explained-Commands-for-T1558.003-emulation-purple-team.html
source: Hacking Dream
date: 2025-10-26
fetch_date: 2025-10-27T16:50:32.254796
---

# Kerberoasting Examples: 5 Commands for T1558.003 Emulation

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

### Kerberoasting Examples: 5 Commands for T1558.003 Emulation

[October 26, 2025](https://www.hackingdream.net/2025/10/kerberoasting-explained-Commands-for-T1558.003-emulation-purple-team.html "permanent link")

Kerberoasting Examples: 5 Commands for T1558.003

# Kerberoasting Examples: 5 Commands for T1558.003

*Updated on October 26, 2025*

Understanding practical **Kerberoasting examples** is crucial for any security professional looking to defend an Active Directory environment. This post-exploitation technique, outlined in [MITRE ATT&CK T1558.003](https://attack.mitre.org/techniques/T1558/003/), allows attackers to request service tickets for accounts with Service Principal Names (SPNs) and crack their passwords offline. Here, we dive into five diverse command-line simulations to help you recognize and mitigate this threat.

|  |
| --- |
| [![Kerberoasting Examples: 5 Commands for T1558.003 Emulation](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRm2F177CSloWv6W_Qb8SqTqOxvOsuZVq_pp2n4S0emRIC-bM7oswcUuz2P3uYNFLXxoTI2oo4-xRpZb8pJu6jamrPvdeO9cA8rnsyHfvYnojBPMCf2Pp86l9hOQOvu-TGtttbINonD_5b5SncCHuOzTs4tBf_8Z5F8BQJTaMfS9WhQMzI1G8zt-90eK4/w640-h456/Kerberoasting-Examples-5-Commands-for-T1558.003-Emulation.jpg "Kerberoasting Examples: 5 Commands for T1558.003 Emulation")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRm2F177CSloWv6W_Qb8SqTqOxvOsuZVq_pp2n4S0emRIC-bM7oswcUuz2P3uYNFLXxoTI2oo4-xRpZb8pJu6jamrPvdeO9cA8rnsyHfvYnojBPMCf2Pp86l9hOQOvu-TGtttbINonD_5b5SncCHuOzTs4tBf_8Z5F8BQJTaMfS9WhQMzI1G8zt-90eK4/s1024/Kerberoasting-Examples-5-Commands-for-T1558.003-Emulation.jpg) |
| Kerberoasting - T1558.003 Emulation |

Table of Contents

* [1. In-Memory Kerberoasting with PowerShell & .NET](#in-memory-kerberoasting)
* [2. The Classic: Kerberoasting with Rubeus](#classic-kerberoasting)
* [3. The Cross-Platform Attack: Impacket from Linux](#cross-platform-attack)
* [4. Stealthy Reconnaissance with PowerView](#stealthy-recon)
* [5. Native Windows Kerberoasting with setspn and klist](#native-windows-kerberoasting)

## 1. In-Memory Kerberoasting with PowerShell & .NET

### The Scenario

An attacker has gained initial access to a workstation as a standard domain user. They want to find and crack the password hash of a high-privilege service account without dropping any tools to disk, using only built-in Windows capabilities.

### The Command

```
# Find a target user with a Service Principal Name (SPN)
$SPNUser = "svc_mssql"

# Request the service ticket using .NET classes
$ErrorActionPreference = "SilentlyContinue"
Add-Type -AssemblyName System.IdentityModel
$SPN = (Get-ADUser -Identity $SPNUser -Properties ServicePrincipalName).ServicePrincipalName[0]
New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $SPN
```

### How It Works

* **Add-Type -AssemblyName System.IdentityModel:** This loads the necessary .NET assembly into the current PowerShell session, giving access to Kerberos-related classes.
* **$SPN = ...:** This line retrieves the SPN string for the target user (svc\_mssql) from Active Directory.
* **New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken:** This is the core of the attack. It uses a .NET method to request a Kerberos Ticket Granting Service (TGS) ticket for the specified SPN. Windows caches this ticket in memory. An attacker would then use a second tool (like Mimikatz) to extract the ticket from memory to crack it offline.

#### Purple Team Focus: What to Look For

**Log Source:** Windows Security Event ID 4769 (A Kerberos service ticket was requested) on the Domain Controller.

**Detection Logic:** Look for a high volume of 4769 events from a single source host, especially if the user is requesting tickets for multiple, distinct services in a short period. Correlate this with PowerShell Script Block Logging (Event ID 4104), which would show the use of `System.IdentityModel.Tokens.KerberosRequestorSecurityToken`. The service name in the 4769 event will match the SPN being targeted.

**SIEM/EDR Alerts:** "Suspicious Kerberos Ticket Request," "Potential Kerberoasting via .NET," "Anomalous PowerShell Activity."

**Mitigation:** Use strong, long (25+ characters), and complex passwords for all service accounts. Implement Group Managed Service Accounts (gMSA), which have automatically managed, complex passwords that are not susceptible to offline cracking in the same way. For more details, review [Microsoft's documentation on securing service accounts](INSERT\_INTERNAL\_URL).

## 2. The Classic: Kerberoasting with Rubeus

### The Scenario

An attacker has uploaded their offensive toolkit to a compromised server. They now use Rubeus, a popular C# tool, to automate the process of finding all Kerberoastable accounts and dumping their service ticket hashes into a file for offline cracking.

### The Command

```
# Execute Rubeus from memory if possible, otherwise from disk
.\Rubeus.exe kerberoast /outfile:hashes.txt /format:hashcat
```

### How It Works

* **.\Rubeus.exe:** Executes the Rubeus tool.
* **kerberoast:** This is the specific action module within Rubeus that performs the attack. It automatically discovers all users with SPNs, requests a TGS ticket for each one, and extracts the encrypted portion.
* **/outfile:hashes.txt:** Specifies that the extracted hashes should be saved to a file named hashes.txt.
* **/format:hashcat:** Instructs Rubeus to format the hashes in a way that is immediately usable by the Hashcat password cracking tool.

#### Purple Team Focus: What to Look For

**Log Source:** Sysmon Event ID 1 (Process Creation) and Windows Security Event ID 4769 (A Kerberos service ticket was requested).

**Detection Logic:** Create a rule that alerts on the execution of `Rubeus.exe` or any process with command-line arguments containing `kerberoast`. Correlate this process execution with a subsequent flood of Event ID 4769s originating from the same machine. Look for tickets requested with the RC4-HMAC encryption type, as this is often targeted because it's faster to crack.

**SIEM/EDR Alerts:** "Known Offensive Security Tool Detected: Rubeus," "Potential Kerberoasting Activity," "Anomalous TGS Ticket Requests."

**Mitigation:** Use Application Control policies (like AppLocker or WDAC) to block the execution of unauthorized or known malicious tools. Ensure service accounts use modern encryption standards like AES-256 by config...
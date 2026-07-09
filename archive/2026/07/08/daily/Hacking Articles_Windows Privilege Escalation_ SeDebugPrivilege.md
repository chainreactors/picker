---
title: Windows Privilege Escalation: SeDebugPrivilege
url: https://www.hackingarticles.in/windows-privilege-escalation-sedebugprivilege/
source: Hacking Articles
date: 2026-07-08
fetch_date: 2026-07-09T05:55:54.183470
---

# Windows Privilege Escalation: SeDebugPrivilege

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
»* [Windows Privilege Escalation: SeDebugPrivilege](https://www.hackingarticles.in/windows-privilege-escalation-sedebugprivilege/)
»

[Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)

# Windows Privilege Escalation: SeDebugPrivilege

[July 8, 2026July 8, 2026](https://www.hackingarticles.in/windows-privilege-escalation-sedebugprivilege/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

This article delivers an end-to-end walkthrough of how a single delegated user right — SeDebugPrivilege — collapses the security boundary between a standard domain user and full administrative control of a Windows Domain Controller. The narrative opens by explaining what the privilege authorises, then builds the exact misconfiguration in a lab: a fresh domain user is created, granted the Debug programs right through Group Policy, and verified over a remote PowerShell session. From that single foothold, four independent exploitation chains are executed against the same Domain Controller. The first dumps LSASS with a signed Microsoft tool and recovers the Domain Administrator’s NTLM hash offline. The second migrates a Meterpreter session into winlogon.exe to land a live SYSTEM shell. The third and fourth chains use a purpose-built token-duplication utility to spawn either an interactive SYSTEM prompt or a reverse shell back to the attacker. The article closes with concrete mitigation guidance covering policy hygiene, LSA Protection, Credential Guard, and the detection opportunities each technique leaves behind.

### **Table of Contents**

* Introduction
* Lab Environment
* Understanding SeDebugPrivilege
* Creating the Domain User
* Assigning SeDebugPrivilege via Group Policy
* Enforcing the Policy
* Verifying the Privilege Remotely
* Exploitation 1 — LSASS Dump with ProcDump and pypykatz
* Exploitation 2 — Meterpreter Migration to winlogon.exe
* Exploitation 3 — SeDebugPrivesc Standalone Exploit
* Mitigation Strategies
* Conclusion

### **Introduction**

**SeDebugPrivilege** is one of the **most dangerous rights an attacker can inherit on a Windows host**. It grants a user the ability to open, read, and write the memory of any process on the system — including the Local Security Authority Subsystem Service (LSASS), the process responsible for caching credentials of every user currently logged on. Once a low-privileged domain account is granted this right, the path to full domain compromise becomes short: dump LSASS, extract secrets, and pivot as an administrator — or borrow the token of any SYSTEM process on the machine and skip the credential recovery step entirely. This article walks through the assignment of **SeDebugPrivilege via Group Policy, verifies the privilege from a remote session, and demonstrates several distinct exploitation chains that each end with SYSTEM or Domain Administrator access on an Active Directory environment**.

### **Lab Environment**

The demonstration targets a Windows Server Domain Controller (DC) belonging to the ignite.local domain, reachable at 192.168.1.11. The attacker operates from a Kali Linux host at 192.168.1.17 using Evil-WinRM for remote PowerShell access. A standard domain user account named raaj is created and later assigned SeDebugPrivilege through Group Policy, simulating a common misconfiguration.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIqX_VHBTsJoTJTY098JrzPcIvvWUhSQau871DjVvaZqKpb0vLgdw6ZTUxMX-HMYhKJKuAklYBzda2Bu1JtyEJanpPterSZUcuwp1DgCH3gLPtpw5ruGjIyq4M8qg478YNfwS4iY7BNyBvAuIJfcEBKvoC22PSZ8e5TqCDQSv2BkpCZ-hHsUgk9-IHUdyI/s1600/0.png)

### **Understanding SeDebugPrivilege**

**SeDebugPrivilege**, exposed in policy editors as “Debug programs”, **allows a security principal to attach a debugger to any process** — including those running under NT AUTHORITY\SYSTEM. Windows originally reserved this right for developers troubleshooting kernel-level and system-service issues, but in practice, it is functionally equivalent to full local administrative access. Holders of the privilege can read the private memory of protected system processes, inject shellcode into them, or impersonate their access tokens. Because LSASS runs as SYSTEM and stores cached NTLM hashes and Kerberos tickets in its address space, any account with SeDebugPrivilege on a Domain Controller effectively controls the domain.

By default, only members of the Administrators group are granted this right. When it is delegated to a lower-privileged user or group — often for legitimate but poorly scoped reasons such as supporting a monitoring agent — the assignment becomes a direct path to privilege escalation.

### **Creating the Domain User**

The attack scenario begins on the Domain Controller, where the administrator provisions a new standard domain account named **raaj** with the password **Password@1**. The /domain switch tells the net user utility to create the object in Active Directory rather than in the local SAM database, and the command completes without elevating the account to any administrative group.

```
net user raaj Password@1 /add /domain
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp0smY5GIv2-pv1NL34ZrpunsX3s2JGfui1u7zIudLIk9WQKAGQCOWKbS8LcigybIuCMeX69CnnapYUhTWwZsJg9dfnyKMrxi-u941_NNdPhYiY0HyKFQo3WkxuMCERK1_97Q3s6RSDyB6x7BuVFjP3kGRa5dUU_YfH7h_82JnoEANm1BqS_lqgLlury7T/s1600/1.png)

The image above confirms the account is created successfully in the domain.

### **Assigning SeDebugPrivilege via Group Policy**

With the account in place, the next step opens the **Group Policy Management Console** (GPMC) — the standard tool for editing domain-wide policy objects. The console launches directly from an elevated command prompt using its Microsoft Management Console snap-in name.

```
gpmc.msc
```

The GPMC window loads once the command executes.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiltS_r0Am4cqC_Eq0JRyuffoWLBjrND1Jz6xHQbE5oq-CJ7k_xod9BTjyi2pf6t0XMWfqBoA-eNtlKrzy-rYVOGqnPBPXSVBbOtFSxb1vBsFt4ZuES8ixAL-luw0lXnWCUlfj0kT6veMGO_sX4i88ZSyG9IFqkC8SLf59LtmfSWAiq_kDqzENq_Ktk_bjN/s1600/2.png)

Inside GPMC, the console tree exposes the forest, its domains, and the organizational units that hold Group Policy Objects. Because Debug programs are a User Rights Assignment that must apply to the Domain Controller itself, the operator navigates to **Forest → Domains → ignite.local → Domain Controllers**, right-clicks the **Default Domain Controllers Policy**, and **selects Edit** to open it in the **Group Policy Management Editor**.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipqhnkm2waadbXvt6nlWtnCKCwMp3nHddHcYGXAe9J2MADOZivmao2gfshGu-O9uhyphenhyphenHMC_FC_yb9qVGFsn0Jns4htOPXKrhwKKKuFxWT7eUZVU89i1vtTMdFrjBKrbFLnYXuzKAnEe9tSSMPh1WVVpp9MbHdRqRC9pcw6sNBIE6ZJGKJPESPfO51cHmOcp/s1600/3.png)

The Group Policy Management Editor exposes the full policy tree for the selected GPO. The path to the target setting runs through **Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → User Rights Assignment**. The right-hand pane lists every user right that can be delegated on machines to which the GPO applies. The setting of interest, Debug programs, appears in the middle of the list and currently reads Not Defined.

![](https://blogg...
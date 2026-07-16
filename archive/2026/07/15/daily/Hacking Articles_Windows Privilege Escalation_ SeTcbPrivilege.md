---
title: Windows Privilege Escalation: SeTcbPrivilege
url: https://www.hackingarticles.in/windows-privilege-escalation-setcbprivilege/
source: Hacking Articles
date: 2026-07-15
fetch_date: 2026-07-16T04:57:28.934868
---

# Windows Privilege Escalation: SeTcbPrivilege

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
»* [Windows Privilege Escalation: SeTcbPrivilege](https://www.hackingarticles.in/windows-privilege-escalation-setcbprivilege/)
»

[Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)

# Windows Privilege Escalation: SeTcbPrivilege

[July 15, 2026July 15, 2026](https://www.hackingarticles.in/windows-privilege-escalation-setcbprivilege/) by [raj](https://www.hackingarticles.in/author/admin/)

### Overview

SeTcbPrivilege — formally “Act as part of the operating system” — is one of the most powerful Windows privileges in existence. It grants the holder the ability to impersonate any user account on the system — including NT AUTHORITY\SYSTEM — by calling trusted authentication APIs that are normally reserved for the Windows Trusted Computing Base (TCB). When a Domain Administrator mistakenly assigns this privilege to a low-privileged domain user through Group Policy, an attacker who gains access to that account can weaponize the privilege to escalate directly to local administrator without requiring any additional credentials or exploiting any software vulnerability.

This article demonstrates a complete, end-to-end exploitation chain: creating a domain user, assigning SeTcbPrivilege via the Default Domain Policy, verifying the privilege over a WinRM session, and leveraging the open-source tcb-lpe exploit (tcb.exe) to add the compromised account to the local Administrators group — all within a controlled penetration-testing lab built on the ignite.local Active Directory domain.

### Table of Contents:

* Introduction
* Lab Environment
* Understanding SeTcbPrivilege
* Creating a Target Domain User
* Opening Group Policy Management
* Editing the Default Domain Policy
* Navigating to User Rights Assignment
* Enabling the Policy Setting
* Adding the User to the Privilege
* Confirming the Policy Assignment
* Forcing a Group Policy Update
* Verifying SeTcbPrivilege over WinRM
* Confirming Standard Group Membership Before Exploitation
* Downloading the tcb-lpe Exploit
* Uploading tcb.exe and Executing the Exploit
* Confirming Local Administrator Privilege
* Mitigation Strategies
  + Restrict SeTcbPrivilege to Required Service Accounts Only
  + Audit User Rights Assignments Regularly
  + Enable Advanced Audit Policy for Privilege Use
  + Monitor Service Control Manager Activity
  + Block Unsigned Executables with Windows Defender Application Control
  + Apply the Principle of Least Privilege
  + Restrict WinRM Access to Administrative Accounts
* Conclusion

### Introduction

Windows privilege management forms the cornerstone of the operating system’s security model. Standard domain users operate with a minimal privilege set that restricts their interaction with sensitive system resources. Certain User Rights Assignments, however, create critical attack surfaces when granted to accounts that do not strictly require them. SeTcbPrivilege is the most dangerous of these rights.

Originally intended for components such as the Local Security Authority (LSA) and trusted authentication services, SeTcbPrivilege allows its holder to act as a fully trusted OS component. A process running under a user who holds this right can craft arbitrary logon sessions, impersonate SYSTEM-level tokens, and inject into privileged service contexts — effectively bypassing the user/kernel trust boundary.

In real-world penetration testing, discovering that a domain account holds SeTcbPrivilege represents an immediate critical finding. The exploitation path is straightforward, reliable, and can be completed in seconds using publicly available tooling. Understanding this attack in depth allows both red teamers to demonstrate impact and defenders to identify and remediate the misconfiguration before a real attacker does.

### Lab Environment

The lab runs on the **ignite.local** Active Directory domain, with **DC.IGNITE.LOCAL** — a Windows Server 2019 machine — serving as the Domain Controller. The target is a Windows host joined to the ignite.local domain, reachable at **192.168.1.15**, against which the privilege escalation chain is executed. The attacker operates from a **Kali Linux** machine, using **Evil-WinRM v3.9** to establish a remote shell over WinRM. Supporting tools include **net.exe** and the **Group Policy Management Console (GPMC)** on the Domain Controller for user creation and privilege assignment, and **tcb-lpe** — specifically the precompiled **tcb.exe** binary authored by CharminDoge — as the exploitation payload delivered to the target.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-1GDS-jduBJLNG6wNyQf7dIqc0L_r9bs4kktzT2UEh7ydYQevDPqJ45aFVUqzS7FWqdxOYt5EhroMbwdTN1NkdSVjtvh_0Ccsx8OR4yJ2RR2tIDnufgp2saTW_obmqvhJXPuA9tnCHlmHd6oij-81zBVs_rCgy1gE3QLe1PROV1SmxYqxg9fmTFyY93Mm/s1600/0.png)

### Understanding SeTcbPrivilege

SeTcbPrivilege (SE\_TCB\_NAME in the Windows security API) **grants a process membership** in the Trusted Computing Base — the set of hardware, firmware, and software components that the operating system trusts absolutely when enforcing its security policy. A process holding this privilege gains the following capabilities:

* Call LsaLogonUser **to create new logon sessions** for any account, including SYSTEM and built-in administrator accounts.
* **Impersonate any access token** on the system without restriction, regardless of the token’s integrity level.
* **Add privileges and modify Security Identifiers** (SIDs) in existing access tokens to elevate their effective rights.
* **Bypass standard user-mode access** checks by presenting a SYSTEM-level token to privileged APIs.
* **Interact with the Service Control Manager** (SCM) to create and start services that execute arbitrary commands under SYSTEM context.

The tcb-lpe exploit (available at github.com/CharminDoge/tcb-lpe) combines all of the above by hooking AcquireCredentialsHandleW to verify that the privilege is active, connecting to the SCM, creating a transient service with an attacker-specified command line, starting it under SYSTEM, and immediately cleaning up the service entry — leaving no persistent artefact behind.

### Creating a Target Domain User

The attacker (or, in a lab setup, the administrator simulating a misconfiguired environment) first creates a new domain user named raaj. On the Domain Controller, an Administrator opens a Command Prompt and runs the following command to add raaj to the domain with the password Password@1:

```
net user raaj Password@1 /add /domain
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjr5J7FyfKtVLLugd2kvF4EOloGMZiM_CSS3qj6nuIWwF2VdE4MSI6yx2-eL3pq2xHahwI3HMU0bTLYSNrLl9uHI_w7M7WoBrGiJs26ZzGOcs7rFQxd0APeiW128iiPJwvhsTc5LovXPF3LkXgDI4fBZKze-z6gFQdrdN88X_QMGRRWJlJA0T5eoQykQ7_N/s981/1.png)

The command executes against the domain controller and returns a success message confirming that the user account now exists in Active Directory. At this stage, raaj is a plain Domain Users member with no elevated rights on any machine.

### Opening Group Policy Management

To assign SeTcbPrivilege via Group Policy, the attacker opens Server Manager on the Domain Controller, clicks the **Tools menu**, and selects **Group Policy Management** from the list of available administrative tools.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvX...
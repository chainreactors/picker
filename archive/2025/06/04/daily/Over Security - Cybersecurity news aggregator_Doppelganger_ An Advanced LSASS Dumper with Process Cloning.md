---
title: Doppelganger: An Advanced LSASS Dumper with Process Cloning
url: https://labs.yarix.com/2025/06/doppelganger-an-advanced-lsass-dumper-with-process-cloning/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-04
fetch_date: 2025-10-06T22:54:31.549064
---

# Doppelganger: An Advanced LSASS Dumper with Process Cloning

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Doppelganger: An Advanced LSASS Dumper with Process Cloning

* [Home](https://labs.yarix.com "Go to Home Page")
* Doppelganger: An Advanced LSASS Dumper with Process Cloning

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2025/05/doppelganger-1024x445.png)

03Jun03/06/2025

## Doppelganger: An Advanced LSASS Dumper with Process Cloning

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2025-06-03T14:52:41+02:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   18 minutes

**Github Repo:** <https://github.com/vari-sh/RedTeamGrimoire/tree/main/Doppelganger>

## ![](https://labs.yarix.com/wp-content/themes/porto/images/lazy.png)

## What is LSASS?

The **Local Security Authority Subsystem Service (LSASS)** is a core component of the Windows operating system, responsible for enforcing the security policy on the system. LSASS is a process that runs as `lsass.exe` and plays a fundamental role in:

* **User authentication:** It verifies users logging into the system, interacting with authentication protocols such as NTLM and Kerberos.
* **Credential management:** It handles the secure storage and retrieval of credential materials like password hashes and Kerberos tickets.
* **Token generation:** It creates access tokens used by Windows to control access rights for processes.
* **Security auditing:** It helps in generating security audit logs related to authentication and account logon events.

Because LSASS has access to sensitive data such as plaintext credentials (in some configurations), NTLM hashes, and Kerberos tickets, it has become a **high-value target** for attackers during post-exploitation. Once an attacker has administrative access on a system, dumping the memory of the LSASS process can yield credentials for other accounts, including domain administrators.

Historically, tools like Mimikatz have been used to extract credentials directly from LSASS. This has led to Microsoft and security vendors implementing increasingly aggressive protective mechanisms around LSASS, including isolating it, preventing access via protected process modes, and introducing virtualization-based protections like **Credential Guard**.

Despite these defenses, LSASS remains at the center of many offensive security strategies—making it a persistent cat-and-mouse game between attackers and defenders.

## Does Dumping LSASS Still Make Sense in 2025?

Dumping LSASS has long been a key post-exploitation technique for adversaries seeking lateral movement and privilege escalation within Windows environments. But in 2025, with modern Windows defenses and increasingly capable Endpoint Detection and Response (EDR) platforms, one might ask: **is it still worth the risk?**

The short answer is: **yes—but only if done stealthily**.

### Evolved Defenses

Microsoft has dramatically hardened LSASS in recent years:

* **Protected Process Light (PPL)**: Prevents even SYSTEM-level processes from reading LSASS memory unless signed with Microsoft-trusted certificates.
* **Virtualization-Based Security (VBS)**: Isolates security-critical components, making traditional memory dumping methods ineffective.
* **Credential Guard**: Runs part of LSASS functionality in a Hyper-V-based isolated container, making even memory-access attempts futile in many cases.
* **Tamper protection** in Microsoft Defender and EDRs: Actively monitors attempts to access or tamper with LSASS, often killing offending processes or blocking the action altogether.

### Still Relevant—With the Right Techniques

While classic methods like `procdump` or `mimikatz sekurlsa::logonpasswords` might now fail or trigger instant alerts, **attackers have adapted**:

* **Process injection and hollowing** evade static signature detection.
* **Kernel-level access using vulnerable drivers** bypasses user-mode protections.
* **Cloning LSASS** allows working on a copy instead of the protected original, avoiding direct tampering.

These techniques, when combined with **custom API resolution**, **in-memory execution**, and **encryption of artifacts**, still allow threat actors and red teamers to extract credentials from LSASS successfully—**even under PPL or VBS**.

### A Tool in the Toolbox

Modern red teamers don’t rely on LSASS dumps alone. Credential access techniques now include:

* Token impersonation and abuse of over-privileged service accounts
* Kerberoasting and AS-REP roasting
* Abuse of LSA secrets and DPAPI blobs
* Accessing cached credentials and password vaults

That said, **a successful LSASS dump still offers high-value access in a single hit**—and can lead directly to domain administrator credentials.

### Conclusion

Dumping LSASS in 2025 isn’t obsolete—**it’s just harder**. When performed correctly, it’s still a powerful way to collect credentials, but it **requires advanced techniques** to remain undetected. This is where tools like **Doppelganger** come into play, using process cloning, obfuscation, and kernel-level manipulation to stay ahead of defensive technologies.

## PPL, VBS, and Credential Guard

To understand why dumping LSASS has become increasingly difficult, it’s essential to grasp three major protection layers introduced by Microsoft: **Protected Process Light (PPL)**, **Virtualization-Based Security (VBS)**, and **Credential Guard**. These mechanisms work together to lock down access to sensitive system components—especially LSASS.

### Protected Process Light (PPL)

**PPL** is a security feature designed to protect high-value processes from tampering—even by other processes running as SYSTEM. When a process like LSASS is run as a PPL, access to its memory space is heavily restricted. Only trusted, Microsoft-signed binaries with specific protection levels can read or write to it.

PPL uses different **protection levels**, and LSASS typically runs as **PsProtectedSignerLsa-Light**. This limits access to processes that either:

* Are signed by Microsoft with a specific certificate,
* Or have the same or higher protection level.

This means that even tools running with administrative privileges (like `procdump.exe`) **cannot access LSASS** unless they’re properly signed and allowed.

### Virtualization-Based Security (VBS)

**VBS** leverages hardware virtualization (e.g., Intel VT-x, AMD-V) to isolate sensitive parts of the Windows OS from the rest of the system. It creates a secure, virtualized environment called **Virtual Secure Mode (VSM)** that hosts highly privileged components.

Within VSM, certain memory regions become entirely inaccessible to standard processes—even those with elevated privileges. VBS enforces process integrity and makes it difficult to inject or tamper with system processes like LSASS.

With VBS enabled, even if an attacker disables PPL, **portions of LSASS memory may still be off-limits**.

### Credential Guard

Built on top of VBS, **Credential Guard** isolates credential material—including password hashes, Kerberos tickets, and NTLM secrets—inside VSM. LSASS still runs in the normal OS space, but the actual secrets are stored in **Isolated LSA (LSAIso)**, a process running in the secure container.

Even if you dump LSASS memory under Credential Guard, **you won’t retrieve actual credentials**, just metadata or stubs pointing to secure handles.

Credential Guard also blocks:

* Direct reading of `lsass.exe` memory,
* Pass-the-hash attacks using local secrets,
* Retrieval of plaintext passwords via tools like Mimikatz.

### Why These Protections Mat...
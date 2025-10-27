---
title: Tear Down The Castle - Part 2
url: https://dfir.ch/posts/tear_down_castle_part_two/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-17
fetch_date: 2025-10-06T20:35:19.978429
---

# Tear Down The Castle - Part 2

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Tear Down The Castle - Part 2

30 Jan 2025

**Table of Contents**

* [6. Privileges](#6-privileges)
  + [6.1 - Introduction](#61---introduction)
  + [6.2 - Findings](#62---findings)
  + [6.3 - References & Tools](#63---references--tools)
* [7. Harden critical accounts](#7-harden-critical-accounts)
  + [7.1 - Introduction](#71---introduction)
  + [7.2 - Findings](#72---findings)
  + [7.3 - References & Tools](#73---references--tools)
* [8. Print Spooler Service](#8-print-spooler-service)
  + [8.1 - Introduction](#81---introduction)
  + [8.2 - Findings](#82---findings)
  + [8.3 - References & Tools](#83---references--tools)
* [9. Easy Wins (for Attackers)](#9-easy-wins-for-attackers)
  + [9.1 - Introduction](#91---introduction)
  + [9.2 - Findings](#92---findings)
  + [9.3 - References & Tools](#93---references--tools)
* [10. Conclusion](#10-conclusion)

This is the second part of a two-part series about Active Directory security. Read the first part [here](https://dfir.ch/posts/tear_down_castle_part_one/).

**To gain insight into common issues and patterns of misconfiguration, we analyzed 250 PingCastle reports collected from Incident Response cases and Compromise Assessments. We indicate how many of the 250 domains checked were affected by the finding (Affected Domains: N/250)**.

[PingCastle](https://www.pingcastle.com/) is a popular tool for auditing the security of Active Directory environments, pinpointing vulnerabilities, and offering actionable recommendations for improvement. We are following along [The Ten AD Commandments](https://dfir.ch/tweets/varia/#10-ad-commandments), mapping every point to the corresponding PingCastle finding(s).

## 6. Privileges

### 6.1 - Introduction

PingCastle lists, among many other things, the privileges assigned to domain users via GPOs. Figure 1 shows that the `Default Notebook Policy` grants Domain Users the `SeLoadDriverPrivilege` privilege.

![SeLoadDriverPrivilege](/images/pingcastle/seloaddriver.png "SeLoadDriverPrivilege")

Figure 1: SeLoadDriverPrivilege

Why is this bad? As [@0xdf](https://0xdf.gitlab.io/) put it: *If I can load a driver, I can load a vulnerable driver and then exploit it.* [1] I am aware that some Endpoint Detection and Response (EDR) solutions generate alerts when a vulnerable driver is loaded or written to disk, as such drivers can be exploited for `Local Privilege Escalation (LPE)`.

![Exploiting a vulnerable driver](/images/pingcastle/vuln_driver.png "Exploiting a vulnerable driver")

Figure 2: If I can load a driver, I can load a vulnerable driver and then exploit it.

Excerpt from a Volexity blog post: *A userland application cannot modify kernel memory, so the malware authors include a vulnerable driver, RTCore64.sys, to read and write into this protected memory space.* A public GitHub repository, KDU, owned by hFiref0x, documents a list of drivers that can be abused for this `Bring Your Own Vulnerable Driver (BYOVD)` technique.

### 6.2 - Findings

#### 6.2.1 - Ensure that dangerous privileges are not granted to everyone by GPO

The purpose is to ensure that standard users are not granted dangerous privileges. The `SeLoadDriverPrivilege` presented above is one of many dangerous privileges. Thomas Roccia (fr0gger) has compiled a [list](https://speakerdeck.com/fr0gger/windows-privileges) of Windows privileges (Figure 3).

![Windows Privileges](/images/pingcastle/privileges.png "Windows Privileges")

Figure 3: Windows Privileges

Figure 4 shows a snippet from a `Default Domain Policy`, granting `Ãveryone` the `SeBackupPrivilege`.

![SeBackup](/images/pingcastle/SeBackup.png "SeBackup")

Figure 4: SeBackup

**Affected Domains: `13/250`**

### 6.3 - References & Tools

* <https://www.volexity.com/blog/2023/03/07/using-memory-analysis-to-detect-edr-nullifying-malware/>
* <https://0xdf.gitlab.io/2020/10/31/htb-fuse.html>
* <https://techcommunity.microsoft.com/t5/microsoft-security-experts-blog/total-identity-compromise-microsoft-incident-response-lessons-on/ba-p/3753391>
* <https://speakerdeck.com/fr0gger/windows-privileges>

## 7. Harden critical accounts

### 7.1 - Introduction

Add critical accounts to the `Protected Users Security Group` to raise the bar for a successful attack against your network. *This group provides protections over and above just preventing delegation and makes them even more secure; however, it may cause operational issues, so it is worth testing in your env.*

**Benefits of using the Protected Users Security Group:**

* `Credential delegation (CredSSP)` will not cache the user’s plain text credentials [..]
* Beginning with Windows 8.1 and Windows Server 2012 R2, `Windows Digest` will not cache the user’s plain text credentials even when `Windows Digest` is enabled.
* `NTLM` will not cache the user’s plain text credentials or `NT one-way function (NTOWF`).
* `Kerberos` will no longer create `DES` or `RC4` keys. Also, it will not cache the user’s plain text credentials or long-term keys after the initial `TGT` is acquired.

Accounts that are members of the Protected Users group that authenticate to a Windows Server 2012 R2 domain are unable to:

â Authenticate with `NTLM authentication`.
â Use `DES` or `RC4` encryption types in `Kerberos pre-authentication`.
â Be delegated with `unconstrained or constrained delegation`.
â Renew the `Kerberos TGTs` beyond the initial four-hour lifetime.

A word of advice â ï¸:

*Accounts for services and computers should never be members of the Protected Users group. This group provides incomplete protection anyway, because the password or certificate is always available on the host.*

### 7.2 - Findings

#### 7.2.1 - At least one member of an admin group is vulnerable to the Kerberoast attack

*To access a service using Kerberos, a user requests a ticket (named TGS) to the DC specific to the service. This ticket is encrypted using a derivative of the service password, but can be brute-forced to retrieve the original password. Any account having the attribute SPN populated is considered as a service account. Given that any user can request a ticket for a service account, these accounts can have their password retrieved. In addition, services are known to have their password not changed at a regular basis and to use well-known words.*

**Affected Domains: `95/250`**

#### 7.2.2 - Check the use of Kerberos with weak encryption (DES algorithm)

*The purpose is to verify that no weak encryption algorithm such as DES is used for accounts. DES is a very weak algorithm and once assigned to an account, it can be used in Kerberos ticket requests, even though it is easily cracked. If the attacker cracks the Kerberos ticket, they can steal the token and compromise the user account.*

**Affected Domains: `103/250`**

#### 7.2.3 - Check for the number of Administrator accounts above the baseline

*The purpose is to verify if the number of administrator accounts is not disproportionate. Very few users should have domain admin accounts.*

**Affected Domains: `51/250`**

#### 7.2.4 - At least one administrator account can be delegated

*The purpose is to ensure that all Administrator Accounts have the configuration flag “this account is sensitive and cannot be delegated” (or are members of the built-in group “Protected Users” when your domain functional level is at least Windows Server 2012 R2).*

**Affected Domains: `232/250`**

### 7.3 - References & Tools

* <https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group>
* <https://techcommunity.microsoft.com/blog/microsoftsecurityexperts/total-identity-compromise-microsoft-incident-response-lessons-on-securing-active/3753391>

## 8. Print Spooler Service

### 8.1 - Introduction

A running `print spooler service` on domain controllers is still a relatively common finding in our Active Di...
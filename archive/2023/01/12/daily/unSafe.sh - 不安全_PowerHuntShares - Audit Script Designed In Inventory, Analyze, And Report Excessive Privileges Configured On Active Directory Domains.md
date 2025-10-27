---
title: PowerHuntShares - Audit Script Designed In Inventory, Analyze, And Report Excessive Privileges Configured On Active Directory Domains
url: https://buaq.net/go-145118.html
source: unSafe.sh - 不安全
date: 2023-01-12
fetch_date: 2025-10-04T03:38:31.407637
---

# PowerHuntShares - Audit Script Designed In Inventory, Analyze, And Report Excessive Privileges Configured On Active Directory Domains

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/0ef9881e43464bbdff4376d8bb70318e.jpg)

PowerHuntShares - Audit Script Designed In Inventory, Analyze, And Report Excessive Privileges Configured On Active Directory Domains

PowerHuntShares is design to automatically inventory, analyze, and report excessive privileg
*2023-1-11 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-145118.htm)
阅读量:36
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjNfJYPDUkGgKdCgJqsu3vnBOgcGihCnXt-WB4_T_Hwkq2ErorINSFiRY5-HguP7ZWB00gfpOC2FZqyiR0_HT8Tm437nczRMLx2zAWeAUmpi1MJUgQpS9tn0SpqqAj0LB6h1BgGQBI_mBQmwd0vqT_1iqGLoB_Z0iH66yCz1Ulk5fjwZrKrzA1U7_Rlvg=w640-h484)](https://blogger.googleusercontent.com/img/a/AVvXsEjNfJYPDUkGgKdCgJqsu3vnBOgcGihCnXt-WB4_T_Hwkq2ErorINSFiRY5-HguP7ZWB00gfpOC2FZqyiR0_HT8Tm437nczRMLx2zAWeAUmpi1MJUgQpS9tn0SpqqAj0LB6h1BgGQBI_mBQmwd0vqT_1iqGLoB_Z0iH66yCz1Ulk5fjwZrKrzA1U7_Rlvg)

PowerHuntShares is design to automatically inventory, analyze, and report excessive privilege assigned to SMB shares on [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") domain joined computers.

It supports functionality to:

* **Authenticate** using the current user context, a credential, or clear text user/password.
* **Discover** accessible systems associated with an Active Directory domain automatically. It will also filter Active Directory computers based on available open ports.
* **Target** a single computer, list of computers, or discovered Active Directory computers (default).
* **Collect** SMB share ACL information from target computers using PowerShell.
* **Analyze** collected Share ACL data.
* **Report** summary reports and excessive privilege details in HTML and CSV file formats.

Excessive SMB share ACLs are a systemic problem and an attack surface that all organizations struggle with. The goal of this project is to provide a proof concept that will work towards building a better share collection and data insight engine that can help inform and priorititize remediation efforts.

Bonus Features:

* Generate directory listing dump for configurable depth
* Search for file types across discovered shares

I've also put together a short presentation outlining some of the common [misconfigurations](https://www.kitploit.com/search/label/Misconfigurations "misconfigurations") and strategies for prioritizing remediation here: [https://www.slideshare.net/nullbind/into-the-abyss-evaluating-active-directory-smb-shares-on-scale-secure360-251762721](https://www.slideshare.net/nullbind/into-the-abyss-evaluating-active-directory-smb-shares-on-scale-secure360-251762721 "https://www.slideshare.net/nullbind/into-the-abyss-evaluating-active-directory-smb-shares-on-scale-secure360-251762721")

PowerHuntShares will inventory SMB share ACLs configured with "excessive privileges" and highlight "high risk" ACLs. Below is how those are defined in this context.

**Excessive Privileges**
 Excessive read and write share permissions have been defined as any network share ACL containing an explicit ACE (Access Control Entry) for the "Everyone", "Authenticated Users", "BUILTIN\Users", "Domain Users", or "Domain Computers" groups. All provide domain users access to the affected shares due to privilege inheritance issues. Note there is a parameter that allow operators to add their own target groups.
 Below is some additional background:

* Everyone is a direct reference that applies to both unauthenticated and authenticated users. Typically only a null session is required to access those resources.
* BUILTIN\Users contains Authenticated Users
* Authenticated Users contains Domain Users on domain joined systems. That's why Domain Users can access a share when the share permissions have been assigned to "BUILTIN\Users".
* Domain Users is a direct reference
* Domain Users can also create up to 10 computer accounts by default that get placed in the Domain Computers group
* Domain Users that have local administrative access to a domain joined computer can also impersonate the computer account.

Please Note: Share permissions can be overruled by NTFS permissions. Also, be aware that testing excluded share names containing the following keywords:

```
print$, prnproc$, printer, netlogon,and sysvol
```

**High Risk Shares**
 In the context of this report, high risk shares have been defined as shares that provide unauthorized [remote access](https://www.kitploit.com/search/label/Remote%20Access "remote access") to a system or application. By default, that includes the shares

```
 wwwroot, inetpub, c$, and admin$
```

However, additional exposures may exist that are not called out beyond that.

Below is a list of commands that can be used to load PowerHuntShares into your current PowerShell session. Please note that one of these will have to be run each time you run PowerShell is run. It is not persistent.

```
# Bypass execution policy restrictions
Set-ExecutionPolicy -Scope Process Bypass

# Import module that exists in the current directory
Import-Module .\PowerHuntShares.psm1

or

# Reduce SSL operating level to support connection to github
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
[Net.ServicePointManager]::SecurityProtocol =[Net.SecurityProtocolType]::Tls12

# Download and load PowerHuntShares.psm1 into memory
IEX(New-Object System.Net.WebClient).DownloadString("https://raw.githubusercontent.com/NetSPI/PowerHuntShares/main/PowerHuntShares.psm1")
```

Important Note: All commands should be run as an unprivileged domain user.

```
.EXAMPLE 1: Run from a domain computer. Performs Active Directory computer discovery by default.
PS C:\temp\test> Invoke-HuntSMBShares -Threads 100 -OutputDirectory c:\temp\test

.EXAMPLE 2: Run from a domain computer with alternative domain credentials. Performs Active Directory computer discovery by default.
PS C:\temp\test> Invoke-HuntSMBShares -Threads 100 -OutputDirectory c:\temp\test -Credentials domain\user

.EXAMPLE 3: Run from a domain computer as current user. Target hosts in a file. One per line.
PS C:\temp\test> Invoke-HuntSMBShares -Threads 100 -OutputDirectory c:\temp\test  -HostList c:\temp\hosts.txt

.EXAMPLE 4: Run from a non-domain computer with credential. Performs Active Directory computer discovery by default.
C:\temp\test> runas /netonly /user:domain\user PowerShell.exe
PS C:\temp\test> Import-Module Invoke-HuntSMBShares.ps1
PS C:\temp\test> Invoke-HuntSMBShares -Threads 100 -Run   SpaceTimeOut 10 -OutputDirectory c:\folder\ -DomainController 10.1.1.1 -Credential domain\user

===============================================================
PowerHuntShares
===============================================================
 This function automates the following tasks:

o Determine current computer's domain
 o Enumerate domain computers
 o Filter for computers that respond to ping reqeusts
 o Filter for computers that have TCP 445 open and accessible
 o Enumerate SMB shares
 o Enumerate SMB share permissions
 o Identify shares with potentially excessive privielges
 o Identify shares that provide reads & write access
 o Identify shares thare are high risk
 o Identify common share owners, names, & directory listings
 o Generate creation, last written, & last accessed timelines
 o Generate html summary report and detailed csv files

Note: This can take hours to run in large environments.
---------------------------------------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
---------------------------------------------------------------
SHARE DISCOVERY
------------------------------------------------...
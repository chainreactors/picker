---
title: Active Directory Security Tip #4: Default/Built-In Active Directory Groups
url: https://adsecurity.org/?p=4607
source: Active Directory & Azure AD/Entra ID Security
date: 2025-09-18
fetch_date: 2025-10-02T20:19:57.583265
---

# Active Directory Security Tip #4: Default/Built-In Active Directory Groups

Toggle search form

Search for:

![Active Directory & Azure AD/Entra ID Security](https://adsecurity.org/wp-content/themes/graphene/images/headers/fluid.jpg "Active Directory & Azure AD/Entra ID Security")

Toggle navigation

[Active Directory & Azure AD/Entra ID Security](https://adsecurity.org "Go back to the front page")

Active Directory & Azure AD/Entra ID: Enterprise Security, Methods to Secure Active Directory, Attack Methods & Effective Defenses, PowerShell, Tech Notes, & Geek Trivia…

* [Home](https://adsecurity.org/)
* [About](https://adsecurity.org/?page_id=8)
* [AD Resources](https://adsecurity.org/?page_id=41)
* [Attack Defense & Detection](https://adsecurity.org/?page_id=4031)
* [Mimikatz](https://adsecurity.org/?page_id=1821)
* [Presentations](https://adsecurity.org/?page_id=1352)
* [Schema Versions](https://adsecurity.org/?page_id=195)
* [Security Resources](https://adsecurity.org/?page_id=399)
* [SPNs](https://adsecurity.org/?page_id=183)
* [Top Posts](https://adsecurity.org/?page_id=2532)

[Active Directory Lab Build Script](https://adsecurity.org/?p=4670)

[Active Directory Security Tip #5: The Default Domain Administrator Account](https://adsecurity.org/?p=4586)

Sep
16
2025

# Active Directory Security Tip #4: Default/Built-In Active Directory Groups

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [ActiveDirectorySecurity](https://adsecurity.org/?cat=565), [PowerShell](https://adsecurity.org/?cat=7), [Technical Reference](https://adsecurity.org/?cat=2)

There are several default/built-in privileged groups that should be reviewed:

* **Account Operators** – should be empty per Microsoft due to highly privileged access in AD.
* **Backup operators** – should only contain backup service accounts to backup and restore Active Directory.
* **Cert Publishers** – should only contain PKI related accounts (CAs & related service accounts) since it can publish certificates for AD users.
* **DNSAdmins** – typically only used when admins other than ADAs perform DNS administration. Use sparingly. \* Enterprise Key Admins – have admin rights on key objects in AD.
* **Event Log Readers** – should only include accounts that require access to Domain Controller event logs.
* **Group Policy Creator Owners** – can modify Group Policies in the domain. Membership should be empty and rights delegated instead.
* **Print Operators** – used only when a Domain Controller is used as a print server (which shouldn’t happen). Group has the ability to logon to Domain Controllers and install drivers which makes this group highly privileged. Group should be empty.
* **Server Operators** – effectively local admin on Domain Controllers. Use sparingly.
* **Schema Admins** – should be empty except when updating the AD schema.

<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups>

![](https://adsecurity.org/wp-content/uploads/2025/09/GzNrh03X0AANTqH.jpg)

PowerShell Script leveraging the Active Directory PowerShell module:
 <https://github.com/PyroTek3/Misc/blob/main/Get-ADBuiltInAdmins.ps1>

(Visited 247 times, 1 visits today)

* [ActiveDirectorySecurityTip](https://adsecurity.org/?tag=activedirectorysecuritytip), [BuiltInActiveDirectoryGroups](https://adsecurity.org/?tag=builtinactivedirectorygroups), [DefaultActiveDirectoryGroups](https://adsecurity.org/?tag=defaultactivedirectorygroups)

[![](https://adsecurity.org/wp-content/uploads/2025/08/Twitter-MI4-150x150.png)](https://adsecurity.org/?author=2)

### Sean Metcalf

I improve security for enterprises around the world working for TrustedSec & I am @PyroTek3 on Twitter.

## Recent Posts

* [Active Directory Security Tip #10: FSMO Roles](https://adsecurity.org/?p=4591)
* [Active Directory Security Tip #9: Active Directory Backups](https://adsecurity.org/?p=4589)
* [Active Directory Security Tip #8: The Domain Kerberos Service Account – KRBTGT](https://adsecurity.org/?p=4597)
* [Active Directory Security Tip #7: The Tombstone Lifetime](https://adsecurity.org/?p=4600)
* [Active Directory Security Tip #6: Domain Controller Operating System Versions](https://adsecurity.org/?p=4594)

## Active Directory & Entra ID Security Services

Have concerns about your Active Directory environment and/or Entra ID tenant?
We help enterprises improve their security posture.

[Find out how...](https://www.trimarcsecurity.com/contact)

## Popular Posts

* [PowerShell Encoding & Decoding (Base64)](https://adsecurity.org/?p=478)
* [Attack Methods for Gaining Domain Admin Rights in…](https://adsecurity.org/?p=2362)
* [AD Reading: Windows Server 2019 Active Directory Features](https://adsecurity.org/?p=4187)
* [Kerberos & KRBTGT: Active Directory’s…](https://adsecurity.org/?p=483)
* [Finding Passwords in SYSVOL & Exploiting Group…](https://adsecurity.org/?p=2288)
* [Securing Domain Controllers to Improve Active…](https://adsecurity.org/?p=3377)
* [Securing Windows Workstations: Developing a Secure Baseline](https://adsecurity.org/?p=3299)
* [Detecting Kerberoasting Activity](https://adsecurity.org/?p=3458)
* [Mimikatz DCSync Usage, Exploitation, and Detection](https://adsecurity.org/?p=1729)
* [Scanning for Active Directory Privileges &…](https://adsecurity.org/?p=3658)

## Categories

* [ActiveDirectorySecurity](https://adsecurity.org/?cat=565)
* [Apple Security](https://adsecurity.org/?cat=55)
* [Cloud Security](https://adsecurity.org/?cat=431)
* [Continuing Education](https://adsecurity.org/?cat=17)
* [Entertainment](https://adsecurity.org/?cat=396)
* [Exploit](https://adsecurity.org/?cat=347)
* [Hacking](https://adsecurity.org/?cat=1039)
* [Hardware Security](https://adsecurity.org/?cat=168)
* [Hypervisor Security](https://adsecurity.org/?cat=172)
* [Linux/Unix Security](https://adsecurity.org/?cat=126)
* [Malware](https://adsecurity.org/?cat=343)
* [Microsoft Security](https://adsecurity.org/?cat=11)
* [Mitigation](https://adsecurity.org/?cat=819)
* [Network/System Security](https://adsecurity.org/?cat=48)
* [PowerShell](https://adsecurity.org/?cat=7)
* [RealWorld](https://adsecurity.org/?cat=698)
* [Security](https://adsecurity.org/?cat=21)
* [Security Conference Presentation/Video](https://adsecurity.org/?cat=234)
* [Security Recommendation](https://adsecurity.org/?cat=1045)
* [Technical Article](https://adsecurity.org/?cat=24)
* [Technical Reading](https://adsecurity.org/?cat=4)
* [Technical Reference](https://adsecurity.org/?cat=2)
* [TheCloud](https://adsecurity.org/?cat=156)
* [Vulnerability](https://adsecurity.org/?cat=930)

## Tags

[ActiveDirectory](https://adsecurity.org/?tag=activedirectory)
[Active Directory](https://adsecurity.org/?tag=active-directory)
[ActiveDirectorySecurity](https://adsecurity.org/?tag=activedirectorysecurity)
[Active Directory Security](https://adsecurity.org/?tag=active-directory-security)
[ActiveDirectorySecurityTip](https://adsecurity.org/?tag=activedirectorysecuritytip)
[ADReading](https://adsecurity.org/?tag=adreading)
[ADSecurity](https://adsecurity.org/?tag=adsecurity)
[AD Security](https://adsecurity.org/?tag=ad-security)
[Azure](https://adsecurity.org/?tag=azure)
[DCSync](https://adsecurity.org/?tag=dcsync)
[DomainController](https://adsecurity.org/?tag=domaincontroller)
[GoldenTicket](https://adsecurity.org/?tag=goldenticket)
[GroupPolicy](https://adsecurity.org/?tag=grouppolicy)
[HyperV](https://adsecurity.org/?tag=hyperv)
[Invoke-Mimikatz](https://adsecurity.org/?tag=invoke-mimikatz)
[KB3011780](https://adsecurity.org/?tag=kb3011780)
[KDC](https://adsecurity.org/?tag=kdc)
[Kerberos](https://adsecurity.org/?tag=kerberos)
[KerberosHacking](https://adsecurity.org/?tag=kerberoshacking)
[KRBTGT](https://adsecurity.org/?tag=krbtgt)
[LAPS](https://adsecurity.org/?tag=laps)
[LSASS](https://adsecurity.org/?tag=lsass)
[MCM](https://adsecurity.org/?tag=mcm)
[MicrosoftEMET](https://adsecurity.org/?tag=microsoftemet)
[MicrosoftWindows](https://adsecurity.org/?tag=microsoftwindows)
[mimikatz](https://adsecurity.org/?tag=mimikatz)
[MS14068](https:...
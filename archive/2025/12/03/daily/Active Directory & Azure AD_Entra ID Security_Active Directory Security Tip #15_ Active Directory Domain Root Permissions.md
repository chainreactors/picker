---
title: Active Directory Security Tip #15: Active Directory Domain Root Permissions
url: https://adsecurity.org/?p=4941
source: Active Directory & Azure AD/Entra ID Security
date: 2025-12-03
fetch_date: 2025-12-04T03:19:41.963910
---

# Active Directory Security Tip #15: Active Directory Domain Root Permissions

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

[Active Directory Security Tip #14: Group Managed Service Accounts (GMSAs)](https://adsecurity.org/?p=4904)

Dec
02
2025

# Active Directory Security Tip #15: Active Directory Domain Root Permissions

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [ActiveDirectorySecurity](https://adsecurity.org/?cat=565), [Microsoft Security](https://adsecurity.org/?cat=11), [PowerShell](https://adsecurity.org/?cat=7)

This week let’s look at Active Directory domain permissions which are configured on the domain root and apply to the domain. There are many different type of concerning permissions, but let’s look at the most egregious.

* Directory Changes & Directory Changes All – provides the ability to pull password hashes for users and computers (aka DCsync permissions).
* Change Owner – provides the ability to set the owner on the domain root and the owner has the ability to set permissions.
* Change Permission – provides the ability to set permissions on the domain root.
* Full Control – provides the ability to control any type of object in the domain.
* Full Control on Users and/or Computers – provides the ability to control the object type.

I wrote a PowerShell script leveraging the Active Directory PowerShell module that can help identify these permissions on the domain root: [https://github.com/PyroTek3/Misc/blob/main/Get-DomainRootPermissions.ps1](https://t.co/d8tu0v1WQS)

For more on Active Directory permissions:
[https://hub.trimarcsecurity.com/post/trimarc-whitepaper-owner-or-pwnd](https://t.co/F0ydpgCE5D)
[https://specterops.io/wp-content/uploads/sites/3/2022/06/an\_ace\_up\_the\_sleeve.pdf](https://t.co/vLp3BunQjK)

For more on DCSync: [https://adsecurity.org/?p=1729](https://t.co/RQh4NnBq5c)

(Visited 125 times, 99 visits today)

* [ActiveDirectory](https://adsecurity.org/?tag=activedirectory), [ActiveDirectorySecurityTip](https://adsecurity.org/?tag=activedirectorysecuritytip), [ADPermissions](https://adsecurity.org/?tag=adpermissions), [Domain Root Permissions](https://adsecurity.org/?tag=domain-root-permissions)

[![](https://adsecurity.org/wp-content/uploads/2025/08/Twitter-MI4-150x150.png)](https://adsecurity.org/?author=2)

### Sean Metcalf

I improve security for enterprises around the world working for TrustedSec & I am @PyroTek3 on Twitter.

### Leave a Reply [Cancel reply](/?p=4941#respond)

Your email address will not be published.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

## Recent Posts

* [Active Directory Security Tip #15: Active Directory Domain Root Permissions](https://adsecurity.org/?p=4941)
* [Active Directory Security Tip #14: Group Managed Service Accounts (GMSAs)](https://adsecurity.org/?p=4904)
* [Improve Entra ID Security More Quickly](https://adsecurity.org/?p=4825)
* [BSides NoVa 2025 Presentation Slides Posted](https://adsecurity.org/?p=4799)
* [Microsoft Interview](https://adsecurity.org/?p=4802)

## Active Directory & Entra ID Security Services

Have concerns about your Active Directory environment and/or Entra ID tenant?
We help enterprises improve their security posture.

[Find out how...](https://www.trimarcsecurity.com/contact)

## Popular Posts

* [PowerShell Encoding & Decoding (Base64)](https://adsecurity.org/?p=478)
* [AD Reading: Windows Server 2019 Active Directory Features](https://adsecurity.org/?p=4187)
* [Attack Methods for Gaining Domain Admin Rights in…](https://adsecurity.org/?p=2362)
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
* [Entra ID Security](https://adsecurity.org/?cat=1536)
* [Exploit](https://adsecurity.org/?cat=347)
* [Hacking](https://adsecurity.org/?cat=1039)
* [Hardware Security](https://adsecurity.org/?cat=168)
* [Hypervisor Security](https://adsecurity.org/?cat=172)
* [Interview](https://adsecurity.org/?cat=1540)
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
[MS14068](https://adsecurity.org/?tag=ms14068)
[PassTheHash](https://adsecurity.org/?tag=passthehash)
[PowerShell](https://a...
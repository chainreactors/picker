---
title: Active Directory Security Tip #1: Active Directory Admins
url: https://adsecurity.org/?p=4577
source: Active Directory & Azure AD/Entra ID Security
date: 2025-09-14
fetch_date: 2025-10-02T20:09:26.309893
---

# Active Directory Security Tip #1: Active Directory Admins

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

[The Art of the Honeypot Account: Making the Unusual Look Normal](https://adsecurity.org/?p=4510)

[Active Directory Security Tip #2: Active Directory User Accounts](https://adsecurity.org/?p=4580)

Sep
12
2025

# Active Directory Security Tip #1: Active Directory Admins

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [ActiveDirectorySecurity](https://adsecurity.org/?cat=565), [PowerShell](https://adsecurity.org/?cat=7)

A critical part of Active Directory security is regularly reviewing your AD admins. The simplest way to do this is to recursively enumerate the membership of the domain Administrators group (that group’s members and all member group members).

Check the AD Admins output for the following:

* Are all the admin accounts associated with people expected?
* Are there service accounts that shouldn’t require AD admin rights (VMware, Exchange, LDAP, VPN, Sharepoint, etc.)?
* Are the associated passwords current?
* Are they as expected with no outliers (all within 2 years but one has a password that’s 10 years old)?
* Has the default domain Administrator account logged on recently?
  + Is that expected/known?
* Are all accounts enabled?
  + Disabled accounts should be removed from being an AD Admin.
* Do all accounts require Kerberos preauthentication?
  + They must if they are AD admins.
* Do any use Kerberos DES?
  + If so fix that.
* Are any set to never expire their password?
  + Is that expected?
  + Accounts with this set rarely change their password.
* Are there any passwords in Active Directory user attributes (commonly description notes/info, Exchange custom attributes, etc.)?
  + Practically all of the attributes are visible to users.

![](https://adsecurity.org/wp-content/uploads/2025/09/GyzetbQWcAANFVq-1-1-1024x199.jpg)

PowerShell code (using Active Directory PowerShell modules):
<https://github.com/PyroTek3/Misc/blob/main/Get-ADAdmins.ps1>

(Visited 325 times, 2 visits today)

* [ActiveDirectoryAdmins](https://adsecurity.org/?tag=activedirectoryadmins), [ActiveDirectorySecurityTip](https://adsecurity.org/?tag=activedirectorysecuritytip)

[![](https://adsecurity.org/wp-content/uploads/2025/08/Twitter-MI4-150x150.png)](https://adsecurity.org/?author=2)

### Sean Metcalf

I improve security for enterprises around the world working for TrustedSec & I am @PyroTek3 on Twitter.

#### 1 comments

1. * ![](https://secure.gravatar.com/avatar/82f739090d00b095bb4ff1b96362798ba51e16b717a81119167fe1a8c0289dc6?s=50&d=mm&r=g)
   * Gxxxx on September 14, 2025 at 7:41 am
   * [#](https://adsecurity.org/?p=4577#comment-21961)

   Thanks for this . Great compliment to my OSCP journey . Keep up the great work

### Comments have been disabled.

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
[MicrosoftWindows](https://adsec...
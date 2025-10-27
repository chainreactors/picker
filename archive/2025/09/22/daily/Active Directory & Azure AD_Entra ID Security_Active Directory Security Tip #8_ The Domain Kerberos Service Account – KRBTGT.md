---
title: Active Directory Security Tip #8: The Domain Kerberos Service Account – KRBTGT
url: https://adsecurity.org/?p=4597
source: Active Directory & Azure AD/Entra ID Security
date: 2025-09-22
fetch_date: 2025-10-02T20:30:18.882117
---

# Active Directory Security Tip #8: The Domain Kerberos Service Account – KRBTGT

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

[Active Directory Security Tip #7: The Tombstone Lifetime](https://adsecurity.org/?p=4600)

[Active Directory Security Tip #9: Active Directory Backups](https://adsecurity.org/?p=4589)

Sep
20
2025

# Active Directory Security Tip #8: The Domain Kerberos Service Account – KRBTGT

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [ActiveDirectorySecurity](https://adsecurity.org/?cat=565), [PowerShell](https://adsecurity.org/?cat=7), [Technical Reference](https://adsecurity.org/?cat=2)

The domain Kerberos service account, KRBTGT (<https://adsecurity.org/?p=483>), is an important account since it is used to sign & encrypt Kerberos tickets. The account is disabled and the password doesn’t change except when moving from Windows 2000/2003 to Windows Server 2008 (or newer).

This is a highly privileged account and if an attacker can gain knowledge of the account’s password hash (or password), they can create forged Kerberos tickets (aka Golden Tickets: <https://adsecurity.org/?p=1640>).

Most AD forests have this account lingering with old passwords. The KRBTGT account stores two passwords, the current one and the previous one and checks them both to validate Kerberos tickets. This means that to ensure that the KRBTGT passwords are fully changed, the password must be changed twice. If an attacker can capture a DC backup that is as old as one of the KRBTGT account passwords (say 15 years), then they can compromise the environment even if the backup is 15 years old!

We can use the “msds-keyversionnumber” attribute to determine how many times the KRBTGT password has changed. The formula n – 2 works to calculate how many times the password has changed. If this value is 2 it hasn’t changed since it was originally set when the domain was created. If the value is 9, then it has changed 7 times (9 – 2 = 7). Sometimes this value is very large, like 100003. In that case we just use the last digit (3) to calculate the number of times it has changed: n – 2 = 1, so it has changed 1x.

We recommend changing the password once, then waiting at least a week, and then changing the password again. When you set the password, a process on the DC actually changes the KRBTGT password to a fully random password.

![](https://adsecurity.org/wp-content/uploads/2025/09/GvlcHcTXIAAfIyD.png)

**PowerShell code to report on the KRBTGT account for the current domain:**

```
$Domain = $env:userdnsdomain
$DomainDC = (Get-ADDomainController -Discover -DomainName $Domain).Name
$DomainKRBTGTAccount = Get-ADUser 'krbtgt' -Properties DistinguishedName,'msds-keyversionnumber',Created,PasswordLastSet -Server $DomainDC
$DomainKRBTGTAccount | Select DistinguishedName,Created,PasswordLastSet,'msds-keyversionnumber' | Format-Table -AutoSize
```

(Visited 432 times, 5 visits today)

* [ActiveDirectorySecurityTip](https://adsecurity.org/?tag=activedirectorysecuritytip), [Domain KerberosServiceAccount](https://adsecurity.org/?tag=domain-kerberosserviceaccount), [KRBTGT](https://adsecurity.org/?tag=krbtgt)

[![](https://adsecurity.org/wp-content/uploads/2025/08/Twitter-MI4-150x150.png)](https://adsecurity.org/?author=2)

### Sean Metcalf

I improve security for enterprises around the world working for TrustedSec & I am @PyroTek3 on Twitter.

### Leave a Reply [Cancel reply](/?p=4597#respond)

Your email address will not be published.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

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
[DCSync](https://adsecurit...
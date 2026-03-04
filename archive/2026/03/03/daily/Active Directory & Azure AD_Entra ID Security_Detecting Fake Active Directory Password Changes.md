---
title: Detecting Fake Active Directory Password Changes
url: https://adsecurity.org/?p=4969
source: Active Directory & Azure AD/Entra ID Security
date: 2026-03-03
fetch_date: 2026-03-04T04:04:29.558295
---

# Detecting Fake Active Directory Password Changes

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

[Active Directory Security Tip #16: Mitigating Kerberoast Attacks](https://adsecurity.org/?p=4955)

Mar
02
2026

# Detecting Fake Active Directory Password Changes

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [ActiveDirectorySecurity](https://adsecurity.org/?cat=565), [Microsoft Security](https://adsecurity.org/?cat=11), [Mitigation](https://adsecurity.org/?cat=819), [PowerShell](https://adsecurity.org/?cat=7)

In Active Directory, there has been a method that’s been around for many years which changes the password last set date but not the actual password. This is what I call a “fake password change” since the account appears to have a recent password when scanning for old passwords based on password last set, but the underlying password hasn’t actually changed.
I spoke about this in my [2015 BSides Charm talk](https://adsecurity.org/wp-content/uploads/2016/03/BsidesCharm-RedvsBlue-v1-2015-04-11-Published.pdf) which was my first conference talk.

**Why does this happen?**
There are times where service account (or admin accounts) need to have password changes, but someone doesn’t want to do the work to change them. The ability to fake a password change requires modify rights on the pwdLastSet attribute which provides the ability to check/uncheck the setting “User must change password at next logon”. This setting is enabled when you want the user to change their own password when they logon.

**How does this work?**

To see how this works, we’ll focus on the service account “svc-AGPM” in my lab. This account last changed its password on August 20th in 2025.

![](https://adsecurity.org/wp-content/uploads/2026/03/image-5.png)

We open up Active Directory Users and Computers (ADUC), double-click on it to open up the account properties and then click on the Account tab.
From here we check the box for “User must change password at next logon” and click Apply.

![](https://adsecurity.org/wp-content/uploads/2026/03/image-6.png)

**What happens to the PasswordLastSet date when this happens?**
It is now blank.  Which makes it seem like the account has never had a password set.

![](https://adsecurity.org/wp-content/uploads/2026/03/image-7.png)

We continue with our process where we uncheck the box we checked and then click Apply.

![](https://adsecurity.org/wp-content/uploads/2026/03/image-8.png)

After performing this action, we can see that the password change date has now been set to the current date and time even though the password itself hasn’t been changed since August 2025. We have successfully faked a password change!

![](https://adsecurity.org/wp-content/uploads/2026/03/image-9.png)

**Why does this happen?**

This happens because the “User must change password at next logon” option is used to force a user to change their password at next logon. With it checked, Active Directory is waiting for the user to attempt to logon which is when the user is directed to change their password. During this time the PasswordLastSet value is blank since it is waiting for a new password. Once the user changes their password, the checkbox is effectively removed and the current date and time are set for the user’s passwordlastset property (technically this is the “pwdlastset” attribute, but the AD PowerShell cmdlets use that property).

**How can we detect a fake password change?**

In order to detect a fake password change we need to figure out how this change occurs on a Domain Controller. We have already identified that the pwdlastset attribute is what shows the date the password is last set. We have to look at another attribute called unicodePwd which is used to store the account’s password on the Domain Controller.

We can use the Active Directory PowerShell module cmdlet “Get-ADReplicationAttributeMetadata” to get AD replication metadata about the account. Running this cmdlet provides the following replication metadata about the account that continues beyond the screenshot.

![](https://adsecurity.org/wp-content/uploads/2026/03/image-10-1024x779.png)

Let’s scope this down to the 2 attributes that we care about, unicodepwd and pwdlastset.

![](https://adsecurity.org/wp-content/uploads/2026/03/image-11-1024x339.png)

The attribute we care about in this output is “LastOriginatingChangeTime”. I have highlighted the values for this attribute in the following screenshot.

![](https://adsecurity.org/wp-content/uploads/2026/03/image-12-1024x339.png)

Here we can clearly see that while the pwdlastset date is 3/03/2026, the date for unicodepwd remains 8/20/2025. This means that the password hasn’t changed, only the value that’s supposed to show when it has last changed.

An attacker could use this technique for an account with an old password they discover and have control of the account (with the ability to flip this bit). This would show that the password changed without it actually changing. This would allow for some sneaky persistence.

**Detect fake Active Directory password changes at scale**

I wrote a PowerShell script that will scan either the Active Directory Admins or All Users in the domain to see if there’s a fake password change that has been performed on them.
<https://github.com/PyroTek3/ActiveDirectory/blob/main/Get-FakePWChanges.ps1>

**Example Script Output**

![](https://adsecurity.org/wp-content/uploads/2026/03/image-13-1024x144.png)

Note that there may be scenarios where an account could be flagged but an admin wasn’t responsible for faking the password change. This does identify when a password shows it changed, but actually has not.

(Visited 423 times, 384 visits today)

* [ActiveDirectory](https://adsecurity.org/?tag=activedirectory), [ActiveDirectoryReplicationMetadata](https://adsecurity.org/?tag=activedirectoryreplicationmetadata), [FakeADPasswordChange](https://adsecurity.org/?tag=fakeadpasswordchange), [FakePasswordChange](https://adsecurity.org/?tag=fakepasswordchange), [PowerShell](https://adsecurity.org/?tag=powershell), [pwdlastset](https://adsecurity.org/?tag=pwdlastset), [unicodepwd](https://adsecurity.org/?tag=unicodepwd)

[![](https://adsecurity.org/wp-content/uploads/2025/08/Twitter-MI4-150x150.png)](https://adsecurity.org/?author=2)

### Sean Metcalf

I improve security for enterprises around the world working for TrustedSec & I am @PyroTek3 on Twitter.

### Leave a Reply [Cancel reply](/?p=4969#respond)

Your email address will not be published.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

## Recent Posts

* [Detecting Fake Active Directory Password Changes](https://adsecurity.org/?p=4969)
* [Active Directory Security Tip #16: Mitigating Kerberoast Attacks](https://adsecurity.org/?p=4955)
* [Active Directory Security Tip #15: Active Directory Domain Root Permissions](https://adsecurity.org/?p=4941)
* [Active Directory Security Tip #14: Group Managed Service Accounts (GMSAs)](https://adsecurity.org/?p=4904)
* [Improve Entra ID Security Mor...
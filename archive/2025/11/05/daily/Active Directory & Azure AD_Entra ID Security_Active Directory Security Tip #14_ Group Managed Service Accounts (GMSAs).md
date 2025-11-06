---
title: Active Directory Security Tip #14: Group Managed Service Accounts (GMSAs)
url: https://adsecurity.org/?p=4904
source: Active Directory & Azure AD/Entra ID Security
date: 2025-11-05
fetch_date: 2025-11-06T03:16:04.971201
---

# Active Directory Security Tip #14: Group Managed Service Accounts (GMSAs)

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

[Improve Entra ID Security More Quickly](https://adsecurity.org/?p=4825)

Nov
04
2025

# Active Directory Security Tip #14: Group Managed Service Accounts (GMSAs)

* By [Sean Metcalf](https://adsecurity.org/?author=2) in [ActiveDirectorySecurity](https://adsecurity.org/?cat=565), [Microsoft Security](https://adsecurity.org/?cat=11), [PowerShell](https://adsecurity.org/?cat=7), [Technical Reference](https://adsecurity.org/?cat=2)

## **Group Managed Service Accounts (GMSAs)**

User accounts created to be used as service accounts rarely have their password changed. [Group Managed Service Accounts (GMSAs)](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview) provide a better approach (starting in the Windows 2012 timeframe). The password is managed by AD and automatically changed. This means that the GMSA has to have security principals explicitly delegated to have access to the clear-text password. Much like with other areas where delegation controls access ([LAPS](https://adsecurity.org/?p=3164)), determining who should have be delegated access needs to be be carefully considered.

## **Key Points for Group Managed Service Accounts (GMSAs)**

* The GMSA password is managed by AD.
* Computers hosting GMSA service account(s) request the current password from Active Directory to start the associated service.
* Configure the GMSA to allow computer account(s) access to the GMSA password.
* If an attacker compromises any computer hosting services using the GMSA, the GMSA is compromised.
* If attacker compromises an account with rights to request the GMSA password, the GMSA is compromised.

Group Managed Service Accounts have the object class “[msDS-GroupManagedServiceAccount](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adsc/219549d4-39eb-4771-bb8c-b3593ff6be48)” and associated attributes specific to GMSAs. These properties include:

* [msDS-GroupMSAMembership](https://docs.microsoft.com/en-us/windows/win32/adschema/a-msds-groupmsamembership) (PrincipalsAllowedToRetrieveManagedPassword) – stores the security principals that can access the GMSA password.
* [msds-ManagedPassword](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/9cd2fc5e-7305-4fb8-b233-2a60bc3eec68) – This attribute contains a BLOB with password information for group-managed service accounts.
* [msDS-ManagedPasswordId](https://docs.microsoft.com/en-us/windows/win32/adschema/a-msds-managedpasswordid) – This constructed attribute contains the key identifier for the current managed password data for a group MSA.
* [msDS-ManagedPasswordInterval](https://docs.microsoft.com/en-us/windows/win32/adschema/a-msds-managedpasswordinterval) – This attribute is used to retrieve the number of days before a managed password is automatically changed for a group MSA.

## **Lab Example**

In order to identify GMSAs in an Active Directory domain, we can use the Active Directory PowerShell cmdlet “Get-ADServiceAccount”.

```
get-adserviceaccount -filter * -prop * | Select Name,DNSHostName,MemberOf,Created,LastLogonDate,PasswordLastSet,msDS-ManagedPasswordInterval,PrincipalsallowedtoDelegateToAccount,PrincipalsAllowedtoRetrieveManagedPassword,msDS-ManagedPassword,ServicePrincipalName | Sort Name
```

In my lab environment (mirroring what I’ve seen in real world AD environments), we notice that there is a GMSA in Domain Admins. Let’s dig into that one.

![](https://adsecurity.org/wp-content/uploads/2025/10/image-43-1024x590.png)

The Citrix GMSA is configured to allow the group “Citrix04” the ability to get the password for the GMSA (property “PrincipalsAllowedToRetrieveManagedPassword”). Now, let’s take a look at the membership of that group.

![](https://adsecurity.org/wp-content/uploads/2025/10/image-45.png)

There’s a user account in that group which means compromise of that user account (AdminJackson) would result in the compromise of the password for the Citrix GMSA and that would result in the compromise of Active Directory since the GMSA is a member of Domain Admins.

I wanted to make it easier to get this information, so I wrote a PowerShell script called [Get-GMSADetail](https://github.com/PyroTek3/Misc/blob/main/Get-GMSADetail.ps1) that captures this information using the Active Directory PowerShell module. This adds a new property called “PasswordAccessPrincipalString which is a list of principals in the group that have the rights to pull the password.
The results are shown here:

![](https://adsecurity.org/wp-content/uploads/2025/11/image.png)

## **Conclusion**

As part of this lab exercise, we learned that if a GMSA is a member of a privileged group (like Domain Admins), compromise of an account that has rights to pull the clear-text password for the GMSA (property “PrincipalsAllowedToRetrieveManagedPassword”) can leverage the GMSA rights (like compromise Active Directory). Furthermore, if we can compromise one of the computer accounts that have the ability to pull the GMSA password, then we can dump the password from the computer.

For more information about attacking GMSAs, read the ADSecurity article “[Attacking Active Directory Group Managed Service Accounts (GMSAs)](https://adsecurity.org/?p=4367)“

(Visited 123 times, 86 visits today)

* [ActiveDirectorySecurityTip](https://adsecurity.org/?tag=activedirectorysecuritytip), [GMSA](https://adsecurity.org/?tag=gmsa), [GroupManagedServiceAccount](https://adsecurity.org/?tag=groupmanagedserviceaccount), [msDS-GroupManagedServiceAccount](https://adsecurity.org/?tag=msds-groupmanagedserviceaccount), [msDS-GroupMSAMembership](https://adsecurity.org/?tag=msds-groupmsamembership), [msds-ManagedPassword](https://adsecurity.org/?tag=msds-managedpassword), [msDS-ManagedPasswordId](https://adsecurity.org/?tag=msds-managedpasswordid), [msDS-ManagedPasswordInterval](https://adsecurity.org/?tag=msds-managedpasswordinterval), [PrincipalsAllowedToRetrieveManagedPassword](https://adsecurity.org/?tag=principalsallowedtoretrievemanagedpassword)

[![](https://adsecurity.org/wp-content/uploads/2025/08/Twitter-MI4-150x150.png)](https://adsecurity.org/?author=2)

### Sean Metcalf

I improve security for enterprises around the world working for TrustedSec & I am @PyroTek3 on Twitter.

### Leave a Reply [Cancel reply](/?p=4904#respond)

Your email address will not be published.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

## Recent Posts

* [Active Directory Security Tip #14: Group Managed Service Accounts (GMSAs)](https://adsecurity.org/?p=4904)
* [Improve Entra ID Security More Quickly](https://adsecurity.org/?p=4825)
* [BSides NoVa 2025 Presentation Slides Posted](https://adsecurity.org/?p=4799)
* [Microsoft Interview](https://adsecurity.org/?p=4802)
* [Active Directory Security Tip #13: Reviewing Foreign Security Principals (FSPs)](https://adsecurity.org/?p=4784)

## Active Direct...
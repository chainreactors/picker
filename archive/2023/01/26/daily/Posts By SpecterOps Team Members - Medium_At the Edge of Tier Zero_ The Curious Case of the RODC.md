---
title: At the Edge of Tier Zero: The Curious Case of the RODC
url: https://posts.specterops.io/at-the-edge-of-tier-zero-the-curious-case-of-the-rodc-ef5f1799ca06?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-01-26
fetch_date: 2025-10-04T04:53:03.909248
---

# At the Edge of Tier Zero: The Curious Case of the RODC

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fef5f1799ca06&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fat-the-edge-of-tier-zero-the-curious-case-of-the-rodc-ef5f1799ca06&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fat-the-edge-of-tier-zero-the-curious-case-of-the-rodc-ef5f1799ca06&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-ef5f1799ca06---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-ef5f1799ca06---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# At the Edge of Tier Zero: The Curious Case of the RODC

[![Elad Shamir](https://miro.medium.com/v2/resize:fill:64:64/1*ocQXH46k-rk5MSdLEXKXfA.jpeg)](https://medium.com/%40elad.shamir?source=post_page---byline--ef5f1799ca06---------------------------------------)

[Elad Shamir](https://medium.com/%40elad.shamir?source=post_page---byline--ef5f1799ca06---------------------------------------)

13 min read

·

Jan 25, 2023

--

1

Listen

Share

The read-only Domain Controller (RODC) is a solution that Microsoft introduced for physical locations that don’t have adequate security to host a Domain Controller but still require directory services for resources in those locations. A branch office is the classic use case.

While RODCs, by definition, are not part of the set of resources that can control “enterprise identities”, known as Tier Zero, we have seen cases where there is a privilege escalation path from an RODC to domain dominance.

In this blog post, we’ll answer the question, “If I compromise a Read-Only Domain Controller, can I compromise the domain?” or, from an architectural perspective, “Do RODCs belong in Tier Zero?”

## Tl;dr — It’s Complicated

In the context of RODCs, the term “compromise” could mean several things:

1. Elevated access to the RODC host
2. Credential access to the RODC computer account
3. Control of the RODC computer object in Active Directory

In the case of elevated access to the RODC host (1) or credential access to the RODC computer account (2), there is a path for domain dominance only if the RODC is permitted to “reveal” the credentials of a Tier Zero security principal.

In the case of control of the RODC computer object in Active Directory (3), there is a generalized path to domain dominance.

**While the RODC hosts and the credentials for their computer accounts do not belong in Tier Zero, all RODC computer objects must be protected as Tier Zero resources.**

## Intro

Microsoft introduced, and since retired, the Enhanced Security Admin Environment (ESAE) architecture as the ideal for securing Active Directory (AD). Part of that architecture was the Administrative Tiering Model, which defined the concept of “Tier Zero” as a set containing the resources that control enterprise identities and their security dependencies. Most crucially, no resources outside of Tier Zero should have any control over anything inside Tier Zero.

RODCs are an alternative for Domain Controllers in less secure physical locations. They maintain a filtered copy of AD, excluding sensitive attributes, such as LAPS passwords, to support LDAP queries, and cache credentials for selected users and computers to support authentication. Typically, an RODC would be allowed to retrieve and cache credentials only for accounts that belong to the same physical location, such as a branch office, and have an equivalent or lower level of physical security.

By definition, Tier Zero resources *should* not be permitted to operate in less trustworthy locations that require RODCs, and RODCs *should* not control any Tier Zero resource. *Should* is the operative word.

## How Are RODCs Managed?

Domain Controllers don’t have local accounts and local groups per se. When a server is promoted to a Domain Controller, AD replaces the local accounts and groups, and the same applies to RODCs. However, if only Tier Zero admins are permitted to manage Domain Controllers, and RODCs aren’t trustworthy enough for Tier Zero admins to log onto them, then how are RODCs managed?

The *managedBy* attribute does not usually serve any function for an AD object, although it can be used for organizational purposes. However, RODC computer objects are the exception. Any user or group specified in the *managedBy* attribute of an RODC has local admin access to the RODC server (thanks to [Guido Grillenmeier](https://twitter.com/ggrillen) for teaching me that!).

![]()

**If you compromise an account listed in the *managedBy* attribute of an RODC, you have local admin on the RODC. And if you compromise an account with delegated rights to modify the *managedBy* attribute of an RODC, you can make yourself an admin.**

## How Do RODCs Authenticate Users?

RODCs need access to the credentials of users and computers to authenticate them locally. Every RODC should have a specific list of principals that it is designated to authenticate and is therefore allowed to retrieve their credentials. This list is stored in the *msDS-RevealOnDemandGroup* attribute of the RODC’s computer object. The list may contain individual accounts or groups.

![]()

A similar list of principals for whom the RODC is explicitly denied from retrieving credentials is stored in the *msDS-NeverRevealGroup* attribute of the RODC. The deny list takes precedence over the allow list, meaning that if a user is listed in both, either directly or via nested groups, the RODC will not be able to retrieve the account’s credentials.

![]()

After the RODC authenticates a user or computer, it needs to generate a Kerberos ticket-granting-ticket (TGT), but the RODC is not trustworthy enough to have access to the domain’s KRBTGT keys. Instead, when a Windows server is promoted to RODC, AD creates a new, dedicated version of the KRBTGT key. The new RODC will use this key to encrypt and sign the TGTs that it generates. The key is assigned a random key version number (typically five digits), stored in a new AD account named *KRBTGT\_XXXXX,* where *XXXXX* is the key version number. The key version number is also stored in the *msDS-SecondaryKrbTgtNumber* attribute of the new KRBTGT account.

The name of the new KRBTGT account is stored in the *msDS-KrbTgtLink* attribute of the RODC’s computer object, and the name of the RODC computer object is stored in the new KRBTGT account’s *msDS-KrbTgtLinkBl* (backlink) attribute. The RODC computer account is also granted the right to reset the password of the associated KRBTGT account.

```
PS C:\Users\elad> Get-ADComputer RODC -Properties msDS-KrbTgtLink

DistinguishedName : CN=RODC,CN=Computers,DC=shenanigans,DC=labs
DNSHostName       : RODC.shenanigans.labs
E...
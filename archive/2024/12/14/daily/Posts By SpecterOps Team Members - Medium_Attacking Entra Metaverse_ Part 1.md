---
title: Attacking Entra Metaverse: Part 1
url: https://posts.specterops.io/attacking-entra-metaverse-part-1-c9cf8c4fb4ee?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-12-14
fetch_date: 2025-10-06T19:43:56.467207
---

# Attacking Entra Metaverse: Part 1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc9cf8c4fb4ee&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fattacking-entra-metaverse-part-1-c9cf8c4fb4ee&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fattacking-entra-metaverse-part-1-c9cf8c4fb4ee&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-c9cf8c4fb4ee---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-c9cf8c4fb4ee---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Attacking Entra Metaverse: Part 1

[![Daniel Heinsen](https://miro.medium.com/v2/resize:fill:64:64/1*GrMTMBFX3ZJ18iZClwxhcA.jpeg)](https://medium.com/%40hotnops?source=post_page---byline--c9cf8c4fb4ee---------------------------------------)

[Daniel Heinsen](https://medium.com/%40hotnops?source=post_page---byline--c9cf8c4fb4ee---------------------------------------)

7 min read

·

Dec 13, 2024

--

Listen

Share

This is part one in a two (maybe three…) part series regarding attacker tradecraft around the syncing mechanics between Active Directory and Entra. This first blog post is a short one, and demonstrates how complete control of an Entra user is equal to compromise of the on-premises user. For the entire blog series the point I am trying to make is this:

**The Entra Tenant is the trust boundary**

That means that if your tenant consists of 100 domains, a compromise of one domain is likely to equal a compromise in all other domains, assuming line of sight to the targeted domain.

## Intro to Entra Connect Sync

*Entra Connect Sync* is the software responsible for propagating changes between Active Directory and Entra (often still referred to as Azure Active Directory). For most cases, the changes are propagated **from** Active Directory **to** Entra. As a quick example, consider a new user created in an on-premises Active Directory. The next time Entra Connect Sync runs a sync cycle, a special Entra sync account will send a provisioning message to adminwebservice.onmicrosoft.com to create a new Entra user that represents that user. This process has been covered very well and tooling exists to manipulate this syncing mechanic in AADInternals. An interesting, and fairly unexplored, part of this mechanic is the “metaverse” within Entra Connect.

The metaverse is a virtual representation of multiple data sources. Think of it like a conflict manager for directories. Each data source (AD and Entra) are called “connected directories”. The connected directories are enumerated via remote protocol (LDAP, https, etc.) by a connected directory specific “connector”. Each connected directory has a virtual representation called a “connector space” that represents all of the desired data synced from the connected directory. Once a connected directory runs an “import”, all of the users/devices/groups/etc. exist in the connector space. After import, a synchronization is executed and the connector space objects are “projected” into the metaverse.

Press enter or click to view image in full size

![]()

The metaverse object is the aggregation of all associated properties from multiple connected directories. Since this is an abundance of lingo, let’s walk through an example. In Active Directory, I’m going to create a user named “jack.burton@hybrid.hotnops.com”. Once the user is created, we run a “delta import” in the Synchronization Service

Press enter or click to view image in full size

![]()

As you can see, we have one “Add” and the user Jack Burton now exists in the connector space, but not the Metaverse yet.

Press enter or click to view image in full size

![]()

In order for the Jack Burton user to be projected into the metaverse, we need to run a sync. In this case, I’ll run a delta sync.

Press enter or click to view image in full size

![]()

Clicking on the “Projections” link, we can see that a new user has been projected into the Metaverse.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

There is also a new export attribute flow, which indicates that this user is to be provisioned to another connected directory (Entra). To trigger this provision, we lastly need to run an export on the Entra connector space.

Press enter or click to view image in full size

![]()

Don’t worry about the export errors, I have been doing *stuff*. At this point, we have an end to end flow of an object being created in AD, projected into the metaverse, and then provisioned in Entra. But from the Entra Connect standpoint, there’s no special differentiator between Entra and Active Directory, they are both simply connector spaces.

***So can attributes go from Entra to Active Directory?***

Yes!

The flow of attributes are specified by the Entra Connect rules, which have a default setup that I will speak to in the next blog post. By default, there is one and only one attribute that is written from an Entra user to an Active Directory user and that is the *searchableDeviceKey -> msDS-KeyCredentialLink* attribute flow. If msDS-KeyCredentialLink sounds familiar, it’s because it has been covered extensively as an abuse primitive known as “[Shadow Credentials](/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab)”. Long story short, if we can add a public key to the msDS-KeyCredentialLink attribute of a user, we can obtain a TGT for that user with the private key. This means that if we can add a key to an Entra user, we can authenticate as them on-premises. This will prove to be a powerful primitive in the following blog posts when we do a deeper dive on Metaverse and cross domain attacks.

## Abusing the WHFB key to gain access to on-premises account

Any key material (Window Hello For Buiness or FIDO2) key that is added to an Entra user will be synced down to the on-premises user to the msDS-KeyCredentialLink attribute. To perform this attack, we are assuming complete control of an Entra user account. This includes plaintext password and access to MFA methods. We will try to ease these assumptions later, but for now I simply want to prove-out the idea.

Press enter or click to view image in full size

![]()

Here are the following commands that we can run to get an msDS-KeyCredentialLink set on the on premises user. As a high level overview, we are going to be registering a WHFB key. We could also do a FIDO2 key in theory, but this will be easier for demonstration. This attack, at the moment, requires knowledge of the plaintext password and possession of at least one MFA authenticator. To register a WHFB key, we are going to create a fake device, obtain a PRT, and enrich it with an ng...
---
title: IPS: Availability of system connectors
url: https://blogs.sap.com/2023/03/01/ips-availability-of-system-connectors/
source: SAP Blogs
date: 2023-03-02
fetch_date: 2025-10-04T08:26:22.331119
---

# IPS: Availability of system connectors

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* IPS: Availability of system connectors

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161202&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [IPS: Availability of system connectors](/t5/technology-blog-posts-by-sap/ips-availability-of-system-connectors/ba-p/13560137)

![D_Olderdissen](https://avatars.profile.sap.com/b/3/idb3832ed980dfa483dbb9872687b640a353a76c4713f07944bd3f898c9faf3b6f_small.jpeg "D_Olderdissen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[D\_Olderdissen](https://community.sap.com/t5/user/viewprofilepage/user-id/8605)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161202)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161202)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560137)

‎2023 Mar 01
11:47 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161202/tab/all-users "Click here to see who gave kudos to this post.")

3,256

* SAP Managed Tags
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [Identity Provisioning](https://community.sap.com/t5/c-khhcw49343/Identity%2520Provisioning/pd-p/73555000100800000425)

* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [Identity Provisioning

  SAP Business Technology Platform](/t5/c-khhcw49343/Identity%2BProvisioning/pd-p/73555000100800000425)

View products (2)

# About me (disclaimer)

In my role at SAP, I help our customers to wrap their heads around the security of SAP Cloud Products. As I am doing that in a presales capacity for many years, I have been part of many deals, discussion and architecture talks. But as I am NOT a consultant who tinkers with those SAP Systems every day, I can and will not provide any type of recommendations. All of my writings are purely my own opinion. So you need to read the respective sources and documents that I may have interpreted (wrongly) and come up with your own educated decisions.

# Identity Provisioning Service (IPS)

The [IPS](https://help.sap.com/docs/IDENTITY_PROVISIONING) is part of the [SAP Identity Services (IAS+IPS](https://help.sap.com/docs/SAP_CLOUD_IDENTITY)). It does transport User Identities and their assigned roles from one system to an other. In order to do that, IPS does bring a bunch of so called connectors and it also exposes a SCIM interface.

## IPS flavors

IPS does have a bit of a history and in consequence there are two flavors available. The main [differentiating factor is the infrastructure](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/329794b497934389b1f1552deb048dca.html) they are deployed upon which can be:

* BTP NEO
* SAP Identity Services Infrastructure

### IPS tenant on BTP NEO

These IPS tenants are deployed as a BTP NEO service. That means handling them should be mostly like any other BTP NEO service. e.g. Login via Cloud Cockpit, rights assignment etc.
The connectors of these tenants [are tied to the so called "Bundles"](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/5db6c8dcf7a347fe81e2a78c3df9ec50.html). And you will most likely already have experienced what the documentation is describing

> "... if your bundle tenant is running on SAP BTP, Neo environment, a limited number of connectors are enabled by default."

So depending on what SAP Cloud Service your company has signed up for, [this or that bundle will be applicable and with that the "bundle connectors" will be more or less a...](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/174d566f39ac4c8ea48d4eafd7f28034.html) to you. As the various bundles have been created with different scenarios in mind and some intended bundles never got to see the light of day, there have been "a few" cases where customers might have gotten stuck with being unable to get a connector.

### IPS on SAP Identity Services Infrastructure (new)

As part of [evolving the IAS & IPS into the SAP Cloud Identity Services](https://blogs.sap.com/2020/06/24/evolving-identity-authentication-and-identity-provisioning-into-sap-cloud-identity-services/), any newly provisioned IPS tenant is deployed on the SAP Cloud Identity Services Infrastructure [since March 15th 2022](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/329794b497934389b1f1552deb048dca.html).
The (new) IPS tenants [bring most of the available system connectors](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/5db6c8dcf7a347fe81e2a78c3df9ec50.html#connectors-availability-in-bundle-tenants-on-sap-cloud-identity-infrastructure) out of the box right away. Let`s look at this particular part of the documentation (as of 02/26/2023) below. If you read carefully, it says all connectors are available just not those listed in this table.

![](/legacyfs/online/storage/blog_attachments/2023/02/Screenshot-2023-02-28-185746.png)IPS SAP Help: Most connectors are available

# Q&A

### How do I find out if my IPS tenant is "New" or still on BTP NEO?

You might [want to try the IAMTENANTS interface](https://help.sap.com/docs/IDENTITY_AUTHENTICATION/6d6d63354d1242d185ab4830fc04feb1/f56e6f24e373404087d6a1a9a13515a2.html). That system should give you a list of all your available IAS & IPS tenants and when they have been created. The creation date is a very good indicator of what IPS deployment type you are facing - anything deployed after [March 15th 2022](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/329794b497934389b1f1552deb048dca.html) should be a IPS tenant on SAP Cloud Identity Infrastructure. And thus should contain most of the connectors right away.
You can also check if you can access the IPS tenant like any other BTP NEO service. If yes, you obviously got a BTP NEO IPS tenant.

[IPS tenants with this service URL syntax](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/61fd82ed48ab42b2bc74626926c1722c.html) should be on the new infrastructure

> https://<tenant\_id>.accounts.ondemand.com/ips/

### How to get access to all those bundle connectors in my IPS?

You could consider [migrating your existing IPS Neo tenant to the SAP Identity Service infrastructure](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/055f92d5e11d491c97b68223c68179ad.html). Please read the documentation carefully and do not trigger a migration lightly. Remember the good old mantra "never touch a running system".

### There are still connectors missing in my IPS?

Revisit the documentation if connector you are missing [is not officially excluded](https://help.sap.com/docs/IDENTITY_PROVISIONING/f48e822d6d484fa5ade7dda78b64d9f5/5db6c8dcf7a347fe81e2a78c3df9ec50.html#connectors-availability-in-bundle-tenants-on-sap-clou...
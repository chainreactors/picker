---
title: Setup Single Sign-On in SAP HANA Cloud Administration Tools
url: https://blogs.sap.com/2023/03/24/setup-single-sign-on-in-sap-hana-cloud-administration-tools/
source: SAP Blogs
date: 2023-03-25
fetch_date: 2025-10-04T10:36:49.052541
---

# Setup Single Sign-On in SAP HANA Cloud Administration Tools

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Setup Single Sign-On in SAP HANA Cloud Administrat...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163720&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Setup Single Sign-On in SAP HANA Cloud Administration Tools](/t5/technology-blog-posts-by-sap/setup-single-sign-on-in-sap-hana-cloud-administration-tools/ba-p/13567752)

![kevin_li](https://avatars.profile.sap.com/d/f/iddf316bc09d7d4bd1b944b6a3eb09d99ef883f49b33dc6655f2401a1a1a2152b2_small.jpeg "kevin_li")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[kevin\_li](https://community.sap.com/t5/user/viewprofilepage/user-id/248561)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163720)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163720)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567752)

‎2023 Mar 24
11:04 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163720/tab/all-users "Click here to see who gave kudos to this post.")

5,273

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)

View products (4)

As SAP HANA Cloud is a modern database as a service (DBaaS), the end users can access SAP HANA Cloud from anywhere with public internet, whether that’s at home, in the office, or even at a third space like a coffee shop. When an organization wants to move to SAP HANA Cloud, the authentication method is a critical component of an organization’s presence in the cloud. The identity authentication controls access to all cloud data and resources. Organizations need an identity control plane that strengthens their security and keeps their cloud data safe from intruders.

SAP HANA Cloud administration tools includes SAP HANA Cloud Central, SAP HANA cockpit and SAP HANA database explorer. By default, the administrators log into the administration tools using SAP Identity Service. You can also use your bundled SAP Identity Authentication service tenant to log into the administration tools ([Establish Trust and Federation of Custom Identity Providers for Platform Users [Feature Set B]](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/c36898473d704e07a33268c9f9d29515.html?version=Cloud "https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/c36898473d704e07a33268c9f9d29515.html?version=Cloud")). Furthermore, you can configure [SAP Identity Authentication tenant as a proxy](https://blogs.sap.com/2021/06/14/setup-multiple-identity-providers-for-sap-analytics-cloud/) to delegate authentications to your Corporate Identity Provider, which enables a seamless, flexible integration with your existing identity authentication infrastructure.

How can you log into SAP HANA Cloud cockpit using single sign-on? How can you connect to SAP HANA database without entering user and password? This blog demonstrates a solution that you can enable JSON Web Token single sign-on (JWT SSO) to log into SAP HANA Cloud cockpit, and connect to SAP HANA database in SAP HANA database explorer. The identity of users accessing the SAP HANA database from cockpit or database explorer can be authenticated by tokens issued by a trusted JWT identity provider. The internal database user to which the external identity is mapped is used for authorization checks during the database session.

![](/legacyfs/online/storage/blog_attachments/2023/03/hana-cloud1-1.png)

Architecture of End-to-end Single Sign-On in SAP HANA Cloud

## Enable JWT SSO Login

1. Log into SAP HANA Cloud cockpit as database administrator.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit1.png)

Logon as Database Administrator

2. On the Database Overview page, click **Enable JWT SSO**, which is located on the shellbar at the top of the page.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit2.png)

Enable JWT SSO

3. Confirm that you want to enable JWT SSO.

***Note**: JWT SSO has to be enabled on each SAP HANA Cloud database individually.*

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit3.png)

Confirmation of JWT SSO

 4. Navigate to the **JWT Identity Providers** application on the Database Overview page to verify the identity providers.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit6.png)

JWT Identity Providers Application

5. You can see a JWT identity provider created by the cockpit. The naming convention for identity providers is: *`XSUAA_JWT_PROVIDER_<uppercase issuer>_<uppercase origin>_<uppercase zone id>`*.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit7.png)

JWT Identity Provider

6. Change the origin value to the origin of your custom identity provider for platform users. If you previously log into the cockpit using your custom IdP before enabling JWT SSO, this value should already be the origin of your custom IdP.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit11-1.png)

*The Origin of Your Custom Identity Provider*

## Create a Database User

1. Navigate to the **User Management** application on the Database Overview page to create and manage database users.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit4.png)

User Management Application

2. Edit an existing database user to edit their configuration, if the user doesn't exist, create a new database user.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit5-1.png)

Database User

3. On the Authentication tab for the database user, click **Add JWT Identity**.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit13.png)

Add JWT Identity Provider

4. Select the identity provider from the dropdown list and then either manually map it to an external identity.

![](/legacyfs/online/storage/blog_attachments/2023/03/cockpit12.png)

Mapping to an External Identity

## Test Logon via Single Sign On

1. Now, you can return to the Database Overview page and click **Log in as a Different User**.

![](/legacyfs/online/storage/blog_attachments/2023/03/c...
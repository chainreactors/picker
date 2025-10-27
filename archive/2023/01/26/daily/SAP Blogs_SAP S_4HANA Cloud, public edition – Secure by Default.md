---
title: SAP S/4HANA Cloud, public edition – Secure by Default
url: https://blogs.sap.com/2023/01/25/sap-s-4hana-cloud-public-edition-secure-by-default/
source: SAP Blogs
date: 2023-01-26
fetch_date: 2025-10-04T04:51:50.772493
---

# SAP S/4HANA Cloud, public edition – Secure by Default

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Cloud, public edition – Secure by Defa...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50568&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Cloud, public edition – Secure by Default (Part 2)](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-cloud-public-edition-secure-by-default-part-2/ba-p/13551008)

![Florian_Eller](https://avatars.profile.sap.com/c/5/idc5f2abf7bbd1f282474e33b4121cc0f6220be9ba9459b247aa8c78101be4a2f7_small.jpeg "Florian_Eller")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[Florian\_Eller](https://community.sap.com/t5/user/viewprofilepage/user-id/131555)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50568)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50568)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551008)

‎2023 Jan 25
9:12 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50568/tab/all-users "Click here to see who gave kudos to this post.")

5,104

* SAP Managed Tags
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (2)

Comparing SAP S/4HANA Cloud, public edition, with SAP S/4HANA on premise, several differences in its IT audit capabilities become obvious. This blog post is part of a series of articles where we compare the audit process of SAP S/4HANA Cloud, public edition, with the audit process for SAP S/4HANA on Premise.

To summarize the most important differences: As SAP S/4HANA Cloud, public edition, is a SaaS offering, the most obvious difference is customer access, which is only possible on application level.

SAP has also evolved its user experience with ERP transactions being replaced by SAP Fiori apps, applications providing access to business functionality in a more modern way. That is why customers only have access through business authorizations authenticated using SAP Identity Authentication Services.

Compared to SAP S/4HANA on premise running in an on-premise environment, some functionality has been replaced with modern apps, some configurations are in the responsibility of SAP and some functionality is no longer accessible. Some examples:

+ System access is only possible through a dedicated authentication service

+ Critical authorizations are no longer available (e.g., SAP\_ALL, or debug and replace authorizations)

+ System table access is no longer possible

+ Direct execution of ABAP reports or transaction codes is no longer available

+ System software changes are applied by SAP on a regular schedule

# Secure by Default

Another area where a SaaS offering differs from an on premise solution is the configuration of security relevant settings.

In a cloud environment, as is the case with SAP S/4HANA Cloud, public edition, SAP is responsible for most platform-related security configurations and has hereby followed a [secure-by-default](https://en.wikipedia.org/wiki/Secure_by_design) approach, which can be clustered into the following paragraphs.

These paragraphs provide more details on the measures SAP applied to SAP S/4HANA Cloud, public edition, and the options customers still have to access required functionality in case of an IT audit.

# Authentication and Authorization

Customer business user authentication is solely possible through a dedicated identity provider, for example the SAP Identity Authentication Service. This also means that authentication settings (e.g., password policy) cannot be reviewed on SAP S/4HANA Cloud, public edition, systems themselves.

Further, so-called business catalogs represent the smallest authorizations entity for customers. Critical authorizations (e.g., containing SAP\_ALL profile or debug & replace authorization) are not available for customers, similar to SAP default users (e.g., users DDIC, SAP\* or TMSADM).

Particularly, technical users must be mentioned here as well. In an on-premise environment, -SAP has not defined roles and authorizations for technical users in the context of a communication scenario, for example establishing a connection between two on-premise systems. In SAP S/4HANA Cloud, public edition, communication users for a similar scenario are strictly defined so that authorizations fit the respective communication arrangement.

While an SAP S/4HANA on premise solution provides report RSUSR100N to access user-related change documents across the system, in SAP S/4HANA Cloud, public edition, two SAP Fiori apps are now available to support customers in getting an overview of existing business users and their authorizations. Users for communication scenarios can be reviewed in a separate SAP Fiori app ([Maintain Communication Users – F1338](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/index.html#/detail/Apps('F1338')/S28)).

## [Maintain Business Users – F1303](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/index.html#/detail/Apps('F1303')/S28)

As the name implies, the SAP Fiori app Maintain Business Users allows editing of business user data, e.g., assigning or removing roles, locking or unlocking users or downloading a list of users. This app also contains the user related change documents to trace user changes like creation, locking, etc.

![](/legacyfs/online/storage/blog_attachments/2022/12/01_Maintain_Business_Users.png)

SAP Fiori application "Maintain Business Users"

## [IAM Information System – F2450](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/index.html#/detail/Apps('F2450')/S28)

The SAP Fiori app IAM Information System allows for the display of information about the usage of business roles, business catalogs, business users and restrictions, and how they are related. The functionality is similar to transaction SUIM in the SAP S/4HANA on premise solution. For example, you can use this app to check if a business user is using a particular app and to check which authorizations they have.

![](/legacyfs/online/storage/blog_attachments/2022/12/02_IAM_Information_System.png)

SAP Fiori application "IAM Information System"

# Security Configuration

As mentioned before, contrary to an on-premise solution, system table access is not possible in SAP S/4HANA Cloud, public edition. As a result, access to tables like USR02, or E070 is not possible. Table data can be accessed through corresponding SAP S/4HANA Cloud Fiori applications, e.g. Maintain Business Users or the recently introduced [Customer Data Browser (CDB)](https://blogs.sap.com/2022/...
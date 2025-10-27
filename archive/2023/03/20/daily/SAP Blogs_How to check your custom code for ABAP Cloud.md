---
title: How to check your custom code for ABAP Cloud
url: https://blogs.sap.com/2023/03/19/how-to-check-your-custom-code-for-abap-cloud/
source: SAP Blogs
date: 2023-03-20
fetch_date: 2025-10-04T10:04:57.544042
---

# How to check your custom code for ABAP Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to check your custom code for ABAP Cloud

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52991&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to check your custom code for ABAP Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-check-your-custom-code-for-abap-cloud/ba-p/13567124)

![OlgaDolinskaja](https://avatars.profile.sap.com/3/d/id3de2dde04a1aa64b641424db3bbbc1eb95d2a09d6ce8813af73d131db316e370_small.jpeg "OlgaDolinskaja")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[OlgaDolinskaja](https://community.sap.com/t5/user/viewprofilepage/user-id/6638)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52991)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52991)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567124)

‎2023 Mar 19
9:02 PM

[40
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52991/tab/all-users "Click here to see who gave kudos to this post.")

23,569

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [ABAP Testing and Analysis](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Testing%2520and%2520Analysis/pd-p/808952988084195139233186926963168)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [ABAP Cloud](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Cloud/pd-p/9ada5ac7-3f77-49de-b5c9-9019df1d1e09)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [ABAP Testing and Analysis

  Programming Tool](/t5/c-khhcw49343/ABAP%2BTesting%2Band%2BAnalysis/pd-p/808952988084195139233186926963168)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Cloud

  Software Product Function](/t5/c-khhcw49343/ABAP%2BCloud/pd-p/9ada5ac7-3f77-49de-b5c9-9019df1d1e09)

View products (7)

As you for sure already know, ABAP Cloud was announced at SAP TechEd 2022 and was part of the [Juergen Mueller’s day 1](https://youtu.be/CIwmZkGH9f8?t=1991) and [Philipp Herzig’s day 2](https://youtu.be/fNGdQ0Xzadk?t=2370)  keynotes. ABAP Cloud is the ABAP development model to build cloud-ready business apps, services, and extensions on the SAP products SAP BTP ABAP Environment, SAP S/4HANA Cloud, public edition, and SAP S/4HANA 2022 Cloud, private edition and on-premise.

You can find more details about ABAP Cloud in the [ABAP Development SAP Community](https://community.sap.com/topics/abap) under the „ABAP Cloud - Developer Resources“ section, and in the [ABAP Cloud](https://blogs.sap.com/2022/12/22/abap-cloud/) blog by the Chief Product Owner of the ABAP Platform boris.gebhardt.

As we have thought about, how to support SAP customers and partners on releases < 2022, who want to strive for the clean core with ABAP Cloud in their landscapes and use released APIs as much as possible we came up with the following considerations.

Currently you can use the Custom Code Migration app  to check your custom code for cloud readiness with the purpose of migration to the SAP BTP ABAP Environment. See also the blog [How to check your custom ABAP code for SAP BTP ABAP Environment](https://blogs.sap.com/2018/10/02/how-to-check-your-custom-abap-code-for-sap-cloud-platform-abap-environment/). In this case the cloud readiness checks will be executed over your custom code in the on-premise system to detect, if your custom code is compliant to the ABAP language version „ABAP for Cloud Development“ , if it uses only allowed object types in the cloud, or if it uses only released APIs of the SAP BTP ABAP Environment system.

These checks are essential for the custom code migration to the SAP BTP ABAP Environment but insufficient if you want to check your custom code for ABAP cloud development model in an SAP S/4HANA system. In this case you would need additionally check your code for the released application APIs of the SAP S/4HANA solution in the target systems, and ideally already get the recommendation which successor released APIs from the SAP S/4HANA application stack to use.

Based on these considerations we have got an idea to provide the information about the released successor APIs for ABAP cloud development on the GitHub in the so-called Cloudification Repository. This information can be then used as the input for the ABAP Test Cockpit cloud readiness checks for released APIs (analogous to the Simplification Database for SAP S/4HANA readiness checks).

The Cloudification Repository can be used with the latest version of the Custom Code Migration app in the SAP BTP ABAP Environment (2302 release).

|
 **NOTE:** The Cloudification Repository is the substitute for using the SAP Note [3088062 - Identifying local APIs for S/4HANA Cloud](https://launchpad.support.sap.com/#/notes/3088062), where you need to look up for the successor released APIs manually in the Excel table. |

![](/legacyfs/online/storage/blog_attachments/2023/02/cloud_repo_overview.png)

Let’s take a look in detail at how it works.

## Choose a custom code package for analysis

We take as an example the ABAP custom code package ZS4HANA\_CLOUD\_MIGRATION\_DEMO in the SAP ERP system. This package should be migrated to the SAP S/4HANA Cloud, public edition, and therefore it must be adapted compliant to the ABAP cloud development model.

![](/legacyfs/online/storage/blog_attachments/2023/02/custom_package.png)

This package contains among other things the ABAP source code objects, like for example the classes ZCL\_MARA\_USAGE and ZCL\_KONV\_USAGE which are not compliant to the ABAP cloud development model, because they access directly with the openSQL the SAP application tables MARA and KONV instead of using the corresponding released APIs:

![](/legacyfs/online/storage/blog_attachments/2023/02/mara_usage.jpg)![](/legacyfs/online/storage/blog_attachments/2023/02/konv_usage.jpg)

Other ABAP source code objects in this package a...
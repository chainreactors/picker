---
title: Understanding license type Basic vs Advanced for SAP Extended Warehouse Management
url: https://blogs.sap.com/2023/08/20/understanding-license-type-basic-vs-advanced-for-sap-extended-warehouse-management/
source: SAP Blogs
date: 2023-08-21
fetch_date: 2025-10-04T11:59:31.486040
---

# Understanding license type Basic vs Advanced for SAP Extended Warehouse Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* Understanding license type Basic vs Advanced for S...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/5379&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Understanding license type Basic vs Advanced for SAP Extended Warehouse Management](/t5/supply-chain-management-blog-posts-by-sap/understanding-license-type-basic-vs-advanced-for-sap-extended-warehouse/ba-p/13580547)

![diogo_iran](https://avatars.profile.sap.com/3/8/id38be74732205cdfba51cebaae81e4d4e3ce4fb705e8a63fa4cda65de896be1e9_small.jpeg "diogo_iran")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[diogo\_iran](https://community.sap.com/t5/user/viewprofilepage/user-id/139273)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=5379)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/5379)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580547)

‎2023 Aug 20
11:29 PM

[18
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/5379/tab/all-users "Click here to see who gave kudos to this post.")

36,453

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [EWM - Basic Functions](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Basic%2520Functions/pd-p/212269919429502086862800135639950)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Basic Functions

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BBasic%2BFunctions/pd-p/212269919429502086862800135639950)

View products (3)

### **Introduction**

In this blog post I will bring your attention for a very common question raised by customers and about the features available on SAP Extended Warehouse Management for license type Basic and Advanced. It means, understand the difference between each license type in order to be able to maximize all the features for the solution designed.

During the life cycle project implementation, when closing the Explore phase or more lately at the beginning of Realize phase, customers and/or partners realized there is a potential impact on the solution designed depending on the license type available for SAP Extended Warehouse Management.

Let's straight to the point and understand which features are part of the Basic License type in which are not. And how this information is relevant for customer to be license compliance and be able to use the all needed features for the warehouse system

### **Basic x Advanced License Type**

Before explain the features available for license type, let's recap and understand the deployment model for SAP Extended Warehouse Management. The solution can be deployed as Embedded or Decentral. In both case for On Premise or running SAP S/4HANA Cloud, private Edition.

Embedded deployment means, run SAP Extended Warehouse Management on the same client of SAP S/4HANA, which is possible since SAP S/4HANA 1610. On the other hand, Decentralized deployment means roughly, run SAP Extended Warehouse Management in a different system of SAP S/4HANA but totally integrated with the core solution for Master data and Transactional Data.

I encourage you to check the latest SAP Note S/4HANA 2022 version [SAP note 3218648 - SAP S/4HANA 2022 FPS00 and FPS01: Release information and restrictions for EWM in...](https://me.sap.com/notes/3218648/E), where you can find detailed information of all features and limitation available for each SAP EWM deployment type.

The license type differentiation for Basic or  Advanced is only applicable for embedded deployment cases.. The Decentral deployment always requires the advanced license type, it means, all the features available on product can be used by customer without any risk on being noncompliance. You can also find the definition of extended features which trigger to need for the EWM license in case of embedded EWM on [SAP S/4HANA Feature Scope Description](https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2022/en-US/FSD_OP2022_latest.pdf) on chapter "SAP S/4HANA LOB functions".

From the solution perspective it is documented on the following IMG Customizing path: *Extended Warehouse Management / Master Data / Acknowledge Use of Advanced Functions.*

![](/legacyfs/online/storage/blog_attachments/2023/08/Blog_EWM_FIG1.jpg)

Features included in each license type

Once customers understand that, the License type is only relevant for  Embedded deployment model, questions may arise such as "What features are included on basic license type?"

For Basic license type, customers are able to perform the main process end to end such as, Inbound, Outbound, Production Integration, Quality management integration, etc. Below you can find all the process included on basic license:

* Inventory Management

* Inbound Processing

* Outbound Processing

* Internal Warehouse Movements

* Physical Inventory

* Reporting (Warehouse Management Monitor, Analytics)

* Resource Management

* Quality Management

* Production Integration

* Integration with Transportation Management (ASR)

* IDOC Integration to third-party MFS systems (SAP Note 2873423)

The advanced license might be required in case of customer would use some features enclosed of the main process, for example, the outbound process designed is required to use Wave management or, the production integration is required to use JIT - Just in Time. It means that the Advanced license type is required in case of use some specific SAP EWM features, such as:

* Material Flow System (MFS)

* Wave Management

* Transportation units

* Yard Management

* Labor Management

* Cross Docking

* Value Added Services (VAS)

* Warehouse Billing

* Kitting

* Dock Appointment Scheduling (DAS)

* Slotting

* Cartonization planning

* Distribution Equipment

* JIT

* WIP Tracking

* Warehouse Zones for advanced interleaving

![](/legacyfs/online/storage/blog_attachments/2023/08/Blog_EWM_FIG2.jpg)

License Management

The list of the extended objects for SAP EWM embedded is technically found on table /SCWM/EXT\_OBJ. SAP Product Solution Team provide 2 reports for customers perform in their system in order to know which objects is being used on their warehouse system with usage detail

* Report /SCWM/RP\_COMPLIANCE\_CHECK is available since S/4HANA 2016 (and higher) and provides the information if the customizing or the licensing  is compliance or non-compliance for each warehouse system.

* Report /SCWM/RP\_LICENCE\_SELF\_AUD**I****T** is available since S/4HANA 2022 (and higher) and provides by warehouse number a view by month of usage of Basic and Advanced features by total num...
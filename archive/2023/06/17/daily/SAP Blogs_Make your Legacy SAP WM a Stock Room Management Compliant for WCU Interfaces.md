---
title: Make your Legacy SAP WM a Stock Room Management Compliant for WCU Interfaces
url: https://blogs.sap.com/2023/06/16/make-your-legacy-sap-wm-a-stock-room-management-compliant-for-wcu-interfaces/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:47:15.817075
---

# Make your Legacy SAP WM a Stock Room Management Compliant for WCU Interfaces

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Make your Legacy SAP WM a Stock Room Management Co...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67999&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Make your Legacy SAP WM a Stock Room Management Compliant for WCU Interfaces](/t5/enterprise-resource-planning-blog-posts-by-members/make-your-legacy-sap-wm-a-stock-room-management-compliant-for-wcu/ba-p/13562262)

![prakashpol1](https://avatars.profile.sap.com/9/8/id983b818054ad6dc9706dcc495d111f6ae482b5a853c715cf9e36ef3954aa7c2b_small.jpeg "prakashpol1")

[prakashpol1](https://community.sap.com/t5/user/viewprofilepage/user-id/581002)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67999)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67999)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562262)

‎2023 Jun 16
12:52 PM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67999/tab/all-users "Click here to see who gave kudos to this post.")

11,635

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [LE Warehouse Management](https://community.sap.com/t5/c-khhcw49343/LE%2520Warehouse%2520Management/pd-p/228778767752950234642521143175334)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [LE Warehouse Management

  Software Product Function](/t5/c-khhcw49343/LE%2BWarehouse%2BManagement/pd-p/228778767752950234642521143175334)

View products (3)

**Introduction**: The objective of this blog is to share my insights on the topic of S/4HANA migration for the Warehouse Control Unit interfaces (WM-LSR) in the classical SAP LE-WM of legacy ECC system.

The control of material movements in the warehouse is hardly carried out manually but by an automated warehouse control units (WCUs). The task of the WCU is to control and monitor the warehouse automation like conveyor systems, automatic loading and unloading equipments etc.

In certain cases, WCU interface messages are not only used for WCU integration but even to integrate other third party warehouse systems like that of 3PL.

As shared in my earlier blog, [What Options to Consider if Legacy LE-WM is Not Compliant for Stock Room Management during S/4HANA M...](https://blogs.sap.com/2022/10/18/what-options-to-consider-if-legacy-le-wm-is-not-compliant-for-stock-room-management-during-s-4hana-migration/)

Warehouse Control Unit (WCU) Interfaces are implemented in LE-WM either via standard ALE IDOC Interface approach or via RFC approach (IMG configuration driven settings), however this is now no longer a part of the the SAP recommended architecture within SAP S/4HANA; since LE-WM itself is now trimmed down to a basic WM in S/4HANA in the form of stock room management.

However, If it is still decided by the organization to migrate classical ECC LE-WM by using Stock Room Management in S/4HANA, this strategy would first require making such warehouse fully compliant by removing the non-compliant configuration of WCU Integration in legacy ECC system. Removal of such non-compliant configuration requires the alternative solution implementation in ECC LE-WM in the form of pre-project, this custom solution will help by retaining the these WCU interfaces even after S/4HANA migration and at the same time making ECC LE-WM warehouses fully compliant with S/4HANA Stock Room Management.

![](/legacyfs/online/storage/blog_attachments/2023/06/Figure1-5.jpg)

**Step 1: Removal of WM-LSR configuration in ECC LE-WM**

Below important configuration settings should be reviewed in legacy ECC system and either removed or deactivated in order to make warehouse number compliant with Stock Room Management.

![](/legacyfs/online/storage/blog_attachments/2023/06/Setting1.jpg)

**1a. Main IMG node for setting up WM-LSR interfaces**

![](/legacyfs/online/storage/blog_attachments/2023/06/Setting2.jpg)

**1b. Warehouse Number Activation Config. for WM-LSR interfaces**

![](/legacyfs/online/storage/blog_attachments/2023/06/Setting3.jpg)

**1c. ECC to External System Interface Configuration**

After deactivating and removing above config. settings, proceed to the next step of implementing alternative solution to integrate WCUs with ECC.

**Step 2: Implement key WM user-exits in ECC to replace standard WM-LSR approach for Integration with WCU**

Some user  exits in LE-WM, for example as given below that are used to send warehouse tasks to WCU towards end of transfer order creation for the outbound transmission of IDocs, can be considered.

* Enhancement MWMTO001 (Enhancements for end of transfer order generation)

* Function exit EXIT\_SAPLL03T\_001

Standard WM-LSR (WCU config.) provided WMTORD can be replaced with ZWMTORD and this Z-IDoc can be triggered and filled after Transfer Order (TO) is saved.

* Enhancement MWMTO002 (Enhancements at end of transfer order confirmations)
  Function exit EXIT\_SAPLL03T\_002

Standard WM-LSR (WCU config.) provided WMTOCO can be replaced with ZWMTOCO (can be Inbound/outbound both) and this Z-IDoc can either be used to confirm Transfer Orders or send already confirmed Transfer Orders to WCU.

**Step 3: Migrate LE-WM custom code during ECC system conversion to S/4HANA**

As part of overall S/4HANA migration execution, especially using the SPAU/SPDD step after the system conversion step is completed, one can adjust these already implemented custom user-exists, if needed.

Once these custom objects are migrated and available in S/4HANA too, S/4HANA is now ready to send Stock Room Management triggered custom IDocs to WCU and also to receive it from WCU.

**Conclusion:** LE-WM can be converted into Stock Room Management compliant during S/4HANA migration, provided that the non-compliant component like WM-LSR used in WCU integration is deactivated and removed, plus an alternative solution is implemented in LE-WM as a pre-project prior to S/4HANA migration for triggering, filling and transmitting custom developed IDocs to WCU.

Key References:

1. [What Options to Consider if Legacy LE-WM is Not Compliant for Stock Room Management during S/4HANA M...](https://blogs.sap.com/2022/10/18/what-options-to-consider-if-legacy-le-wm-is-not-compliant-for-stock-room-management-during-s-4hana-migration/)

2. [Should I migrate from LE-WM to Stock Room Management? by Prakash Pol](https://blogs.sap.com/2020/05/29/should-i-migrate-from-le-wm-to-stock-room-management/)

3. [Stock Room Management Comparison with EWM by Prakash Pol](https://blogs.sap.com/2021/10/06/stock-room-management-comparison-with-ewm/)

4. Note 2577428 – Road map for LE-WM in SAP S/4HANA

5. 2270211-  – S4TW...
---
title: Outbound Process – From DC site to Customer in S/4 HANA embedded EWM TM – Advanced Shipping & Receiving (ASR) integration – Shipper’s Scenario
url: https://blogs.sap.com/2023/01/17/outbound-process-from-dc-site-to-customer-in-s-4-hana-embedded-ewm-tm-advanced-shipping-receiving-asr-integration-shippers-scenario/
source: SAP Blogs
date: 2023-01-18
fetch_date: 2025-10-04T04:08:40.415709
---

# Outbound Process – From DC site to Customer in S/4 HANA embedded EWM TM – Advanced Shipping & Receiving (ASR) integration – Shipper’s Scenario

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Outbound Process – From DC site to Customer in S/4...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4985&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Outbound Process – From DC site to Customer in S/4 HANA embedded EWM TM – Advanced Shipping & Receiving (ASR) integration - Shipper's Scenario](/t5/supply-chain-management-blog-posts-by-members/outbound-process-from-dc-site-to-customer-in-s-4-hana-embedded-ewm-tm/ba-p/13570472)

![PrashantSoman](https://avatars.profile.sap.com/b/f/idbfce280717bc36e64d1eeb621bb3e92f36fd3f1627dddfb83ff25c44752f9817_small.jpeg "PrashantSoman")

[PrashantSoman](https://community.sap.com/t5/user/viewprofilepage/user-id/45412)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4985)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4985)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570472)

‎2023 Jan 17
10:47 PM

[20
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4985/tab/all-users "Click here to see who gave kudos to this post.")

14,604

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)
* [EWM - Shipping and Receiving](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Shipping%2520and%2520Receiving/pd-p/551700313515132864819929295213440)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [EWM - Shipping and Receiving

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BShipping%2Band%2BReceiving/pd-p/551700313515132864819929295213440)

View products (3)

Many industries have been using Logistics Execution - Transportation (LE-TRA) to support their shipping process in SAP. As per the latest change from SAP, the compatibility package support is valid till the end of 2030 (see KBA [2269324](https://launchpad.support.sap.com/#/notes/2269324)).

As part of S/4 HANA digital supply chain transformation journey, many industries prefer to migrate from their existing process in warehouse management (SAP WM) and LE-TRA to embedded EWM (Extended Warehouse Management) and embedded TM (Transportation Management) respectively. Depending upon their overall IT needs (budget, business volume, complexity, urgency etc), the companies decide whether to go for basic or advanced EWM / TM.

This ASR (Advanced Shipping and Receiving) scenario is explained using basic embedded EWM and advanced embedded TM in S/4 HANA 2022 as the transportation planning process is order-based. (The same process will work using basic EWM and basic TM using delivery-based transportation planning.)

**Process Flow** -

![](/legacyfs/online/storage/blog_attachments/2023/01/DC-to-Customer-ASR.png)

Process Flow – DC to Customer in S/4 HANA with embedded EWM TM – ASR Integration

This blog will cover the additional configuration steps involved in this scenario, master data and the process till setting the Outbound Delivery Order status in EWM to "Ready for Shipping" and its linkage with Freight Order (FO) in the document flow in TM. Remaining process steps in EWM can be performed as per standard process in EWM.

**Configuration** –

A) Below steps are essential in case you do not want to disturb standard SAP settings -

1. SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Cross-Process Settings->Delivery-Warehouse Request->  Status Management->Define Status Profiles->Execute-> Create new Status Profile for Outbound Delivery Order and Outbound Delivery Item by copying existing profiles # /SCDL/OUT\_PRD\_STANDARD and /SCDL/OUT\_PRD\_DLV\_STANDARD respectively and ensure the settings as shown below -

![](/legacyfs/online/storage/blog_attachments/2023/01/ODO-Status-Profile-DSH-DTD-DTU-1.png)

Outbound Delivery Order Status Profile - DSH, DTD, DTU Status Type

![](/legacyfs/online/storage/blog_attachments/2023/01/ODO-Item-Status-Profile-DTU.png)

Outbound Delivery Order Item Status Profile - DTU Status Type

2. SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Goods Issue Process->Outbound Delivery->Define Document Types for Outbound Delivery Process->Execute-> Create new document type # ZASR by copying from OUTB and assign Status Profile from step 1 as shown below -

![](/legacyfs/online/storage/blog_attachments/2023/01/Outboud-Delivery-Order-Document-Type.png)

Outbound Delivery Order Document Type

 3.SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Goods Issue Process->Outbound Delivery->Define Item Types for Outbound Delivery Process->Execute-> Create new item type # ZASR by copying from ODLV and assign Status Profile from step 1 as shown below -

![](/legacyfs/online/storage/blog_attachments/2023/01/Outboud-Delivery-Order-Item-Type.png)

Outbound Delivery Item Type

Perform below steps # 4,5 and 6 for new document types -

4.SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Goods Issue Process->Outbound Delivery->Define Document Type Determination  for Outbound Delivery Process->Execute-> Create new entry for new document type

5.SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Goods Issue Process->Outbound Delivery->Define Allowed Item Types in Outbound Delivery Process->Execute-> Create new entry for new item type

6.SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Goods Issue Process->Outbound Delivery->Define Item Type Determination for Outbound Delivery Process->Execute-> Create new entry for new item type

B) Below steps are optional in case you do not want to disturb standard SAP settings -

* SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Interfaces->ERP Integration->Delivery Processing->Map Document Types from ERP System to EWM->Execute-> Create new entry (New LE delivery type # ZLF was created by copying from standard delivery type # LF and linked to sales order type) to link ERP delivery type # ZLF with document type # ZASR

* SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Interfaces->ERP Integration->Delivery Processing->Map Item Types from ERP System to EWM->Execute-> Create new entry to link ERP delivery type # ZLF with item type # ZASR

* SPRO->Display IMG->SCM Extended Warehouse Management-> Extended Warehouse Management->Cross-Process Settings->Warehouse Task->Determine Warehouse Process Type->Map new document type # ZASR and item type # ZASR to outbound warehouse process type for ...
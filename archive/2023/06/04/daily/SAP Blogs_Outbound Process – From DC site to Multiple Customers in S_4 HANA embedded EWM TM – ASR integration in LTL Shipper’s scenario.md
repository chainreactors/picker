---
title: Outbound Process – From DC site to Multiple Customers in S/4 HANA embedded EWM TM – ASR integration in LTL Shipper’s scenario
url: https://blogs.sap.com/2023/06/03/outbound-process-from-dc-site-to-multiple-customers-in-s-4-hana-embedded-ewm-tm-asr-integration-in-ltl-shippers-scenario/
source: SAP Blogs
date: 2023-06-04
fetch_date: 2025-10-04T11:45:44.823076
---

# Outbound Process – From DC site to Multiple Customers in S/4 HANA embedded EWM TM – ASR integration in LTL Shipper’s scenario

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Outbound Process – From DC site to Multiple Custom...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4964&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Outbound Process – From DC site to Multiple Customers in S/4 HANA embedded EWM TM – ASR integration in LTL Shipper's scenario](/t5/supply-chain-management-blog-posts-by-members/outbound-process-from-dc-site-to-multiple-customers-in-s-4-hana-embedded/ba-p/13568298)

![PrashantSoman](https://avatars.profile.sap.com/b/f/idbfce280717bc36e64d1eeb621bb3e92f36fd3f1627dddfb83ff25c44752f9817_small.jpeg "PrashantSoman")

[PrashantSoman](https://community.sap.com/t5/user/viewprofilepage/user-id/45412)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4964)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4964)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568298)

‎2023 Jun 03
11:15 AM

[16
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4964/tab/all-users "Click here to see who gave kudos to this post.")

8,926

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

Many industries do not have full truck load (FTL) every time in their outbound supply chain process when they distribute their finished products to their dealers or sell to their end customers. In such cases, most of their business of customer order fulfillment is achieved using "less Than Truck" (LTL) or parcel scenario. Although the process in this blog covers LTL scenario, the same concept can be used in parcel scenario as well.

This blog will be the continuation of my previous blog. In case you have not read my previous blog, you may refer the same from below link -

[Outbound Process – From DC site to Customer in S/4 HANA embedded EWM TM – Advanced Shipping & Receiv...](https://blogs.sap.com/2023/01/17/outbound-process-from-dc-site-to-customer-in-s-4-hana-embedded-ewm-tm-advanced-shipping-receiving-asr-integration-shippers-scenario/)

Here is scenario -

The shipper , always has the outbound shipment using LTL. As part of manual transport planning, the transportation planner tries to aggregate all the LTL's that have different end customer locations and those will be delivered by the same carrier. The carrier sends one trailer to the warehouse to pick up multiple LTL's scheduled for dispatch on the same day. The transportation planner plans to consolidate all LTL's for a particular day. The charge calculation will be still based on the distance between source and destination location of end customer in each LTL shipment.

(Note - This process is not similar to star-shaped based FU stages wherein each stage tracking is necessary during multi-drop customer milk-run.)

As part of new versions of S/4 HANA 2020 onwards, new object called "Consignment Order" is introduced to meet various shipping demands related to LTL scenarios. The purpose of this blog is to explain the use of new object # Consignment Order in SAP TM. The grouping of FU's to one Consignment order can be done based on same carrier, same incoterm, same loading/unloading point etc.

You can read more about this Consignment Order on the SAP Help

[https://help.sap.com/viewer/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/2020.000/en-US/908e8ab6945a47edb1ade56e...](https://help.sap.com/viewer/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/2020.000/en-US/908e8ab6945a47edb1ade56ec6533b2f.html)

**Process Flow** -

![](/legacyfs/online/storage/blog_attachments/2023/05/DC-to-Multiple-Customers-LTL.png)

Process Flow – DC to Multiple Customers - LTL Scenario

This blog will cover the additional configuration steps involved in this scenario, and the process till PGI of the Outbound Delivery Order in EWM.

**Configuration** –

1. SPRO->Display IMG->Transportation Management -> Freight Order Management -> Consignment Order -> Define Consignment Order Type.  - The new order type can be configured for charge calculation (specific for each customer delivery), separate output type for delivery/ shipping note for each customer, freight settlement against multiple LTL deliveries under one consignment order for a specific customer.

**Documents in S/4 HANA** –

1. Multiple Sales Orders are created for different customers to initiate the outbound process. These orders are relevant for TM.

![](/legacyfs/online/storage/blog_attachments/2023/06/Consignment-order-process-sales-order-1-1.png)

Sales Order 1 - TM relevant

![](/legacyfs/online/storage/blog_attachments/2023/06/Consignment-order-process-sales-order-2-1.png)

Sales Order 2 - TM relevant

2. Multiple Freight Units (FU's) get created automatically.

3. In this scenario, consignment orders are created manually using "Create Consignment Order" App by the transportation planner. The planner groups all the LTL FU's of different customers for which the start date of loading, loading point are same and also the same carrier is predetermined. For each individual customer, one consignment order is created and charge calculation is done.

![](/legacyfs/online/storage/blog_attachments/2023/06/Consignment-order-doc-flow-1.png)

Consignment Order 1

![](/legacyfs/online/storage/blog_attachments/2023/06/Consignment-order-doc-flow-2.png)

Consignment Order 2

4. The consignment orders pertaining to two different customers represent the customer specific LTL and these will be loaded onto the same trailer of the carrier. Consolidation of the consignment orders is done to Freight Order (FO) and this FO represents the carrier's trailer. The consolidation of multiple consignment orders is done with the help of "Consignment Orders Worklist." App. The FO will not be relevant for subcontracting.

5. Single FO gets created to represent the truck trailer. The multiple deliveries are created with reference to FO as part of delivery proposal.

![](/legacyfs/online/storage/blog_attachments/2023/06/FO-with-consignment-orders-document-flow.png)

Freight Order Document Flow

6. The deliveries are also replicated to S/4 HANA and are EWM relevant.

7. All the process steps in EWM will be performed on Outbound Delivery Orders (ODO) in EWM and the ODO is set for ...
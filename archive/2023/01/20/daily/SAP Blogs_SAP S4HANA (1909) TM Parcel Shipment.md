---
title: SAP S4HANA (1909) TM Parcel Shipment
url: https://blogs.sap.com/2023/01/19/sap-s4hana-1909-tm-parcel-shipment/
source: SAP Blogs
date: 2023-01-20
fetch_date: 2025-10-04T04:22:38.458781
---

# SAP S4HANA (1909) TM Parcel Shipment

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* SAP S4HANA (1909) TM Parcel Shipment

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/5011&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S4HANA (1909) TM Parcel Shipment](/t5/supply-chain-management-blog-posts-by-members/sap-s4hana-1909-tm-parcel-shipment/ba-p/13571505)

![former_member835162](https://avatars.profile.sap.com/former_member_small.jpeg "former_member835162")

[former\_member835162](https://community.sap.com/t5/user/viewprofilepage/user-id/835162)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=5011)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/5011)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571505)

‎2023 Jan 19
11:03 PM

[14
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/5011/tab/all-users "Click here to see who gave kudos to this post.")

10,965

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)

View products (2)

**Introduction -**

In this blog post, you will learn how SAP TM enables you to commission a carrier to transport parcels from a shipping point to several consignees. You can create parcel shipments in SAP TM based on deliveries from an ERP system / S4CORE.

Users can then either select a direct shipment option for the parcel shipment or opt for an automatic option based on the DSO Rule configuration within Freight Unit Type configuration and plan and execute the transportation of shipments to the consignees.

The direct shipment option involves selecting a carrier with the relevant transportation services based on carrier service level (For example Express Delivery, Standard Delivery) while considering the applicable charges.

The case that serves as the basis for the detailed scenario is as follows: the sales assistant receives an urgent request for goods and enters a sales order. Immediately after the material’s availability has been checked and the sales order has been saved, an outbound delivery is created. The process in SAP TM follows the standard document flow for planning and settlement

**Solution Approach -**

The following section provides an important configuration step to process the parcel shipment process in SAP TM.

* Create a Freight Unit Types for Parcel Shipment and DSO setting using the below-mentioned node:

In this setting, the user can opt for automatic determination of the DSO option or determine DSO in the Freight unit manually.

The user should also define the DSO strategy and rules which control how the DSO option is determined apart from the above setting.

DSO DEF - > Determine the DSO option along with carrier assignment. In this option selected user needs to run the report /SCMTMS/DIRECT\_SHIPMENT\_BATCH or tcode /SCMTMS/DSO\_BATCH to convert FU to FO or assign to existing FO.

DSO\_RESULT-> after DSO DEF steps are performed system either converts the Freight unit to a Freight order or assigns it to an existing FO if the criteria match for source location, carrier, and pickup Date using the best DSO option available.

– SPRO -> IMG -> Transportation Management -> Planning ->Freight Unit -> Define Freight Unit Type.

![](/legacyfs/online/storage/blog_attachments/2023/01/image010-1.png)

Freight Unit Type Configuration

* Define Freight Order Type using the below-mentioned node:

* SPRO -> IMG -> Transportation Management -> Freight Order Management -> Freight Order -> Define Freight Order Type.

![](/legacyfs/online/storage/blog_attachments/2023/01/image015-1.png)

Freight Order Type

In the above setting important setting is the sequence type of stages which is 08 Star Shaped Based on FU Stages which means it has the same source location and different end customer location. In the case of a parcel manifest, there can be multiple parcels to be delivered to different customers in one freight order.

* Carrier Selection Setting in planning profile:

Choose the direct shipment option in the carrier selection setting. Assign the same setting in the Freight unit type configuration.

Assign TSPS\_DEF planning strategy to choose carrier.

TM Fiori App ->Planning Profile.

![](/legacyfs/online/storage/blog_attachments/2023/01/image018.png)

Carrier Selection Setting-Planning Profile

* Master Data - Carrier Service Level in Business Partner using the below-mentioned node:

SAP Easy Access -> BP

![](/legacyfs/online/storage/blog_attachments/2023/01/image020-1.png)

Carrier Business Partner BP

* Master Date - Define Freight Agreement using the Fiori app ->Edit Freight Agreement.

-Create a new Freight Agreement type for Parcel (CEP1 in this case)

-As per the service level there are three calculation sheets which linked to different transit times. Please refer below screenshot. Hence for each service level, there are different transit times. For example, Service Level D1 -> One-day delivery hence transit time is 24:00

![](/legacyfs/online/storage/blog_attachments/2023/01/image023.png)

Freight Agreement

![](/legacyfs/online/storage/blog_attachments/2023/01/image025.png)

Freight Agreement Item

* Master Data - Define Rate table based on weight and service level using the Fiori app Create Rate table Definition.

As per the below screenshot example, Carrier ZCARDHL charges 100 per kg with service level D1-(A Day delivery).

![](/legacyfs/online/storage/blog_attachments/2023/01/image028.png)

Rate Table based on Weight and Service Level

**Testing -**

* Created Sales Order for Parcel Shipment

Sales Order: 107 - >

The requirement date is 10th Feb 2023 and hence pick up date is 08th Feb ( As per Route determination and shipping condition D2 which is 2 days delivery)

![](/legacyfs/online/storage/blog_attachments/2023/01/image032.png)

Sales Order 107 Created

* Created outbound Delivery 80000170 for Parcel Sales Order

HU was created as per packing instructions. (5 CAR in one Box)

![](/legacyfs/online/storage/blog_attachments/2023/01/image035.gif)

Outbound Delivery Created

![](/legacyfs/online/storage/blog_attachments/2023/01/image036.png)

Handling Unit in Outbound Delivery

* Once Delivery saves below activities are executed in the background automatically.

Freight Unit 4100000100 Created based on FUBR (Freight Unit Building Rule)->Service level copied from DSO option in Freight unit

![](/legacyfs/online/storage/blog_attachments/2023/01/image041.gif)

Freight Unit Created Auto

Since DSO strategy DSO\_RESULT is configured in Freight Unit type configuration, Freight order 6100000652 was created automatically. Carrier already selected in FU as per DSO option.

![](/legacyfs/onli...
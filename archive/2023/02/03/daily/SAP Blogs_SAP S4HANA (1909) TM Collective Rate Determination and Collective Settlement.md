---
title: SAP S4HANA (1909) TM Collective Rate Determination and Collective Settlement
url: https://blogs.sap.com/2023/02/02/sap-s4hana-1909-tm-collective-rate-determination-and-collective-settlement/
source: SAP Blogs
date: 2023-02-03
fetch_date: 2025-10-04T05:34:32.414344
---

# SAP S4HANA (1909) TM Collective Rate Determination and Collective Settlement

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP S4HANA (1909) TM Collective Rate Determination...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67931&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S4HANA (1909) TM Collective Rate Determination and Collective Settlement](/t5/enterprise-resource-planning-blog-posts-by-members/sap-s4hana-1909-tm-collective-rate-determination-and-collective-settlement/ba-p/13560719)

![former_member835162](https://avatars.profile.sap.com/former_member_small.jpeg "former_member835162")

[former\_member835162](https://community.sap.com/t5/user/viewprofilepage/user-id/835162)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67931)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67931)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560719)

‎2023 Feb 02
10:48 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67931/tab/all-users "Click here to see who gave kudos to this post.")

3,530

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)

View products (2)

**Introduction -**

In this blog post, you will learn how the grouping rule can be used in SAP TM to enable users to create collective settlement documents for multiple Freight orders wherein you can choose to sum up the values of the calculation bases with scales of different dimensions (as specified in the grouping rule) in multiple freight orders and determine a rate for the collective value.

The system controls the grouping based on the resolution base.

Using the grouping rule, the rates are fetched for the combined data source value of the charge items, not individual data source values. In this blog, you will understand this well using a sample scenario.

Sample Scenario-

Carrier ZCARINT02 (XYZ Logistics Ltd.) regularly shipped material from plant ZVP1 (Shipping point location SP\_ZVS5) to customer ZCUST\_VIR.

A Truck goes 3-4 times weekly to the same destination. Using collective settlement and collective rate determination, the total freight cost can be saved rather than spending for each shipment and this was agreed upon with the carrier to post freight settlement on a weekly basis and the total weight shipped that week.

Below are the rate table charges agreed upon.

|
 Rate Table Weight Based | | | |

|
 Gross Weight |
 Destination |
 Rate in INR |
 Unit |

|
 >= 100 |
 ZCUST\_VIR |
 20 |
 Per Kg |

|
 >=300 |
 ZCUST\_VIR |
 15 |
 Per Kg |

|
 >=500 |
 ZCUST\_VIR |
 10 |
 Per Kg |

In this example, we will consider two freight orders shipped in a week. The next section will show you in detail how the collective rate gets determined while posting collective FSD.

**Solution Approach -**

The following section provides an important configuration step to process the collective settlement using the grouping rule in SAP TM.

Create a grouping rule for a resolution base

In this sample scenario, we are going to group based on the destination location. That means all freight orders for the same destination for a given carrier, the collective settlement can be posted.

T Code - /SCMTMS/TCM\_RULES

![](/legacyfs/online/storage/blog_attachments/2023/02/image006.png)

/SCMTMS/TCM\_RULES - Grouping Rule

Assign grouping rule in Calculation sheet along with resolution base:

TM Fiori app Edit Calculation Sheet

![](/legacyfs/online/storage/blog_attachments/2023/02/image009.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/image011.png)

Calculation Sheet and Grouping Rule

Create and Maintain Rate Table based on weight and scale as DESTINATION LOCATION

The rates are maintained as per weight and destination location which is part of the grouping rule.

TM Fiori App ->Maintain Rate Table

![](/legacyfs/online/storage/blog_attachments/2023/02/image013.png)

Rate Table based on weight and Destination Loc

**Testing**

* Create two Sales Order for the same destination with different requirement date

Sales Order: 110 and 111 - >

![](/legacyfs/online/storage/blog_attachments/2023/02/image017.png)

Sales Orders for the same destination

* Create outbound Delivery 80000173 and 80000173 for the above sales order

![](/legacyfs/online/storage/blog_attachments/2023/02/image020.png)

Delivery 80000173

![](/legacyfs/online/storage/blog_attachments/2023/02/image021.png)

Delivery 80000174

* Once Delivery saves Freight Units are created in the background automatically.

Freight Units 200000250 and 200000251 were created.

![](/legacyfs/online/storage/blog_attachments/2023/02/image025.png)

* Using TM Optimizer freight units are planned, and Freight orders are created along with carrier selection as per the carrier selection setting in the planning profile.

Charges are updated as per the new rate table mentioned in the freight agreement via the Calculation sheet.

FO1 -610000704 – Charges calculated as per gross weight rata table with rate 20 Per KG = 2700 INR

FO2 -610000705 – Charges calculated as per gross weight rata table with rate 20 Per Kg = 5400 INR

![](/legacyfs/online/storage/blog_attachments/2023/02/image029.gif)

![](/legacyfs/online/storage/blog_attachments/2023/02/image030.png)

Freight Order charge calculation as per Ind Rate

![](/legacyfs/online/storage/blog_attachments/2023/02/image033.gif)

Freight Order charge calculation as per Ind Rate

* Create and Post collective Freight Settlement Document using TM Fiori app > Freight order for settlement worklist.  Choose option Collective from the dropdown. This will consider the total weight of both freight orders and apply the rate table for the total weight.

So the total weight of both freight orders is 405 KG and as per the rate table for gross weight, more than 300 KG is 15 INR per KG. Hence total FSD value is 405 X 15 = 6075 INR

![](/legacyfs/online/storage/blog_attachments/2023/02/image035.gif)

Collective FSD option

![](/legacyfs/online/storage/blog_attachments/2023/02/image037.gif)

FSD posted for collective weight

**Conclusion**

This blog post walks you through various steps involved in collective settlement using grouping rules and rate determination accordingly.

* [Collective FSD](/t5/tag/Collective%20FSD/tg-p/board-id/erp-blog-members)
* [SAP TM Charge calculation](/t5/tag/SAP%20TM%20Charge%20calculation/tg-p/board-id/erp-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F...
---
title: Refurbishment Process – in simple terms
url: https://blogs.sap.com/2023/03/12/refurbishment-process-in-simple-terms/
source: SAP Blogs
date: 2023-03-13
fetch_date: 2025-10-04T09:25:20.024156
---

# Refurbishment Process – in simple terms

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Refurbishment Process – in simple terms

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53341&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Refurbishment Process – in simple terms](/t5/enterprise-resource-planning-blog-posts-by-sap/refurbishment-process-in-simple-terms/ba-p/13570204)

![arvind_aj](https://avatars.profile.sap.com/5/7/id57a8443f7a0bd77df7daec9823dac10bbae2da35b24cbf04158715613ebdd148_small.jpeg "arvind_aj")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[arvind\_aj](https://community.sap.com/t5/user/viewprofilepage/user-id/6386)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53341)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53341)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570204)

‎2023 Mar 12
12:07 PM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53341/tab/all-users "Click here to see who gave kudos to this post.")

22,114

* SAP Managed Tags
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)

* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)

View products (1)

## Introduction: What & why refurbishment?

Repairing of high value faulty spares of an equipment is economic importance for companies and is a core process in Maintenance Processing. Refurbishment is much more cost effective than a new purchase.

There are many ways to implement the refurbishment process depending upon the customer's requirements. I am trying to replicate the simple & standard refurbishment process in this blog.

### **Valuation Types:**

The spare part has different valuation types to represent different values. Because it is also a high
value spare part or critical part, this spare part is serial-number managed.

Serial numbers can be assigned to the procured material. While receiving the material with serial number, equipment will be created automatically in back end for the respective material with serial number. These repairable spare parts can be identified with different cost assignments & valuation types like:

o New (C1)
o Repaired or Refurbished (C2)
o Damaged (C3)

### **Process Initiation:**

## **![](/legacyfs/online/storage/blog_attachments/2023/03/1-9.jpg)**

If the installed equipment malfunctions, it is dismantled from the functional location and a spare
part / equipment is withdrawn and installed at the functional location. The defective equipment is returned as damaged item to the warehouse by marking it as C3 - Valuation type. The stock in the warehouse is automatically updated (Valuation types) with the corresponding cost. This whole process of dismantling & moving the faulty equipment to store is done by creating a maintenance order.

![](/legacyfs/online/storage/blog_attachments/2023/03/2-9.jpg) Components for replacement

Quantity specified is “-1” for the faulty equipment by marking it as “C3” in batch field & the same is dismantled from the functional location & moved to store with reference to order. The other material which is going to replace is marked as “C1” with quantity “1”. This will be assigned to the same functional location.

In this process, make sure to maintain the serial number during the material movement (TA: MIGO) & settlement of this maintenance order is done with cost center as the receiver.

## **Refurbishment Order**

![](/legacyfs/online/storage/blog_attachments/2023/03/3-7.jpg)

Refurbishment Process

In next step, the maintenance planner creates a refurbishment order. These defective repairable spares (Valuation class C3) are withdrawn from the warehouse and repaired. When the refurbishment is finished, the equipment is returned to warehouse as repaired material (Valuation type C2) and the cost is updated accordingly in the material master.

To carry out the refurbishment for a piece of equipment, you need to link the equipment with a material because refurbishment is done for a material & not for an equipment.

In refurbishment order: specify the same from/source material & to/target material. Refurbishment can be done either by internal processing or subcontracting.

![](/legacyfs/online/storage/blog_attachments/2023/03/4-6.jpg)

IW81: Create Refurbishment order

Maintain the component details with serial number. This faulty Material is issued for Refurbishment from stores.

Transaction IW8W “Goods Receipt for Refurbishment Order” is used to get that faulty material back to stores after its repair or refurbish work with valuation type “C2”. Material is moved from Valuation type C3 (Defective) to C2 (Repaired).

![](/legacyfs/online/storage/blog_attachments/2023/03/6-3.jpg)

MMBE Details

Refurbishment orders are settled directly to the material stock. Settlement rule is maintained accordingly in the order with category = “MAT” & receiver is the equipment.

![](/legacyfs/online/storage/blog_attachments/2023/03/5-4.jpg)

Settlement Rule in Maint Order

Moving average price of the material will be updated automatically after the work order settlement which can be viewed in MM03: Accounting1: Material Price Analysis.

### Transactions to know:

IW81: Create Refurbishment order

IQ08: Change equipment's serial number + dismantling faulty equipment from the functional location & assigning new equipment to the same functional location.

IW8W: Perform goods receipt of refurbished material/equipment

MIGO: Goods movement

MMBE: stock overview with the valuation type.

There are many applications like EAM, MM, FICO & others are involved in the entire refurbishment process & many steps are involved in each modules.

SAP supports the end-to-end activities of refurbishment process whether its done internally or sub-contracting.

Labels

* [Expert Insights](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/expert%20insights)

* [refurbishment order](/t5/tag/refurbishment%20order/tg-p/board-id/erp-blog-sap)
* [refurbishment process](/t5/tag/refurbishment%20process/tg-p/board-id/erp-blog-sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Frefurbishment-process-in-simple-terms%2Fba-p%2F13570204%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Con...
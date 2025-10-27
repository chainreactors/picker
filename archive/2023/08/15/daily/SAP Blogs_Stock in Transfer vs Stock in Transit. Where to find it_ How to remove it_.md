---
title: Stock in Transfer vs Stock in Transit. Where to find it? How to remove it?
url: https://blogs.sap.com/2023/08/14/stock-in-transfer-vs-stock-in-transit.-where-to-find-it-how-to-remove-it/
source: SAP Blogs
date: 2023-08-15
fetch_date: 2025-10-04T12:01:43.356605
---

# Stock in Transfer vs Stock in Transit. Where to find it? How to remove it?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Stock in Transfer vs Stock in Transit. Where to fi...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/54546&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Stock in Transfer vs Stock in Transit. Where to find it? How to remove it?](/t5/enterprise-resource-planning-blog-posts-by-sap/stock-in-transfer-vs-stock-in-transit-where-to-find-it-how-to-remove-it/ba-p/13577561)

![afracalossi](https://avatars.profile.sap.com/9/5/id9557354ca207b92e84c1b2adb133fe3600979ea7533bf15c8428bd24e739904b_small.jpeg "afracalossi")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[afracalossi](https://community.sap.com/t5/user/viewprofilepage/user-id/155649)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=54546)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/54546)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13577561)

‎2023 Aug 15
12:27 AM

[20
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/54546/tab/all-users "Click here to see who gave kudos to this post.")

60,114

* SAP Managed Tags
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)
* [MM Inventory Management](https://community.sap.com/t5/c-khhcw49343/MM%2520Inventory%2520Management/pd-p/402489426158095572469338199787586)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [MM Inventory Management

  Software Product Function](/t5/c-khhcw49343/MM%2BInventory%2BManagement/pd-p/402489426158095572469338199787586)

View products (4)

The purpose of this blog post is to explain the difference between Stock in Transfer and Stock in Transit demonstrating where we can check the stock (table/tcode), and how to remove the stock if necessary.

### What is the difference between Stock in Transfer and Stock in Transit?

**- The Stock in Transfer** > stock is moved (plant-to-plant) or (storage location-to-storage location) without a Stock Transport Order.
**- The Stock in Transit** > stock is moved between different plants of the same/different company code via STO.

### Where we can check the stock (table)?

- The stock in transfer at storage location level is stored in MARD-UMLME.
- The stock in transfer at plant level is stored in MARC-UMLMC.
- The stock in transit is stored at MARC-TRAME. However, there is an exception:
> *\*\*\* In Cross-Company Stock Transport Orders there is no "real" stock in transit: we do not have stock in transit updated in any table(MARC-TRAME is only updated in the case of Intra-Company Stock Transport Orders. In the Cross-Company scenario, the stock in transit is "virtual": it is dynamically calculated by the program via the purchase order history, as the difference between the goods receipt and the goods issue quantity).*

### Where we can check the stock (tcode)?

> Stock in Transfer can be checked in transactions MB52 and MMBE:

MMBE:![](/legacyfs/online/storage/blog_attachments/2023/08/mmbe.jpg)

MARD-UMLME is under column 'Transfer (SLoc)' and MARC-UMLMC is under column 'Stck trans.(plant).

MB52:![](/legacyfs/online/storage/blog_attachments/2023/08/mb52-1.jpg)

> Stock in Transit can be checked in transactions MB52(previous image column 'Stock in Transit') and MB5T below:![](/legacyfs/online/storage/blog_attachments/2023/08/mb5t.jpg)

At MB5T it is possible to check the Material, Purchase Doc., Supplying plant (SPlt), Supplying Storage Location (StLoc), Receiving Plant (Plnt), Receiving Storage Location (SLoc), and the quantity that is currently in transit (Quantity).

The transit stock displayed by transaction MB5T is calculated based on the PO history and this does not always match the actual transit stock of the material (MARC-TRAME). This is because cross-company STO does not update the MARC-TRAME field.

### How to clear the stock in transfer at storage location level (MARD-UMLME)?

The stock in transfer at storage location level is created (increased) in the receiving storage location with the movement type 313. It is decreased with the corresponding movement 315.

To remove the stock from MARD-UMLME MIGO can be used. It will be needed to perform a goods movement to receive the stock in transfer into the receiving storage location.

Steps:
MIGO - Place In Storage - Other - Movement Type 315.
Enter material / receiving plant / receiving storage location / batch (if relevant).
Enter the relevant quantity to receive from stock in transfer.
Post
The stock in transfer at storage location level (MARD-UMLME) is transferred to unrestricted use.

After this, if this material does not exist physically anymore, you need to remove it from the unrestricted stock (MARD-LABST):

Steps:
1 - create a physical inventory document in MI01
2 - enter count in MI04
3 - post physical inventory document in MI07

Or it is also possible to scrap this material in MIGO with movement type 551. If you would not like to allocate this cost to any cost center, please set KOSTL field as optional entry in OMJJ transaction before going to MIGO transaction.

### How to clear the stock in transfer at plant level (MARC-UMLMC)?

The stock in transfer (MARC-UMLMC) contains quantity transferred via Inventory management (movements 303/305 and 603/605, and their corresponding reversal movements) and not via stock transport orders.

To remove the stock from MARC-UMLMC you can perform a reversal mvt 305/605 or you would have to move the stock to a storage location and scrap the stock from the storage location (if this material does not exist physically anymore), as follows:

Step 1: Move the stock from MARC-UMLMC to MARD-LABST by a 305/605 mvt, the storage location can be any in the same plant as this stock will be removed in the next step.
Step 2: Remove the stock from MARD-LABST with a goods issue movement type, e.g. 562 mvt, 551 mvt, or via a physical inventory process (701 mvt).

It is also important to mention that the system does not build any real link between these two postings(103/305 and 313/3015).
You can check more information about this on: KBA [1800451](https://launchpad.support.sap.com/#/notes/1800451) - No link between the documents of a two step stock transfer (with movement types 303/313 and 305/315).

### How to clear the stock in transit (MARC-TRAME)?

The stock in transit is increased in the receiving plant with the movement types 351 and 641 (if shipping is involved), and it is decreased when the goods...
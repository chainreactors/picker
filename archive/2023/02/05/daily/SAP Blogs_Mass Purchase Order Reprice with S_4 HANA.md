---
title: Mass Purchase Order Reprice with S/4 HANA
url: https://blogs.sap.com/2023/02/04/mass-purchase-order-reprice-with-s-4-hana/
source: SAP Blogs
date: 2023-02-05
fetch_date: 2025-10-04T05:45:30.274317
---

# Mass Purchase Order Reprice with S/4 HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Mass Purchase Order Reprice with S/4 HANA

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67995&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Mass Purchase Order Reprice with S/4 HANA](/t5/enterprise-resource-planning-blog-posts-by-members/mass-purchase-order-reprice-with-s-4-hana/ba-p/13562214)

![RaviDave](https://avatars.profile.sap.com/8/5/id851dec481f1fa5b14f10605fa0ca3d2057d6978e9bd2347131f54bde516f4ff8_small.jpeg "RaviDave")

[RaviDave](https://community.sap.com/t5/user/viewprofilepage/user-id/121795)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67995)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67995)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562214)

‎2023 Feb 04
4:52 AM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67995/tab/all-users "Click here to see who gave kudos to this post.")

11,346

* SAP Managed Tags
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)

* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)

View products (1)

**Introduction:** In this blog, I will try to demonstrate the functionality of mass purchase order reprice in SAP S/4 HANA.

The pandemic lead to a massive shutdown followed by a slowdown and cause supply chain disruption. Disruption in the supply chain, raising fuel and freight costs often leads to frequent price changes from the vendors (especially oversees long lead time items). As a buyer, it's important to catch up with frequent and fast changes to make sure the landed cost of the product is correct and 3-way match happens as accurately as possible. This blog will help on how to achieve the solution.

**Prerequisites:**

* Price update from the vendor will be updated on Purchasing Info Record as a new valid condition record.

**Standard SAP options:**

Below is the standard SAP option that was explored:

* Standard SAP has t-code: MEI1 which allows updating PO based on condition changes, but standard SAP looks at the PO creation date and condition validity period date and updates the price.

* It was also found that once we process records using MEI1, it is deleting the Table: WIND entries for that vendor of all the items. That means as a buyer, if you want to work on certain items on the PO the next day, you lost visibility of price updates.

Both of the above challenges force me to think of a custom solution.

**Solution Approach/Design:**

* Create a Fiori tile as per the below layout

![](/legacyfs/online/storage/blog_attachments/2023/02/Layout.png)

Selection Layout

* + No of Day in the Past\*: Mandatory; This is for performance. From day of execution, how many days back do we want to go for the document date; by default 180 days.

  + Purchasing Group\*: Mandatory; Multiple selection drop-down; Validation: T024- T024; E: Purchasing Group Required or E: Invalid Purchasing Group.

  + Purchasing Document Type: Optional; Multiple selection drop-down; Validation: T161- BSART; E: Invalid Document type.

  + Supplier: Optional; Multiple selection drop-down; Validation: LFA1- LIFNR; E: Invalid Supplier.

  + Supplier Subrange: Optional; Multiple selection drop-down; Validation: WYT1- LTSNR; E: Invalid Supplier Subrange.

  + Plant#: Optional; Multiple selection drop-down; Validation: T001W-WERKS; E: Invalid Plant.

  + Material Group#: Optional; Multiple selection drop-down; Validation: T023-MATKL; E: Invalid material group.

  + Material#: Optional; Multiple selection drop-down; Validation: MARC-MATNR; E: Invalid material.

  + Next Period Price/Currency: Optional;

  + Price Over-Ride: Optional

  + Future Cost Match: Optional; drop-down; values are Yes Or No

* Fiori tile validates the data keyed in by the user and captures the appropriate error message in case of errors as stated above.

* After validating input screen data, once the user clicks on go, the program does the following:

* + Based on the input, fetch the only open PO(s) undelete and without Free of Charge. Open PO(s) can be found where EKPO-ELIKZ not equal to X and undeleted PO(s) can be found where EKPO-LOEKZ is not equal to L and EKPO- REPOS = X (Excluding Free PO(s) as well).

  + Only fetch the PO(s) where item category EKPO-PSTYP not equal to 2 – Consignment and 7 – Stock Transfer (Basically, we don’t want consignment and stock transfer PO(s) as it doesn’t have net price).

* Below are the fields and logic:

|
 **Field(s)** |
 **Logic** |

|
  |
  |

|
 Purchase Order |
 From EKPO-EBELN |

|
 Vendor |
 From EKKO-LIFNR |

|
 Vendor Name |
 Pass Vendor from EKKO to LFA1 and get LFA1-NAME1 |

|
 Supplier Subrange |
 From EKPO-LTSNR |

|
 Supplier Subrange Description |
 Pass Vendor and Subrange to WYT1 and get WYT1-LTSBZ |

|
 Purchasing Group |
 From EKKO-EKGRP |

|
 Purchasing Group Name |
 Pass the purchasing group code to T024 and get T024 – EKNAM. |

|
 Document Type |
 From EKKO-BSART |

|
 Item No |
 EKPO-EBELP |

|
 Item Category |
 EKPO-PSTYP |

|
 Material |
 EKPO-MATNR |

|
 Material Group |
 EKPO-MATKL |

|
 Material Group Description |
 Pass material group to T023 and get T023- WGBEZ |

|
 Plant |
 EKPO-WERKS |

|
 Material Description |
 MARA-MAKTX |

|
 PO Creation Date |
 EKKO-AEDAT |

|
 PO Quantity |
 EKPO-MENGE |

|
 Ordering Unit |
 EKPO-MEINS |

|
 Conf. Control |
 EKPO-BSTAE |

|
 Inbound Delivery |
 Pass PO number, item number, Confirm. Cat.: LA to EKES and get the inbound delivery number. If multiple found, then sort in descending order and get the latest one. |

|
 PO History |
 Pass PO and item to EKBE and see entries found. If entry is there, then show the graph. Note: T-code: ME2N is prime example on how to show the graph. If developer can find, then we should leverage that. |

|
 PO Item Delivery Date |
 Pass PO and item number to EKET and get EKET-EINDT |

|
 Price Overwrite |
 Pass PO to Table: EKKO and get the Doc. Condition No. (EKKO- KNUMV). Pass Condition No. To table: PRCD\_ELEMENTS with PO item number and Inactive condition (KINAK) as blank and see if we have PBXX. If yes then show PBXX else blank |

|
 PO Net Price/Currency |
 EKPO-NETPR/EKKO-WAERS (for example $2800/USD) |

|
 PO Price Unit/Ordering Price Unit |
 EKPO-PEINH/EKPO-BPRME (for example 100/EA) |

|
 Current Period Validity Date (From - to) |
 Note: Within PB00 pricing team is loading price in tables: A017 and A018. If the A017 record then gets trigger else it will go to A018.    \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*    Logic: (Developer can explore functional module. I have tried using ME\_GET\_INFORECORD\_CONDITIONS which works fine for PB00 and PB01)    Pass Application - KAPPL = M, Condition Type - KSCHL = PB00, Vendor - LIFNR, Material - MATNR, Purchasing Org...
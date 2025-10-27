---
title: Sales kits in S/4 Hana Cloud Order to Cash process ( ERLA, LUMF, CPFH, DISH ) – Scope item 31Q
url: https://blogs.sap.com/2023/01/02/sales-kits-in-s-4-hana-cloud-order-to-cash-process-erla-lumf-cpfh-dish-scope-item-31q/
source: SAP Blogs
date: 2023-01-03
fetch_date: 2025-10-04T02:55:00.860035
---

# Sales kits in S/4 Hana Cloud Order to Cash process ( ERLA, LUMF, CPFH, DISH ) – Scope item 31Q

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Bill of Material Variants in SAP S/4HANA Cloud for...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51828&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Bill of Material Variants in SAP S/4HANA Cloud for Sales – Scope Item 31Q ( ERLA, LUMF, CPFH, DISH )](/t5/enterprise-resource-planning-blog-posts-by-sap/bill-of-material-variants-in-sap-s-4hana-cloud-for-sales-scope-item-31q/ba-p/13560201)

![Ralf_Kammerer](https://avatars.profile.sap.com/0/f/id0fc65dd9b57b299b64ca4c511c6df61c6c68cea9dbb1cd17c74f365fd4d9fec0_small.jpeg "Ralf_Kammerer")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[Ralf\_Kammerer](https://community.sap.com/t5/user/viewprofilepage/user-id/131480)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51828)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51828)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560201)

‎2023 Jan 02
9:25 AM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51828/tab/all-users "Click here to see who gave kudos to this post.")

11,060

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (1)

### Purpose of this BLOG:

Provide a comprehensive overview on the different feature and functions of pre delivered Bills of material in **SAP S/4HANA Cloud**  including links to more detailed docu materials.

####

# 1. Bill of materials variants

In **SAP S/4HANA Cloud** we provide content for 4 Bill of material variants which can be used out of the box when scope item 31Q is activated.

## 1.1 Overview

### Variant ERLA

#### Pricing and logistics execution on main item level of the Bill of material.

### Variant LUMF

#### Pricing and logistics execution on sub item level of the Bill of material

####

### Variant CPFH

#### Pricing on main item and logistics execution on sub item level of the Bill of material.

### Variant DISH

#### Logistics execution on main item and pricing on sub item level of the Bill of material.

##

The following slides show the differences and capabilities of the different variants:

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview01.jpg)

At SAP the term Bill of material is commonly used.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview02.jpg)

Typically the item category group as defined in the material master does determine the variant of the Bill of material and therefore the characteristics of the main item and the subitems.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview03.jpg)

Below you find examples for the 4 different variants

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview-last-versionc1.jpg)

In this example you sell a bike. The bike is in stock and has a defined price. The subitems of the Bill of material are only used as 'Information' in order to specify the components of the bike in detail.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview05-1.jpg)

In this example you sell a tool set. The individual tools in the set are priced individually and stock relevant. The main item does only serve as a 'bracket' to sell the single individual items together.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview06-1.jpg)

In this example you sell a Computer. The single items are in stock, but sold together for 1 defined price which is maintained for the main item of the Bill of material.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview07-1.jpg)

In this example you sell a dental display. Here the separate items on the display have their individual prices. The display itself is the material in stock.

ERLA & LUMF are straight forward use cases where the dimensions Cost, Price, Profitability relevance is either on the main OR on the subitem. This means in the:

* ERLA case the main item does behave like a regular TAN (sell from stock item) with regards to Cost, Price & Profitability relevance. The subitems have only informative character.

* LUMF case the subitem does behave like a regular TAN (sell from stock item) with regards to Cost, Price & Profitability relevance. The main item does serve only as a bracket.

CPFH & DISH were introduced in release 2105 (CPFH) and 2208 (DISH). In the following sections these variants will be explained more in detail.

## 1.2. CPFH - Pricing on main item and logistics execution on sub item level of the sales kit.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview-last-version-c1.jpg)

In CPFH the pricing is done on main item level. However- as the inventory management in this variant is done on subitem level, there is no cost condition record determined on the main item.

The cost condition record is determined on sub item level.

As we have now cost and revenue not within the same item- but split across multiple items- from a profitability point of view ( profit margin) we have to bring the cost and revenue back together on one common level. As the profitability analysis is done in Financials based on the profitability segment of a single item- for CPFH the profitability segments of the subitems are derived from the main item and therefore all items are accounted on the main item of the Bill of material. This means from a profitability point of view cost and revenues are consolidated on the main item of the Bill of material.

please see the example below.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview09.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview10.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview11.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview12.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview13.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/Sales-Kits-CPFH-DISH-overview14.jpg)

**Limitations for variant CPFH:**

* Scenarios with 3rd party items, bought in items and service materials are not supported.

* Customer Consignment processes is not enabled for the CPFH scenario.

* Subitems must have the same delivering plant as main item.

* Intercompany feature of process is not supported at the moment, as the intercompany pricing is not fully supported by CPFH variant.

* Milestone based sales billing is not supported in the ‘Sales Order Management’ Fiori app. (planned 2308)

* When creating a sales order, the item category field in main Bill of m...
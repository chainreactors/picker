---
title: SAP S/4HANA Demand and Supply Segmentation – A practical guide for Solution Architects
url: https://blogs.sap.com/2022/12/30/sap-s-4hana-demand-and-supply-segmentation-a-practical-guide-for-solution-architects/
source: SAP Blogs
date: 2022-12-31
fetch_date: 2025-10-04T02:47:37.445509
---

# SAP S/4HANA Demand and Supply Segmentation – A practical guide for Solution Architects

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Demand and Supply Segmentation - A pra...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51452&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Demand and Supply Segmentation - A practical guide for Solution Architects](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-demand-and-supply-segmentation-a-practical-guide-for-solution/ba-p/13557622)

![maiko_rahman](https://avatars.profile.sap.com/0/0/id00a9aa9aeca10fd4e0662a134dfa2c8fa13f326ba9a1e0368173eff5960f52fb_small.jpeg "maiko_rahman")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[maiko\_rahman](https://community.sap.com/t5/user/viewprofilepage/user-id/268283)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51452)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51452)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557622)

‎2022 Dec 30
12:49 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51452/tab/all-users "Click here to see who gave kudos to this post.")

8,655

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

Since Demand and Supply Segmentation (LO-SGT) was made available for every industry within SAP S/4HANA OP, I have experienced an increasing demand from customers of discrete industries and process industries to evaluate and assess the business value as well as the impact on business processes, solution design and change management.

The functionality is already widely used by our customers using the industry solutions for Retail or Fashion. For other industries, however, I have experienced a need for an extended approach to acquaint customers with the concept of Segmentation.

This guide intents to provide a practical guide for solution architects to introduce customers to the functionality of SAP S/4HANA Demand and Supply Segmentation during a sales cycle, solution discovery or high-level solution design.

**Demand and Supply Segmentation**

Quick recap, Segmentation offers a unique value proposition embedded into master data maintenance and E2E business processes along the logistical and financial value chain (please refer to other blog posts for a detailed description of the functional scope). It became standard functionality in S/4HANA OP for all industries and further functional enhancements have been released with SAP S/4HANA 2021 (PPPI) and 2022 (EWM, ePPDS and QM).

The functionality helps to:

* Manage the supply chain and product costing/material valuation by product attributes rather than separate master data (material codes, BOMs, master recipes, info records, prices, etc.)

* Reduce significantly the number of master data objects by associating attributes rather than creation additional master data. Those attributes in turn, are fully reflected and embedded in the application to control the execution of business processes.

* Improve business agility by enhanced inventory transparency to fulfil sales orders by product substitutions with common characteristic (country of origin, quality, sales channel, market approval, etc.)

* Establish E2E processes to streamline regulatory compliance of supply chain planning and execution, from raw material purchase through issue of delivery documents

* Automate regulatory checks before batch release or fulfilling sales orders, thus reducing errors and preventing stockouts

* Reduce the cost of managing master data in S/4HANA compared to SAP ECC

**The extended approach**

Embracing the concept of Segmentation requires a mind-shift from customers. In the absence of Segmentation, they have often experienced the proliferation of material codes and other master data objects (like routings/master recipe, BOM, inspection plan, etc.) to account for differentiating characteristics of the supply chain/logistics or in product costing/material valuation. Some customers even have very sophisticated decision trees when to create a new material code for e.g. a country version, packaging variant or country of origin.

Based on my experience, this mind-shift takes some time and extra effort to let the huge potential of Segmentation really resonate at our customers. The following approach has its basis on lessons learned from several workshops conducted with customers from manufacturing industries, life sciences and crop sciences.

It’s divided into the following 5 steps:

* Introduction

* Deep-dive supply chain/logistics

* Deep-dive product costing/material valuation

* Customer use-case (if required)

* Conclusion

*Step 1: Introduction*

Typically, customers had already a first touchpoint with Segmentation but cannot fully contextualize it. Therefore, I let them present the actual business requirements resp. uses cases. Followed by the problem statement that arose out of it with regards to master data proliferation, supply chain and product costing issues.

As a second part of the introduction, I present a general example that explains how Segmentation works. Typically, I use a generalized product (cordless drill-driver) for customers from discrete industries and a fictitious pharmaceutical product (liquid drug) for process industry customers (see figures below).

![](/legacyfs/online/storage/blog_attachments/2022/12/Cordless-drill-driver-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Liquid-Drug-1.png)

Demo Scenarios for Discrete Industry and Process Industry

I kick it off with presenting the very basic configuration steps with regards to Segmentation Characteristics, Segmentation Structure and Segmentation Strategy based on a supply chain E2E process including program planning, MRP, purchasing, production execution, goods receipt, inventory overview and quality management which I present on slides only w/o any system demo.

In the third part, I touch upon additional topics. Very common questions are with regards to E2E processes which include other SAP solutions or non-SAP applications. I also mention relevant SAP notes, links to the SAP Help Portal and the SAP API Hub. Important to mention is also that the Segmentation settings can be maintained through standard backend transactions but also Fiori Apps.

I recommend to plan for 2h for the initial workshop and would reserve sufficient time for discussion and Q&A.

*Step 2: Deep-dive Supply Chain*

The deep-dive sessions are meant for system demo. I walk the customer through a scenario that I have set-up in a demo system. It includes in detail the configuration steps, master data setup and E2E processes in program planning, MRP, Manufacturing, QM, sales, Purchasing and materials management.

Focus should be on the understanding of the basic concept of Segmentation. In order not to overwhelm the participan...
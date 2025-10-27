---
title: SAP S/4HANA aATP Supply creation-Based Confirmation (SBC) Series Part 4 – Complex Use Case
url: https://blogs.sap.com/2023/06/16/sap-s-4hana-aatp-supply-creation-based-confirmation-sbc-series-part-4-complex-use-case/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:47:05.949868
---

# SAP S/4HANA aATP Supply creation-Based Confirmation (SBC) Series Part 4 – Complex Use Case

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA aATP Supply creation-Based Confirmatio...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52723&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA aATP Supply creation-Based Confirmation (SBC) Series Part 4 - Complex Use Case](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-aatp-supply-creation-based-confirmation-sbc-series-part-4/ba-p/13565415)

![Andras_Kovacs1](https://avatars.profile.sap.com/9/c/id9c144816305fb5011f430cccbcbc434a7503a337592e301bd7ab4dccb5431f24_small.jpeg "Andras_Kovacs1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Andras\_Kovacs1](https://community.sap.com/t5/user/viewprofilepage/user-id/342693)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52723)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52723)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565415)

‎2023 Jun 16
2:24 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52723/tab/all-users "Click here to see who gave kudos to this post.")

4,983

* SAP Managed Tags
* [SAP Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Supply%2520Chain%2520Management/pd-p/01200615320800000492)
* [SAP S/4HANA for advanced ATP](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520for%2520advanced%2520ATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)
* [SAP S/4HANA Cloud Private Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Private%2520Edition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

* [SAP Supply Chain Management

  SAP Supply Chain Management](/t5/c-khhcw49343/SAP%2BSupply%2BChain%2BManagement/pd-p/01200615320800000492)
* [SAP S/4HANA for advanced ATP

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bfor%2Badvanced%2BATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)
* [SAP S/4HANA Cloud Private Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPrivate%2BEdition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

View products (3)

# Intro

In this series I am talking about S/4HANA aATP Supply creation-Based Confirmation (SBC). We are now at the last part 4, to discuss a complex SBC use case and create an example for it in the system:

* [Part 1 - SBC Functional Overview](https://blogs.sap.com/?p=1733215)

* [Part 2 - SBC Setup Guide](https://blogs.sap.com/?p=1733193)

* [Part 3 - SBC Simple Use case](https://blogs.sap.com/2023/04/19/sap-s-4hana-aatp-supply-creation-based-confirmation-sbc-series-part-3-simple-use-case/)

* **(current one) [Part 4 - SBC Complex Use Case](https://blogs.sap.com/?p=1733288)**

If you are reading this and made up to this point, congratulations! You are doing a really great job by testing the scenarios and/or reading so far. You have now a basic knowledge about SBC in aATP and PP/DS understanding how the integration between the two components work.

We are coming now to the advanced part of SBC. Today we discuss the details about how planning with characteristics work, how to setup block planning, how they can help you reaching your goal modeling a business process of your needs. We will also include Sales and Capacity Product Allocations into the example, which helps you model constraints for both sales and capacity restrictions.

## PPAC with Supply Creation, Characteristics, Block Planning and Product Allocation - Color coated coil production

We have a customer, who is producing hot rolled coils with color coating. The customer has multiple challenges modeling this business process, where they need to focus on the most important ones relevant for the best outcome, in my example I identified the following factors:

1. Some important characteristics of the product (defined by the ordering customer in the sales order) have a high influence on the production process:

   * width of the coil: the ordering customer accepts a range of width (eg.: 1500-2000mm)

   * color of the coating, which defines the block planning blocks, how production is executed

2. Ordering customers need to be restricted, preventing that few customers are utilizing the full production capacity of the company

3. Transport capacities are bottlenecks, delivery need to be splitted accordingly into weekly buckets.

The requirements can be modelled like depicted in the picture below, taking the example that a customer would like to order 500kg of yellow coated steel coil with a width range of 1500-2000mm:

![](/legacyfs/online/storage/blog_attachments/2023/05/Blog4_complex_usecase_sketch.png)

Complex use case: color coated coil production

To achieve this scenario, we will use the following functions in ATP:

* **Sales PAL:** Sales Product Allocation for sales restrictions

* **PPAC:** Production Planning-Based Availability Check with characteristics to check for stock with characteristic ranges

* **Supply Creation** based on characteristics, to create new supply in case there is not enough on stock, with the correct configuration and taking into account block planning **blocks**

* **Capacity PAL:** Capacity Product Allocation for transport capacity restrictions

The Bill of Material (BOM) is the following, with some important settings highlighted:

![](/legacyfs/online/storage/blog_attachments/2023/06/Blog4_BOM.png)

Color coated coil production: Bill of Material

We are using the following settings in this use case:

* Scenario: **Make-to-Stock with fixed pegging** - because there can be some stock left, which should be reused

* Checking group: **DS** - which means we are using PPAC (aka net requirements calculation) with Supply Creation

* Our finished product is **Color coated steel coil - AKD21FERT,** multilevel with a BOM and finite time-continuous capacities (later as well with block planning)

* Semi-finished products:

  + **Steel coil - AKD21SEMI11** the system plans immediately to cover demands, finite, based on time-continuous capacities

  + **Coating - AKD21SEMI12** the system plans immediately to cover demands, finite, based on time-continuous capacities

* Raw materials:

  + **Slab - AKD21RAW111** planned in planning run (only dependent requirements are created)

  + **Paint - AKD21RAW121** planned in planning run (only dependent requirements are created)

* **Characteristics-Dependent Planning: yes**

* **Block planning: yes** (first testing without it, later enabling it)

* **Product Allocation: yes**, both Sales and Capacity allocations

## Post goods receipt (stock)

As in real life, there can be some available stock laying around in the storage location or plant, that can be used for incoming sales orders. To model this, let's book in some stock with batch characteristics for the finished product with "MIGO". Open the Goods receipt App, select "Goods receipt", "Other", fill out Material, quantity, plant, storage location and then hit on the Classification button on the...
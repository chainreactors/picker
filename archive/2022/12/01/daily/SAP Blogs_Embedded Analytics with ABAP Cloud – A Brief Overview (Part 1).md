---
title: Embedded Analytics with ABAP Cloud – A Brief Overview (Part 1)
url: https://blogs.sap.com/2022/11/30/embedded-analytics-with-abap-cloud-a-brief-overview-part-1/
source: SAP Blogs
date: 2022-12-01
fetch_date: 2025-10-04T00:11:03.160373
---

# Embedded Analytics with ABAP Cloud – A Brief Overview (Part 1)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Embedded Analytics with ABAP Cloud - A Brief Overv...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52025&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Embedded Analytics with ABAP Cloud - A Brief Overview (Part 1)](/t5/enterprise-resource-planning-blog-posts-by-sap/embedded-analytics-with-abap-cloud-a-brief-overview-part-1/ba-p/13561831)

![fabianfellhauer](https://avatars.profile.sap.com/9/2/id92f214c2bba0b6e0aa689bfc9b8375fe556ac7ca1641ab4317680107ab2d68b2_small.jpeg "fabianfellhauer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[fabianfellhauer](https://community.sap.com/t5/user/viewprofilepage/user-id/354017)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52025)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52025)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561831)

‎2022 Nov 30
10:36 PM

[26
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52025/tab/all-users "Click here to see who gave kudos to this post.")

6,797

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA Embedded Analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Embedded%2520Analytics/pd-p/8492b555-b489-4972-8e37-83f2f27ae399)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP S/4HANA Embedded Analytics

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BEmbedded%2BAnalytics/pd-p/8492b555-b489-4972-8e37-83f2f27ae399)

View products (3)

Cheers ABAP Folks!

Have you ever asked yourself what Embedded Analytics is all about and how your company can benefit from it? In this blog post I, want to give you an insight into Embedded Analytics done with the lately announced ABAP Cloud.

## **Conceptual Basics**

Alright, first I need to admit: Yes - there are numerous different possibilities to do analytical reporting for data stored in ABAP-based systems. And yes, each of them has its benefits. For example, for a distributed system landscape it makes sense to have a dedicated solution, like SAP BW/4HANA or SAP Data Warehouse Cloud, which brings all the scattered data of your different systems together. However, some just want to have an analytical reporting for their data stored in their central core system. And here Embedded Analytics comes into the game.

Embedded Analytics is an easy-to-use reporting strategy, which allows to aggregate and display data of your core ABAP solution – without any cross-system overhead. And do you know what’s the best about it? It’s already included in the most common ABAP-Cloud-based solutions like Steampunk or SAP S/4HANA powered Embedded Steampunk. All those solutions have the required analytical engine, modeling tools and, depending on the concrete application, a publicly released Core Data Service (CDS) model shipped – ready to be exploited by you!

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_1.png)

## **It’s all about ABAP Core Data Services**

With ABAP Cloud based Embedded Analytics, the foundation of all analytical reporting is the data model defined by Core Data Services (CDS). Most data models of applications built in the ABAP universe are separated in different layers. On the very bottom, there are the classical ABAP Dictionary database tables, which store all the data, and which are kept private in ABAP Cloud. On top of that there's a CDS-based reuse layer, which allows publicly released read-only access to those database tables. And on top of that, there are scenario-specific applications that make use of those data models. Either transactional RAP applications, which allow data maintenance, or analytical applications, which allows reporting of the underlying data.

Ok – but what’s the big deal about using the same data model for all kinds of applications? What sounds trivial to the most of you, wasn't usual in the past. Transactional and analytical applications often didn't share the same data persistence, leading to mandatory data replications even for embedded scenarios. Today, with the column storage technology of SAP HANA and the Core Data Services in the ABAP Server, the same underlying data structures can be used, without any performance penalties for analytical applications.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_2.png)

It’s even getting better: You as an ABAP developer are empowered to either build your own CDS-based application from scratch or to build your own analytical reporting on top of released CDS models by SAP or partners. And that’s all without the need to subscribe to any further stand-alone solutions outside the ABAP system.

## **Great – I’m in, but how to get started?**

First, we need to understand how an analytical application is built with CDS. Let’s imagine we've a simple shop application that manages sales orders of various products. A sales order of this application has an amount (called measure in analytical contexts) as well as some further attributes like a concrete customer, an order date or a concrete related product (called dimensions in analytical contexts), which can have further related attributes.

Those different attribute classifications are important, because measures are numeric fields, which we're interested in, as soon as they're aggregated. For a CEO, it would be the summed-up turnover at the end of a year. However, dimensions are fields that allow us to fine-tune our reporting by defining the attributes relevant for aggregation. With that, we can split up the turnover based on the customer's location, based on the year or even based on the products sold. There might also be scenarios in which we want to combine those dimensions, because the CEO exactly wants to know how many MyPad 7 were sold back in 2020 in Seattle.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_3.png)

But that’s by far not all. Due to the data model defined with ABAP Core Data Services, it's even possible to define different aggregation levels, which can be accessed via so called drill-down / rollup actions. This means hierarchical data models (some of them are already available within each ABAP platform) can be used to roll up from a city to a region to a country. By that the concrete reporting can't only be defined for Seattle, but also for all orders created in Canada.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4.png)

The same is of course possible vice versa for other dimensions, like a concrete order date.

![](/leg...
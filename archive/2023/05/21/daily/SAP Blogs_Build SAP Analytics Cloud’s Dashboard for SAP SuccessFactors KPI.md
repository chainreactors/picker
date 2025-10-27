---
title: Build SAP Analytics Cloud’s Dashboard for SAP SuccessFactors KPI
url: https://blogs.sap.com/2023/05/20/build-sap-analytics-clouds-dashboard-for-sap-successfactors-kpi/
source: SAP Blogs
date: 2023-05-21
fetch_date: 2025-10-04T11:37:51.644832
---

# Build SAP Analytics Cloud’s Dashboard for SAP SuccessFactors KPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Build SAP Analytics Cloud's Dashboard for SAP Succ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157287&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Build SAP Analytics Cloud's Dashboard for SAP SuccessFactors KPI](/t5/technology-blog-posts-by-sap/build-sap-analytics-cloud-s-dashboard-for-sap-successfactors-kpi/ba-p/13549021)

![lalitmohan](https://avatars.profile.sap.com/4/d/id4dd8a7a057f018170e1925ef2a912e57921bd84e15123909d0de4b3dd687ddbc_small.jpeg "lalitmohan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[lalitmohan](https://community.sap.com/t5/user/viewprofilepage/user-id/1038)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157287)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157287)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549021)

‎2023 May 20
4:49 AM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157287/tab/all-users "Click here to see who gave kudos to this post.")

5,552

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

Nowadays, data is primarily used to drive business decisions, which means having the right **reporting dashboard is essential** for executives to get a quick overview of a company's performance and to help in business decision-making.

However, many executives and business owners need to pay more attention to this information in exchange for a business intelligence solution. It might be challenging to decide between a **reporting dashboard** and a **business intelligence solution** when they have access to so many different types of data. It's essential to understand a few important aspects when a company has to choose a reporting dashboard and business intelligence solution.

A **reporting dashboard**, which offers a comprehensive business performance assessment, acts as your organization's control panel. Data analytics and dashboard tools work together to support data-driven action. These tools assist businesses in quickly identifying overall company health based on metrics known as **key performance indicators (KPIs)**. Dashboards improve the ultimate efficiency of corporate analytics by enabling users to quickly visualize and examine data, which leads to better decision-making and, ultimately, more success.

A **reporting dashboard** offers the following **essential elements** that are critical to your business intelligence success:

* A snapshot of how your company is performing

* An "at a glance" viewing of business performance

* Instant access to company information

* Easy-to-monitor KPIs

This is exactly how **SAP Analytics Cloud** delivers the right reporting dashboard to **make decisions without doubt and act with confidence**. So, what is **SAP Analytics Cloud**? It is the analytics and planning solution within **the SAP Business Technology Platform**, **SAP Analytics Cloud** supports trusted insights and integrated planning processes enterprise-wide to help you make decisions. ([Read the announcement](https://www.sap.com/products/technology-platform/cloud-analytics.html))

**SAP Datasphere**, together with **SAP Analytics Cloud**, can combine your data sources and extract insights from them based on stories. Effective **data visualizations** make your data appear alive in the story. The arrangement of charts, graphs, tables, and other visual components tells the **story of your business or organization**. You will begin visualizing the insightful data you obtained and be ready to share those insights with your stakeholders.

In this blog post, let us take a look at how we can consume **SAP SuccessFactors** data exposed via **an analytic model** which we have built using SAP Datasphere in my previous article([Connecting SAP SuccessFactors and SAP Datasphere](https://blogs.sap.com/2023/04/20/connecting-sap-successfactors-and-sap-datasphere/)) for the **Talent Analysis** Metrics in SAP Analytics Cloud.

|
 **Blog post series for our learning Journey with SAP Datasphere and SAP Analytics Cloud together to handle complex analytics scenarios.**    1. Connecting SAP SuccessFactors and SAP Datasphere ([click here](https://blogs.sap.com/2023/04/20/connecting-sap-successfactors-and-sap-datasphere/))  2. Bring SAP SuccessFactor Data into SAP Datasphere ([click here](https://blogs.sap.com/2023/04/20/bring-sap-successfactors-data-into-sap-datasphere/))  3. Modeling SAP SuccessFactors Data in SAP Datasphere ([click here](https://blogs.sap.com/2023/05/01/modeling-sap-successfactors-data-in-sap-datasphere/))  4. Building Analytic Models for SAP SuccessFactors KPI ([click here](https://blogs.sap.com/2023/05/08/building-analytic-models-for-sap-successfactors-kpi/))  5. Build SAP Analytics Cloud’s Dashboard for SAP SuccessFactors KPI (this blog) |

## Prerequisite

You need to have:

1. **SAP BTP global account** setup and to entitled the SAP Datasphere Cloud Foundry environment please follow the excellent blog [How to create SAP Datasphere service instance in the SAP BTP Platform?](https://blogs.sap.com/2023/03/17/how-to-create-sap-datasphere-service-instance-in-the-sap-btp-platform/)

2. A **SAP SuccessFactors** instance.

3. Create or have access to an **SAP Analytics Cloud** live data connection to your **SAP Datasphere** tenant. For more information, see the [official SAP Analytics Cloud documentations](https://help.sap.com/viewer/00f68c2e08b941f081002fd3691d86a7/release/en-US/ad4281e2875949f0b4d45d1072ff4c38.html)

## Let’s proceed Step By Step

Before we start, ensure that you have followed and completed the steps mentioned in the following blog posts:

1. The first blog post [Connecting SAP SuccessFactors and SAP Datasphere](https://blogs.sap.com/2023/04/20/connecting-sap-successfactors-and-sap-datasphere/), will help you to connect **SAP SuccessFactors** and **SAP Datasphere.**

2. The second blog post, [Bring SAP SuccessFactors Data into SAP Datasphere](https://blogs.sap.com/2023/04/...
---
title: SAP Datasphere Analytic Model Series – Motivation & Comparison with the Analytical Dataset
url: https://blogs.sap.com/2023/03/28/sap-datasphere-analytic-model-series-motivation-comparison-with-the-analytical-dataset/
source: SAP Blogs
date: 2023-03-29
fetch_date: 2025-10-04T11:00:53.746163
---

# SAP Datasphere Analytic Model Series – Motivation & Comparison with the Analytical Dataset

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Datasphere Analytic Model Series – Motivation ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159919&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere Analytic Model Series – Motivation & Comparison with the Analytical Dataset](/t5/technology-blog-posts-by-sap/sap-datasphere-analytic-model-series-motivation-comparison-with-the/ba-p/13556108)

![philine15](https://avatars.profile.sap.com/f/b/idfbdb14a4abe314959399c2b2961d0f10b0154fa8c2b05a41589ea76adaa80327_small.jpeg "philine15")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[philine15](https://community.sap.com/t5/user/viewprofilepage/user-id/129424)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159919)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159919)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556108)

‎2023 Mar 28
11:39 PM

[22
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159919/tab/all-users "Click here to see who gave kudos to this post.")

9,424

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

# ![](/legacyfs/online/storage/blog_attachments/2023/03/291189_GettyImages-1171730142_small.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/03/line.png)

## Introduction

The [**SAP Datasphere Analytic Model Series**](https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/) is intended to provide you with useful guidance on how to utilize the new Analytic Model to leverage the potential of your data landscape. The Analytic Model allows for rich analytical modelling in a targeted modelling environment and will be THE go-to analytic consumption entity for SAP Datasphere.

This article is the **third** in the blog post series and highlights the **motivation for the new artifact** and draws **comparisons to the Analytical Dataset** conceptually as well as w.r.t. feature details.

So far, the following blogs have been published:

* Blog Post #1: [Introducing the Analytic Model in SAP Datasphere](https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/)

* Blog Post #2: [Data Model Introduction](https://blogs.sap.com/2023/03/20/sap-datasphere-analytic-model-series-data-model-introduction/)

* Blog Post #3: Motivation and Comparison with the Analytical Dataset (Current Post)

* Blog Post #4: [Calculated and Restricted Measures](https://blogs.sap.com/2023/04/03/sap-datasphere-analytic-model-series-calculated-and-restricted-measures/)

* Blog Post #5: [Exception Aggregation](https://blogs.sap.com/2023/04/06/exception-aggregation-in-sap-datasphere/)

* Blog Post #6: [Variable Usage](https://blogs.sap.com/2023/04/17/sap-datasphere-analytic-model-series-using-variables-in-analytic-model/)

* Blog Post #7: [Time Dependency for Dimensions and Texts](https://blogs.sap.com/2023/04/21/time-dependency-for-dimensions-and-texts-in-analytic-model/)

* Blog Post #8: [Data Preview](https://blogs.sap.com/2023/05/02/sap-datasphere-analytic-model-series-data-preview/)

* Blog Post #9: [User Experience and Navigation Paradigm](https://blogs.sap.com/2023/05/09/sap-datasphere-analytic-model-series-user-experience-and-navigation-paradigm/)

* Blog Post #10: [Multi Fact Model](https://blogs.sap.com/2023/05/24/sap-datasphere-analytic-model-series-blog-post-10-design-multi-fact-in-analytic-model/)

Let’s start by taking a closer look at what an Analytical Dataset “really” is.

## Properties of the Analytical Dataset (ADS)

Views modelled as a graphical or SQL view are initially always of the **semantic usage “Relational Dataset**”. This implies that upon deployment, a relational, SQL-consumable database view will be created in the HANA cloud database powering SAP Datasphere.

At some point in time, users can select to **change the semantic usage to "Analytical Dataset"**. This **enables** some **additional features** in the view’s design-time that are important for subsequent consumption of the view by SAP Analytics Cloud. These new features consist of mainly:

* Classification of view columns as either attribute or measure (including its aggregation type)

* Possibility to add semantic type information to columns. This way, modelers can add a usage context that classifies a column for example as label, currency, unit, business date (relevant for time-dependency) etc.

* Adding of associations to other entities like text or dimension objects

For a good example of this, please [load the example data model of the blog series](https://blogs.sap.com/2023/03/20/sap-datasphere-analytic-model-series-data-model-introduction/) and inspect its exact properties w.r.t. semantic types & associations between entities.

On deployment of the Analytical Dataset, there will now be TWO runtime artefacts generated on SAP HANA Cloud, namely

1. An **analytical**, SAC-consumable **star schema**

2. A **relational**, SQL-consumable **database view**

![](/legacyfs/online/storage/blog_attachments/2023/03/figure1.png)

*Figure 1: Runtime artefacts of Analytical Datasets*

Both of them come under the name of the Analytical Dataset itself, but

* one allows for **relational queries**, typically via SQL (e.g. when using an OpenSQL schema) and “lives” on HANA’s SQL engine. Its data is displayed when you preview the Analytical Dataset in the View Builder

* the other one allows for **analytical queries** and “lives” on [SAP HANA’s Multi-Dimensional Services (MDS) engine](https://launchpad.support.sap.com/#/notes/2670064). It is queried by SAP Analytics Cloud via the Information Access (InA) protocol.

For the comparison with the Analytic Model, let’s focus on the analytical star-schema artefact only.

Since the focus of the Analytical Dataset was always to make **analytical consumption of the underlying view data extremely simple**, it needed to make sacrifices with regards to the complexity of the analytical modelling itself. Concretely, these are:

* Measures in Analytical Datasets always use **standard aggregations only**.
  These are SUM, MAX, MIN, COUNT and NONE. Other, more complex measures can be built in SAP Analytics Cloud stories

* Users **cannot decide which columns and associations are provided**.The system automatically exposes all measures & attributes of the Analytical Datasets and always includes all first-level dimensions into the star schema also. By first-level dimensions we mean dimensions that are directly associated to the Analytical Datasets. If those associated dimensions themselves bear associations to yet other dimensions, then these will not be included. We’ll look at example cases further down in the post.

##

## Motivation of the Analytic Model

The Analytic Model now goes beyond the analytical capabilities of the Analyti...
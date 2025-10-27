---
title: Extending SAC Planning – Acessing planning data with SAP Datasphere
url: https://blogs.sap.com/2023/05/17/extending-sac-planning-acessing-planning-data-with-sap-datasphere/
source: SAP Blogs
date: 2023-05-18
fetch_date: 2025-10-04T11:39:34.349803
---

# Extending SAC Planning – Acessing planning data with SAP Datasphere

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Extending SAC Planning - Acessing planning data wi...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164266&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extending SAC Planning - Acessing planning data with SAP Datasphere](/t5/technology-blog-posts-by-sap/extending-sac-planning-acessing-planning-data-with-sap-datasphere/ba-p/13569660)

![vlad-andrei_sladariu](https://avatars.profile.sap.com/1/b/id1b81ef5d9548a7af86582960f5d612ade0178e89165c5b6d3c22aea773cb5f5c_small.jpeg "vlad-andrei_sladariu")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[vlad-andrei\_sladariu](https://community.sap.com/t5/user/viewprofilepage/user-id/207132)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164266)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164266)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569660)

‎2023 May 17
11:14 PM

[29
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164266/tab/all-users "Click here to see who gave kudos to this post.")

16,937

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [Extended Planning and Analysis](https://community.sap.com/t5/c-khhcw49343/Extended%2520Planning%2520and%2520Analysis/pd-p/bcbf0782-ce74-43b8-b695-dafd7c1ff1c1)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [Extended Planning and Analysis

  Product Category](/t5/c-khhcw49343/Extended%2BPlanning%2Band%2BAnalysis/pd-p/bcbf0782-ce74-43b8-b695-dafd7c1ff1c1)

View products (7)

Learn how a SAC Planning model can be populated with data coming from custom calculations or Machine Learning. We describe this concept in a series of three blogs.

The blogs in the series are:

* Accessing planning data with SAP Datasphere (this blog)

  + Create a simple planning model in SAC

  + Make the planning data available in SAP Datasphere, so that it can be used by a Machine Learning algorithm

* [Creating custom calculations or ML](https://blogs.sap.com/2023/05/22/extending-sac-planning-creating-custom-calculations-or-ml/)

  + Define the Machine Learning Logic

  + Create a REST-API that makes the Machine Learning logic accessible for SAC Planning

* [Orchestrating the end-to-end business process](https://blogs.sap.com/2023/05/22/extending-sac-planning-importing-calculation-results-from-sap-datasphere-and-e2e-workflow/)

  + Import the predictions into the planning model

  + Operationalise the process

*Note: The hyperlinks to the other blogs of this series and to the sample repository might not yet be working for you. They will be updated as soon as those links are public / permanent.*

This diagram shows the architecture and process from a high level:

![](/legacyfs/online/storage/blog_attachments/2023/05/esp-0-0-architecture.png)

The whole concept and blog series has been put together by maria.tzatsou2, andreas.forster, gonzalo.hernan.sendra and vlad-andrei.sladariu.

## Intro for this blog

In the current blog, 'Accessing planning data with SAP Datasphere' we will achieve the following tasks:

1. create a simple P&L model in SAC and add some data to it

2. expose the data in the P&L model in DataSphere

In order to complete the steps described, you will need:

* an SAP Analytics Cloud (SAC) instance

* an SAP Datasphere instance

* a Data Provisioning Agent (DP Agent) set up in your Datasphere instance

## 1. Create a simple P&L model

### 1.1 Prepare the data

We will implement the following P&L model:

* Profit = Revenue - Cost

* Revenue = UnitsSold \* UnitPrice

* Cost = DirectCost + IndirectCost

* DirectCost = UnitsSold \* UnitCost

UnitsSold, UnitPrice, UnitCost and IndirectCost are all inputs to the model

We have to consider two types of data:

* actuals: this is input data that we record about the past

* planning: this is input data that we create for the future

In the current example, we will create:

* 12 months of planning data: 202301 to 202312

* 15 months of actuals data: 202201 to 202303

Then, we will use the actuals for UnitPrice and UnitsSold and the plan for UnitPrice to estimate the plan for UnitsSold via external ML.

We prepare this data in csv and will later upload it to the SAC Planning model.

The data for one month looks like this:

![](/legacyfs/online/storage/blog_attachments/2023/05/ESP-1-1-data-in-excel.png)

Note that the costs are recorded as negatives. This is to allow hierarchical aggregation.

The sample data is available [here](https://github.com/SAP-samples/btp-global-center-of-excellence-samples/blob/c7b31696d667a42c0399c208f35c6da4213c323e/Extending%20SAC%20Planning/ExtSACP01-sample-data.xlsx).

### 1.2 Define the model in SAC

This sections assumes some basic familiarity with the SAC interface - so we won't add screenshots with the location of the required buttons.

We start with an empty model (Modeler -> Create new model -> New Model). This is a planning model by default.

![](/legacyfs/online/storage/blog_attachments/2023/05/esp-1-2-sac-new-model.png)

We need one measure which we name 'Value' and keep the default decimal type. This will hold the data values.

![](/legacyfs/online/storage/blog_attachments/2023/05/esp1-3-sac-new-measure-value.png)

We need one dimension, 'Account'. Here we will add members for all the different elements in the P&L model.

The dimension type is 'Account'. This will create a hierarchy allowing us to aggregate accounts hierarchically.

![](/legacyfs/online/storage/blog_attachments/2023/05/esp-1-4-sac-new-dimension-account.png)

We add all the elements of the P&L as member...
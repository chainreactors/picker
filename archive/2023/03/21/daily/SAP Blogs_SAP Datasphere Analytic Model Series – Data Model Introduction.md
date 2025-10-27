---
title: SAP Datasphere Analytic Model Series – Data Model Introduction
url: https://blogs.sap.com/2023/03/20/sap-datasphere-analytic-model-series-data-model-introduction/
source: SAP Blogs
date: 2023-03-21
fetch_date: 2025-10-04T10:08:27.751909
---

# SAP Datasphere Analytic Model Series – Data Model Introduction

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Datasphere Analytic Model Series – Data Model ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158028&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere Analytic Model Series – Data Model Introduction](/t5/technology-blog-posts-by-sap/sap-datasphere-analytic-model-series-data-model-introduction/ba-p/13550812)

![jaigupta](https://avatars.profile.sap.com/7/5/id7519e643db7b44d5296701489a87efcce63f4f346a469dac3b37df929f48ffcd_small.jpeg "jaigupta")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jaigupta](https://community.sap.com/t5/user/viewprofilepage/user-id/39263)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158028)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158028)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550812)

‎2023 Mar 20
9:48 PM

[22
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158028/tab/all-users "Click here to see who gave kudos to this post.")

22,279

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

![](/legacyfs/online/storage/blog_attachments/2023/03/image001-1.png)

*Figure 1: A complex data model that we’ll use along the entire blog series*

![](/legacyfs/online/storage/blog_attachments/2023/03/image004-1.png)

# **Introduction**

The [**SAP Datasphere Analytic Model Series**](https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/) is intended to provide you with useful guidance on how to utilize the new Analytic Model to leverage the potential of your data landscape. The Analytic Model allows for rich analytical modelling in a targeted modelling environment and will be THE go-to analytic consumption entity for SAP Datasphere.

This article is the second in the blog post series and introduces an example data model that we’ll use along the entire blog series listed below:

+ Blog Post #1: [Introducing the Analytic Model in SAP Datasphere](https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/)
+ Blog Post #2: Data Model Introduction - Current blog
+ Blog Post #3: [Motivation & Comparison with the Analytical Dataset](https://blogs.sap.com/2023/03/28/sap-datasphere-analytic-model-series-motivation-comparison-with-the-analytical-dataset/)
+ Blog Post #4:[SAP Datasphere Analytic Model Series – Calculated and Restricted Measures](https://blogs.sap.com/?p=1731623 "SAP Datasphere Analytic Model Series – Calculated and Restricted Measures")
+ Blog Post #5: [Exception Aggregation](https://blogs.sap.com/2023/04/06/exception-aggregation-in-sap-datasphere/)
+ Blog Post #6: [Using Variables in Analytic Model](https://blogs.sap.com/2023/04/17/sap-datasphere-analytic-model-series-using-variables-in-analytic-model/)
+ Blog Post #7: [Time Dependency for Dimensions and Texts in Analytic Model](https://blogs.sap.com/2023/04/21/time-dependency-for-dimensions-and-texts-in-analytic-model/)
+ Blog Post #8:[SAP Datasphere Analytic Model Series – Data Preview](https://blogs.sap.com/2023/05/02/sap-datasphere-analytic-model-series-data-preview/)
+ Blog Post #9:[SAP Datasphere Analytic Model Series – User Experience and Navigation Paradigm | SAP Blogs](https://blogs.sap.com/2023/05/09/sap-datasphere-analytic-model-series-user-experience-and-navigation-paradigm/)
+ Blog Post #10: [SAP Datasphere Analytic Model Series Blog Post # 10– Design Multi Fact in Analytic Model](https://community.sap.com/t5/technology-blogs-by-sap/sap-datasphere-analytic-model-series-blog-post-10-design-multi-fact-in/ba-p/13551770)

In this blog, we describe the data model structure and help you import it with data. As a result, you’ll have a rich model for your own experiments with the Analytic Model and you’ll also be able to immediately apply the learnings of upcoming blogs since they are all based on exactly this model.

# **Understanding the Data Model**

Data model consists of sales opportunity data of employees for various products and customers of the company across different cost centers within sales organizations of the company.
Also, Time related Dimensions linked to data model provide options for doing time related drilldown, reporting and filtering. Moreover, Hierarchies for Employees and Products can be used for further analysis.
Some of the example reporting scenarios are mentioned below:

+ Identify Top/Bottom N Employees in current month/quarter/year in terms of Sales opportunity value.
+ Identify total value of Missed opportunities across products in current month/quarter/year
+ Identify Top/Bottom N Products in terms of Sales opportunity value

PFB list of tables in our Data Model:

* Sales Opportunity Data
  + Header Table - MCT\_Opportunities
  + Item Table - MCT\_OpportunityItems

* Product data
  + Product dimension with hierarchy - MCT Products
  + Product categories dimension table - MCT\_ProductCategories
  + Product Groups texts table - MCT\_ProductGroupTexts -

* Controlling Area data
  + Dimension MCT\_ControllingArea

* Cost Center data
  + Dimension *MCT Cost Center*

* Sales Organization data
  + Dimension - MCT\_SalesOrganization
  + Sales Organization Texts - MCT\_SalesOrgText

* Item Status Texts - MCT\_ItemStatusTexts
* Employee data

+ Dimension with hierarchy data - MCT\_Employees

* Time data
  + Dimension Day - SAP.TIME.VIEW\_DIMENSION\_DAY
  + Translation Table – Quarter - SAP.TIME.M\_TIME\_DIMENSION\_TDAY
  + Dimension Day - SAP.TIME.VIEW\_DIMENSION\_DAYTime data
  + Translation Table – Month - SAP.TIME.M\_TIME\_DIMENSION\_TMONTH -
  + Translation Table – Day - SAP.TIME.M\_TIME\_DIMENSION\_TQUARTER

These tables are associated to each other as is depicted in the image at the top of this blog or in the impact & lineage diagram shown below:

![](/legacyfs/online/storage/blog_attachments/2023/03/image005.png)

*Figure 2 : Impact and Lineage Diagram of the sample data model*

To check the association further in detail, please refer the tables and views associations once you have imported the data model into SAP Datasphere.

# **Importing the Data Model**

For data model import, it’s preferred to create a new space. However, you can use existing spaces if you are confident that there will be no conflict which will arise due to the existing objects like Table, Views in your space.

1. As a first step, download the ZIP files from below path to your local directory. It contains the data CSV files and the CSN export for the data model.

[https://github.com/SAP-samples/analytics-cloud-datasphere-community-content/releases/tag/DSPSampleAM...](https://github.com/SAP-samples/analytics-cloud-datasphere-community-content/releases/tag/DSPSampleAM_1.0.0)

![](/legacyfs/online/storage/blog_attachments/2023/03/image009-1.png)

*Figure 3: Item List screenshot z...
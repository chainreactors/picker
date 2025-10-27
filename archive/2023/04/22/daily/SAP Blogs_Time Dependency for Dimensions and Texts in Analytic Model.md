---
title: Time Dependency for Dimensions and Texts in Analytic Model
url: https://blogs.sap.com/2023/04/21/time-dependency-for-dimensions-and-texts-in-analytic-model/
source: SAP Blogs
date: 2023-04-22
fetch_date: 2025-10-04T11:33:27.752267
---

# Time Dependency for Dimensions and Texts in Analytic Model

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Time Dependency for Dimensions and Texts in Analyt...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160102&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Time Dependency for Dimensions and Texts in Analytic Model](/t5/technology-blog-posts-by-sap/time-dependency-for-dimensions-and-texts-in-analytic-model/ba-p/13556566)

![hongzhou03](https://avatars.profile.sap.com/c/0/idc0c352ba2218cad90287b3d8d5b39a476ecf0b4ca5962a6f40434819bd66bd53_small.jpeg "hongzhou03")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[hongzhou03](https://community.sap.com/t5/user/viewprofilepage/user-id/115750)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160102)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160102)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556566)

‎2023 Apr 21
10:07 PM

[15
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160102/tab/all-users "Click here to see who gave kudos to this post.")

11,408

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

![](/legacyfs/online/storage/blog_attachments/2023/04/280852_GettyImages-597529071_medium_jpg.jpg)

*Figure 1: Time Dependency for Dimensions and Texts in Analytic Model (Source: SAP)*![](/legacyfs/online/storage/blog_attachments/2023/04/Yellow-Line-3.png)

# Introduction

The [**SAP Datasphere Analytic Model Series**](https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/) is intended to provide you with useful guidance on how to utilize the new Analytic Model to leverage the potential of your data landscape. The Analytic Model allows for rich analytical modelling in a targeted modelling environment and will be THE go-to analytic consumption entity for SAP Datasphere.

This article is the 7th of the blog post series and introduces **Time Dependency for Dimensions and Texts in Analytic Model**. The following blogs have been published so far:

* #1: [Introducing the Analytic Model in SAP Datasphere](https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/)

* #2: [Data Model Introduction](https://blogs.sap.com/2023/03/20/sap-datasphere-analytic-model-series-data-model-introduction/)

* #3: [Motivation & Comparison with the Analytical Dataset](https://blogs.sap.com/2023/03/28/sap-datasphere-analytic-model-series-motivation-comparison-with-the-analytical-dataset/)

* #4: [Calculated and Restricted Measures](https://blogs.sap.com/2023/04/03/sap-datasphere-analytic-model-series-calculated-and-restricted-measures/)

* #5: [Exception Aggregation](https://blogs.sap.com/2023/04/06/exception-aggregation-in-sap-datasphere/)

* #6: [Using Variables in Analytic Model](https://blogs.sap.com/2023/04/17/sap-datasphere-analytic-model-series-using-variables-in-analytic-model/)

Stay tuned for more blogs around the Analytic Model in the coming weeks.

Time-Dependency enablement for dimension or text in SAP Datasphere is available since Q4.2022, it was firstly supported in Analytical Dataset. The Analytic Model supports it as well and adds the possibility to collect the reference date via a model parameter.

# Business Value

Master data often changes over time. This is known as “time-dependency”. Let us take “Employee” as an example, an employee could change the marital status, the record in the system will be like this:![](/legacyfs/online/storage/blog_attachments/2023/04/Figure-1-Sample-data-of-Employee.png)

*Figure 2: Sample data of Employee (Source: Own Image)*

With this feature enabled, the report could display appropriate marital status for any given time period.

# How to Apply

Modelers can specify the periods of validity of each record of your dimension or text entity. The following illustrations are based on below simple data model:

![](/legacyfs/online/storage/blog_attachments/2023/04/Figure-2-Simple-example-of-data-model.png)

*Figure 3: Simple data model for illustration (Source: Own Image)*

Dimension: *Employee\_TimDep*, is associated with Analytical Dataset: *V\_Sales\_TD*, which is the fact source of Analytic Model *AM\_TimeDep*.

Three steps are required to implement the time-dependency feature in Analytic Model.

* Step 1: Specify Time-Dependent Semantic Types in your Dimension or Text Entity

* Step 2: Associate the dimension with Analytical Dataset and create Analytic Model

* Step 3(Optional): Add a variable to allow SAP Analytics Cloud users to enter a date of their choice and show dimension members based on that key date

Step 1: Specify Time-Dependent Semantic Types in your Dimension or Text Entity

In above example of dimension: *Employee\_TimDep*, make the changes accordingly as below:![](/legacyfs/online/storage/blog_attachments/2023/04/Figure-3-dimension-setting.png)

*Figure 4: Time-Dependent setting on Dimension (Source: Own Image)*

By default, the “*Business Date - From”* and “*Business Date - To”* are treated inclusively, however you could change the behavior, please refer to [SAP Help: Enable Time-Dependency for a Dimension or Text Entity](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/11b2ff4179a14c379bfdf7b7b85b09a1.html).

Step 2: Associate the dimension with Analytical Dataset and create Analytic Model

Any Analytical Dataset pointing to a time-dependent dimension via an association automatically benefits from its time-dependent data. The dimension members and their names are displayed based on the current date by default. Technically, this means that reference date is pushed down in the WHERE condition when the dimension members or text members are selected during query execution.

For example, let’s create an association on the Analytical Dataset: *V\_Sales\_TD.*![](/legacyfs/online/storage/blog_attachments/2023/04/Figure-5-associate-dimension-with-ADS.png)

*Figure 5: Association between Dimension and Analytical Dataset (Source: Own Image)*

As the reference date (aka key date) is not specified, the system uses the current date by default. Click on the button “Create Analytic Model” on the panel of Analytical Dataset: *V\_Sales\_TD*.![](/legacyfs/online/storage/blog_attachments/2023/04/Figure-6-create-AM.png)

*Figure 6: Create Analytic Model from Analytical Dataset (Source: Own Image)*

After deployment of Analytic Model: *AM\_TimeDep*, perform the data preview to verify the data. The current date is April 24th in 2023, the retrieved “*Marital\_Status*” is “Married”.![](/legacyfs/online/storage/blog_attachments/2023/04/Figure-7-data-preview-of-AM.png)

*Figure 7: Data Preview of Analytic Model (Source: Own Image)*

Step 3 (Optional): Add a variable to allow SAP Analytics Cloud users to enter a date of their choice and show dimension members based on that key date

With Analytic Model, there is a new variable type called “Refer...
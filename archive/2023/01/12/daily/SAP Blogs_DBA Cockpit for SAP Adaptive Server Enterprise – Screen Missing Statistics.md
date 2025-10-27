---
title: DBA Cockpit for SAP Adaptive Server Enterprise – Screen Missing Statistics
url: https://blogs.sap.com/2023/01/11/dba-cockpit-for-sap-adaptive-server-enterprise-screen-missing-statistics/
source: SAP Blogs
date: 2023-01-12
fetch_date: 2025-10-04T03:39:12.003364
---

# DBA Cockpit for SAP Adaptive Server Enterprise – Screen Missing Statistics

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* DBA Cockpit for SAP Adaptive Server Enterprise – S...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163414&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [DBA Cockpit for SAP Adaptive Server Enterprise – Screen Missing Statistics](/t5/technology-blog-posts-by-sap/dba-cockpit-for-sap-adaptive-server-enterprise-screen-missing-statistics/ba-p/13566974)

![SteffiP](https://avatars.profile.sap.com/2/1/id212f14021e66adbd4d8405ff403edb174a9dc7337b2aa83d403c7226167e415f_small.jpeg "SteffiP")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[SteffiP](https://community.sap.com/t5/user/viewprofilepage/user-id/46608)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163414)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163414)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566974)

‎2023 Jan 11
9:14 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163414/tab/all-users "Click here to see who gave kudos to this post.")

1,114

* SAP Managed Tags
* [SAP Adaptive Server Enterprise](https://community.sap.com/t5/c-khhcw49343/SAP%2520Adaptive%2520Server%2520Enterprise/pd-p/67837800100800005166)
* [SAP ASE - ERP Enablement](https://community.sap.com/t5/c-khhcw49343/SAP%2520ASE%2520-%2520ERP%2520Enablement/pd-p/680295143422925801844118105092535)

* [SAP Adaptive Server Enterprise

  SAP Adaptive Server Enterprise](/t5/c-khhcw49343/SAP%2BAdaptive%2BServer%2BEnterprise/pd-p/67837800100800005166)
* [SAP ASE - ERP Enablement

  Software Product Function](/t5/c-khhcw49343/SAP%2BASE%2B-%2BERP%2BEnablement/pd-p/680295143422925801844118105092535)

View products (2)

## Introduction

In my previous article [DBA Cockpit for SAP ASE – New Screens and Enhancements](https://blogs.sap.com/2023/01/06/dba-cockpit-for-sap-ase-new-screens-and-enhancements/), I introduced a new screen called Missing Statistics for the DBA Cockpit for the SAP Adaptive Server Enterprise. Missing Statistics can be a useful indicator to improve and to optimize the query performance. The more accurate information about the data and the database the optimizer has, the better the achieved performance. However, capturing missing statistics will not always lead to different or better query plans and comes with a cost, because it consumes system resources such as CPU, buffer pools, sort buffers, and procedure cache. In addition to it, enabling the server to capture missing statistics is primarily intended for a development environment. Due to performance and stability implications capture missing statistics is not intended to be used in a production environment. At least, it should be carefully considered when it is used in a productive environment.

## Overview

In this article, I would like:

* to provide more information about Missing Statistics in general,

* to introduce the new screen Missing Statistics in the DBA Cockpit for SAP Adaptive Server Enterprise in-depth,

* to explain how to analyze missing statistics and,

* to provide recommendations for additional statistics.

## Missing Statistics

There are two types of statistics: **Object Level Statistics** and **Column Level Statistics**. In this article, we will solely focus on **Column Level Statistics**. Those statistics describe the distribution of values in the column. It consists of the column’s histogram and density values. It is updated when an index is created or an update statistics command is run. In general, **Column Level Statistics** needs to be updated from time to time.

## How to Collect Missing Statistics

Missing Statistics can be collected with **Capture Missing Statistics**. **Capture Missing Statistics** stores the data in the system table **sysstatistic*s***. A detailed description how to collect missing statistics can be found [here](https://help.sap.com/docs/SAP_ASE/a7b3e46335184f5caf70a08c91c540f3/be369170571d444587593cb9e7b3adb4.html).

## Analysis of Missing Statistics

The new screen Missing Statistics is designed to help you to investigate a negative change in performance quickly and to determine when to create additional statistics or when to update statistics. After Capture Missing Statistics is enabled, you will see a single column or a list of columns which were counted as missing. For example, the column TASKNAME of the table /BDL/TASKS were counted 1860 times as missing.

![](/legacyfs/online/storage/blog_attachments/2023/01/screenshot1-2.png)

Figure 1: Missing Statistics for Column TASKNAME

The fact that this column was missing 1860 times doesn’t mean that you need to update statistics for this column. It is required to investigate it further. To start your investigations, you can check the **Cached Statements** or **Top SQL Statements** screen whether you find a query related to it. Those screens are available in the **Performance Menu > SQL Statement** of the DBA Cockpit for SAP Adaptive Server Enterprise. To investigate the Missing Statistics further, you will also find more information related to the affected table when scrolling down to the Details screen of **Missing Statistics**. The Overview screen Missing Statistics and all Features related to this screen are explained in my first article [here](https://blogs.sap.com/2023/01/06/dba-cockpit-for-sap-ase-new-screens-and-enhancements/). In this article, will focus on the details screen of Missing Statistics.

### Key Metric – Data Change

Data Change is an indicator for how much data has changed in the data distribution since update statistics last ran. In particular, this indicator provides the number of inserts, updates, and deletes on a  given object, partition, or column. It is summarized as a percentage of the total number of rows in the table or partition (if the partition is specified). This value can be greater than 100 percent because the number of changes to an object can more than the number of rows in the table. Data Change is used to estimate the cost of an additional index.

* If there is no or less data change, additional index is inexpensive.

* If there is a lot of data change, additional index is expensive.

![](/legacyfs/online/storage/blog_attachments/2023/01/screenshot2-2.png)

Figure 2: Data Change for the affected Table

### Other Useful Metrics

#### Number of Rows

Number of Rows is used to estimate the cost of additional statistics.

* It is more feasible to create additional statistics for smaller tables than for larger tables.

* If a table is empty, then it is less feasible to create additional statistics.

![](/legacyfs/online/storage/blog_attachments/2023/01/screenshot3-2.png)

Figure 3: Number of Rows for the affected Table

#### Forwarded Rows

Forwarded Rows is used to determine forwarding record pointer on the original page to point to the new page.

* Forwarded records are rows in a heap that have been moved from the original page to a new page.

* Updates can cause forwarded records if the updated da...
---
title: DBA Cockpit for SAP ASE – New Screens and Enhancements
url: https://blogs.sap.com/2023/01/06/dba-cockpit-for-sap-ase-new-screens-and-enhancements/
source: SAP Blogs
date: 2023-01-07
fetch_date: 2025-10-04T03:15:18.698395
---

# DBA Cockpit for SAP ASE – New Screens and Enhancements

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* DBA Cockpit for SAP ASE – New Screens and Enhancem...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161874&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [DBA Cockpit for SAP ASE – New Screens and Enhancements](/t5/technology-blog-posts-by-sap/dba-cockpit-for-sap-ase-new-screens-and-enhancements/ba-p/13561944)

![SteffiP](https://avatars.profile.sap.com/2/1/id212f14021e66adbd4d8405ff403edb174a9dc7337b2aa83d403c7226167e415f_small.jpeg "SteffiP")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[SteffiP](https://community.sap.com/t5/user/viewprofilepage/user-id/46608)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161874)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161874)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561944)

‎2023 Jan 06
6:29 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161874/tab/all-users "Click here to see who gave kudos to this post.")

2,088

* SAP Managed Tags
* [SAP Adaptive Server Enterprise](https://community.sap.com/t5/c-khhcw49343/SAP%2520Adaptive%2520Server%2520Enterprise/pd-p/67837800100800005166)
* [SAP ASE - ERP Enablement](https://community.sap.com/t5/c-khhcw49343/SAP%2520ASE%2520-%2520ERP%2520Enablement/pd-p/680295143422925801844118105092535)

* [SAP Adaptive Server Enterprise

  SAP Adaptive Server Enterprise](/t5/c-khhcw49343/SAP%2BAdaptive%2BServer%2BEnterprise/pd-p/67837800100800005166)
* [SAP ASE - ERP Enablement

  Software Product Function](/t5/c-khhcw49343/SAP%2BASE%2B-%2BERP%2BEnablement/pd-p/680295143422925801844118105092535)

View products (2)

My name is Steffi. I started to work for SAP as support engineer for SAP Business ByDesign and SAP Cloud for Customer in Galway, Ireland in 2019. After two years, I transitioned to a new role as Developer in St. Leon-Rot, Germany. Here, I am responsible for designing, developing, enhancing, and supporting monitoring and administration tools for SAP Adaptive Server Enterprise database.

In this article, I will provide you an overview of some of the new features and enhancements of the DBA Cockpit for SAP Adaptive Server Enterprise in the past two years.

## Missing Statistics

In the **Diagnostics Menu**, there is a new screen called **Missing Statistics**. This screen is based on the configuration parameter **Capture Missing Statistics** and on the system table **sysstatistics**. Once Capture Missing Statistics is enabled, this screen shows:

* the **Date** the statistic was reported as **first time missing**,

* the **Database**,

* the **Table name**,

* the **Column name(s)**, and

* the **Number of times** the statistic was **counted** as **missing**.

This screen features the possibility to **activate** and to **deactivate Capture Missing Statistics** **ad-hoc** and on an **hourly basis** (with the help of the SAP ASE Job Scheduler). In addition to it, there is also a possibility to **jump to** the **Single Table Analysis Screen** and to **update statistics** directly from this screen.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot9.png)

Figure 1: Features of the Screen Missing Statistics

More information about the topic Missing Statistics will follow in a separate blog article.

## SSL Certificates

In the **Diagnostics** menu, there is another new screen called **SSL Certificates** that shows:

* the **file path**,

* the **start date**, and

* the **end date** of the SSL certificate.

This information comes from the table **master..monSSLCertInfo** which provides information about installed SSL certificates. The screen features a filter on end date to sort the end date in a way that the certificate with the smallest end date is at the top of the overview.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot2-1.png)

Figure 2: Screen SSL Certificates

## Dump Overview & Dump History

The reason for the re-design of the screen Dump History was that a new API to retrieve information on backups has been made available with the introduction of BALDR. The screen **Dump Overview** located below the **Backup & Recovery Menu** will provide the **time of the last successful dump** as well as the **time elapsed since the last successful dump** for each database of the database server and for each type of dump:

* database dumps,

* cumulative dumps,

* delta dumps, and

* transaction log dumps.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot10-2.png)

Figure 3: Screen Dump Overview

The  screen **Dump History** features a summary of the number of the failed as well as of the successful database and transaction dumps, a filter to get all dumps for a specific database and for a specific status. The overview table is split into **Database Dump tab** where database dumps, cumulative dumps, and delta dumps and **Transaction Dump tab** where Transaction Dump can be monitored for a specific time frame.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot14.png)

Figure 4: Screen Dump History

If a dump with the status failed is selected in the table, it will also display an error code and description.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot15-1.png)

Figure 5: Error Information

## Baldr Version

For all database systems where the owner of the DBA Cockpit is Baldr we show the **Baldr Version** on the **Instance Overview Plugin** and on the screen **Data Collectors and Admin Procedures**. For older systems where the owner is not Baldr it shows that the information is not applicable.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot11.png)

Figure 6: Baldr Version

## Synchronisation State & Mode

The **Replication Plugin** on the Dashboard was split into three views:

* **HADR Overview**,

* **HA/DR: HA Status**, and

* **HA/DR: DR Standby**.

The first view will show the **logical host**, the **HADR State** and the **HADR Mode**. The second view will show the **site 1** & **site 2** as well as the **Synchronisation State** and the **Synchronisation Mode**. The third view will show the same information like the second view, but for the **site 3** (if existing).

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot13-1.png)

Figure 7: Replication Plugins

## IMRS Cache

The screen **IMRS Caches** located in the **Configuration Menu** will provide an overview of the IMRS caches that have been created on a specific database system. It shows

* the **Cache name**,

* the **Cache size**,

* the **Used Size**,

* the **database name**, and

* the **status**.

This information comes from the table **master..monIMRSCache**. On this screen, you can create a new IMRS cache, change the current size of an existing IMRS cache or change the assigned database, and remove an existing IMRS cache.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot12.png)

Figure 8: IMRS Cache Configuration

Information on memory usage such as...
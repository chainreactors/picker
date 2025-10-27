---
title: SAP S/4HANA migration cockpit – Transferring Data from CSV Template Files to Staging Tables
url: https://blogs.sap.com/2023/02/06/sap-s-4hana-migration-cockpit-transferring-data-from-csv-template-files-to-staging-tables/
source: SAP Blogs
date: 2023-02-07
fetch_date: 2025-10-04T05:51:05.241927
---

# SAP S/4HANA migration cockpit – Transferring Data from CSV Template Files to Staging Tables

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA migration cockpit - Transferring Data ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52166&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA migration cockpit - Transferring Data from CSV Template Files to Staging Tables - CSV File Upload](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-migration-cockpit-transferring-data-from-csv-template-files-to/ba-p/13562540)

![IlianaOlvera7](https://avatars.profile.sap.com/7/6/id7653c2fbea927c91e39ba0c1a9d06c9f0207afac025265516f164c2014acd29b_small.jpeg "IlianaOlvera7")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[IlianaOlvera7](https://community.sap.com/t5/user/viewprofilepage/user-id/131553)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52166)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52166)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562540)

‎2023 Feb 06
8:25 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52166/tab/all-users "Click here to see who gave kudos to this post.")

14,937

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA migration cockpit](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520migration%2520cockpit/pd-p/791935194581077217831679640306539)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA migration cockpit

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bmigration%2Bcockpit/pd-p/791935194581077217831679640306539)

View products (3)

This blog post will give details on how to populate the ****SAP S/4HANA Migration Cockpit staging tables using CSV files****. It will give an overview of the CSV feature of the SAP S/4HANA Migration Cockpit and will provide step-by-step examples on **how to load data into the staging tables using** ****CSV files**** for ****SAP S/4HANA Cloud 2302****.

Note that the process for transferring data to the staging tables ***for** **SAP S/4HANA 2022*** is slightly different. You can find more details about this in the Knowledge Base Article (KBA) [3296020](https://launchpad.support.sap.com/#/notes/3296020).

First, let’s have a **short introduction** and **overview** of the **S/4HANA migration cockpit:**

The ****SAP S/4HANA migration cockpit**** is designed for customers who have just installed SAP S/4HANA and want to move their legacy data from SAP or non-SAP software systems. It allows you to migrate your master data and transactional data to SAP S/4HANA, and it facilitates this process by providing predefined migration content and mapping. It can be launched using the “****Migrate Your Data****” ****app**** in the Fiori Launchpad (Data Migration Launchpad). The migration cockpit is part of both SAP S/4HANA and SAP S/4HANA Cloud and is included in these licenses.

For SAP S/4HANA (On-Premise) for the Migrate your Data – Migration Cockpit two different **migration approaches** are available. Namely, ****Migrate Data Using Staging Tables**** and ****Migrate Data Directly from SAP System****.

The migration approach ****Migrate Data Using Staging Tables**** is recommended if you want to transfer a lot of data to SAP S/4HANA in an automated way. It is the most efficient way of transferring large volumes of data. Staging tables are database tables and therefore provide greater flexibility than files regarding managing data (for example sorting data, searching for data, checking for duplicate records and so on).

If you use the **migration approach Migrate Data Using Staging Tables**, the SAP S/4HANA migration cockpit automatically creates staging tables for each migration object that is relevant for your project. You can **fill the staging tables** with data either using ***XML templates***, ***CSV files***, or manually using the SAP HANA Studio or by using ***third party or SAP’s ETL tools (***for example SAP Agile Data Preparation).

If you want to have short introduction and overview of the SAP S/4HANA migration cockpit and, more details about the migration approach Migrate Data Using Staging Tables see the blog in the link below. There you can also find more details about loading data to the staging tables using XML files:

* [Part 1: Migrate your Data – Migration Cockpit (from SAP S/4HANA 2020, SAP S/4HANA Cloud 2008), Migra...](https://blogs.sap.com/2021/03/10/part-1-migrate-your-data-migration-cockpit-from-sap-s-4hana-2020-sap-s-4hana-cloud-2008-migrate-data-using-staging-tables-and-methods-for-populating-the-staging-tables-with-data/)

The ****CSV feature**** is available with SAP S/4HANA Cloud 2208 and SAP S/4HANA 2022. With this feature, you can use CSV files to populate the staging tables with data in the Migration Cockpit - Migrate Your Data app.

For **SAP S/4HANA Cloud 2302** and higher, there are some **new functions for uploading CSV files**, for example, you have now the option to remove columns and change the orders of the columns with the CSV header option “First Row is Header Row”.

For more details see:

* SAP Help Portal: [Transferring Data from CSV Template Files to Staging Tables](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/85148c2930b54c9f8c4e2808c0e79f58.html?version=2208.500)

* Knowledge Base Article (KBA) [3210687](https://launchpad.support.sap.com/#/notes/3210687) and [3296020](https://launchpad.support.sap.com/#/notes/3296020).

# **Prerequisites**

* In the SAP S/4HANA migration cockpit You have created a migration project that uses the migration approach **Migrate Data Using Staging Tables**.

* You have selected the relevant migration objects for your migration project.

* If you use the SAP HANA Remote Database connection, you must create first an SAP HANA database connection between the SAP S/4HANA system and the staging system (a remote system that uses the SAP HANA database).

* You have one or more CSV file (.csv) with data to upload or you have created a Zip file that contains your CSV files.

* You have reviewed and adjusted the CSV file options for the migration project you are currently working on.

****Note:**** For more details about prerequisites and other relevant information about Migrate Data Using Staging Tables see KBA [2733253](https://launchpad.support.sap.com/#/notes/2733253) – FAQ for SAP S/4HANA migration cockpit – Transfer option: Transfer data from staging tables.

**GENERAL REMARK:** Using CSV template files is an expert option for filling the staging ...
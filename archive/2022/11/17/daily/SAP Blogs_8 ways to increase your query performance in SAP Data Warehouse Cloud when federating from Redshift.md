---
title: 8 ways to increase your query performance in SAP Data Warehouse Cloud when federating from Redshift
url: https://blogs.sap.com/2022/11/16/8-ways-to-increase-your-query-performance-in-sap-data-warehouse-cloud-when-federating-from-redshift/
source: SAP Blogs
date: 2022-11-17
fetch_date: 2025-10-03T22:59:57.581794
---

# 8 ways to increase your query performance in SAP Data Warehouse Cloud when federating from Redshift

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* 8 ways to increase your query performance in SAP D...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161789&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [8 ways to increase your query performance in SAP Datasphere when federating from Redshift](/t5/technology-blog-posts-by-sap/8-ways-to-increase-your-query-performance-in-sap-datasphere-when-federating/ba-p/13561637)

![karishma_kapur90](https://avatars.profile.sap.com/f/2/idf27113e374f0f3499add64272c1f665e94dbd4154b9700fcfdc5468d2b99e71f_small.jpeg "karishma_kapur90")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[karishma\_kapur90](https://community.sap.com/t5/user/viewprofilepage/user-id/804676)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161789)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161789)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561637)

‎2022 Nov 16
9:09 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161789/tab/all-users "Click here to see who gave kudos to this post.")

4,293

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

**Background**

Data federation is the process of aggregating data from different sources into a virtual database. This allows data to be combined resulting in more insightful analytics and business intelligence. The key advantage with data federation is that the data isn't duplicated into another table but rather queried on the fly from the original source into a virtual table that is used for further analytics.

However, federating massive amounts of data can become time consuming. The query time for federation is not only long-delayed due to the source’s execution of the query, but also from the data transfer (latency) time from the source to SAP Datasphere. Here, I will state some features SAP Datasphere has to monitor performance, as well as go through some steps you can take to increase your federation query performance.

For this blog, I have used the [sample database](https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html) as provided by AWS Redshift, and uploaded the data as shown through AWS Redshift’s [Getting Started Guide](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html). To learn how to federate data from Redshift to SAP Datasphere, please refer to my former colleague’s blog, [Data Federation Between SAP Datasphere and Amazon Redshift](https://blogs.sap.com/2021/02/02/data-federation-between-sap-data-warehouse-cloud-and-amazon-redshift/).

**SAP Datasphere Performance Features**

SAP Datasphere provides several features and tools that monitor queries and streamline performance. These features are summarized below.

* [System Monitor](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/9f804b8efa8043539289f42f372c4862/28910cded17a42a0bf16225309cb8bf6.html). Monitor the performance of your system. You can see what tasks failed and dive deeper into the logs and view the statement that failed specifically.

* [Restrict Remote Table Data Loads](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/c8a54ee704e94e15926551293243fd1d/bd1ece5c9f78444c87708ef11eed0a31.html). Remove unnecessary columns and create filters. This will reduce the volume of data that is loaded in the remote table.

* Use the Data Builder to remove the unnecessary columns, define a central filter to load only the data that is needed, add new columns available in the source, or reinsert previously excluded columns.

* [Cloud Connector](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/be5967d099974c69b77f4549425ca4c0/e6b63f176d3640609adcf06297fb37e9.html#loio77cec6a1e8d04371a791658e641dc0d5) for SAP HANA on premise.

* [Run in Analytical mode](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/c8a54ee704e94e15926551293243fd1d/ce26fd3da31b414f9482292d3969340a.html)may improve view performance, particularly if a union is performed.

* [Remote Table Monitor](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/be5967d099974c69b77f4549425ca4c0/e4120bbb98e44994aa1e0b32ff3f209d.html). Create statistics for your remote table to improve query performance.

* [Remote Query Monitor](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/be5967d099974c69b77f4549425ca4c0/806d7f0c45a14f1fb07db0a226b2b822.html). Track queries sent to your source and analyze them.

* Activate the OLAP hint to view performance through a [graphical view](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/c8a54ee704e94e15926551293243fd1d/27efb479c4814252964d3fbc6ca2dfc3.html) or a [sql view](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/c8a54ee704e94e15926551293243fd1d/81920e4d583f45fd8761c662d3c8abab.html).

**Steps to increase query performance specific to Redshift federation**

**1.** Geographic Locations

First and foremost, it is important to note that the geographic locations of your SAP Datasphere instances and hyperscaler data sources matter. If the regions are the same, the latency (or data transfer) time is reduced, thereby increasing your query performance.

**2.** Select only the columns you need when writing your query.

When performing the following query:

`SELECT "salesid", "listid", "sellerid", "buyerid", "eventid", "dateid", "qtysold", "pricepaid", "commission", "saletime" FROM "sales_redshiftblog"`

As compared to this query:

`SELECT "listid", "qtysold", "commission", "dateid" FROM "sales_redshiftblog"`

The top query takes 1 second to complete in SAP Datasphere, whereas the second one takes 755 ms to complete.![](/legacyfs/online/storage/blog_attachments/2022/11/point2pic1.png)![](/legacyfs/online/storage/blog_attachments/2022/11/point2pic2-1.png)

In Redshift, the top query took 995 ms, and the second query took 464 ms.![](/legacyfs/online/storage/blog_attachments/2022/11/point2pic3.png)![](/legacyfs/online/storage/blog_attachments/2022/11/point2pic4.png)

As such, it is important to only query what you need, as time and space is wasted when you query columns that do not provide value to your use case.

**3.** Sortkeys and Distkeys

When using sortkeys and distkeys to define your table, it appears that queries run faster when these keys are in the list of columns to select.

For example, when running

`SELECT "salesid", "sellerid", "buyerid", "qtysold", "pricepaid", "commission", "saletime" FROM "sales_redshiftblog"`

The query takes 6 seconds to complete in SAP Datasphere and 6 seconds in Redshift.![](/legacyfs/online/storage/blog_attachments/2022/11/point3pic1.png)![](/legacyfs/online/storage/blog_attachments/2022/11/point3pic2.png)

However, when running

`SELECT "listid","qtysold","commission","dateid" FROM "sales_redshiftblog"`

The query takes 755 ms to complete in SAP Datasphere and 464 ms in Redshift.

![](/legacyfs/online/storage/blog_attachments/2022/11/point3pi...
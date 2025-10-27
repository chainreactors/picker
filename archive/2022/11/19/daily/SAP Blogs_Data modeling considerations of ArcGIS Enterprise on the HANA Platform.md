---
title: Data modeling considerations of ArcGIS Enterprise on the HANA Platform
url: https://blogs.sap.com/2022/11/18/data-modeling-considerations-of-arcgis-enterprise-on-the-hana-platform/
source: SAP Blogs
date: 2022-11-19
fetch_date: 2025-10-03T23:13:05.913602
---

# Data modeling considerations of ArcGIS Enterprise on the HANA Platform

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Data modeling considerations of ArcGIS Enterprise ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158495&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data modeling considerations of ArcGIS Enterprise on the HANA Platform](/t5/technology-blog-posts-by-sap/data-modeling-considerations-of-arcgis-enterprise-on-the-hana-platform/ba-p/13552077)

![tom_turchioe](https://avatars.profile.sap.com/d/9/idd9a3078344db18f94eea08d7feb02af94bf4502a9317dd7733a975900301adbd_small.jpeg "tom_turchioe")

[tom\_turchioe](https://community.sap.com/t5/user/viewprofilepage/user-id/324787)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158495)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158495)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552077)

‎2022 Nov 18
8:19 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158495/tab/all-users "Click here to see who gave kudos to this post.")

1,499

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [Utilities](https://community.sap.com/t5/c-khhcw49343/Utilities/pd-p/48826897347003784259801)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA multi-model processing](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520multi-model%2520processing/pd-p/ca0132d1-ba23-4d3c-a7ef-5bcbd1cf01a3)
* [SAP HANA Spatial](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Spatial/pd-p/de9a1528-5ec2-4e53-8fd1-65f670054c68)

* [Utilities

  Industry](/t5/c-khhcw49343/Utilities/pd-p/48826897347003784259801)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP HANA multi-model processing

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2Bmulti-model%2Bprocessing/pd-p/ca0132d1-ba23-4d3c-a7ef-5bcbd1cf01a3)
* [SAP HANA Spatial

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2BSpatial/pd-p/de9a1528-5ec2-4e53-8fd1-65f670054c68)

View products (5)

![](/legacyfs/online/storage/blog_attachments/2022/11/282833_GettyImages-615428378_2600-scaled.jpg)

Some of our asset intensive customers, like utilities, who are implementing ArcGIS on HANA with SAP ERP have asked me: how do the pieces fit together and where can I read about this in one place?

While the value that the HANA platform brings to ArcGIS Enterprise is based on the same capabilities that HANA has provided to our customers since it was released, integrating ArcGIS, HANA and S/4HANA are different enough that our customers are asking for a roadmap of some kind.  To help fill that gap, this is the first of a series of blogs that will help fill in those blanks on why integrating these two technology stacks delivers substantial value to our customers who utilize both platforms.

Let's take a look at some challenges of obtaining insight from data faced by any analyst whether or not ArcGIS Enterprise and S/4HANA are involved.  To obtain insight, data from different systems is traditionally copied to one place and put into a form where insight can be extracted from the data.  Techniques used to do this include pre-calculating aggregates in result tables and copying data from remote systems into a data warehouse of some kind.  ArcGIS admins are especially familiar with this because medium and large asset intensive business use ArcGIS publication geodatabases which are ArcGIS specific data warehouses that underpin an ArcGIS system of engagement.  The ArcGIS utility network changes this - that will be covered in another blog.

HANA has a number of capabilities that eliminate or mitigate these challenges.  For example, HANA is able to aggregate at high speed over large volumes of data on-the-fly.  This is because HANA has at its core a modern, columnar in-memory database.  HANA was also designed to avoid the need to replicate data.  But if needed, you can still replicate data using built in HANA capabilities.  The HANA platform makes it easy to connect to data, rather than collect it because HANA has data federation capabilities built in.  The key is these HANA capabilities reduce and/or eliminate the complexity and technical debt of ETL.  Remember that ETL was created in part to address shortcomings in disk based DBMSs like IO bottlenecks but at the same time introduces data latency, complexity and increased data footprint.

![](/legacyfs/online/storage/blog_attachments/2022/11/image001-2.png)

Figure 1: Schema on write with ETL

By eliminating the need for ETL, the analyst goes from a schema on write scenario (where the results and data available to them are fixed) to a schema on read scenario.  Because HANA holds data at the finest granularity, the analyst can aggregate on the fly and has access to all of the attributes.  Note in Figure 2, the Extract, Transform and Load steps are replaced by a Replicate step.  By simply replicating data into the HANA instance, there is no filtering (selection criteria) or other processing.  There's no need to map fields and define the target table(s).  It's a straight mapping from the source into the HANA instance which is much simpler than extraction, transformation and loading/mapping.

Having a schema on read scenario makes the analyst much more agile because they can simply ask a different question without having to modify, test and maintain ETL. This provides insight based on the latest state of the business, not on a snapshot some number of hours, days or weeks old.  For a utility, for example, this means they can understand the state of their network at that moment - where the demand is and who is producing power (i.e. rooftop solar) for instance.

![](/legacyfs/online/storage/blog_attachments/2022/11/image002-4.png)

Figure 2: Schema on read with finest level of granularity data loaded into HANA

You can utilize HANA's data federation capability called Smart Data Access to query data where it resides as shown in Figure 3 below.  In this case, you don't even need to load that data into HANA.  In either case, the analyst can change their analytical lens simply by modifying the information view (called a calculation view) and they can utilize the built in analytic engines in HANA as shown in Figures 2 and 3.

![](/legacyfs/online/storage/blog_attachments/2022/11/image003-3.png)

Figure 3: Schema on read with data federation (Smart Data Access)

These capabilities (and others) in the HANA platform provide the same value for spatial data and analytics provided by the ArcGIS Enterprise platform.  Spatial datatypes in HANA are first class citizens of the HANA platform - they are not an add-on and are treated like any other type of data that HANA can store and process.

Since you're reading this blog, you are most likely either in the process of implementing or on the path to SAP S/4HANA for your ERP system.  You may also be ...
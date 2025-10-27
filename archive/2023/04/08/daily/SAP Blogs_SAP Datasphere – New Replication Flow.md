---
title: SAP Datasphere – New Replication Flow
url: https://blogs.sap.com/2023/04/07/sap-datasphere-new-replication-flow/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:12.992681
---

# SAP Datasphere – New Replication Flow

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Datasphere – New Replication Flow

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164380&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere – New Replication Flow](/t5/technology-blog-posts-by-sap/sap-datasphere-new-replication-flow/ba-p/13569993)

![Mastan](https://avatars.profile.sap.com/b/e/idbe3fcd0b19c57cabff6cafed86dff17a0ebb658b10a5cfdd735c074a9cda2b83_small.jpeg "Mastan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Mastan](https://community.sap.com/t5/user/viewprofilepage/user-id/150362)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164380)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164380)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569993)

‎2023 Apr 07
9:15 PM

[32
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164380/tab/all-users "Click here to see who gave kudos to this post.")

37,679

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

In this article, we’ll take a look at one of the new features of SAP Datasphere which is **New Replication Flow**.

**Background:**

We already know replication capability is available in SAP Datasphere with Smart Data Integration (SDI) and SAP is not going to remove it. With the **"New Replication Flow",** SAP Basically bring in a new cloud-based replication tool. This cloud-based data replication tool is designed to simplify data integration processes by eliminating the need for additional on-premises components. This means that it does not rely on DP-Server/DP-Agent technology which requires installation and Maintenace but instead uses the Data Intelligence Embedded environment and Data Intelligence Connectors to connect to remote sources.

**User Interface:**

When it comes to the user experience, it also has been integrated and inbuilt into the existing data builder and the same comes with the monitoring features, the replication flow monitoring into the existing data integration monitor where users already find as of today the monitoring for the data flows.

**When to use replication flow?**

If you want to copy multiple data assets from the same source to the same target in a fast and easy way and do not require complex projections.

One thing we need to keep in mind is that replication flows will copy only certain source objects which are mentioned below.

+ CDS views (in ABAP-based SAP systems) that are enabled for extraction.

+ Tables that have a unique key (primary key)

+ Objects from ODP providers, such as extractors or SAP BW artifacts

The New Replication Flow also supports delta load along with the initial load. As of now, it supports minutes and hour-based scheduling, which means the delta load occurs based on the specified time frame, capturing and replicating changes from the selected source to the target. These capabilities will be further extended.

![Replication delta.png](/t5/image/serverpage/image-id/80327i71193CA15EADC838/image-dimensions/327x311?v=v2 "Replication delta.png")

Please find the details here: [Load Type](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/3f5ba0c5ae3944c1b7279bb989a2a5b5.html)

**Use case and overview comparison:**

![](/legacyfs/online/storage/blog_attachments/2023/04/Comparision-between-RF-and-DF.png)

**Overview of Connectivity:**[**SAP HELP – Connection Types Overview**](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/eb85e157ab654152bd68a8714036e463.html#loioeb85e157ab654152bd68a8714036e463__section_connection_overview)

   On the source system side

+ SAP S4HANA Cloud or S4HANA on-premises, where we mainly talk about CDS Views extraction.

+ SAP ECC or Business Suite systems that we connect via SLT for mainly table-based extraction and the DMIS add-on will be installed (DMIS add-on is kind of a requirement that we need that brings in all the prerequisites into the SAP system that we need as a framework or a foundation to be able to use the replication flows).

+ SAP BW and BW/4HANA integration (We have different data assets that can be exposed via ODP, like ADSOs, DSOs and so on)

+ SAP HANA Cloud as well as HANA on-premises.

+ Non-SAP source which is Azure Microsoft SQL database that we can use as a source.

    On the Target system side

+ SAP Datasphere.

+ Standalone HANA on-premises and Standalone HANA cloud.

+ HANA Data Lake Files.

+ Google BigQuery

+ Google Cloud Storage

+ Amazon Simple Storage (AWS S3)

+ Azure Data Lake Generation 2

**With that lets jump into the scenario...**

In this scenario, I am going to use SAP HANA Cloud system as a source.

Let's see the connection creation with the source system.

+ Go the dedicated Datasphere space and click on "Go to connections".

+ Click on Create connection and you can see the list of connection types.

+ Click on information icon of SAP HANA Cloud connection, there you go... it supports Replication Flows

![](/legacyfs/online/storage/blog_attachments/2023/04/Connection-Type-2.png)

+ Select the connection and provide the information about the source system you have, that's it. You are good to go...

![](/legacyfs/online/storage/blog_attachments/2023/04/Connection-Creation-1.png)

Now, we will see how to create a **Replication Flow** in **SAP Datasphere**.

+ Jump into the **Data Builder** and click on **New Replication Flow**.

![](/legacyfs/online/storage/blog_attachments/2023/04/New-Replication-Flow.png)

**Note:** If you don’t find the "New Replication flow", Please Check whether you have “SAP Datasphere Integrator” role assigned to your user.

+ To choose the source for replication click on the "**Select Source Connection**" which indeed shows the connections created in your Datasphere space.

![](/legacyfs/online/storage/blog_attachments/2023/04/Source-Connection-Selection.png)

+ Here, I am going to connect to a HANA Cloud system from where I am going to consume tables. So, select the connection and continue.

![](/legacyfs/online/storage/blog_attachments/2023/04/Connection-Name.png)

+ The next thing is you need to choose "**Source container**". Container is like a root path of target file. (For example: In case of a database, it's the database schema)

![](/legacyfs/online/storage/blog_attachments/2023/04/Select-Source-Container.png)

+ Here, I am selecting the container so that it will show the list of tables within the system.

![](/legacyfs/online/storage/blog_attachments/2023/04/Container-selection-1.png)

+ The final thing in setting up the source system is we need to select the source objects from the path we provided in the previous step for that click on the "**Add Source Objects**" and choose the tables that you want and click on Next.

![](/legacyfs/online/storage/blog_a...
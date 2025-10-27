---
title: Data Federation Between SAP Data Warehouse Cloud and Azure Synapse
url: https://blogs.sap.com/2022/11/23/data-federation-between-sap-data-warehouse-cloud-and-azure-synapse/
source: SAP Blogs
date: 2022-11-24
fetch_date: 2025-10-03T23:38:39.214796
---

# Data Federation Between SAP Data Warehouse Cloud and Azure Synapse

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Data Federation Between SAP Datasphere and Azure S...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158363&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data Federation Between SAP Datasphere and Azure Synapse](/t5/technology-blog-posts-by-sap/data-federation-between-sap-datasphere-and-azure-synapse/ba-p/13551764)

![karishma_kapur90](https://avatars.profile.sap.com/f/2/idf27113e374f0f3499add64272c1f665e94dbd4154b9700fcfdc5468d2b99e71f_small.jpeg "karishma_kapur90")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[karishma\_kapur90](https://community.sap.com/t5/user/viewprofilepage/user-id/804676)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158363)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158363)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551764)

‎2022 Nov 23
8:13 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158363/tab/all-users "Click here to see who gave kudos to this post.")

12,869

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

**Background**

With data being spread across multiple hyperscalers, it becomes hard to derive insights on your combined data sources. However, SAP Datasphere bridges this gap through data federation. Data federation is the process of aggregating data from different sources into a virtual database. As a result, SAP’s Datasphere provides customers and users the ability to federate their data from different sources in real time into virtual tables in SAP Datasphere without duplicating the data. This allows data to be combined resulting in more insightful analytics and business intelligence.

**Goal and Architecture**

In this blog, I will show you how to federate your data from Azure Synapse into SAP Datasphere using SAP HANA® smart data integration data provisioning agent and the MSSQL Log Reader Adapter. I will also show you how you can leverage SAP Datasphere’s analytical capabilities to derive useful insights through SAP Analytics Cloud.

![](/legacyfs/online/storage/blog_attachments/2022/11/AzureSynapseFederationARD_DatasphereUpdate-1.png)

Azure Synapse Federation ARD

**Pre-requisite Steps to Integrate Azure Synapse with SAP Datasphere**

The prerequisites for this connection are as follows. You will need:

* to [download and install](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/9f804b8efa8043539289f42f372c4862/f1a39d1a763e48c8872f45c110a5a4e2.html) the latest SAP HANA® smart integration data provisioning agent on a machine with a Linux operating system,

* an [Azure Synapse Workspace](https://learn.microsoft.com/en-us/azure/synapse-analytics/get-started-create-workspace) properly set up,

* a SQL Pool (either [dedicated](https://learn.microsoft.com/en-us/azure/synapse-analytics/get-started-analyze-sql-pool) or [serverless](https://learn.microsoft.com/en-us/azure/synapse-analytics/get-started-analyze-sql-on-demand)), and

* [tables](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-azure-sql-data-warehouse?view=aps-pdw-2016-au7) created in Azure Synapse.

**Steps to Integrate Azure Synapse with SAP Datasphere**

1. Create an on-premise agent in SAP Datasphere.

   * In SAP Datasphere, you will first need to navigate to the on-premise agent screen through the System -> configuration tab.

     + ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture1-1-1.png)

   * Then you will need to click on the plus (+) tile to create a new on-premise agent.

     + ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture1-2-1.png)

   * After clicking on the +, it will ask you for an agent name. Please provide an agent name here. After clicking create, the agent settings will appear. Please take note of the agent name, HANA server, port number, HANA user name for agent messaging, and the HANA user password for agent messaging.

     + If you have lost the password, you can open the settings for the on-premise agent using the three dots on the agent’s tile, and then click on request new password and a new one will be provided to you.

2. Gather the Azure Synapse Information Needed for the Connection

   * In the Azure Portal, navigate to the Azure Synapse Workspace. Please open the Workspace web URL.

     + ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture2-1-1.png)

   * Once you’re in the Workspace Studio, please go to the Manage Tab and click on SQL Pools.

     + ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture2-2-1.png)

   * Please click the pool for which you want to federate data from. This will open up the pool’s properties.

     + Change connection strings to JDBC (SQL authentication) and note down the connection string it gives you.

       - ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture2-3-1.png)

3. Now we need to [create](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/sql-authentication?tabs=provisioned) an SQL Database contained database user.

   * Open up the Develop tab in Synapse Studio.

   * Create a new SQL script and make sure you are connected to the correct SQL Pool you want to use.

   * While connected to the master database, please perform the following command.

     + ```
       CREATE LOGIN <username here> WITH PASSWORD = '<your password here>';
       ```

     + ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture3-1-1.png)

   * Next, create a new SQL script and connect to the database for which you want access to in SAP Datasphere and perform these commands:

     + ```
       CREATE USER <username here> FROM LOGIN <username here>;
       ```

     + ```
       GRANT CONTROL ON DATABASE::<database name> to <username here>;
       ```

     + ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture3-2-1.png)

4. [Download](https://learn.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server?view=sql-server-ver16) the Microsoft JDBC Driver and copy it into the <DPA\_install\_dir>/lib folder on the SAP HANA® smart data integration data provisioning agent’s server.

   * ![](/legacyfs/online/storage/blog_attachments/2022/11/Picture4-1-2.png)

5. Set up the connection to SAP Datasphere using the DPA’s configuration tool.

   * Navigate to the <DPA\_install\_dir>/bin folder and run:

     + ```
       ./agentcli.sh –-configAgent
       ```

   * Enter the number corresponding to ‘SAP HANA Connection” and then the number corresponding to “Connect to SAP Datasphere via JDBC”

   * It will then ask you for the agent name, host name, port, HANA user name for agent messaging, and the HANA user password for agent messaging that we noted down earlier. For “Use encrypted JDBC connection”, I have entered true and for “Use Proxy Server” I have entered false.

     + ![](/legacyfs/onl...
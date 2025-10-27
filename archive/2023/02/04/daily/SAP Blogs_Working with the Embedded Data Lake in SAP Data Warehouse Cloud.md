---
title: Working with the Embedded Data Lake in SAP Data Warehouse Cloud
url: https://blogs.sap.com/2023/02/03/working-with-the-embedded-data-lake-in-sap-data-warehouse-cloud/
source: SAP Blogs
date: 2023-02-04
fetch_date: 2025-10-04T05:40:33.805652
---

# Working with the Embedded Data Lake in SAP Data Warehouse Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Working with the Embedded Data Lake in SAP Datasph...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164289&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Working with the Embedded Data Lake in SAP Datasphere](/t5/technology-blog-posts-by-sap/working-with-the-embedded-data-lake-in-sap-datasphere/ba-p/13569701)

![s_morio](https://avatars.profile.sap.com/e/2/ide2a8c151d533e67c477c6fbdf26766b9ec2aed33e14c4cff896ba9434abfa84f_small.jpeg "s_morio")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[s\_morio](https://community.sap.com/t5/user/viewprofilepage/user-id/758732)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164289)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164289)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569701)

‎2023 Feb 03
7:08 PM

[26
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164289/tab/all-users "Click here to see who gave kudos to this post.")

15,299

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

In this blog post you will learn how to realize a Cold-To-Hot data tiering scenario in SAP Datasphere and the embedded SAP HANA Cloud data lake. In this scenario, data will be loaded from a S3 Bucket in AWS into the SAP HANA Cloud data lake using a Data Flow in SAP Datasphere. Part of this data will then be snapshotted and stored as hot in-memory data. The Hot-To-Cold scenario will be covered in a different blog.

![](/legacyfs/online/storage/blog_attachments/2023/01/data-tiering-scenario-1.png)

Fig. 1: Data Tiering Scenarios

The figure below shows the overall approach for this scenario. First, we will create a new table in the SAP HANA Cloud data lake and a SAP HANA Cloud virtual table which is mapped to that table. The virtual table is used in SAP Datasphere to insert the S3 data into the data lake. Once the data is inserted four views are created one of which contains snapshotted in-memory data. These views will then be consumed by SAP Analytics Cloud to visualize the data and show performance differences in query times. In this example, space names such as “UK\_SPACE” are used, however, feel free to set the space names according to your naming convention.

![](/legacyfs/online/storage/blog_attachments/2023/01/architecture3-6.png)

Fig. 2: Architecture Overview

The following steps will guide you through the scenario to set up a Cold-To-Hot data tiering scenario in SAP Datasphere:

1. As a first step, the embedded Data Lake in flexible tenant configuration needs to be configured. Check out more in the following [blog.](https://blogs.sap.com/2022/02/18/configure-the-size-of-your-sap-data-warehouse-cloud-tenant/)

2. Next, a space needs to be selected that connects to the embedded Data Lake. This can be done in the Space Management in the Overview Tab. Here the checkbox “Use this space to access the data lake” needs to be activated. Note that only one space can be assigned to access the SAP HANA Cloud data lake.

![](/legacyfs/online/storage/blog_attachments/2023/02/space_management.png)

Fig. 3: Space Management

3. A database user needs to be created so that you can access the underlying SAP HANA Cloud database and create the tables. This option can also be found in the Space Management. Create a new database user with read & write privileges and click on “Save”.

![](/legacyfs/online/storage/blog_attachments/2023/01/database_user-1.png)

Fig. 4: Create a database user

4. Once this is done you can use your preferred SQL tool to create tables in the data lake and access those tables via SAP HANA virtual tables in your open SQL schema. In this blog, the SAP HANA Database Explorer will be used. It can directly be opened from the Space Management via “Open Database Explorer”. In the explorer click on the corresponding instance and enter your credentials to connect to the database.

5. SAP Datasphere offers two stored procedures that you can use to easily create and access the tables. To create tables in the data lake you can use the stored procedure "DWC\_GLOBAL"."DATA\_LAKE\_EXECUTE". Now create a table in the data lake and make sure that the columns’ data types match to the respective S3 data you are going to use.

```
CALL "DWC_GLOBAL"."DATA_LAKE_EXECUTE"('CREATE TABLE UK_SALES_ACQUISITION (

    Location VARCHAR(40 char),

    Product VARCHAR(40 char),

    Time_ VARCHAR(8 char),

    Sales_Unit DECIMAL(9,1),

    Year VARCHAR(4 char)

)');
```

Edit 08/07/2023: The create statement was updated with 'char' at the end to ensure that the same semantics (character-length) are used in the SAP HANA Cloud virtual table and the embedded SAP HANA Cloud data lake. For more information, please have a look at the following [link](https://help.sap.com/docs/hana-cloud-data-lake/sql-reference-for-data-lake-relational-engine-sap-hana-db-managed/supported-data-types-when-using-create-table-statement-for-data-lake-relational-engine-sap-hana-db-managed-tables-e77d8889ae14496881ac55495b4262ea).

6. Next you can create a virtual table in your open SQL Schema that refers to the table in the data lake. This can be done with the following procedure:

```
CALL "DWC_GLOBAL"."DATA_LAKE_CREATE_VIRTUAL_TABLE"

	( VIRTUAL_TABLE_NAME => '0_UK_SALES_ACQUISITION',

      DATA_LAKE_TABLE_NAME => 'UK_SALES_ACQUISITION'

    );
```

7. Another important step is to grant the space in SAP Datasphere privileges to insert and update the virtual table. Otherwise, the data flow would not be able to insert data into the table. The following procedure will grant the space all privileges:

```
GRANT ALL PRIVILEGES on "AASPACE_W21_20220921#ONBOARDING"."0_UK_SALES_ACQUISITION"

to AASPACE_W21_20220921 with grant option
```

8. Now that the virtual table is created, you can go back to SAP Datasphere into your Space with data lake access and create a data flow. To choose the S3 Bucket go to “Sources” -> “Connections” and to your S3 connection. Choose your source file from the S3 bucket and drop it into the canvas of the data flow.

9. The virtual table previously created in the open SQl schema is also available in the sources panel. Drag and drop it onto the canvas of the data flow and click on import and deploy to make it useable as a native SAP Datasphere artefact.

![](/legacyfs/online/storage/blog_attachments/2023/01/connections_virtual_table-2.png)

Fig. 5: Add the virtual table to the canvas

Also make sure that it is connected to the source S3 data. A projection node is inserted into the data flow to filter and remove columns that are not needed. In this example, Location, Time, Product and the KPI sales unit are retained. Also, a calculated column Year is created to make it easier to filter on different time periods.

![](/legacyfs/online/s...
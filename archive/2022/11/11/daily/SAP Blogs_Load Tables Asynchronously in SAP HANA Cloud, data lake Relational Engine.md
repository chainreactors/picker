---
title: Load Tables Asynchronously in SAP HANA Cloud, data lake Relational Engine
url: https://blogs.sap.com/2022/11/10/load-tables-asynchronously-in-sap-hana-cloud-data-lake-relational-engine/
source: SAP Blogs
date: 2022-11-11
fetch_date: 2025-10-03T22:22:36.191992
---

# Load Tables Asynchronously in SAP HANA Cloud, data lake Relational Engine

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Load Tables Asynchronously in SAP HANA Cloud, data...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163947&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Load Tables Asynchronously in SAP HANA Cloud, data lake Relational Engine](/t5/technology-blog-posts-by-sap/load-tables-asynchronously-in-sap-hana-cloud-data-lake-relational-engine/ba-p/13568504)

![former_member804450](https://avatars.profile.sap.com/former_member_small.jpeg "former_member804450")

[former\_member804450](https://community.sap.com/t5/user/viewprofilepage/user-id/804450)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163947)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163947)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568504)

‎2022 Nov 10
9:10 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163947/tab/all-users "Click here to see who gave kudos to this post.")

1,245

* SAP Managed Tags
* [SQL](https://community.sap.com/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA Cloud, data lake](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520data%2520lake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)

* [SQL

  Programming Tool](/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA Cloud, data lake

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2Bdata%2Blake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)

View products (4)

**Overview of the blog:**

It is common to load data into HANA Cloud, Data Lake. Loads can also take a long time, and because they run through a database connection, it can be tedious to keep an open DBX (or client application) session to facilitate a long-running load from object storage.

A built-in event scheduler in SAP HANA Cloud, data lake relational engine can be used to schedule SQL functionality. Through this blog you will learn how to schedule data movement from a SAP HANA Cloud, HANA database to a SAP HANA Cloud, data lake relational engine instance using this event scheduler.

Let's walkthrough the entire process from the Data Prep to the EVENT creation to Load Tables Asynchronously in HANA Cloud, data lake Relational Engine.

First step over here will be to import data into the SAP HANA Cloud, HANA Database. The primary step over here is to directly Import the TPCH data.csv file from [this](https://github.com/SAP-samples/hana-cloud-relational-data-lake-onboarding/blob/main/TPCH/customer.tbl) GitHub repository.

**Step 1: Download the TPCH CUSTOMER DATASET from GitHub**

1. To IMPORT data into your HANA DB Instance/Tables start by downloading the TPCH data file from [this](https://github.com/SAP-samples/hana-cloud-relational-data-lake-onboarding/blob/main/TPCH/customer.tbl) GitHub repository. Once you click on the link, it will redirect you to the GitHub TPCH data file directory. We can directly download the file from there.

1. The **TPCH CUSTOMER Dataset** will be an example for this blog. Save the ***customer.tb***l file to ***customer.csv*** on your local machine.

![](/legacyfs/online/storage/blog_attachments/2022/11/image1-7.png)

**Step 2: Create Table in HANA and Import the Data**

Now, once the data file is downloaded. We need to create a Table in our HANA Database Instance. That’s where we will be importing the data into.

Open a SQL console to the HANA DB instance and create the following table. The following code will create a TPCH schema in the HANA DB instance and then create a CUSTOMER table within that schema.

```
CREATE SCHEMA TPCH;

CREATE TABLE TPCH.CUSTOMER (

C_CUSTKEY            integer                        not null,

C_NAME               varchar(25)                    not null,

C_ADDRESS            varchar(40)                    not null,

C_NATIONKEY          integer                        not null,

C_PHONE              varchar(15)                    not null,

C_ACCTBAL            decimal(15,2)                  not null,

C_MKTSEGMENT         varchar(10)                    not null,

C_COMMENT            varchar(117)                   not null,

primary key (C_CUSTKEY)

);
```

Once the table is created, right click on the HANA DB Instance and select on IMPORT Data.

![](/legacyfs/online/storage/blog_attachments/2022/11/image2-6.png)

On the **“Import Type”** page select **“Import Data From”**.

Proceed to the **“Import Source”** step. On the “Import Source” step select **“Local”** and then **uncheck** the “**File has header in first row”** box.

Then select the **“customer.csv”** file that was downloaded earlier.

![](/legacyfs/online/storage/blog_attachments/2022/11/image3-6.png)

On the **“Import Target”** step, select **“Add to an existing table”** and fill in the information for the TPCH.CUSTOMER table that was created.

![](/legacyfs/online/storage/blog_attachments/2022/11/image4-6.png)

We need to verify the table mapping and go to step 5 to finish the import. So, this is how we IMPORT data into the TPCH HANA DB TABLES.

**Step 3: Set up a Remote Server**

Next step is to  Set up a Remote Server from SAP HANA Cloud, data lake to SAP HANA Cloud, HANA Database. Making a remote server connection between HDLRE and the HDB instance containing the data you want to retrieve is the first step in setting up an HDLRE instance.

First, choose properties from the context menu when you right-click the HANA database in Database Explorer and copy the host value.

![](/legacyfs/online/storage/blog_attachments/2022/11/image5-8.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/image6-5.png)

Since we have already imported the data into our HANA database, we can proceed to preparing HDLRE connection for Scheduling data movement. The below syntax will create a remote HANA server and through that we can Load the data into our HDRLE tables.

Use a SQL console that is connected directly to the HDLRE instance. Run this SQL against the HDLRE instance using a user with the **MANAGE ANY REMOTE SERVER** privilege to **Create Remote server**.

Notice, you are naming the remote server **HDBSERVER**. Replace the **<HANA Host Name>** with the host copied from the properties section.

```
CREATE SERVER HDBSERVER CLASS 'HANAODBC'

USING

'Driver=libodbcHDB.so;

ConnectTimeout=0;

CommunicationTimeout=15000000;

RECONNECT=0;

ServerNode= <HANA Host Name>:443;

ENCRYPT=TRUE;

ssltruststore= <HANA Host Name>:443;

ssltrustcert=Yes;'

DEFAULT LOGIN 'DBADMIN' IDENTIFIED BY 'Password1';
```

The CREATE SERVER Statement for Data Lake Relational Engine is documented here :[CREATE SERVER Statement for Data Lake Relational Engine | SAP Help P...
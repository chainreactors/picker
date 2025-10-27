---
title: Integrate Large Data Sets from Flat File to SAP HANA Cloud using SAP IS JDBC Adapter
url: https://blogs.sap.com/2023/02/21/integrate-large-data-sets-from-flat-file-to-sap-hana-cloud-using-sap-is-jdbc-adapter/
source: SAP Blogs
date: 2023-02-22
fetch_date: 2025-10-04T07:42:32.791022
---

# Integrate Large Data Sets from Flat File to SAP HANA Cloud using SAP IS JDBC Adapter

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Integrate Large Data Sets from Flat File to SAP HA...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163635&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrate Large Data Sets from Flat File to SAP HANA Cloud using SAP IS JDBC Adapter](/t5/technology-blog-posts-by-members/integrate-large-data-sets-from-flat-file-to-sap-hana-cloud-using-sap-is/ba-p/13571346)

![asoni](https://avatars.profile.sap.com/1/0/id10d770a58ad980f263fa30e9877f7bc431fa16d36516890a2e4d7f951d77048c_small.jpeg "asoni")

[asoni](https://community.sap.com/t5/user/viewprofilepage/user-id/115637)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163635)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163635)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571346)

‎2023 Feb 21
10:10 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163635/tab/all-users "Click here to see who gave kudos to this post.")

4,822

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)

* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)

View products (2)

## **Introduction:**

This blog post details a scenario in which data needs to be loaded from files from a demand and supply planning system into SAP HANA Cloud DB to build BI reports. The integration process should achieve the following high-level requirements:

1. A tab-delimited file with close to 2 million rows will be received via SFTP from the source system.

2. The staging table in SAP HANA Cloud DB should be truncated before loading the data.

3. The data should be loaded from the Tab-delimited flat file into the HANA table.

4. After the data is loaded, a stored procedure call should be initiated to take a snapshot of the data into another table that will be used for reporting.

While designing this integration process, there are a few things to consider. First, since there is a high number of rows in the incoming file, it is essential to split them into batches and run them in parallel to avoid the DB insert through the JDBC receiver from timing out or taking too long to respond. Second, the procedure call should be serialized and triggered only once all the data in the table is loaded. Finally, if the process takes longer than 15 minutes, the default lock timeout for the sender SFTP must be increased to avoid a duplicate run.

## **Pre-requisites:**

1. Create a JDBC user in SAP HANA Cloud through SAP HANA Cockpit -> User & Role Management -> User Management

2. Grant required roles for schema under which tables exist and Execute object privileges for the stored procedure also through SAP HANA Cockpit -> User & Role Management -> Privilege Management![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-97.png)

3. Create JDBC data source using JDBC user created above in SAP Integration Suite -> Manage Security -> JDBC MaterialJDBC URL: jdbc:sap://<SAP HANA Cloud host>:443/?encrypt=true![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-37.png)Refer - [JDBC for SAP HANA Cloud | SAP Help Portal](https://help.sap.com/docs/SAP_INTEGRATION_SUITE/51ab953548be4459bfe8539ecaeee98d/187a8e8c16e44fc1bae2bfee793ab7b9.html?locale=en-US&q=JDBC%20receiver%20) (Do not pass the databaseName property to be able to successfully connect to SAP HANA Cloud). You can refer to [JDBC Connection Properties | SAP Help Portal](https://help.sap.com/docs/SAP_HANA_CLIENT/f1b440ded6144a54ada97ff95dac7adf/109397c2206a4ab2a5386d494f4cf75e.html?locale=en-US&q=nonBlockingIO) for a full set of JDBC connection properties

## **Integration Process Flow:**

![](/legacyfs/online/storage/blog_attachments/2023/02/Integration-Design-Work-Area_2023-02-21_04-05-49.png)

Integration Process

1. **SFTP sender** channel polls for the file and picks it up for processing when available.

2. **Content Modifier**: backs up the incoming file name to be retrieved later in case of any exception.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture4-29.png)

3. **Parallel Multicast:** used to archive the incoming file on the internal server in one branch and to load the data to HANA in another branch.

4. **Content Modifier:** generates SQL for truncating the staging table and backs up the incoming dataset in the property variable to be retrieved later.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture6-19.png)![](/legacyfs/online/storage/blog_attachments/2023/02/Picture7-17.png)

5. **Request-Reply:** calls SAP HANA Cloud using JDBC receiver adapter for executing the SQL query constructed in the Content Modifier.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture8-14.png)

6. **Content Modifier:** sets a dummy payload to create two serialized processes once a success message is received from the JDBC call![](/legacyfs/online/storage/blog_attachments/2023/02/Picture9-12.png)

7. **Iterating Splitter:** configured with Line Break and parallel processing turned OFF to create two serialized sub-processes![](/legacyfs/online/storage/blog_attachments/2023/02/Picture10-12.png)

8. **Content Modifier:** creates a property for the body of the splitter dummy payload in the DBInsert or ProcedureCall branch. The reason for storing it in the property is because Router doesn’t allow to use of ${in.body} expression in the routing condition is required to branch both serialized processes to different branches.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture11-14.png)

9. **Router:** branch based on the between DBInsert & ProcedureCall subprocess.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture12-14.png)

10. **Content Modifier:** resets the original incoming file data (tab-delimited) from the property variable which was backed up in earlier steps.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture13-14.png)

11. **General Splitter:** splits the rows in tab files into multiple groups of 10k records, which can be executed in parallel using the maximum concurrent processes supported (50)![](/legacyfs/online/storage/blog_attachments/2023/02/Picture14-11.png)

12. **CSV to XML converter:** converts data in each split process into XML, which is used to map to insert structure for the database.![](/legacyfs/online/storage/blog_attachments/2023/02/Picture15-12.png)

13. **Message Mapping:** Message mapping is used to map the incoming data into the structure on the receiver side for data insert. Refer to SAP Help [Batch Payload and Operation | SAP Help Portal](https://h...
---
title: Optimizing SAP DB2 11.1 Performance: Running Offline Reorg, Runstats, and Reducing Tablespace
url: https://blogs.sap.com/2023/03/18/optimizing-sap-db2-11.1-performance-running-offline-reorg-runstats-and-reducing-tablespace/
source: SAP Blogs
date: 2023-03-19
fetch_date: 2025-10-04T10:02:15.995626
---

# Optimizing SAP DB2 11.1 Performance: Running Offline Reorg, Runstats, and Reducing Tablespace

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Optimizing SAP DB2 11.1 Performance: Running Offli...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160648&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Optimizing SAP DB2 11.1 Performance: Running Offline Reorg, Runstats, and Reducing Tablespace](/t5/technology-blog-posts-by-members/optimizing-sap-db2-11-1-performance-running-offline-reorg-runstats-and/ba-p/13553541)

![adil_fahim](https://avatars.profile.sap.com/5/3/id534bf7884320338037e2df3906ea3f03bfa95ab91db6b31730fa005b4215204e_small.jpeg "adil_fahim")

[adil\_fahim](https://community.sap.com/t5/user/viewprofilepage/user-id/276276)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160648)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160648)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553541)

‎2023 Mar 20
9:06 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160648/tab/all-users "Click here to see who gave kudos to this post.")

4,203

* SAP Managed Tags
* [IBM Db2 for Linux, UNIX, and Windows](https://community.sap.com/t5/c-khhcw49343/IBM%2520Db2%2520for%2520Linux%252C%2520UNIX%252C%2520and%2520Windows/pd-p/478365276179134788459108226555898)

* [IBM Db2 for Linux, UNIX, and Windows

  Database](/t5/c-khhcw49343/IBM%2BDb2%2Bfor%2BLinux%25252C%2BUNIX%25252C%2Band%2BWindows/pd-p/478365276179134788459108226555898)

View products (1)

As databases grow in size, it’s important to periodically reorganize and reduce the tablespaces to maintain performance and optimize storage. As an SAP BASIS consultant, Housekeeping/Cleanup is the essential part of his role which help SAP system to run smoothly and also increase the overall system performance The are some standard housekeeping jobs which you can schedule via SM36 however some table cleanup still requires which doesn’t come under standard procedure. That tables are which are related to Application Logs, SAP office documents, table changes record data etc. The cleanup of these table requires extra attention and with proper handling/procedure.

Let’s take an example of BALDAT(Application Logs) transparent table which is also associated with BALHDR(Header Table)

--------------------------------------------------------------------------------------------------------------------------------------

Update - Mar 28, 2023

We have deleted around 170 Million of records from BALDAT table and results are amazing by performing above steps -

Table Size - 480 GB (Before Reorg and Reduce)

Table Size - 68 GB (After Reorg and Reduce)

Reduce Help help us to reclaim the space at OS level and 400+ GB space has been added to /sapdata mount points back.

--------------------------------------------------------------------------------------------------------------------------------------

The first step is to get a approved retention period to perform any cleanup/housekeeping activity for your business system. This period value should be approved by your business and comes under SOX policy. let’s take an example that company need data for last 2 years(730 days) for current date.

SAP provide an standard job (SBAL\_DELETE) to cleanup the application logs which eventually decrease the count from BALHDR and BALDAT table both. Remember one thing while cleanup that it’s not mandatory that 1 header record in BALHDR table is associated to 1 record in BALDAT table. There must be 1 record(BALHDR) to many records(BALDAT) exists. This is the reason that the count and size of both tables are different and it’s a huge difference.

After running the cleanup job via SBAL\_DELETE for keeping the retention period of 730 days, you checked that table size is still same even though there is an feature of online REORG and RUNSTATS is already enabled in DB2. Now what next –

This requires an offline reorg of table which need a SAP system downtime. This feature is used to improve database performance by reorganizing tables, indexes, and other database objects. The Offline Reorg process involves four phases(Short, build, replace and Recreate all indexes). In build phase copying the data from the original tablespace to a system tablespace, which is then optimized for performance. This process can be time-consuming, especially for large databases but here is an catch, if you want to run offline reorg of any table suppose the current size of the table is 500GB and then there should be similar space available in tablespace container filesystem as this process is going to copy tablespace to temporary location.

To run an Offline Reorg in DB2 11.1, follow these steps:

**Take Approval & Shutdown your SAP system.**

Identify the tablespace you want to reorg (we need to check the BALDAT comes under which tablespace)

**db2 list tablespaces show detail | grep -i BALDAT**

other way to identify the tablespace by using the ***“syscat.tablespace”***

Restart the DB and keep the instance in quiesce mode

**db2 quiesce instance *INSTANCE\_NAME* immediate**

run the offline reorg on respective table

**db2 reorg table BALDAT**

The above process will take long time to complete (depend on size). once REORG activity get completed then trigger the RUNSTATS.

Runstats is a DB2 feature that updates statistics on tables and indexes. This feature is used to optimize the performance of SQL statements by providing the optimizer with accurate statistics about the data in the tables and indexes.

To run Runstats in DB2 11.1, follow these steps:

**db2 runstats on table BALDAT with distribution and detailed indexes all**

Above both commands run during downtime.

Now run the unquiesce command to release the DB for use.

**db2 unquiesce instance *INSTANCE\_NAME***

Once the above process get completed then we can proceed for reducing the tablespace, this is an uptime command and during this command, the system can be accessible. this feature will reduce the amount of space used by a tablespace and optimize database performance by freeing up space and reducing disk usage.

To reduce a tablespace in DB2 11.1, follow these steps:

Run the Tablespace Reduction command:

**db2 alter tablespace tablespace\_name reduce max**

The above process will take time to complete depend on your database and tablespace size. This will increase and boost your overall system performance and also release the space at OS level which is visible on sapdata mount points (df -h).

There are some PROS and CONS as well for the above activities which also need to consider before performing –

Offline Reorg –

Pros:
Improves performance by removing fragmentation in the table.
Improves storage efficiency by reclaiming unused space.
Can be run offline, without affecting the availability of the database.

Cons:
Requires enough free space in the tablespace container path to create a new copy of the table.
Can take a long time to complete, depending on the size of the table.

Runstats –

Pros:
Improves query performance by providing accurate statistics for the query optimizer to use.
Can ...
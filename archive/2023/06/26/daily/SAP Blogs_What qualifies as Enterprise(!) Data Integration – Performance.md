---
title: What qualifies as Enterprise(!) Data Integration – Performance
url: https://blogs.sap.com/2023/06/25/what-qualifies-as-enterprise-data-integration-performance/
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:46:00.514466
---

# What qualifies as Enterprise(!) Data Integration – Performance

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* What qualifies as Enterprise(!) Data Integration -...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163216&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What qualifies as Enterprise(!) Data Integration - Performance](/t5/technology-blog-posts-by-members/what-qualifies-as-enterprise-data-integration-performance/ba-p/13568413)

![werner_daehn](https://avatars.profile.sap.com/7/e/id7e55fc0a863a36761fa8ff89b580f1f72a58b0f895dbc09e4cc692747c73ebbe_small.jpeg "werner_daehn")

[werner\_daehn](https://community.sap.com/t5/user/viewprofilepage/user-id/182245)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163216)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163216)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568413)

‎2023 Jun 25
9:08 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163216/tab/all-users "Click here to see who gave kudos to this post.")

1,621

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (3)

Moving data from one system to another with some transformations is Data Integration. This is fine for ad hoc integrations but if such a pipeline is executed regularly and part of an entire ecosystem, I would add more requirements to a data integration process. Let's coin it Enterprise-grade Data Integration.

To make things more obvious, the task shall be very basic: Move data from a source database into a different target database. This can be achieved in multiple ways. Some examples:

1. Create a SQL select command, execute it, write the results to a file and import the file.

2. A Python script executing the SQL select row by row and and for each returned row, execute an insert statement into the target database.

3. If the source or target database allows to create a database link, meaning it can make remote tables appear as if they were local, an insert...select statement does the trick.

4. A script executed in an Apache Spark cluster.

5. Various ELT/ETL tools in general and SAPs Data Services (6), SAP Data Intelligence (onPrem 7a, cloud 7b), SAP Cloud Integration (8).

All of these methods (and countless more) do work. But the core quality of any Data Integration tool must be performance. It can't be that an initial load takes multiple days, and maybe even requires the source system to be locked for changes to guarantee consistent data, or a daily batch delta takes more than 24 hours. Unfortunately the volumes of data we deal with on a regular basis are vast enough to require the use of all techniques available to speed up the process.

### Some approximations the get a feel

Just imagine we must move a laughable 10 million rows and the batch window is graciously 4 hours long. That would require to move 694 rows/sec in average. Not an impressive amount but for some approaches the number might be challenging. I would be concerned about (1), (2), (8) from above list.

If we assume one row has 100 columns and the data must be converted from the SQL driver's format to an internal format and then to the target database driver's format, 2 billion conversions will  happen. But CPUs are fast, that should pose no problem. On the other hand, it is not nothing. Some string to datetime conversions, some column based transformations (ltrim?) and it can get tight for a single CPU quickly.

Let's further assume one column has an average width of 4 byte. Then a row is 4 bytes \* 100 columns = 400 bytes big. A single disk can process 500MB/s, then one disk can process 1.25 million rows per second. Nice. Even better, if that happens to be too slow, double the disks in a RAID setup will double the throughput.

Network is different, though. A standard local 1GBit Lan has a throughput of only 110MByte/sec. That means 275'000 rows/sec. Still okay. But the network is a shared media. If the data moves from the source database via a single network hop directly into the target database, we get the full 275'000 rows/sec. If the architecture is with a separate server running the integration, the network bandwidth is used for read and write, so the throughput would be half: 137'500rows/sec.

### Cloud integration software

Informatica deploy an agent on demand that is capable of performing the entire transformations without moving any data to the cloud and back. Most cloud integration tool however perform the transformation in the cloud, hence they must read and write from the source via the WAN network into the cloud center and back. A WAN connection will certainly be not with a distinct 1GBit cable between source-to-cloud-to-target. (2), (4), (7b) and (8) are of that kind and should be evaluated carefully in that regard.

### Data Integration in compute clusters

Things get even worse when a cluster is used and the architecture is such that each node does parts of the transformations. Say we have 10 nodes and 10 distinct steps. Then the reader node reads all rows - one network hop - hands over the data to the next node - one network hop - it performs transformation step number 2 and gives the data to the next node - one network hop - and .... the writer sends all data into the target - one network hop. In worst case, all data must pass the network 11 times and the overall performance would be 275'000/11 = 25'000rows/sec. (7) and maybe (4) if reshuffles happen.

If the software is designed badly, it happens that a cluster gets slower the larger it is and a single laptop would outperform the expensive solution. (7) is such a candidate.

### Conclusions

Frankly, the assumptions about the data volumes made are unrealistically low. Real projects will require to move ten times more data in a tenth of the time (24 minutes for 10m rows instead of 4hours).

But all of that is beside the point. There is not a single data integration project at a customer where the data movement is considered to be too quickly. The conclusion is hence, **the tool of choice must support every single optimization technique available** to maximize the performance.

These techniques are no rocket science and well known, yet for some reason not implemented by all data integration tools. It is your job to asses if your tool of choice supports all and how well and if you can live with the compromises.

### Techniques for maximum performance

1. As little **data conversions...
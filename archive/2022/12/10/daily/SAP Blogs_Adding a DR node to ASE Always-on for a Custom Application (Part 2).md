---
title: Adding a DR node to ASE Always-on for a Custom Application (Part 2)
url: https://blogs.sap.com/2022/12/09/adding-a-dr-node-to-ase-always-on-for-a-custom-application-part-2/
source: SAP Blogs
date: 2022-12-10
fetch_date: 2025-10-04T01:05:46.906756
---

# Adding a DR node to ASE Always-on for a Custom Application (Part 2)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Adding a DR node to ASE Always-on for a Custom App...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161047&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Adding a DR node to ASE Always-on for a Custom Application (Part 2)](/t5/technology-blog-posts-by-sap/adding-a-dr-node-to-ase-always-on-for-a-custom-application-part-2/ba-p/13559457)

![ChrisBaker](https://avatars.profile.sap.com/9/4/id94acce996b325f1d48459d6ff45f5b861ec7ec841c6fac3ea5e62915ecad19e3_small.jpeg "ChrisBaker")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ChrisBaker](https://community.sap.com/t5/user/viewprofilepage/user-id/189912)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161047)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161047)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559457)

‎2022 Dec 09
9:25 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161047/tab/all-users "Click here to see who gave kudos to this post.")

1,435

* SAP Managed Tags
* [SAP Adaptive Server Enterprise](https://community.sap.com/t5/c-khhcw49343/SAP%2520Adaptive%2520Server%2520Enterprise/pd-p/67837800100800005166)
* [SAP ASE - HADR Enablement](https://community.sap.com/t5/c-khhcw49343/SAP%2520ASE%2520-%2520HADR%2520Enablement/pd-p/223412072590469366196755173464619)

* [SAP Adaptive Server Enterprise

  SAP Adaptive Server Enterprise](/t5/c-khhcw49343/SAP%2BAdaptive%2BServer%2BEnterprise/pd-p/67837800100800005166)
* [SAP ASE - HADR Enablement

  Software Product Function](/t5/c-khhcw49343/SAP%2BASE%2B-%2BHADR%2BEnablement/pd-p/223412072590469366196755173464619)

View products (2)

(...continuing from [Part 1](https://blogs.sap.com/?p=1650773))

# Adding a database to the HADR cluster

Existing databases can be added to the HADR cluster for replication in one of 2 ways:

* Using the setuphadr response file to create the devices and database.

* Using the RMA command 'sap\_update\_replication' and 'sap\_materialize' commands.

The first method has already been demonstrated in Part 1 using the response file to add the <SID> database to the HADR cluster and DR node.

The steps to follow when adding a database are as follows:

1. a database first must be created or exist on the primary (active) node.

2. the database must be created on the standby (and DR nodes) and should be the same size as the primary.

3. as the master database is already being replicated, any addition of a new SUID for dbo will be replicated, but the changes to the dbo for the database must be run on each target database instance as well.

4. DR\_maint (already an SUID in master) must also be added as an alias for the database's **dbo per target instance**.  This is not done by .sap\_update\_replication' (below).

5. any changes to a database's options must also be run **per target instance**.

6. the database is added to the standby and dr nodes by running the 'sap\_update\_replication' RMA command.

7. the database must be materialized to the target instances by issuing separate 'sap\_materialize' RMA commands **per target instance**.

For example:

For step 1) and 2) above, the following commands are run on each instance - PRIMARY\_ASE, COMPANION\_ASE, DR\_ASE - using isql:

```
disk init name="tpccdata",physname="/data/ASE/data/tpccdata.dat",size="2048M"

go

disk init name="tpcclog",physname="/data/ASE/data/tpcclog.dat",size="2048M"

go

create database tpcc on tpccdata = "2048M" log on tpcclog = "2048M"

go

sp_dboption tpcc, 'trunc. log on chkpt.', true

go
```

with example output:

```
PRIMARY_ASE:

CREATE DATABASE: allocating 131072 logical pages (2048.0 megabytes) on disk 'tpccdata' (131072 logical pages requested).

CREATE DATABASE: allocating 131072 logical pages (2048.0 megabytes) on disk 'tpcclog' (131072 logical pages requested).

Processed 103 allocation unit(s) out of 1024 units (allocation page 143104). 10% completed.

Processed 205 allocation unit(s) out of 1024 units (allocation page 156160). 20% completed.

Processed 308 allocation unit(s) out of 1024 units (allocation page 169216). 30% completed.

Processed 410 allocation unit(s) out of 1024 units (allocation page 182272). 40% completed.

Processed 512 allocation unit(s) out of 1024 units (allocation page 66560). 50% completed.

Processed 615 allocation unit(s) out of 1024 units (allocation page 208384). 60% completed.

Processed 717 allocation unit(s) out of 1024 units (allocation page 92928). 70% completed.

Processed 820 allocation unit(s) out of 1024 units (allocation page 234240). 80% completed.

Processed 922 allocation unit(s) out of 1024 units (allocation page 247296). 90% completed.

Processed 1024 allocation unit(s) out of 1024 units (allocation page 261888). 100% completed.

Database 'tpcc' is now online.

Database option 'trunc. log on chkpt.' turned ON for database 'tpcc'.

Running CHECKPOINT on database 'tpcc' for option 'trunc. log on chkpt.' to take effect.

(return status = 0)

COMPANION_ASE:

CREATE DATABASE: allocating 131072 logical pages (2048.0 megabytes) on disk 'tpccdata' (131072 logical pages requested).

CREATE DATABASE: allocating 131072 logical pages (2048.0 megabytes) on disk 'tpcclog' (131072 logical pages requested).

Processed 103 allocation unit(s) out of 1024 units (allocation page 143104). 10% completed.

Processed 205 allocation unit(s) out of 1024 units (allocation page 156160). 20% completed.

Processed 308 allocation unit(s) out of 1024 units (allocation page 40192). 30% completed.

Processed 410 allocation unit(s) out of 1024 units (allocation page 53248). 40% completed.

Processed 512 allocation unit(s) out of 1024 units (allocation page 66304). 50% completed.

Processed 615 allocation unit(s) out of 1024 units (allocation page 208640). 60% completed.

Processed 717 allocation unit(s) out of 1024 units (allocation page 221696). 70% completed.

Processed 820 allocation unit(s) out of 1024 units (allocation page 105728). 80% completed.

Processed 922 allocation unit(s) out of 1024 units (allocation page 118784). 90% completed.

Processed 1024 allocation unit(s) out of 1024 units (allocation page 261888). 100% completed.

Database 'tpcc' is now online.

Database option 'trunc. log on chkpt.' turned ON for database 'tpcc'.

Running CHECKPOINT on database 'tpcc' for option 'trunc. log on chkpt.' to take effect.

(return status = 0)

DR_ASE:

CREATE DATABASE: allocating 131072 logical pages (2048.0 megabytes) on disk 'tpccdata' (131072 logical pages requested).

CREATE DATABASE: allocating 131072 logical pages (2048.0 megabytes) on disk 'tpcclog' (131072 logical pages requested).

Processed 103 allocation unit(s) out of 1024 units (allocation page 13824). 10% completed.

Processed 205 allocation unit(s) out of 1024 units (allocation page 26880). 20% completed.

Processed 308 allocation unit(s) out of 1024 units (allocation page 169472). 30% completed.

Processed 410 allocation unit(s) out of ...
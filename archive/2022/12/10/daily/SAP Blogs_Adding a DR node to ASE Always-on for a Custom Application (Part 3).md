---
title: Adding a DR node to ASE Always-on for a Custom Application (Part 3)
url: https://blogs.sap.com/2022/12/09/adding-a-dr-node-to-ase-always-on-for-a-custom-application-part-3/
source: SAP Blogs
date: 2022-12-10
fetch_date: 2025-10-04T01:05:49.856490
---

# Adding a DR node to ASE Always-on for a Custom Application (Part 3)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Adding a DR node to ASE Always-on for a Custom App...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164050&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Adding a DR node to ASE Always-on for a Custom Application (Part 3)](/t5/technology-blog-posts-by-sap/adding-a-dr-node-to-ase-always-on-for-a-custom-application-part-3/ba-p/13568841)

![ChrisBaker](https://avatars.profile.sap.com/9/4/id94acce996b325f1d48459d6ff45f5b861ec7ec841c6fac3ea5e62915ecad19e3_small.jpeg "ChrisBaker")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ChrisBaker](https://community.sap.com/t5/user/viewprofilepage/user-id/189912)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164050)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164050)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568841)

‎2022 Dec 09
9:25 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164050/tab/all-users "Click here to see who gave kudos to this post.")

1,621

* SAP Managed Tags
* [SAP Adaptive Server Enterprise](https://community.sap.com/t5/c-khhcw49343/SAP%2520Adaptive%2520Server%2520Enterprise/pd-p/67837800100800005166)
* [SAP ASE - HADR Enablement](https://community.sap.com/t5/c-khhcw49343/SAP%2520ASE%2520-%2520HADR%2520Enablement/pd-p/223412072590469366196755173464619)

* [SAP Adaptive Server Enterprise

  SAP Adaptive Server Enterprise](/t5/c-khhcw49343/SAP%2BAdaptive%2BServer%2BEnterprise/pd-p/67837800100800005166)
* [SAP ASE - HADR Enablement

  Software Product Function](/t5/c-khhcw49343/SAP%2BASE%2B-%2BHADR%2BEnablement/pd-p/223412072590469366196755173464619)

View products (2)

(...continuing from [Part 2](https://blogs.sap.com/?p=1655606))

# Dropping the DR node

Dropping the DR node can be done in 3 steps from the primary RMA:

1. Drop database replication to DR:

   ```
   1> sap_disable_replication Toronto, Offsite, tpcc

   2> go

    TASKNAME            TYPE              VALUE

    ------------------- ----------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------

    Disable Replication Start Time        Thu Dec 08 21:54:47 UTC 2022

    Disable Replication Elapsed Time      00:00:45

    DisableReplication  Task Name         Disable Replication

    DisableReplication  Task State        Completed

    DisableReplication  Short Description Disable the flow of Replication

    DisableReplication  Long Description  Successfully disabled Replication for database 'tpcc'. Please execute 'sap_enable_replication Toronto, Offsite, tpcc' to enable replication for database.

    DisableReplication  Task Start        Thu Dec 08 21:54:47 UTC 2022

    DisableReplication  Task End          Thu Dec 08 21:55:32 UTC 2022

    DisableReplication  Hostname          primarynode.openstack.na-ca-1.cloud.sap

   (9 rows affected)

   1>

   ​
   ```

2. Remove DR node from the HADR system:

   ```
   1> sap_update_replication remove Offsite

   2> go

    TASKNAME           TYPE              VALUE

    ------------------ ----------------- ---------------------------------------------------------------------------

    Update Replication Start Time        Thu Dec 08 21:57:52 UTC 2022

    Update Replication Elapsed Time      00:01:54

    UpdateReplication  Task Name         Update Replication

    UpdateReplication  Task State        Completed

    UpdateReplication  Short Description Update configuration for a currently replicating site.

    UpdateReplication  Long Description  Update replication request to remove host 'Offsite' completed successfully.

    UpdateReplication  Task Start        Thu Dec 08 21:57:52 UTC 2022

    UpdateReplication  Task End          Thu Dec 08 21:59:46 UTC 2022

    UpdateReplication  Hostname          primarynode.openstack.na-ca-1.cloud.sap

   (9 rows affected)

   ​
   ```

3. Clean up replication definitions to the DR host:

   ```
   1> sap_drop_host Offsite

   2> go

    TASKNAME    TYPE              VALUE

    ----------- ----------------- --------------------------------------------------------------------

    Drop Host   Start Time        Thu Dec 08 22:03:12 UTC 2022

    Drop Host   Elapsed Time      00:00:01

    DropHostApi Task Name         Drop Host

    DropHostApi Task State        Completed

    DropHostApi Short Description Drop the logical host from the environment.

    DropHostApi Long Description  Submission of the design change for a model property was successful.

    DropHostApi Task Start        Thu Dec 08 22:03:12 UTC 2022

    DropHostApi Task End          Thu Dec 08 22:03:13 UTC 2022

    DropHostApi Hostname          primarynode.openstack.na-ca-1.cloud.sap

   (9 rows affected)

   ​
   ```

The DR host is now removed from the HADR environment:

```
1> sap_status path

2> go

 PATH                  NAME                      VALUE                   INFO

 --------------------- ------------------------- ----------------------- ------------------------------------------------------------------------------------

                       Start Time                2022-12-08 22:03:50.498 Time command started executing.

                       Elapsed Time              00:00:00                Command execution time.

 London                Hostname                  companionnode           Logical host name.

 London                HADR Status               Standby : Inactive      Identify the primary and standby sites.

 London                Synchronization Mode      Synchronous             The configured Synchronization Mode value.

 London                Synchronization State     Inactive                Synchronization Mode in which replication is currently operating.

 London                Distribution Mode         Remote                  Configured value for the distribution_mode replication model property.

 London                Replication Server Status Active                  The status of Replication Server.

 Toronto               Hostname                  primarynode             Logical host name.

 Toronto               HADR Status               Primary : Active        Identify the primary and standby sites.

 Toronto               Synchronization Mode      Synchronous             The configured Synchronization Mode value.

 Toronto               Synchronization State     Synchronous             Synchronization Mode in which replication is currently operating.

 Toronto               Distribution Mode         Remote                  Configured value for the distribution_mode replication model property.

 Toronto               Replication Server Status Active                  The status of Replication Server.

 London.Toronto.DEM    State                     Suspended               Path is suspended (Replication Agent Thread). Transactions are not being replicated.

 London.Toronto.DEM    Latency Time...
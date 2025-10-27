---
title: Adding a DR node to ASE Always-on for a Custom Application (Part 1)
url: https://blogs.sap.com/2022/12/09/adding-a-dr-node-to-ase-always-on-for-a-custom-application-part-1/
source: SAP Blogs
date: 2022-12-10
fetch_date: 2025-10-04T01:05:52.953130
---

# Adding a DR node to ASE Always-on for a Custom Application (Part 1)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Adding a DR node to ASE Always-on for a Custom App...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158662&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Adding a DR node to ASE Always-on for a Custom Application (Part 1)](/t5/technology-blog-posts-by-sap/adding-a-dr-node-to-ase-always-on-for-a-custom-application-part-1/ba-p/13552569)

![ChrisBaker](https://avatars.profile.sap.com/9/4/id94acce996b325f1d48459d6ff45f5b861ec7ec841c6fac3ea5e62915ecad19e3_small.jpeg "ChrisBaker")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ChrisBaker](https://community.sap.com/t5/user/viewprofilepage/user-id/189912)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158662)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158662)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552569)

‎2022 Dec 09
9:25 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158662/tab/all-users "Click here to see who gave kudos to this post.")

4,044

* SAP Managed Tags
* [SAP Adaptive Server Enterprise](https://community.sap.com/t5/c-khhcw49343/SAP%2520Adaptive%2520Server%2520Enterprise/pd-p/67837800100800005166)
* [SAP ASE - HADR Enablement](https://community.sap.com/t5/c-khhcw49343/SAP%2520ASE%2520-%2520HADR%2520Enablement/pd-p/223412072590469366196755173464619)

* [SAP Adaptive Server Enterprise

  SAP Adaptive Server Enterprise](/t5/c-khhcw49343/SAP%2BAdaptive%2BServer%2BEnterprise/pd-p/67837800100800005166)
* [SAP ASE - HADR Enablement

  Software Product Function](/t5/c-khhcw49343/SAP%2BASE%2B-%2BHADR%2BEnablement/pd-p/223412072590469366196755173464619)

View products (2)

# **Introduction**

Currently we document creating an Always-on (HADR) environment for Custom and Business Suite applications [HADR Users Guide](https://help.sap.com/docs/SAP_ASE/6ca21b96f7cb456fabb2b32b2121a6ae/a6645e28bc2b1014b54b8815a64b87ba.html) and adding a 3rd node DR to a Business Suite Application  [HADR System with DR Node Users Guide](https://help.sap.com/docs/SAP_ASE/4bffede51dd7415680ec880c9bb63fd5/8a56f81106e94a80be3a1e4af17fa091.html), but in the latter document there is no section on "Adding a DR Node to an Existing Custom HA System".

My intention is to have such information added to the documentation in the future, but in the meantime, the purpose of this blog is to demonstrate how to do this with a custom system.

For a description and diagrams of HADR and HADR + 3rd node, I will point you to the following blog post [High Availability + Disaster Recovery (3 Node HADR) with SAP ASE 16.0 SP03](https://blogs.sap.com/2018/04/19/high-availability-disaster-recovery-3-node-hadr-with-sap-ase-16.0-sp03/). For this blog and examples, I will be using ASE 16.0 SP04PL03.

This blog of how to do this will be broken down into several sections:

* Installing and configuring a primary and companion node HADR configuration (Part 1)

* Adding the DR node (Part 1)

* Adding a database to the HADR cluster ([Part 2](https://blogs.sap.com/?p=1655606))

* Planned Failover ([Part 2](https://blogs.sap.com/?p=1655606))

* Planned Failback ([Part 2](https://blogs.sap.com/?p=1655606))

* Removing a database from the HADR cluster ([Part 3](https://blogs.sap.com/?p=1662268))

* Dropping the DR node ([Part 3](https://blogs.sap.com/?p=1662268))

The components of an HADR configuration are shown here:

![](/legacyfs/online/storage/blog_attachments/2022/11/HADR-2-node.png)

**HADR Cluster**

All components required for the HADR installation are provided with the SAP Adaptive Server Enterprise (ASE) installation media.  No additional

Adding the DR node as the third node allows a disaster recovery capability for the HADR cluster.  (Recovering the HADR cluster from the DR node is documented at [Recovering the HADR Cluster from the DR Node](https://help.sap.com/docs/SAP_ASE/38af74a09e48457ab699e83f6dfb051a/86f66867f99b4e7d8e2b9cd3443e86de.html)).![](/legacyfs/online/storage/blog_attachments/2022/11/HADR-3-node.png)

**HADR Cluster + 3rd node DR**

The Fault Manager (FM) and SAP Host Agent are only required on the HADR cluster as failover and failback is still only between the two instances of the HADR cluster.

As with the components shown in the first diagram, the DR node does have a Replication Management Agent (RMA) and SAP Replication Server (SRS) instance installed.

The addition of the DR node **does not require any additional SAP Replication Server license**.  The Replication Management Agent and SAP Replication Server instances will be configured when adding the DR node to an existing HADR cluster.

Failover, whether planned or unplanned, and failback, **do** take into account the presence of the DR environment and automatically switch the source of replication for the DR node database(s) to the active source database(s).

When configuring HADR + 3rd node, remember that all 3 ASE instances must be configured as follows:

* ASE sa passwords must match.

* RMA DR\_admin passwords must match.

* RMA DR\_maint passwords must match.

* master db must be the same size (this will be replicated).

* the <SID> database must be created on all instances.  This will be created automatically if using Method 1 (below).  If using Method 2 (below), the database can be created on the primary, companion and DR manually or by the setup\_hadr response file.

* server page size, character set and sort order must be the same.

# **Installing and configuring a primary and companion node HADR configuration**

There are 2 methods that I will document here for installing and configuring an HADR cluster:

* Install and build a new HADR cluster from the installation media

* Add HADR to an existing ASE primary instance

Regardless of the method chosen, the companion or standby node and the future DR node should be new ASE instances.  Existing instances cannot be used, primarily due to conflicts with possibly already created SUIDs.

Regardless of the method selected, the final HADR cluster built using either method can have a DR node added.

Also, user databases can be added to the HADR system during the HADR cluster creation or later via RMA commands.

To simplify things, the ASE installation directory is /opt/sybase/ASE while all the data devices for ASE, the data movement (DM) components (SRS) are under a /data folder as shown below.

```
/data

├── ASE

│   ├── data

│   └── dump

└── SRS

    ├── data

    └── ssd
```

Regardless of the method used, a Backup Server instance will be needed use by HADR.  (AMC also requires a Job Scheduler, so all open servers were created anyway).

## Method 1 - Install and build a new HADR cluster from the installation media

This method assumes no existing $SYBASE directory is installed on any node of the HADR cluster, but the installation media has been un-tarred and is available in an installation directory on both nodes that will participate in the HADR cluster.

Most of this is already ...
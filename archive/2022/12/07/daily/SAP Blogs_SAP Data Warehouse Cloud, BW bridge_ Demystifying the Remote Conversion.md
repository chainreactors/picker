---
title: SAP Data Warehouse Cloud, BW bridge: Demystifying the Remote Conversion
url: https://blogs.sap.com/2022/12/06/sap-data-warehouse-cloud-bw-bridge-demystifying-the-remote-conversion/
source: SAP Blogs
date: 2022-12-07
fetch_date: 2025-10-04T00:40:20.065942
---

# SAP Data Warehouse Cloud, BW bridge: Demystifying the Remote Conversion

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Datasphere, SAP BW bridge: Demystifying the Re...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163625&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere, SAP BW bridge: Demystifying the Remote Conversion](/t5/technology-blog-posts-by-sap/sap-datasphere-sap-bw-bridge-demystifying-the-remote-conversion/ba-p/13567584)

![fcapano](https://avatars.profile.sap.com/e/b/ideb9596130df35902247d3d5834567768903801f3e349d15814dc151f56f26415_small.jpeg "fcapano")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[fcapano](https://community.sap.com/t5/user/viewprofilepage/user-id/529798)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163625)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163625)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567584)

‎2022 Dec 06
10:13 PM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163625/tab/all-users "Click here to see who gave kudos to this post.")

12,426

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP BW/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520BW%252F4HANA/pd-p/73554900100800000681)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP BW/4HANA

  SAP BW/4HANA](/t5/c-khhcw49343/SAP%2BBW%25252F4HANA/pd-p/73554900100800000681)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

## Abstract

This blog intends to provide an overview about the end-to-end process of the Remote Conversion to SAP Datasphere, BW bridge. For a deep dive into the details of all activities involved, check our [*SAP Datasphere, SAP BW bridge* *Runbook*](https://www.sap.com/documents/2022/12/9c8eb576-527e-0010-bca6-c68f7e60039b.html) which contains practical examples, tips and recommendations based on experience with real customer projects.

## Overview

The Remote Conversion offers the possibility to transfer the metadata plus the business data from your on-premise BW system to a target BW system (also called receiver system), which can be a BW/4HANA or a BW SAP BW bridge system. The Remote Conversion to BW/4HANA is available since 2017 and now is also available for Datasphere, BW bridge.

The transfer of only the metadata is offered by the Shell Conversion. The metadata transfer is also part of the Remote Conversion process therefore we can say that the Shell Conversion of a subset of the Remote Conversion. Which option to use depends on some variables such as the scope definition, number of objects and data volume involved.

BW bridge is a feature of Datasphere and offers the possibility to use BW artifacts in SAP Datasphere. The ABAP Tenant (where the BW modeling happens) is integrated by its own space into SAP Datasphere The tables of the ABAP Tenant (e.g. ADSOs, InfoObjects) can be exposed as remote tables in the BW bridge Space of Datasphere and shared to be consumed by other spaces.

The BW bridge space has limitations and its main functionality is to expose the shared remote tables to other spaces. Data Flows, views, etc. using the remote tables can only be created in other spaces based on the shared remote tables.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-05-at-16.50.36.png)

Figure 1: Remote Conversion overview

There are some differences between the Shell and Remote Conversion in terms of the scope collection logic for the metadata transfer, especially because of the relationship and dependencies of the request management. When using the Remote Conversion, data and request Information need to be copied and converted from the sender into the receiver system (Request ID to TSN), therefore all objects on which a data request is touching become relevant for the scope collection in order to ensure consistency.

The metadata transfer converts object types (TLOGO). For example, Classical DSOs and InfoCubes to Advanced DSOs; PSAs to Advanced DSOs (depending on the data flow, it can be optional or mandatory); InfoPackages to DTPs.

![](/legacyfs/online/storage/blog_attachments/2022/12/pic2.png)

Figure 2: Metadata transfer

## Prerequisites

The Remote Conversion to SAP Datasphere, BW bridge is supported by the tooling from BW 7.3 (SP10 and higher) and BW/4HANA 2021 (SP00 and higher) releases. The DMIS add-on installation is required (not needed for the Shell Conversion).

For detailed information about pre-requisites and preparations, see: SAP Note [3141688](https://launchpad.support.sap.com/#/notes/3141688) - *Conversion from SAP BW or SAP BW/4HANA to SAP Datasphere, SAP BW Bridge.*

This note contains a .zip file (*SAP\_Bridge\_Transfer\_Note\_Analyzer\_YYYY-MM-DD.zip*) with .xml files for each scenario. There are 2 (two) for the Remote Conversion: 1 (one) for when the sender system is on BW 7.x and 1 (one) for when the sender system is on BW/4HANA.

![](/legacyfs/online/storage/blog_attachments/2022/12/pic3.png)

Figure 3: Note Analyzer .zip file

You should import one of these 2 files (depending on your sender system release) to the sender system by using the [Note Analyzer](https://help.sap.com/doc/b235b5bd94664d9986f721f049d72cbb/1.0/en-US/User_Guide_for_SAP_BW_Note_Analyzer.pdf) report (it is also included into the above .zip file).

The file *Source\_System\_for\_SAP\_BW4HANA\_YYYY-MM-DD.xml* is also required to be imported to the source systems which are connected to the sender system (e.g. ECC, SCM, etc.). This is required especially for ODP enablement of the DataSources (see SAP Notes [2481315](https://launchpad.support.sap.com/#/notes/2481315) and [2232584](https://launchpad.support.sap.com/#/notes/2232584))

The imported .xml files contain a list of notes which are required to be implemented to enable the Remote Conversion. It brings enhancements and corrections in a frequent manner therefore it is important and recommended to always have the latest version implemented.

Differently when the receiver system is on BW/4HANA on-premise, there is no .xml file to be imported to the receiver system as BW bridge is on cloud.

Differently when the receiver system is on BW/4HANA, backend access to BW bridge via SAP GUI is not possible for partners and customers. BW bridge objects and data flows are only accessible via Eclipse/HANA Studio (BWMT).

## Data Transfer Logic

For the business data transfer, programs are automatically generated for each table in scope, to select, transfer and insert the respective data into the receiver system. Cluster tables are used to control and manage the data transfer process.

![](/legacyfs/online/storage/blog_attachments/2022/1...
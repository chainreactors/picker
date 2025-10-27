---
title: Realtime (delta) Data Replication from SAP Analytics Cloud to BW/4 HANA
url: https://blogs.sap.com/2022/11/07/realtime-delta-data-replication-from-sap-analytics-cloud-to-bw-4-hana/
source: SAP Blogs
date: 2022-11-08
fetch_date: 2025-10-03T21:56:13.030893
---

# Realtime (delta) Data Replication from SAP Analytics Cloud to BW/4 HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Realtime (delta) Data Replication from SAP Analyti...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161338&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Realtime (delta) Data Replication from SAP Analytics Cloud to BW/4 HANA](/t5/technology-blog-posts-by-sap/realtime-delta-data-replication-from-sap-analytics-cloud-to-bw-4-hana/ba-p/13560594)

![zili_zhou](https://avatars.profile.sap.com/4/8/id48e987efd192d8959ed74e9dceae18dd14bafd5b97368185d29e5b319db3bca7_small.jpeg "zili_zhou")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[zili\_zhou](https://community.sap.com/t5/user/viewprofilepage/user-id/232650)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161338)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161338)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560594)

‎2022 Nov 07
5:52 PM

[38
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161338/tab/all-users "Click here to see who gave kudos to this post.")

23,311

* SAP Managed Tags
* [BW (SAP Business Warehouse)](https://community.sap.com/t5/c-khhcw49343/BW%2520%28SAP%2520Business%2520Warehouse%29/pd-p/242586194391178517100436979900901)
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)

* [BW (SAP Business Warehouse)

  Software Product Function](/t5/c-khhcw49343/BW%2B%252528SAP%2BBusiness%2BWarehouse%252529/pd-p/242586194391178517100436979900901)
* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)

View products (4)

# Motivation:

[updated on 27.11.2023 with common mistakes or tips in the customers' projects]

As planning data in SAC is often changed by business users, these changes need to be replicated to the target systems like BW/BPC, S/4 HANA or Data Warehouse Cloud. This is a feature highly demanded by many customers.

The [Data Export Service API i](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/74c0e8614a074faa981cf03232bd6b05/40528c71abe14ec5a8c2e72c2a584a29.html?state=DRAFT&q=data%20export%20service)s already GA in Q2.2022 with full data. With SAC QRC4 2022 the Data Export Service **Delta** feature will also be generally available without any delta toggle. Currently, if you are on a fast-track tenant, you can request the feature to be toggled on in your system. For further information please have a look at the [help](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/14cac91febef464dbb1efce20e3f1613/8bcc3e6217dc49939b4a28ea9f163cf7.html) document for the delta feature in this API.

This blog will focus on how to use BW/4 HANA (as target) integrated features (Smart Data Integration) to pull the delta data from SAC (source) using the Data Export Service. Please be aware that this in contrast to a live connection or an import connection where SAC is the target and BW is the source.

# Content

Architecture and Prerequisites

Steps

|  |  |  |
| --- | --- | --- |
| **Step** | **Actions** | **Purpose** |
| 1 | Install DP Agent and connect BW/4 to SAC | Prepare for the connections |
| 2 | Using SAC Planning model as BW source  -        Verification at HANA side  -        Create BW source system  -        Create Data Source  -        Understand the logic of changing data  -        Understand the logic of deleting data | Understand the delta logic from SAC to the replicated table at BW source |
| 3 | Setup BW data flow  -        Create an ADSO Z1DETADSO with  change log.  -        Create a DTP and simple mapping from data source to the ADSO  -        How changes at SAC side are reflected the ADSO Inbound Table, change log and Active Data | Understand the delta logic from replicated table to BW ADSO. |

FAQ

Further Links

Call for actions

# Architecture and Prerequisites:

Below is the architecture we are going to use. Compared to the way to use ABAP and the API to write to a specific table, the advantages are here 1) best to utilize the HANA artifacts and memory for the real-time replication with SDI technology; 2) No programing is required.

![](/legacyfs/online/storage/blog_attachments/2022/11/1.architeture.png)

Architecture

A DP Agent of version 2.5.3 or higher is necessary. It is recommended to use the latest DP Agent.

The target systems can be a BW/4HANA, DWC, or HANA on premise system (at time of publication of this article). Please check the latest [PAM HANA SDI](https://support.sap.com/content/dam/launchpad/en_us/pam/pam-essentials/TIP/PAM_HANA_SDI_2_0.pdf) to check the latest status if more target systems are supported.

![](/legacyfs/online/storage/blog_attachments/2022/11/2.SDI_PAM.png)

SDI CloudDataIntegrationAdapter PAM

# Steps 1: Install DP Agent and connect BW/4 to SAC

There is already blog introducing this. Please refer to this help about the details [how to install DP Agent](https://help.sap.com/docs/HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/44cedf222fa045d8a056175cf21054b7.html) and connect to the HANA system under BW/4: [Leverage the SAP Analytics Cloud Data Export Service to extract your planning data to SAP HANA, SAP ...](https://blogs.sap.com/2022/05/30/leverage-the-sap-analytics-cloud-data-export-service-to-extract-your-planning-data-to-sap-hana-sap-business-warehouse-and-sap-s-4hana/)

Important: If you do not change the DP Agent default setting, it only allows to use max 4 GB memory even DP Agent is installed on a machine with much larger memory.  We see this in general cause performance issues in many customer cases. Most of the cause, a small and medium DP Agent sizing will meet your requirement in this SAC--> BW integration.  Thus it is recommended to set DPAgent ini, parameter Xmx to at least 8192m or higher, Increase Xms to the same or similar number.

More details could be found in [SAP 2688382 - SAP HANA Smart Data Integration Memory Sizing Guideline](https://me.sap.com/notes/0002688382)

|  |  |  |  |
| --- | --- | --- | --- |
|  | SMALL | MEDIUM | LARGE |
| Use Case | A small scenario with:  ·       One source system  ·       Up to 40 tables  ·       A weighted table size category of S-M  ·       Federation (initial load) of tables balanced based on HANA target capacity  ·       Modification rate less than 1,500,000 records/hour  ·       *The example above fits here* | A midrange scenario with:  ·       Approximately 1-3 different source systems  ·       And/or up to 100 tables in ...
---
title: SAP Commissions – Smart Data Integration[SDI] – Part 6
url: https://blogs.sap.com/2023/03/25/sap-commissions-smart-data-integrationsdi-part-6/
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:42:48.842896
---

# SAP Commissions – Smart Data Integration[SDI] – Part 6

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions – ⚙️Smart Data Integration[SDI] –...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5566&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions – ⚙️Smart Data Integration[SDI] – Part 6](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-%EF%B8%8Fsmart-data-integration-sdi-part-6/ba-p/13546425)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5566)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5566)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13546425)

‎2023 Mar 25
8:05 AM

[4
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5566/tab/all-users "Click here to see who gave kudos to this post.")

1,972

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)
* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)

View products (2)

Dear All,

This article is intended for database admins, consultants, customers & partners to know the basics & understanding of **available Standard Adapters and Custom Adapter details** for your SDI Project Implementation.

# Configure your own Data Provisioning Adapters![](/legacyfs/online/storage/blog_attachments/2023/03/cfc4d4a2304b3f527e3453012f320213.png)

Data provisioning adapters can connect to a variety of sources to move data into SAP HANA, and well as other use cases.

---

Also keep watching What's new where regular new updates keeps rolling in ...

**[What's New](https://help.sap.com/doc/ee97e2a15c194511bfb854740dbb6f80/2.0_SPS06/en-US/882edc1db9f64d9da75589dc187107bf.html) in SAP HANA Smart Data Integration and SAP HANA Smart Data Quality**

![](/legacyfs/online/storage/blog_attachments/2023/03/2023-03-25_09-02-41.png)

---

## See the Product Availability Matrix for information about supported versions.

The adapters in the following table are delivered with the **Data Provisioning Agent.**

Adapter Name Description

|  |  |
| --- | --- |
| ABAPAdapter | Retrieves data from virtual tables through RFC for ABAP tables and ODP extractors. It also provides change data capture for ODP extractors. |
| AgentMgmtAdapter | Allows SAP HANA to access and execute Data Provisioning Agent functions. |
| ASELTLAdapter | Retrieves data from SAP ASE. It can also receive changes that occur to tables in real time. You can also write back to a virtual table. The ASELTLAdapter uses LTL technology exclusively. |
| ASELTLECCAdapter | Retrieves data from an SAP ERP system running on SAP ASE. The ASELTLECCAdapter uses LTL technology exclusively. The only difference between this adapter and the ASELTLAdapter is that this adapter uses the data dictionary in the SAP ERP system when browsing metadata. |
| BWAdapter | This adapter is available for use only with SAP Agile Data Preparation.   **Note**  This adapter is deprecated and will be removed in a future release. |
| CamelAccessAdapter | Retrieves data from a Microsoft Access source. The Camel Access adapter is a predelivered component that is based on the Apache Camel adapter. |
| CamelFacebookAdapter | The Camel Facebook adapter is a predelivered component that is based on the Apache Camel adapter. Use the Camel Facebook component to connect to and retrieve data from Facebook. |
| CamelInformixAdapter | Retrieves data from an Informix source. It can also write back to an Informix virtual table. The Camel Informix adapter is a predelivered component that is based on the Camel adapter. |
| CamelJdbcAdapter | The Camel JDBC adapter is a predelivered component that is based on the Apache Camel adapter.  Use the Camel JDBC adapter to connect to most databases for which SAP HANA smart data integration doesn’t already provide a predelivered adapter.  In general, the Camel JDBC adapter supports any database that has SQL-based data types and functions, and a JDBC driver. |
| CassandraAdapter | Retrieves data from an Apache Cassandra remote source. You can also write to an Apache Cassandra target. |
| CloudDataIntegrationAdapter | Use the Cloud Data Integration adapter to retrieve data from a Cloud Data Integration (CDI) service endpoint. |
| DataAssuranceAdapter | Use the Data Assurance adapter to connect to an SAP HANA remote source to use the Data Assurance option to monitor the quality of data replication. |
| DB2ECCAdapter | Retrieves data from an SAP ERP system running on IBM DB2. It can also receive changes that occur to tables in real time. The only difference between this adapter and the DB2LogReaderAdapter is that this adapter uses the data dictionary in the SAP ERP system when browsing metadata. |
| DB2LogReaderAdapter | Retrieves data from IBM DB2. It can also receive changes that occur to tables in real time. You can also write back to a virtual table. |
| DB2LTLMainframeAdapter | Similar to the SDIDB2MainframeLogreaderAdapter, this adapter provides real-time replication functionality for DB2 for z/OS sources. This adapter uses LTL technology exclusively. |
| DB2MainframeLogreaderAdapter | Retrieves data from IBM DB2 for z/OS. IBM DB2 iSeries, formerly known as AS/400, is also supported. **Note**   The DB2MainframeLogreaderAdapter is deprecated and will be removed in a future release. To connect to ASE remote sources, see the DB2LTLMainframeAdapter, which uses Logging Transferring Language (LTL) exclusively. |
| ExcelAdapter | Retrieves data from Microsoft Excel.  You can also access SharePoint source data. |
| FileAdapter | Retrieves data from formatted text files. You can also write back to a virtual table.  You can also access SharePoint source data, as well as write to an HDFS target file. |
| FileAdapterDatastore  SFTPAdapterDatastore | File datastore adapters use the SAP Data Services engine as the underlying technology to read from a wide variety of sources. |
| HanaAdapter | This adapter provides real-time changed-data capture capability in order to replicate data from a remote SAP HANA database to a target SAP HANA database. You can also write back to a virtual table. Use this adapter to extract data from an ECC on an...
---
title: BW/4HANA Security: SAP BW/4HANA Migration (Remote Conversion)
url: https://blogs.sap.com/2023/08/06/bw-4hana-security-sap-bw-4hana-migration-remote-conversion/
source: SAP Blogs
date: 2023-08-07
fetch_date: 2025-10-04T11:59:41.472907
---

# BW/4HANA Security: SAP BW/4HANA Migration (Remote Conversion)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* BW/4HANA Security: SAP BW/4HANA Migration (Remote ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/166287&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BW/4HANA Security: SAP BW/4HANA Migration (Remote Conversion)](/t5/technology-blog-posts-by-sap/bw-4hana-security-sap-bw-4hana-migration-remote-conversion/ba-p/13575339)

![Krishan_Singh_Chauhan](https://avatars.profile.sap.com/3/8/id3812b007b0795cb26a8a16005bb28fa4d01218ed58a9b99f3b86543dfe507baa_small.jpeg "Krishan_Singh_Chauhan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Krishan\_Singh\_Chauhan](https://community.sap.com/t5/user/viewprofilepage/user-id/14777)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=166287)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/166287)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13575339)

‎2023 Aug 06
4:44 AM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/166287/tab/all-users "Click here to see who gave kudos to this post.")

4,364

* SAP Managed Tags
* [BW (SAP Business Warehouse)](https://community.sap.com/t5/c-khhcw49343/BW%2520%28SAP%2520Business%2520Warehouse%29/pd-p/242586194391178517100436979900901)
* [SAP BW/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520BW%252F4HANA/pd-p/73554900100800000681)
* [NW ABAP User Administration and Authorization](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520User%2520Administration%2520and%2520Authorization/pd-p/856729761471794137198600667374174)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [BW (SAP Business Warehouse)

  Software Product Function](/t5/c-khhcw49343/BW%2B%252528SAP%2BBusiness%2BWarehouse%252529/pd-p/242586194391178517100436979900901)
* [SAP BW/4HANA

  SAP BW/4HANA](/t5/c-khhcw49343/SAP%2BBW%25252F4HANA/pd-p/73554900100800000681)
* [NW ABAP User Administration and Authorization

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BUser%2BAdministration%2Band%2BAuthorization/pd-p/856729761471794137198600667374174)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

View products (4)

# **Introduction**

SAP BW/4HANA is a next generation data warehouse solution developed by SAP. The underlying foundation of SAP BW/4HANA is the SAP HANA in-memory database, which means that the data is stored and processed in the main memory of the server resulting faster data retrieval, processing, and analytics compared to traditional disk-based databases.

SAP BW/4HANA simplifies data modeling, enables real-time analytics, and supports integration with advanced technologies like big data and machine learning. It helps organizations consolidate, manage, and analyze large volumes of data, providing timely insights for data-driven decision-making.

Organizations that have been using the earlier version of SAP BW can migrate to SAP BW/4HANA. The migration process involves converting the existing data models, objects, and applications to the new platform, taking advantage of the improved features and capabilities.

## **Business Scenario:**

Organization is planning to migrate from BW to BW/4HANA solution but they are keen to know the impact on security authorizations. Also, the security authorization activities to be carried out as a part of the migration. This article will help the organization to achieve their requirements in terms of security authorizations.

## **Step1: Transport SU25 changes**

+ Create a transport request in BW system for customer tables.

+ Transport the customer tables from BW to BW/4HANA system.

## **Step2: SAP BW Users.**

+ Discuss with the business about the SAP BW user master i.e. how they want to handle the users in BW/4HANA system.

+ If business agrees for client copy via BW system then copy profile SAP\_UONL (User Without Authorization Profiles and Roles) into BW/4HANA system.

## **Step3: Transport BW Analysis Authorizations**

+ Discuss with the business and identify the list of BW analysis authorizations which are in scope i.e. BW analysis authorizations which needs to be available in BW/4HANA system.

+ Transport the scoped analysis authorizations from BW to BW/4HANA system.

## **Step4: Transport BW roles**

+ Discuss with the business and identify the list of BW roles which are in scope i.e. BW roles which needs to be available in BW/4HANA system.

+ Transport the scoped roles from BW to BW/4HANA system.

## **Step5: Run SU25 Steps**

+ Execute SU25 steps i.e. Step 2A, 2B, 2D and 2C

+ Extract the list of impacted roles, discuss with the business and remediate the roles.

## **Step6: Execute Transfer of Authorizations into BW/4HANA**

+ BW specific authorizations for object types get impacted when we convert SAP BW to SAP BW/4HANA system like InfoCubes and those must be replaced by authorizations for corresponding object types like ADSO.

+ Program “RS\_B4HTAU\_CREATE\_RUN” gives you the list of impacted authorizations for the corresponding object types.

+ Run Program “RS\_B4HTAU\_CREATE\_RUN” into BW/4HANA system.

![](/legacyfs/online/storage/blog_attachments/2023/08/1-13.png)

Fig.1.1

+ Create Rule ID to perform Transfer of Authorizations

![](/legacyfs/online/storage/blog_attachments/2023/08/2-11.png)

Fig.1.2

+ Add the required BW/scoped roles which needs to be analyzed.

![](/legacyfs/online/storage/blog_attachments/2023/08/3-10.png)

Fig.1.3

+ Click on the settings button to add the Suffix for the new BW/4HANA role i.e. when you execute this tool, system automatically creates new role with adjustment of authorizations for corresponding object types.

![](/legacyfs/online/storage/blog_attachments/2023/08/5-5.png)

Fig.1.4

+ Selected BW/scoped roles with corresponding new BW/4HANA roles (with suffix) gets available in the Transfer of Authorizations tool.

![](/legacyfs/online/storage/blog_attachments/2023/08/6-5.png)

Fig.1.5

+ Click on Initial Run and Delta Run to perform the analysis on the selected BW roles.

![](/legacyfs/online/storage/blog_attachments/2023/08/7-2.png)

Fig.1.6

The output of Initial Run and Delta Run gives you the following Action Types:

**ASSUME:** No change in authorizations for object types i.e. Authorization will continue to work even after the conversion.

![](/legacyfs/online/storage/blog_attachments/2023/08/7-3.png)

Fig.1.7

**ADJUST:** Check if there is any change in the values of authorization object and adapt it accordingly.

![](/legacyfs/online/storage/blog_attachments/2023/08/8-4.png)

Fig.1.8

**REPLACE:** Change the Authorization Objects and adapt it's values accordingly.

![](/legacyfs/online/storage/blog_attachments/2023/08/9-2.png)

Fig.1.9

![](/legacyfs/online/storage/blog_attachments/2023/08/10-2.png)

Fig.1.10

**OBSOLETE:** Authorization object is not supported or obsolete, should be removed/deactivated from the role.

![](/legacyfs/online/storage/blog_attachments/2023/08/11...
---
title: Add BW Bridge and/or Embedded Data Lake to SAP Datasphere Service Instance created from SAP BTP Platform
url: https://blogs.sap.com/2023/04/01/add-bw-bridge-and-or-embedded-data-lake-to-sap-datasphere-service-instance-created-from-sap-btp-platform/
source: SAP Blogs
date: 2023-04-02
fetch_date: 2025-10-04T11:27:05.930985
---

# Add BW Bridge and/or Embedded Data Lake to SAP Datasphere Service Instance created from SAP BTP Platform

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Add BW Bridge and/or Embedded Data Lake to SAP Dat...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163183&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Add BW Bridge and/or Embedded Data Lake to SAP Datasphere Service Instance created from SAP BTP Platform](/t5/technology-blog-posts-by-sap/add-bw-bridge-and-or-embedded-data-lake-to-sap-datasphere-service-instance/ba-p/13566245)

![linda_peruzzi](https://avatars.profile.sap.com/8/9/id8937160b5760904b56e08a030f42895f185fe3e15fbdea60754b06ec81be62e6_small.jpeg "linda_peruzzi")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[linda\_peruzzi](https://community.sap.com/t5/user/viewprofilepage/user-id/182109)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163183)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163183)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566245)

‎2023 Apr 01
1:04 AM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163183/tab/all-users "Click here to see who gave kudos to this post.")

3,091

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

#### Disclaimer: Starting January 1st, 2026, the service mentioned below will no longer be available through BTPEA, CPEA, or PAYG models.It will instead be offered exclusively via the SAP Business Data Cloud Subscription Model. Please note, this blog will no longer be relevant after that date.

##

## Introduction

This blog is an extension of my colleague Jeetandra Kapase's informative blog on  [How to create SAP Datasphere service instance in the SAP BTP Platform](https://blogs.sap.com/2023/03/17/how-to-create-sap-datasphere-service-instance-in-the-sap-btp-platform/#Types%20of%20SAP%20BTP%20offerings) as customers have had questions on the next steps on adding the **BW Bridge** or the embedded **Data Lake**.

By the end of doing the steps in Jeetandra’s blog, a Datasphere service instance will be created and the **System Owner** will receive an activation email with instructions on how to access the tenant. They will then have the authorizations to perform the next configuration steps.

Some customers may also want to include SAP BW Bridge and/or the HANA Cloud Data Lake offering in their new Datasphere tenant created from SAP BTP Platform.  This blog will link you to resources to size the required components and how to access the tenant configuration.

Please note that BW Bridge and Data Lake are not available as part of the free tier option in BTP.  See [SAP Note 3227267](https://launchpad.support.sap.com/#/notes/3227267).

There may also be some limitations on using the Flexible Tenant Configuration based on the region you are in. See [SAP Note 3144215](https://launchpad.support.sap.com/#/notes/3144215).

For any questions you may have about **BW Bridge** and the **Embedded Data Lake** through BTP as far as your use cases, costs etc. , please contact your SAP Account team.

### ![](/legacyfs/online/storage/blog_attachments/2023/03/OverallArchitecture.jpg)

##

## What is SAP Datasphere BW Bridge and who would benefit from it?

SAP Datasphere, BW Bridge is a function enhancement of SAP Datasphere.  Organizations that may consider using the BW Bridge include those that:

1. Already have investments in SAP BW and BW/4HANA and want to leverage the benefits of cloud-based data warehousing by either migrating or extending their current investments with SAP BW and BW/4HANA.

1. Seek to integrate SAP BW and BW/4HANA with other SAP Datasphere capabilities and artifacts.

1. Are looking for a scalable, flexible, and cost-effective solution for data warehousing and analytics.

The BW Bridge supports ABAP ODP Data Sources. It also utilizes the familiar BW Tooling (Eclipse, SAP HANA Studio etc.) so experienced BW users can start using BW Bridge without much of a learning curve.   Objects in the BW Bridge can then be shared with other Datasphere Core Artifacts for further integration with other system data to create Analytic Models and other uses.

For more information on the BW Bridge and its use case, please see the following blog for a  [BW Bridge technical deep dive](https://blogs.sap.com/2021/11/17/sap-data-warehouse-cloud-sap-bw-bridge-overview-and-technical-deep-dive/)

![](/legacyfs/online/storage/blog_attachments/2023/03/SAP-Datasphere-BW-Bridge.jpg).

Architecture of BW Bridge

## What is SAP Datasphere's Embedded HANA Cloud Data Lake?

The **Data Lake** in **SAP Datasphere** is an essential component designed to store and process large volumes of raw and unstructured data leveraging inexpensive storage options to lower costs. This is generally data that does not frequently change.  **SAP Datasphere** has the option to include an **embedded Data Lake** in its environment and access the data to integrate with other SAP Datasphere artifacts.  For more information, please see the following blog [Working with the embedded data lake in Datasphere](https://blogs.sap.com/2023/02/03/working-with-the-embedded-data-lake-in-sap-data-warehouse-cloud/)

### ![](/legacyfs/online/storage/blog_attachments/2023/03/HANACloudDatalake.jpg)

Some customers may already have a standalone **HANA Cloud with Data Lake**.  In this case, they do not need to add the Datasphere embedded Data Lake as they can also interact with a Stand Alone Hana Cloud environment and its Data Lake by creating Connections in Datasphere.

## Sizing Resources

To view all supported size combinations, go to the [SAP Datasphere Capacity Unit Estimator](https://datasphere-estimator-sac-saceu10.cfapps.eu10.hana.ondemand.com/ "https://datasphere-estimator-sac-saceu10.cfapps.eu10.hana.ondemand.com/").

Before allocating resources to **BW Bridge**, it helps to understand the sizing required for your company. Refer to the blog [Get ready for SAP BW Bridge SAP Datasphere Cloud Sizing Report](https://blogs.sap.com/2022/12/28/get-ready-for-sap-bw-bridge-sap-data-warehouse-cloud-sizing-report/)

For the **Data Lake**, You can specify from 0 TB (minimum) to 90 TB (maximum), by increments of 5 TB.

When adding additional components in the ***Tenant Configuration***, it is advised to talk to your SAP Account Team for any guidance if there are any doubts as once the sizing is set on the tenant, currenty it can't be downsized without SAP's support. See [SAP Note 3144215](https://launchpad.support.sap.com/#/notes/3144215)

## Steps to assign resources for BW Bridge and Data Lake

Once the System User ...
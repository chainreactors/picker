---
title: SAP Analytic Cloud Content Network Package Transport via BTP Transport Management service.
url: https://blogs.sap.com/2023/08/20/sap-analytic-cloud-content-network-package-transport-via-btp-transport-management-service./
source: SAP Blogs
date: 2023-08-21
fetch_date: 2025-10-04T11:59:52.469801
---

# SAP Analytic Cloud Content Network Package Transport via BTP Transport Management service.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Analytic Cloud Content Network Package Transpo...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/166809&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Analytic Cloud Content Network Package Transport via BTP Transport Management service.](/t5/technology-blog-posts-by-sap/sap-analytic-cloud-content-network-package-transport-via-btp-transport/ba-p/13576783)

![ashokkumar_kn](https://avatars.profile.sap.com/3/7/id37e5b775d07d912b355f146f1d81b009efd6bd6091083ffd3dbdbefe38241512_small.jpeg "ashokkumar_kn")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ashokkumar\_kn](https://community.sap.com/t5/user/viewprofilepage/user-id/206733)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=166809)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/166809)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13576783)

‎2023 Aug 20
10:47 AM

[16
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/166809/tab/all-users "Click here to see who gave kudos to this post.")

10,075

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Cloud Transport Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Transport%2520Management/pd-p/73554900100800001901)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Cloud Transport Management

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BTransport%2BManagement/pd-p/73554900100800001901)

View products (2)

# Introduction.

The aim of this blog post is to explore the integration of SAC Content Network storage with BTP Cloud Transport management service for transport use cases. The post will cover both the functional overview and instructions on how to achieve this integration.

This feature is available in SAC Version 2023.16 (2023 QRC 3 Release)

*---Short 5 Min demo*

[![](/legacyfs/online/storage/blog_attachments/2023/08/Thumbnain-1.jpg)](https://video.sap.com/media/t/1_0a13eksv)

## About BTP Cloud Transport Management Service (cTMS)

SAP Cloud Transport Management service helps to manage Software deliverables between accounts of different environments.

* Helps to define Landscape and Transport Route ( Dev > Test > Production )

* Manual and Schedule transport of Application content.

* Integrated with SolMan, ChaRM and Clould ALM Tools.

If you require additional information regarding cTMS, plse visit  [help.sap.com](https://help.sap.com/docs/cloud-transport-management?version=Cloud)

![](/legacyfs/online/storage/blog_attachments/2023/08/ctms-overview.png)

## Integration between SAC and cTMS

With this integration with cTMS, users can now manage the transport of Content Network packages via cTMS.

Below are the key value proposition with integration.

* **Manage SAC Transport along with other SAP Application Transport.**

* **Leverage Landscape Management and Transport Route defined in cTMS.**

* **Schedule of SAC transport. Users can schedule SAC Transport for any particular Date and time.**

* **Separation of Concerns.**

* **Transport between Landscape.**

## ![](/legacyfs/online/storage/blog_attachments/2023/08/CTMS.jpg)

##

## Manage SAC Transport along with other SAP Applications.

Several SAP Applications starts supporting cTMS including HANA Cloud. Having a common tool across SAP products helps to visualize and manage transport holistically.

For example, if SAC story depends on HANA Cloud data source, Customers can manage Hana Cloud and SAC transport via cTMS. For some reason, if Hana Could transport fails, the Transport admin can decide not to transport SAC objects until HANA Cloud transport issue is resolved.

## Leverage Landscape Management and transport Route defined in cTMS

cTMS allows defining of Landscape and Transport Routes. SAC customers can define their SAC Landscape in cTMS and perform transport.

For example, if SAC customers have 3 Tenant setups (Dev, Test, Production), then they can define each node representing Dev/Test/Prod and define Transport Route.

![](/legacyfs/online/storage/blog_attachments/2023/08/Transport-Route.png)

## Schedule of SAC Transport.

cTMS allows scheduling of Import in the destination tenant. This functionality would help transport Admin to perform transport during their project scheduled downtime.

The granularity of the schedule could be as small as Daily every hour (or) Weekly for a Particular Data and Time.

![](/legacyfs/online/storage/blog_attachments/2023/08/schedule.png)

## Separation of Concerns

Having a dedicated tool (cTMS) for transport helps to achieve separation of concerns.

Developers can just focus on creating content and defining packages in SAC > Export> Content Network (Focus on defining package).

Transport admin can have access only to cTMS can focus and transport specific activities and execute transport based on their project schedule.

For more information related to cTMS please refer Help document: <https://help.sap.com/docs/cloud-transport-management?version=Cloud>

## Transport between Landscape

cTMS support cross landscape transport.

For example, if you have Development in non-EUDP Tenant and Production in EUDP tenants, it is possible to transport SAC packages via cTMS.

## How to Configure

In this section let's look at the configurations required to set up SAC and cTMS Integration.

Please refer to the official Help documentation: [help.sap.com](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/92f02ae572fa44d4b78cca0d323f49de.html)

* Configuring cTMS

  + Creating a Destination in BTP

  + Configure Node and Routes in cTMS

* SAC Configuration

  + Administration settings

  + Configure cTMS endpoints.

* Workflow

  + Export ACN Package to cTMS

  + Trigger transport

**Configuring cTMS**

Create Destination.

It is required to create a destination for each Target SAC tenant.

1. Login to SAP BTP Cockpit.

2. Go to left pane > Destination > New Destination.

Note: Create new destination for each SAC Target node. For example if you 3 tenant model, Dev to Test to Prod.

Create separate BTP destinations for Test and Prod.

|
 Name |
 Provide name of the Destination, This is to identify specific SAC Tenant.   In 3 tenant setup, users need to create 2 destination       * One for SAC Test Tenant. (Ex SAC\_TEST\_TENANT)  * One for Production Tenant.(Ex SAC\_PROD\_TENANT) |

|
 Type |
 HTTP |

|
 Description |
 Provide a description of destination tenant. |

|
 URL |
 Provide API URL which cTMS will use to trigger import during transport.   https:// <SAC Tenant>/api/v1/content/deploy/ |

|
 Proxy Type |
 Internet. |

|
 Authentication |
 Supported Authentication   OAuth2ClientCredentials ( Configured in SAC > System > Administration > Configure Clients)       * Client ID : Provide Client ID  * Client...
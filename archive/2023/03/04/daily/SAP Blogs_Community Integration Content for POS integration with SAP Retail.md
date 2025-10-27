---
title: Community Integration Content for POS integration with SAP Retail
url: https://blogs.sap.com/2023/03/03/community-integration-content-for-pos-integration-with-sap-retail/
source: SAP Blogs
date: 2023-03-04
fetch_date: 2025-10-04T08:37:45.805489
---

# Community Integration Content for POS integration with SAP Retail

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Community Integration Content for POS integration ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161378&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Community Integration Content for POS integration with SAP Retail](/t5/technology-blog-posts-by-sap/community-integration-content-for-pos-integration-with-sap-retail/ba-p/13560688)

![bobby_liu](https://avatars.profile.sap.com/e/7/ide7402c5699897baf6b6bf12afdd560b7272481b9cb87a2993dca6ed54daaee1f_small.jpeg "bobby_liu")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[bobby\_liu](https://community.sap.com/t5/user/viewprofilepage/user-id/261692)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161378)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161378)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560688)

‎2023 Mar 03
8:36 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161378/tab/all-users "Click here to see who gave kudos to this post.")

3,807

* SAP Managed Tags
* [Retail](https://community.sap.com/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [Retail

  Industry](/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (3)

One of the important aspects mentioned for the success of the SAP Cloud Integration is delivery of Prepackaged Integration Content. Today there are nearly 300+ integration packages & 1800+ iFlows delivered by SAP that are developed based SAP Cloud Integration covering numerous business use cases. All the integration contents are available on SAP [API Business Hub](https://api.sap.com/) (For more detail introduction about API Business Hub, please refer Daniel’s [blog](https://blogs.sap.com/2022/09/16/overview-about-the-sap-api-business-hub/)).

In addition, SAP also introduced community and partner collaboration in SAP API Business Hub (for more detail introduction please refer Jagadish’s [blog](https://blogs.sap.com/2019/12/13/introducing-community-and-partner-collaboration-in-sap-api-business-hub/) and Aaditya’s [blog](https://blogs.sap.com/2022/02/21/community-content-on-the-sap-api-business-hub/)).

In this blog, I would like to introduce one of the integration package I submitted and published to the community recently, which has been built and live for a retail customer, for a quite general and typical integration scenario in SAP Retail solution – Point-of-Sale (POS) integration.

*Comment: Community contents are still treated as customized content, SAP would not take responsibility for bug fixing, but product development team would monitor the download regularly and forward customers’ feedback to the content contributor for further improvement, frequent downloaded contents would be considered by product development team to be further standardized and delivered as SAP prepackaged content.*

**Integration Package introduction**

The package ([SAP Retail Integration with SAP Point-of-Sale](https://api.sap.com/package/SAPRetailIntegrationwithSAPPOS/overview)) is available in the community of SAP API Business Hub.

*Business Scenario:*

In Retail industry, Point-of-Sale(POS) system is a key system of store operation, helping in-store sales as well as inventory management, staffing and etc.

Hereby in SAP Retail solution, there are typical integration scenarios between core Retail (S/4HANA or ECC) and POS system, 2 of the most important scenarios are master data (articles, prices, promotions and etc.) outbound from SAP Retail to POS, and sales upload from POS to SAP CAR (Customer Activity Repository).

![](/legacyfs/online/storage/blog_attachments/2023/03/POS_Int.png)

*Current solution:*

In SAP NW PI/PO, there are standard ESR content for POS integration (STORE CONNECT and TE STORE CONNECT), but no content available in BTP Cloud Integration till now.

*Motivation to adopt Cloud Integration instead of PI/PO:*

* + Benefit from elastic capability of SAP BTP, data volume of retail customers could be varied a lot, for example, sales on Black Friday could be hundreds of times more than a normal working day, with SAP BTP the processing power of customers’ tenants could be scale up/down much more easily than on-premise NW PI/PO.

  + SAP CAR (Customer Activity Repository) would move to a cloud solution in future, which makes the whole scenario a cloud focus.

  + Simplify the network settings, especially for customers with chain of retail convenience stores (e.g. 7-Eleven, Wawa), thousands of POS located nationwide or even globally, which brings huge effort on VPN setting up for on-premise communication.

*iFlows:*

POS Outbound (S/4HANA(suitable for ECC also) -> CI -> SAP POS)

* 4 iFlows to replicate article master, EAN/UPC, pricing, promotions and etc. to POS system

* Standard Enterprise Services triggered from S/4HANA via XI protocol (MerchandiseERPReplicationBulkRequest\_Out – article, price and EAN/UPC, ProductCategoryHierarchyERPReplicationRequest\_Out – department, RetailIncentiveERPStoreOfferReplicationBulkRequest\_Out – MixMatch and RetailEventERPStoreReplicationRequest\_Out – Promotion)

* CI converts SOAP-XML to ASC files accepted by SAP POS

* XSLT mappings from standard ESR content (TE STORE CONNECT) are partially re-used

POS Inbound (SAP POS -> CI -> SAP CAR)

* An iFlow to upload sales data (per receipt) to SAP CAR

* CI loads ASC files in TLOG format from SAP POS

* CI converts TLOG into standard IDOC (/POSDW/POSTR\_CREATEMULTIPLE06) and posts to SAP CAR

* Conversion achieved via Message Mapping built from scratch

Potential enhancements in future

* The iFlows are for SAP POS integration, transformations for message formats of other POS systems (e.g. GK, ARTS format, …) could be implemented by referring standard ESR contents accordingly

* Enhance the inbound mapping for more business scenarios (Good Receipt, Orders, Financial Transactions and etc.)

**Summary**

Therefore, if you are also implementing SAP POS integration in your SAP Retail project, this community content would be a good fit for you, you just need to copy the package to your own DEV tenant, complete the configurations of connectivity, then all the mentioned 5 scenarios above are ready to be used in your Cloud Integration.

additional configurations:

For ERP system -

1. functional configurations to trigger those master data service messages

2. Settings to communicate with cloud integration via XI protocol, pls refer Mandy's [blog](https://blogs....
---
title: Extend SAP S/4HANA Business Processes on SAP BTP, Kyma Runtime
url: https://blogs.sap.com/2023/01/08/extend-sap-s-4hana-business-processes-on-sap-btp-kyma-runtime/
source: SAP Blogs
date: 2023-01-09
fetch_date: 2025-10-04T03:21:33.286631
---

# Extend SAP S/4HANA Business Processes on SAP BTP, Kyma Runtime

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Extend SAP S/4HANA Business Processes on SAP BTP, ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162739&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extend SAP S/4HANA Business Processes on SAP BTP, Kyma Runtime](/t5/technology-blog-posts-by-sap/extend-sap-s-4hana-business-processes-on-sap-btp-kyma-runtime/ba-p/13564785)

![shankari_gr](https://avatars.profile.sap.com/f/a/idfaf0d22f15876adeec59cd0eb1bf34a0bcb6ee6a300fd352cced3a9ec110fc3b_small.jpeg "shankari_gr")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[shankari\_gr](https://community.sap.com/t5/user/viewprofilepage/user-id/200091)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162739)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162739)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564785)

‎2023 Jan 08
6:25 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162739/tab/all-users "Click here to see who gave kudos to this post.")

1,991

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Connectivity service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Connectivity%2520service/pd-p/67837800100800004901)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)

* [SAP Connectivity service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BConnectivity%2Bservice/pd-p/67837800100800004901)
* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (4)

We are happy to release a new mission [Extend SAP S/4HANA Business Processes on SAP Business Technology Platform, Kyma Runtime](https://discovery-center.cloud.sap/missiondetail/3586/) in [SAP Discovery Center](https://discovery-center.cloud.sap/). The main intent of this scenario is to complement an existing business process in an SAP solution – currently SAP S/4HANA on-premise with additional business process steps. This involves adding major logic and additional data and goes beyond simple UI changes.

This application showcases:

* Building applications on [SAP Business Technology Platform (SAP BTP), Kyma Runtime](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/468c2f3c3ca24c2c8497ef9f83154c44.html) using [SAP Cloud Application Programming Model (CAP)](https://cap.cloud.sap/docs/)

* Consuming events from SAP S/4HANA on-premise using [SAP Event Mesh](https://help.sap.com/viewer/bf82e6b26456494cbdd197057c09979f/Cloud/en-US/df532e8735eb4322b00bfc7e42f84e8d.html)

* Consuming REST APIs from SAP S/4HANA on-premise using [SAP BTP Connectivity Service](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/14ad61db386949d8abaf45c641aa7dc9.html)

* Building and deploying a function in [SAP BTP Kyma Runtime, Serverless](https://kyma-project.io/docs/components/serverless)

## **Business Scenario:**

A business scenario is used to showcase how to build a SAP S/4HANA on-premise extension application on SAP BTP, Kyma runtime.

John, who is an employee of Business Partner Validation Firm iCredible, which is a third-party vendor of ACME Corporation, would like to get notifications whenever new Business Partners are added in the SAP S/4HANA on-premise system of ACME Corporation. John would then be able to review the Business Partner details in his extension app. He would proceed to visit the Business Partner’s registered office and do some background verification. John would then proceed to update or validate the verification details into the extension app. Once the details are verified, the Business Partner gets activated in the SAP S/4HANA system of ACME Corporation.

The scenario covers:

* Custom extension application that works independently from SAP S/4HANA

* Changes in SAP S/4HANA communicated via events in real time to extension application

* Compute intensive processing available on demand (using serverless)

* Vendor personnel needs access to only custom app

## Mission Project Board

Project board provides a step by step guidance through which you will get a full picture on how the end to end use case works. By trying out the use case you will also get a flavour of the different technologies showcased in this mission.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-08-at-11.21.39-AM.png)

Mission Project Board

## Solution Diagram

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-08-at-11.22.20-AM.png)

Solution Diagram

References:

The sample project can be accessed at [SAP-Samples Github.](https://github.com/SAP-samples/btp-s4hana-kyma-business-process-extension)

You can also explore other exciting mission here: <https://blogs.sap.com/2021/06/28/building-end-to-end-extension-scenarios-on-sap-btp/>

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

8 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fextend-sap-s-4hana-business-processes-on-sap-btp-kyma-runtime%2Fba-p%2F13564785%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensibility-in-the-age-of-ai-why-abcd-is-easier-and-smarter-than-you/ba-p/14234516)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  an hour ago
* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  4 hours ago
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  6 hours ag...
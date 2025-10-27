---
title: SAP BTP DMS for S/4 HANA
url: https://blogs.sap.com/2023/05/05/sap-btp-dms-for-s-4-hana/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:24.091015
---

# SAP BTP DMS for S/4 HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP BTP DMS for S/4 HANA

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68308&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BTP DMS for S/4 HANA](/t5/enterprise-resource-planning-blog-posts-by-members/sap-btp-dms-for-s-4-hana/ba-p/13566278)

![varunbiswas](https://avatars.profile.sap.com/7/8/id78dbc83e574e3a6184efdbc81fc3d9069e6602db08616f404d11bdd73b0ebde0_small.jpeg "varunbiswas")

[varunbiswas](https://community.sap.com/t5/user/viewprofilepage/user-id/775171)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68308)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68308)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566278)

‎2023 May 05
4:16 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68308/tab/all-users "Click here to see who gave kudos to this post.")

12,319

* SAP Managed Tags
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Document Management service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520Management%2520service/pd-p/73555000100800002121)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Document Management service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BDocument%2BManagement%2Bservice/pd-p/73555000100800002121)

View products (4)

While several blogs cover all aspects of creating, connecting, and setting up BTP DMS service with/for S/4HANA, this write-up will not repeat those. Instead, I will share the challenges I faced and the steps I took to configure and integrate the service. If you do not read the linked blogs, this article may not make sense.

SAP BTP DMS for S/4 HANA

1. > [Start with SAP BTP Document Management Service (DMS)](https://blogs.sap.com/2022/04/07/start-with-sap-btp-document-management-service-dms/)
   >
   > 1. Start config - [Set up your SAP BTP account and subscribe to SAP BTP DMS](https://blogs.sap.com/2022/04/07/start-with-sap-btp-document-management-service-dms/#:~:text=But%20the%20first%20step%20is%20to%20set%20up%20your%20SAP%20BTP%20account%20and%20subscribe%20SAP%20BTP%20DMS%20there).
   >
   > 2. Until - [Navigate to “Users” and select yourself or the user you want to grant access to DMS. Then, assign Ro...](https://blogs.sap.com/2022/04/07/start-with-sap-btp-document-management-service-dms/#:~:text=Navigate%20to%20%E2%80%9CUsers%E2%80%9D%20and%20select%20yourself%20or%20the%20user%20you%20want%20to%20grant%20access%20to%20DMS.%20Assign%20Role%20Collection%20%E2%80%9CDMS_ADMIN%E2%80%9D%20created%20in%20previous%20step).
   >
   > 3. I received 401 and 415 errors. In addition, I could not use the JWT token properly and repeatedly got an ‘Unsupported media’ error. However, following the blog from #2, I did not receive any errors.

2. > [Creating a Repository](https://blogs.sap.com/2020/10/22/integrating-sap-cp-document-management-service-ui-in-the-fiori-app/#:~:text=Creating%20a%20Repository%3A)

   1. > In POSTMAN, unchecked the default ‘Content-Type: text/plan’ and created my own ‘Content-Type: application/json’. ![](/legacyfs/online/storage/blog_attachments/2023/04/image001-2.png)

   2. > You could also do this by changing the content type under the Body tab. ![](/legacyfs/online/storage/blog_attachments/2023/04/image002-2.png)

   3. > I did not create a repository with authorization ‘bearer’ of ‘JWT’ from [https://\*cf.authentication.us10.hana.ondemand.com/oauth/token?grant\_type=client\_credentials](https://*cf.authentication.us10.hana.ondemand.com/oauth/token?grant_type=client_credentials) but instead used ‘OAuth 2.0’ and ‘Get New Access Token’ at [https://\*.cfapps.us10.hana.ondemand.com/rest/v2/repositories](https://*.cfapps.us10.hana.ondemand.com/rest/v2/repositories).

   4. > However, later, I successfully changed the authorization of the /browser GET call to bearer token with JWT token.

   5. > Using OAuth 2.0 would require me to generate/get a new access token.

   6. > I accidentally created the repository twice. DMS will create a repository with the same name but with different IDs.
      >
      > * *My request to POST /rest/v2/repositories.*
      >
      > ```
      > {
      >
      >
      >
      >     "repository": {
      >
      >
      >
      >         "displayName": "ZDMSTEST",
      >
      >
      >
      >         "externalId": "ZDMSTEST",
      >
      >
      >
      >         "isContentBridgeEnabled":"true",
      >
      >
      >
      >         "description": "Repository",
      >
      >
      >
      >         "repositoryType": "internal",
      >
      >
      >
      >         "isVersionEnabled": "true",
      >
      >
      >
      >         "isVirusScanEnabled": "false",
      >
      >
      >
      >         "skipVirusScanForLargeFile": "true",
      >
      >
      >
      >         "hashAlgorithms": "None"
      >
      >
      >
      >
      >
      >
      >
      >     }
      >
      >
      >
      > }
      > ```
      >
      >
      >
      > * > *My response*
      >
      > ```
      > {
      >
      >
      >
      >     "cmisRepositoryId": "cmisRepositoryId",
      >
      >
      >
      >     "createdTime": "2023-03-23T14:45:17.199Z",
      >
      >
      >
      >     "description": "Repository",
      >
      >
      >
      >     "externalId": "ZDMSTEST",
      >
      >
      >
      >     "id": "2his-is the-repo-sitory-idthatyouwillneed",
      >
      >
      >
      >     "lastUpdatedTime": "2023-03-23T14:45:17.199Z",
      >
      >
      >
      >     "name": "ZDMSTEST",
      >
      >
      >
      >     "repositoryCategory": "Instant",
      >
      >
      >
      >     "repositoryParams": [
      >
      >
      >
      >         {
      >
      >
      >
      >             "paramName": "isVersionEnabled",
      >
      >
      >
      >             "paramValue": true
      >
      >
      >
      >         },
      >
      >
      >
      >         {
      >
      >
      >
      >             "paramName": "isThumbnailEnabled",
      >
      >
      >
      >             "paramValue": false
      >
      >
      >
      >         },
      >
      >
      >
      >         {
      >
      >
      >
      >        ...
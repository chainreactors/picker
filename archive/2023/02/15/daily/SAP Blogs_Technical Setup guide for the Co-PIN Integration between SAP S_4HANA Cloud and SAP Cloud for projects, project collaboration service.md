---
title: Technical Setup guide for the Co-PIN Integration between SAP S/4HANA Cloud and SAP Cloud for projects, project collaboration service
url: https://blogs.sap.com/2023/02/14/technical-setup-guide-for-the-co-pin-integration-between-sap-s-4hana-cloud-and-sap-cloud-for-projects-project-collaboration-service/
source: SAP Blogs
date: 2023-02-15
fetch_date: 2025-10-04T06:36:59.581563
---

# Technical Setup guide for the Co-PIN Integration between SAP S/4HANA Cloud and SAP Cloud for projects, project collaboration service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Technical Setup guide for the Co-PIN Integration b...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162992&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Technical Setup guide for the Co-PIN Integration between SAP S/4HANA Cloud and SAP Cloud for projects, project collaboration service](/t5/technology-blog-posts-by-members/technical-setup-guide-for-the-co-pin-integration-between-sap-s-4hana-cloud/ba-p/13566871)

![sg25](https://avatars.profile.sap.com/8/6/id865f4e593b064cf51ba465adfc83ad9aea58c16db93d25e3acdbaf396eba0353_small.jpeg "sg25")

[sg25](https://community.sap.com/t5/user/viewprofilepage/user-id/124196)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162992)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162992)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566871)

‎2023 Feb 14
11:58 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162992/tab/all-users "Click here to see who gave kudos to this post.")

2,142

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Engineering, Construction, and Operations](https://community.sap.com/t5/c-khhcw49343/Engineering%252C%2520Construction%252C%2520and%2520Operations/pd-p/193926939960921617562539)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Project Intelligence Network](https://community.sap.com/t5/c-khhcw49343/SAP%2520Project%2520Intelligence%2520Network/pd-p/73554900100800000970)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Engineering, Construction, and Operations

  Industry](/t5/c-khhcw49343/Engineering%25252C%2BConstruction%25252C%2Band%2BOperations/pd-p/193926939960921617562539)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Project Intelligence Network

  Software Product](/t5/c-khhcw49343/SAP%2BProject%2BIntelligence%2BNetwork/pd-p/73554900100800000970)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (6)

Hello Everyone,

Welcome you to my 1st blog. I want to share my experience on technical setup the Co-PIN Integration between SAP S/4HANA Cloud and SAP S/4HANA Cloud for projects, project collaboration service.

**Business Purpose and Flow**

The integration allows you to integrate the SAP S/4 HANA Cloud with the application SAP Project Intelligence Network. With this integration, you connect with project owners, engineering service providers, contractors, subcontractors, and building material suppliers on a single BIM collaboration platform to eliminate waste and rework and increase productivity with the SAP Project Intelligence Network application.

* Cloud deployment

* Single repository of construction information

* Shared digital twin that supports open BIM standards

* Source of reusable operations information

**Process Steps:**

1. Configuration in S/4HANA Cloud

2. Configuration in SAP Cloud Integration

3. Configuration in SAP BTP Cockpit

**A. Configuration in S/4HANA Cloud**

Step 1: Go to maintain communication user and create one communication user named as COPIN.

![](/legacyfs/online/storage/blog_attachments/2023/02/1-8.png)

communication user

Step 2: Create one Communication system.

![](/legacyfs/online/storage/blog_attachments/2023/02/2-5.png)

communication system

Step 3: Enter the host name and port no. Host name as S/4HC api url and port as 443.

![](/legacyfs/online/storage/blog_attachments/2023/02/3-1.png)

Step 4: Add the new communication user in the inbound user.

![](/legacyfs/online/storage/blog_attachments/2023/02/4-2.png)

Step 5: Create communication arrangement (SAP\_COM\_0308) and add the communication system into it.

![](/legacyfs/online/storage/blog_attachments/2023/02/5-2.png)

communication arrangement

**B. Configuration in SAP Cloud Integration**

Step 1: Go to Cloud Integration and click on Monitor --> Security material.

![](/legacyfs/online/storage/blog_attachments/2023/02/6-1.png)

Step 2: Deploy the communication user details as S4H\_CPI

![](/legacyfs/online/storage/blog_attachments/2023/02/7-1.png)

Step 3: Copy this package from Discover tab and then come in the design tab.

![](/legacyfs/online/storage/blog_attachments/2023/02/8-1.png)

Step 4: Click on Actions-> Configure.

![](/legacyfs/online/storage/blog_attachments/2023/02/9-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/10-1.png)

Step 5: Provide S/4Hana cloud url in the oDataBaseUrl and provide the S4 deployed credential name in credential part.

![](/legacyfs/online/storage/blog_attachments/2023/02/11-2.png)

Step 6: In More section,

ApplicationBse URL : <S/4Hana Cloud url> + /ui#EnterpriseProject-maintain&/C\_PPM\_ProjectControlTP(ProjectUUID=guid'%projectUUID%',IsActiveEntity=true)

ApplicationBaseUrlCustomerProjects : : <S/4Hana Cloud url> +  /ui#CustomerProject-maintainCustomerProject&/Display/ProjEngagementsSet/%project%/?tab=infoTab

ApplicationBaseUrlInternalProjects : <S/4Hana Cloud url> +  /ui#InternalProject-createInternalProject&/Display/ProjEngagementsSet/%project%/?tab=infoTab

Save and deploy the package

![](/legacyfs/online/storage/blog_attachments/2023/02/12-1.png)

Step 7: Go to monitor --> Manage integration Content.

![](/legacyfs/online/storage/blog_attachments/2023/02/13.png)

Step 8: Filter the i-flow name and take the endpoint url.

![](/legacyfs/online/storage/blog_attachments/2023/02/14.png)

**C. Configuration in SAP BTP Cockpit**

Step 1:Go to CF BTP account and create one subscription for “ SAP S/4HANA C4P, CoPM – Demo “ Service.

![](/legacyfs/online/storage/blog_attachments/2023/02/15.png)

Step 2: Create instance of the service “SAP S/4HANA Cloud, Project Collaboration Demo” and create service key.

![](/legacyfs/online/storage/blog_attachments/2023/02/16.png)

Step 3: Assign the roles to the user to access the pin tenant.

![](/legacyfs/online/storage/blog_attachments/2023/02/17.png)

Step 4: Go to destinations and create one destination.

Name: <suitable name>

URL : <CPI end point url>

User: <p user details / Client key>

Password: <p user password/ Client Secret>

In Additional Properties,

copin.int.display\_name : <suitable name>

copin.int.object : ProjectPlan

...
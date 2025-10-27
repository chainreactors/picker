---
title: SAP Task Center setup for S/4HANA On-Premise
url: https://blogs.sap.com/2022/12/01/sap-task-center-setup-for-s-4hana-on-premise/
source: SAP Blogs
date: 2022-12-02
fetch_date: 2025-10-04T00:17:03.468336
---

# SAP Task Center setup for S/4HANA On-Premise

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Task Center setup for S/4HANA On-Premise

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/171731&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Task Center setup for S/4HANA On-Premise](/t5/technology-blog-posts-by-sap/sap-task-center-setup-for-s-4hana-on-premise/ba-p/13569054)

![SomaskandanK](https://avatars.profile.sap.com/b/c/idbcc36c11e450d1df65e5133c716b24558bc0a029e5d78b834381e23c17e8d6d5_small.jpeg "SomaskandanK")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[SomaskandanK](https://community.sap.com/t5/user/viewprofilepage/user-id/138204)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=171731)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/171731)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569054)

‎2022 Dec 01
11:13 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/171731/tab/all-users "Click here to see who gave kudos to this post.")

24,410

* SAP Managed Tags
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)
* [Identity Provisioning](https://community.sap.com/t5/c-khhcw49343/Identity%2520Provisioning/pd-p/73555000100800000425)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Build Work Zone, standard edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520standard%2520edition/pd-p/73554900100800003081)
* [SAP Task Center](https://community.sap.com/t5/c-khhcw49343/SAP%2520Task%2520Center/pd-p/73555000100800002171)
* [SAP Integration Strategy](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Strategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [Identity Provisioning

  SAP Business Technology Platform](/t5/c-khhcw49343/Identity%2BProvisioning/pd-p/73555000100800000425)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Build Work Zone, standard edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Bstandard%2Bedition/pd-p/73554900100800003081)
* [SAP Task Center

  Software Product](/t5/c-khhcw49343/SAP%2BTask%2BCenter/pd-p/73555000100800002171)
* [SAP Integration Strategy

  Topic](/t5/c-khhcw49343/SAP%2BIntegration%2BStrategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)

View products (6)

## Introduction:

The SAP Task Center service enables integration with various SAP applications to provide a single entry point for end users to access all their assigned approval tasks. The tasks can be accessed by end users through the SAP Task Center Web application

This blog details integration of Task Center in BTP with S/4HANA on-premise.

## Prerequisites:

+ SAP BTP Cloud Foundry environment

+ Task Center service in BTP

+ Launchpad service in BTP

+ Identity Authentication service (IAS)

+ Identity Provisioning service (IPS)

+ SAP Cloud Connector

+ SAP S/4HANA On-premise

The integration of SAP Task center with On-Premise S/4HANA involves the below listed activities

1. Task Center configuration with S/4HANA On-Premise system.

1. Update user UUID from IAS to S/4HANA user.

1. Integration of My inbox app with SAP BTP Launchpad service

1. Configure Launchpad site and Role Assignment

## 1.   Task Center configuration with S/4HANA On-Premise system

### 1.1   Deployment of Task Center & Launchpad Service in BTP

SAP Task center is available on **BTP Cloud Foundry environment** only. Establish trust between Identity Provider and subaccount of Task center.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture1-6.jpg)

Run the **Booster setup** for Task center to complete the Automatic setup of Task Center, which creates the sample destinations for the SAP Solutions to be connected with sample values for the properties and subscription to the SAP Launchpad service application. Refer to the [help](https://help.sap.com/docs/TASK_CENTER/08cbda59b4954e93abb2ec85f1db399d/3a499676e7ae4282af84092f778e3737.html?version=Cloud) document to run booster setup.

### 1.2   SAP Launchpad service configuration for Task Center

1.2.1.   Navigate to **Instance and Subscriptions** in BTP, Select the Launchpad Service and click Go to Application to access the Site Manager

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture2.jpg)

1.2.2.   Update the content of Launchpad service from **Site manager** and add the apps to My Content.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture3-4.jpg)

1.2.3.   Create new **Group and Role** in Site Manager for Task center and Task Center Administration.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture4-3.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture5-4.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture6-2.jpg)

1.2.4.   Create a new **site for Task center application** and add the Task Center Role.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture7-2.jpg)

### 1.3   Cloud connector setup for Task Center and S/4HANA On-Premise

The cloud connector is used to connect Task Center with On-Premise S/4HANA. The cloud connector must be configured to use **UUID of the user** as subject pattern for Principal Propagation to S/4HANA.

**Note:** In case the cloud connector is currently configured with different subject pattern for Principal Propagation (for example, e-mail), use other cloud connector with user UUID as the subject pattern for Task center to communicate with S/4HANA.

1.3.1.   Configure the BTP CF subaccount in Cloud Connector

1.3.2.   Create **http** connection to backend S/4HANA with Principal Propagation using **X.509 Certificate (strict usage)**. In the URL path section, allow access to **/sap/opu/odata4/sap/** path and sub path.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture8.jpg)

1.3.3.   Navigate to **configuration** menu in SAP Cloud Connector, Select **On-Premise** section to generate system certificate and CA certificate. It can be Self signed or CA signed certificate.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture9-19.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture10-14.png)

1.3.4.   In the Principal Propagation section, Configure the **“user\_uuid”** as the subject pattern and download the sample certificate.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture11-9.png)

### 1.4  Configuration in S/4HANA system

In S/4HANA System, execute the **SPRO** transaction, choose SAP Reference IMG -> SAP NetWea...
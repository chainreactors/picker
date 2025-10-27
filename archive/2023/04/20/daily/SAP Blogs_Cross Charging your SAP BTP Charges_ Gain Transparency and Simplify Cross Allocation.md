---
title: Cross Charging your SAP BTP Charges: Gain Transparency and Simplify Cross Allocation
url: https://blogs.sap.com/2023/04/19/cross-charging-your-sap-btp-charges-gain-transparency-and-simplify-cross-allocation/
source: SAP Blogs
date: 2023-04-20
fetch_date: 2025-10-04T11:33:01.368993
---

# Cross Charging your SAP BTP Charges: Gain Transparency and Simplify Cross Allocation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Cross Charging your SAP BTP Charges: Gain Transpar...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164537&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cross Charging your SAP BTP Charges: Gain Transparency and Simplify Cross Allocation](/t5/technology-blog-posts-by-sap/cross-charging-your-sap-btp-charges-gain-transparency-and-simplify-cross/ba-p/13570451)

![former_member274698](https://avatars.profile.sap.com/former_member_small.jpeg "former_member274698")

[former\_member274698](https://community.sap.com/t5/user/viewprofilepage/user-id/274698)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164537)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164537)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570451)

‎2023 Apr 19
11:43 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164537/tab/all-users "Click here to see who gave kudos to this post.")

2,480

* SAP Managed Tags
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (1)

A step-by-step guide to understanding your SAP BTP sub-account costs and facilitating cross-allocation across your business units.

## Introduction

Many customers take advantage of the consumption-based pricing model of SAP BTP. In doing so, customer teams need to organize their account structure to distribute consumption across different units, departments, and regions within their organization. While SAP bills customers for each Global Account, customers often want to cross-charge these units according to their usage. To achieve this, customer account teams require transparency of usage patterns per sub-account and an easy way to cross-charge their internal units accordingly. This article outlines a solution to this problem.

## Solution Approach

The solution is broken down into four steps:

1. Configure labels in the BTP Cockpit for each sub-account – to mark sub-accounts to exclude in subscription data.

2. Create entitlements for "Cloud Management Service" and "Usage Data Management."

3. Create instances of "Cloud Management Service" and "Usage Data Management" services.

4. Use simple code to extract the metering data using a Resource Consumption API.

## Step 1 – Configure Labels in the BTP Cockpit for Each Sub Account

The first step is to define labels for your sub-account. You need to use a specific label name called “EXCLUDE”. This is important because the code which you will see in later steps uses the hard-coded label called “EXCLUDE”.  This is needed for all subaccounts which you want to be “excluded” from the metering calculations.

* Go to your subaccount edit page and add a new label. No need to add any values for this label.

![](/legacyfs/online/storage/blog_attachments/2023/03/01-Edit-Subaccount.png)

EXCLUDE Label

* After creating the label, you can view it in your Global Account – Account Explorer.

### ![](/legacyfs/online/storage/blog_attachments/2023/03/02-Account-Explorer.png)

## Step 2 - Create entitlements for “Cloud Management Service” and “Usage Data Management

Next, create entitlements for the two services used in extracting usage data for all your sub-accounts in your global account. In the BTP Cockpit, go to "Service Assignments" to check the Quota Assignments of the two services. Then, go to Entity Assignments, select your sub-account in "Select Entities," and provide an entitlement for the Cloud Management Service and Usage Data Management service.

* [Cloud Management Service](https://discovery-center.cloud.sap/serviceCatalog/cloud-management-service?region=all)

* [Usage Data Management](https://discovery-center.cloud.sap/serviceCatalog/usage-data-management-service?service_plan=reporting-ga-admin&region=all&commercialModel=cpea)

1. In BTP Cockpit, go to “Service Assignments“ to check the Quota Assignments of the two service

![](/legacyfs/online/storage/blog_attachments/2023/03/03-Service-Assignments.png)

2. Go to Entity Assignments, select your subaccount in “Select Entities”

![](/legacyfs/online/storage/blog_attachments/2023/03/04-Entity-Assignments.png)

Entity Assignments

3. Give entitlement to the Cloud Management Service

* + Click Add Service Plan

  + Click Configure Entitlements

  + Search for “Cloud Management Service”

  + Select the “central” option

  + “Add 1 Service Plan”

  + Click Save

![](/legacyfs/online/storage/blog_attachments/2023/03/05-Add-Entitlements.png)

Add CMS Entitlement

![](/legacyfs/online/storage/blog_attachments/2023/03/06-Cloud-Management.png)

Cloud Management Service

4. Repeat the same for the “Usage Data Management” service

* + Click Configure Entitlements

  + Click Add Service Plan

  + Search for “Usage Data Management”

  + Select the “reporting-ga-admin” option

  + “Add 1 Service Plan”

  + Click Save

![](/legacyfs/online/storage/blog_attachments/2023/03/07-Add-UDM.png)

### Step 3 - Create an instance of “Cloud Management Service” and “Usage Data Management” services

Create instances of the two services, and then create service keys and bindings for each service. Remember to save the JSON data for each service key and binding as this will be used in the next step.

* Go to Service Market Place, Select Cloud Management Service, and click “Create”

![](/legacyfs/online/storage/blog_attachments/2023/03/08-Create-Instances.png)

Create Service instances

* Enter an Instance Name – ex “TEST\_CMS” and make sure you **select “Other”** in the runtime environment

![](/legacyfs/online/storage/blog_attachments/2023/03/09-Craete-CMS.png)

Create CMS Instance

* Instantiate the *Usage Data Management* service in any subaccount as this service reports usage data for the whole of the Global Account

* Go to Service Market Place, Select *Usage Data Management,* and click “*Create*”

* Enter an Instance Name – ex “TEST\_UDM” and make sure you **select “Cloud Foundry”** in the runtime environment

![](/legacyfs/online/storage/blog_attachments/2023/03/010-Create-UDM.png)

Create UDM Instance

* Check and make sure instances are created under “instances and subscriptions”

![](/legacyfs/online/storage/blog_attachments/2023/03/011-Instances.png)

Check Instances

* Select the *Usage Data Management* service and click on *Create Service Key*

* Enter the *Service Key* name – ex “Test\_UDM”

* Enter the X509 Json:

```
{

"credential-type": "x509",

"x509": {

    "key-length": 2048,

    "validity": 7,

    "validity-type": "DAYS"

}

}
```

```
![](/legacyfs/online/storage/blog_attachments/2023/04/new_binding.png)
```

* Once the key is created, keep a copy of the service key. This will help in binding the application in GitHub to the User Data Management service.

![](/legacyfs/online/storage/blog_attachments/2023/04/test_udm_2.png)

* Create Service Binding for...
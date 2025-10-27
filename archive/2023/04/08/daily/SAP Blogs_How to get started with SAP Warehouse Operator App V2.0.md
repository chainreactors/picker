---
title: How to get started with SAP Warehouse Operator App V2.0
url: https://blogs.sap.com/2023/04/07/how-to-get-started-with-sap-warehouse-operator-app-v2.0/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:17.884712
---

# How to get started with SAP Warehouse Operator App V2.0

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to get started with SAP Warehouse Operator App...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162990&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to get started with SAP Warehouse Operator App V2.5](/t5/technology-blog-posts-by-sap/how-to-get-started-with-sap-warehouse-operator-app-v2-5/ba-p/13565699)

![sandeep_tp](https://avatars.profile.sap.com/7/3/id737271d0de414321fa581b89a5d130d40bd6b353f896bec5bf58055a063c9957_small.jpeg "sandeep_tp")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[sandeep\_tp](https://community.sap.com/t5/user/viewprofilepage/user-id/130839)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162990)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162990)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565699)

‎2023 Apr 07
8:55 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162990/tab/all-users "Click here to see who gave kudos to this post.")

10,381

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [Mobile](https://community.sap.com/t5/c-khhcw49343/Mobile/pd-p/246015353107843540080736084568477)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [Mobile

  Topic](/t5/c-khhcw49343/Mobile/pd-p/246015353107843540080736084568477)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (3)

# Introduction

SAP Warehouse Operator is a native mobile app integrated with Warehouse Management in SAP S/4HANA Cloud public edition, that supports warehouse operators with business processes like picking and putaway. SAP Warehouse Operator is currently available for iOS mobile devices.

This blog talks about integrating the App with SAP S/4HANA cloud system.

# Required Systems and Components

+ Warehouse Management in SAP S/4HANA Cloud, public edition

+ SAP Business Technology Platform (SAP BTP) with SAP Mobile Services

+ iPhone 8, iPhone SE 2nd generation or newer with iOS 16 or above

The SAP Warehouse Operator app can be downloaded for free from [Apple App Store here](https://apps.apple.com/app/sap-warehouse-operator/id1579937556?l=en) or using the QR code below.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture-1.png)

SAP Warehouse Operator – QR Code

# Configure trust between the S/4HANA IAS tenant and the Cloud Foundry Organization

Follow the steps described in the [help document](https://help.sap.com/docs/CP_AUTHORIZ_TRUST_MNG/ae8e8427ecdf407790d96dad93b5f723/7c6aa87459764b179aeccadccd4f91f3.html) to establish trust with an Identity Authentication tenant and registering the Subaccount with the tenant.

# Configuration Tasks

Follow the steps described in the [help document](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/configuration-tasks) to set up user propagation between S/4HANA Cloud and the SAP BTP Cloud Foundry environment.

+ [Configure OAuth Communication](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/configuration-tasks#loio6e5e004b6553403486a03da53bfcaf4e__oauth)

+ [Configure Communication Settings in S/4HANA cloud](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/configuration-tasks#loio6e5e004b6553403486a03da53bfcaf4e__s4).

+ [Configure Communication Settings in SAP BTP](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/configuration-tasks#loio6e5e004b6553403486a03da53bfcaf4e__scp)

When **Configuring Communication Settings in S/4HANA cloud** make sure you create Communication Arrangements for the following Communication Scenarios, as these are required by the Warehouse Operator Mobile Application.

Note:

The Communication Arrangement mentioned in the SAP Help document is just for reference and is not required for the Warehouse Operator Mobile App.

The SAP Warehouse Operator App requires the following Communication Scenarios.

|  |  |  |
| --- | --- | --- |
|  | **Communication Scenario ID** | **Communication Scenario** |
| 1 | SAP\_COM\_0009 | Product Integration |
| 2 | SAP\_COM\_0353 | Warehousing - Process Warehouse Task Integration |
| 3 | SAP\_COM\_0374 | Warehousing - Master Data Integration |
| 4 | SAP\_COM\_0755 | Warehousing - Stock Integration |
| 5 | SAP\_COM\_0364 | Handling Unit Integration |
| 6 | SAP\_COM\_0385 | Warehousing - Inbound Delivery Integration |

Note:

When creating the Communication Arrangement for Scenario SAP\_COM\_0009, untick the ***Service Status*** checkbox to disable **all** Outbound Services. Only Inbound Communication is required for the SAP Warehouse Operator App.

When [Configuring Communication Settings in SAP BTP](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/configuration-tasks#loio6e5e004b6553403486a03da53bfcaf4e__scp) as mentioned in the help document, make sure to add the following Additional Properties as shown below. Properties that are not available in the dropdown list can be added manually.

Note:

The URL mentioned in the SAP Help document is just an example; you need to enter the correct base URL of the services. You can find it in the Service URL / Service Interface column of the Inbound Services section when creating a Communication Arrangement.

The base URL would be for ex: <https://myXXXXXX-api.s4hana.ondemand.com/sap/opu/odata4/sap>

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture-1-1.png)

Configuring Destination in BTP

# Create a Mobile Application

In the above section, you have seen that the SAP Warehouse Operator app uses APIs provided by the SAP S/4HANA Cloud system. These need to be configured in SAP Mobile Services which is part of SAP Business Technology Platform. In this section, you will learn how to configure the mobile destination on SAP Mobile Service for the SAP Warehouse Operator app.

We now create a Mobile Application in SAP BTP Mobile Service.

Log in to your SAP Mobile Services cockpit.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture-1-2.png)

SAP Mobile Services Cockpit

Next, select ‘Native/Hybrid’ from the left panel of the cockpit and create a new entry using the ‘New’ button as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture-1-3.png)

SAP Mobile Services – New Mobile Application

You need to maintain both mandatory fields ‘ID’ and ‘Name’ for basic information.

+ **ID:** com.sap.mobile.apps.warehouseoperator

+ **Name:** SAP Warehouse Operator

Enter the details as displayed below and click ‘Next’.

![](/legacyfs/onli...
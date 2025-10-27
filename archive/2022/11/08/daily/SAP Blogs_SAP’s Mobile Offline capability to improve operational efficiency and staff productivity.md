---
title: SAP’s Mobile Offline capability to improve operational efficiency and staff productivity
url: https://blogs.sap.com/2022/11/07/saps-mobile-offline-capability-to-improve-operational-efficiency-and-staff-productivity/
source: SAP Blogs
date: 2022-11-08
fetch_date: 2025-10-03T21:55:55.920792
---

# SAP’s Mobile Offline capability to improve operational efficiency and staff productivity

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP’s Mobile Offline capability to improve operati...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/156284&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP’s Mobile Offline capability to improve operational efficiency and staff productivity](/t5/technology-blog-posts-by-members/sap-s-mobile-offline-capability-to-improve-operational-efficiency-and-staff/ba-p/13525711)

![former_member17247](https://avatars.profile.sap.com/former_member_small.jpeg "former_member17247")

[former\_member17247](https://community.sap.com/t5/user/viewprofilepage/user-id/17247)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=156284)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/156284)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13525711)

‎2022 Nov 07
7:14 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/156284/tab/all-users "Click here to see who gave kudos to this post.")

2,697

* SAP Managed Tags
* [SAP Mobile Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Services/pd-p/668874921104038800958643358380369)
* [SAP BTP SDK for Android](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520SDK%2520for%2520Android/pd-p/73555000100800001281)

* [SAP Mobile Services

  Software Product Function](/t5/c-khhcw49343/SAP%2BMobile%2BServices/pd-p/668874921104038800958643358380369)
* [SAP BTP SDK for Android

  Software Product](/t5/c-khhcw49343/SAP%2BBTP%2BSDK%2Bfor%2BAndroid/pd-p/73555000100800001281)

View products (2)

These days the smartphone usage has increased adversely and it is expected to grow in the coming years.

Several business process has transformed mobile and is changing people's life throughout the world. Mobile applications are handy to use and allows us to connect from anywhere and everywhere. Most of the applications are internet driven which causes a limitation of usage.

In order to break this boundary and to provide business continuity we can now develop offline mobile applications. You will need internet only during the start and end of the business process. Rest all can function offline. But there is no limitation to fetch real time data while having good internet connectivity.

In this blog, I would like to share my experience in designing an offline application and the lessons learnt during this journey.

SAP provides various offerings to enable this feature. With SAP BTP in existence and the SAP Mobile Service to consume, below were the list of possibilities we considered.

* **SAP Hybrid Application Toolkit**

* **SAP Mobile Development Kit**

* **SAP BTP SDK for native mobile application development**

SAP these days doesn’t recommend their customers to implement new applications with SAP Hybrid Application Toolkit (HAT). Hence, we went for alternatives.

The SAP Mobile Development Kit (MDK) is a tool to build hybrid applications(mobile and web). The code will be written once in SAP BAS and can be rendered on multiple devices as native mobile application on iOS and Android and as web application in a browser. MDK provides a wide range of UI styling. MDK documentation can be referred for the same. As our customer is brand focused, we observed deviations from the possible styling opportunities provided by MDK, so we opted for SAP BTP SDK for Android.

To better understand the approach of the online/offline scenario, I pasted the screenshot of the process flow diagram :-

It is a scenario of Delivery PGI in warehouse management process where the entire open shipment and delivery details for a plant gets downloaded onto the mobile device with which the user can transact. Referred to as initial or full sync. The offline updated data is posted to ECC. SAP Mobile Service delta sync kicks in, to sync the local store with modified records from ECC.

![](/legacyfs/online/storage/blog_attachments/2022/09/Del-PGI-Flow-1.jpg)

Delivery PGI Process Flow

![](/legacyfs/online/storage/blog_attachments/2022/09/Del-PGI-Flow-2.jpg)

Delivery PGI Flow continued...

While designing the offline application, I recommend to segregate the master data APIs and the transactional APIs. The reason being, we call the master data API during the initial login for reusability purposes in comparison to the transactional data which is called when the respective application gets triggered.

Another point to consider, is the size of data that the application is expected to download. It’s a good practice to bring only that fragment of data which you expect to work with. Adding date filters to the API is the best way to target these records and will improve performance.

SAP framework doesn’t allow the utilization of the navigation property of the oData service with offline delta sync functionality. Hence, we split the oData call into multiple APIs and created our local store.

The response format of an oData delta sync call is ATOM+XML whereas the standard SAP oData response call is JSON format. SAP Mobile Service Offline configuration needs alteration to support both.

Value added services to consider:

* A feature to notify the user, when unsynched offline record gets unnoticed, while the user logs off from the application.

* Download feature of erroneous records (Error Archives) helps user track the failed transactions and take appropriate action either via mobile or backend ECC.

Below are few code snippets which I would like to share.

**Android Implementation**

**Step 1: Add SAP BTP Dependencies**

```
implementation group:'com.sap.cloud.android', name:'odata', version: sdkVersion

implementation group: 'com.sap.cloud.android', name: 'offline-odata', version: sdkVersion
```

**Step 2: Initialize SAP Offline Store**

The step below refers to the communication to base URL and creation of offline store.

```
val offlineDELPGIDataProvider = OfflineODataProvider(

        URL("$serviceUrl$GW_OFS_Dest/Z_OFS_DELIVERY_PGI_OFFLINE_SRV_01"),

        offlineODataParameters,

        getClient(),

        delegate

)
```

OffineODataProvider is a 4 parameter class. The object created from this class is used to upload, download, clear the offline database.

**Param 1: URL**

The first parameter is the base url of backend server from where we download data.

Ex: URL("$serviceUrl$GW\_OFS\_Dest/Z\_OFS\_DELIVERY\_PGI\_OFFLINE\_SRV\_01"),

**Param 2: Database configuration**

The second parameter is OfflineODataParameter object in which we define the name of offline store and encryption type.

```
val offlineODataParameters = OfflineODataParameters().apply {

    isEnableRepeatableRequests = false

    storeName = OFFLINE_DEL_PGI_DATASTORE

    currentUser = FlowContextRegistry.flowContext.getCurrentUserId()

    isForceUploadOnUserSwitch = runtimeMultipleUserMode

    isEnableIndividualErrorArchiveDeletion = true

    val encryptionKey = if (runtimeMultipleUserMode) {

        UserSecureStoreDelegate.getInstance().getOfflineEncryptionKey()

    } else { //If is single user mode, create and save a key ...
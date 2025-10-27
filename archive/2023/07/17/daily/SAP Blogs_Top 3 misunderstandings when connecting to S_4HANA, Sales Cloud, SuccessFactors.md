---
title: Top 3 misunderstandings when connecting to S/4HANA, Sales Cloud, SuccessFactors
url: https://blogs.sap.com/2023/07/16/top-3-misunderstandings-when-connecting-to-s-4hana-sales-cloud-successfactors/
source: SAP Blogs
date: 2023-07-17
fetch_date: 2025-10-04T11:52:41.072115
---

# Top 3 misunderstandings when connecting to S/4HANA, Sales Cloud, SuccessFactors

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Top 3 mistakes when connecting to S/4HANA, Sales C...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159192&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Top 3 mistakes when connecting to S/4HANA, Sales Cloud, SuccessFactors](/t5/technology-blog-posts-by-sap/top-3-mistakes-when-connecting-to-s-4hana-sales-cloud-successfactors/ba-p/13554017)

![Dan_Wroblewski](https://avatars.profile.sap.com/d/6/idd630780f059388c9e8e8fa9d85021d5fbf6d51e34b585117ee5e4425f1998531_small.jpeg "Dan_Wroblewski")

![Developer Advocate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Developer Advocate")
[Dan\_Wroblewski](https://community.sap.com/t5/user/viewprofilepage/user-id/72)

Developer Advocate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159192)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159192)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554017)

‎2023 Jul 16
4:00 PM

[16
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159192/tab/all-users "Click here to see who gave kudos to this post.")

1,690

* SAP Managed Tags
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [SAP Sales Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Sales%2520Cloud/pd-p/73554900100700002221)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Sales Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BSales%2BCloud/pd-p/73554900100700002221)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (5)

I've helped many people in the community or during our recent [CodeJam](https://blogs.sap.com/2023/04/13/sap-build-code-jam-is-now-available/) who were trying to connect SAP Build Apps to their SAP backend – like S/4HANA Cloud or SAP Sales Cloud, or SuccessFactors – and there seems to be a few misunderstandings of how SAP Build Apps works. So I want to clear some things up and show you how to quickly connect to S/4HANA Cloud.

## Only Connect Via REST or OData

I've had people ask me how to connect SAP Build Apps with RFCs, or BAPIs, or CDS views or other methods. SAP Build Apps can make connections to REST and OData resources only, so if you can expose your data this way, you'll be OK.

![](/legacyfs/online/storage/blog_attachments/2023/07/dataresources.png)

**Google Firebase** is a special, legacy case (and I assume the connection is made via REST calls) and **Marketplace search** are preconfigured data resources in the Marketplace, themselves either REST or OData services.

**NOTE:** SAP Build Apps can connect to data stores built with SAP Build Apps: Either data models created with [Visual Cloud Functions](https://blogs.sap.com/2022/12/14/unboxing-cloud-functions-in-sap-build-apps/), or [on-device data models](https://www.youtube.com/watch?v=kg-pgIsEhtI) that stores local data on the current device.

## REST and OData Services Are Set Up in Different Places

I think the layout of the **Data** tab has caused some confusion of how to start connecting to backend data resources, especially if a destination is required.

The UI for selecting OData or REST services **without a destination** are right next to each other.

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_17-19-21.png)

But if you are working **with a destination**, which most SAP developers are, the method for setting up the data resource is different and in different places.

For a REST call, you use the same "classic data entities" menu with most of the other data resources, and within the UI you select your destination.

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_17-19-212.png)

But if you want to call an OData service, you need to add an "integration", whose UI is a little bit above and follows a different patter.

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_17-24-05.png)

NOTE: If you want to work with destination, you must enable BTP authentication in the **Auth** tab.

## Your Destination Must Point to OData Service Document

Specifically, someone came to me because they tried to connect their SAP Build Apps to SAP Sales Cloud. Now, I don't know anything about SAP Sales Cloud, but I still looked into it. To be honest, one OData/REST service is pretty much like the other.

Well they first created a destination to the system, and that did not work.

Then they created a destination to a specific OData entity, and that did not work.

That's because when you create a destination to expose OData in SAP Build Apps, you must provide the service document for a specific OData service, for example:

```
https://myServer.s4hana.ondemand.com/sap/opu/odata/sap/API_BUSINESS_PARTNER
```

In SAP Build Apps, this will expose all the entities within this specific OData service (Business Partners).

![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_17-38-53.png)

## How to Connect to S/4HANA Cloud

I've written this before but I'd thought it couldn't hurt to do it again.

I am assuming that you set up a communication user or principal propagation, and set up all the permissions to your S/4HANA Cloud system. I used a technical user for the sake of explaining on SAP Build Apps works, but principal propagation will work, too.

1. Create a destination pointing to your S/4HANA Cloud OData service – remember, to the OData service document – including all the proper additional properties. ![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_17-43-37.png)

2. In SAP Build Apps, enable SAP BTP authentication in the **Auth** tab. ![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_17-46-48.png)

3. In the **Data** tab, click **Add Integration → BTP Destinations**, and select your destination.

   * If the destination is not there, you did not set the additional properties.

   * If it is incompatible format, the URL is not an OData service.

4. Now you can click Add Integration and select the entities you want to expose. You can view real-time data, and you can set up test data.![](/legacyfs/online/storage/blog_attachments/2023/07/2023-07-16_17-51-58.png)

Then you use it like any other data reso...
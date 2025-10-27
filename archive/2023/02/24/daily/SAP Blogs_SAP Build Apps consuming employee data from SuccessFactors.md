---
title: SAP Build Apps consuming employee data from SuccessFactors
url: https://blogs.sap.com/2023/02/23/sap-build-apps-consuming-employee-data-from-successfactors/
source: SAP Blogs
date: 2023-02-24
fetch_date: 2025-10-04T07:58:13.116258
---

# SAP Build Apps consuming employee data from SuccessFactors

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Build Apps consuming employee data from Succes...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159680&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Build Apps consuming employee data from SuccessFactors](/t5/technology-blog-posts-by-sap/sap-build-apps-consuming-employee-data-from-successfactors/ba-p/13555577)

![Alejandro1](https://avatars.profile.sap.com/a/f/idafced0cba95f8154496cc5adf8081a717b74429d46df9af2648acc6ebf290ae6_small.jpeg "Alejandro1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Alejandro1](https://community.sap.com/t5/user/viewprofilepage/user-id/18957)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159680)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159680)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555577)

‎2023 Feb 23
5:49 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159680/tab/all-users "Click here to see who gave kudos to this post.")

6,821

* SAP Managed Tags
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (4)

In this Blog post, I'll dive into the technical details behind the SAP SuccessFactors and SAP Build use case explained in [my previous Blog: Extend SAP SuccessFactors with SAP Build](https://blogs.sap.com/2023/02/20/extend-sap-successfactors-with-sap-build/). Today, I will be showing you step-by-step how to create the application. The goal is to help you better understand the integration and extension capabilities of SAP Build Apps & SAP SuccessFactors and inspire you to start building your own applications.

![](/legacyfs/online/storage/blog_attachments/2023/02/Arquitectura-Build-apps-1.png)

Architecture - SAP Build Apps

To get started, you'll need to create a project in the SAP Build Lobby. This can be done quickly and easily using the pre-built UI components and templates available in the service:

![](/legacyfs/online/storage/blog_attachments/2023/02/Create-Build-Apps-projects-2.gif)

### **Data**

Once you have created the project, the first thing is to enable the data section:![](/legacyfs/online/storage/blog_attachments/2023/02/Build-Apps_Data.png)

To start pulling data for your application, it's important to know which APIs are available and which one best fits your use case. I recommend familiarizing yourself with the [API Business Hub for SuccessFactors](https://api.sap.com/products/SAPSuccessFactors/overview) to explore the APIs and their capabilities.

For this use case, I decided to use the [User Management API](https://api.sap.com/api/PLTUserManagement/overview) to consume employee data from SuccessFactors. With this API, we were able to show and filter the data as I needed:![](/legacyfs/online/storage/blog_attachments/2023/02/API-SFSF-1.png)

By understanding the available APIs and selecting the appropriate one for your use case, you can ensure the success of your custom application with SAP SuccessFactors.

As explained in the [Blog Post: Configuring access to an SAP SuccessFactors API in SAP Build Apps](https://blogs.sap.com/2023/02/01/configuring-access-to-an-sap-successfactors-api-in-sap-build-apps/) by my colleague Antonio Maradiaga, we have two options when integrating SAP Build with SAP SFSF:

1. SAP BTP Destinations

2. SAP API Management

For this example, I have decided to use SAP API Management in order to overcome the CORS Issue but I have tested the BTP Destination and it works fine as you can see:![](/legacyfs/online/storage/blog_attachments/2023/02/SFSF-Destination.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/BTP-Destination.png)

As I mentioned, I’m going to be using SAP API Management. Please review [Antonio’s Blog to configure the API and overcome the CORS Issue](https://blogs.sap.com/2023/02/01/configuring-access-to-an-sap-successfactors-api-in-sap-build-apps/). Once you have done so, please come back and configure the Rest API Call in Build Apps:![](/legacyfs/online/storage/blog_attachments/2023/02/SFSF-API-configuration-in-SAP-Build-Apps-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/SFSF-API-configuration-in-SAP-Build-Apps_2-1.png)

It’s very important that you add the response Key path “d.results” in order to be able to access the results for all employees located from the Madrid office as it’s filtered in the query parameter. Feel free to explore other options to filter the API.

Let's setup another API for the User Details screen, so we can pull all data for a specific user:![](/legacyfs/online/storage/blog_attachments/2023/02/SFSF-API-per-User-ID-configuration-in-SAP-Build-Apps-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/SFSF-API-per-User-ID-configuration-in-SAP-Build-Apps_v2-1.png)

In this case, as the API only recovers one employee you only need to add in the Response key path “d” as we don’t have more results.

####

### Variables

Let’s go back to the UI Canvas and let’s start defining the variables that we need for the project:![](/legacyfs/online/storage/blog_attachments/2023/02/Variables.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/app-variables-for-later-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/build-apps-data-variables-1.png)

###

### **UI Interface for the initial Screen**

Let’s go back to the UI Canvas and start building up the UI Interface. I have used the following elements:![](/legacyfs/online/storage/blog_attachments/2023/02/UI-Canvas.png)

* “*Title*” for adding Compliance Form text as a header.

* *“Row”* below the Title so I can add two *“Text”* (Employee Name and Email Addres).

* *“Container”* below the Row with the text and inside the container we add *“Icon List Item”* and a *“Button”*

Next, we are going to define the container as an item that repeats with any result that bring the API *“SFSF\_Users\_Spain”* that we have created in the Data section:

*Select the container > Repeat with icon > Data and Variables > Data Variable > SFSF\_Users\_Spain*

![](/leg...
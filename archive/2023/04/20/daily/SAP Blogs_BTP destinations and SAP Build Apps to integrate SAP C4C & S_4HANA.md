---
title: BTP destinations and SAP Build Apps to integrate SAP C4C & S/4HANA
url: https://blogs.sap.com/2023/04/19/btp-destinations-and-sap-build-apps-to-integrate-sap-c4c-s-4hana/
source: SAP Blogs
date: 2023-04-20
fetch_date: 2025-10-04T11:33:07.367890
---

# BTP destinations and SAP Build Apps to integrate SAP C4C & S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* BTP Destinations and SAP Build Apps to integrate S...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158422&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BTP Destinations and SAP Build Apps to integrate SAP C4C & S/4HANA](/t5/technology-blog-posts-by-sap/btp-destinations-and-sap-build-apps-to-integrate-sap-c4c-s-4hana/ba-p/13551925)

![sobhapujari1818](https://avatars.profile.sap.com/3/3/id333a877a0b34cc12a6a5c0384cfef5b885d4f0a1f58e18d5d6e893d93b659cbd_small.jpeg "sobhapujari1818")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[sobhapujari1818](https://community.sap.com/t5/user/viewprofilepage/user-id/795373)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158422)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158422)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551925)

‎2023 Apr 19
11:34 PM

[19
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158422/tab/all-users "Click here to see who gave kudos to this post.")

12,617

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

View products (1)

**Introduction:** In today's digital world, businesses are looking for ways to streamline their processes and enhance their customer experience. One way to achieve this is through the integration of different systems. In this blog post, we will explore how to integrate SAP C4C and S/4 HANA using BTP destinations and SAP Build apps.

To integrate SAP C4C and S/4 HANA, we can use BTP (Business Technology Platform) destinations and SAP Build Apps.

**BTP destinations** are endpoints that define how to connect to a remote system or service. BTP Destinations are typically used in cloud-based scenarios where different cloud services need to communicate with each other securely. They provide a way to define the connection details for target systems such as the endpoint URL, authentication credentials, and other settings. BTP Destinations can be created and maintained using the SAP Cloud Platform cockpit or SAP Cloud SDK. They can be used in various scenarios, such as connecting to remote data sources, invoking external web services, or sending notifications to third-party systems.

**SAP Build Apps** is a visual programming environment where citizen and professional developers can build enterprise-ready custom software without writing any code. It makes it easier for users to create engaging and functional SAP Fiori apps without the need for extensive technical expertise or coding knowledge. It provides a streamlined and collaborative design process that helps organizations deliver high-quality apps faster and more efficiently.

You can sign up for a free trial of SAP Build to get hands-on experience with the tool. The trial account provides access to all the features and functionalities of SAP Build, allowing you to create and prototype your own SAP Fiori apps. You can find it [here](https://www.sap.com/products/technology-platform/low-code.html).

For Quick on-boarding & Certification to SAP Build you can refer to the blog post [SAP Build Low-code/No-code Applications](https://blogs.sap.com/2023/01/05/sap-build-low-code-no-code-applications-and-automations-sap-certification/).

Let us quickly get into our use case.

**Use Case:** An SAP Build App is embedded into the Agent desktop screen in C4C tenant where you will be able to view the S/4HANA transactions like Sales Orders, Customer Returns, Outbound Deliveries etc based on the Customer like below.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture1-54.png)

Let’s take an example of integrating Sales orders from S/4HANA in to C4C screen.

**Step 1**: Set up the BTP Destination in the BTP Sub account.

You can follow below steps:

* Open the SAP Cloud Platform Cockpit and log in to your BTP sub-account.

* Navigate to the "Destinations" page under the "Connectivity" tab.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture2-37.png)

* Click on the "New Destination" button to create a new destination.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture3-34.png)

* In the "Destination Name" field, enter a name for your destination.

* In the "Type" field, select "HTTP" as the destination type.

* In the "Description" field, enter a brief description of your destination.

* In the "URL" field, enter the URL of the S/4HANA Sales order API ([https://myXXXXXX.s4hana.ondemand.com/sap/opu/odata/sap/API\_SALES\_ORDER\_SRV)that](https://myXXXXXX.s4hana.ondemand.com/sap/opu/odata/sap/API_SALES_ORDER_SRV%29that) you want to integrate.

* In the "Proxy Type" field, select "Internet" as the proxy type.

* In the "Authentication" section, select "BasicAuthentication" as the authentication method.

* Enter the username and password credentials for the API service.

* In the "Additional Properties" section, add the following key-value pairs:

  + "WebIDEEnabled": "true"

  + “HTML5.DynamicDestination” :"true"

  + "AppgyverEnabled" :"true"

![](/legacyfs/online/storage/blog_attachments/2023/04/new-1.png)

* These properties will allow you to access the API service using the SAP Web IDE.

* Click on the "Save" button to save your destination.

* Once you set up, you can click Check Connection to see if the Connection is Successful.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture5-27.png)

**Step 2**: Create an Appgyver app with basic screens to display the values from the S/4HANA. Add a list view to the page to display the results and a page parameter to read the Account id and Query the Sales orders based on Account ID. Here are some steps to follow.

* Create a new page in Appgyver by selecting "Create New Page" from the Pages menu.

* Name the page and select a layout that will suit your needs.![](/legacyfs/online/storage/blog_attachments/2023/04/Picture6-23.png)

* Add a container component to the page to hold the sales order query results.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture7-22.png)

* You can create a page Parameter to read the Account id from the C4C Screen and pass that to S/4HANA system to query sales orders based on Account.

* Next we have to enable BTP Authentication. click on the AUTH tab -> Enable Authentication

![](/legacyfs/online/storage/blog_attachments/2023/04/1-62.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/2-27.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/3-25.png)

* Add the BTP destination created in the Previous step by clicking on the Data tab -> Add integration.

![](/legacyfs/online/storage/blog_attachments/2023/04/new1.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/new2.png)

* Then select the BTP Destination you have created.

![](/legac...
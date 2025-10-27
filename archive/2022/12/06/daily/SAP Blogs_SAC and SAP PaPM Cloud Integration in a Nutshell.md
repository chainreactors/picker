---
title: SAC and SAP PaPM Cloud Integration in a Nutshell
url: https://blogs.sap.com/2022/12/05/sac-and-sap-papm-cloud-integration-in-a-nutshell/
source: SAP Blogs
date: 2022-12-06
fetch_date: 2025-10-04T00:34:28.370105
---

# SAC and SAP PaPM Cloud Integration in a Nutshell

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* SAC and SAP PaPM Cloud Integration in a Nutshell

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/8040&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAC and SAP PaPM Cloud Integration in a Nutshell](/t5/financial-management-blog-posts-by-sap/sac-and-sap-papm-cloud-integration-in-a-nutshell/ba-p/13567273)

![paulgabog](https://avatars.profile.sap.com/3/c/id3c43d9d8ff0a5f25ba5dc49963670f9342c29b6c3a7da58a805261c2e64a54ca_small.jpeg "paulgabog")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[paulgabog](https://community.sap.com/t5/user/viewprofilepage/user-id/622792)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=8040)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/8040)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567273)

‎2022 Dec 05
7:08 PM

[20
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/8040/tab/all-users "Click here to see who gave kudos to this post.")

13,938

* SAP Managed Tags
* [SAP Profitability and Performance Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Profitability%2520and%2520Performance%2520Management/pd-p/73555000100800000092)

* [SAP Profitability and Performance Management

  SAP Profitability and Performance Management](/t5/c-khhcw49343/SAP%2BProfitability%2Band%2BPerformance%2BManagement/pd-p/73555000100800000092)

View products (1)

Do you want to know *How to utilize the Calculation prowess of SAP Profitability and Performance Management Cloud (SAP PaPM Cloud) and use the processed data for SAP Analytics Cloud (SAC) reporting*, and analysis and have no idea yet where to start or how it can be achieved? Well, this blogpost is for you!

As context, SAC recently released a [MultiAction step to support API calling](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/b1a98c566bc64ce78871ee3c0b559d6f.html#create-a-multi-action) which meant that we now have the possibility to make use of SAP PaPM Cloud's configured process without the need to trigger the execution of process manually in Process Management but directly to your SAC Story. Isn't it good news?

In this blogpost, I will give you a digestible End to End (E2E) scenario which can be used as your baseline in order to achieve SAC and SAP PaPM Cloud integration in a nutshell**.**

Let's dive in!

![](/legacyfs/online/storage/blog_attachments/2022/12/SAC-Story.png)

The goal of this example is to produce a simple comparison simulation story in SAC, like the one above, which can be leveraged for presentation purposes. In this example, it will consist of three components:

1) **INPUT** : Data from SAC Planning Model is available for comparison

2) **TRIGGER** : Multi Action with SAP PaPM Cloud’s API in order to execute the Process Execution remotely.

3) **RESULT** : Output Data from SAC Planning Model wherein data comes from a Query Function in SAP PAPM Cloud.

This report looks neat, isnt it? With just a click of the trigger button everything will be executed simultaneously. Now the question is “What is the process to be able to configure such a report?”.

To continue with it, this easy looking presentation is achieved based on the technical diagram below.

![](/legacyfs/online/storage/blog_attachments/2022/12/Technical-Diagram-1.png)

If you are into some technical stuff, then the diagram above might be easy to digest for you but for the sake of all our diverse readers let me explain it a bit. There are two types of arrows in the above technical diagram:

1. **Solid arrow (Calling)** means that the arrow-tail calls the service from the arrowhead (e.g. SAC calls SAP PaPM Cloud API Service to trigger the Process Activity).

2. **Broken arrow (Data Flow)** means that the arrow-tail is the source of data which flows to the arrowhead. (e.g. SAC provides input data to SAP PaPM for data processing)

For visual learners like myself, I prepared a visual ption which catches the same meaning as the technical diagram above. This diagram tells a story on how the two solutions are interconnected.

![](/legacyfs/online/storage/blog_attachments/2022/12/Final-Visual-Diagram.png)

Considering both the technical and visual diagram presented above, I will explain the process on how the APIStep MultiAction of SAC can be used and setup in an orderly manner.

Since the goal is the automated run of processes using a click of a button, user can start with [configuration of MultiAction Planning trigger within a SAC Story](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/bfbd4e31cd2e4bf0879dfb0a6b692b9a.html).

![](/legacyfs/online/storage/blog_attachments/2022/12/SAC-Story-Trigger.png)

Once user clicks this button the underlying list of activities will start sequentially.

### **Step 1 - SAC Planning Model with data is available for consumption in SAP PaPM Cloud**

To start of, existing SAC Planning Model where relevant data for calculation in SAP PaPM Cloud should be available. This model can be reused from previous SAC Planning models or by creating a new one. To create a new SAC Planning Model, you may refer to help document guide as starting point: [How to Create Planning Models from Blank Models](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/235bb144e9d44b46af5d26053b030b3c.html)

Data here will be then used in next step.

![](/legacyfs/online/storage/blog_attachments/2022/12/SAC-Planning-Input-Model.png)

###

### **Step 2 - Model View OData (MV OData) function will run which will read data from SAC Planning Model**

The configuration of MV OData in Modeling entails **ONE TIME configuration of SAC Data Export Service in SAC side**. All other configuration details are included in the separate blogpost [How to setup Model View OData](https://blogs.sap.com/2022/06/02/how-to-setup-model-view-odata/).

![](/legacyfs/online/storage/blog_attachments/2022/12/MVOData.png)

### **Step 3 - SAC triggers SAP PaPM API service..**

The API Step Multi Action is configured here containing the step which requires a **ONE TIME setup of HTTP API connection** pointing to your subaccount where authentication to run SAP PaPM API is configured. See Blogpost [Integrate remote application via API step of Multi Actions](https://blogs.sap.com/2022/10/27/integrate-remote-application-via-api-step-of-multi-actions/) for detailed steps.

![](/legacyfs/online/storage/blog_attachments/2022/12/MultiAction-API-Trigger-Process-1.png)

### **Step 4 SAP PaPM Execution Process starts..**

Once the API Step Multi Action is executed, SAP PaPM Cloud execution activity will be triggered in the background. Data processing is being done here which in turn will contain the input data for the Query Function.

![](/legacyfs/online/storage/blog_attachments/2022/12/PaPM-Process-Instance-Execution.png)

...
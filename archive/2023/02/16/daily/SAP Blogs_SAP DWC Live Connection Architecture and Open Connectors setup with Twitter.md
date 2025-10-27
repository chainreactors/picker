---
title: SAP DWC Live Connection Architecture and Open Connectors setup with Twitter
url: https://blogs.sap.com/2023/02/15/sap-dwc-live-connection-architecture-and-open-connectors-setup-with-twitter/
source: SAP Blogs
date: 2023-02-16
fetch_date: 2025-10-04T06:45:51.731454
---

# SAP DWC Live Connection Architecture and Open Connectors setup with Twitter

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP DWC Live Connection Architecture and Open Conn...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163454&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP DWC Live Connection Architecture and Open Connectors setup with Twitter](/t5/technology-blog-posts-by-members/sap-dwc-live-connection-architecture-and-open-connectors-setup-with-twitter/ba-p/13569963)

![former_member212011](https://avatars.profile.sap.com/former_member_small.jpeg "former_member212011")

[former\_member212011](https://community.sap.com/t5/user/viewprofilepage/user-id/212011)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163454)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163454)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569963)

‎2023 Feb 15
10:24 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163454/tab/all-users "Click here to see who gave kudos to this post.")

2,876

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [Open Connectors](https://community.sap.com/t5/c-khhcw49343/Open%2520Connectors/pd-p/73555000100800001531)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [Open Connectors

  SAP Business Technology Platform](/t5/c-khhcw49343/Open%2BConnectors/pd-p/73555000100800001531)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (3)

**Introduction**

This blogpost is concentrated mainly on the explanation of Live connection architecture in SAP DWC and how to setup the live connections using Open Connectors with Twitter. Live connection setup helps business analyze the data sets appearing in Datawarehouse Cloud from multiple source systems, both SAP and non-sap.

Using SAP DWC you can implement hybrid landscape architecture for the organization under single umbrella. With the advancement of on-premise SAP BW systems on cloud applications SAP suggests using DWC for future reporting applications eg. SAC. SAP DWC integrates very easily with the SAP source systems but when it has to connect with non-SAP source systems then you need to setup additional parameters for it. Before setting up any connection in DWC please go through the Workspace concept once from developers point of view.

SAP DWC works as a single point of entry for all sets of data from different source systems and hence is super powerful from the data modeling perspective on Cloud which offers more advanced ETL capabilities. With its tight coupling with SAC which offers primarily data consumption, reporting and Financial Planning functionalities you can expose the analytical data models created in DWC for further reporting. At the backend DWC uses SDA (Smart Data Access) and SDI (Smart Data Integration) for virtual and physical data replications respectively.

**SAP DWC Connections Compatibility Matrix for different connection types**

[Preparing Connectivity for Connections | SAP Help Portal](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/9f804b8efa8043539289f42f372c4862/bffbd58c15784a62af0520f171018ded.html)

DP Agent configuration is only needed to connect the source systems when physical replication of data is required in SAP DWC. And, SAP Basis admin needs to perform the configuration in Cloud Connector when virtual replication is required, eg. creating Data Flows in DWC using views. Cloud connector setup is done using BTP cockpit, a one time setup. The scenario remains same for setting up connections in mobile phones (iOS or android) / tablets. Implementing Cloud connector will help you bypass the firewall using a Tunnel connection. Direct connection has less data latency issues compared to the Tunnel connection.

Below diagrams show the overall connection architecture (simplified and detailed) which is needed to connect SAP systems with DWC.

![](/legacyfs/online/storage/blog_attachments/2023/02/1-17.jpg)

Live Connection Architecture

![](/legacyfs/online/storage/blog_attachments/2023/02/2-11.jpg)

All the connections in SAP DWC are allocated to a specified workspace. A workspace is a secure area created by DWC Administrator, in which members can acquire, prepare, and model data. The Administrator allocates disc and in memory storage to the space, set its priority, and can limit how much memory and how many threads its statements can consume.

Tip- Check the Prerequisites and Compatibility Matrix of the source systems needed to connect with SAP DWC.

Once you are logged in to DWC, navigate to the Connections from left hand side panel. Select the workspace where connection needs to be built. Pass on the mandatory parameters of source system and Cloud Connector.

![](/legacyfs/online/storage/blog_attachments/2023/02/3-6.jpg)

Connection

Now Validate the connection by clicking on the Validate button in above screen. If no issues encountered then the connection will be successful and a prompt will appear.

If DP Agent is not setup then below screenshot should match with the connection parameters after successful connection.

![](/legacyfs/online/storage/blog_attachments/2023/02/4-3.jpg)

DP Agent not configured

**Open Connectors-**It can connect any non-sap system using APIs. The configuration for Open connectors is done via BTP cockpit. If you have access to the BTP cockpit then even Trial account can be used. Open Connectors empowers DWC and provides enormous capabilities to connect any non-sap source systems. In case SAP provided open connectors does not fulfill the requirements then custom Open Connectors can also be built.

![](/legacyfs/online/storage/blog_attachments/2023/02/5-2.jpg)

Note that inside BTP cockpit, subscriptions need to be added to the Integration Suite.

Meanwhile, in the same browser login to the Twitter account. Using the cookies while performing next steps for configuring Open Connectors we need to authorize access to the Twitter account.

![](/legacyfs/online/storage/blog_attachments/2023/02/6-3.jpg)

Create Sub-Account inside the main account & Add Instances and Subscriptions.

![](/legacyfs/online/storage/blog_attachments/2023/02/7-1.jpg)

SAP BTP Cockpit

![](/legacyfs/online/storage/blog_attachments/2023/02/8-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/9-1.jpg)

Subscription

Click on Integration Suite in the above screenshot to login. Integration Suite is a complete package inbuilt in BTP cockpit to connect any Cloud/ API/ non-SAP products directly with SAP DWC.

![](/legacyfs/online/storage/blog_attachments/2023/02/10-1.jpg)

SAP Integration Suite

Landing page will appear like below showing multiple connector options.

![](/legacyfs/online/storage/blog_attachments/2023/02/11-1.jpg)

Open Connectors

Please click on the required connector. Click...
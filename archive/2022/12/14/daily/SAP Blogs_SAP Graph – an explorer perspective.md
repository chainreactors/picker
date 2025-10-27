---
title: SAP Graph – an explorer perspective
url: https://blogs.sap.com/2022/12/13/sap-graph-an-explorer-perspective/
source: SAP Blogs
date: 2022-12-14
fetch_date: 2025-10-04T01:23:57.306406
---

# SAP Graph – an explorer perspective

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Graph – an explorer perspective

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157314&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Graph – an explorer perspective](/t5/technology-blog-posts-by-sap/sap-graph-an-explorer-perspective/ba-p/13549076)

![ianbunker](https://avatars.profile.sap.com/b/7/idb7ec42d075fadd93aeb2b581e1925cc576eb692466e9ea6396ed02fada354dc6_small.jpeg "ianbunker")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ianbunker](https://community.sap.com/t5/user/viewprofilepage/user-id/46008)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157314)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157314)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549076)

‎2022 Dec 13
8:41 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157314/tab/all-users "Click here to see who gave kudos to this post.")

3,396

* SAP Managed Tags
* [SAP Graph](https://community.sap.com/t5/c-khhcw49343/SAP%2520Graph/pd-p/da20f5de-7c9f-47c9-b766-b98820e5be12)

* [SAP Graph

  Topic](/t5/c-khhcw49343/SAP%2BGraph/pd-p/da20f5de-7c9f-47c9-b766-b98820e5be12)

View products (1)

This blog is written from the perspective of a complete novice of SAP Graph and its capabilities and covers the learnings and observations while following some of the excellent training and reference material available [1,3,4]. Including building and testing a free tier SAP Graph instance.

SAP Graph is an enabler for businesses and business users to build applications primarily accessing SAP information from multiple line of business (LOB) systems for example SAP S/4HANA Cloud, SAP Success Factors, SAP S/4HANA [15]. SAP Graph is configured (by an Administrator) to connect to these systems and after a ‘collection run’ provides API paths to interrogate the data and help rapidly build business applications, for example, through low code/no code techniques such as SAP AppGyver[8].

**SAP Graph – how to set it up?**

The initial setup of an SAP Graph instance is relatively straight forward and if already using SAP BTP (who isn’t!) will be very familiar – search for the service and select the plan that matches requirements. Initially, there is a free tier plan available to trial out and become familiar; however, I did find that there is a requirement on the SAP BTP Account itself – needs global administrator access (not trial account), as when creating the SAP Graph instance, a new subaccount is provisioned. Under the hood you can see numerous technology elements are provisioned such as Cloud Foundry, Kyma, Kubernetes (K8s).

![](/legacyfs/online/storage/blog_attachments/2022/12/img1_graph-plan.jpg)

Also, note the region which SAP Graph is deployed in, for example, if connecting to existing subaccounts. At the time of these investigations the Europe region was the only one available, but more regions will/have subsequently become available such as CF-US10 (US-East).

Once up and running there are several administrator level tasks that need to take place. This is around the area of connecting to the LOB systems that are the data sources. In the referenced training material, there are good examples of the steps to follow and include template accelerators for prefilling in a lot of the fields. The templates are available for download from GitHub. Without the templates, determining the right input values will be a “difficult” task.

![](/legacyfs/online/storage/blog_attachments/2022/12/img2_graph-connectivity.jpg)

*\*Note cxsales namespace has been renamed to c4c since May 2022*

In the training material followed,[1] there are examples for connecting to SAP sandbox systems and this was a straightforward task, mainly due to access and security considerations being relaxed. In a real-world example, how the data is to be accessed is a critical consideration. The process for determining the appropriate access setup is shown in the training demonstrations through a flow chart, for example whether to use email authentication or configure service accounts.

![](/legacyfs/online/storage/blog_attachments/2022/12/img3_graph-authorisation.jpg)

SAP Graph does not manage users themselves or directly authenticate with the connecting client. Business user authorization is in the responsibility of the source system. The advantage of this is existing user authorizations are maintained even in the usage of the technical user, the data that the technical user can access is maintained and controlled within the source system itself. The ability for SAP Graph to perform updates [12] to data is a relatively recent innovation and this builds further on ensuring the access setup is appropriate.

**Overview of the access process**

* SAP Graph uses token-based authentication, based on OAuth 2.0. To interact securely with SAP Graph, a client application must present an access token (A), as shown below. The token represents the authorization of the client process to access data.

![](/legacyfs/online/storage/blog_attachments/2022/12/img4_graph-sources_c.jpg)

*\*Multiple data sources shown, can be single source*

* SAP Graph communicates securely with data sources in the landscape on behalf of the client (B); as per the destinations configured in SAP Graph.

* You need users in the system(s) for a scenario to work. SAP Graph does not manage user identities and it cannot directly authenticate clients. Instead, it relies on the XSUAA, SAP Authorization and Trust Management Service to do that. By setting a trust relationship to XSUAA, SAP Graph accepts the identities verified by XSUAA and passed to it in the form of bearer tokens. It supports token-based authentication

Once the connectivity is in place, the next step is to interrogate the source systems and build the data model. This is done though a command line interface *graphctl* similar to many cloud cli’s. the high-level process is to logon to the appropriate account through the cli and use the command to generate the model file and then run another command to activate and actually create the model. This 2-step approach gives you the opportunity to edit the model file if desired, remove/rename entities etc.

![](/legacyfs/online/storage/blog_attachments/2022/12/img5_graph-cli.jpg)

The activation time obviously depends on how many LOBs or instances are being connected and the amount of data. One thing to note, the model when built will only find data it has access to, if it can’t see it, it’s not in the model. Initially, this means the connections setup will likely have very high and widespread authorizations – once configured this should be closed down as appropriate.

**SAP Graph – accessing the data**

Once SAP Graph is up and running *graphctl* can be used to check status and run commands for normal administration functionality. The data model is also available to interrogate and access through tools such as Postman or if more code o...
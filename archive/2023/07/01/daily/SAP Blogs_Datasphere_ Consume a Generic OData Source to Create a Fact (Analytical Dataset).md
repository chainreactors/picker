---
title: Datasphere: Consume a Generic OData Source to Create a Fact (Analytical Dataset)
url: https://blogs.sap.com/2023/06/30/datasphere-consume-a-generic-odata-source-to-create-a-fact-analytical-dataset/
source: SAP Blogs
date: 2023-07-01
fetch_date: 2025-10-04T11:53:51.230765
---

# Datasphere: Consume a Generic OData Source to Create a Fact (Analytical Dataset)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Datasphere: Consume a Generic OData Source to Crea...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164529&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Datasphere: Consume a Generic OData Source to Create a Fact (Analytical Dataset)](/t5/technology-blog-posts-by-sap/datasphere-consume-a-generic-odata-source-to-create-a-fact-analytical/ba-p/13570327)

![merza](https://avatars.profile.sap.com/c/e/idce35b688ab7e2f4f8232b4f493f126ed87be97ec6c3019e68233d55f689134b9_small.jpeg "merza")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[merza](https://community.sap.com/t5/user/viewprofilepage/user-id/16662)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164529)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164529)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570327)

‎2023 Jun 30
10:10 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164529/tab/all-users "Click here to see who gave kudos to this post.")

8,793

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)

* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (2)

## 0. Introduction

In today's data-driven business landscape, the ability to seamlessly integrate and analyze vast amounts of data has become paramount for organizations seeking to unlock valuable insights. SAP Datasphere (DSP) emerges as a powerful solution, providing a unified and scalable platform for data warehousing and analytics. To fully leverage the potential of DSP, establishing an efficient connections to external data sources is crucial. One such method is utilizing the OData protocol, a widely adopted standard for data exchange and integration.

This technical article aims to demystify the process of creating and consuming OData connections within SAP Datasphere. By following our step-by-step guide, you will gain the knowledge and confidence to create and deploy a consumable a Fact (aka Analytical Dataset) in DSP based on a generic OData connection.

## 1. Select the Datasource

From you desired datasource, you need the following details:

1. Host URL of the remote OData Service

2. OData version: V2, V3 or V4

3. Authentication type and details

For our test-case scenario, we'll use the well known [Northwind OData test service](https://services.odata.org/V2/Northwind/Northwind.svc/).

## 2. Create the Connection

In DSP, go to Connections -> Create -> search for "odata"

![](/legacyfs/online/storage/blog_attachments/2023/06/odataConnection.png)

Then enter the details as the following

![](/legacyfs/online/storage/blog_attachments/2023/06/odataConnection2.png)

Hint: note that the default Northwind service URL is of version 3. We needed to change this manually in the URL to V2, since V3 is not supported in Datashpere. Otherwise, the entities would be recognized inside the connection, but no data could be fetched:

![](/legacyfs/online/storage/blog_attachments/2023/06/odataError.png)

##

## 3. Consume the Connection in Data Builder

If we try to create a Graphical View using the created OData connection, no entities can be read from the connection. To get more details, we validate the connection in the Connections tile, and we get the following warning:

![](/legacyfs/online/storage/blog_attachments/2023/06/remoteWarning.png)

So the reason is that the Graphical View tried to access the data remotely, which faces an SSL issue because the requested service will be accessed through HTTPS (<https://services.OData.com>), as described in this [help page](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/46f5467adc5242deb1f6b68083e72994.html?locale=en-US).

### Solution-1: Security Certificate

Download the certificate of the OData service and upload it in DSP as given in the previous given help page. However, you will need for this the DW Administrator role. So if don't have it, move to the 2nd solution.

### Solution-2: Create a Data Flow First

The Data Flow has an ETL behaviour in replicating data. So the connection's entities and their data can be accessed and consumed successfully.

![](/legacyfs/online/storage/blog_attachments/2023/06/df.png)

After applying the operators that you need (join, project, ..) as part of the Data Flow, you need to add a target table, Create & Deploy it, and finally **Run** the flow.

## 4. Now, you can create your Fact (Analytical Dataset)

The created and deployed table NW\_Orders (visible on the previous Figure) can now be found while creating a Graphical View, and it be can consumed with its data to create a Fact.

![](/legacyfs/online/storage/blog_attachments/2023/06/graphView.png)

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fdatasphere-consume-a-generic-odata-source-to-create-a-fact-analytical%2Fba-p%2F13570327%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [From REST to Datasphere: A CAP-based Integration Approach](/t5/technology-blog-posts-by-members/from-rest-to-datasphere-a-cap-based-integration-approach/ba-p/14218922)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [Unsupported Features with SAP Datasphere Live Connections in SAP Analytics Cloud](/t5/technology-blog-posts-by-members/unsupported-features-with-sap-datasphere-live-connections-in-sap-analytics/ba-p/14228053)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [My expert playlist, SAP TechEd, Berlin](/t5/technology-blog-posts-by-members/my-expert-playlist-sap-teched-berlin/ba-p/14226668)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [$count not returned anymore in OData calls to analytical models in SAP Datasphere](/t5/technology-q-a/count-not-returned-anymore-in-odata-calls-to-analytical-models-in-sap/qaq-p/14227580)
  in [...
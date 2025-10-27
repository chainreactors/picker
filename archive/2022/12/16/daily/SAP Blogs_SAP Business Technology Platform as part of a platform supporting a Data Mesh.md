---
title: SAP Business Technology Platform as part of a platform supporting a Data Mesh
url: https://blogs.sap.com/2022/12/15/sap-business-technology-platform-as-part-of-a-platform-supporting-a-data-mesh/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:40:13.162515
---

# SAP Business Technology Platform as part of a platform supporting a Data Mesh

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Business Technology Platform as part of a plat...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157588&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Business Technology Platform as part of a platform supporting a Data Mesh](/t5/technology-blog-posts-by-sap/sap-business-technology-platform-as-part-of-a-platform-supporting-a-data/ba-p/13549813)

![andreas_engel](https://avatars.profile.sap.com/5/3/id53ebb6a24838b65dc95fe2f8459257f658958c514a2bddc23999d6080118b2f1_small.jpeg "andreas_engel")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[andreas\_engel](https://community.sap.com/t5/user/viewprofilepage/user-id/301006)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157588)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157588)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549813)

‎2022 Dec 15
6:40 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157588/tab/all-users "Click here to see who gave kudos to this post.")

2,972

* SAP Managed Tags
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [Big Data](https://community.sap.com/t5/c-khhcw49343/Big%2520Data/pd-p/139269250608756787992873)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Big Data

  Topic](/t5/c-khhcw49343/Big%2BData/pd-p/139269250608756787992873)
* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

# **Why to read this blog**

In his [blog series](https://blogs.sap.com/2022/06/04/more-than-just-a-hype-data-mesh-as-a-new-approach-to-increase-agility-in-value-creation-from-data/) on Data Mesh Wolfgang Epting gives a comprehensive and detailed introduction to Data Mesh and which components in the SAP Business Technology Platform (SAP BTP)  can be leveraged as foundation to implement Data Mesh in an organization.

In this blog I wanted to add an additional angle to the discussion. While the phrase “The winner takes is all” might be true in many areas of life, this mustn’t be the case in the context of a Data Mesh project. The question which technology to leverage to implement a Data Mesh is not an either-or question. SAP BTP is well suited to be leveraged as part of a ‘bigger’ platform supporting a Data Mesh implementation.

Concerning wording:

I use term BTP based data products for data products hosted on SAP Business Technology Platform (as described in Wolfgang’s [blog series](https://blogs.sap.com/2022/06/04/more-than-just-a-hype-data-mesh-as-a-new-approach-to-increase-agility-in-value-creation-from-data/)).

# **Data Mesh leveraging SAP and Non-SAP Technology**

Looking at your data from a (SAP-biased) bird’s view there are domains mainly residing in SAP Systems and others in non-SAP Systems. When starting your Data Mesh project with data products in the non-SAP area, non-SAP technology could be the best choice to build your initial data products. Your Data Mesh initiative is initially based on non-SAP technology.

As soon as you start to include data products and domains residing in SAP systems (S/4HANA or ECC or ERP, and SAP Data Warehouses), you should consider leveraging SAP-Technology. Here is why:

* Not only do SAP systems contain high value data, but they also contain domains and domain knowledge. I.e, SAP S/4HANA contains business and entity data models for customer data in a company.

* Out-of-the box data products are delivered as content packages (in SAP Analytic Cloud and SAP Datawarehouse Cloud see Wolfgang’s [blog series](https://blogs.sap.com/2022/06/04/more-than-just-a-hype-data-mesh-as-a-new-approach-to-increase-agility-in-value-creation-from-data/)), which can be tailored to your needs.

* SAP BTP offers supreme out-of-the-box integrations to SAP systems, enabling easy re-use of the semantic models and domain data models as well as virtual real-time access to the actual data.

Your Data Mesh will be built on SAP and non-SAP technology. The combination of both technologies will serve your needs best.

[Remark: As explained in Wolfgang’s [blog series](https://blogs.sap.com/2022/06/04/more-than-just-a-hype-data-mesh-as-a-new-approach-to-increase-agility-in-value-creation-from-data/), SAP BTP can be leveraged for non-SAP data as well, especially to build data products containing SAP and  non-SAP-Data. If most of your data products rely on data in SAP Systems, leveraging only SAP BTP for your Data Mesh initiative is an option, you should consider.]

Here is how SAP BTP fits into a Data Mesh platform combining SAP BTP and non-SAP technology. Let me go through the 4 pillars of Data Mesh to explain how the pieces fit together.

## **Domain-oriented decentralized data ownership and architecture**

Domain Ownership is a key principle for a Data Mesh. To view SAP S/4HANA or ECC or ERP and SAP Data Warehouse systems only as data provider is too short sighted. These systems contain domains and domain knowledge. The users of these systems are domain experts, both on the IT as well as on the business side. SAP systems serve as trusted source of information on customers, products, equipment and many more domains.

Therefore, all the domain knowledge within your SAP eco system (IT and LOB) in your company can be leveraged by including SAP experts in your domain teams. Technically the well-established SAP data and semantic models can - and should be - reused for building data products.

![](/legacyfs/online/storage/blog_attachments/2022/12/DomainandDaaP.png)

Figure 1: SAP Business Technology Platform as part of a 'bigger' Data Mesh: Domain Ownership and Data as a Product

## **Data as a Product**

SAP S/4HANA or ECC or ERP and SAP Business Warehouse systems are a great source to build source-oriented data products. Data products for data in SAP Systems can be best build (see above) based on the SAP BTP.

SAP Data Catalog entries can be published/integrated via APIs to/with an Enterprise Data Catalog leveraged in a Data Mesh.  BTP based data products can be easily consumed by standard APIs and within a Data Mesh.

## **Self-serve data infrastructure as a platform**

Provisioning of underlying the platform based on a self-serve data infrastructure is another key pillar for a Data Mesh initiative. The SAP Business Technology Platform does not offer Infrastructure as a Service, but all services can be provisioned either via automation based on scripts or in a self-serve manner. The infrastructure and resources needed for the services are provisioned alongside with the service.

Scripts for provisioning the SAP BTP services can be included in an overarching approach for pro...
---
title: SAP Datasphere – Q&A and Partnerships
url: https://blogs.sap.com/2023/03/12/sap-datasphere-qa-and-partnerships/
source: SAP Blogs
date: 2023-03-13
fetch_date: 2025-10-04T09:25:14.773113
---

# SAP Datasphere – Q&A and Partnerships

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Datasphere - Q&A and Partnerships

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163552&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere - Q&A and Partnerships](/t5/technology-blog-posts-by-members/sap-datasphere-q-a-and-partnerships/ba-p/13570461)

![pbaumann](https://avatars.profile.sap.com/c/8/idc8c457b999d268dfbaa0942f2ccff2e490f3114f22b089b9bc62ff13945b5830_small.jpeg "pbaumann")

[pbaumann](https://community.sap.com/t5/user/viewprofilepage/user-id/942)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163552)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163552)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570461)

‎2023 Mar 12
2:43 PM

[22
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163552/tab/all-users "Click here to see who gave kudos to this post.")

12,218

* SAP Managed Tags
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)
* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (3)

On 8th of March 2023, SAP launched SAP Datasphere and on the same day already renamed the SAP Data Warehouse Cloud tenants to the new name.

SAP Datasphere shall deliver a Business [Data Fabric](https://blogs.sap.com/2022/08/19/data-architecture-with-sap-data-fabric/) to offer a seamless access to your data, independently where it is stored.

In the session a lot of questions where asked and answered by different SAP employees (thank you for this dialog!) about what this means and what is the impact to other SAP solutions. I compiled the most important questions I have seen from the session in the following part 1. After that I want to write down my first thoughts and considerations about the new strategic partnership.

### Part 1 - Q&A:

Here, just updated is the external [SAP Datasphere FAQ](https://community.sap.com/topics/data-warehouse-cloud/datasphere-faq).

**----- General Questions -----**

Q: Will the Datasphere eventually replace DWC?

A: SAP Datasphere is the evolution of SAP Data Warehouse Cloud.

---

Q: What does evolution mean when talking about SAP Datasphere is the evolution of SAP DWC? Will DWC be renamed/rebranded or will they co-exist?

A: It is a rebranding. SAP DWC will become SAP Datasphere.

---

Q: What is the difference/advantage of SAP Datasphere over SAP Data Warehouse Cloud?

A: SAP Datasphere is the evolution of SAP Data Warehouse Cloud. It includes many new features include a global data catalog, deep partnerships, and an advanced analytic model.

**----- SAP Data Intelligence -----**

Q: Will you provide a clear roadmap for SAP Data Intelligence today?

A:  SAP Data Intelligence Cloud will continue as a supported product with ongoing innovation and investment.

---

Q: Is SAP Data Intelligence embedded within Datasphere ?

A: SAP Data Intelligence Cloud will continue as its own product but many of the capabilities will be included in SAP Datasphere as well. The underlying engines are the same (that handle data movement) and in that sense yes it is embedded. However there are still differences in the two solutions: SAP Data Intelligence Cloud is fully dedicated infrastructure per customer whereas SAP Datasphere is a true multi-tenant shared infrastructure solution (for example).

---

Q: Will all features of SAP Data Intelligence be included in SAP Dataspehere? Or what would be a reason to have both products?

A: SAP Data Intelligence Cloud continues as its own solution. We intend to have SAP Datasphere and SAP Data Intelligence Cloud co-exist until SAP Datasphere supports all SAP Data Intelligence Cloud customer use cases. The plan is that SAP Datasphere will eventually be able to cover all the major capabilities, target systems, and use cases that SAP Data Intelligence Cloud provides. We plan to also provide tools to facilitate the technical transition.

**----- Integration Aspects -----**

Q: SAP Datasphere is purely federated or still requires persistent data in the cloud data model when combining different data sources for Analytics?

A: SAP Datasphere follows a federation first approach - meaning you leave data where it resides, build your models and later on decide whether you want to replicate full tables, create view persistencies to cater for source system workload, data egress, and performance towards the end user.

---

Q: What mechanism type that DataSphere is using for realtime replication?

A: SAP Datasphere will support a cloud native real time replication mechanism (trigger based) which allows to efficiently replicate large data sets. You will find this functionality as "Replication Flow" as part of SAP Datasphere.

---

Q: How are you planning to enable seamless integration with on-premise solutions? DP Agent will be there for the long run?

A: For SAP S/4 and ERP systems we will make use of DMIS (part of SAP Landscape Transformation) and CDS views as a way to integrate data in near real time with initial and delta replication. For other on premise solutions we will initially use DP Agent but over time our intent is to enable seamless integration without an on premise agent being required.

---

Q: Is Datasphere replication able to move on prem data to on prem targets without a roundtrip to the cloud?

A: Our main focus of SAP Datasphere is to replicate data into cloud and distribute it further. We are planning for hybrid scenarios where workload could be executed e.g. on premise while orchestrated in the cloud to avoid the roundtrip.

**----- BW/4HANA & SAC -----**

Q: Where does SAP BW/4HANA fit into the SAP Datashpere?

A: SAP BW/4HANA objects and other objects can be imported via SAP Datasphere, BW bridge that lets users access their data and models via a workspace within SAP Datashphere.

---

Q: How will these products interact with SAP Analytics Cloud?

A: SAP Datasphere is tightly integrated with SAP Analytics Cloud to support analytics and planning use cases. We intend to further strengthen the integration with the release of the Analytic Model in SAP Datasphere. The Analytic Model offers a multi-dimensional modeling experience and comes with powerful new features, such as calculated and restricted measures, exception aggregations and the pruning of attributes and measures.

### Part 2 - Strategic Partnerships:

SAP announced four strategic new partnerships to support the idea of a Business Data Fabric...
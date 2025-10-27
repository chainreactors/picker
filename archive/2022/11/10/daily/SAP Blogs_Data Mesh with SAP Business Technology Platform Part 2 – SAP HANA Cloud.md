---
title: Data Mesh with SAP Business Technology Platform Part 2 – SAP HANA Cloud
url: https://blogs.sap.com/2022/11/09/data-mesh-with-sap-business-technology-platform-part-2-sap-hana-cloud/
source: SAP Blogs
date: 2022-11-10
fetch_date: 2025-10-03T22:15:00.945456
---

# Data Mesh with SAP Business Technology Platform Part 2 – SAP HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Data Mesh with SAP Business Technology Platform Pa...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/155988&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data Mesh with SAP Business Technology Platform Part 2 – SAP HANA Cloud](/t5/technology-blog-posts-by-sap/data-mesh-with-sap-business-technology-platform-part-2-sap-hana-cloud/ba-p/13544966)

![Wolfgang_Epting](https://avatars.profile.sap.com/6/a/id6a53647710761a1c0cff3bdd76390b90599e560c101a3ae803506233f0e61c55_small.jpeg "Wolfgang_Epting")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Wolfgang\_Epting](https://community.sap.com/t5/user/viewprofilepage/user-id/6372)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=155988)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/155988)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13544966)

‎2022 Nov 09
7:44 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/155988/tab/all-users "Click here to see who gave kudos to this post.")

2,941

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (5)

***Summary:** In my first blog with the title: [More than just a hype: Data Mesh as a new approach to increase agility in value creation from data](https://blogs.sap.com/2022/06/04/more-than-just-a-hype-data-mesh-as-a-new-approach-to-increase-agility-in-value-creation-from-data/) I explained the four principles of [Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html) at a high level and mapped some helpful capabilities of the SAP Unified Data & Analytics Portfolio. In the current and subsequent episodes, I will look at individual SAP products and explain in more detail which of their technical capabilities can support the introduction of a Data Mesh. Having started the series with [SAP Data Warehouse Cloud](https://www.sap.com/products/technology-platform/data-warehouse-cloud.html) in the previous [blog](https://blogs.sap.com/2022/09/27/data-mesh-with-sap-business-technology-platform-part-1-sap-data-warehouse-cloud/), this time I will talk about [SAP HANA Cloud](https://www.sap.com/products/technology-platform/hana.html) and later on continue with [SAP Analytics Cloud](https://www.sap.com/products/technology-platform/cloud-analytics.html), [SAP Data Intelligence Cloud](https://www.sap.com/products/technology-platform/data-intelligence.html) and [SAP Master Data Governance](https://www.sap.com/products/technology-platform/master-data-governance.html).*

To understand this blog, it is at least necessary to have read my first [blog](https://blogs.sap.com/2022/06/04/more-than-just-a-hype-data-mesh-as-a-new-approach-to-increase-agility-in-value-creation-from-data/) or another respective publication to be familiar with the [four principles of Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html) and to understand why centralized  monolithic data architectures suffer from some inherent problems.

![](/legacyfs/online/storage/blog_attachments/2022/10/HANA-Cloud-2.jpg)

SAP HANA Cloud - Build a trusted Data Foundation

[SAP HANA Cloud](https://blogs.sap.com/2022/01/13/all-you-want-to-know-on-sap-hana-cloud/) is a single database as a service (DBaaS) foundation for modern applications and analytics across all enterprise data and the cloud-based data foundation for SAP Business Technology Platform. Several of its functionalities predestine SAP HANA Cloud to be used in Data Mesh scenarios. In the following, I will explain the three, from my point of view, most relevant:

## **Applying Domain-Driven Design strategies to data:**

"Each domain can model its data according to its context, share this data and its models with others, and identify how one model can relate and map to others." This statement comes verbatim from the book "[Data Mesh - Delivering Data-Driven Value at Scale](https://www.amazon.de/-/en/Zhamak-Dehghani/dp/1492092398)" by [Zhamak Deghani](https://www.linkedin.com/in/zhamak-dehghani/) and expresses that the principles of [Domain-Driven Design](https://www.amazon.de/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)1) used in software development are now also pentrating the analytical data space. Going into more detail about this concept at this point would go beyond the scope of this article. If you want to know more about adapting it to the world of data and analytics I recommend to read this [article](https://martinfowler.com/bliki/DomainDrivenDesign.html) from [Martin Fowler](https://martinfowler.com/).

At this point it is of higher importance to derive the requirements towards technology to enable the domains to model its data as efficiently as possible? A data and technology platform must provide multi-models in order to cover the complexity of todays reality and enable smart processing on top. [Multi-model data platforms](https://www.sap.com/germany/products/technology-platform/hana/features/multi-model.html) represent the intersection of various data models such as JSON documents, graph networks, and relational tables in a single data platform. With a multi-model database, domains can unify various data types and models into a single solution, without having individual technologies for each specific purpose.

With SAP HANA and SAP HANA Cloud, we are a long-term player in this domain offering a comprehensive solution, infused with additional features like geospatial analysis, enterprise search, machine learning and predictive modelling. SAP HANA Cloud seamlessly blends smart multi-model data to power intelligent data products.

Forrester Research Inc., a leading global research and advisory firm, researched, analyzed and scored vendors and positioned SAP as a Leader in “[The Forrester Wave™: Multimodel Data Platforms](htt...
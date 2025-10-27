---
title: BI 4.3 – WebI Ad-hoc Query & Analysis
url: https://blogs.sap.com/2022/10/20/bi-4.3-webi-ad-hoc-query-analysis/
source: SAP Blogs
date: 2022-10-21
fetch_date: 2025-10-03T20:29:23.745051
---

# BI 4.3 – WebI Ad-hoc Query & Analysis

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* BI 4.3 – WebI Ad-hoc Query & Analysis

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157551&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BI 4.3 – WebI Ad-hoc Query & Analysis](/t5/technology-blog-posts-by-sap/bi-4-3-webi-ad-hoc-query-analysis/ba-p/13549716)

![former_member245744](https://avatars.profile.sap.com/former_member_small.jpeg "former_member245744")

[former\_member245744](https://community.sap.com/t5/user/viewprofilepage/user-id/245744)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157551)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157551)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549716)

‎2022 Oct 20
7:33 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157551/tab/all-users "Click here to see who gave kudos to this post.")

3,547

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP BusinessObjects Business Intelligence platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520Business%2520Intelligence%2520platform/pd-p/01200314690800000337)
* [SAP BusinessObjects - Semantic Layer](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520-%2520Semantic%2520Layer/pd-p/280909257853820289811451573728573)
* [SAP BusinessObjects - Web Intelligence (WebI)](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520-%2520Web%2520Intelligence%2520%28WebI%29/pd-p/907900296036854683333078008146613)

* [SAP BusinessObjects Business Intelligence platform

  SAP BusinessObjects Business Intelligence](/t5/c-khhcw49343/SAP%2BBusinessObjects%2BBusiness%2BIntelligence%2Bplatform/pd-p/01200314690800000337)
* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP BusinessObjects - Semantic Layer

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusinessObjects%2B-%2BSemantic%2BLayer/pd-p/280909257853820289811451573728573)
* [SAP BusinessObjects - Web Intelligence (WebI)

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusinessObjects%2B-%2BWeb%2BIntelligence%2B%252528WebI%252529/pd-p/907900296036854683333078008146613)

View products (4)

# Universes & WebI, the winning combination

# for Ad-hoc Query, Analysis & Reporting

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture3-31.png)

[SAP BusinessObjects Business Intelligence suite](https://www.sap.com/products/technology-platform/bi-platform.html) remains one of the best BI platforms thanks to the powerful combination of Semantic Layer (**Universes**) and Web Intelligence (**WebI**).

Dashboards and data warehouses are powerful to monitor defined KPIs and SAP is proposing amazing solutions. The most recent one is [SAP Data Warehouse Cloud](https://www.sap.com/products/technology-platform/data-warehouse-cloud.html) making data meaningful with a single business semantic service unifying all data.

But with the huge amount of data available today and the speed of decision making, the agile BI is a complementary Business Intelligence expectation. Exploring all data for deeper or new analysis must be easy, fast and available for all business users who are doing data driven decisions regularly.

The BI Semantic Layer {*Patent* [*US5555403A*](https://patents.google.com/patent/US5555403A/)} (**Universe**) has always been a foundation of the BI Suite value proposition. Invented and released for the first time in the 90’s, the BI Semantic Layer is very mature and has been used intensively by all our customers for decades.

Compared to ETL or Data warehouse, **Universe** is not storing data but is providing a business semantic on top of your existing data sources, without modifying them, allowing your users to manipulate classic notions of their business without any code writing requirement. **Associated with WebI** that is the only BI Tool that can leverage the Universe capabilities entirely, it’s providing a great example of **No-Code** technology enabling a **very simple, fast and efficient way to consume any kind of data** in a self-service mode (without any scripts or SQL required to be written).

All query results (fetched data) are stored in the WebIntelligence document and are moved into memory when the document is opened. The **Mature and** **powerful cubes & C++ in-memory engines** enable several very interesting use cases. This is one of the reasons why WebI is considered being the BI Swiss knife:

* Users can efficiently manipulate and consume the data in offline mode regardless of the data source access. Compared to a live data access, business users will refresh of their data explicitly and can do so at any time (Live vs. On Demand). At database level, the “**On Demand**” fetch approach can generate bigger queries than a live access one. However, we deal with a **one-shot loading** rather than query data that is regularly pushed to the database based on business user’s actions. Added to that, WebI documents can be purged so that the data is no longer stored, and we offer a data refreshing option taking effect when users open their documents. As a result, you can start your analysis with fresh data. Depending on your constraints and use cases, SAP is providing great experience for both approaches:

  + **Live data access experience** with [SAP Analytics Cloud](https://www.sap.com/products/technology-platform/cloud-analytics.html) mainly with SAP Sources.

  + **Ad-hoc and On Demand queries** with [SAP BusinessObjects](https://www.sap.com/products/technology-platform/bi-platform.html) Universes & WebI (data sources supported available in the [Product Availability Matrix](https://apps.support.sap.com/sap/support/pam?hash=s%3DSBOP%2520BI%2520PLATFORM%25204.3%26o%3Dmost_viewed%257Cdesc%26st%3Dl%26rpp%3D20%26page%3D1%26pvnr%3D73555000100900001819%26pt%3Dg%257Cd))

* Data cubes can also provide other advantages. E.g users can create very **complex variables** (Formula Editor with functions, conditions and operators but also with contextual aggregation capabilities) mixing data from different sources to create **enriched data** **and analytics**.

* This calculation engine also enables **advanced reporting capabilities** (sections, breaks, cross-tables, measure aggregations, etc.).

* The “in-memory cubes and engines” provide also a **high-performance experience**. It’s less roundtrip with the databases, the cubes are optimized for fast analytic calculations, while also supporting and leveraging OLAP data, etc.

* In the coming **BI 4.3 SP03**, the WebI data mode will be back. It offers a lot of great enhancements compared to the 4.2 release. E.g **Joins & transformations** (a.k.a Lumira capabilities). The WebI cubes will again be leveraged to enable simpler data preparation use cases.

* And finally, it also offers a **lightweight ETL experience**, i.e data prepared in a WebI Document can now be reused easily thanks to “WebI as a Source” or OData ...
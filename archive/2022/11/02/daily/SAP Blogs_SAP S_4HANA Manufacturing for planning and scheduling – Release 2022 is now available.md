---
title: SAP S/4HANA Manufacturing for planning and scheduling – Release 2022 is now available
url: https://blogs.sap.com/2022/11/01/sap-s-4hana-manufacturing-for-planning-and-scheduling-release-2022-is-now-available/
source: SAP Blogs
date: 2022-11-02
fetch_date: 2025-10-03T21:31:43.981408
---

# SAP S/4HANA Manufacturing for planning and scheduling – Release 2022 is now available

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Manufacturing for planning and schedul...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51713&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Manufacturing for planning and scheduling - Release 2022 is now available](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-manufacturing-for-planning-and-scheduling-release-2022-is-now/ba-p/13559203)

![ulrich_mast](https://avatars.profile.sap.com/3/4/id34e3d39fcc270c41665c3276157d52610089491b1437937406c6445997f8c6f4_small.jpeg "ulrich_mast")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ulrich\_mast](https://community.sap.com/t5/user/viewprofilepage/user-id/138788)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51713)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51713)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559203)

‎2022 Nov 01
7:23 PM

[21
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51713/tab/all-users "Click here to see who gave kudos to this post.")

14,083

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Manufacturing/pd-p/2b555401-a867-4c2d-9d12-e709d78d635f)
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)
* [SAP S/4HANA Manufacturing for planning and scheduling](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Manufacturing%2520for%2520planning%2520and%2520scheduling/pd-p/0b12b27e-805d-43cb-bb87-975360c1f671)

* [SAP S/4HANA Cloud Public Edition Manufacturing

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BManufacturing/pd-p/2b555401-a867-4c2d-9d12-e709d78d635f)
* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP S/4HANA Manufacturing for planning and scheduling

  Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BManufacturing%2Bfor%2Bplanning%2Band%2Bscheduling/pd-p/0b12b27e-805d-43cb-bb87-975360c1f671)

View products (3)

As the release of the SAP S/4HANA 2022 version of **SAP S/4HANA Manufacturing for planning** **and scheduling (aka embedded / ePPDS)** is available (since 12th of October) this blog summarizes major innovations in this area and how customers can benefit from it now and moving forward with planned innovations in the future.

**SAP S/4HANA Manufacturing for planning and scheduling** allows the creation of feasible production plans and schedules that optimize your scarce resources to stabilize production and help you make reliable commitments to your internal and external customers. This S/4HANA Enterprise Management core extension, available both on premise and as private cloud edition, in stack and extra stack (side by side), ensures that planning and execution are synchronized in real time.

To recap what has happened in the past – a Customer Engagement Initiative was launched two years ago (2020) where customers’ direct feedback for key improvement areas was collected. This input has helped shape and influence the roadmap for ePPDS in SAP S/4HANA.

Major innovations in business process coverage especially for process industries, more flexible integration and UI-modernization have been shipped in 2021 already and are now extended by key innovations with the S/4HANA 2022 release (overview see below).

![](/legacyfs/online/storage/blog_attachments/2022/10/Figure-1-MPS-Strategy.png)

Figure 1: Overview Manufacturing Planning and Scheduling Strategy

**Advanced Scheduling Board – FIORI-Gantt 2.0**After the introduction of a new FIORI-based Gantt chart for production scheduling with S/4HANA 1610 with limited functionality we are now replacing it with the Advanced Scheduling Board on based on FIORI-Gantt 2.0 technology. It provides scheduling capabilities in a resource chart for interactive planning (drag and drop) and allows scheduling automation with standard and customized heuristics. The integrated alert framework helps the planner to efficiently work on exceptions which the algorithms couldn´t resolve automatically. Multiple charts e.g. for stock, resource utilization and operation and order views can be selected in addition. We continue to develop this new app and plan to incorporate more configuration concepts e.g. for coloring of shapes and table entries and allow the detailed-scheduling optimizer to be launched directly from the app. For complete overview of capabilities see the following blog ([Advanced Scheduling Board – F5460 | SAP Blogs](https://blogs.sap.com/2022/09/14/advanced-scheduling-board-f5460/)).

![](/legacyfs/online/storage/blog_attachments/2022/10/ASB-2022.png)

Figure 2: Advanced Scheduling Board

**Multi-Level Time Buffers**There is an increased demand for better decision support when doing simulations and this also applies for production planning and scheduling when displaying the consequences of schedule changes in an easy to consume fashion e.g. directly on the resource Gantt-chart. With the introduction of the multi-level Time-Buffer feature, the planner can easily compare currently planned end dates and times with latest possible end dates and times and recognize buffers / delays on the fly – not only to directly connected up- and downstream operations and orders, but also to the top-level demand. This is managed by a new infinite scheduling algorithm which allows the computation of these new key figures in real-time.

![](/legacyfs/online/storage/blog_attachments/2022/10/Figure-3-MLTB.png)

Figure 3: Multilevel Time Buffers

**Tank Planning**With the release of S/4HANA 2021 we started the innovation roadmap for tank planning with an initial focus to provide better visualization of tank fill levels in the Gantt-Chart and a new periodic fill level view in the product planning table. With the 2022 release we provide additional tank planning scope to manage also raw material tanks and silos for integrated planning of external and stock transfer purchasing requisitions / orders which consume storage capacity during and after the goods receive process.

Additional innovations delivered include a simplified modelling of groups of (dedicated) tanks, improved handling of residual quantities, simplified way of switching between tanks, the consideration of cleaning activities via set-up matrices and the improved maintenance of Product Storage Definitions (see [help portal](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f899ce30af9044299d573ea30b533f1c/5a2198b6d77f45dea5ba0cdf432e75a7.html?locale=en-US)).

**Improved Setup Matrix Generation**The efficient management of a setup matrix is the basis for successful setup optimization in planning. Generating matrices b...
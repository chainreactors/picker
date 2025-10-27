---
title: Introducing the Analytic Model in SAP Datasphere
url: https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/
source: SAP Blogs
date: 2023-03-14
fetch_date: 2025-10-04T09:30:11.652561
---

# Introducing the Analytic Model in SAP Datasphere

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Introducing the Analytic Model in SAP Datasphere

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163971&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Introducing the Analytic Model in SAP Datasphere](/t5/technology-blog-posts-by-sap/introducing-the-analytic-model-in-sap-datasphere/ba-p/13568591)

![jan_fetzer](https://avatars.profile.sap.com/5/3/id53744f70240ab1a7280ccb7f9604a8f0cd1b4abdf89348c421206795d13d5c70_small.jpeg "jan_fetzer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jan\_fetzer](https://community.sap.com/t5/user/viewprofilepage/user-id/199387)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163971)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163971)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568591)

‎2023 Mar 13
7:21 PM

[56
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163971/tab/all-users "Click here to see who gave kudos to this post.")

45,106

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (2)

Last week we [launched SAP Datasphere](https://news.sap.com/2023/03/sap-datasphere-business-data-fabric/) as the next generation of SAP Data Warehouse Cloud, but with new capabilities for enhanced data discovery, modeling & distribution.

The new Analytic Model is one of the cornerstones of SAP Datasphere in that it allows multi-dimensional and semantically rich analytical modelling to answer business questions easier, faster and more efficiently.

![](/legacyfs/online/storage/blog_attachments/2023/03/AM-Launch-Blog-white-Analytic-Model-Gif.gif)

Developing an Analytic Model in SAP Datasphere

Today, we are starting an own blog series to bring you all the details about the rich feature set of the Analytic Model. Guided by concrete examples, we’ll be looking in detail on features like measure modelling, variable modelling, data preview, exception aggregation and time-dependency. We will also focus on the benefits over the Analytical Dataset, touch on the positioning with regards to Business Layer, inspect the usage in SAP Analytics Cloud and much more.

We plan to release a new blog every Monday for the coming weeks. These blogs have been released so far:

1. Introducing the Analytic Model (this blog)

2. [Example Data Model used along the entire blog series](https://blogs.sap.com/2023/03/20/sap-datasphere-analytic-model-series-data-model-introduction/)

3. [Motivation & Comparison with the Analytical Dataset](https://blogs.sap.com/2023/03/28/sap-datasphere-analytic-model-series-motivation-comparison-with-the-analytical-dataset/)

4. [Calculated & Restricted Measures](https://blogs.sap.com/2023/04/03/sap-datasphere-analytic-model-series-calculated-and-restricted-measures/)

5. [Exception Aggregation](https://blogs.sap.com/2023/04/06/exception-aggregation-in-sap-datasphere/)

6. [Variables](https://blogs.sap.com/2023/04/17/sap-datasphere-analytic-model-series-using-variables-in-analytic-model/)

7. [Time-Dependency](https://blogs.sap.com/2023/04/21/time-dependency-for-dimensions-and-texts-in-analytic-model/)

8. [Data Preview](https://blogs.sap.com/2023/05/02/sap-datasphere-analytic-model-series-data-preview/)

9. [User Experience & Navigation Paradigm](https://blogs.sap.com/2023/05/09/sap-datasphere-analytic-model-series-user-experience-and-navigation-paradigm/)

10. [Multi-Fact Support in Analytic Models](https://blogs.sap.com/2023/05/24/sap-datasphere-analytic-model-series-blog-post-10-design-multi-fact-in-analytic-model/)

Stay tuned for more blogs around the Analytic Model in the coming weeks

# Introducing the Analytic Model & its benefits

The Analytic Model elevates the rich data & semantics of SAP Datasphere for immediate consumption in SAP Analytics Cloud and other channels. It provides

* **Rich measure modelling:** With calculation after aggregation, restricted measures & exception aggregation as well as the possibility to stack all of these, users can build very complex calculation models and even refine them in SAC stories

* **Careful design how analytics users see the data**: modelers can curate which measures, attributes and associated dimensions to expose to users. This helps analytics users to see exactly the data that is relevant to them, reduces likelihood for errors & boosts performance

* **Collection of user input via prompts in SAP Analytics Cloud:** these can be used for subsequent calculations, filters & time-dependency. Value helps are provided too, of course.

* **Rich previewing possibility:** modelers can inspect the result of their modelling efforts in-place because the Data Analyzer of SAP Analytics Cloud is tightly embedded into the Analytic Model editor. So slice & dice, pivoting, filtering, hierarchy usage and many more features are available to help users understand the data how it’ll be presented for consumption

* **Time-dependency support:** Analytic Models support this critical feature to let users travel back & forth in time while Lines of Business, structures & organizations are constantly evolving.

* **Dependency Management & Transport:** Complex analytic projects require careful planning and a sophisticated toolset for managing the dependency and lifecycle of all modelling artefacts. The Analytic Model is fully integrated into the SAP Datasphere repository and thus benefits from impact & lineage analysis, change management & transport management

The Analytic Model will ultimately be THE go-to analytical consumption artefact of SAP Datasphere for all channels. While Analytical Datasets in the Data Layer and Business Layer Perspectives will not go away any time soon, the Analytic Model already today offers a superior feature set for almost all modelling situations.

As a quick overview, let’s see the Analytic Model in action:

# I’m in – how do I start?

The Analytic Model is automatically available the the Data Builder of your SAP Datasphere tenant.

Let's use this 8-step process to get you started:

1. To start, just launch the Data Builder and **hit *New Analytic Model***. You can add any Analytical Dataset as fact source and the wizard will prompt you on which attributes, measures & associated dimensions to include.

2. From here, just **add additional reachable dimensions and their attributes**. The system will automatically create the necessary database joins to let users drill-down by even the farthest of dimensions. This way, modelers can very carefully design what parts of the data model to expose for a given analytics use case.

...
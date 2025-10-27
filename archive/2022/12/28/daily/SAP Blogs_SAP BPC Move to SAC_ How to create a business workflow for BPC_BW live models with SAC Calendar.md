---
title: SAP BPC Move to SAC: How to create a business workflow for BPC/BW live models with SAC Calendar
url: https://blogs.sap.com/2022/12/27/sap-bpc-move-to-sac-how-to-create-a-business-workflow-for-bpc-bw-live-models-with-sac-calendar/
source: SAP Blogs
date: 2022-12-28
fetch_date: 2025-10-04T02:36:06.349787
---

# SAP BPC Move to SAC: How to create a business workflow for BPC/BW live models with SAC Calendar

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP BPC Move to SAC: How to create a business work...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160593&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BPC Move to SAC: How to create a business workflow for BPC/BW live models with SAC Calendar](/t5/technology-blog-posts-by-sap/sap-bpc-move-to-sac-how-to-create-a-business-workflow-for-bpc-bw-live/ba-p/13557986)

![Nektarios_Vasileiou33](https://avatars.profile.sap.com/b/6/idb61029aa183460136e925bbfe70f1f4cba48259d725e078f5ac3ede4881ca2e0_small.jpeg "Nektarios_Vasileiou33")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Nektarios\_Vasileiou33](https://community.sap.com/t5/user/viewprofilepage/user-id/7476)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160593)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160593)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557986)

‎2022 Dec 27
10:27 AM

[17
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160593/tab/all-users "Click here to see who gave kudos to this post.")

5,691

**Introduction**

The aim of this blog series is to explain the status of SAP Business Planning & Consolidation (SAP BPC) integration with SAP Analytics Cloud (SAC) and our strategic direction. Furthermore, we want to show you how SAP Analytics Cloud can extend and provide a positive ROI for your current planning, forecasting and analysis scenarios and help you run an Intelligent Enterprise. This is going to create new opportunities for planning, forecasting and analysis and thus it will help you steer your organisation even more effectively.

We also want to provide some guidance about the supported scenarios and high-level architectures and what can be done when it comes to modernising the existing planning & analysis solution of SAP BPC by adding SAC as:

+ a unified user experience for:

  * a planning (data entry) user interface,

  * a data analysis interface,

+ a planning extension,

+ a pure SAC scenario (complete move from SAP BPC).

There will be several blog posts in the series that will cover relevant topics about integration and supported workflows, so please stay tuned for the updates of this blog post with all relevant links to additional blogs of the series:

+ [SAP BPC Move to SAC: Benefits & scenarios of moving SAP BPC planning scenarios to SAP Analytics Clou...](https://blogs.sap.com/2023/02/17/sap-bpc-move-to-sac-benefits-scenarios-of-moving-sap-bpc-planning-scenarios-to-sap-analytics-cloud/)

+ [SAP BPC Move to SAC: Use SAP Analytics Cloud as data entry UI for SAP BPC](https://blogs.sap.com/2023/02/23/sap-bpc-move-to-sac-use-sap-analytics-cloud-as-data-entry-ui-for-sap-bpc/)

+ [SAP BPC Move to SAC: Work with BPC planning sequences in SAP Analytics Cloud](https://blogs.sap.com/2023/03/01/sap-bpc-move-to-sac-work-with-bpc-planning-sequences-in-sap-analytics-cloud/)

+ SAP BPC Move to SAC: How to create a business workflow for BPC/BW live models with SAC Calendar (THIS BLOG POST)

+ [SAP BPC Move to SAC: How to analyse data](https://blogs.sap.com/2023/03/30/sap-bpc-move-to-sac-how-to-analyse-data/)

+ [SAP BPC Move to SAC: MS Office/Excel add-in](https://blogs.sap.com/2023/04/06/sap-bpc-move-to-sac-ms-office-excel-add-in/)

+ [SAP BPC Move to SAC: Collaboration](https://blogs.sap.com/2023/05/02/sap-bpc-move-to-sac-collaboration/)

We want to simplify our SAP Business Planning and Consolidation (BPC) customers’ transition journey to xP&A and to SAP Analytics Cloud (SAC) by allowing them to move at their own pace progressively, without disruption of their planning processes. To facilitate the MOVE of SAP BPC customers to SAP Analytics Cloud, we changed our commercial policy by introducing the [BPC Embedded Access Rights](https://blogs.sap.com/2022/08/23/introducing-bpc-runtime-license/) and we provide technical solutions for tight integration and live connectivity options with on-premise BPC applications. With this approach you can avoid double licensing, safeguard your BPC on-premise investments, even extend and combine them with other use cases in the cloud.

In SAP Analytics Cloud you can integrate your BPC embedded planning models via the [BPC live-connection](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/3c284ec47d8542b79f5ed82662574f32.html?locale=en-US). This enables live planning with your existing BPC models by using SAC as a frontend user interface, leveraging the existing BPC objects. You can consume BPC input queries and BPC planning sequences into SAC stories and do a writeback from the SAC front end into your BPC planning providers, so data modelling and data persistency resides in your on-premise BPC system.

So far, so good…but how about the business workflows? How can I organize the planning process and monitor activities with BPC live planning in SAC?

Business Process Flows (BPF), the functionality to guide the business users through pre-defined steps in BPC Embedded, is currently not covered by the BPC Embedded Access Rights. You also cannot seamlessly integrate the SAC story hyperlink into your BPF steps since the context/parameter cannot be passed from BPF to the SAC hyperlink. On the other hand, the Calendar functionality in SAC provides many capabilities to manage processes and orchestrate workflows but does not currently support live BW/BPC models.

In this blog I am going to describe how you can use the SAC calendar with BPC live planning in SAC.

**How to**

To start, I already have in place a simple BPC live planning example, which follows a quantity times price approach for planning sales and contribution margin of vehicles across Europe per Region and Product Category. See below the overall architecture, where SAC is used as the frontend user interface:

![](/legacyfs/online/storage/blog_attachments/2022/12/2022-12-22_16-37-06-1.png)

Now I want to create a simple workflow for data collection from all regions. Leveraging the wizard in the SAC calendar I want to generate tasks and processes from a driving dimension, which will be the Region dimension in this example. But how can this be done given that the BPC live models are not supported in the SAC calendar?

+ Build an empty Dummy Model in SAC and include only the driving dimension for the SAC calendar wizard (g. Region). In this dimension, maintain the responsible users of each regional level. There are different options to maintain the user assignments: 1) manually in dimension, 2) use an Analytic Application to maintain the dimension properties, 3) if a public dimension is used, you can import the user assignments through a BW query from a mapping table in BW/BPC. This is a more robust approach since it could be synchronized with the analysis authorizations in BW.

![](/legacyfs/online/storage/blog_attachments/2022/12/picturelast11-1.png)

+ In the SAC story used for data collection, where the BPC input query and plann...
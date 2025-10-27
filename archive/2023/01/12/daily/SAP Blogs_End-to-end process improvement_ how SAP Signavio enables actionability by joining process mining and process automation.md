---
title: End-to-end process improvement: how SAP Signavio enables actionability by joining process mining and process automation
url: https://blogs.sap.com/2023/01/11/end-to-end-process-improvement-how-sap-signavio-enables-actionability-by-joining-process-mining-and-process-automation/
source: SAP Blogs
date: 2023-01-12
fetch_date: 2025-10-04T03:39:30.771368
---

# End-to-end process improvement: how SAP Signavio enables actionability by joining process mining and process automation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* End-to-end process improvement: how SAP Signavio e...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163607&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [End-to-end process improvement: how SAP Signavio enables actionability by joining process mining and process automation](/t5/technology-blog-posts-by-sap/end-to-end-process-improvement-how-sap-signavio-enables-actionability-by/ba-p/13567434)

![sarcangeli](https://avatars.profile.sap.com/6/f/id6fb212efe1edb2674f023f6027ea6a89631f348a1351b5d7ccd4ca0b7dbc6c49_small.jpeg "sarcangeli")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[sarcangeli](https://community.sap.com/t5/user/viewprofilepage/user-id/5465)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163607)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163607)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567434)

‎2023 Jan 11
6:09 PM

[33
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163607/tab/all-users "Click here to see who gave kudos to this post.")

6,195

* SAP Managed Tags
* [SAP Signavio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Signavio/pd-p/088166be-6441-4660-9e5b-1a046de322bf)
* [SAP Signavio Process Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Signavio%2520Process%2520Intelligence/pd-p/73554900100800003814)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Signavio

  Additional Software Product](/t5/c-khhcw49343/SAP%2BSignavio/pd-p/088166be-6441-4660-9e5b-1a046de322bf)
* [SAP Signavio Process Intelligence

  business process transformation](/t5/c-khhcw49343/SAP%2BSignavio%2BProcess%2BIntelligence/pd-p/73554900100800003814)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (4)

In our recent [SAP Signavio Business Transformation Forum](https://www.signavio.com/events/business-process-transformation-forum-berlin/#agenda), in Berlin, we unveiled and discussed our vision around enabling enterprises to achieve [Process Observability](https://dam.sap.com/mac/app/p/video/asset/preview/xjj6HNP?ltr=a&rc=10&includeRelatedAssets=true). When approaching the process observability topic, the first major focus is on how one can tackle all the organizational unknowns, technically and methodologically, as my colleague Timotheus Kampik analyzed in detail [in this blog post](https://blogs.sap.com/2022/09/16/what-is-business-process-observability-and-why-does-it-matter/).

But that is only one side of the coin: “a process is observable if stakeholders and systems understand how it operates, where the process outcomes are **known**, and **actions** can be derived to **improve** or change these outcomes.” On one side, organizations must know how they’re currently operating. On the other side, such knowledge must be turned into actions that can drive improvement. And it’s only the completion of this full flow allows the organization to gain business value and competitive advantage.

In a [recent blog post](https://blogs.sap.com/2022/12/07/get-actionable-insights-on-your-processes-from-sap-signavio-and-rapidly-improve-with-sap-build-process-automation/), Sebastian Schroetel explained how we aim to streamline insight-to-action flows in SAP Signavio, leveraging SAP Build Process Automation as an integral part of the SAP Signavio Process Transformation Suite. In this post, I will dig deeper into that, analyzing how we aim to foster **actionability** from our **process mining** solution, SAP Signavio Process Intelligence.

## Driving improvements from process mining: a dual-speed approach

Our vision at SAP Signavio, is to leverage process mining to enable enterprises to drive holistic process improvement initiatives out of their data and knowledge. Insights gathered from process mining analysis can drive process change across two different and complementary routes, as depicted in the following diagram:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture1-20.png)

Dual speed process improvement

* **The deep cycle – Process transformation initiatives**: in SAP Signavio Process Transformation Suite, process mining insights can guide changes to business process models (mining-to-modeling), which can then drive redeployment of the process in the core systems themselves (model-to-deploy) for deep and permanent process improvements.

* **The fast cycle – Process operations improvement initiatives**: in SAP Signavio Process Transformation Suite, process mining insights can now trigger the execution of actions that involve workflows or RPA bots in SAP Build Process Automation, to quickly deliver continuous improvements on the process on top of its core implementation and core model, which do not change.

While the “deep cycle” has been part of Signavio’s DNA for quite a while now (and will remain so and get further strengthened in the future), the “fast cycle” is instead an area of great innovations and growth, thanks to the powerful synergies enabled by SAP Build Process Automation.

## Process Mining + Process Automation: improving process operations at scale

Let’s have a closer look at the “fast cycle” and how the process mining capabilities of SAP Signavio Process Intelligence and the automation capabilities of SAP Build Process Automation can work in synergy. For that, I would outline three main categories of use cases, as depicted in the following diagram:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture2-10.png)

SAP Signavio Process Intelligence + SAP Build Process Automation

1. **Process quick fixes**: the “actions” that SAP Signavio Process Intelligence can generate out of process mining metrics can trigger the execution of workflows or RPA bots in SAP Build Process Automation, in an event-driven (asynchronous) fashion. Besides this, process mining metrics can also be synchronously queried from SAP Build Process Automation to influence the behavior of business rules that control workflow execution. These touch points open up several possibilities for implementing “quick fixes” to existing processes. For example, suppose the percentage of order reworks for a given supplier goes above a safety threshold in a Procure-to-Pay process. In that case, we could execute a workflow that activates an additional approval on the currently ongoing purchase requests for that supplier, because we know they are likely to incur operational issues. Or, to quote a different example that Sebastian shared in his previous blog...
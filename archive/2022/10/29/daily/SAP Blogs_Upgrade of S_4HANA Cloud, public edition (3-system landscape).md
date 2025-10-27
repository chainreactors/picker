---
title: Upgrade of S/4HANA Cloud, public edition (3-system landscape)
url: https://blogs.sap.com/2022/10/28/upgrade-of-s-4hana-cloud-public-edition-3-system-landscape/
source: SAP Blogs
date: 2022-10-29
fetch_date: 2025-10-03T21:13:28.364295
---

# Upgrade of S/4HANA Cloud, public edition (3-system landscape)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Upgrade of S/4HANA Cloud Public Edition (3-system ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51125&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Upgrade of S/4HANA Cloud Public Edition (3-system landscape)](/t5/enterprise-resource-planning-blog-posts-by-sap/upgrade-of-s-4hana-cloud-public-edition-3-system-landscape/ba-p/13555548)

![Ying](https://avatars.profile.sap.com/5/e/id5ebdfc9e14ee56abf1a20b7a663064899f138a34605c98ded622ef10f68feff3_small.jpeg "Ying")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Ying](https://community.sap.com/t5/user/viewprofilepage/user-id/78188)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51125)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51125)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555548)

‎2022 Oct 28
4:56 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51125/tab/all-users "Click here to see who gave kudos to this post.")

5,705

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)

View products (2)

In my previous blog [Release and Update Cycle of S/4HANA Cloud](https://blogs.sap.com/2022/03/25/release-and-update-cycle-of-s-4hana-cloud/), I talked about the three different types of life cycle events for S/4HANA Cloud. Having a 3-system landscape (Dev, Test and Production) is the new default for S/4HANA Cloud Public Edition. In the Activate [roadmap](https://go.support.sap.com/roadmapviewer/#/group/658F507A-D6F5-4B78-9EE1-0300C5F1E40F/roadmapOverviewPage/82b2db84548d41209cda972f0fac428b) for 3-system landscape, there is an Update and Release Cycle deliverable, described all the three different types of life cycle events on public cloud, hotfix, continuous feature delivery and release upgrade.

For the release upgrade scenario in 3-system landscape, there is an [upgrade roadmap](https://go.support.sap.com/roadmapviewer/#/group/1B9D1B79-D03B-42F6-937C-08DE7C252BB6/roadmapOverviewPage/b6cc8dc5bbb749a59e1e21a4796c796f) that provides structure and details with regard to this process. It is a separate roadmap dedicated to S/4HANA Cloud, public edition (3-system landscape) upgrade, covering the 2 weeks preparation related steps before software upgrade starts with Test System, describe the regression test that customer needs to be focusing on during the 3 weeks of upgrade period in Test System, and highlights the tasks to be completed right after the software upgrade of Dev and Production system, including the deployment of upgraded business configuration content, which is ***new*** with the introduction of 3-system landscape.  ![](/legacyfs/online/storage/blog_attachments/2022/10/upgrade.jpg)

What is ***business configuration content***? For those of us have worked in the old R/3 ERP world, we all know that the flexibility with R/3 ERP is all about the configuration or customizing that is maintained in IMG. Without any code changes, setting in configuration tables can lead to different ways how customers want to use the same SAP product. The ***decoupling***of the business content managed via these configuration table vs. software or code updates are a natural progression with public cloud. This allows the software or code line continuously being updated in cloud without impacting how customer run their solution per current configuration setting for their business. Customers are given more time to make mandatory adoptions in their business process and implement new innovation per their own timeline.

In the [Initiate Upgrade Project](https://go.support.sap.com/roadmapviewer/#/group/1B9D1B79-D03B-42F6-937C-08DE7C252BB6/roadmap/b6cc8dc5bbb749a59e1e21a4796c796f:FA163ED752201EDBA8A6CE64CE06CF19/node/FA163EAF25B21EDBA8D4E2DD0B81D5F2) task of upgrade roadmap, the chapter in [SAP help portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/638379d9db2847989d56836d91b31906.html) is referenced as an accelerator, providing an overview of software delivery and the content delivery.

![](/legacyfs/online/storage/blog_attachments/2022/10/planning-in-upgrade-1.jpg)

From project planning point of view, as the green bar indicated here, there are quite a lot of design and configuration activities can be carried out throughout the 3 weeks software upgrade period. For example, customer can still scope and make organizational structure changes and access configuration activities via the SAP Central Business Configuration tool.

There are certainly some restrictions on S/4HANA side, as indicated with couple of short red bar, around the software upgrade weekends where transport related activities in the respective systems are impacted.

During the upgrade period, Test System should be used for Regression Testing to ensure functionality that worked before are not impacted by the upgrade. Although transports can still be moved across the landscape from Dev to Test to Production, it should be minimized in order to maintain a valid testing environment.

After the 1st week, if customer creates a new project in SAP Central Business Configuration, it will have the upgraded reference content, the new content version. Therefore, avoid deploying this new project to Dev system till after Dev system is software upgraded at a later point.

Here are the respective recommendations and limitations from the above diagram:

1. System getting prepared for Upgrade. No Import & Export of transports
2. Moving transport cross the landscape (D-T-P) is still possible. For urgent needs only to ensure valid regression testing environment for customer are live in P
3. Access Configuration Activity is possible until the respective S/4HANA Cloud systems (Development, Starter, Partner Demo) getting prepared for upgrade.
4. Organizational structure enhancements, adding new scope or country are possible until project in SAP Central Business Configuration is locked when upgraded business configuration content is uploaded. It is however, not recommended to activate new country during the 3 week period as it may delay the application of content upgrade in case of activation issues at the end of the 3-week period.
5. Avoid deploy a project created new after the 1st week in SAP Central Business Configuration. Applicable to both Evaluation and Implementation project

As a result of the previously mentioned ***decoupling***, one key difference ...
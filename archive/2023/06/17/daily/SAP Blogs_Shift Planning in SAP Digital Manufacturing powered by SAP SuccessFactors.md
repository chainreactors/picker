---
title: Shift Planning in SAP Digital Manufacturing powered by SAP SuccessFactors
url: https://blogs.sap.com/2023/06/16/shift-planning-in-digital-manufacturing-powered-by-sap-successfactors/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:47:08.293083
---

# Shift Planning in SAP Digital Manufacturing powered by SAP SuccessFactors

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Shift Planning in SAP Digital Manufacturing powere...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6117&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Shift Planning in SAP Digital Manufacturing powered by SAP SuccessFactors](/t5/human-capital-management-blog-posts-by-sap/shift-planning-in-sap-digital-manufacturing-powered-by-sap-successfactors/ba-p/13562406)

![Frans_Smolders](https://avatars.profile.sap.com/4/b/id4bc2a6d9a4339b96aa28fdd58ac11cf80cdd193720ac7b7f73c4a587f39ac512_small.jpeg "Frans_Smolders")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Frans\_Smolders](https://community.sap.com/t5/user/viewprofilepage/user-id/17823)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6117)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6117)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562406)

‎2023 Jun 16
2:11 PM

[14
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6117/tab/all-users "Click here to see who gave kudos to this post.")

7,879

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors Time Tracking](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Time%2520Tracking/pd-p/73555000100800002827)
* [SAP Digital Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Digital%2520Manufacturing/pd-p/73555000100800001492)

* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP Digital Manufacturing

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BDigital%2BManufacturing/pd-p/73555000100800001492)
* [SAP SuccessFactors Time Tracking

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BTime%2BTracking/pd-p/73555000100800002827)

View products (3)

Hi all,

We're often asked what our SAP SuccessFactors Time Management strategy is to cover shift planning. In this blog I would like to highlight our strategy and also the rationale behind it.

For customers who run SAP SuccessFactors Time Management our strategy for Shift Planning is in essence 2-fold:

1. The first option is for customers who want a standalone shift planning app. For these customers we offer a range of planning apps via our [SAP Store](https://store.sap.com/dcp/en/categories/try-and-buy-human-capital-management-apps-and-software).

2. The second option, for customers who favour SAP solutions we have targeted (often Industry specific) resource planning and deployment solutions. For example, we have SAP S/4HANA Resource Management for the scheduling of consultants and SAP Digital Manufacturing for complete manufacturing related planning processes which can include labor.

In scheduling, there is hardly a one-size fits all as every industry has own specific scheduling types and needs. In this blog I would like to show and explain our integration approach with SAP Digital Manufacturing.

# SAP Digital Manufacturing

First of all, let me start by explaining what SAP Digital Manufacturing is and offers:

In SAP Digital Manufacturing, demand-based shift planning can be achieved through various features and functionalities offered by the system. Here's an overview of the steps involved in implementing demand-based shift planning:

1. Demand Forecasting: Obtain accurate demand forecasts for your manufacturing operations. This can be achieved by leveraging SAP's Demand Planning module or integrating external forecasting tools with SAP Digital Manufacturing.

2. Production Planning: Utilise SAP's Production Planning module to create production plans based on the demand forecast. This module helps you determine the required production quantities, scheduling, and resource allocation.

3. Shift Planning: In SAP Digital Manufacturing, shift planning involves assigning resources, such as operators or machines, to specific shifts based on the production plan. You can create shift profiles that define shift durations, break times, and other shift-specific parameters.

4. Capacity Evaluation: Evaluate the capacity of your production resources against the planned shifts. SAP Digital Manufacturing provides capacity evaluation tools that allow you to analyse resource utilisation, identify bottlenecks, and optimise shift assignments.

5. Shift Optimisation: Once the initial shift plan is created, you can use SAP's optimisation algorithms to fine-tune the plan. The system considers factors such as resource availability, skill requirements, and production constraints to automatically optimise the shift assignments and minimise costs or maximise throughput.

6. Shift Scheduling: Generate shift schedules based on the optimised shift plan. The schedules can be communicated to operators through the SAP Digital Manufacturing platform or integrated with other scheduling tools.

7. Monitoring and Adjustments: Continuously monitor the execution of the shift plan and track key performance indicators (KPIs) to ensure the plan aligns with the demand. If necessary, make adjustments to the plan in real-time to accommodate changing demand or resource availability.

SAP Digital Manufacturing provides a comprehensive suite of tools to enable demand-based shift planning, integrating demand forecasting, production planning, and shift optimisation. By leveraging these capabilities, you can align your manufacturing operations with customer demand, optimise resource utilisation, and improve overall efficiency.

# How does Labor Planning work in SAP Digital Manufacturing?

Now, let me get to the SAP SuccessFactors related aspects which mainly focus on the exchange of labor related information to SAP Digital Manufacturing to e.g. facilitate labor related planning. This involves the process of effectively allocating and managing labor resources for manufacturing operations. Here's an overview of how labor related planning works in SAP Digital Manufacturing:

1. Resource Master Data: Start by defining and maintaining resource master data in the system. This includes information such as the skills and qualifications of labor resources, availability, work shifts, and any constraints or preferences. When SAP Digital Manufacturing is connected to SAP SuccessFactors the Resource Master Data is highly aligned.

2. Work Center Setup: Configure work centers within SAP Digital Manufacturing to represent the physical locations or areas where labor activities occur. Assign the appropriate labor resources to each work center based on their skills and qualifications.

3. Production Orders: Create production orders in SAP Digital Manufacturing to represent the planned manufacturing activities. These orders ...
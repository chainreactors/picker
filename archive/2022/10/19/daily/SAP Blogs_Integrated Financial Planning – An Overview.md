---
title: Integrated Financial Planning – An Overview
url: https://blogs.sap.com/2022/10/18/integrated-financial-planning-an-overview/
source: SAP Blogs
date: 2022-10-19
fetch_date: 2025-10-03T20:15:05.957177
---

# Integrated Financial Planning – An Overview

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Integrated Financial Planning - An Overview

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/155755&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrated Financial Planning - An Overview](/t5/technology-blog-posts-by-sap/integrated-financial-planning-an-overview/ba-p/13544197)

![hartmut_koerner](https://avatars.profile.sap.com/2/4/id247ae63c81cc991785f73e8b0e59a5aa51337013a2f92141970b0d7af18f32d5_small.jpeg "hartmut_koerner")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[hartmut\_koerner](https://community.sap.com/t5/user/viewprofilepage/user-id/250539)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=155755)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/155755)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13544197)

‎2022 Oct 18
4:58 PM

[37
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/155755/tab/all-users "Click here to see who gave kudos to this post.")

28,247

* SAP Managed Tags
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)
* [Extended Planning and Analysis](https://community.sap.com/t5/c-khhcw49343/Extended%2520Planning%2520and%2520Analysis/pd-p/bcbf0782-ce74-43b8-b695-dafd7c1ff1c1)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)
* [Extended Planning and Analysis

  Product Category](/t5/c-khhcw49343/Extended%2BPlanning%2Band%2BAnalysis/pd-p/bcbf0782-ce74-43b8-b695-dafd7c1ff1c1)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (4)

## Introduction

**Integrated Financial Planning for SAP S/4HANA and S/4HANA Cloud** is the content package for SAP Analytics Cloud that covers the complete area of financial planning. This package already exists several years now, it was enhanced step by step in the last years and with the 2022.Q2 release it was migrated to the **New Model** in SAC. With this blog post I want to create a single entry point for all important information around this topic.

![2024-08-23_08-52-55.png](/t5/image/serverpage/image-id/156368iC959CA581F252144/image-size/large?v=v2&px=999 "2024-08-23_08-52-55.png")

The content package consists of five integrated planning areas:

+ **Operating expense planning** manages the expenses for different areas of responsibility within the company, e.g. cost centers or projects. Expenses can be planned and allocated between the respective cost objects. In a quantity driven approach, expenses can be combined with activity quantity planning and an iterative activity price calculation

+ **Product cost planning** has the task to calculate the costs of a product. The two main ingredients of product costs are the raw material costs and the activity costs, for example machine costs. Cost center planning is one important input for product cost planning because it determines the activity prices (e.g. for a machine hour) to calculate the activity costs

+ **Sales and profitability planning** calculates the revenues, deductions and costs based on the planned sales quantities. Product related costs originate from product cost planning whereas product independent costs like administration costs originate from cost center planning directly

+ **Capital expense planning**allows to plan asset additions and depreciations. The depreciations are an important input for the cost center planning and the asset additions can be rolled up into the financial statement planning

+ **Financial statement planning** brings together all the detail plans and creates an equated balance sheet and cash flow statement

The five modules of integrated financial planning can be used altogether to cover the whole financial planning process from an operational to a strategic level. On the other hand they are loosely coupled and can be used easily standalone. E.g. in a non-manufacturing industry like professional services, one would leave out the product cost planning module. Concentrating on a high-level financial plan, one could use the financial statement planning even standalone.

Integrated Financial Planning covers all different business roles that are engaged with financial planning in a company: Corporate controlling or corporate FP&A that set up and manage the planning process in the company and set the targets, the single planners in financial accounting, regional controlling and even sales departments (cost center managers, production controller, sales planner) that manual enter their plan data and the planning administrators that run planning functions across the different modules.

Looking at the legacy planning solutions of SAP, Integrated Financial Planning covers both the "classical" planning in the FI/CO area of SAP ERP and S/4HANA as well as a model driven BW/BPC based planning solution be it BPC Optimized embedded in S/4HANA or a BPC planning solution in a standalone BW system.

Integrated Financial Planning can handle different currencies (global, local, transactional), different time granularity, fixed or rolling time horizons and it can be used tightly or loosely coupled to S/4HANA data and processes. It supports both a bottom-up and a top-down planning approach and a combination of both leveraging a powerful version management.

Integrated Financial Planning also is part of the [xP&A suite](https://community.sap.com/topics/cloud-analytics/planning/content) and very well integrates out-of-the-box both with other SAC based planning applications like HXM Workforce Planning and Consumer Products Sales Planning and non-SAC based planning applications like SAP Integrated Business Planning.

Steering business towards a decarbonize economy is a major goal today. Greenhouse gas (GHG) emission planning that is part of this content package extends integrated financial planning by the carbon dimension. It evaluates the financial plan with carbon emission factors and calculates the future carbon footprints of the organization. The financial plan data, including expenses, activities, and sales quantities, serves as the foundation for calculating carbon dioxide equivalents (CO2e). The same plan structures, such as the quantity structures and allocation rules used for cost allocation, can also be reused to allocate CO2e to respective cost obj...
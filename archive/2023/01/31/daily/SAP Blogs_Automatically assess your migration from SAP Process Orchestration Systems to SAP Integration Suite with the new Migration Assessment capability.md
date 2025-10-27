---
title: Automatically assess your migration from SAP Process Orchestration Systems to SAP Integration Suite with the new Migration Assessment capability
url: https://blogs.sap.com/2023/01/30/automatically-assess-your-migration-from-sap-process-orchestration-systems-to-sap-integration-suite-with-the-new-migration-assessment-capability/
source: SAP Blogs
date: 2023-01-31
fetch_date: 2025-10-04T05:13:58.694542
---

# Automatically assess your migration from SAP Process Orchestration Systems to SAP Integration Suite with the new Migration Assessment capability

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Automatically assess your migration from SAP Proce...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159674&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automatically assess your migration from SAP Process Orchestration Systems to SAP Integration Suite with the new Migration Assessment capability](/t5/technology-blog-posts-by-sap/automatically-assess-your-migration-from-sap-process-orchestration-systems/ba-p/13555563)

![RichK](https://avatars.profile.sap.com/c/a/idcadc77284521a56a80c1fedadec244145bdb5e261079296d5924cbfc214f7a31_small.jpeg "RichK")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[RichK](https://community.sap.com/t5/user/viewprofilepage/user-id/8607)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159674)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159674)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555563)

‎2023 Jan 30
8:17 PM

[16
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159674/tab/all-users "Click here to see who gave kudos to this post.")

10,247

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (4)

# Introduction

As organizations work on digital transformation initiatives, modernizing IT technology is imperative to take advantage of the latest innovations to drive new business value while reducing costs.  The adoption of new software applications and technology in the cloud has led to highly distributed system landscapes and new integration standards which require modern integration technology.  In order to provide seamless business processes an integration technology is needed which can support the latest API and event-driven architectures.  SAP Integration Suite is SAP’s cloud-native, fully managed integration platform as a service (iPaaS) offering.  It supports all forms of modern-day integration patterns, along with pre-built content and intelligent technology built-in to help accelerate the development of new integration scenarios both internally as well as externally providing many advantages over technology like SAP Process Integration or SAP Process Orchestration.

To make the transition from SAP Process Integration/Orchestration to SAP Integration Suite as efficient as possible, it’s important to have the necessary tools to help assess the ability to migrate your current landscape (including the interfaces, security aspects and connectivity aspects), and then plan your migration strategy. For that, we are pleased to announce the release of the **Migration Assessment** capability in the SAP Integration Suite.

This capability helps you to estimate the technical efforts involved in the migration process and evaluates how various integration scenarios can be migrated. Migration Assessment focuses on the extraction and assessment of your current landscape design time artefacts. This capability serves as the basis for your overall migration planning.

# **Key Steps to assess the artefacts for migration using the Migration Assessment Tool**

In summary, to assess your artefacts from an existing SAP Process Orchestration 7.5 system to SAP Integration Suite the following steps should be performed:

* Connect your SAP Process Orchestration system to SAP Integration Suite

* Extract data from your system

* Evaluate the extracted artefact metadata based on the flexible rule framework

* Estimate the potential effort of migrating integrated configuration objects from your SAP Process Orchestration 7.5 system to the SAP Integration Suite

# **Migration Assessment Tool Overview**

The Migration Assessment tool consists of two steps under the **Request** option:

* ****Data Extractions****

* **Scenario Evaluation**

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-2-2.png)

* **Data Extractions**: A process wherein the application gathers data, for example, integration scenarios, mapping objects, communication channels and other design time artefacts from a connected SAP Process Orchestration system and prepares the data for assessment.

* **Scenario Evaluation**: Once the data is extracted, the integration scenarios are evaluated based on the predefined rules, and an assessment is performed. The assessment includes:

  + an overall estimation in days of the effort according to the sizing classification (Small(S), Medium(M), Large(L), Extra Large (XL)) required to technically migrate the integration scenarios to SAP Integration Suite.

  + An assessment result that gives information regarding functional readiness to move those scenarios to SAP Integration Suite for each integration scenario.

  + The results of the assessment are described in detailed reports.

For a scenario evaluation request the following actions are available:

* **Open Dashboard**: It displays an analysis of your scenario evaluations with details specific about your integration flows such as assessment categories, adapters, and an overview of the rules used in the evaluation, which can be accessed and downloaded.

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-3-1.png)

* **Trigger analysis:** It is also possible to schedule a new evaluation run based on the current extracted data**.**

* **Download:** The scenario evaluation results can be downloaded in the form of reports as **.xlsx** and **.pdf** files.

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-4-3.png)

The **.xslx file** contains all the integration scenarios that were part of the request with migration effort according to the sizing classification, rules applied to them, weight, assessment categories and status.

![](/legacyfs/online/storage/blog_attachments/2023/01/MicrosoftTeams-image-7-1.png)

The .**pdf file** provides a general summary report of the assessed integration scenarios as well as adapters with various charts and tables which help summarize the overall migration complexity and effort.

![](/legacyf...
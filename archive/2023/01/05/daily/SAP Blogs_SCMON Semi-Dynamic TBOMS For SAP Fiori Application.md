---
title: SCMON Semi-Dynamic TBOMS For SAP Fiori Application
url: https://blogs.sap.com/2023/01/04/scmon-semi-dynamic-tboms-for-sap-fiori-application/
source: SAP Blogs
date: 2023-01-05
fetch_date: 2025-10-04T03:04:06.779586
---

# SCMON Semi-Dynamic TBOMS For SAP Fiori Application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SCMON Semi-Dynamic TBOMS For SAP Fiori Application

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161036&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SCMON Semi-Dynamic TBOMS For SAP Fiori Application](/t5/technology-blog-posts-by-sap/scmon-semi-dynamic-tboms-for-sap-fiori-application/ba-p/13559426)

![MGZ](https://avatars.profile.sap.com/d/8/idd8792e52e244d74abe5b30c0ac4e28925f16d48a735f8162e1d210cfde7cc467_small.jpeg "MGZ")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[MGZ](https://community.sap.com/t5/user/viewprofilepage/user-id/45578)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161036)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161036)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559426)

‎2023 Jan 04
5:25 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161036/tab/all-users "Click here to see who gave kudos to this post.")

2,391

* SAP Managed Tags
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [SOLMAN Test Suite](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Test%2520Suite/pd-p/132949817163443344955330185779754)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SOLMAN Test Suite

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BTest%2BSuite/pd-p/132949817163443344955330185779754)

View products (2)

**Intro**

This blog serves as a quick introduction to BPCA, but mainly to aims to provide the required knowledge and information about the SCMON Semi-Dynamic TBOMs for SAP Fiori Apps, its prerequisites, limitations and capabilities

Working with BPCA & SEA enables the users to analyze and forecast the required testing effort for new changes in enhancement packages, support packages, or even customer developments that may impact business processes.

This is done through BPCA functionalities where the objects in a transport are compared against the TBOMs in the managed system.

The BPCA can get an object list for business functions, as well as objects in transport, and compares this object list with the objects in TBOMs. Since every TBOM is assigned to an executable entity in a scenario, business process, or process step, you can determine which parts of a solution documentation are affected by any changes. To be able to use the BPCA, make requisite preparations in your system. Record the TBOMS and apply filter and criticality settings.

Please note the following requisite preparations:

* Assign executables to the solution documentation.

* Create a list of objects TBOM for every executable entity.

* Define test cases for the solution documentation.

* This process guides you through the required steps.

For more information, see [Business Process Change Analyzer (BPCA).](https://help.sap.com/docs/SAP_Solution_Manager/fbc7b5ecf5094fe0b6a2eb966160008f/e7ae57e0291149adaca93a9dcce33abb.html)

![](/legacyfs/online/storage/blog_attachments/2022/12/BPCA_BLOG.png)

**What is a TBOM?**

A TBOM is a list that contains all objects in an executable entity. These objects could be classes, UI elements, FM and tables.

For more information please visit the official website [here](https://help.sap.com/docs/SAP_Solution_Manager/fbc7b5ecf5094fe0b6a2eb966160008f/fb1ce5f08a14454eb7ead8193db2491b.html?locale=en-US).

TBOM could be created dynamically, statically, or semi-dynamically depending on the use case.

* Dynamic TBOM: They are considered the most precise. They can be generated manually by recording a transaction while it is being executed. All objects that were used in this execution are captured in the background and copied to the TBOM content.

The recorded/created dynamic TBOM will be attached to the executable position (e.g.:  process level, process step level, it  depends on where the executable exists and where the recording is executed).

you can find more details regarding Dynamic TBOMS [here.](https://help.sap.com/docs/SAP_Solution_Manager/fbc7b5ecf5094fe0b6a2eb966160008f/8da40909ff0a4b5285ef215a7c6932b8.html?locale=en-US)

* Semi Dynamic TBOM:

Semi-dynamic TBOMs are created in mass fashion using background job in BPCA. They are more accurate that the static TBOMs  as they are based on usage data (SCMON/UPL) in the production system. The created Semi Dynamic TBOM will be created and  attached to the executable in the executable's library, this TBOM will be referenced/inherited in all process steps/processes  where this executable exists.

Check the attached screenshot to see the data flow for Semi Dynamic TBOMs generation.

you can find more details regarding Semi Dynamic TBOM [here.](https://help.sap.com/docs/SAP_Solution_Manager/fbc7b5ecf5094fe0b6a2eb966160008f/8da40909ff0a4b5285ef215a7c6932b8.html?locale=en-US)

![](/legacyfs/online/storage/blog_attachments/2022/12/TBOM_DATA_FLOW_BLOG.png)

* Static TBOMs, which are based on ABAP trace data. They were the first developed TBOMs type.

Static TBOMs are also mass generated like the Semi Dynamic TBOMs, however, the Static TBOMs don’t use and usage data, so  no authorizations for the managed system are required. The dynamic calls or generated objects are not detected so they are not  part of the static TBOM. Therefore, the result is not as good as Semi Dynamic TBOMs or Dynamic TBOMs.

you can find more details regarding Static TBOM [here.](https://help.sap.com/docs/SAP_Solution_Manager/fbc7b5ecf5094fe0b6a2eb966160008f/8da40909ff0a4b5285ef215a7c6932b8.html?locale=en-US)

***NOTE: Static and semi-dynamic TBOMs do not support SAP Web Link (SAP\_LONG\_URL) applications (the URL of a portal, for example, which are used to start an SAP application in an ABAP application server). In this case, create dynamic TBOMs..***

**What is SCMON Data?**

The purpose of the ABAP Call Monitor (transaction SCMON) is to monitor the execution (usage) of ABAP code (function modules, method calls etc.) in your productive system.

 The advantage of the SCMON compared to the UPL (Usage Procedure Logging in SAP Solution Manager) is that using this tool, you not only collect the usage data (how often a specific ABAP object was called), but also the information about the calling business process.

 Since SCMON comes along with an enhanced functionality scope compared with UPL, you can consider SCMON as a successor and use it instead of UPL.

*For more information, please check the blog* [*here*](https://blogs.sap.com/2017/04/06/abap-call-monitor-scmon-analyze-usage-of-your-code/)*.*

**What is SAP Fiori?**

SAP Fiori is the main concepts/guidelines  used to design SAP applications.

It does not address only the UI design but it is concerned with the whole User Experience (UX).

It aims to provide role based applications, to enable the end users best experience possible using the app. For more information related to SAP Fiori please visit the provided links[*1*](https://exper...
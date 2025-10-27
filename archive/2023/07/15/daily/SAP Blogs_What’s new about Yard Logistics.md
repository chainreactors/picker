---
title: What’s new about Yard Logistics
url: https://blogs.sap.com/2023/07/14/whats-new-about-yard-logistics/
source: SAP Blogs
date: 2023-07-15
fetch_date: 2025-10-04T11:53:04.924512
---

# What’s new about Yard Logistics

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* What's new about Yard Logistics 2023

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51094&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What's new about Yard Logistics 2023](/t5/enterprise-resource-planning-blog-posts-by-sap/what-s-new-about-yard-logistics-2023/ba-p/13555341)

![nancy_an](https://avatars.profile.sap.com/7/0/id70c75c8782d2f6fa153a26b8f2290807eec58ae8cd02eeb022356fc0bbcf70b7_small.jpeg "nancy_an")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[nancy\_an](https://community.sap.com/t5/user/viewprofilepage/user-id/568703)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51094)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51094)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555341)

‎2023 Jul 14
6:45 PM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51094/tab/all-users "Click here to see who gave kudos to this post.")

3,887

* SAP Managed Tags
* [SAP NetWeaver Application Server](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server/pd-p/01200615320800000352)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [UI SAP Business Client (NWBC)](https://community.sap.com/t5/c-khhcw49343/UI%2520SAP%2520Business%2520Client%2520%28NWBC%29/pd-p/514184132407067932511783863172239)

* [SAP NetWeaver Application Server

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer/pd-p/01200615320800000352)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [UI SAP Business Client (NWBC)

  Software Product Function](/t5/c-khhcw49343/UI%2BSAP%2BBusiness%2BClient%2B%252528NWBC%252529/pd-p/514184132407067932511783863172239)

View products (3)

All the new features to be introduced have already been included in S/4HANA YARD LOGISTICS 2021 - Support Package 03. It would be recommended to have this SP installed instead of installing notes one by one, especially since some notes are too complex to be installed.

## Same Level Container Stacking

SAP Note: [3325118](https://launchpad.support.sap.com/#/notes/3325118)

A new feature for container stacking.

Prior to this feature, only one container is allowed on each level, now multiple containers can be stacked on one level which improves the utilization of available stacking locations

Please take care of the following restrictions:

+ Only 20ft and 40ft containers supported

+ Only top-level container can be moved

+ Need to switch on the option in customizing SPRO -> Yard Logistics -> Master Data -> Setting Up the Yard -> Yard Structure -> Define Stacking Storage Bin Types

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1-17.png)

## Pendel Moves

SAP Note: [3315523](https://launchpad.support.sap.com/#/notes/3315523)

A new feature allows activating and confirming Yard Task, even if preceding Yard Task is still in process which allows early Yard Task handling for occupied locations.

Movement Yard Task of truck 1 is in process, the movement will take time when the destination is far away from the source location.

With the new feature, Yard Task of truck 2 can be activated and confirmed even if the movement of truck 1 is still in process.

Please take care of the following restrictions:

+ Cancellation and rejection of preceding Yard Task prohibited

+ For Yard Task confirmation, need to implement BADI to change/enhance capacity consumption

+ Need to switch on the option in customizing SPRO -> Yard Logistics -> Master Data -> Setting Up the Yard -> Yard Structure -> Define Storage Type

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2-10.png)

## Enable UI Adaptation For Fiori Apps

SAP Notes: [3189880](https://launchpad.support.sap.com/#/notes/3189880), [3193848](https://launchpad.support.sap.com/#/notes/3193848), [3203716](https://launchpad.support.sap.com/#/notes/3203716) and [3196693](https://launchpad.support.sap.com/#/notes/3196693)

A new feature is introduced to enable UI adaptation for apps:

+ Self-Check in

+ Yard Task Execution

+ Adhoc YT

+ Berth Planning

In addition, a new field “License Plate” is available to show on Yard Task execution app.

With UI adaptation at runtime (RTA), key users can adapt the UI of UI5 apps in the SAP Fiori launchpad to fit the tasks and processes at their company – intuitively and without having to create new code, at runtime of the apps. The key user is the user who has been assigned the authorization role SAP\_UI\_FLEX\_KEY\_USER.

RTA has been enabled for UI5 apps: Self Check-In, Yard Task Execution, Ad hoc Yard Task and Berth Planning in SAP Yard Logistics 2009 for SAP S/4HANA and SAP Yard Logistics 2021 for SAP S/4HANA. The Berth Planning app is available in SAP Yard Logistics 2021 for SAP S/4HANA only.

Possibility to change the UI

+ Change positions of Yard Task elements

+ Rename fields

+ Add additional fields

+ Remove fields

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture3-7.png)

## Enable Description Change For Yard Task List

SAP Note: [3247038](https://launchpad.support.sap.com/#/notes/3247038) and [3246970](https://launchpad.support.sap.com/#/notes/3246970)

A new feature is introduced to enhance the description of Yard Task on the left Yard Task List area, for example adding source bin and destination bin into description.

BAdI is provided to custom the description. The customizing path of BAdI implementation:

SPRO->Yard Logistics->Business Add-Ins (BAdIs) for Yard Logistics->Yard Tasks->BAdI: Yard Task Execution App Enhancements

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture4-7.png)

## Automatic Refresh For Yard Task Execution In Manual Selection Mode

SAP Note: [3285245](https://launchpad.support.sap.com/#/notes/3285245)

SAP Yard Logistics provides a Fiori application for Yard Task execution with two selection modes, Queue and Manual selection modes.

In the previous versions, only the Queue selection mode supports automatically refresh on available Yard Task List.

This function is now extended to the Manual selection mode, which means both the Queue and the Manual selection of Yard Task Execution application support automatically refresh on available Yard Task List.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture5-7.png)

## New Alert Types 2815 & 2816 Are Available For Yard Task

SAP Note: [3317759](https://launchpad.support.sap.com/#/notes/3317759)

SAP Yard Logistics provides different Alert Types to raise alerts in the case of time deviations for a yard using Alert Monitor. The time deviation could relate to one of the following business objects of the yard:

+ Yard request

+ Yard order

+ Yard task

+ Transportation unit

Now two new Alert Types are delivered to customer for yard task execution:

+ 2815: Start of Yard Task delayed

+ 2816: Completion of Yard...
---
title: How to ensure that users can efficiently enter data in SAP Fiori elements applications
url: https://blogs.sap.com/2022/12/05/how-to-ensure-that-users-can-efficiently-enter-data-in-sap-fiori-elements-applications/
source: SAP Blogs
date: 2022-12-06
fetch_date: 2025-10-04T00:34:12.715470
---

# How to ensure that users can efficiently enter data in SAP Fiori elements applications

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to ensure that users can efficiently enter dat...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162958&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to ensure that users can efficiently enter data in SAP Fiori elements applications](/t5/technology-blog-posts-by-sap/how-to-ensure-that-users-can-efficiently-enter-data-in-sap-fiori-elements/ba-p/13565574)

![mariusfreitag](https://avatars.profile.sap.com/7/7/id77cccda6835578e8918499a78205c7a6ffbec2e1cb838bb43340d2ddd6efb081_small.jpeg "mariusfreitag")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[mariusfreitag](https://community.sap.com/t5/user/viewprofilepage/user-id/13884)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162958)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162958)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565574)

‎2022 Dec 05
9:51 PM

[15
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162958/tab/all-users "Click here to see who gave kudos to this post.")

4,021

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (4)

For a great user experience, it is very important that users can enter data quickly, fluently, and efficiently – even on a slow network. This is particularly relevant for power users, i.e., users who spend significant time with data entry, often using keyboard shortcuts to move from field to field. In this post, we will provide guidance on how to achieve efficient data entry for **draft-enabled SAP Fiori elements apps**.

![](/legacyfs/online/storage/blog_attachments/2022/12/SAP-Sales-Order-User-Version-B.png)

There are many aspects to consider when building efficient applications. Here, we will focus on the following aspects:

* [using the appropriate table type](#using-the-appropriate-table-type),

* [providing multiple empty table rows in edit mode](#providing-multiple-empty-table-rows-in-edit-mode),

* [optimizing the execution of side effects](#optimizing-the-execution-of-side-effects),

* and [simulating slow networks for testing](#simulating-slow-networks-for-testing).

While most of this post is relevant for any backend, it also covers some aspects that are specific to apps based on the [SAP ABAP RESTful Application Programming Model](https://help.sap.com/docs/BTP/923180ddb98240829d935862025004d6/289477a81eec4d4e84c0302fb6835035.html) (RAP) or the [SAP Cloud Application Programming Model](https://cap.cloud.sap/docs/) (CAP).

# Core principles of efficient data entry

* Minimize waiting times caused by validations or side effects – the consistency of the business object can be checked by the user at any time by pressing the ENTER key on a field.

* Avoid error or warning messages for fields that have not been filled out yet.

* Support column-based data entry in a table without error or warning messages.

* Allow entering incomplete data or references to not yet existing (master) data.

# Terminology

Before discussing concrete suggestions, on how you can optimize your applications, we have to clarify some important terminology:

* [**Draft handling**](https://ui5.sap.com/#/topic/ed9aa41c563a44b18701529c8327db4d.html)**:**

  + A draft is an interim version of a business entity that has not yet been saved as active version explicitly. This version is automatically saved in the background whenever its data is added or changed.

  + SAP Fiori elements leverages the draft concept to help prevent data loss and to allow users to pause and resume data entry corresponding to their own workflow.

* [**Side effects**](https://ui5.sap.com/#/topic/18b17bdd49d1436fa9172cbb01e26544):

  + If a user changes the content of a field, or performs another activity, this change can potentially influence other aspects (like fields, tables, etc.) on the UI. This system behavior is called a side effect.

  + Side effects are performed in the backend. However, the frontend needs to be informed which fields might be influenced by a change and thus need to be updated. Otherwise, the UI might still display outdated data.

  + For SAP Fiori elements apps, side effect annotations can be used for updating fields on the UI, for changing the visibility or enablement of fields, or for checking the consistency of fields.

  + Each side effect can define some triggering conditions (e.g. source entities or source properties) as well as targets that are to be refreshed or triggered after the source data was changed (e.g. target entities, target properties, or actions).

  + You can explore different ways to leverage side effect definitions in the [SAP Fiori elements flexible programming model explorer](https://ui5.sap.com/test-resources/sap/fe/core/fpmExplorer/index.html#/advancedFeatures/guidance/guidanceSideEffects).

* **Actions:**

  + An action represents business functionality that is part of the OData service and can be triggered by the frontend. Actions can implement validation functionality, calculate additional data, or contain any other logic that might be required for the use case.

  + Actions are declared by the backend and their implementation is specific to the used technology.

Some RAP-specific terms include:

* [**Validations**](https://help.sap.com/docs/BTP/923180ddb98240829d935862025004d6/171e26c36cca42699976887b4c8a83bf.html)**:**

  + A validation in RAP is a part of the business object behavior that checks the consistency of business object instances based on trigger conditions.

  + A validation is implicitly invoked by the business object’s framework when the trigger condition of the validation is fulfilled.

  + Trigger conditions can be create, update, and delete operations or field value changes.

  + Validations are always invoked during the save sequence.
...
---
title: Display Group Journal Entries with Reporting Logic
url: https://blogs.sap.com/2023/06/11/display-group-journal-entries-with-reporting-logic/
source: SAP Blogs
date: 2023-06-12
fetch_date: 2025-10-04T11:45:21.661874
---

# Display Group Journal Entries with Reporting Logic

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Display Group Journal Entries with Reporting Logic

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51382&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Display Group Journal Entries with Reporting Logic](/t5/enterprise-resource-planning-blog-posts-by-sap/display-group-journal-entries-with-reporting-logic/ba-p/13557159)

![harivenkatesh_subramanian](https://avatars.profile.sap.com/5/f/id5f0e63cf03b4c138ac485135c235cf8bbda2d35ba05cb5a6b272c4d2e6b56ba4_small.jpeg "harivenkatesh_subramanian")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[harivenkatesh\_subramanian](https://community.sap.com/t5/user/viewprofilepage/user-id/396424)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51382)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51382)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557159)

‎2023 Jun 11
8:11 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51382/tab/all-users "Click here to see who gave kudos to this post.")

2,825

* SAP Managed Tags
* [SAP S/4HANA Finance for group reporting](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance%2520for%2520group%2520reporting/pd-p/d43f39e4-1f4c-4ba5-9bba-dbadada2e08b)

* [SAP S/4HANA Finance for group reporting

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance%2Bfor%2Bgroup%2Breporting/pd-p/d43f39e4-1f4c-4ba5-9bba-dbadada2e08b)

View products (1)

## Introduction

Display Group Journal Entry with Reporting Logic app is now optimized for performance and memory consumptions. In this blog, we will have a detailed look about the recent enhancements.

## What would be part of SAP S/4HANA Cloud Release 2302.4?

We have introduced the following new tabs:

* Group Journal Entries: The Journal entries reflects the records from Group reporting only (ACDOCU table).

* Merged Journal Entries: The Journal entries reflects both group reporting and accounting records (ACDOCU and ACDOCA).

## How does the drill through / navigation work?

You can jump from Group Data Analysis and Group Financial statements – Review Booklet app to Display Group Journal Entry with reporting logic app. The default tab will always be “Group Journal Entries”.

From the tab “Group Journal Entries” you will be able to navigate to Display Group Journal entry without reporting logic app. On clicking the Document Number, the "Document Number" is passed as the navigation context. However, on clicking the Line (Posting) Item both the Document Number and Line (Posting) Item are passed to the target.

The  navigation / drill through of the new tabs is shown below:

## What are the other options in this app?

There is a possibility to select the sequence of the columns as per your choice, as shown below:

![](/legacyfs/online/storage/blog_attachments/2023/06/DGJEwRR_Columns.png)

Display Group Journal Entries with Reporting Logic - Columns

You can also group the fields and display it as per the selected groups:

![](/legacyfs/online/storage/blog_attachments/2023/06/DGJEwRR_GroupBy.png)

Display Group Journal Entry with Reporting Logic - Fields Group

## What are the known Limitations?

* The default tab will always be “Group Journal Entries”.

* When you are performing a jump from Group Data Analysis, the fiscal year period needs to be single selection in the variable prompt. The range and multiple single selection will not work. However, after the jump you can change the selections (both range and multiple single selections). This limitation is only valid for the jump/navigation scenario and not while loading the app as a standalone execution.

* You will only be able to jump to Display Group Journal Entries app (without reporting logic) from the tab “Group Journal Entries”.

## Conclusion

Please feel free to share your thoughts by commenting on this blog. Also, we can use this blog as a communication tool for any clarification that you require on this topic. You can also follow my profile for more content on analytical application for group reporting. I would recommend posting your questions by specifying the tag: “SAP S/4HANA Finance for group reporting”.

## Additional Links

[Group Journal Entries | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/90c07e91c7a64f328be3fd6b48955b13/d7c6ad9e3d844b1ca470697f2cfc3bfc.html?version=2302.503)

[UI Changes in the Display Group Journal Entries app | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/085edb30fb3d413da552832f3d5c01c0/c1f0a6e0356146acb5e3bc58e8715566.html?version=2302.500)

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [S4HANA](/t5/tag/S4HANA/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fdisplay-group-journal-entries-with-reporting-logic%2Fba-p%2F13557159%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Authorization control to display data for Manage Supplier Line Items using BP authorization group](/t5/enterprise-resource-planning-blog-posts-by-sap/authorization-control-to-display-data-for-manage-supplier-line-items-using/ba-p/14231135)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [I'm not getting the same result with my FI-GL validation on user account when using F2548 and when](/t5/enterprise-resource-planning-q-a/i-m-not-getting-the-same-result-with-my-fi-gl-validation-on-user-account/qaq-p/14228714)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [Introducing the WalkMe-based alternative in-app help user experience: What and How to Activate](/t5/enterprise-resource-planning-blog-posts-by-sap/introducing-the-walkme-based-alternative-in-app-help-user-experience-what/ba-p/14228279)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  a week ago
* [Import from Excel Journal Entries Date Error](/t5/enterprise-resource-planning-q-a/import-from-excel-journal-entries-date-error/qaq-p/14227395)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [Is it possible to add the Services Rendered Date field to the Journal Entry Analyzer?](/t5/enterprise-resource-planning-q-a/is-it-possible-to-add-the-services-rendered-date-field-to-the-journal-entry/qaq-p/14226198)
  in [Enterprise Resource...
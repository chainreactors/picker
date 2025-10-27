---
title: Fiori Tracker: Tiles usage and User monitoring for SAP Fiori launchpad (Monitoring SAP Fiori Launchpad)
url: https://blogs.sap.com/2023/07/29/fiori-tracker-tiles-usage-and-user-monitoring-for-sap-fiori-launchpad-monitoring-sap-fiori-launchpad/
source: SAP Blogs
date: 2023-07-30
fetch_date: 2025-10-04T11:52:48.130574
---

# Fiori Tracker: Tiles usage and User monitoring for SAP Fiori launchpad (Monitoring SAP Fiori Launchpad)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Fiori Tracker: Tiles usage and User monitoring for...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/155363&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Fiori Tracker: Tiles usage and User monitoring for SAP Fiori launchpad (Monitoring SAP Fiori Launchpad)](/t5/technology-blog-posts-by-members/fiori-tracker-tiles-usage-and-user-monitoring-for-sap-fiori-launchpad/ba-p/13520765)

![kevindass](https://avatars.profile.sap.com/0/2/id0265f9dc962bc7f4310e0d970efb6679636d1023921339b71ea54e554fb7161f_small.jpeg "kevindass")

[kevindass](https://community.sap.com/t5/user/viewprofilepage/user-id/1417)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=155363)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/155363)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13520765)

‎2023 Jul 29
8:44 AM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/155363/tab/all-users "Click here to see who gave kudos to this post.")

15,045

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Gateway](https://community.sap.com/t5/c-khhcw49343/SAP%2520Gateway/pd-p/01200615320800003185)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Gateway

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BGateway/pd-p/01200615320800003185)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)

View products (4)

## Intro

For any application or product monitoring and usage statistics is undoubtedly one of very demanded and most helpful when it comes to evaluate any planning to be done or decisions to be taken.

At present for on-premises SAP Fiori system there isn't a out-of-the box SAP standard UI5 application(s) or ABAP report for usage of various SAPUI5 applications hosted/configured onto Fiori launchpad, meaning users can’t run a ABAP report/open UI5 app and have the list of most popular SAP Fiori applications or pull user statistics.
> Currently SAP didn’t provide any tools to track the usage of the application (Tiles) in the launchpad. I came across several option & suggestions but none of them were really giving the real usages.

This is something many people have been looking for since the beginning of the SAP Fiori offering. So we thought(nikita\_bhat and myself) to come up with a custom framework solution based on the SAP Fiori launchpad plugin. The technical artifacts reside on Fiori gateway central hub system that collects data for each of backend systems in the landscape.

This is an open source project and we look forward for all of you to make use of it and come forward for improvements/feedback and features.

## **Target Audience**

This document is for whom has the experience of SAPUI5 along with ABAP OData service development

## Sneak peek of end results

Before getting into deep dive, let us see what is final goal

![](/legacyfs/online/storage/blog_attachments/2022/09/firstLook.png)

### Application Activity Tracker:

![](/legacyfs/online/storage/blog_attachments/2022/10/AppTracker-1.png)

This is an Fiori overview page (OVP) driven by ABAP CDS on Fiori gateway system.

### User Activity Tracker

## ![](/legacyfs/online/storage/blog_attachments/2023/05/UserCount.png)

This is an Fiori overview page (OVP) driven by ABAP CDS on Fiori gateway system.

On the first card, one could click on "Date" column and navigate to "User Logon Details" app via app-to-app navigation for various users logged in for a given date.

### User Logon Details

![](/legacyfs/online/storage/blog_attachments/2022/10/UserDetails.png)

This is an Fiori List Report driven by ABAP CDS on Fiori gateway system.

## Implementation Steps

Could be found on Github repo with documentation. Steps are as below for Launchpad Plugin Tracker:

1. [Launchpad Event Tracker](https://github.com/kevindass/poc-vs-FlpPluginEventTracker)

2. [Application Overview Page](https://github.com/kevindass/poc-vs-FlpPluginTrackerAppOVP)

3. [User Overview Page](https://github.com/kevindass/poc-vs-FlpPluginTrackerUserOVP)

4. [User Logon Details](https://github.com/kevindass/poc-vs-FlpPluginTrackerUserLogon)

5. [Purge Fiori activity application & user data](https://github.com/kevindass/poc-vs-FlpPluginTrackerPurgeData)

## Summary:

With above custom SAPUI5 applications it is now possible to monitor all Fiori tiles usage and user monitoring.

Thank you for reading and would like to hear from you and/or clarifying questions in the comment section.

* [Launchpad](/t5/tag/Launchpad/tg-p/board-id/technology-blog-members)
* [Monitoring](/t5/tag/Monitoring/tg-p/board-id/technology-blog-members)
* [sapfiori](/t5/tag/sapfiori/tg-p/board-id/technology-blog-members)
* [sapfiorilaunchpad](/t5/tag/sapfiorilaunchpad/tg-p/board-id/technology-blog-members)
* [SAPUI5](/t5/tag/SAPUI5/tg-p/board-id/technology-blog-members)

9 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Ffiori-tracker-tiles-usage-and-user-monitoring-for-sap-fiori-launchpad%2Fba-p%2F13520765%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Thursday
* [Top 10 SAP Cloud AL...
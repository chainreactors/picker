---
title: Data migration
url: https://blogs.sap.com/2023/02/24/data-migration-2/
source: SAP Blogs
date: 2023-02-25
fetch_date: 2025-10-04T08:03:52.163331
---

# Data migration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Data migration

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67386&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data migration](/t5/enterprise-resource-planning-blog-posts-by-members/data-migration/ba-p/13554425)

![JurgenLootens](https://avatars.profile.sap.com/b/6/idb657e37789b27235c53253b2dbbedf1d5ed61385db353217f2a44efe5ff7fde9_small.jpeg "JurgenLootens")

[JurgenLootens](https://community.sap.com/t5/user/viewprofilepage/user-id/125579)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67386)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67386)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554425)

‎2023 Feb 24
6:19 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67386/tab/all-users "Click here to see who gave kudos to this post.")

2,106

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Data Migration](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Data%2520Migration/pd-p/be32fdc2-968e-4717-97e2-1be5fb65bf99)

* [SAP S/4HANA Cloud Public Edition Data Migration

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BData%2BMigration/pd-p/be32fdc2-968e-4717-97e2-1be5fb65bf99)

View products (1)

Has anyone else felt that data migration tools are tough to use?

The toolset I would like to manage a data migration is the following:

**1. A data dump area in the SAP environment** where the data from the source system is dumped, as is, everything as character strings (no length limitation). Basically, this should be a case of "just grab me the data and I'll dump it in SAP". No errors, no conversions, no cleansing, no specs, no extractors, no nothing. Just some selects in SQL to a file or the windows clipboard and an upload into a generic data store.

In previous projects, I have see tremendous effort being put into writing extractor specifications, building extractors, building upload tools and developing templates to then realize that something was forgotten, the spec wasn't quite right, and all objects in the chain have to be amended and rerun. I believe this is a hassle that can be avoided.

**2. A data viewer/enhancer**. An environment where you can look at the datasets you have loaded. You should be able to start applying data conversions (like silly date formats or whatever), validity checks and data fixes, filling additional fields using formulas and lookups (in standard SAP or in the generic data store) and filtering data out. The key thing is that this should be visual, i.e. you should see the affect on the data straight away telling you if you've missed a mapping or a formula isn't generating a sensible result.

There should also be a way to link datasets together. Like for example if you dump the headers and lines of documents as two separate datasets, you should be able to link the two datasets in a visual way. The system should check that each child record has a parent, and immediately show you which records don't have a parent with a sad face - like my old mac did when its disk crashed.

In previous projects, looking at the data was usually a case of opening lots of excel spreadsheets saved in network drives or sharepoint folders and doing VLOOKUPS all over the place. Often people would make changes and lose them again or start creating many versions of the data files. Such a real hassle.

**3.** Then you should have **a nicely organized library of load modules:** the infamous BAPIs and function modules but also possibly class methods and batch upload programs etc. This library should be easily searchable and well documented: when to use each one and all the checks and validations they contain, auth required etc...

Consistenly good SAP documentation of BAPIs is notoriously hard to come by but I'm happy to be proven wrong on this point...

**4. A mapper/loader**. This is the magic. So once you've looked over the source data and gotten rid of the stuff you don't care about and added the missing columns with the data SAP needs etc... you should be able to simply drag your data columns onto the input fields of the load module you've selected and hit a load button. Obviously you wanna save this mapping and give it a pretty name so you remember what it was all about and also transport it to QAS and PRD to execute there.

The most recent data migration tool from SAP seems to be the data migration cockpit (DMC) which runs partly on LTMOM (SAP GUI transaction where you define your migration 'projects') and LTMC or the equivalent Fiori App where you can download templates, upload data files and load the data into SAP using the project's BAPI. Certainly in recent years, this tool is very powerful and complete. But for me, it starts from a couple of false assumptions:

- *You know up front which fields* will be used in SAP, how they are populated (under all circumstances) by the load module you've chosen and you know what source data maps to it how. That is the assumption to steers you towards a solution based on generated templates and putting the workload on the source data side. "Fill my templates perfectly, or else..." The amount of understanding required from the source data consultant about SAP needs to be very high in this scenario.

*- You don't need a programmer to do data migration.* *You don't need to understand the ins and outs of the BAPIs themselves*. For simple data loads, yes, but most environments will have complex scenarios where you will need to understand the BAPI very well (especially its reliance on the right customizing) to get through the load. Debugging is definitely needed at times. And the new OO code in ABAP is much tougher to navigate than the old procedural code (I'm a big fan of OO - or should I say 'enormous' ![:winking_face:](/html/@3246D6F4728FD081A343FF5678BB6F29/emoticons/1f609.png ":winking_face:") ).

- *Everything can be loaded using BAPIs*. Not always so...

* [Data Migration cockpit using staging table Option](/t5/tag/Data%20Migration%20cockpit%20using%20staging%20table%20Option/tg-p/board-id/erp-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fdata-migration%2Fba-p%2F13554425%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-s-4hana-public/ba-p/14234546)
  in [Enterprise Resource Planning Blog Posts b...
---
title: SAP Readiness Check for SAP S/4HANA – Note Analyzer Input File
url: https://blogs.sap.com/2023/03/02/sap-readiness-check-for-sap-s-4hana-note-analyzer-input-file/
source: SAP Blogs
date: 2023-03-03
fetch_date: 2025-10-04T08:31:42.318974
---

# SAP Readiness Check for SAP S/4HANA – Note Analyzer Input File

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP Readiness Check for SAP S/4HANA - Note Analyze...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51882&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Readiness Check for SAP S/4HANA - Note Analyzer Input File](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-readiness-check-for-sap-s-4hana-note-analyzer-input-file/ba-p/13560836)

![greg_clavier](https://avatars.profile.sap.com/c/d/idcdc17b98acd256436a4734eb2357b865189bd570150031514247ba9c7c1132cf_small.jpeg "greg_clavier")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[greg\_clavier](https://community.sap.com/t5/user/viewprofilepage/user-id/259873)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51882)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51882)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560836)

‎2023 Mar 02
11:21 PM

[29
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51882/tab/all-users "Click here to see who gave kudos to this post.")

28,390

* SAP Managed Tags
* [SAP Readiness Check](https://community.sap.com/t5/c-khhcw49343/SAP%2520Readiness%2520Check/pd-p/1647bf27-5e10-4efd-89e1-a59efaf4e250)

* [SAP Readiness Check

  Additional Software Product](/t5/c-khhcw49343/SAP%2BReadiness%2BCheck/pd-p/1647bf27-5e10-4efd-89e1-a59efaf4e250)

View products (1)

Have you been asked to run SAP Readiness Check for SAP S/4HANA to analyze your existing SAP ERP system? Or are you wanting to update the SAP Notes already applied within your landscape to take advantage of new or updated functionality in SAP Readiness Check for SAP S/4HANA? Are you now wondering which SAP Notes need to be implemented or updated?

Previously, identifying and implementing SAP Notes relevant to SAP Readiness Check for SAP S/4HANA took time and effort. The process started by evaluating the central guidance SAP Note (SAP Note [2913617 - SAP Readiness Check for SAP S/4HANA](https://launchpad.support.sap.com/#/notes/2913617)), which led to the manual navigation of dependent and prerequisite SAP Notes. As a result of the vast scope of SAP Readiness Check for SAP S/4HANA, this could involve searching, reviewing, and assessing over one hundred SAP Notes to determine those that need to implement within your system.

Today we are excited to announce the availability of support for those of you wanting to implement or update the SAP Notes required for enabling the data collectors of SAP Readiness Check for SAP S/4HANA. With the input file attached to SAP Note [3308130 - Note Analyzer Input File for SAP Readiness Check for SAP S/4HANA](https://launchpad.support.sap.com/#/notes/3308130), you can now use the note analyzer (available in the note assistant, also known as transaction SNOTE) to help identify missing or outdated SAP Notes necessary for running SAP Readiness Check for SAP S/4HANA. SAP Note [3200109 - SNOTE : Note Analyzer](https://launchpad.support.sap.com/#/notes/3200109) includes guidance and correction instructions for enabling this new note assistant functionality. In addition, as an attachment, SAP Note [3200109 - SNOTE : Note Analyzer](https://launchpad.support.sap.com/#/notes/3200109) offers a detailed user guide for this new capability. Below is some supplemental information on using the note analyzer to support the SAP Readiness Check for SAP S/4HANA data collectors.

|
 **Update from August 14, 2023**    Today we released SAP Note [3365856 - Note Analyzer Input File for SAP Readiness Check for SAP S/4HANA upgrades](https://me.sap.com/notes/3365856) to support customers upgrading from an older SAP S/4HANA product version to a newer one. Attached to this new SAP Note is a note analyzer input file for the checks included in SAP Readiness Check for SAP S/4HANA upgrades. See SAP Note [3059197 - SAP Readiness Check for SAP S/4HANA upgrades](https://me.sap.com/notes/3059197) for more information on this SAP Readiness Check scenario. The information below is also valid for this new note analyzer input file. |

## Preparing Your System

The first step in preparing your system for consuming the note analyzer input file is to be sure that both the software component ST-A/PI and SPAM are current.

Then confirm that the note assistant supports processing digitally signed SAP Notes and SAP Note transport-based correction instructions (TCIs). While many SAP Notes address both topics, we found that following SAP Note [2836302 - Automated guided steps for enabling Note Assistant for TCI and Digitally Signed SAP Notes](https://launchpad.support.sap.com/#/notes/2836302) provides the best end-to-end guidance.

The next step is to validate that the note assistant is up to date. Depending on the SAP\_BASIS software component version and support package level, you may need to implement several SAP Notes during this step. If you are on SAP\_BASIS 702 or lower, you will follow SAP Note [875986 - Note Assistant: Important notes for SAP\_BASIS up to 702](https://launchpad.support.sap.com/#/notes/875986) to update the note assistant. For SAP\_BASIS 730 or higher systems, you will follow SAP Note [1668882 - Note Assistant: Important notes for SAP\_BASIS 730,731,740,750,751,752,753,754,755,756](https://launchpad.support.sap.com/#/notes/1668882).

After updating the note assistant, you will enable the note analyzer following the guidance in [3200109 - SNOTE : Note Analyzer](https://launchpad.support.sap.com/#/notes/3200109). This SAP Note includes a transport-based correction instruction, so you must manually download the corresponding SAR file and upload it to your system. For more information on this process, see this SAP Help Portal page: [Implementing SAP Note Transport-Based Correction Instructions for the First Time.](https://help.sap.com/docs/ABAP_PLATFORM_NEW/9d6aa238582042678952ab3b4aa5cc71/8dc5621ba47b445e8ac5431fee7e5104.html?q=Implementing%20SAP%20Note%20Transport-Based%20Correction%20Instructions)

Once you have enabled the note analyzer in your system, the last preparation step is downloading the SAP Readiness Check for SAP S/4HANA input file attached to SAP Note [3308130 - Note Analyzer Input File for SAP Readiness Check for SAP S/4HANA](https://launchpad.support.sap.com/#/notes/3308130) and storing it in your local filesystem.

## Starting Note Analyzer in Note Assistant

After implementing the note analyzer within your system, start transaction SNOTE and select *Goto* --> *Other Tools* --> *Launch Note Analyzer* to enable the input file prompt. Depending on the SAP\_BASIS component version and support package level, part of the menu path may be in German.

Example 1: Note assistant menu path screenshot from a system on SAP\_BASIS 740 SP 0013:![](/legacyfs/online/storage/blog_attachments/2023/03/2023-02-21_10-23-57.png)

Example 2: Note assistant menu path screenshot from a system on SAP\_BASIS 753 SP 0007:![](/legacyfs/online/storage/blog_attachments/2023/03/2-1.p...
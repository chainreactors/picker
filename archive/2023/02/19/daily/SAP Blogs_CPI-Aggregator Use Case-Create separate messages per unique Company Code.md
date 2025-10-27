---
title: CPI-Aggregator Use Case-Create separate messages per unique Company Code
url: https://blogs.sap.com/2023/02/18/cpi-aggregator-use-case-create-separate-messages-per-unique-company-code/
source: SAP Blogs
date: 2023-02-19
fetch_date: 2025-10-04T07:29:57.783199
---

# CPI-Aggregator Use Case-Create separate messages per unique Company Code

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* CPI-Aggregator Use Case-Create separate messages p...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163224&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [CPI-Aggregator Use Case-Create separate messages per unique Company Code](/t5/technology-blog-posts-by-members/cpi-aggregator-use-case-create-separate-messages-per-unique-company-code/ba-p/13568421)

![pkaushiksrinivas](https://avatars.profile.sap.com/5/7/id57a83de789d7907bf663211edaadebb140c94ed9efe1af6f8ff52d51ec4f2d85_small.jpeg "pkaushiksrinivas")

[pkaushiksrinivas](https://community.sap.com/t5/user/viewprofilepage/user-id/721484)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163224)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163224)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568421)

‎2023 Feb 18
7:57 AM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163224/tab/all-users "Click here to see who gave kudos to this post.")

23,547

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

# Introduction

This blog covers an idea on how we can put CPI Aggregator to use for clubbing payloads having a similar value and creating separate files for them.

As an example, we can take Customer Master payloads being triggered from SAP to CPI. All these messages may have different company codes, but output needs to be created in such a way that, separate files need to be created for each unique company code viz. All payloads having Company Code=A will be present in a file, al payloads having Company Code=B will be present in another file and so on.

**Requirement :**

* Flow : SAP S4 --> CPI --> 3rd party system

* Source Message : IDOC (multiple IDOCs sent in a single Batch)

* Target Message : External Messgae

* Customer Master IDOCs will be sent from S4 HANA to CPI

* CPI will have to create a new file on 3rd party SFTP per unique Company Code (Messages having a particular Company Code will be clubbed together in one file)

**Sample Input :**

![](/legacyfs/online/storage/blog_attachments/2023/02/IDocSample.jpg)

Sample Input Having 2 unique Company Codes

**Output Expected :** 2 Files, one for 1156 Company Code and other for 1152 (As a Sample case, here Mail adapter is used instead of SFTP)

**CPI iFlow Sample :**

To mock a scenario-Content Modifier holds the IDOC data here, post which individual IDOCs are split in a general splitter. IDOC-External definition mapping is done in next step and aggregated further.

![](/legacyfs/online/storage/blog_attachments/2023/02/iflow-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/iflow1.png)

CPI iFlow Sample with Aggregation Condition

Using an Aggregator pattern, we can collect and store individual messages until a complete set of related messages have been received. The aggregated message is then sent to the actual receiver (One message per unique value in Correlation Condition)

We use an Aggregator to group all messages related to a particular Company Code by giving the Correlation Expression. (In the image above, the XPath in Aggregator Correlation is taken from External message post mapping)

**Output :**

![](/legacyfs/online/storage/blog_attachments/2023/02/output.jpg)

Output showing 2 separate eMails received for each unique customer code

**Pros :**

* Instead of writing complex mappings to achieve the above requirement, Aggregator makes it easier to group the message based on Correlation condition

**Cons :**

* Aggregator expects a waiting time, which means once data is received in an aggregator, it will wait for that amount of time after which it will send output to further steps.

Additional Observations :

Scenarios wherein grouping messages having a particular similar value like above is required, but instead of creating 2 separate files like above, only 1 file is required which contains data related to both company codes segregated within file at output, the use of Aggregator may have a limitation here.

However, would welcome integration experts to add observations and comments w.r.t the same.

## Summary

The use of Aggregator in CPI with a simple use case was explained above.

Comments or feedback/suggestions, pros/cons with respect to the above are welcome from fellow Integration folks.

## References :

* [Define Aggregator | SAP Help Portal](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/aa238166757b4f11878c50b07eb8b4b9.html)

* [EIPinCPI – Aggregator | SAP Blogs](https://blogs.sap.com/2020/04/12/eipincpi-aggregator/)

* [Aggregator in SAP CPI : Tutorial - Recode Hive](https://recodehive.com/aggregator-in-sap-cpi-tutorial/#:~:text=The%20aggregator%20is%20used%20to,the%20order%20of%20the%20messages.)

* [aggregator](/t5/tag/aggregator/tg-p/board-id/technology-blog-members)
* [CPI](/t5/tag/CPI/tg-p/board-id/technology-blog-members)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcpi-aggregator-use-case-create-separate-messages-per-unique-company-code%2Fba-p%2F13568421%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Error while extracting data: DataSource 0CO\_PC\_ACT\_02, package 000000 Message no. RODPS\_SAPI009](/t5/technology-q-a/error-while-extracting-data-datasource-0co-pc-act-02-package-000000-message/qaq-p/14234415)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [CAP - Use i18n for Error Messages](/t5/technology-q-a/cap-use-i18n-for-error-messages/qaq-p/14234048)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [Basic Configurations for SAP EWM Material Flow System: Part-1](/t5/t...
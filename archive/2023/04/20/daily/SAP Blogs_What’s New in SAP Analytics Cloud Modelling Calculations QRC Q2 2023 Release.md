---
title: What’s New in SAP Analytics Cloud Modelling Calculations QRC Q2 2023 Release
url: https://blogs.sap.com/2023/04/19/whats-new-in-sap-analytics-cloud-modelling-calculations-qrc-q2-2023-release/
source: SAP Blogs
date: 2023-04-20
fetch_date: 2025-10-04T11:32:57.775442
---

# What’s New in SAP Analytics Cloud Modelling Calculations QRC Q2 2023 Release

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* What’s New in SAP Analytics Cloud Modelling Calcul...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159691&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What’s New in SAP Analytics Cloud Modelling Calculations QRC Q2 2023 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modelling-calculations-qrc-q2-2023/ba-p/13555601)

![AmandaJMurphy](https://avatars.profile.sap.com/2/b/id2be1139995632ff49b683765e3c5f1a5f2827b8fa89cfa8a83947d2764e6f2a9_small.jpeg "AmandaJMurphy")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AmandaJMurphy](https://community.sap.com/t5/user/viewprofilepage/user-id/46075)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159691)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159691)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555601)

‎2023 Apr 19
11:53 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159691/tab/all-users "Click here to see who gave kudos to this post.")

1,580

* SAP Managed Tags
* [SAP Analytics Cloud, data modeling](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520data%2520modeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)

* [SAP Analytics Cloud, data modeling

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Bdata%2Bmodeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)

View products (1)

**Purpose**

Hello SAP Community colleagues!

This blog introduces the latest Modelling Calculations feature of the SAP Analytics Cloud 2023.07 release available for SAP Analytics Cloud FastTrack customers. For SAP Analytics Cloud Quarterly Release Cycle (QRC) customers, this feature will be available as part of the QRC Q2 2023 release. For more information, view the QRC release schedule [here](https://blogs.sap.com/2023/01/18/sap-analytics-cloud-tenants-on-quarterly-release-cycle-qrc-updates-in-2023/).

**Overview**

Modellers can access two new formulas within the Calculations Workspace of SAP Analytics Cloud:

* SUBTOTAL

* %SUBTOTAL

These return the subtotal & percentage of subtotal for a member, broken down by one or multiple dimensions.

They are available for account models and for models that contain both measures and accounts.

Let’s take a closer look at these new formulas.

* **SUBTOTAL**

SUBTOTAL returns the subtotal of a member, broken down by a dimension or multiple dimensions. Up to 10 dimensions can be passed in as parameters.

![](/legacyfs/online/storage/blog_attachments/2023/04/SubtotalImageWithBorder.png)

New SUBTOTAL formula

In the screenshot, we can see an example of SUBTOTAL, where at the top level of the TST\_PRODUCT dimension, Alcohol, Juice, Soft Drinks & Water are added to give a subtotal of 429 million.

At the next level of the hierarchy, PRD005 & PRD006 are combined to give a subtotal of 251m for Water.

* **%SUBTOTAL**

%SUBTOTAL returns the % of subtotal for a member broken down by dimension or multiple dimensions.  Up to 10 dimensions can be passed in as parameters.

![](/legacyfs/online/storage/blog_attachments/2023/04/SubtotalWithBorder.png)

New %SUBTOTAL Formula

In the screenshot above, %SUBTOTAL is calculated using the Measure \* 100 / subtotal value.

For example, Water is (251m \* 100) / 429 = 58.61%

**Note**

For both formulas, values are not aggregated over non-aggregable dimensions.  For example, other Accounts, other Versions, or other Categories.

We also recommend that modelers apply their own preferred scaling option to their results.  For example, set the result to million with two decimal places for SUBTOTAL and set the result to percent with two decimal places for %SUBTOTAL.

**Conclusion**

There are plenty more innovative new Model Calculations features to come in 2023, so watch this space!

If you have any questions, feel free to comment below or post a question to our [SAP Analytics Cloud Questions & Answers](https://community.sap.com/topics/cloud-analytics?ct=qa&lng=en&tab=content) forum.

See this [SAP Knowledge Base Article](https://userapps.support.sap.com/sap/support/knowledge/E/2728183) if you’d like to learn more about FastTrack and Quarterly Release Cycle releases.

For further information, visit our [SAP Analytics Cloud Community](https://community.sap.com/topics/cloud-analytics) pages to find more product information, best practices, and more. And check out our [SAP Road Map Explorer](https://roadmaps.sap.com/board?PRODUCT=67838200100800006884&amp;range=CURRENT-LAST&range=CURRENT-LAST) to see more upcoming features of SAP Analytics Cloud.  Thanks for reading!

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [Modelling Calculations](/t5/tag/Modelling%20Calculations/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fwhat-s-new-in-sap-analytics-cloud-modelling-calculations-qrc-q2-2023%2Fba-p%2F13555601%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Adding calculated rows in SAP Analytics Cloud table for lightweight calculations](/t5/technology-q-a/adding-calculated-rows-in-sap-analytics-cloud-table-for-lightweight/qaq-p/14234439)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [SAP analytic Model disappeared](/t5/technology-q-a/sap-analytic-model-disappeared/qaq-p/14233735)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Thursday
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Thursday
* [Exploring CDS based Analytical Models with the Relation Explorer - analytical view/perspective](/t5/technology-blog-posts-by-sap/exploring-cds-based-analytical-models-with-the-relation-explorer-analytical/ba-p/14229070)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Choosing the Right SAP Analytics Tool: Features, Benefits, and Strategy](/t5/technology-blog-posts-by-sap/choosing-the-right-sap-analytics-tool-features-benefits-and-strategy/ba-p/14230016)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110...
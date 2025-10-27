---
title: SAP S/4HANA Migration Cockpit – Direct Transfer: understand selection
url: https://blogs.sap.com/2022/11/25/sap-s-4hana-migration-cockpit-direct-transfer-understand-selection/
source: SAP Blogs
date: 2022-11-26
fetch_date: 2025-10-03T23:48:59.452830
---

# SAP S/4HANA Migration Cockpit – Direct Transfer: understand selection

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Migration Cockpit – Direct Transfer: u...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51668&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Migration Cockpit – Direct Transfer: understand selection](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-migration-cockpit-direct-transfer-understand-selection/ba-p/13558778)

![HJensen](https://avatars.profile.sap.com/2/c/id2ceb60e70789cbce1491826e4d728df948f3af0b5afef1670cbede41ee60e3be_small.jpeg "HJensen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[HJensen](https://community.sap.com/t5/user/viewprofilepage/user-id/131431)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51668)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51668)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558778)

‎2022 Nov 25
2:10 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51668/tab/all-users "Click here to see who gave kudos to this post.")

3,341

* SAP Managed Tags
* [SAP S/4HANA migration cockpit](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520migration%2520cockpit/pd-p/791935194581077217831679640306539)

* [SAP S/4HANA migration cockpit

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bmigration%2Bcockpit/pd-p/791935194581077217831679640306539)

View products (1)

Hello!

My name is Heike Jensen and I am a member of SAP’s **SAP S/4HANA Migration Cockpit Product Management** team.

Today, I want to talk about the topic "selection".

In the SAP S/4HANA Migration Cockpit – Direct Transfer, the step *selection* is a crucial step.

On the surface it looks quite "easy" - nevertheless, the logic underneath to derive the right organisational units and to decide which records or parts of records have to be selected is indeed very complex. Just think about objects where you don't find the org units in the header table.

SAP predefines the selection criteria, e.g. in the case of an SAP ERP source system the company code. So you use one or more company codes to select from the source system.

In addition, the logic defined in the migration objects you added to your project is applied.

So what to do if you get selection results you did not expect?

1. **Check the migration object documentation - what is in scope and out of scope for this object**

[Available Migration Objects | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/d3a3eb7caa1842858bf0372e17ad3909/8dd142b479f9481891fa8b3f86648df3.html)

Pls. make sure that you choose the right release in the header of the page.

**2. Check out background information in the LTMOM Deep dive slide deck**

[LINK](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.sap.com%2Fdocuments%2F2020%2F10%2F62dc808c-b87d-0010-87a3-c30de2ffd8ff.html)

Slides 32 - 43 provide background information. On slide 40 you find an example (which refers to the object *product*) which illustrates how complex such a selection logic can be.

**3. Have a look into the migration object definition (use transaction LTMOM)**

**4. Check out technical deep dive paper**

We recently published **KBA** [3249988](https://launchpad.support.sap.com/#/notes/3249988): Details on selection process – SAP S/4HANA Migration Cockpit – Direct Transfer. The **PDF** attached there explains in very technical details how the selection works. This document might help to find the root cause in case you get selection results you did not expect.

**It is not possible to debug the selection as it is executed in batch.**

The requirement to provide more capabilities to analyse the selection outcome is known.

I hope these explanations give a better understanding of this complex topic and the tips are of use for you.

Best regards,

Heike

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [analyse](/t5/tag/analyse/tg-p/board-id/erp-blog-sap)
* [debug](/t5/tag/debug/tg-p/board-id/erp-blog-sap)
* [Error](/t5/tag/Error/tg-p/board-id/erp-blog-sap)
* [issue](/t5/tag/issue/tg-p/board-id/erp-blog-sap)
* [problem](/t5/tag/problem/tg-p/board-id/erp-blog-sap)
* [selection](/t5/tag/selection/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsap-s-4hana-migration-cockpit-direct-transfer-understand-selection%2Fba-p%2F13558778%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [Agentic AI Testing for Greenfield S/4HANA Outbound Interfaces - Part 1](/t5/enterprise-resource-planning-blog-posts-by-members/agentic-ai-testing-for-greenfield-s-4hana-outbound-interfaces-part-1/ba-p/14232427)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Wednesday
* [What’s New in SAP Central Business Configuration 2506 FD2](/t5/enterprise-resource-planning-blog-posts-by-sap/what-s-new-in-sap-central-business-configuration-2506-fd2/ba-p/14231324)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [How to update or maintain Multilingual Text for Equipment's/Functional Location in SAP Public Cloud](/t5/enterprise-resource-planning-q-a/how-to-update-or-maintain-multilingual-text-for-equipment-s-functional/qaq-p/14227440)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [Extensibility Assistant for Key Users: The extensibility expert right next to you](/t5/enterprise-resource-planning-blog-posts-by-sap/extensibility-assistant-for-key-users-the-extensibility-expert-right-next/ba-p/14216097)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-i...
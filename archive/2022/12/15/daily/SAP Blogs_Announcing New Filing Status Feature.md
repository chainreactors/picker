---
title: Announcing New Filing Status Feature
url: https://blogs.sap.com/2022/12/14/announcing-new-filing-status-feature/
source: SAP Blogs
date: 2022-12-15
fetch_date: 2025-10-04T01:32:03.050101
---

# Announcing New Filing Status Feature

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Announcing New Filing Status Feature

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50468&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Announcing New Filing Status Feature](/t5/enterprise-resource-planning-blog-posts-by-sap/announcing-new-filing-status-feature/ba-p/13550741)

![leakuhn15](https://avatars.profile.sap.com/0/a/id0af57fd83e69cdf875cd2c9ee9091de97b3e168345336d5a79bc8f3f1239f4a7_small.jpeg "leakuhn15")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[leakuhn15](https://community.sap.com/t5/user/viewprofilepage/user-id/46138)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50468)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50468)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550741)

‎2022 Dec 14
11:00 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50468/tab/all-users "Click here to see who gave kudos to this post.")

2,118

* SAP Managed Tags
* [HCM Payroll USA](https://community.sap.com/t5/c-khhcw49343/HCM%2520Payroll%2520USA/pd-p/462200480581075348782619056800112)

* [HCM Payroll USA

  Software Product Function](/t5/c-khhcw49343/HCM%2BPayroll%2BUSA/pd-p/462200480581075348782619056800112)

View products (1)

### Prerequisites

The feature described in this blog post is only valid for release 608 and above. See SAP Note [3223858](https://launchpad.support.sap.com/#/notes/3223858).

#### **BSI TaxFactory 11.0**

For customers using BSI TaxFactory 11.0 OnPremise: minimum Cyclic H level.
For customers using BSI TaxFactory 11.0 SaaS: the solution is already available on the TaxFactory instance.

### Introduction

Now you can synchronize your Filing Status information with BSI TaxFactory 11.0 data automatically, and no maintenance is required anymore. The only thing you have to do is set the new **BSI Filing Status Synchronization** (BSIFS) configuration option to active (ON), and the **BSI Filing Status** (T5UTKZ) table will be used as source of information.

Let me show you this feature in more details:

### New source for valid Filing Status

Up until now, you maintain the **Withholding Info W4/W5 US** (0210) and the **IRS Limits USA** (0161) infotypes and the unique source of information for valid filing statuses within the system is the **Marital Status** (T5UTK) table, and the maintenance is your responsibility.

But from now on, you can use the **Marital Status** (T5UTK) table or the **BSI Filing Status** (T5UTKZ) table as source of information for valid filing statuses, depending on the value in configuration option **BSI Filing Status Synchronization** (BSIFS).

So, to wrap things up, this valid filing statuses data is provided by BSI, as the **BSI Filing Status** (T5UTKZ) table is synchronized with the BSI Tax Factory 11.0 API ReturnMaritalStatusInfoForFormula, and there is no maintenance needed on the new table.

Okay, but how can you use this? To do that, see more information on the configuration below:

SAP Note [3223858](https://launchpad.support.sap.com/#/notes/3223858) - *BSI: Filing status synchronization with TaxFactory 11.0* delivers the **BSI Filing Status Synchronization** (BSIFS) configuration option. And you can use this configuration to activate (ON) or deactivate (OFF) the usage of the **BSI Filing Status** (T5UTKZ) as source of information for valid filing statuses, in the **Customer values for configuration options** (V\_T5F99K2) table view.

#### Note

By default, SAP system will consider the **Manual Filing Status (maint required)** as deactivated (OFF). If you use the configuration option as OFF, it will have no impact on the current functionality of the system.

If you want to know more and implement this feature, see SAP Note [3223858](https://launchpad.support.sap.com/#/notes/3223858) - *BSI: Filing status synchronization with TaxFactory 11.0* and system documentation.

Did you enjoy this blog post? Give it a Like and share the content with your colleagues, and feel free to leave a feedback, comments, or questions in the space below. And don’t forget to follow the tag HCM Payroll USA in SAP Community to stay tuned on the Payroll USA blogs.

You can also leave your questions in our [Q&A platform on SAP Community](https://answers.sap.com/tags/462200480581075348782619056800112) using the HCM Payroll USA Tag.

All the best, and happy reading!

Lea Kuhn

User Assistance Developer

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fannouncing-new-filing-status-feature%2Fba-p%2F13550741%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [Japan Bank Charges in Payment Lots](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-lots/ba-p/14231915)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [Enhanced Variant Table Handling in PMEVC: Excel Download and Upload of Variant Tables](/t5/enterprise-resource-planning-blog-posts-by-sap/enhanced-variant-table-handling-in-pmevc-excel-download-and-upload-of/ba-p/14231777)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [Supply Chain Management in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/supply-chain-management-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14214877)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [EAM: F6065 : Features Send Output/Output status are greyed out](/t5/enterprise-resource-planning-q-a/eam-f6065-features-send-output-output-status-are-greyed-out/qaq-p/14204657)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2025 Sep 02

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0...
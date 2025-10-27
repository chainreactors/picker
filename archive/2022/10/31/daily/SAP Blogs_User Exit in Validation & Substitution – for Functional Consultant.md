---
title: User Exit in Validation & Substitution – for Functional Consultant
url: https://blogs.sap.com/2022/10/30/user-exit-in-validation-substitution-for-functional-consultant/
source: SAP Blogs
date: 2022-10-31
fetch_date: 2025-10-03T21:21:03.748708
---

# User Exit in Validation & Substitution – for Functional Consultant

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* User Exit in Validation & Substitution - for Funct...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67671&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [User Exit in Validation & Substitution - for Functional Consultant](/t5/enterprise-resource-planning-blog-posts-by-members/user-exit-in-validation-substitution-for-functional-consultant/ba-p/13558598)

![former_member225722](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225722")

[former\_member225722](https://community.sap.com/t5/user/viewprofilepage/user-id/225722)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67671)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67671)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558598)

‎2022 Oct 30
10:59 AM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67671/tab/all-users "Click here to see who gave kudos to this post.")

13,104

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)
* [FIN Asset Accounting](https://community.sap.com/t5/c-khhcw49343/FIN%2520Asset%2520Accounting/pd-p/253758978139952938680563247610563)
* [FIN Controlling](https://community.sap.com/t5/c-khhcw49343/FIN%2520Controlling/pd-p/165905235116577077914579113243106)
* [FIN General Ledger](https://community.sap.com/t5/c-khhcw49343/FIN%2520General%2520Ledger/pd-p/141573396494884189617506284133567)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)
* [FIN Asset Accounting

  Software Product Function](/t5/c-khhcw49343/FIN%2BAsset%2BAccounting/pd-p/253758978139952938680563247610563)
* [FIN Controlling

  Software Product Function](/t5/c-khhcw49343/FIN%2BControlling/pd-p/165905235116577077914579113243106)
* [FIN General Ledger

  Software Product Function](/t5/c-khhcw49343/FIN%2BGeneral%2BLedger/pd-p/141573396494884189617506284133567)

View products (7)

# **Purpose**

How to write a user exit for validation and substitution. Sometime there is a requirement which we can achieve only with the help of technical team. Here I am explaining how a functional guy can make some basic user exit and ask ABAP team to write the correct logic.

# **Introduction**

This document aims to identify and describe all steps associated with the user exit during validation & Substitution. In addition, This document will be used as a key communication who want to explore the possibilities in Validation & Substitution by ABAP.

**Audience** – This will help functional consultant.

## **Configuration**

T code – GGB1

Create a substitution rule like ZXXXXXXX

Write a prerequisite condition for the rule.

Write a substitution and mention the user exit

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-30-at-4.19.09-PM.png)

There is standard program available for Validation/Substitution, we need to copy these and make our Z program and assign these Z program to Application area

T code – GXC2

GBLR - RGGBR000 (Validation-Standard)

GBLS - RGGBS000 (Substitution-Standard)

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-30-at-4.19.48-PM.png)

Write your logic in Z program with mentioned user exit with help of ABAP

Here I am mentioning standard for reference.

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-30-at-4.20.18-PM.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-30-at-4.20.40-PM.png)

Please share your feedback and let me know in case you need blog on any specific topic.

**Please follow my blog for FI cutover activities –**

<https://blogs.sap.com/2022/10/14/sap-fi-cutover-activity-plan-complete-activities/>

Please follow the below link for related topic

<https://answers.sap.com/tags/648420875567243523242285841826221>

and read other posts on the topic –

<https://blogs.sap.com/tags/648420875567243523242285841826221/>

**Please follow my profile for related information. Thanks Everyone** **![:slightly_smiling_face:](/html/@CB4E4CB9DC3C08A3AD56D3C681CE34D1/emoticons/1f642.png ":slightly_smiling_face:")**

* [find user exit](/t5/tag/find%20user%20exit/tg-p/board-id/erp-blog-members)
* [HANA](/t5/tag/HANA/tg-p/board-id/erp-blog-members)
* [SAP](/t5/tag/SAP/tg-p/board-id/erp-blog-members)
* [sap hana](/t5/tag/sap%20hana/tg-p/board-id/erp-blog-members)
* [substituion in the account document](/t5/tag/substituion%20in%20the%20account%20document/tg-p/board-id/erp-blog-members)
* [Validation](/t5/tag/Validation/tg-p/board-id/erp-blog-members)
* [validation and substitution](/t5/tag/validation%20and%20substitution/tg-p/board-id/erp-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fuser-exit-in-validation-substitution-for-functional-consultant%2Fba-p%2F13558598%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Int4 Suite Agents Empowers Functional Consultants To Test Integrated SAP S/4HANA Business Processes](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-agents-empowers-functional-consultants-to-test-integrated-sap-s/ba-p/14234100)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  4 hours ago
* [Agentic AI Testing for Greenfield S/4HANA Outbound Interfaces - Part 1](/t5/enterprise-resource-planning-blog-posts-by-members/agentic-ai-testing-for-greenfield-s-4hana-outbound-interfaces-part-1/ba-p/14232427)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Wednesday
* [Multiple Functional Modules](/t5/enterprise-resource-planning-q-a/multiple-functional-modules/qaq-p/14228215)
 ...
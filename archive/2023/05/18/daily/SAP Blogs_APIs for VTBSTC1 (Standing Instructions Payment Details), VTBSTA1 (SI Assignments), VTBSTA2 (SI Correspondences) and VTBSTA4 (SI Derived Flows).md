---
title: APIs for VTBSTC1 (Standing Instructions Payment Details), VTBSTA1 (SI Assignments), VTBSTA2 (SI Correspondences) and VTBSTA4 (SI Derived Flows)
url: https://blogs.sap.com/2023/05/17/apis-for-vtbstc1-standing-instructions-payment-details-vtbsta1-si-assignments-vtbsta2-si-correspondences-and-vtbsta4-si-derived-flows/
source: SAP Blogs
date: 2023-05-18
fetch_date: 2025-10-04T11:39:46.786893
---

# APIs for VTBSTC1 (Standing Instructions Payment Details), VTBSTA1 (SI Assignments), VTBSTA2 (SI Correspondences) and VTBSTA4 (SI Derived Flows)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* APIs for VTBSTC1 (Standing Instructions Payment De...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50889&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [APIs for VTBSTC1 (Standing Instructions Payment Details), VTBSTA1 (SI Assignments), VTBSTA2 (SI Correspondences) and VTBSTA4 (SI Derived Flows)](/t5/enterprise-resource-planning-blog-posts-by-sap/apis-for-vtbstc1-standing-instructions-payment-details-vtbsta1-si/ba-p/13553809)

![monika_eggers](https://avatars.profile.sap.com/f/6/idf6679f41b87014c50068e1552a6bd82a32a3a48290642a39a1d397d3f801d86a_small.jpeg "monika_eggers")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[monika\_eggers](https://community.sap.com/t5/user/viewprofilepage/user-id/183717)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50889)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50889)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553809)

‎2023 May 17
10:46 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50889/tab/all-users "Click here to see who gave kudos to this post.")

3,611

* SAP Managed Tags
* [FIN Treasury](https://community.sap.com/t5/c-khhcw49343/FIN%2520Treasury/pd-p/506578197626473234529624753618175)

* [FIN Treasury

  Software Product Function](/t5/c-khhcw49343/FIN%2BTreasury/pd-p/506578197626473234529624753618175)

View products (1)

Have you found yourself in the difficult situation of needing to mass-create or update VTBSTC1 data (Standing Instructions Payment Details), VTBSTA1 data (SI Assignments), VTBSTA2 data (SI Correspondences) and/or VTBSTA4 data (SI Derived Flows) that are part of the EA-FINSERV extension of the company code data of the Financial Services Business Partner)? Until recently the only way to maintain them other than through transaction BP used to be via Direct Input, i.e. function module FTB\_BUPA\_DARK\_MAINTAIN\_INTERN.

![](/legacyfs/online/storage/blog_attachments/2023/05/Screenshot_VTBSTC1_SI_Payment_Details.png)

Now with note [3146931](https://launchpad.support.sap.com/#/notes/3146931) there is an API (no BAPI though) and it is part of the CIF (complex interface for business partner, customer and vendor/supplier (function module CVI\_EI\_INBOUND\_MAIN / method CL\_MD\_BP\_MAINTAIN=>MAINTAIN / method CVI\_EI\_ADAPTER=>START\_INBOUND\_MAIN / START\_INBOUND\_MAIN\_SINGLE, but also function module BUPA\_INBOUND\_MAIN\_SAVE). You can find the four new datasets at this navigation path:

I\_DATA TYPE CVIS\_EI\_EXTERN\_T -> CVIS\_EI\_EXTERN -> PARTNER Type BUS\_EI\_EXTERN -> **FINSERV\_DATA\_CC** Type FTBP\_EI\_DATA\_CC -> COMPANY\_CODE Type FTBP\_EI\_COMPANY\_CODE\_T -> FTBP\_EI\_COMPANY\_CODE.

![](/legacyfs/online/storage/blog_attachments/2023/05/Screenshot_FTBP_EI_COMPANY_CODE.png)

Please be advised to leave the field FTBP\_EI\_COMPANY\_CODE-TASK empty. It is only still there for downward compatibility.

Then, as usual, set the individual tasks to I, U. M or D for insert, update, modify (combined insert/update) and delete, and for update and modify set the DATAX flags for the fields that are to be changed, unless of course the data is being sent in current state.

There is currently no integration yet into the business partner replication service {[http://sap.com/xi/SAP\_BS\_FND/MDG/Global2}BusinessPartnerSUITEBulkReplicateRequest\_In](http://sap.com/xi/SAP_BS_FND/MDG/Global2%7DBusinessPartnerSUITEBulkReplicateRequest_In).

If you are looking for information about the API for VTBSTA3, which has existed for two years, please refer to <https://blogs.sap.com/2021/04/14/apis-for-vtbsta3-standing-instructions-authorizations/>.

Now with this new API you will have a much easier time when you need to mass-create or update Standing Instructions data. If you have questions you can comment here or ask in the SAP Q&A Community under the [FIN Treasury](https://answers.sap.com/tags/506578197626473234529624753618175) tag.

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [business partner](/t5/tag/business%20partner/tg-p/board-id/erp-blog-sap)
* [fsbp](/t5/tag/fsbp/tg-p/board-id/erp-blog-sap)
* [ftbp](/t5/tag/ftbp/tg-p/board-id/erp-blog-sap)

14 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fapis-for-vtbstc1-standing-instructions-payment-details-vtbsta1-si%2Fba-p%2F13553809%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Common configuration issues: Joule for SAP S/4HANA Cloud Private Edition](/t5/enterprise-resource-planning-blog-posts-by-sap/common-configuration-issues-joule-for-sap-s-4hana-cloud-private-edition/ba-p/14125996)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Jun 12
* [Packaging Instruction creation and assignment](/t5/enterprise-resource-planning-q-a/packaging-instruction-creation-and-assignment/qaq-p/14094128)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2025 May 06
* [Manage Assignments with Assignment API in SAP Project and Resource Management](/t5/enterprise-resource-planning-blog-posts-by-sap/manage-assignments-with-assignment-api-in-sap-project-and-resource/ba-p/14012529)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Feb 27
* [Finance with SAP S/4HANA Cloud Public Edition 2502](/t5/enterprise-resource-planning-blog-posts-by-sap/finance-with-sap-s-4hana-cloud-public-edition-2502/ba-p/13957394)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Feb 12
* [Setup Resource Management Capability in SAP Projects and Resource Management](/t5/enterprise-resource-planning-blog-posts-by-sap/setup-resource-management-capability-in-sap-projects-and-resource/ba-p/13999829)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Feb 03

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/2233182) | 8 |
| [![Andrew_Ford](https://avatars.profile.sap.com/4/2/id42fc9a5c18fc3229159993b...
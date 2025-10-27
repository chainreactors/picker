---
title: Two-Tier Master Data Replication using BTP Master Data Integration Service (MDI)
url: https://blogs.sap.com/2022/12/21/two-tier-master-data-replication-using-btp-master-data-integration-service-mdi/
source: SAP Blogs
date: 2022-12-22
fetch_date: 2025-10-04T02:13:12.986062
---

# Two-Tier Master Data Replication using BTP Master Data Integration Service (MDI)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Two-Tier Master Data Replication using BTP Master ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51254&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Two-Tier Master Data Replication using BTP Master Data Integration Service (MDI)](/t5/enterprise-resource-planning-blog-posts-by-sap/two-tier-master-data-replication-using-btp-master-data-integration-service/ba-p/13556426)

![abhijitbolakhe](https://avatars.profile.sap.com/7/8/id785970a42e950d25a92c67a33d56236b322a438045dc56e530a0e3274784fa7a_small.jpeg "abhijitbolakhe")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[abhijitbolakhe](https://community.sap.com/t5/user/viewprofilepage/user-id/155223)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51254)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51254)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556426)

‎2022 Dec 21
3:16 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51254/tab/all-users "Click here to see who gave kudos to this post.")

2,037

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)

View products (2)

Master Data Replication between Head Office and Subsidiary is the most critical aspects for a smooth functioning of 2Tier Scenarios.

Now we can replicate Master Data using Master Data Integration BTP Service.

SAP Master Data Integration (MDI) is a multi-tenant cloud service for master data integration. It provides a consistent view on master data across a hybrid landscape. SAP Master Data Integration based on the SAP One Domaine Model is a key component of the Intelligent Enterprise’s suite qualities and hence, helps enterprises to become an intelligent and sustainable enterprise

![](/legacyfs/online/storage/blog_attachments/2022/12/MDI1.jpg)

SAP Master Data Integration

Replicate Master Data from S/4HANA On-Premise /Private Cloud to BTP MDI

In S/4HANA OP/Private Cloud , Data Replication Framework can be used to invoke SOAP Services.

[https://help.sap.com/docs/SAP\_MASTER\_DATA\_INTEGRATION/c7713d6177ad479d9ea00958db9f2f81/5877c76703484...](https://help.sap.com/docs/SAP_MASTER_DATA_INTEGRATION/c7713d6177ad479d9ea00958db9f2f81/5877c7670348479889c3a756bfd87e90.html)

BTP Master Data Service needs to be configured with Service Key as given in below SAP Help Link

[https://help.sap.com/docs/SAP\_MASTER\_DATA\_INTEGRATION/c7713d6177ad479d9ea00958db9f2f81/dab76d5506a44...](https://help.sap.com/docs/SAP_MASTER_DATA_INTEGRATION/c7713d6177ad479d9ea00958db9f2f81/dab76d5506a44c8e85f314fc3be30e13.html)

Then BTP Master Data Integration (Orchestration) needs to be configured

BTP MDO allows master data replication according to predetermined master data distribution models. SAP Master Data Orchestration can only be used in combination with the SAP Master Data Integration service

![](/legacyfs/online/storage/blog_attachments/2022/12/MDI2.jpg)

Master Data Orchestration

![](/legacyfs/online/storage/blog_attachments/2022/12/MDI3.jpg)

MDO Business Objects

Manage Business Object Type  is used to configure the business object type so that the business context is applied during the distribution of your master data. You can also add extension fields to extend the business object type

The Distribution Model will be used to Pull Master data from MDI to S/4Hana Cloud.

A detailed blog will follow with end to end scenario

Labels

* [Expert Insights](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/expert%20insights)

* [Hybrid Cloud ERP](/t5/tag/Hybrid%20Cloud%20ERP/tg-p/board-id/erp-blog-sap)
* [SAP S4HANA Insight Series](/t5/tag/SAP%20S4HANA%20Insight%20Series/tg-p/board-id/erp-blog-sap)
* [Two-Tier ERP](/t5/tag/Two-Tier%20ERP/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Ftwo-tier-master-data-replication-using-btp-master-data-integration-service%2Fba-p%2F13556426%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Enterprise Support Academy Newsletter October 2025](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-enterprise-support-academy-newsletter-october-2025/ba-p/14232476)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [A Practical Guide to Cost Center APIs in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/a-practical-guide-to-cost-center-apis-in-sap-s-4hana-cloud/ba-p/14229337)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday
* [[Korea] Direct Integration of SAP with National Tax Service (NTS) Hometax Site](/t5/enterprise-resource-planning-q-a/korea-direct-integration-of-sap-with-national-tax-service-nts-hometax-site/qaq-p/14226387)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [IDOCs are Still Safe for SAP S/4HANA - SAP Clean Core Extensibility Level B](/t5/enterprise-resource-planning-blog-posts-by-members/idocs-are-still-safe-for-sap-s-4hana-sap-clean-core-extensibility-level-b/ba-p/14225439)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/223318...
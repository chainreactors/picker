---
title: Demand Planning for Expiring Lots
url: https://blogs.sap.com/2022/12/09/demand-planning-for-expiring-lots/
source: SAP Blogs
date: 2022-12-10
fetch_date: 2025-10-04T01:06:07.145869
---

# Demand Planning for Expiring Lots

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Demand Planning for Expiring Lots

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66915&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Demand Planning for Expiring Lots](/t5/enterprise-resource-planning-blog-posts-by-members/demand-planning-for-expiring-lots/ba-p/13548629)

![faisal_aslam12478](https://avatars.profile.sap.com/2/5/id256f07037a2e3a4963aba48ad71ecb6111b9605c9e426c58d4646eed5c8edd30_small.jpeg "faisal_aslam12478")

[faisal\_aslam12478](https://community.sap.com/t5/user/viewprofilepage/user-id/826267)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66915)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66915)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548629)

‎2022 Dec 09
5:50 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66915/tab/all-users "Click here to see who gave kudos to this post.")

1,123

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)

View products (1)

**Introduction:**

Demand planning is the procedure of forecasting the demand for a product or service. So, it can be produced and delivered more proficiently and to the satisfaction of clients. Demand planning is considered a necessary step in supply chain and enables a company to project future demand planning and successfully customize the company’s output in effective manners.

**Objective:**

The objective of this blog is to explain and demonstrate the basic and advanced concepts of Demand Plan for Expiring Lots process. For this purpose, we have plans to replenish expiring stock so that there is no disruption to Production. Currently, SAP Supply Planning doesn’t consider the expiry date of inventory so that a future proposal is considered to have enough Supply even if the intended Raw Materials inventory is set to expire before the date of the proposal it is intended for.

**Audience**

Consultants/Business Users/Beginners

**Enhancements for Demand Plan for Expiring Lots:**

A Custom WorkCentre has been developed Demand Plan for Expiring Lots for this purpose to.

* Demand Plan for Expiring Lots

**Process Flow and Views:**

Navigate Supply Planning WorkCentre>>Go to Stock Overview>>Enter Product ID>> Enter Site ID>>Set Expiry Date>>Check Stock Overview of selected Product in given time period

![](/legacyfs/online/storage/blog_attachments/2022/12/S1.png)

Navigate Demand Plan Work Center>>Select Stock\_Expiry\_Month/Week>>Click on Scope Maintenance tab and add product that you have checked in stock overview>>Click on save and Close

![](/legacyfs/online/storage/blog_attachments/2022/12/S2.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/S3.png)

Navigate Demand Plan For Expiring Lots Work Center>>Go to Demand Plan Run Setting>>Fill all required fields (Month/Week)>>Click on Save

![](/legacyfs/online/storage/blog_attachments/2022/12/S4.png)

Navigate Demand Plan for Expiring Lots Work Center>>Go to Demand Plan Information>>Check the product and stock including planning period which you have selected in last step

![](/legacyfs/online/storage/blog_attachments/2022/12/S6.png)

Navigate Demand Plan for Expiring Lots Work Center>>Go to Demand Plan Run>>Run Demand Plan For Expiring Lot

![](/legacyfs/online/storage/blog_attachments/2022/12/S7.png)

Navigate Demand Plan Work Center>>Select Stock\_Expiry\_Month/Week>>Click on Plan Tab>>Check the Planning period and Stock of the Product

![](/legacyfs/online/storage/blog_attachments/2022/12/S8.png)

I have tried to explain the process flow of Demand Plan for Expiring Lots in simple terms. It may be helpful for those who want to understand the basic and advanced process of ‘Demand Plan for Expiring Lots’ in SAP Business ByDesign.

Looking forward to hearing your ideas and comments.

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fdemand-planning-for-expiring-lots%2Fba-p%2F13548629%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Integrating SAP IBP with SAP S/4HANA Private Cloud for Demand Planning Using CI-DS](/t5/enterprise-resource-planning-blog-posts-by-sap/integrating-sap-ibp-with-sap-s-4hana-private-cloud-for-demand-planning/ba-p/14219426)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Supply Chain Management in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/supply-chain-management-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14214877)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [Retail, fashion and vertical business in SAP S/4HANA Cloud public edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/retail-fashion-and-vertical-business-in-sap-s-4hana-cloud-public-edition/ba-p/14197250)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  a month ago
* [Purchasing Planning Monitor for Collective Evaluation of MRP Planning Results](/t5/enterprise-resource-planning-blog-posts-by-sap/purchasing-planning-monitor-for-collective-evaluation-of-mrp-planning/ba-p/14200697)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 02
* [Professional Services in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/professional-services-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14202789)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![former_member816598](https://avatars.profile.sap.com/former_member_small.jpeg "former_member81...
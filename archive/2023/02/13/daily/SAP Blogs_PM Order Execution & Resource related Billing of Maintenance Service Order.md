---
title: PM Order Execution & Resource related Billing of Maintenance Service Order
url: https://blogs.sap.com/2023/02/12/pm-order-execution-resource-related-billing-of-maintenance-service-order/
source: SAP Blogs
date: 2023-02-13
fetch_date: 2025-10-04T06:27:57.031141
---

# PM Order Execution & Resource related Billing of Maintenance Service Order

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* PM Order Execution & Resource related Billing of M...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53140&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [PM Order Execution & Resource related Billing of Maintenance Service Order](/t5/enterprise-resource-planning-blog-posts-by-sap/pm-order-execution-resource-related-billing-of-maintenance-service-order/ba-p/13568510)

![former_member446064](https://avatars.profile.sap.com/former_member_small.jpeg "former_member446064")

[former\_member446064](https://community.sap.com/t5/user/viewprofilepage/user-id/446064)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53140)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53140)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568510)

‎2023 Feb 12
11:54 AM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53140/tab/all-users "Click here to see who gave kudos to this post.")

2,436

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)

View products (2)

**Introduction:**

In this blog we will discuss the process of creation of confirmation wrt PM order to build the actual cost base. And subsequently creating DMR (Debit Memo Request) through RRB (Resource related Billing) of MS Order is demonstrated through a recording.

**Overview**

The price for customer specific services are more often determined based on various resources consumed viz, personnel, material, travel to perform the service. This is enabled through Resource related Billing process. At the high level, following are the prerequisites for processing RRB of Maintenance Service order.

Configuration of

1. PM order configuration of confirmations, Goods Movements, External Procurement

2. DIP Profile

3. Debit Memo Request / Credit Memo Request document type

4. Item Category

5. Item Category Assignment to Document Type (DMR/CMR)

6. Assign cost condition type to Document Type (DMR/CMR)

7. Copy control Sales Document (& item category) to Billing Document (& item category)

8. Pricing Procedure

Master Data and Transaction level activities

9. Service Material (ex., Labour, Travel, Expense etc.,)

10. Spare Part

11. Price master data (of Service Material, Spare Part)

12. Assigning of DIP profile, setting Billing Relevance attribute to summarized billing or itemized billing to MSO line item.

13. PM Order with confirmation of actuals– Labour confirmation, Goods Issue , Expense booking etc.,

**Related blog to refer** :       [Maintenance Service Processing in S4 HANA | SAP Blogs](https://blogs.sap.com/2023/02/12/maintenance-service-processing-in-s4-hana/)

Kindly go through recording to visualize in SAP system the process of Resource Related Billing of Maintenance Service Order and another variant of billing for fixed price billing through the App Release for Billing. Through this app we will create a BDR first (Billing Document request) and then the billing document.

[Execution of PMO and Billing of MSO - SAP Media Share](https://video.sap.com/media/t/1_d7xq9wc9)

**Plz visit SAP Help**

[https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/3757ad8f98484812b58947bb8e6a2663/51cfa721e37542a5b08...](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3757ad8f98484812b58947bb8e6a2663/51cfa721e37542a5b082cdb86ce5556f.html?q=maintenance%20service)

You can also follow the S/4HANA Services roadmap for the future directions of the solution on Maintenance Service Processing.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [Maintenance Service RRB](/t5/tag/Maintenance%20Service%20RRB/tg-p/board-id/erp-blog-sap)
* [S4HANA - Advance Execution Service](/t5/tag/S4HANA%20-%20Advance%20Execution%20Service/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fpm-order-execution-resource-related-billing-of-maintenance-service-order%2Fba-p%2F13568510%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [My Learning Journal on BTP (5) - Build A Small Finance Agent: CAP + Generative AI Hub + LangChain](/t5/enterprise-resource-planning-blog-posts-by-sap/my-learning-journal-on-btp-5-build-a-small-finance-agent-cap-generative-ai/ba-p/14222295)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [S/4HANA Cloud Public Data Migration Plan](/t5/enterprise-resource-planning-q-a/s-4hana-cloud-public-data-migration-plan/qaq-p/14219226)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago
* [Corrective Maintenance End To End Process with Material Management Integration](/t5/enterprise-resource-planning-blog-posts-by-members/corrective-maintenance-end-to-end-process-with-material-management/ba-p/14206779)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  3 weeks ago
* [All about SAP S/4HANA Service solution – collection of links in SAP S/4HANA Service topic](/t5/enterprise-resource-planning-blog-posts-by-sap/all-about-sap-s-4hana-service-solution-collection-of-links-in-sap-s-4hana/ba-p/14203325)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 01
* [Professional Services in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/professional-services-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14202789)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_i...
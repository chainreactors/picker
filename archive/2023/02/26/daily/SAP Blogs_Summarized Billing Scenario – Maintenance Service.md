---
title: Summarized Billing Scenario – Maintenance Service
url: https://blogs.sap.com/2023/02/25/summarized-billing-scenario-maintenance-service/
source: SAP Blogs
date: 2023-02-26
fetch_date: 2025-10-04T08:08:25.306746
---

# Summarized Billing Scenario – Maintenance Service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Summarized Billing Scenario – Maintenance Service

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51447&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Summarized Billing Scenario – Maintenance Service](/t5/enterprise-resource-planning-blog-posts-by-sap/summarized-billing-scenario-maintenance-service/ba-p/13557611)

![former_member446064](https://avatars.profile.sap.com/former_member_small.jpeg "former_member446064")

[former\_member446064](https://community.sap.com/t5/user/viewprofilepage/user-id/446064)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51447)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51447)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557611)

‎2023 Feb 25
1:07 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51447/tab/all-users "Click here to see who gave kudos to this post.")

1,446

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)

View products (2)

Summarized Billing is a onetime billing of the maintenance service job for example resource related billing. At the outset let us understand the business use cases where this can be applied.

The customer has to be charged based on:

1. Total cost-plus uplift – An equipment repair of a competitor’s product as a one-off service request from the customer has to be processed. Typically, most of the resources consumed may not have a price master.

Service jobs of a newly introduced product line for the resources consumed need not have price master, as they are in the initial stages of establishing service support / stabilization of price master for billing support.

2. Agreed cost plus uplift – The individual service agreement is the actuals will be reviewed and jointly agreed on what will be considered / will not be considered as chargeable cost. Certain type of expenses are permitted to be charged or limitations imposed on what qty / percentage of that expense can be charged (say labour limited to maximum of 20 hrs and travel / boarding subject to evidence with receipts will be allowed). An uplift over chargeable cost incurred is explicitly agreed for the job.

It is pertinent to note if different resources consumed for the job are to be taxed at different rates, an itemized billing scenario as one time billing with the same principle of cost-plus uplift has to be considered.

Illustrative screen shots are given below for the summarized billing scenario:

1. Maintenance Service Order line with billing relevance value = F summarized billing with a DIP profile is set up.

![](/legacyfs/online/storage/blog_attachments/2023/02/image001-2.png)

Agreed mark up for this job is 15 %. It can be defaulted from price master data or manually updated as agreed for the job.

![](/legacyfs/online/storage/blog_attachments/2023/02/image003-1.png)

2.  On Release of the line-item PM order is created as per integration set up.

![](/legacyfs/online/storage/blog_attachments/2023/02/image005.png)

3.  PM Order is Released and confirmations are processed wrt this Order.

![](/legacyfs/online/storage/blog_attachments/2023/02/image007-1.png)

4.   Run the App **Create Resource Related Billing Request** – Maintenance Service.

Make a decision to reject labor billing for Qty > 10 as agreed with customer. Last 2 dynamic lines proposed are rejected by service professional.

![](/legacyfs/online/storage/blog_attachments/2023/02/image009-3.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/image011-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/image014.png)

Actual cost (PCO4)  = 500  (labor cost ) +  13.51  (spare part cost)  = **513.51** for the service product **SM\_PROD02** .

On this actual cost  uplift percentage of 15% is applied.

![](/legacyfs/online/storage/blog_attachments/2023/02/image017-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/image020-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/image022-1.png)

DMR is successfully created.

![](/legacyfs/online/storage/blog_attachments/2023/02/dmr.jpg)

**Reference :  [Maintenance Service Processing in S4 HANA | SAP Blogs](https://blogs.sap.com/2023/02/12/maintenance-service-processing-in-s4-hana/)**

Labels

* [Life at SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/life%20at%20sap)

* [Maint Service RRB](/t5/tag/Maint%20Service%20RRB/tg-p/board-id/erp-blog-sap)
* [Summarized BIlling](/t5/tag/Summarized%20BIlling/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsummarized-billing-scenario-maintenance-service%2Fba-p%2F13557611%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [A Practical Guide to Cost Center APIs in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/a-practical-guide-to-cost-center-apis-in-sap-s-4hana-cloud/ba-p/14229337)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday
* [Parts with 01 and 04 inspection types activated for subcontracting PO process-need UD auto](/t5/enterprise-resource-planning-q-a/parts-with-01-and-04-inspection-types-activated-for-subcontracting-po/qaq-p/14221863)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago
* [Supply Chain Management in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/supply-chain-management-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14214877)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [Retention Process in SAP Purchase Orders: A Practical Guide](/t5/enterprise-resource-planning-blog-posts-by-members/retention-process-in-sap-purchase-orders-a-practical-guide/ba-p/14212122)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-...
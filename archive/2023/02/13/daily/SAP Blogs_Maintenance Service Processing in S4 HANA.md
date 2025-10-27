---
title: Maintenance Service Processing in S4 HANA
url: https://blogs.sap.com/2023/02/12/maintenance-service-processing-in-s4-hana/
source: SAP Blogs
date: 2023-02-13
fetch_date: 2025-10-04T06:28:07.702479
---

# Maintenance Service Processing in S4 HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Maintenance Service Processing in S4 HANA

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/49497&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Maintenance Service Processing in S4 HANA](/t5/enterprise-resource-planning-blog-posts-by-sap/maintenance-service-processing-in-s4-hana/ba-p/13543611)

![former_member446064](https://avatars.profile.sap.com/former_member_small.jpeg "former_member446064")

[former\_member446064](https://community.sap.com/t5/user/viewprofilepage/user-id/446064)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=49497)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/49497)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543611)

‎2023 Feb 12
4:41 AM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/49497/tab/all-users "Click here to see who gave kudos to this post.")

4,143

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

**Introduction:**

**A Maintenance Service Order (MSO)** is created to manage commercial aspects of service agreed between the service provider and recipient. This MSO line item is integrated with a **plant** **maintenance order** **(PMO)** wherein planning and execution of technical aspects are managed. This is an equivalent representation of ERP Customer Service (CS) Order say SM02 (Revenue Bearing) Order Type.

The best of both worlds of these two objects in S/4HANA should bring in business benefits in various forms for the customers exploring migration and transformational journey.

**Overview**

At the high level,

The combination of MSO line item and PMO is equivalent to CS Order.

The customer, sales area, billing relevance data etc., are maintained at the MSO and each line item will automatically generate a PMO when life cycle status of MSO line is set as Released.

PMO covers technical aspect like Maintenance operations, spare parts planning, execution, monitoring and control of maintenance.

The MSO can have multiple line items each supported by an individual PM order and depending upon the billing requirement, the billing relevance attributes will be selected for each of the MSO line.

**Presently the following billing capabilities are available in Maintenance Service Processing are:**

A. **Resource Related Billing of MSO** (for an individual line or set of lines)

1. Itemized Billing (equivalent to billing using DP90 transaction with Bill Form = 02 or blank in ERP CS solution)

2. Summarized Billing (equivalent to billing using DP90 transaction with Bill Form = 01 in ERP CS solution)

B. **Fixed price Billing**

This can be done using the S/4HANA Service APP "Release for Billing"

The Maintenance Service Solution will be aligned to New Financial Accounting Solution for Services in S4HANA.

Please share your questions. We will try to add subsequent blogs to help you explore our solution in S4HANA.

Regards

Plz visit SAP Help

[https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/3757ad8f98484812b58947bb8e6a2663/51cfa721e37542a5b08...](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3757ad8f98484812b58947bb8e6a2663/51cfa721e37542a5b082cdb86ce5556f.html?q=maintenance%20service)

You can also follow the S/4HANA Services roadmap for the future directions of the solution on Maintenance Service Processing.

Kindly watch out for follow up blogs on

1. MSO creation leading to automated PMO creation;                                                                **Link** :   [Creation of PM Order from Maintenance Service Order | SAP Blogs](https://blogs.sap.com/2023/02/12/creation-of-pm-order-from-maintenance-service-order/)

2. PMO creation leading to automated MSO creation

3. PM Execution (confirmation) & Resource related Billing

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [S4HANA - Advance Execution Service](/t5/tag/S4HANA%20-%20Advance%20Execution%20Service/tg-p/board-id/erp-blog-sap)
* [S4HANA - Maintenance Service](/t5/tag/S4HANA%20-%20Maintenance%20Service/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fmaintenance-service-processing-in-s4-hana%2Fba-p%2F13543611%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [Van stock visibility without using storage locations](/t5/enterprise-resource-planning-q-a/van-stock-visibility-without-using-storage-locations/qaq-p/14232928)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday
* [A Practical Guide to Cost Center APIs in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/a-practical-guide-to-cost-center-apis-in-sap-s-4hana-cloud/ba-p/14229337)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday
* [How to Create and Manage Blanket or Framework Purchase Orders in SAP S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-create-and-manage-blanket-or-framework-purchase-orders-in-sap-s/ba-p/14226571)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  a week ago
* [API Call API\_MAINTAINANCEORDER ends with HTTP RC 423 and message "Billable Order 4001380 is not sup](/t5/enterprise-resource-planning-q-a/api-call-api-maintainanceorder-ends-with-http-rc-423-and-message-quot/qaq-p/14225480)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/2233182) | 8 |
| [![Andrew_Ford](https://avatars.profile.sap.com/4/2/id42fc9a5c18fc3229159993bbd8c3abd793e64af5050b65e9a4b850c04ce6bbb7_small.jpeg "Andrew_Ford")  ![Product and Topic Expert](/html/@138D6F765B6...
---
title: Creation of PM Order from Maintenance Service Order
url: https://blogs.sap.com/2023/02/12/creation-of-pm-order-from-maintenance-service-order/
source: SAP Blogs
date: 2023-02-13
fetch_date: 2025-10-04T06:28:05.117065
---

# Creation of PM Order from Maintenance Service Order

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Creation of PM Order from Maintenance Service Orde...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53114&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creation of PM Order from Maintenance Service Order](/t5/enterprise-resource-planning-blog-posts-by-sap/creation-of-pm-order-from-maintenance-service-order/ba-p/13568353)

![former_member446064](https://avatars.profile.sap.com/former_member_small.jpeg "former_member446064")

[former\_member446064](https://community.sap.com/t5/user/viewprofilepage/user-id/446064)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53114)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53114)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568353)

‎2023 Feb 12
5:26 AM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53114/tab/all-users "Click here to see who gave kudos to this post.")

5,201

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)

View products (2)

**Introduction:**

In this blog the process of creation of MS Order and through that  automation of creation of PM order is demonstrated through a recording.

**Overview**

At the high level, following are the pre requisites for running the process of creation of PM order through MS order:

1. Configuration of MS transaction type, item category and determination of item category.

2. Configuration of PM Order Type

3. Specifically, Configuration that integrates MS transaction type, item category with PM order type

![](/legacyfs/online/storage/blog_attachments/2023/02/MSO-PMO-int.jpg)

1. Master Data of BP, Service product, Equipment , task list

2. Mapping of service product to task list group/ counter thru transaction OISD.

On creation of a MS order and setting the life cycle status of MS order item to Released the PM order creation is automated.

The customer, sales area, billing relevance data etc., are maintained at the MSO and each line item will automatically generate a PMO when life cycle status of MSO line is set as Released.

Related Blog  <http://Maintenance> Service Processing in S4 HANA | SAP Blogs

The embedded recording will help in the visualization in SAP system of the above process.

**Create PMO from MSO video link is given below**

[Create PMO from MSO-1 - SAP Media Share](https://video.sap.com/media/t/1_67r0txx5)

**Plz visit SAP Help**

[https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/3757ad8f98484812b58947bb8e6a2663/51cfa721e37542a5b08...](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3757ad8f98484812b58947bb8e6a2663/51cfa721e37542a5b082cdb86ce5556f.html?q=maintenance%20service)

You can also follow the S/4HANA Services roadmap for the future directions of the solution on Maintenance Service Processing.

Kindly watch out for follow up blog on

PM Execution (confirmation) & Resource related Billing

Pls do leave your feed back.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [S4HANA - Advance Execution Service](/t5/tag/S4HANA%20-%20Advance%20Execution%20Service/tg-p/board-id/erp-blog-sap)
* [SAP Maintenance Service](/t5/tag/SAP%20Maintenance%20Service/tg-p/board-id/erp-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fcreation-of-pm-order-from-maintenance-service-order%2Fba-p%2F13568353%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Van stock visibility without using storage locations](/t5/enterprise-resource-planning-q-a/van-stock-visibility-without-using-storage-locations/qaq-p/14232928)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [A Practical Guide to Cost Center APIs in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/a-practical-guide-to-cost-center-apis-in-sap-s-4hana-cloud/ba-p/14229337)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday
* [API Call API\_MAINTAINANCEORDER ends with HTTP RC 423 and message "Billable Order 4001380 is not sup](/t5/enterprise-resource-planning-q-a/api-call-api-maintainanceorder-ends-with-http-rc-423-and-message-quot/qaq-p/14225480)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago
* [Purchase requisition is not automatically generated when creating the process order](/t5/enterprise-resource-planning-q-a/purchase-requisition-is-not-automatically-generated-when-creating-the/qaq-p/14221625)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/2233182) | 8 |
| [![Andrew_Ford](https://avatars.profile.sap.com/4/2/id42fc9a5c18fc3229159993bbd8c3abd793e64af5050b65e9a4b850c04ce6bbb7_small.jpeg "Andrew_Ford")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") Andrew\_Ford](/t5/user/viewprofilepage/user-id/98013) | 8 |
| [![DianaMala](https://avatars.profile.sap.com/6/d/id6db8ca00c3368971fe9ea45165f8ca02b42d3fc0d2b18891c590b300d9206a82_small.jpeg "DianaMala")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png ...
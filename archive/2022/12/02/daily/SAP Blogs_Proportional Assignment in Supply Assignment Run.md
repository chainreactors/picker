---
title: Proportional Assignment in Supply Assignment Run
url: https://blogs.sap.com/2022/12/01/proportional-assignment-in-supply-assignment-run/
source: SAP Blogs
date: 2022-12-02
fetch_date: 2025-10-04T00:17:09.336926
---

# Proportional Assignment in Supply Assignment Run

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Proportional Assignment in Supply Assignment Run(A...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52127&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Proportional Assignment in Supply Assignment Run(ARun)](/t5/enterprise-resource-planning-blog-posts-by-sap/proportional-assignment-in-supply-assignment-run-arun/ba-p/13562347)

![rameshraja_r](https://avatars.profile.sap.com/9/2/id926f49500d9a6885bfa0041021daf44eb0df6fdc5cf5a0bb4fca2481385c3ab3_small.jpeg "rameshraja_r")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[rameshraja\_r](https://community.sap.com/t5/user/viewprofilepage/user-id/213652)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52127)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52127)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562347)

‎2022 Dec 01
10:56 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52127/tab/all-users "Click here to see who gave kudos to this post.")

1,470

* SAP Managed Tags
* [SAP Fashion Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fashion%2520Management/pd-p/67838200100800006229)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA for advanced ATP](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520for%2520advanced%2520ATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fashion Management

  SAP Fashion Management](/t5/c-khhcw49343/SAP%2BFashion%2BManagement/pd-p/67838200100800006229)
* [SAP S/4HANA for advanced ATP

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bfor%2Badvanced%2BATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)

View products (3)

In previous blogs, we discussed about the [overview of Supply Assignment](https://blogs.sap.com/2022/10/10/supply-assignment-arun-in-sap-s-4-hana/) and how it can be executed through a BOP Variant. In this blog, we will see the use cases for proportional assignment of supply to demand and to achieve this in Supply Assignment.

There are situations where limited supply of a product needs to be distributed among the customer orders in such a way that each order gets a fair share of the available supply.

In below example, if orders are assigned sequentially then Sales Order 4 does not get any supply. Whereas proportional distribution ensures the available supply is distributed among the demand.

![](/legacyfs/online/storage/blog_attachments/2022/11/Proportional-Distribution-2.png)

Sequential vs Proportional Assignment

**Configuration:**

Below set up is required to carry out proportional assignment in Supply Assignment Rule.

![](/legacyfs/online/storage/blog_attachments/2022/11/Configure-Supply-Assignment-Rule-Proportional.png)

Configuration Supply Assignment (Proportional)

Attach the Supply Assignment Rule in BOP Variant.

![](/legacyfs/online/storage/blog_attachments/2022/11/Configure-BOP-Variant1.png)

Configure BOP Variant

Execute the BOP Variant and check the results in Monitor Supply Assignment Runs.

![](/legacyfs/online/storage/blog_attachments/2022/11/Monitor-Supply-Assignment-Runs1-1.png)

Monitor Supply Assignment Runs

![](/legacyfs/online/storage/blog_attachments/2022/11/Compare-Supply-Assignment-Runs.png)

Compare Supply Assignment Runs

Proportional assignment provides great value to business by improving customer satisfaction and fulfill requirements in a fair share manner with the available supply. Demand Grouping rule provides more flexibility to group the demand for proportional distribution.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fproportional-assignment-in-supply-assignment-run-arun%2Fba-p%2F13562347%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Adding custom condition types to calculation schema for purchasing info records in SAP Public Cloud](/t5/enterprise-resource-planning-q-a/adding-custom-condition-types-to-calculation-schema-for-purchasing-info/qaq-p/14232451)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday
* [Japan Bank Charges in Payment Lots](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-lots/ba-p/14231915)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [Japan Bank Charges in Payment Run](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-run/ba-p/14231441)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [Issues configuring input document types in SAP S/4HANA 2023 GRDC](/t5/enterprise-resource-planning-q-a/issues-configuring-input-document-types-in-sap-s-4hana-2023-grdc/qaq-p/14231361)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Tuesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/2233182) | 8 |
| [![DianaMala](https://avatars.profile.sap.com/6/d/id6db8ca00c3368971fe9ea45165f8ca02b42d3fc0d2b18891c590b300d9206a82_small.jpeg "DianaMala")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") DianaMala](/t5/user/viewprofilepage/user-id/1565064) | 8 |
| [![Andrew_Ford](https://avatars.profile.sap.com/4/2/id42fc9a5c18fc3229159993bbd8c3abd793e64af5050b65e9a4b850c04ce6bbb7_small.jpeg "Andrew_Ford")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") Andrew\_Ford](/t5/user/viewprofilepag...
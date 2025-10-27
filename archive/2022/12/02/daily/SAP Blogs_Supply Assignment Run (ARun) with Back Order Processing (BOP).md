---
title: Supply Assignment Run (ARun) with Back Order Processing (BOP)
url: https://blogs.sap.com/2022/12/01/supply-assignment-run-arun-with-back-order-processing-bop/
source: SAP Blogs
date: 2022-12-02
fetch_date: 2025-10-04T00:17:11.660347
---

# Supply Assignment Run (ARun) with Back Order Processing (BOP)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Supply Assignment Run (ARun) with Back Order Proce...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52133&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Supply Assignment Run (ARun) with Back Order Processing (BOP)](/t5/enterprise-resource-planning-blog-posts-by-sap/supply-assignment-run-arun-with-back-order-processing-bop/ba-p/13562370)

![rameshraja_r](https://avatars.profile.sap.com/9/2/id926f49500d9a6885bfa0041021daf44eb0df6fdc5cf5a0bb4fca2481385c3ab3_small.jpeg "rameshraja_r")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[rameshraja\_r](https://community.sap.com/t5/user/viewprofilepage/user-id/213652)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52133)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52133)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562370)

‎2022 Dec 01
10:55 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52133/tab/all-users "Click here to see who gave kudos to this post.")

3,618

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

For Overview of Supply Assignment (ARun), refer [blog](https://blogs.sap.com/2022/10/10/supply-assignment-arun-in-sap-s-4-hana/).

This blog explains how to execute Supply Assignment through BOP Variant. For more details on Back Order Processing (BOP), refer [documentation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/73a1a457ef816b10e10000000a441470.html).

**Pre-requisites:**

1. Check the Pre-requisites mentioned [here](https://blogs.sap.com/2022/10/10/supply-assignment-arun-in-sap-s-4-hana/).

2. User must have roles SAP\_BR\_ORDER\_FULFILLMNT\_MNGR and SAP\_BR\_ORDER\_FULFILLMNT\_MNGR\_R

**Scenario:**

In a Make to Stock business, where there is a huge demand for a product, below are some of the key business requirements where supply assignment helps to achieve them:

* Customers' Orders need to be prioritized based on the business requirements

* Once product availability is committed to customers, the committed dates and units must be preserved

* Allocate on hand inventory based on certain priorities (such as manufacturing date, shelf life, storage location, etc.)

* Allocate future receipts (Purchase Orders, Inbound Deliveries, Production Orders) to demand and reserve the supply for deliveries

* Ensure minimum % of the ordered quantity is met so that customer is satisfied, and also multiple shipments can be avoided

In this example, let us take 4 Customer Orders which has 100 units each. There are 3 batches in the system with 100 units each.

**Configuration/Setup:**

Below are the configuration/setup required to carry out supply assignment.

* **Supply Assignment Rule:**

From S/4 HANA 2020, it is mandatory to configure Supply Assignment Rule, and this will be maintained in BOP Variant.

Go to Fiori App, ‘Configure Supply Assignment Rule’ and create a new rule.

![](/legacyfs/online/storage/blog_attachments/2022/11/Configure-Supply-Assignment-Rule.png)

Configure Supply Assignment Rule

**Note:** In this example, we enter a supply sort rule which sorts the supply based on the shelf-life expiry date.

![](/legacyfs/online/storage/blog_attachments/2022/11/Configure-Supply-Sort-Rule.png)

Configure Supply Sort Rule

* **BOP Segment:**

Go to Fiori app, Configure BOP Segment.

Create a new BOP Segment and maintain the desired selection and sorting criteria for requirements. (In this example, we use delivery priority and requested delivery date).

![](/legacyfs/online/storage/blog_attachments/2022/11/Configure-BOP-Segment.png)

Configure BOP Segment

* **BOP Variant:**

Go to Fiori app, Configure BOP Variant.

Create a new BOP Variant. Select Execution Method as ‘Supply Assignment’. Enter the Supply Assignment Rule.

![](/legacyfs/online/storage/blog_attachments/2022/11/Configure-BOP-Variant.png)

Configure BOP Variant

**Execute Supply Assignmen**t

Click on ‘Run’ in BOP Variant. You can also use ‘Schedule BOP Variant’ Fiori app to schedule the execution of BOP Variant.

![](/legacyfs/online/storage/blog_attachments/2022/11/Execute-BOP-Variant.png)

Execute BOP Variant

![](/legacyfs/online/storage/blog_attachments/2022/11/Schedule-BOP-Run.png)

Schedule BOP Run

**Analyze Results**

The Results of Supply Assignment can be seen in multiple places such as Insight to Action (ARUNITA), Monitor Supply Assignment Runs, Monitor Supply Assignment Demand, Supply Demand Overview (Flexible Analysis), etc.

For instance, go to Fiori app, Monitor Supply Assignment Runs. Here you can see the details of the requirements and assignments.

![](/legacyfs/online/storage/blog_attachments/2022/11/Monitor-Supply-Assignment-Runs.png)

Monitor Supply Assignment Runs

![](/legacyfs/online/storage/blog_attachments/2022/11/Monitor-Supply-Assignment-Runs-Details.png)

Monitor Supply Assignment Runs (Details)

In this example, Supply Assignment was executed in sequential mode. It is also possible to execute a proportional supply distribution in Supply Assignment which will be covered in next blog.

Please share your comments/questions/thoughts on this, if you find this is a valid fit for your requirement.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

8 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsupply-assignment-run-arun-with-back-order-processing-bop%2Fba-p%2F13562370%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Japan Bank Charges in Payment Lots](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-lots/ba-p/14231915)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  W...
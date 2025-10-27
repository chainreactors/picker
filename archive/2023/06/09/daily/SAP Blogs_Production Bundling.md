---
title: Production Bundling
url: https://blogs.sap.com/2023/06/08/production-bundling/
source: SAP Blogs
date: 2023-06-09
fetch_date: 2025-10-04T11:46:58.550771
---

# Production Bundling

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Production Bundling

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67455&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Production Bundling](/t5/enterprise-resource-planning-blog-posts-by-members/production-bundling/ba-p/13555830)

![faisal_aslam12478](https://avatars.profile.sap.com/2/5/id256f07037a2e3a4963aba48ad71ecb6111b9605c9e426c58d4646eed5c8edd30_small.jpeg "faisal_aslam12478")

[faisal\_aslam12478](https://community.sap.com/t5/user/viewprofilepage/user-id/826267)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67455)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67455)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555830)

‎2023 Jun 08
10:22 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67455/tab/all-users "Click here to see who gave kudos to this post.")

1,672

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)

View products (1)

**Introduction:**

Some manufacturing process involves manufacturing products in steps spread over several days. Standard SAP creates the Supply to Production tasks for all the products in one go which is not viable as the raw materials need to be added to the production floor over a period of time. To gain efficiencies, would like to be able to confirm the goods movement split based on Marks set up on a production order and tasks should be generated on a daily or periodic basis. Input Products that with different Storage Conditions will also be split off as their own Bundles.

**Objective:**

The objective of this Blog is to provide a mechanism to split and create multiple goods movement bundles for the raw materials consumed for each Mark, Storage Condition and Location on the Production order. A MORO should be in ice to generate these bundles on a daily/periodic basis. Each good movement will be treated as a production bundle and can be moved multiple times within the site before it is brought to the production floor. All these moves need to be treated as a production bundle move and not as separate input products.

**Audience**

Consultants/Business Users/Beginners

**P****rocess Flow and Views:**

Navigate Production Control WorkCentre>>Go to Production Control>>Select New >>Enter Product ID>> Enter Site ID>>Set Quantity for that product>>Release Production Order

![](/legacyfs/online/storage/blog_attachments/2023/06/2023-05-29-22_50_37-Settings.png)

Navigate Production Bundling Work Center>>Select Goods Movement WoC>>Fill all fields on Wizard>>Click on Finish and Close>> You will get Production Bundles against Production Order In Preparation Status

![](/legacyfs/online/storage/blog_attachments/2023/06/Pic-2.png)

Now click on bundle button to create a bundle >>select the logistics area to (where you want to put the bundle).

![](/legacyfs/online/storage/blog_attachments/2023/06/Pic-3.png)

If you want to Move any Bundle to from one logistic area to another logistic area, then click on Move button>>Select Logistic area to>>Check Stock overview to check that bundle moved to desire logistic area or not

![](/legacyfs/online/storage/blog_attachments/2023/06/Pic-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Pic-5.png)

Click on Confirm button to Confirm the Bundle ID>> After Confirm a Bundle ID you will see that Production Order task status changes to Started and Production order status also changed

![](/legacyfs/online/storage/blog_attachments/2023/06/Pic-6.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Pic-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Pic-8.png)

I have tried to explain the process flow of Production Bundling. It may be helpful for those who want to understand the basic and advanced learning in SAP Business ByDesign.

Looking forward to hearing your ideas and comments.

* [analytics](/t5/tag/analytics/tg-p/board-id/erp-blog-members)
* [business process expert](/t5/tag/business%20process%20expert/tg-p/board-id/erp-blog-members)
* [Business Trends](/t5/tag/Business%20Trends/tg-p/board-id/erp-blog-members)
* [SAP](/t5/tag/SAP/tg-p/board-id/erp-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fproduction-bundling%2Fba-p%2F13555830%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Int4 Suite Agents Empowers Functional Consultants To Test Integrated SAP S/4HANA Business Processes](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-agents-empowers-functional-consultants-to-test-integrated-sap-s/ba-p/14234100)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  yesterday
* [Production Order Variances](/t5/enterprise-resource-planning-q-a/production-order-variances/qaq-p/14234140)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [MD01N Behavior: Issuing Storage Location Not Set in Stock Transport Requisitions](/t5/enterprise-resource-planning-q-a/md01n-behavior-issuing-storage-location-not-set-in-stock-transport/qaq-p/14234045)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [Need to activate enhancement implementation that depends on a switch](/t5/enterprise-resource-planning-q-a/need-to-activate-enhancement-implementation-that-depends-on-a-switch/qaq-p/14233496)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Thursday
* [Agentic AI Testing for Greenfield S/4HANA Outbound Interfaces - Part 1](/t5/enterprise-resource-planning-blog-posts-by-members/agentic-ai-testing-for-greenfield-s-4hana-outbound-interfaces-part-1/ba-p/14232427)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Wednesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.s...
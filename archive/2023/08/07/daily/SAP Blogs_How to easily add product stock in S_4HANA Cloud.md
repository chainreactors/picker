---
title: How to easily add product stock in S/4HANA Cloud
url: https://blogs.sap.com/2023/08/06/how-to-easily-add-product-stock-in-s-4hana-cloud/
source: SAP Blogs
date: 2023-08-07
fetch_date: 2025-10-04T11:59:26.990814
---

# How to easily add product stock in S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to easily add product stock in S/4HANA Cloud

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/54067&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to easily add product stock in S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-easily-add-product-stock-in-s-4hana-cloud/ba-p/13575449)

![varunvenkat](https://avatars.profile.sap.com/6/d/id6d9836d543f88d438477c8e54903aa6ba4a079c87ec08d808dc512a637a4c55f_small.jpeg "varunvenkat")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[varunvenkat](https://community.sap.com/t5/user/viewprofilepage/user-id/83606)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=54067)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/54067)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13575449)

‎2023 Aug 06
11:06 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/54067/tab/all-users "Click here to see who gave kudos to this post.")

7,758

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Supply Chain](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Supply%2520Chain/pd-p/253c6759-2b52-46f4-be45-e2ab78f2f420)
* [SAP S/4HANA Cloud Public Edition Master Data](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Master%2520Data/pd-p/771f6577-e8ec-415f-99a7-6b73add46c47)
* [MM Inventory Management](https://community.sap.com/t5/c-khhcw49343/MM%2520Inventory%2520Management/pd-p/402489426158095572469338199787586)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [MM Inventory Management

  Software Product Function](/t5/c-khhcw49343/MM%2BInventory%2BManagement/pd-p/402489426158095572469338199787586)
* [SAP S/4HANA Cloud Public Edition Supply Chain

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSupply%2BChain/pd-p/253c6759-2b52-46f4-be45-e2ab78f2f420)
* [SAP S/4HANA Cloud Public Edition Master Data

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BMaster%2BData/pd-p/771f6577-e8ec-415f-99a7-6b73add46c47)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (4)

In this short blog post, I would like to demonstrate the different ways in inventory managed storage locations that one can initialize product stock in S/4HANA Cloud. The methods shown here are just for demo purposes, to create stock that you can use for testing purposes. In productive systems, changes to stock will usually only take place with the help of production orders or purchase orders.

In S/4HANA Cloud, there are 3 different methods available to add stock for a particular product. Make sure you have the necessary business roles required to access these apps. Let’s look at SRV\_05 (Stock Service Part) as an example material for which we want to add stock:

**Method 1**: “Manage Stock”

The simplest way to initialize stock in a particular storage location is by using the “Manage Stock” app. Simply enter the product SRV\_05 in the search field and then click the up arrow icon to increase stock to the desired storage location.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture1-6.png)

In the subsequent popup, simply enter the desired quantity of stock to be added and click ‘Post’.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture2-7.png)

**Method 2**: “Post Goods Receipt without reference”

This second way of initializing stock is also quite straightforward. Simply open the “Post Goods Receipt without reference” app. There you can enter the product, quantity, plant and storage location in which the stock should be initialized and click ‘Post’.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture3-5.png)

**Method 3**: “Post Goods Movement” (MIGO transaction)

* Open the “Post Goods Movement” app and choose the Goods Receipt – Other option.

* Under the Material tab, specify the material for which the stock should be increased.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture4-6.png)

* Under the Quantity tab, select the desired quantity and under the Where tab, specify which plant and storage location the stock should be added.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture5-5.png)

* Finally, click Post and the selected quantity of the product SRV\_05 will be added to the storage location 101A in this case.

After reading this blog, you should have gotten a quick overview of the different ways to quickly add stock for a product to a particular storage location. With all three of the methods shown above, you can view the end result of executing the above transactions in the apps “Manage Stock” or “Display Stock Overview”.

Labels

* [Life at SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/life%20at%20sap)

* [Cloud](/t5/tag/Cloud/tg-p/board-id/erp-blog-sap)
* [S4HANA](/t5/tag/S4HANA/tg-p/board-id/erp-blog-sap)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fhow-to-easily-add-product-stock-in-s-4hana-cloud%2Fba-p%2F13575449%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Enhancing Manufacturing Excellence: What's New in SAP S/4HANA Cloud 2508.1](/t5/enterprise-resource-planning-blog-posts-by-sap/enhancing-manufacturing-excellence-what-s-new-in-sap-s-4hana-cloud-2508-1/ba-p/14222217)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Integrating SAP IBP with SAP S/4HANA Private Cloud for Demand Planning Using CI-DS](/t5/enterprise-resource-planning-blog-posts-by-sap/integrating-sap-ibp-with-sap-s-4hana-private-cloud-for-demand-planning/ba-p/14219426)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [SAP Fiori development newsletter September2025 (issue #36)](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-fiori-development-newsletter-september2025-issue-36/ba-p/14212556)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [Error message: FINOC165 and FINOC297 - Manage Cost Centers ...
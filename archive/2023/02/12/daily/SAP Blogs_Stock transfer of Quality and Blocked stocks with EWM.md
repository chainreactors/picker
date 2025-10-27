---
title: Stock transfer of Quality and Blocked stocks with EWM
url: https://blogs.sap.com/2023/02/11/stock-transfer-of-quality-and-blocked-stocks-with-ewm/
source: SAP Blogs
date: 2023-02-12
fetch_date: 2025-10-04T06:25:57.691860
---

# Stock transfer of Quality and Blocked stocks with EWM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Stock transfer of Quality and Blocked stocks with ...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4922&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Stock transfer of Quality and Blocked stocks with EWM](/t5/supply-chain-management-blog-posts-by-members/stock-transfer-of-quality-and-blocked-stocks-with-ewm/ba-p/13567984)

![narsimha_namburi](https://avatars.profile.sap.com/9/d/id9d5557d6c55837dfd912b0099ec21a90b449299047adb5988fdedbd1346f46e1_small.jpeg "narsimha_namburi")

[narsimha\_namburi](https://community.sap.com/t5/user/viewprofilepage/user-id/559130)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4922)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4922)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567984)

‎2023 Feb 11
5:49 AM

[9
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4922/tab/all-users "Click here to see who gave kudos to this post.")

21,588

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)

View products (3)

In some cases, it is necessary to transfer the stock from one plant to another even though stock is not cleared by quality **(*quality stock*)** or even if the stock is rejected by quality **(*blocked stock*).**

Best example for this kind of requirement is, if a manufacturing plant has limited warehouse space, business may decide to move the stock to a distribution center and store the inventory in DC with quality or blocked or unrestricted use.

While this is not a new functionality of EWM, Intention of the blog is to explain the process of stock transfer of quality and blocked stocks from one plant to another.

To work with this kind of process, it is must to enable the source stock type for STO.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture6-11.png)

This will enable the field source stock type in delivery tab of the STO.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture7-9.png)

**Quality stock transfer:** During creation of STO, if we decide to transfer the quality stock, we should choose source stock type manually.

When delivery is created, stock type will be carried to delivery document in ERP and same will be distributed to EWM.

ERP Delivery:

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture8-8.png)

EWM Document:

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture9-5.png)

Inventory position before creating the pick list.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture10-4.png)

Warehouse task for the delivery:

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture11-6.png)

After Goods Issue:

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture12-6.png)

Upon GI, SPED output triggers to generate Inbound delivery in receiving plant.

Stock type is quality inspection as per inspection set up of material master.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture13-6.png)

Inbound delivery in EWM

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture14-5.png)

After the goods receipt, stock will be posted in quality inspection in receiving plant.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture15-6.png)

Even though only quality stock to quality stock transfer executed in this test case, it is possible to transfer quality stock to unrestricted or quality stock to blocked stock.

**Block stock transfer:** Just like quality stock, we can also transfer blocked stock from source plant to destination.

In this example, blocked stock transferred from source plant and received as unrestricted stock in destination plant.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture16-4.png)

Delivery created in ERP with block stock.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture17-5.png)

Same distributed to EWM and creates a document with block stock as source stock.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture18-3.png)

After completing the picking and goods issue, inbound delivery generated in receiving plant with unrestricted use.

ERP Delivery:

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture19-3.png)

EWM Delivery:

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture20-5.png)

Upon goods receipt, stock will be posted in unrestricted use.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture21-3.png)

This is out of the box configuration and no development involved.

PS: This is my personal observation based on requirements that I worked, and this blog is based on S4 HANA 2022 version sandbox. Functionality available in older versions also.

Thank you for reading the post, please share thoughts and feedback.

Follw <https://community.sap.com/topics/extended-warehouse-management> for more content.

Follow Narsimha Namburi for more updates.

References

<https://help.sap.com>

12 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-members%2Fstock-transfer-of-quality-and-blocked-stocks-with-ewm%2Fba-p%2F13567984%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Material & Quality Management in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/material-amp-quality-management-in-sap-s-4hana/ba-p/14234018)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  15 hours ago
* [Variant Configuration (LO-VC) in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/variant-configuration-lo-vc-in-sap-s-4hana/ba-p/14234012)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  15 hours ago
* [Master Data and Core Logistics Processes in SAP S/4HANA](/t5/supply-chain-management-blog-...
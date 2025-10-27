---
title: SAP Business Network for Supply Chain 2303 Release – My top two features
url: https://blogs.sap.com/2023/03/29/sap-business-network-for-supply-chain-2303-release-my-top-two-features/
source: SAP Blogs
date: 2023-03-30
fetch_date: 2025-10-04T11:06:40.895293
---

# SAP Business Network for Supply Chain 2303 Release – My top two features

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)
* SAP Business Network for Supply Chain 2303 Release...

Spend Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-sap/article-id/1820&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Business Network for Supply Chain 2303 Release – My top two features](/t5/spend-management-blog-posts-by-sap/sap-business-network-for-supply-chain-2303-release-my-top-two-features/ba-p/13561242)

![damian_edelberg](https://avatars.profile.sap.com/2/f/id2f90378aebe5983cd9e68ec9300eef0e8ac6067874f61c358f56507f5aef5149_small.jpeg "damian_edelberg")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[damian\_edelberg](https://community.sap.com/t5/user/viewprofilepage/user-id/239573)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-sap&message.id=1820)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-sap/article-id/1820)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561242)

‎2023 Mar 29
11:49 PM

[4
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-sap/message-id/1820/tab/all-users "Click here to see who gave kudos to this post.")

489

* SAP Managed Tags
* [SAP Business Network Supply Chain Collaboration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520Supply%2520Chain%2520Collaboration/pd-p/1cf9720a-eb8a-4dde-8031-c97087082c4e)
* [SAP Business Network for Procurement and SAP Business Network for Supply Chain](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520for%2520Procurement%2520and%2520SAP%2520Business%2520Network%2520for%2520Supply%2520Chain/pd-p/67838200100800005701)

* [SAP Business Network for Procurement and SAP Business Network for Supply Chain

  SAP Business Network for Procurement and SAP Business Network for Supply Chain](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2Bfor%2BProcurement%2Band%2BSAP%2BBusiness%2BNetwork%2Bfor%2BSupply%2BChain/pd-p/67838200100800005701)
* [SAP Business Network Supply Chain Collaboration

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2BSupply%2BChain%2BCollaboration/pd-p/1cf9720a-eb8a-4dde-8031-c97087082c4e)

View products (2)

Welcome to the first in a series of blog posts where I will focus on SAP Business Network for Supply Chain and the new features delivered with every major release.

While you can get a full overview of the 2303 release items for SAP Business Network for Supply Chain under the following [link](https://help.sap.com/docs/ariba/978b7e36451a4c2c85321a3ef6f3a7e5/7ede8ccbfae74e6f9321bc83f55b3e7f.html), I wanted to focus on two of them that I consider pretty cool and great additions to the solution.

* **Automated Transfer of New Handling-Unit Packaging Instructions.**

This feature enables customers to handle automated replication of packaging instructions from their SAP S/4HANA backend system to SAP Business Network for the initial load of the entire set of available packaging instructions and the update of existing ones.

Packaging and handling unit processes are quite diverse based on industry and customer requirements.  What we have seen with our customers is that the number of available packaging specifications can be quite big, encompassing hundreds or thousands of versions. And market dynamics indicate that several, or at least one of these packaging instructions will be updated frequently.

**Why does this matter?** This feature delivers more integration and automation between SAP S/4HANA and SAP Business Network in an area that is critical. Packaging is one of those functions where there is no time to add further manual processes.

* **Prevent Advanced Shipping Notification creation when an open quality notification for** **material without a purchase order reference exists**

Prior to this feature we are introducing, SAP Business Network Supply Chain Collaboration using the Quality Collaboration Add-On were able block their suppliers from creating ship notices for materials with an open quality notification **but at the purchase-order level**. This means, for example, if a material in question is in 20 purchase orders, the buyer had to create 20 quality notifications to block the shipment of the material.

This great thing about this feature is that blocking happens at the **material level**.  See below the new error message that the supplier will get when attempting to create a Shipping Notification for a material with an open quality notification.

**![](/legacyfs/online/storage/blog_attachments/2023/03/Error-Message.png)**

**Why does this matter?** This feature brings more transparency around quality collaboration. Suppliers will no longer be able to send shipping notifications that contain a faulty material, unless the purchase order contains an accepted quality inspection.
Furthermore, more efficiency on the buy-side will be realized, since now there is a way to reduce the number of incoming Shipping Notifications for materials that do not meet quality requirements.

To learn more about SAP Business Network for Supply Chain visit  [SAP Business Network Supply Chain Collaboration](https://www.sap.com/products/business-network/supply-chain-collaboration.html)

For further questions and feedback related to the blog, please feel free to post your questions with the tag SAP Business Network for Supply Chain.

Labels

* [Product Updates](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fspend-management-blog-posts-by-sap%2Fsap-business-network-for-supply-chain-2303-release-my-top-two-features%2Fba-p%2F13561242%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [New video tutorials to help our Suppliers master the network catalog](/t5/spend-management-blog-posts-by-sap/new-video-tutorials-to-help-our-suppliers-master-the-network-catalog/ba-p/14233312)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)  Thursday
* [What’s New in SAP Ariba Central Procurement – SAP S/4HANA Cloud Public Edition 2508](/t5/spend-management-blog-posts-by-sap/what-s-new-in-sap-ariba-central-procurement-sap-s-4hana-cloud-public/ba-p/14226583)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)  Monday
* [What’s New in Purchase Requisitions - SAP S/4HANA Cloud Public Edition 2508](/t5/spend-management-blog-posts-by-sap/what-s-new-in-purchase-requisitions-sap-s-4hana-cloud-public-edition-2508/ba-p/14226600)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spe...
---
title: How to split WIP into separate accounts for Material and Overhead Costs
url: https://blogs.sap.com/2023/03/09/how-to-split-wip-into-separate-accounts-for-material-and-overhead-costs-2/
source: SAP Blogs
date: 2023-03-10
fetch_date: 2025-10-04T09:08:12.568555
---

# How to split WIP into separate accounts for Material and Overhead Costs

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to split WIP into separate accounts for Materi...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52578&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to split WIP into separate accounts for Material and Overhead Costs](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-split-wip-into-separate-accounts-for-material-and-overhead-costs/ba-p/13564340)

![Svetlana73](https://avatars.profile.sap.com/6/8/id68b222621d8c623da198a19b8b08e7609ede99862780805f327f65f5307f7e7d_small.jpeg "Svetlana73")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Svetlana73](https://community.sap.com/t5/user/viewprofilepage/user-id/125881)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52578)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52578)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564340)

‎2023 Mar 09
9:48 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52578/tab/all-users "Click here to see who gave kudos to this post.")

2,069

* SAP Managed Tags
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN Controlling](https://community.sap.com/t5/c-khhcw49343/FIN%2520Controlling/pd-p/165905235116577077914579113243106)
* [FIN Cost Object Controlling](https://community.sap.com/t5/c-khhcw49343/FIN%2520Cost%2520Object%2520Controlling/pd-p/251991085556036308395324851400611)

* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN Controlling

  Software Product Function](/t5/c-khhcw49343/FIN%2BControlling/pd-p/165905235116577077914579113243106)
* [FIN Cost Object Controlling

  Software Product Function](/t5/c-khhcw49343/FIN%2BCost%2BObject%2BControlling/pd-p/251991085556036308395324851400611)

View products (3)

In this article, I would like to share a successful experience with a business challenge in the context of FI Reporting of how to split WIP ( Work in Progress)  to separate GL accounts for Material and Overhead costs during WIP settlement of Production Orders/Process Orders at Period Closing in S/4HANA.

### The business requirement:

Split the WIP to separate P&L and B/S accounts for Material and Overhead to comply with FI reporting needs.

* Material and Added Value costs and to be assigned to different line items in WIP posting during the Process Order/Production Order settlement:

* Each line item is settled in financial accounting using separate P&L and Balance sheet accounts

* Negative WIP is settled in financial accounting using another set of P&L and B/S accounts

### The technical solution:

To deliver the business need, a standard S/4HANA configuration can be used.

First, you need to create Result Analysis key and RA version: Do not forget to activate the box *Transfer to Financial Accounting**.*

![](/legacyfs/online/storage/blog_attachments/2020/10/RA-key-4.png)

Furthermore to Create Line IDs in order to assign to source cost elements:

* COP for Material Costs

* COS for the Overhead ( Added Value Costs)

![](/legacyfs/online/storage/blog_attachments/2020/10/Line-IDs.png)

The next step is to map mask cost elements for WIP and Result Analysis:

![](/legacyfs/online/storage/blog_attachments/2020/10/Mask.png)

What you need to do additionally is the configuration step *Update of WIP calculations and Result Analysis where you* assign the cost elements to be used in the target structure:

![](/legacyfs/online/storage/blog_attachments/2020/10/CEs.png)

Finally, you define Posting Rules for WIP where the split is configured for P&L and BS accounts:

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-11.png)

As a result, when you run WIP calculation for Production / Process orders at Period Closing via transaction KKAO and then during Production / Process order settlement, the system will post WIP to separate GL accounts for Material and Overhead costs.

Here is an example of an FI document posted during the  settlement via CO88 in Universal Journal in S/4HANA:

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-9.png)

**Business Benefits:**

This config enables WIP to be split into separate accounts for Material and Overhead costs for better analysis of the production costs recognized as WIP and reporting different production costs for different lines in the BS and P&L.

**Conclusion :**

Using this feature customers can maintain a different GL account for different production costs recognized as WIP at Period End Closing,

Please, feel free to share your thoughts and if you have any queries by writing in the comments section below.

Please, follow the FIN Cost Object Controlling, post and answer questions <https://answers.sap.com/tags/251991085556036308395324851400611>,

and read other posts on the topic

<https://blogs.sap.com/tags/251991085556036308395324851400611>

Stay with me and follow my profile for similar FI topics.

FollowLikeRSS Feed

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fhow-to-split-wip-into-separate-accounts-for-material-and-overhead-costs%2Fba-p%2F13564340%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Account Assignment Q (Project Stock) - possible for Services and for Orders without Material Number?](/t5/enterprise-resource-planning-q-a/account-assignment-q-project-stock-possible-for-services-and-for-orders/qaq-p/14227735)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [Lean Service Procurement for Project Network in SAP S/4 Hana](/t5/enterprise-resource-planning-blog-posts-by-members/lean-service-procurement-for-project-network-in-sap-s-4-hana/ba-p/14217832)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  3 weeks ago
* [Professional Services in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/professional-services-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14202789)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 01
* [Data Migration - Bulgaria EUR Transition for S/4HANA Cloud Public Cloud Live Customers](/t5/enterprise-resource-planning-blog-posts-by-sap/data-migration-bulgaria-eur-transit...
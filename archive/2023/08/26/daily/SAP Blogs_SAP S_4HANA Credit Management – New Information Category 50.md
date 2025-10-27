---
title: SAP S/4HANA Credit Management – New Information Category 50
url: https://blogs.sap.com/2023/08/25/sap-s-4hana-credit-management-new-information-category-50/
source: SAP Blogs
date: 2023-08-26
fetch_date: 2025-10-04T12:00:00.890566
---

# SAP S/4HANA Credit Management – New Information Category 50

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Credit Management - New Information Ca...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/55134&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Credit Management - New Information Category 50](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-credit-management-new-information-category-50/ba-p/13581519)

![meow](https://avatars.profile.sap.com/1/3/id132d83c1b83450b4352728a8a8c36a69844e1335bb7bb6732061a17749eb43a2_small.jpeg "meow")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[meow](https://community.sap.com/t5/user/viewprofilepage/user-id/150918)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=55134)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/55134)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13581519)

‎2023 Aug 25
9:21 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/55134/tab/all-users "Click here to see who gave kudos to this post.")

6,354

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

This blog covers necessary configuration and the behavior of one of new functions in Credit Management in SAP S/4HANA 2021. It is about a new information category 50 (Additional Adjustment) and Information Type 01 (High Season) in BP master data.

With this function, you can top up credit limit in certain period of time (e.g. holiday season), so that you can take more orders than usual from the customer.

**1. Customizing**
Both customizing and changes to master data are required.

* BP master data
  Information Category 50 (Additional Adjustment)
  Information Type 01 (High Season)

* Customizing (IMG)
  Flag "Include Additional Adjustments"

Let's have a look at the customizing first.

IMG: Financial Supply Chain Management > Credit Management > Credit Risk Monitoring > Credit Limit Check > Define Checking Rules
![](/legacyfs/online/storage/blog_attachments/2023/08/CM14.png)Here, you find a flag "Include Additional Adjustments" under Check Rule -> Checks.
It is available since SAP S/4HANA 2021.
Tick this flag.
![](/legacyfs/online/storage/blog_attachments/2023/08/CM1.png)

 **2. Master Data**
On BP master (Role UKM0000), you need to do the two things.

* In [ General Data - Credit Profile ] tab, set the Check Rule where the flag in the previous section is ON.

* Either in [ General Data - Credit profile ] tab or [ Credit Segment Data - Credit Limit and Control ] tab, make an entry under "Futher Information".

You need to select Information Category 50 (Additional Adjustment) and insert an entry with Information Type 01 (High Season).
Information Type 01 is displayed as 1 on the screen.

Then enter amount with currency and period.

Do not forget to tick the flag "Relevance for Credit Check". It activates the function to increase the credit limit during specific time period.

"Further Information" section is in [ General Data - Credit Profile ] tab, too, but you don't need to maintain both tabs.![](/legacyfs/online/storage/blog_attachments/2023/08/CM2.png)![](/legacyfs/online/storage/blog_attachments/2023/08/CM9.png)

You are done with the configuration now.

**3. Test the behavior**
You can switch the system behavior with flag "Relevance" in BP master without changing customizing.

As prerequisite, the sales order is created on August 23rd.

When the flag is OFF, a popup comes up and tells you that credit limit is exceeded for this customer.
![](/legacyfs/online/storage/blog_attachments/2023/08/CM12.png)![](/legacyfs/online/storage/blog_attachments/2023/08/CM6.png)

Now, change the flag ON and test again.
You do not get a popup and find that the order can be taken because the limit is temporarily increased because of high season.![](/legacyfs/online/storage/blog_attachments/2023/08/CM13.png)

A sales order was saved without popup.![](/legacyfs/online/storage/blog_attachments/2023/08/CM8.png)

**[ Additional Information ]**
Transaction UKM\_ADDINFOS\_DISPLAY to display "Further Inforation" in BP master is now found in SAP Menu as of SAP S/4HANA 2020.![](/legacyfs/online/storage/blog_attachments/2023/08/CM10.png)![](/legacyfs/online/storage/blog_attachments/2023/08/CM11.png)

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [Credit management](/t5/tag/Credit%20management/tg-p/board-id/erp-blog-sap)
* [Credit Management S4HANA Credit Management](/t5/tag/Credit%20Management%20S4HANA%20Credit%20Management/tg-p/board-id/erp-blog-sap)
* [fscm credit management](/t5/tag/fscm%20credit%20management/tg-p/board-id/erp-blog-sap)

8 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsap-s-4hana-credit-management-new-information-category-50%2Fba-p%2F13581519%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [SAP Enterprise Support Academy Newsletter October 2025](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-enterprise-support-academy-newsletter-october-2025/ba-p/14232476)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [VIM Foundation & Invoice Solution Configuration Overview](/t5/enterprise-resource-planning-blog-posts-by-sap/vim-foundation-amp-invoice-solution-configuration-overview/ba-p/14229743)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Sunday
* [HIDE FIELDS IN ADVANCED RETURNS MANAGEMENT SD](/t5/enterprise-resource-planning-q-a/hide-fields-in-advanced-returns-management-sd/qaq-p/14227088)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-que...
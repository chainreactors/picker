---
title: Universal Parallel Accounting in SAP S/4HANA
url: https://blogs.sap.com/2022/10/21/universal-parallel-accounting-in-sap-s-4hana/
source: SAP Blogs
date: 2022-10-22
fetch_date: 2025-10-03T20:35:40.126373
---

# Universal Parallel Accounting in SAP S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Universal Parallel Accounting in SAP S/4HANA

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50572&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Universal Parallel Accounting in SAP S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-sap/universal-parallel-accounting-in-sap-s-4hana/ba-p/13551060)

![Sarah_Roessler](https://avatars.profile.sap.com/0/2/id0254ce6e7e6ec5b4c0410cc8c23c4adcd820178604aa5960e1953a8e1c73f142_small.jpeg "Sarah_Roessler")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Sarah\_Roessler](https://community.sap.com/t5/user/viewprofilepage/user-id/44369)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50572)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50572)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551060)

‎2022 Oct 21
7:27 PM

[61
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50572/tab/all-users "Click here to see who gave kudos to this post.")

61,121

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)

* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)

View products (2)

This blog introduces the topic of Universal Parallel Accounting which was delivered in SAP S/4HANA Cloud, public edition 2105 and will be delivered to SAP S/4HANA 2022 and SAP S/4HANA Cloud, private edition customers in October 2022 (for a general product update on SAP S/4HANA 2022, please refer to this [blog](https://blogs.sap.com/2022/10/21/sap-s-4hana-cloud-private-edition-and-sap-s-4hana-for-finance-2022-product-update/) by ulrich.hauke).

I will outline the motivation for the delivery, the use cases addressed by Universal Parallel Accounting and discuss how you can judge the impact on your SAP S/4HANA implementation.

**Motivation**

Parallel Accounting has been supported by SAP for some time, initially using parallel accounts and later using parallel ledgers. It allowed customers to fulfill their reporting requirements according to different GAAPs. In addition, SAP provided the option to add parallel “management” valuations represented by additional currency types to distinguish a legal valuation from a group valuation. However, these solutions had some shortcomings since currencies and ledgers were not consistently supported across the different subledgers (specifically Material Ledger, Controlling and Asset Accounting). This led to additional period-end closing activities to adjust the local GAAP values, complex configuration, and cumbersome filtering of values in reporting, since the additional currency types were part of the leading ledger.

Universal Parallel Accounting provides a **harmonized** architecture for ledgers and currencies. This provides a foundation for not only calculating and posting values per ledger and currency along end-to-end processes, but also the baseline for future innovations in the area of Finance such as [Value Chain Analysis](https://www.youtube.com/watch?v=FhkXmycLliw) and Transactional Carbon Accounting.

**Use Cases**

Let’s take a closer look at the use cases currently covered by Universal Parallel Accounting.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture1-68.png)

Figure 1: Use Cases addressed by Universal Parallel Accounting

Support of **parallel legal valuations** means consistent calculation and posting of values for legal ledgers, e.g. Group GAAP and Local GAAP. This worked already before Universal Parallel Accounting in some processes, e.g. depreciation or Universal Allocation, but not in many of the Management Accounting processes. During distribution, assessment and settlement, the values in the leading ledger values were posted in all ledgers, meaning that the sender values were not cleared properly in the second GAAP. This “shortcut” led to issues in processes like asset capitalization according to different GAAPs or when companies require to perform actual costing according to parallel GAAPs. This is solved now with Universal Parallel Accounting where we support settlement per ledger and – optionally – ledger-specific settlement rules, as shown in Figure 1. For a more detailed description of the changes in the area of Overhead Accounting, please refer to the blog focusing on [Overhead Accounting in the context of Universal Parallel Accounting](https://blogs.sap.com/2022/10/24/overhead-accounting-with-universal-parallel-accounting-in-sap-s-4hana-2022/) by janetdorothy.salmon.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture2-49.png)

Figure 2: Ledger-specific settlement rules

Actual cost rate calculation and actual costing is done per ledger with Universal Parallel Accounting and thus allows to perform actual costing for only one ledger or even both ledgers in parallel. Figure 2 shows the selection screen for a costing run with the link to the ledger that will be updated when actual costing is complete. For more details on the impact of Universal Parallel Accounting in Inventory Accounting, please refer to the blog focusing on [Inventory Accounting in the context of Universal Parallel Accounting](https://blogs.sap.com/2022/10/24/inventory-accounting-and-universal-parallel-accounting-in-sap-s-4hana-2022/) by janetdorothy.salmon.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture3-32.png)

Figure 3: Actual Costing Run per ledger

When talking about legal requirements, there is often the requirement to support **alternative fiscal year variants** for company codes in countries like India, where the fiscal year starts in April and ends in March, whereas financial reporting might have to be done according to calendar year on group level. In the past, the support of alternative fiscal year variants was limited, especially in the area of asset accounting (see note [844029](https://launchpad.support.sap.com/#/notes/844029)), where the fiscal year has an impact on the required movement types, accounts and the posting itself . These restrictions were often the reason that customers created separate Controlling Areas or made subsequent adjustment postings. These restrictions have been resolved with Universal Parallel Accounting which now consistently supports alternative fiscal year variants as long as the period borders are the same in each fiscal year. For more details on the impact of Universal Parallel Accounting in Asset Accounting, please refer to the blog focusing on [Asset ...
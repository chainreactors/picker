---
title: CO Account Assignment and Attribution with S/4HANA
url: https://blogs.sap.com/2023/08/06/co-account-assignment-and-attribution-with-s-4hana/
source: SAP Blogs
date: 2023-08-07
fetch_date: 2025-10-04T11:59:32.929477
---

# CO Account Assignment and Attribution with S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* CO Account Assignment and Attribution with S/4HANA

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/54060&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [CO Account Assignment and Attribution with S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-sap/co-account-assignment-and-attribution-with-s-4hana/ba-p/13575394)

![stefan_walz](https://avatars.profile.sap.com/0/f/id0fc80ce5cae3c4a29f5ac311063b570155d6a72aa8883009a6e32f3407ec3846_small.jpeg "stefan_walz")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[stefan\_walz](https://community.sap.com/t5/user/viewprofilepage/user-id/550996)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=54060)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/54060)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13575394)

‎2023 Aug 06
9:59 PM

[25
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/54060/tab/all-users "Click here to see who gave kudos to this post.")

19,771

* SAP Managed Tags
* [SAP Profitability and Cost Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Profitability%2520and%2520Cost%2520Management/pd-p/01200314690800000353)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN Controlling](https://community.sap.com/t5/c-khhcw49343/FIN%2520Controlling/pd-p/165905235116577077914579113243106)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP Profitability and Cost Management

  SAP Profitability and Cost Management](/t5/c-khhcw49343/SAP%2BProfitability%2Band%2BCost%2BManagement/pd-p/01200314690800000353)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN Controlling

  Software Product Function](/t5/c-khhcw49343/FIN%2BControlling/pd-p/165905235116577077914579113243106)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (4)

*Co-authored by* [Birgit Oettinger](https://people.wdf.sap.corp/profiles/D023549) and [Stefan Walz](https://www.linkedin.com/in/stefan-walz-430222a3/)

Welcome to this blog, in which we will provide insights into the new options of multiple CO account assignments and market segment attribution – innovations made possible with the Universal Journal in S/4HANA. The blog explains for which business processes this functionality is supported, which new reporting insights are enabled and which rules for CO account assignment - still - apply. The examples shown are taken out of *SAP S/4HANA Cloud, public edition*, but the principles also apply for the on-premise solution.

With the Universal Journal, all accounting applications share a common database. All the individual applications are views of the Universal Journal. This not only makes data transfers between the applications and subsequent reconciliations obsolete, but also makes the attributes of one application available to all others. Examples:

+ the G/L ledger is also available in Controlling, revenue recognition and market segment reporting, this allows parallel valuations end-to-end.

+ the market segments of the margin analysis application are available in G/L and revenue recognition.

+ the CO account assignments are also available in G/L and revenue recognition.

Thus, the journal entries can be enriched with new information (done automatically by the system). This enables completely new insights and simplifies processes. The following example shows the different attributes updated in a customer project scenario:![](/legacyfs/online/storage/blog_attachments/2023/08/F1-Universal-Journal.png)
Figure 1: the universal journal

With every cost posting to the project (journal entry 1), work in process and realized revenue is recognized and posted (journal entry 2). All postings are account assigned to the WBS element – also the balance sheet journal entry item. The journal entries for cost and event-based revenue recognition (EBRR) postings automatically derive the market segment. Thus, market segment reporting is directly available without the need for settlement or any other additional process steps. The *account assignment type – here WBS element -* defines the real account assignment in the universal journal.

The detailed information stored in the universal journal (ACDOCA) is the basis for financial reporting. SAP HANA supports performant reporting for all applications by aggregating the individual journal entries. This enables an aggregated reporting for all attributes and a drill-down to the detailed information, the individual journal entry, for all amounts and KPIs.

This example shows how additional update of market segments enrich reporting:![](/legacyfs/online/storage/blog_attachments/2023/08/F2-productandservice-motivation.png)

Figure 2: Product and Service Margin report for a customer project

The user posts expenses and time confirmations, performs a partial billing, and enters manual accruals. Together with these business transactions the system automatically creates additional revenue recognition postings to ensure costs and revenues are matching.
All journal entries are account assigned to a project (determined by account assignment type PR). In addition to the project account assignment market segment attributes are updated.
Thus, not only project reporting is possible, but also market segment reporting for example for product sold, customers or sales order.

To provide correct and value adding data, the update of additional CO Objects and market segment fields needs to follow clear rules. These rules are predefined by SAP per business process and cannot be changed. The additional attributes are derived by the system and cannot be entered manually. Details will be described in the next sections.

The glossary shows which different types of CO account assignments are described in this blog.

### ![](/legacyfs/online/storage/blog_attachments/2023/08/glossary-1.png)

### I CO Object as Account Assignment for P&L Postings

With S/4HANA cost elements and G/L accounts were merged. Now the *general ledger account type* determines how the general ledger account can be used in financial accounting (FI-GL) and management accounting (CO). The cost element is determined by the G/L account type "Primary Costs or Revenue" or "Secondary Costs" These G/L accounts are relevant for management accounting (CO). **Postings to such G/L “cost element” accounts require a CO account assignment**. P&L G/L accounts of type Secondary Costs control the value flow within Controlling, as they define for which kind of cost allocation methods the different P&L accounts can be used.

In combina...
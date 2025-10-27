---
title: Which ledger scenarios are available as of SAP S/4HANA Cloud 2302?
url: https://blogs.sap.com/2023/01/31/which-ledger-scenarios-are-available-as-of-sap-s-4hana-cloud-2302/
source: SAP Blogs
date: 2023-02-01
fetch_date: 2025-10-04T05:20:10.153138
---

# Which ledger scenarios are available as of SAP S/4HANA Cloud 2302?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Which ledger scenarios are available as of SAP S/4...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51647&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Which ledger scenarios are available as of SAP S/4HANA Cloud 2302?](/t5/enterprise-resource-planning-blog-posts-by-sap/which-ledger-scenarios-are-available-as-of-sap-s-4hana-cloud-2302/ba-p/13558601)

![Verena_Stuetz](https://avatars.profile.sap.com/5/b/id5bebcdec980a854dc65ed0c817a695481a7cd890213b8f50f344408bd2c8a3de_small.jpeg "Verena_Stuetz")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Verena\_Stuetz](https://community.sap.com/t5/user/viewprofilepage/user-id/124098)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51647)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51647)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558601)

‎2023 Jan 31
4:43 PM

[21
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51647/tab/all-users "Click here to see who gave kudos to this post.")

8,560

* SAP Managed Tags
* [FIN General Ledger](https://community.sap.com/t5/c-khhcw49343/FIN%2520General%2520Ledger/pd-p/141573396494884189617506284133567)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [FIN General Ledger

  Software Product Function](/t5/c-khhcw49343/FIN%2BGeneral%2BLedger/pd-p/141573396494884189617506284133567)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (2)

When you set up your SAP S/4HANA Cloud system for the first time, there's a number of decisions you need to make regarding the settings that'll be valid for the whole system.

Among other things, you're deciding how many and which ledgers you're going to use. This is a big decision that depends on your business environment and whether your company is operating on a national or international level, for example.

The **ledger** is one of the core entities in the system. It combines many of the settings that are critical for accounting. A standard ledger has the following key characteristics:

+ It's based on the Universal Journal and is the central repository for accounting data.

+ It's the entity that records all business transactions and includes the corresponding general ledger accounts.

+ It contains other critical settings that are relevant for a company code using this ledger, such as currencies and accounting standards.

+ And you can use additional standard ledgers for parallel accounting. This is useful when, for example, you need to do your financial reporting according to different sets of accounting standards, such as IFRS and US GAAP.

Based on your company's requirements, you make the ledger-specific settings in the initial scoping phase by selecting the relevant scenarios.
Here are the ledger scenarios and combinations that are available to you:

* Scenario **J58**: One standard ledger that covers your local accounting standard:

  - Ledger **0L** (leading ledger): This ledger is always included in your scope and can't be removed.

* Scenarios **J58 +** **1GA**: Two parallel standard ledgers to allow you to use one local and one corporate accounting standard (IFRS) in parallel:

  - Ledger **0L** (leading ledger): The local accounting standard is assigned to this ledger by default.

  - Ledger **2L** (non-leading ledger): The corporate accounting standard IFRS is assigned to this ledger by default.

* Scenarios **J58 +** **2VA**: Two parallel standard ledgers to fulfill the business need to use one local and one corporate accounting standard (US-GAAP) in parallel:

  - Ledger **0L** (leading ledger): The local accounting standard is assigned to this ledger by default.

  - Ledger **3L** (non-leading ledger): The corporate accounting standard US GAAP is assigned to this ledger by default.

For the parallel accounting options described above (that is, options 2. and 3.), we recommend that you change the default assignments as follows: Assign ledger **0L** to the corporate accounting standard and ledgers **2L** and/or **3L** to the local accounting standard.

* Scenarios **J58 + 1GA + 2VA**: Three parallel standard ledgers to cover you when you need to use a local and two corporate accounting standards (IFRS and US GAAP) in parallel:

+ Ledger **0L** (leading ledger): The local accounting standard is assigned to this ledger by default.

+ Ledger **2L** (non-leading ledger): The corporate accounting standard IFRS is assigned to this ledger by default.

+ Ledger **3L** (non-leading ledger): The corporate accounting standard US GAAP is assigned to this ledger by default.

![](/legacyfs/online/storage/blog_attachments/2023/01/LedgerCombinationsNew.png)

Figure 1: Available combinations of ledgers and accounting standards included in the scenarios delivered by SAP

Please note that this is the default assignment defined in the scoping phase. You can assign any of the available accounting standards (that is, IFRS, USGP and all local accounting standards of the countries that are in your scope) to the relevant ledgers before making the first posting in your system.

As stated above, we recommend that you use the leading ledger with a corporate accounting standard on ledger level, and one of the non-leading ledgers for the local accounting standard.

Things to keep in mind:

What's important to know is that for each ledger that's activated in your system, additional steps are required during the monthly or annual closing activities. The system performs all closing activities, such as settlement, depreciation, or allocation, by ledger.

So you should consider this before making your decision in order to avoid unnecessary data redundancies and not to strain your system performance with ledgers your company doesn't need for its business.

On the other hand, if you know that your company is going to expand its business to another country in the future, it could make sense to activate the relevant scenario already.

Either way, please remember that once you complete the initial scoping of your ledgers, the activation setup can't be reversed. Once you have it, you have it, but you retain the option to change the default assignments of your ledgers to different accounting standards if you need to.

So, for example, let's say your business requirements, such as parallel accounting, call for a change of the assignment of accounting standards to your ledger. You can change this assignment before making the first posting in your system. This means, that you can, for example, assign the leading ledger 0L to your corporate accounting standard (for example, IFRS), and assign your non-leading ledger 2L to your local accounting standard (for example, D...
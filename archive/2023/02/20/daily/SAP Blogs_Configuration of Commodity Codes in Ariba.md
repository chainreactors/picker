---
title: Configuration of Commodity Codes in Ariba
url: https://blogs.sap.com/2023/02/19/configuration-of-commodity-codes-in-ariba/
source: SAP Blogs
date: 2023-02-20
fetch_date: 2025-10-04T07:33:18.112969
---

# Configuration of Commodity Codes in Ariba

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by Members](/t5/spend-management-blog-posts-by-members/bg-p/spend-management-blog-members)
* Configuration of Commodity Codes in Ariba

Spend Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-members/article-id/1839&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Configuration of Commodity Codes in Ariba](/t5/spend-management-blog-posts-by-members/configuration-of-commodity-codes-in-ariba/ba-p/13552521)

![Chhetan1](https://avatars.profile.sap.com/d/3/idd35a10cb1334547512e63e16f648267bf6ed163abca1e3b31a32e8fb0ee05204_small.jpeg "Chhetan1")

[Chhetan1](https://community.sap.com/t5/user/viewprofilepage/user-id/46979)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-members&message.id=1839)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-members/article-id/1839)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552521)

‎2023 Feb 19
12:27 PM

[13
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-members/message-id/1839/tab/all-users "Click here to see who gave kudos to this post.")

22,834

* SAP Managed Tags
* [SAP Ariba Buying and Invoicing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Buying%2520and%2520Invoicing/pd-p/088a2ce1-412b-458b-becb-2311c968d328)

* [SAP Ariba Buying and Invoicing

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BBuying%2Band%2BInvoicing/pd-p/088a2ce1-412b-458b-becb-2311c968d328)

View products (1)

**Hello, welcome to my blog post!** It’s a complete guide for Ariba consultants and administrators who configures and manages commodity codes in Ariba buying solution and Ariba guided buying.

**Introduction**

Commodity codes are created to classify goods and services. They are made up of different levels such as segment, family, class and commodity code and each level of commodity code provides varying details. For example:![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-93.png)

Customers can create custom commodity codes to classify goods and services. A custom commodity code can have 6, 8 or 10 digits. In Ariba, they can map their custom commodity codes or taxonomy codes to standard classification codes which are created by the following classification system

* United Nations Standard Products and Services Code (UNSPSC)

* The Harmonized System (HSN SAC ->Codes are used by Indian customer)

Commodity codes are used to calculate tax, track spend, categorize items in catalogs, simplify 2-way and 3-way match processes, control goods receipts process, set up validation and approval processes etc.

Let’s discuss how to manage commodity codes in Ariba, if customer is using custom commodity codes instead of UNSPSC’s

* Configuration of commodity codes in Ariba buying solution

* Configuration of Ad-hoc classifier in Ariba guided buying

**How to configure commodity codes in Ariba?**

Ariba consultants creates commodity codes in Commodity Code Manager workspace or by using .csv file. A user who has following roles can create, modify, delete, map commodity codes in Ariba buying solution

* Customer Administrator

* Commodity Code Manager

* Purchasing Manager

* Purchasing Agent

* Procurement Manager

* Procurement Agent

There are 3 files required to configure commodity codes in Ariba buying solution. System commodity codes and classification code relationships files need to be loaded to parent realm and ERP commodity to commodity file need to be loaded to child realm

* System Commodity codes

* Classification code Relationships

* ERP Commodity to Commodity Mapping

**Instructions to fill System CommodityCodes.csv**![](/legacyfs/online/storage/blog_attachments/2023/02/Picture-X2.png)

**Domain:** Enter the domain of the commodity code being used, for example: custom or unspsc

**UniqueName:** Update unique code/number of the commodity code

**Name:** Update description or title of the commodity code

**ParentUniqueName:** It shows the hierarchical relationship between commodity codes. Update the unique name of parent commodity code such as level 1, level 2, or level 3 commodities

**Enabled:** This field is useful to hide or show codes. The default value is “Yes”

**AdhocClassification:** This field is optional and can be used to display classification of commodity codes for ad-hoc purchases

**Sample System CommodityCodes.csv file format:****![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-35.png)**

**Steps to import the file in Ariba**

* Go to Parent realm

* On Dashboard, Click Manage

* Click Core Administration

* Dropdown Site Manager and click Data Import/Export

* In the search bar, type commodity and click search

* Click on Export tab

* Click on export button to export “Export Commodity Codes” file

* Update the commodity codes as per the above instructions

* Save the file in .csv file

* Go to Import tab

* Search for Import System Commodity Codes

* Click on Import button

* Select Load radio button

* Browse the file

* Click on Run

**Note:**

* Status “Completed’ indicates that the file has been loaded successfully with no errors

* Status “Completed(!)” indicates that the file has been loaded but there are errors/warnings

**Instructions to fill classification Code Relationships.csv****![](/legacyfs/online/storage/blog_attachments/2023/02/Picture4-26.png)**

**DomainFrom:** Enter the domain of the commodity code to map from, for example: custom

**ValueFrom:** Update the unique name/code of the commodity of From Domain

**DomainTo:** Enter the domain of the commodity code to map to, for example: unspsc

**ValueTo:** Update the unique name/code of the commodity of To Domain

**Sample Classification Code Relationships.csv file format:**![](/legacyfs/online/storage/blog_attachments/2023/02/Picture5-15.png)

**Steps to import the file in Ariba**

* Go to Parent realm

* On Dashboard, Click Manage

* Click Core Administration

* Dropdown Site Manager and click Data Import/Export

* In the search bar, type classification and click search

* Click on Export tab

* Click on export button to export “Export Classification Code Relationships” file

* Update the commodity codes as per the above instructions

* Save the file in .csv file

* Go to Import tab

* Search for Import Classification Code Relationships

* Click on Import button

* Select Load radio button

* Browse the file

* Click on Run

**Note:**

* Status “Completed’ indicates that the file has been loaded successfully with no errors

* Status “Completed(!)” indicates that the file has been loaded but there are errors/warnings

**Instructions to fill ERP Commodity to Commodity mapping.csv**![](/legacyfs/online/storage/blog_attachments/2023/02/Picture6-17.png)

**AccountType:** It should be updated as per AccountType.csv file. It shows operating expenses or capital expenditures. Customers can create multiple account types as per their requirements.

For Example: CapEx, OpEx, Asset, Lease, Audit, Expense, Sundry Exp etc.

**MaterialGroup:** It should be updated as per ERPCommodityCode.csv file. It indicates SAP material group code.

**CommonIdDomain:** Update the name of dom...
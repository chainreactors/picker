---
title: Material Price Determination in SAP Material Ledger (SAP S/4HANA Public Cloud)
url: https://blogs.sap.com/2023/06/10/material-price-determination-in-sap-material-ledger-sap-s-4hana-public-cloud/
source: SAP Blogs
date: 2023-06-11
fetch_date: 2025-10-04T11:45:18.528252
---

# Material Price Determination in SAP Material Ledger (SAP S/4HANA Public Cloud)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Material Price Determination in SAP Material Ledge...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161120&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Material Price Determination in SAP Material Ledger (SAP S/4HANA Public Cloud)](/t5/technology-blog-posts-by-members/material-price-determination-in-sap-material-ledger-sap-s-4hana-public/ba-p/13556561)

![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")

[mickaelquesnot](https://community.sap.com/t5/user/viewprofilepage/user-id/150004)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161120)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161120)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556561)

‎2023 Jun 10
8:59 AM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161120/tab/all-users "Click here to see who gave kudos to this post.")

20,369

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [FIN Controlling](https://community.sap.com/t5/c-khhcw49343/FIN%2520Controlling/pd-p/165905235116577077914579113243106)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [FIN Controlling

  Software Product Function](/t5/c-khhcw49343/FIN%2BControlling/pd-p/165905235116577077914579113243106)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)

View products (6)

Material price determination determines how the valuation of a material occurs after each business transaction for a material. If SAP Material Ledger is active, this field should be set in the material master with an appropriate combination of price control and material price determination. When SAP Material Ledger is active for a valuation area, additional fields become available in the valuation area view.

The following two price indicator options are available in the material master Accounting 1 view for price determination. The Accounting 1 view contains current valuation data of a material.
Transaction-based (2)
If you select this option, you can choose your inventory price control indicator as V (moving average) or S (standard price). With S, the moving average price is calculated for information purposes only.

1 Transaction-Based Material Price Determination

1.1 Use
This function makes it possible for you to calculate the moving average price after every goods movement.
 If the material ledger is not active, you can only calculate the moving average price in the company code currency.
 If the Material Ledger is active, you can calculate the moving average prices for materials in up to three currencies/valuations.
1.2 Integration
After each valuation-relevant transaction, the system automatically performs price determination to adjust the valuation price of the material and the value of the material stock.
For more information, see Collecting Actual Data for the Material Ledger .
1.3 Prerequisites
If you want to calculate the moving average price in up to three currencies/valuations, check the following settings:
 The material ledger is active for the material.
 The material has material price determination 2 .
 The material has price control indicator V .
Note
If the material has material price determination 2 and price control S , the moving average price is calculated for information only. The material is valuated with the standard price.
1.4 Features
Transaction-based material price determination takes the following amounts into account:
 Price differences
 Exchange rate differences
 Revaluation amounts
The standard price can be calculated statistically for materials having price control indicator V, but it has no impact on the valuation of the material.
Postings for Transaction-Based Material Price Determination
The posting logic of transaction-based price determination corresponds to that of the system without the material ledger. Two accounting documents and a Material Ledger document are created for transaction-based material price determination: one of the accounting documents documents the updating of costs in accordance with the expected material price. The other accounting document documents the distribution of price and exchange rate differences. The Material Ledger document exists as a follow-on document to the material document.

Single/Multilevel (3)
If you choose this option the price control must be S. A moving average or Period Unit Price (PUP) is calculated at month end. Single/Multilevel price determination allows you to calculate single and multi-level price differences and carry them over through a multiple level manufactured production structure.

2 Multilevel Price Determination
2.1 Use
Multilevel price determination calculates the periodic unit price for a material. The standard price, the single-level differences cumulated in the period, the differences between planned and actual prices, as well as input material differences (multilevel differences) are all taken into account. The material price calculated in multilevel price determination can be used for inventory valuation.
For more information on the process flow, see: Periodic Actual Costing .
2.2 Prerequisites
The material ledger is active.
Actual costing is active.
The price determination indicator in the material master is set to 3 .
The price control indicator in the material master is set to S .
Single-level price determination has been performed.
2.3 Features
A level is identified by a material and its associated procurement process . Multiple levels are the result of one material being used in another material. These multiple levels are reflected in the actual BOM that is created in the costing run in the step Determine Sequence .
In multilevel production, both single-level and multilevel price differences exist. If one material is used in another material, and single-level price differences exist for the input material, this results in multilevel price differences. In this way, difference...
---
title: Scrap Value, Cut off Value and Memo Value in Fixed Asset Accounting
url: https://blogs.sap.com/2023/01/29/scrap-value-cut-off-value-and-memo-value-in-fixed-asset-accounting/
source: SAP Blogs
date: 2023-01-30
fetch_date: 2025-10-04T05:10:21.091894
---

# Scrap Value, Cut off Value and Memo Value in Fixed Asset Accounting

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Scrap Value, Cut off Value and Memo Value in Fixed...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67510&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Scrap Value, Cut off Value and Memo Value in Fixed Asset Accounting](/t5/enterprise-resource-planning-blog-posts-by-members/scrap-value-cut-off-value-and-memo-value-in-fixed-asset-accounting/ba-p/13556371)

![thaider110](https://avatars.profile.sap.com/e/d/idedc54c4a46b387261185083b85e69968218c8f6cd8ee50f2266ad5c72a5c7f88_small.jpeg "thaider110")

[thaider110](https://community.sap.com/t5/user/viewprofilepage/user-id/43116)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67510)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67510)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556371)

‎2023 Jan 29
6:56 AM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67510/tab/all-users "Click here to see who gave kudos to this post.")

13,844

* SAP Managed Tags
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Asset Accounting](https://community.sap.com/t5/c-khhcw49343/FIN%2520Asset%2520Accounting/pd-p/253758978139952938680563247610563)

* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Asset Accounting

  Software Product Function](/t5/c-khhcw49343/FIN%2BAsset%2BAccounting/pd-p/253758978139952938680563247610563)

View products (2)

Hello everyone!

In this blog post, I will try to give you some insights into the scrap value, cut-off value, and memo value in Fixed Asset accounting.

In certain countries it is a legal requirement that assets must not be fully depreciated; depreciation should stop when a certain net book value is reached. There are various options available in SAP to handle this requirement.

* Scrap Value

* Cut Off Value Key

* Memo Value

***Scrap Value:*** Definite Scrap value (Absolute amount or in percentage) can be entered in Asset master data for the specified depreciation area.

This can be used where; the scrap value is not specific or varies from asset to asset. Hence, value can be entered directly in the asset master for the specified depreciation area.

As shown in the example, double-click on the depreciation area for which the scrap value needs to be set.![](/legacyfs/online/storage/blog_attachments/2023/01/S1.jpg)

Depreciation Tab in Asset Master

In this case, a scrap value of 10% is maintained for depreciation area 01.

![](/legacyfs/online/storage/blog_attachments/2023/01/S2-1.jpg)

Scrap value of 10% maintained in the Asset master

If we maintained both an absolute value and also a percentage, then the absolute value will be ignored, and the percentage will be considered for scrap value calculation.

I do not have the system, to demonstrate the scrap value testing, but this is how it needs to be maintained.

***Cut-Off Value Key:*** If we are aware of the percentage or the value to consider stopping depreciation, then the cut-off value key can be used. With the use of a cut-off value key, we can stop depreciation once a certain net book value is reached. By defining a cut-off key and assigning it to the depreciation key used in the depreciation area.

The cut-off value key can be configured to determine automatically scrap values. Cutoff percentage rates for each year of acquisition and with a validity period can be specified, from what point the system should start calculating the validity period. Different cut-off percentages for each scrap value key can be entered. Cut-off percentages/levels per acquisition year, and the validity can be of any length.

**Cut off value key can be defined in the following ways.**

* Depreciation should first be determined without considering the cut-off value, and then ends when the cut-off value is reached. In this case, depreciation will stop before the end of the planned useful life.

* The cut-off value should be deducted from the base depreciation value from the start. In this case, the cut-off value is reached as the net book value.

Once the cut-off value key is configured it can be assigned to the depreciation key used in the depreciation area. Once the depreciation key is assigned to an asset and acquisition cost is posted to the asset, the cut-off key will calculate the cut-off value and will show the planned depreciation amount for the periods of the fiscal year.

Cut-Off Key can be defined in the below path of SAP customizing.

**SPRO ==> Financial Accounting ==> Asset Accounting ==> Depreciation ==> Valuation Methods ==> Further Settings ==> Define Cutoff Value Key**

Or

**ORFA** **==> Asset Accounting ==> Depreciation ==> Valuation Methods ==> Further Settings ==> Define Cutoff Value Key**

**The following parameters need to be defined for creating a cut-off value key.**

![](/legacyfs/online/storage/blog_attachments/2023/01/S3.jpg)

Path of Cut-off value key configuration

![](/legacyfs/online/storage/blog_attachments/2023/01/S4.jpg)

Default Cut off value key

![](/legacyfs/online/storage/blog_attachments/2023/01/S5.jpg)

Cut off value key configuration

**Scrap Value Deduction from Base Value** (Check this box if you want to deduct a cut-off value from Base Value.

If we set this indicator, the scrap value or percentage of the scrap value will be deducted from the depreciation base at the start of depreciation. If this indicator is not set, then depreciation will be calculated without considering scrap value and it will stop once the cut-off value is reached.

**Start Date of Calculation of percentages:** From Asset Capitalization date.

![](/legacyfs/online/storage/blog_attachments/2023/01/S6.jpg)

Cut off value key configuration

**Valid to:** Fiscal year up to and including which the specs are valid. Update 9999 if valid for all the years.

**To Year of Acquisition:** This is the acquisition year up to which this entry is valid.

**Validity in Years:** Validity period for a percentage rate in a calendar year

**Cut-off Percentage:** Cut-off value percentage.

**Once the cut-off value key is defined it can be assigned to the depreciation key.**

![](/legacyfs/online/storage/blog_attachments/2023/01/S7.jpg)

Cut off value key assignment to depreciation key

Once depreciation key KRL3 is assigned to an asset for the assigned depreciation areas, once acquisition cost is posted. The cut-off value will be automatically get determined.

This cut-off value key and depreciation key shown in the screenshots are default values provided by SAP. Based on the requirement cut-off value key can be customized.

***Memo Value:*** Memo value is a standard functionality provided by SAP to allow managing memo values from the legacy system. Memo value is set at the company code and depreciation area level. The system decreases planned annual depreciation in the acquisition year for the asset...
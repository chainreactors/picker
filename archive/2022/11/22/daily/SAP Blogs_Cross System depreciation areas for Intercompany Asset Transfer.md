---
title: Cross System depreciation areas for Intercompany Asset Transfer
url: https://blogs.sap.com/2022/11/21/cross-system-depreciation-areas-for-intercompany-asset-transfer/
source: SAP Blogs
date: 2022-11-22
fetch_date: 2025-10-03T23:23:22.783620
---

# Cross System depreciation areas for Intercompany Asset Transfer

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Cross System depreciation areas for Intercompany A...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67351&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cross System depreciation areas for Intercompany Asset Transfer](/t5/enterprise-resource-planning-blog-posts-by-members/cross-system-depreciation-areas-for-intercompany-asset-transfer/ba-p/13554285)

![thaider110](https://avatars.profile.sap.com/e/d/idedc54c4a46b387261185083b85e69968218c8f6cd8ee50f2266ad5c72a5c7f88_small.jpeg "thaider110")

[thaider110](https://community.sap.com/t5/user/viewprofilepage/user-id/43116)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67351)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67351)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554285)

‎2022 Nov 21
10:06 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67351/tab/all-users "Click here to see who gave kudos to this post.")

5,646

* SAP Managed Tags
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN Asset Accounting](https://community.sap.com/t5/c-khhcw49343/FIN%2520Asset%2520Accounting/pd-p/253758978139952938680563247610563)

* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN Asset Accounting

  Software Product Function](/t5/c-khhcw49343/FIN%2BAsset%2BAccounting/pd-p/253758978139952938680563247610563)

View products (2)

Hello everyone!!

This blog is a continuation of my earlier blog on Intercompany Asset Transfer.

I recommend you go through my previous blog; the link is below for the same.

[https://blogs.sap.com/2022/11/16/asset-transfer-between-the-company-codes-intercompany-asset-transfe...](https://blogs.sap.com/2022/11/16/asset-transfer-between-the-company-codes-intercompany-asset-transfer/)

**Introduction**

Earlier we have seen different types of Intercompany asset transfer and their Pros and Cons. Now here we will discuss the configuration needed for automatic intercompany asset transfer where depreciation areas have different functions or purposes or the number of depreciation areas are different in both the charts of depreciation.

If the purpose of depreciation areas in two charts of depreciation is different or the depreciation area codes are different, then we have to use a manual process in which we have to retire an asset in sending the company code and acquire an asset in receiving company code with manual updates of a trading partner.

As this is a cumbersome process, where we have to execute two different transaction codes, to make use of the standard process of intercompany transfer (transaction code ABT1N), we have to define **Cross-System Depreciation Areas.** Cross-system depreciation areas are configured to set depreciation areas from different Charts of Depreciation to a single key (cross-system depreciation area) and then give these areas the same significance across the system.

**Use of Cross-system Depreciation Areas:**

Cross-system depreciation areas need to be configured when two company codes use different charts of depreciation and if they want to use the standard process of intercompany asset transfer. Below are the possible scenarios.

* If depreciation areas in these two charts of depreciation areas have the same functions, but they have different codes.

* The depreciation areas in these two charts of depreciation have the same code but different functions.

* The other possibility could be the number of depreciation areas in these two charts of depreciation may not be the same.

* If values of any depreciation area that you do not want to transfer. Then do not assign that area to a cross-system depreciation area.

Cross-system depreciation areas are used to manage the transfer of values during intercompany asset transfer in the above scenarios.

Cross-system depreciation areas are defined and unique assignments from one depreciation area to another depreciation area with the same function. We assign depreciation areas from different charts of depreciation, that have the same function, to the same cross-system depreciation area.

**There could be 3 different possibilities when we do the asset intercompany transfer using cross-system depreciation areas**

* **Depreciation area exists on sending asset and on receiving asset**

The receiving asset has a depreciation area with the same code as the depreciation area on the sending asset: In this case, the system transfers the values according to the transfer method defined in the transfer variant (gross or net) for this company code relationship type.

* **Depreciation area exists only on the receiving asset**

There is a depreciation area on receiving asset that is **not on the sending asset,** The system does not transfer values for this depreciation area if we use the **gross** transfer method. However, if we use the **net** transfer method, this depreciation area in the receiving asset can take up values from another depreciation area during the asset transfer transaction, if the depreciation area in the receiving asset has been defined as a dependent area in customizing, meaning that it depends on another depreciation area to adopt values.

* **Depreciation area exists only on the sender asset**

There is a depreciation area in the sending asset, and that depreciation area is **not on the receiving asset,** in this case, we can use only **net** transfer method. The system does carry out the posting but does not transfer values for this depreciation area. Any depreciation areas that are transferred using the **gross** method must exist in both the sending and the receiving asset, otherwise, the system will not accept the postings and gives an error message.

If you have any of the above scenarios then it is imperative to make use of cross-system depreciation areas, you have to create cross-system depreciation areas explicitly for all depreciation areas that are transferred. Even if we need a cross-system depreciation area for one depreciation area and all other depreciation areas have similar functions with the same codes, we need to assign cross-system depreciation areas to all depreciation areas of all charts of depreciation.

Cross-system depreciation areas have no influence on the creation of the depreciation areas on the receiving asset, cross-system depreciation areas only affect the transfer of values. The creation of depreciation areas on the receiving asset is controlled by the customizing configuration <*Determine Depreciation Areas in the Asset Class>.*

**Configuration Steps for cross-system depreciation areas.**

To define the cross-system depreciation area go to SPRO -> Financial Accounting-> Asset Accounting -> Transactions -> Intercompany asset transfer -> Automatic Intercompany Asset Transfers -> Define Cross-System Depreciation Areas.

OR

You can also go to Asset...
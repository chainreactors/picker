---
title: Error M8783 Negative moving average price prevents posting – how to resolve
url: https://blogs.sap.com/2022/12/15/error-m8783-negative-moving-average-price-prevents-posting-how-to-resolve/
source: SAP Blogs
date: 2022-12-16
fetch_date: 2025-10-04T01:40:20.564197
---

# Error M8783 Negative moving average price prevents posting – how to resolve

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Error M8783 Negative moving average price prevents...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50667&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Error M8783 Negative moving average price prevents posting - how to resolve](/t5/enterprise-resource-planning-blog-posts-by-sap/error-m8783-negative-moving-average-price-prevents-posting-how-to-resolve/ba-p/13551787)

![davidowen](https://avatars.profile.sap.com/d/1/idd15df3b3b657fd3ef61e86869796b9ce7532d4e4650fffe24cfb99d75b870ea0_small.jpeg "davidowen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[davidowen](https://community.sap.com/t5/user/viewprofilepage/user-id/95441)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50667)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50667)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551787)

‎2022 Dec 15
6:22 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50667/tab/all-users "Click here to see who gave kudos to this post.")

22,354

* SAP Managed Tags
* [MM Invoice Verification](https://community.sap.com/t5/c-khhcw49343/MM%2520Invoice%2520Verification/pd-p/458360983784136828334119370605946)

* [MM Invoice Verification

  Software Product Function](/t5/c-khhcw49343/MM%2BInvoice%2BVerification/pd-p/458360983784136828334119370605946)

View products (1)

The target audience for this blog include; SAP Finance & Accounts Payable Super-users and implementation partners.

## What to expect from this blog:

The purpose of this blog is to describe the conditions that lead to an M8783 “Negative MAC” error and how it might be overcome. An understanding of the principles behind Moving Average Cost is necessary to make sense of this situation.

**TLDR** You can use the GL Posting feature of MIRO (and BAPI invoice post) to “force” any price difference between GR and IR to an account of your choice and avoid the M8783 error.

The error is documented in SAP Note 66754 first published in 1997

## 66754 - Negative moving price prevents posting

<https://launchpad.support.sap.com/#/notes/66754>

*A document cannot be posted since the user receives the error message M8783 "Moving average price for material & & & is negative". It concerns a material which is valuated with the moving average price. The system makes no automatic posting to a price difference account.*

## 753286 - Moving average price becomes very low

<https://launchpad.support.sap.com/#/notes/753286>

*You post invoice documents with the online transactions of the Logistics Invoice Verification. When you update the Moving Average Price (MAP), for specific constellations this may result in the MAP continuously decreasing until it nearly reaches 0, or the system issues error message M8 783 "Moving average price for material is negative: ..."*

In layperson terms, the conditions that lead to this error include:

A product is valued with moving average price

Over time, the product is purchased and received on multiple orders

The price of the product is dropping with each PO (perhaps natural price decreases or user-error inputting PO price)

The quantity of goods on hand are being partial consumed by various business processes. And/or the moving average price is being manually corrected down via transaction MR22 Material price Debit/Credit.

Invoices are posted, at consistently lower values than the original PO price and subsequent goods receipt

As these invoices are posted, they need to clear out the original GR amount posted to the GRIR account, the difference between GR and IR is always posted back into moving average price (with 2 exceptions; zero stock and partial stock coverage) If these are of interest to you, refer to “How-To” note 3073585 - Procurement - Invoice Verification - Standard behaviors guide and How-to scenarios – section 2

<https://launchpad.support.sap.com/#/notes/3073585>

In this situation, the difference to be cleared from GRIR account exceeds the remaining value of inventory on hand and triggers the M8783 error – MAC cannot go negative.

I won’t go into a detailed discussion of the exact conditions under which this error occurs, you can read the notes referenced above for detailed information. Suffice to say that SAP has determined that a hard-error is the only appropriate response to this condition – which is problematic in a high-volume environment. The corrective steps described by SAP are time-consuming to carry out, require access to multiple transactions which may not be part of a finance back-office user’s security profile and may require the use of a firefighter ID to resolve.

The standard solution proposed by SAP is to arbitrarily increase the value of inventory on hand to allow the invoice to be posted – using transaction MR22.

Problems arise with this approach, customers find it to be in conflict with generally accepted accounting principles and time consuming, additionally it can be difficult to know exactly how much to increase the price. A user needs to look at the PO history to determine the quantity ordered/delivered and original price.

Secondly, it is possible for a multi-line invoice to have multiple M8783 errors however, the system will error out at the first instance and the user will not know of subsequent errors until they adjust the first material price. This can be frustrating and time-consuming for the user.

Third, the delay in processing invoices may lead to a situation where a supplier withholds future deliveries and leads to an out-of-stock situation and subsequent business impact.

# Alternate solution to M8783 error

Most customers who encounter this situation expect that SAP standard functionality would be to post the invoice difference to a price difference account (modifier PRD) as is done in the cases of limited stock coverage or zero stock. SAP has stated that they do not have a valid basis to determine the variance amount to be posted and therefore do not treat it as a price difference posting.

There is a simple technique in standard MIRO to post a price variance manually to avoid the M8783 error. During invoice entry, accept the default value for invoice header amount and the default item price from the Purchase Order. To make the document balance, create a manual line item on the “GL Posting” tab of MIRO, the account can be your default purchase price variance account. This GL posting line will override the standard functionality which would try to apply the price variance to moving average cost.

You may need to configure MIRO for direct posting to G/L in the IMG, follow the path:

SPRO > Materials Management > Logistics Invoice Verification > Incoming Invoice > Activate Direct Posting to G/L Accounts and Material Accounts > Activate "Dir.posting to G/L acct = active" and save.

In transaction MIRO - It will show additional Tab as "GL Account" along with "Reference"

This solution can ...
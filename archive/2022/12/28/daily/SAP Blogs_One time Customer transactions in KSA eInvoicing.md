---
title: One time Customer transactions in KSA eInvoicing
url: https://blogs.sap.com/2022/12/27/one-time-customer-transactions-in-ksa-einvoicing/
source: SAP Blogs
date: 2022-12-28
fetch_date: 2025-10-04T02:36:09.073377
---

# One time Customer transactions in KSA eInvoicing

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* One time Customer transactions in KSA eInvoicing

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51651&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [One time Customer transactions in KSA eInvoicing](/t5/enterprise-resource-planning-blog-posts-by-sap/one-time-customer-transactions-in-ksa-einvoicing/ba-p/13558618)

![zaheer4sana](https://avatars.profile.sap.com/8/6/id863b72fe3ccc97f5268916569b2c742228a08c21c297e1014d414c2e01cec4b3_small.jpeg "zaheer4sana")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[zaheer4sana](https://community.sap.com/t5/user/viewprofilepage/user-id/40999)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51651)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51651)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558618)

‎2022 Dec 27
9:49 AM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51651/tab/all-users "Click here to see who gave kudos to this post.")

1,945

* SAP Managed Tags
* [Retail](https://community.sap.com/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Document and Reporting Compliance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520and%2520Reporting%2520Compliance/pd-p/73554900100700003181)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Document and Reporting Compliance

  Software Product](/t5/c-khhcw49343/SAP%2BDocument%2Band%2BReporting%2BCompliance/pd-p/73554900100700003181)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Retail

  Industry](/t5/c-khhcw49343/Retail/pd-p/99624789925257984685885)

View products (4)

## What's in this Blog?

For the non-returning customers in your business, you may have created one-time customer master with which you may at time create orders and subsequently invoice documents in your business.

How are such transactions handled in the SAP's solution for KSA eInvoicing ? what data's and where do they need to be maintained? what are the constraints?

you may have multiple questions as above. Don't worry, this Blog explains it all.

## One time - customer

What generally we first think about one time customer is that it is relevant only for B2C business scenarios where just just one customer master is used to transact with multiple persons and still record their individual identity. This is not always the case. One-time customers can also be used for B2B business scenarios as well.

Having said this, you may just create one single one time customer master in the Business partner transaction and still use it for both B2B or standard invoices and associated credit / debit notes as well as B2C transactions depending on your requirements. Or you may also choose to create one unique OT customer master for B2B and another one for B2C.

## The differentiator

The key that differentiates between B2B and B2C transactions in OT customer transactions is the Natural person indicator (BSEC-STKZN). This is shown in the picture below

When this field is set in the OT data entry screen, the transaction is identified as B2C transaction. If not, then it is considered as B2B transaction.

![](/legacyfs/online/storage/blog_attachments/2022/12/Onetime-customer-screen-in-FI.jpg)

We may enable the natural person indicator at the BP level but that is not considered to identify the type of transaction. So, in case you want the transaction to be created as B2C transaction, you will have to ensure that this field is enabled at the transaction level before saving the document.

## VAT number for one-time B2B customer

As all other data are read from the transaction level for one time customer, the VAT number also s read from the transaction level. By standard, the VAT number entered in the screen for OT customers at transaction level is copied to its relevant billing document and the einvoicing solution reads the VAT number from the billing document itself.

## ![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-8.jpg)

## Preparatory activities:

The fields used for capturing the one-time customer data is the same as the master data read happening for normal customers in the KSA eInvoicing solution, just that the tables where data is stored is different.

Depending on your system setting you may need to prepare the OT data entry screen to facilitate the entry of the customer information in your system. you may refer to the [blog](https://blogs.sap.com/2021/11/01/entry-of-master-data-for-one-time-accounts/)

**Other blogs on KSA eInvoicing**

[Solution onboarding guide](https://blogs.sap.com/2022/10/25/sap-erp-solution-unit-onboarding-guide-for-e-invoicing-in-ksa/comment-page-1/#comment-645327)

[Master data mapping in KSA eInvoicing solution | SAP Blogs](https://blogs.sap.com/2022/11/15/master-data-mapping-in-ksa-einvoicing-solution/)

[Handling Intercompany transactions in KSA eInvoicing | SAP Blogs](https://blogs.sap.com/2022/12/28/handling-intercompany-transactions-in-ksa-einvoicing/)

**Some useful links**

* [SAP Document Compliance topic page](https://community.sap.com/topics/document-compliance)

* [Document Compliance Help Page](https://help.sap.com/viewer/product/SAP_E_DOCUMENT/)

* [Announcement Legal Notification](https://launchpad.support.sap.com/#/legalchangenotification)

* [KSA eInvoicing Webinar (Login required)](https://jam4.sapjam.com/groups/aDJPUFaeB2noMhwk999hKH/documents/xCoWRQdXKqEl2B9nV7VBXk/slide_viewer)

* [Saudi Arabia E-Invoice Webinar 28Sep2022.pdf (sapjam.com) (Login required)](https://jam4.sapjam.com/groups/aDJPUFaeB2noMhwk999hKH/documents/xCoWRQdXKqEl2B9nV7VBXk/slide_viewer)

* [[Release announcement] Phase 2 Solution for Saudi Arabia Electronic Invoicing (sapjam.com) (Login re...](https://jam4.sapjam.com/blogs/show/U3t5340x2oQxetbRbPlDxu?_lightbox=true)

* [Entry of master data for one-time accounts | SAP Blogs](https://blogs.sap.com/2021/11/01/entry-of-master-data-for-one-time-accounts/)

**Note**: For accessing the last three links listed above you need to login to [MENA Localization SIG – Overview (sapjam.com)](https://jam4.sapjam.com/groups/aDJPUFaeB2noMhwk999hKH/overview_page/tIrpXHotIJc48uFvrBozQc)

Thank you for reading this blog. I hope the information is useful to you. Please share your feedback in the comments section below.

I encourage you to follow my profile for similar content.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

2 Comments

You must be...
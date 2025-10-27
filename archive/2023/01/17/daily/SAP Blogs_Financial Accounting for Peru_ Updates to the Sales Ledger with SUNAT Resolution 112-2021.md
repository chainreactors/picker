---
title: Financial Accounting for Peru: Updates to the Sales Ledger with SUNAT Resolution 112-2021
url: https://blogs.sap.com/2023/01/16/financial-accounting-for-peru-updates-to-the-sales-ledger-with-sunat-resolution-112-2021/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:44.402905
---

# Financial Accounting for Peru: Updates to the Sales Ledger with SUNAT Resolution 112-2021

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Financial Accounting for Peru: Updates to the Sale...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53403&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Financial Accounting for Peru: Updates to the Sales Ledger with SUNAT Resolution 112-2021](/t5/enterprise-resource-planning-blog-posts-by-sap/financial-accounting-for-peru-updates-to-the-sales-ledger-with-sunat/ba-p/13570746)

![BarnabasKirk](https://avatars.profile.sap.com/d/1/idd1578ae940af54f2732324180a256ca04e1910354c0ae6fadb006d2e018cd2d5_small.jpeg "BarnabasKirk")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[BarnabasKirk](https://community.sap.com/t5/user/viewprofilepage/user-id/12122)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53403)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53403)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570746)

‎2023 Jan 16
1:43 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53403/tab/all-users "Click here to see who gave kudos to this post.")

1,327

* SAP Managed Tags
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/01/TitlePicture_Peru_Blog_EN.png)

Updates to the Sales Ledger with SUNAT Resolution 112-2021

I’m pleased to share with you the recent updates to the Peru **Sales Ledger** report (*Registro de Ventas e Ingresos Electrónico*, RVIE) for **SAP ERP Central Component** (SAP ECC). These changes were implemented to meet the legal requirements specified by the Peruvian tax authority, SUNAT (*Superintendencia Nacional de Aduanas y de Administración Tributaria*) in the Resolution 112-2021.

* For legal details on the SUNAT Resolution 112-2021, please refer to the [SUNAT website](https://www.gob.pe/institucion/sunat/normas-legales/2115590-112-2021-sunat).

* For technical implementation details for you SAP solution, please refer to [SAP Note 3152563](https://launchpad.support.sap.com/#/notes/3152563).

In this blog post, I’ll list the key updates to the Peru Sales Ledger (RFCLLIB03\_PE) report and explain how you can make the most of the new functionalities.

**1. Generate TXT files**

You now have the option to generate a file in the SUNAT-mandated TXT format, which you can download and submit electronically to the Peruvian tax authority.  If you prefer not to generate a TXT file, you can still preview the report output with the ABAP List Viewer (ALV).

Generating your TXT file couldn’t be easier, simply select the “Create File” checkbox when completing the report information:

![](/legacyfs/online/storage/blog_attachments/2023/01/Peru_SalesLedger_CreateFile.png)

The screenshot shows the Create File checkbox in the Output File Creation section of the Sales Ledger report.

**2. Specify the TXT file location**

To generate a file in TXT format, you first need to specify the file path and the file name.

Before running the Sales Ledger report, run the ***FILE*** transaction and configure the following information:

2.1: Logical file path: FI\_PE\_SALES\_LEDGER

2.2: Logical File name: FI\_PE\_ARCHIVE\_SL\_FILE

**3. New configuration activities**

There are two new configuration activities that you need to complete to run the Sales Ledger report:

3.1: Group Tax Balances (V\_T007L)

3.2: Group Tax Base Balances (V\_T007K)

For documentation on the SPRO pathways for these configuration activities, refer to the most recent version of the SAP Help Portal documentation: [SAP Help Portal Documentation for Peru FI](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/fccf2ded571b4269ba14877b195df45a/14b4c2920dd94a07b6a2011611e759c2.html?locale=en-US,301).

For documentation on generating these configuration activities, and for which Group Numbers to enter in each activity, select the Document icon in your configuration environment:

![](/legacyfs/online/storage/blog_attachments/2023/01/Peru_Configuration_Documentation.png)

The screenshot shows the Documentation icon positioned alongside the Run icon in the configuration environment.

**4. Error Messages**

You can now access the Application Log for any error messages that are generated during the report validation process.

To access the Application Log, run the transaction ***SLGI*** and inform the following information:

4.1: Object: FI\_LOC\_PE

4.2: Subobject: SALES\_LEDGER

**Closing Remarks**

The Peru **Sales Ledger** report is now updated with these changes and ready for you to use. If you have any further questions about this report or any of these recent changes, then please let me know in the comments. Your feedback is always appreciated and can even be the subject of my next blog post.

Thank you and until next time,

Barnabas Kirk

#SAPGoGlobal #SAPLocalization

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [Configuration](/t5/tag/Configuration/tg-p/board-id/erp-blog-sap)
* [fi](/t5/tag/fi/tg-p/board-id/erp-blog-sap)
* [Legal Change](/t5/tag/Legal%20Change/tg-p/board-id/erp-blog-sap)
* [peru](/t5/tag/peru/tg-p/board-id/erp-blog-sap)
* [sap ecc](/t5/tag/sap%20ecc/tg-p/board-id/erp-blog-sap)
* [sunat](/t5/tag/sunat/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Ffinancial-accounting-for-peru-updates-to-the-sales-ledger-with-sunat%2Fba-p%2F13570746%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [Japan Bank Charges in Payment Lots](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-lots/ba-p/14231915)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint...
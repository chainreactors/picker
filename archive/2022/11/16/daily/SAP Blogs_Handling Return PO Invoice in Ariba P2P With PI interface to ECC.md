---
title: Handling Return PO Invoice in Ariba P2P With PI interface to ECC
url: https://blogs.sap.com/2022/11/15/handling-return-po-invoice-in-ariba-p2p-with-pi-interface-to-ecc/
source: SAP Blogs
date: 2022-11-16
fetch_date: 2025-10-03T22:52:45.954610
---

# Handling Return PO Invoice in Ariba P2P With PI interface to ECC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by Members](/t5/spend-management-blog-posts-by-members/bg-p/spend-management-blog-members)
* Handling Return PO Invoice in Ariba P2P With PI in...

Spend Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-members/article-id/1818&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Handling Return PO Invoice in Ariba P2P With PI interface to ECC](/t5/spend-management-blog-posts-by-members/handling-return-po-invoice-in-ariba-p2p-with-pi-interface-to-ecc/ba-p/13548143)

![RajeshSubbaiah](https://avatars.profile.sap.com/7/2/id72b8d79cb053613cc86a30e765162d9d5b26be7f2b69f978d2f3befdd4269826_small.jpeg "RajeshSubbaiah")

[RajeshSubbaiah](https://community.sap.com/t5/user/viewprofilepage/user-id/45110)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-members&message.id=1818)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-members/article-id/1818)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548143)

‎2022 Nov 15
8:36 PM

[1
Kudo](/t5/kudos/messagepage/board-id/spend-management-blog-members/message-id/1818/tab/all-users "Click here to see who gave kudos to this post.")

1,188

* SAP Managed Tags
* [SAP Ariba Procurement](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Procurement/pd-p/73554900100700001921)

* [SAP Ariba Procurement

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BProcurement/pd-p/73554900100700001921)

View products (1)

**Work around for handling Return-PO Credit Memo in Ariba Invoice Pro to ECC**

Vendors return PO process in ECC

Normally in some Chemical and Process industries materials are purchased with reusable containers or IBC totes which have unit price and can be refunded from vendors when those are returned to Vendor. In normal process the customer will gather these empty special containers or totes after consuming the material in it. They will ship to vendor when sufficient numbers of those to fit for their normal truck/wagon load by a separate Vendor return PO process. In ECC this scenario is handled by most of the customers by Vendor Return PO in which return indicator is checked in the PO and net value will be negative. GR returns can be done by 161 Movement type and Direct Credit Memo can be done in ECC.

Limitation in Ariba Invoice Management

In Ariba Invoice Pro Return-PO (Vendor Return Process) and direct Credit Memo for PO Invoices is not supported. Only direct credit memo is supported for Non-PO Scenarios. And customers are forced to handle this scenario out of Ariba Invoice pro or by different payment method to get credit from vendors for these return items.

Work around process & Minor enhancement in ECC

The Return-PO will be integrated with Ariba-Invoice Pro as a normal PO, and it won’t handle the return-PO field (EKPO-RETPO). We need to do minor enhancement in ECC for Vendor returns movement to integrate with Ariba as Rejected Qty like below to match ECC 161 GI to Vendor.

In “/ARBA/PARAM\_TAB” an Ariba table for configurable parameters, we need to maintain 161-Movement Type as RETURN\_MVT to integrate this GI to Ariba Invoice Pro.

ECC Setting in Table **/ARBA/PARAM\_TAB**

![](/legacyfs/online/storage/blog_attachments/2022/11/Return-PO.jpg)

*Note:* *Even we are maintaining parameter for 161 Mov-Type as return in ECC as Ariba Invoice management isn’t supporting return functionality fully so it will show as Rejected in Ariba which means inventory sent to Vendor.*

Once PO and GR are integrated to Ariba Invoice pro as expected then we need to do a small tweak while posting Invoice (credit memo).

Technically we need to post Negative Invoice in Ariba-Inv Pro like changing qty or price with negative value once it pulls data based on PO#. Now in the Invoice “Payable to supplier” will be showing as “-$100.00 USD”.

Invoice Integration to ECC

In ECC the Invoice should be posted as a Credit Memo instead of Invoice, for that we need to make some changes in exit “EXIT\_SAPLMRMH\_011” posting IDoc in ECC to post this particular type as “CRME” instead of “INVO” when the IDOC Field E1EDK01-BSART=Document Type specific Return PO with Return PO Indicator Checked.

This will make Invoice posted as Credit Memo in ECC and Vendor Payment integration will work fine without any Modification.

**Benefits: -**

Any Customer where this return to Vendor process is handled separately without referencing the purchase PO, mostly process and Chemical manufacturing & Pharma will use this work around to fulfil their process without contrary. By the small tweak & minor enhancement we can match the $ amount value exactly same in Ariba Invoice Pro vs ECC without any Deviation or audit query.

Refer below links for SAP Ariba standard Process

<https://apps.support.sap.com/sap/support/knowledge/preview/en/2533755>

<https://help.sap.com/doc/e1a7635fc81845edbc43c61376258598/cloud/en-US/InvoiceProcess.pdf>

* [Work around for handling Return-PO Credit Memo in Ariba Invoice Pro to ECC](/t5/tag/Work%20around%20for%20handling%20Return-PO%20Credit%20Memo%20in%20Ariba%20Invoice%20Pro%20to%20ECC/tg-p/board-id/spend-management-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fspend-management-blog-posts-by-members%2Fhandling-return-po-invoice-in-ariba-p2p-with-pi-interface-to-ecc%2Fba-p%2F13548143%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [The Procurement Monthly - September 2025](/t5/spend-management-blog-posts-by-sap/the-procurement-monthly-september-2025/ba-p/14216757)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)  3 weeks ago
* [SAP Ariba Central Invoice Management 2508 Release Highlights](/t5/spend-management-blog-posts-by-sap/sap-ariba-central-invoice-management-2508-release-highlights/ba-p/14162051)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)  2025 Jul 31
* [SAP Ariba 2508 Release Key Innovations Preview](/t5/spend-management-blog-posts-by-sap/sap-ariba-2508-release-key-innovations-preview/ba-p/14159593)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)  2025 Jul 31
* [What's New in 2508 - Release Navigator for Spend Management](/t5/spend-management-blog-posts-by-sap/what-s-new-in-2508-release-navigator-for-spend-management/ba-p/14164748)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)  2025 Jul 28
* [Handling Field Length Differences in SAP Ariba – SAP ERP including S/4 HANA Integration Using CIG.](/t5/spend-management-blog-posts-by-sap/handling-field-length-differences-in-sap-ariba-sap-erp-including-s-4-hana/ba-p/14143805)
  in [Spend Management Blog Posts by SAP](/t5/spend-managem...
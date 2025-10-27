---
title: Consume CDS View inside AMDP Procedure
url: https://blogs.sap.com/2022/12/03/consume-cds-view-inside-amdp-procedure/
source: SAP Blogs
date: 2022-12-04
fetch_date: 2025-10-04T00:28:47.955939
---

# Consume CDS View inside AMDP Procedure

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Consume CDS View inside AMDP Procedure

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68271&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Consume CDS View inside AMDP Procedure](/t5/enterprise-resource-planning-blog-posts-by-members/consume-cds-view-inside-amdp-procedure/ba-p/13565767)

![chau1995](https://avatars.profile.sap.com/1/8/id186df8aa26624d10502d6761be8fc5c3f99a26f958b84af86b163dcb2b147279_small.jpeg "chau1995")

[chau1995](https://community.sap.com/t5/user/viewprofilepage/user-id/526082)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68271)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68271)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565767)

‎2022 Dec 03
2:58 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68271/tab/all-users "Click here to see who gave kudos to this post.")

17,361

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SQL](https://community.sap.com/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SQL

  Programming Tool](/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)

View products (4)

In previous [article](https://blogs.sap.com/2022/12/03/consume-cds-view-inside-cds-table-function-by-using-amdp/), we have experienced by using CDS View inside CDS Table function. And now, we will try with AMDP procedure

Like as CDS table function, with AMDP Procedure, we will also catch an error

![](/legacyfs/online/storage/blog_attachments/2022/12/CDS_001.png)

Because this CDS View which we used in this article is a client specific. But AMDP is not. Basically, AMDP will get all data of all client (assume your system have several clients), that is a reason why you catch this error when working with CDS view.

So, how to resolve it? Please read this article with me.

**Prerequisites**:

A little bit CDS View and AMDP. If you don’t have any experience, please follow [link](https://blogs.sap.com/2020/08/25/first-program-with-amdp-method/)

**Solution**

We will create Global Class and handle method to get data from CDS View, both standard CDS View and Customized CDS View are good

```
CLASS zcl_demo_amdp DEFINITION

  PUBLIC

  FINAL

  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES if_amdp_marker_hdb .

    TYPES: BEGIN OF ty_test,

             mandt TYPE mandt,

             bukrs TYPE bukrs,

             belnr TYPE belnr_d,

             gjahr TYPE gjahr,

             docln TYPE docln,

           END OF   ty_test.

    TYPES: tt_test TYPE STANDARD TABLE OF ty_test.

    CLASS-METHODS:

      get_CDS  AMDP OPTIONS CDS SESSION CLIENT current

               EXPORTING VALUE(tt_return) TYPE tt_test .

  PROTECTED SECTION.

  PRIVATE SECTION.

ENDCLASS.

CLASS zcl_demo_amdp IMPLEMENTATION.

  METHOD get_CDS BY DATABASE PROCEDURE

                 FOR HDB LANGUAGE SQLSCRIPT

                 OPTIONS READ-ONLY  USING i_journalentryitem .

    TT_RETURN = SELECT MANDT                    AS MANDT,

                       CompanyCode              AS BUKRS,

                       AccountingDocument       AS BELNR,

                       FiscalYear               AS GJAHR,

                       LedgerGLLineItem         AS DOCLN

            FROM I_JournalEntryItem;

  ENDMETHOD.

ENDCLASS.
```

**AMDP OPTIONS CDS SESSION CLIENT current** is very important, With this statement, the system will only get the correct data of the current client

Yeah, we have successfully used CDS view inside AMDP Procedure, I hope it can help you!!!

If this blog is good, please like and share it. If you don't understand something, please leave a comment in the article.

Thanks so much.

* [abap amdp](/t5/tag/abap%20amdp/tg-p/board-id/erp-blog-members)
* [amdp](/t5/tag/amdp/tg-p/board-id/erp-blog-members)
* [CDS](/t5/tag/CDS/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fconsume-cds-view-inside-amdp-procedure%2Fba-p%2F13565767%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [How SAP’s ABAP Cloud Partner Reference App Simplifies Multi-Tenant Side-by-Side Extensions on BTP](/t5/enterprise-resource-planning-blog-posts-by-sap/how-sap-s-abap-cloud-partner-reference-app-simplifies-multi-tenant-side-by/ba-p/14223705)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [How to Add a Custom OData Field to a Smart Form in Fiori App F1511 using an Adaptation Project?](/t5/enterprise-resource-planning-q-a/how-to-add-a-custom-odata-field-to-a-smart-form-in-fiori-app-f1511-using-an/qaq-p/14207605)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a month ago
* [Unpacking the new SAP Business Suite](/t5/enterprise-resource-planning-blog-posts-by-sap/unpacking-the-new-sap-business-suite/ba-p/14191891)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Aug 26
* [Build A Web App and Connect to S/4HANA with SAP Integration Suite](/t5/enterprise-resource-planning-blog-posts-by-members/build-a-web-app-and-connect-to-s-4hana-with-sap-integration-suite/ba-p/14179607)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  2025 Aug 13
* [Navigating the Labyrinth: Choosing the Right Persistent Data Storage for Your Custom Development](/t5/enterprise-resource-planning-blog-posts-by-members/navigating-the-labyrinth-choosing-the-right-persistent-data-storage-for/ba-p/14133660)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  2025 Jul 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/vi...
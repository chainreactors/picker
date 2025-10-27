---
title: Consume CDS View inside CDS Table Function by using AMDP
url: https://blogs.sap.com/2022/12/03/consume-cds-view-inside-cds-table-function-by-using-amdp/
source: SAP Blogs
date: 2022-12-04
fetch_date: 2025-10-04T00:28:50.138015
---

# Consume CDS View inside CDS Table Function by using AMDP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Consume CDS View inside CDS Table Function by usin...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162791&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Consume CDS View inside CDS Table Function by using AMDP](/t5/technology-blog-posts-by-members/consume-cds-view-inside-cds-table-function-by-using-amdp/ba-p/13565733)

![chau1995](https://avatars.profile.sap.com/1/8/id186df8aa26624d10502d6761be8fc5c3f99a26f958b84af86b163dcb2b147279_small.jpeg "chau1995")

[chau1995](https://community.sap.com/t5/user/viewprofilepage/user-id/526082)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162791)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162791)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565733)

‎2022 Dec 03
3:26 AM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162791/tab/all-users "Click here to see who gave kudos to this post.")

12,534

* SAP Managed Tags
* [ABAP Connectivity](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Connectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [ABAP Connectivity

  Programming Tool](/t5/c-khhcw49343/ABAP%2BConnectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (4)

We are familiar with getting data from a table using AMDP procedure or AMDP table function. But, how about CDS View, I tried a case and got the following error

![](/legacyfs/online/storage/blog_attachments/2022/12/demo_000.png)

Basically, AMDP will get data from database, and it will get all client (assume your system have several clients), that is a reason why you catch this error when working with CDS view.

So, how to resolve it? Please read this article with me.

**Prerequsites**:

ABAP 7.55 or newer for using view entity. In case of using CDS DDIC View, don’t worry it

A little bit CDS View and AMDP. If you don’t have any experience, please follow link:

<https://blogs.sap.com/2020/08/25/first-program-with-amdp-method/>

**Solution**

**Step 1**: Create CDS View:

![](/legacyfs/online/storage/blog_attachments/2022/12/demo_001.png)

```
@AbapCatalog.viewEnhancementCategory: [#NONE]

@AccessControl.authorizationCheck: #CHECK

@EndUserText.label: 'Demo CDS View'

@Metadata.ignorePropagatedAnnotations: true

@ObjectModel.usageType:{

    serviceQuality: #X,

    sizeCategory: #S,

    dataClass: #MIXED

}

define view entity zchau_acdoca as select from I_JournalEntryItem {

    key CompanyCode             as BUKRS,

    key AccountingDocument      as BELNR,

    key FiscalYear              as GJAHR,

    key LedgerGLLineItem        as DOCLN,

        GLAccount               as RACCT,

        CostCenter              as RCNTR,

        ProfitCenter            as PRCTR

}

where SourceLedger = '0L' and Ledger = '0L'
```

**Step 2**: Create CDS Table function

![](/legacyfs/online/storage/blog_attachments/2022/12/demo_002.png)

```
@EndUserText.label: 'Demo CDS Table function'

@ClientHandling.type: #CLIENT_DEPENDENT

@ClientHandling.algorithm: #SESSION_VARIABLE

define table function zchau_cds_001 with parameters

    @Environment.systemField: #CLIENT

    p_date: mandt

returns {

  key CLIENT     : abap.clnt;

  key RBUKRS     : bukrs;

  key DOC_NUM    : belnr_d;

  key GJAHR      : gjahr;

  key DOCLN      : docln6;

      RACCT      : racct;

      RCNTR      : kostl;

      PRCTR      : prctr;

}

implemented by method ZCL_DEMO_AMDP=>GET_ACDOCA;
```

We need declare Client by adding annotation to this CDS View, If you don’t do it, you can’t create AMDP to consume CDS View. These annotations are very important

**Step 3:** Create Class to consume CDS View

We will create Global Class and handle method to get data from CDS View which was created in step 1

![](/legacyfs/online/storage/blog_attachments/2022/12/demo_003.png)

```
CLASS zcl_demo_amdp DEFINITION

  PUBLIC

  FINAL

  CREATE PUBLIC .

  PUBLIC SECTION.

    INTERFACES if_amdp_marker_hdb .

    CLASS-METHODS:

      get_acdoca     FOR TABLE FUNCTION zchau_cds_001.

  PROTECTED SECTION.

  PRIVATE SECTION.

ENDCLASS.

CLASS zcl_demo_amdp IMPLEMENTATION.

  METHOD get_acdoca BY DATABASE FUNCTION FOR HDB LANGUAGE SQLSCRIPT OPTIONS READ-ONLY USING zchau_acdoca.

    RETURN SELECT _raw.mandt as client,

            _raw.bukrs as rbukrs,

            _raw.belnr as doc_num,

            _raw.gjahr as gjahr,

            _raw.docln as docln,

            _raw.RACCT as RACCT,

            _raw.RCNTR as RCNTR,

            _raw.PRCTR as PRCTR

     from zchau_acdoca as _raw;

  endmethod.

ENDCLASS.
```

**Result**:

Run CDS Table Function and you will see data is shown

![](/legacyfs/online/storage/blog_attachments/2022/12/demo_004.png)

That's right, we have successfully used CDS view inside a CDS View table function, I hope it can help you!!!

If this blog is good, please like and share it. If you don't understand something, please leave a comment in the article.

Thanks so much!!!

* [abap amdp](/t5/tag/abap%20amdp/tg-p/board-id/technology-blog-members)
* [amdp](/t5/tag/amdp/tg-p/board-id/technology-blog-members)
* [CDS](/t5/tag/CDS/tg-p/board-id/technology-blog-members)
* [cds table function](/t5/tag/cds%20table%20function/tg-p/board-id/technology-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fconsume-cds-view-inside-cds-table-function-by-using-amdp%2Fba-p%2F13565733%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Service and Asset Manager 2405 - MDK Metadata Deployment Error in SAP BAS Environment](/t5/technology-q-a/sap-service-and-asset-manager-2405-mdk-metadata-deployment-error-in-sap-bas/qaq-p/14231957)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Tuesday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Goodbye Vibe-Coding: The Future of SAP Development with...
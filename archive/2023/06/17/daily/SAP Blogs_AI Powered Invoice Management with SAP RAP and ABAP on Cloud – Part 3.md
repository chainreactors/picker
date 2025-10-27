---
title: AI Powered Invoice Management with SAP RAP and ABAP on Cloud – Part 3
url: https://blogs.sap.com/2023/06/16/ai-powered-invoice-management-with-sap-rap-and-abap-on-cloud-part-3/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:47:18.462288
---

# AI Powered Invoice Management with SAP RAP and ABAP on Cloud – Part 3

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* AI Powered Invoice Management with SAP RAP and ABA...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162241&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [AI Powered Invoice Management with SAP RAP and ABAP on Cloud – Part 3](/t5/technology-blog-posts-by-members/ai-powered-invoice-management-with-sap-rap-and-abap-on-cloud-part-3/ba-p/13562298)

![sabarna17](https://avatars.profile.sap.com/6/f/id6f95e54989e9420a7c74c3bb9b65026c71e38b140551079234b6357e877c9d01_small.jpeg "sabarna17")

[sabarna17](https://community.sap.com/t5/user/viewprofilepage/user-id/147402)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162241)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162241)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562298)

‎2023 Jun 16
12:20 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162241/tab/all-users "Click here to see who gave kudos to this post.")

1,473

* SAP Managed Tags
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP AI Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Services/pd-p/73555000100700001042)
* [SAP Document AI](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520AI/pd-p/73554900100800002861)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP AI Services

  Software Product](/t5/c-khhcw49343/SAP%2BAI%2BServices/pd-p/73555000100700001042)
* [SAP Document AI

  SAP AI Services](/t5/c-khhcw49343/SAP%2BDocument%2BAI/pd-p/73554900100800002861)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

View products (6)

## All Blogs in this Series -

### [AI Powered Invoice Management with SAP RAP and ABAP on Cloud](https://blogs.sap.com/2023/06/16/ai-powered-invoice-management-with-sap-rap-and-abap-on-cloud/)

### [AI Powered Invoice Management with SAP RAP and ABAP on Cloud – Part 1](https://blogs.sap.com/2023/06/16/ai-powered-invoice-management-with-sap-rap-and-abap-on-cloud-part-1/)

### [AI Powered Invoice Management with SAP RAP and ABAP on Cloud – Part 2](https://blogs.sap.com/2023/06/16/ai-powered-invoice-management-with-sap-rap-and-abap-on-cloud-part-2/)

### [AI Powered Invoice Management with SAP RAP and ABAP on Cloud – Part 3](https://blogs.sap.com/2023/06/16/ai-powered-invoice-management-with-sap-rap-and-abap-on-cloud-part-3/)

If you want to know the reference of this blog, please go through the Part 1 & Part 2 sections of this AI Powered Invoice Management Series.

This is going to be the last part of the AI Powered Invoice Management Series. What we are focusing here is -

1. Creating a Unmanaged scenario

2. Creation of a ABAP Workflow

3. Creation of a NodeJS based Wrapper on top of the ABAP Unmanaged API

## Process Flow

![](/legacyfs/online/storage/blog_attachments/2023/06/Architecture-2.jpg)

## On-premise developments ( Create RAP Unmanaged API )

Create a custom table -

![](/legacyfs/online/storage/blog_attachments/2023/06/On-premise-1.jpg)

Create CDS Entity

```
@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'Interface of WF Trigger'

define root view entity Z_I_INV_PO_WF

 as select from

// zinv_po_status

 ekko left outer join

 zinv_po_status on ekko.ebeln = zinv_po_status.ebeln

{

// key ekko.ebeln,

 key zinv_po_status.ebeln,

 zinv_po_status.amount,

 zinv_po_status.status

}
```

Create a Projection view -

```
@EndUserText.label: 'Peojection view for INV PO WF'

@AccessControl.authorizationCheck: #NOT_REQUIRED

define root view entity Z_P_INV_PO_WF

provider contract transactional_query

as projection on Z_I_INV_PO_WF {

 key ebeln,

 amount,

 status

}
```

Create Behavior Definition -

```
unmanaged

implementation in class zbp_i_inv_po_wf unique;

define behavior for Z_I_INV_PO_WF

{

 create;

}

projection;

//strict;

define behavior for Z_P_INV_PO_WF //alias <alias_name>

{

 use create;

// use update;

// use delete;

}
```

Implement the Behavior class

```
CLASS lhc_z_i_inv_po_wf DEFINITION INHERITING FROM

cl_abap_behavior_handler.

 PRIVATE SECTION.

 METHODS create FOR MODIFY

 IMPORTING entities FOR CREATE z_i_inv_po_wf.

 METHODS read FOR READ

 IMPORTING keys FOR READ z_i_inv_po_wf RESULT result.

ENDCLASS.

CLASS lhc_z_i_inv_po_wf IMPLEMENTATION.

 METHOD create.

 DATA: ls_line TYPE zinv_po_status,

 lt_lines TYPE TABLE OF zinv_po_status.

 LOOP AT entities ASSIGNING FIELD-SYMBOL(<ls_entity>).

 ls_line = CORRESPONDING #( <ls_entity> ).

 APPEND ls_line TO lt_lines.

 DATA : lv_objectkey TYPE swr_struct-object_key.

 DATA: lt_input_container TYPE TABLE OF swr_cont,

 lv_subrc TYPE sy-subrc,

 lv_value TYPE swe_evtid,

 lt_msglns TYPE TABLE OF swr_messag,

 lt_msgstr TYPE TABLE OF swr_mstruc.

 lv_objectkey = ls_line-ebeln.

 lt_input_container = VALUE #( ( element = 'PurchasingDocument'

value = ls_line-ebeln ) ( element = 'TargetValue' value = ls_lineamount ) ).

 CALL FUNCTION 'SAP_WAPI_CREATE_EVENT' STARTING NEW TASK

lv_objectkey

 EXPORTING

 object_type = 'ZINV_PUORD'

 object_key = lv_objectkey

 event = 'PROCESS_PAY_FOR_INV'

 TABLES

 input_container = lt_input_container

 message_lines = lt_msglns

 message_struct = lt_msgstr.

 ENDLOOP.

 zcl_inv_payment=>update_table( it_table = lt_lines ).

 ENDMETHOD.

 METHOD read.

 ENDMETHOD.

ENDCLASS.

CLASS lsc_z_i_inv_po_wf DEFINITION INHERITING FROM

cl_abap_behavior_saver.

 PROTECTED SECTION.

 METHODS finalize REDEFINITION.

 METHODS check_before_save REDEFINITION.

 METHODS save REDEFINITION.

 METHODS cleanup REDEFINITION.

 METHODS cleanup_finalize REDEFINITION.

ENDCLASS.

CLASS lsc_z_i_inv_po_wf IMPLEMENTATION.

 METHOD finalize.

 ENDMETHOD.

 METHOD check_before_save.

 ENDMETHOD.

 METHOD save.

 ENDMETHOD.

 METHOD cleanup.

 ENDMETHOD.

 METHOD cleanup_finalize.

 ENDMETHOD.

ENDCLASS.
```

## On-premise developments ( Workflow Developments )

Create a basic workflow -

![](/legacyfs/online/storage/blog_attac...
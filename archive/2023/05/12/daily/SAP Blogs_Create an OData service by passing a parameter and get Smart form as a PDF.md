---
title: Create an OData service by passing a parameter and get Smart form as a PDF
url: https://blogs.sap.com/2023/05/11/create-an-odata-service-by-passing-a-parameter-and-get-smart-form-as-a-pdf/
source: SAP Blogs
date: 2023-05-12
fetch_date: 2025-10-04T11:39:33.047355
---

# Create an OData service by passing a parameter and get Smart form as a PDF

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Create an OData service by passing a parameter and...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68551&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create an OData service by passing a parameter and get Smart form as a PDF](/t5/enterprise-resource-planning-blog-posts-by-members/create-an-odata-service-by-passing-a-parameter-and-get-smart-form-as-a-pdf/ba-p/13570686)

![Jeevitha](https://avatars.profile.sap.com/6/a/id6a62e5567d1e575728dfc52f7cb94db7b39350772a0e21038c2242f73f6f1273_small.jpeg "Jeevitha")

[Jeevitha](https://community.sap.com/t5/user/viewprofilepage/user-id/126301)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68551)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68551)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570686)

‎2023 May 11
7:26 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68551/tab/all-users "Click here to see who gave kudos to this post.")

25,616

* SAP Managed Tags
* [Media](https://community.sap.com/t5/c-khhcw49343/Media/pd-p/46151026338704711996502)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [Media

  Industry](/t5/c-khhcw49343/Media/pd-p/46151026338704711996502)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)

View products (4)

Introduction

This blog shows the gateway project using OData service to obtain an output as a PDF by using Smart form. The objective is to pass the parameter as input and obtain an output as a PDF using Smart Form.

**Requirement:** Pass the Invoice Document number (Belnr) as input and obtain Plant, Purchase document number, Item number, Fiscal year, Material Number, and Reference number as an output through OData Service by using the smart form.

* Below structure is used as a sample source of our data model.

![](/legacyfs/online/storage/blog_attachments/2023/05/1-12.png)

* To create an OData service go to SAP Gateway Service Builder (transaction SEGW). Below I made an OData service named ZDEMO\_ODATA\_01 and saved it in the Local object.

![](/legacyfs/online/storage/blog_attachments/2023/05/2-4.png)

* Create a data model by importing DDIC structure ‘ZDEMO\_STR\_01’.

![](/legacyfs/online/storage/blog_attachments/2023/05/3-7.png)

* Select the required fields, set the primary key, and click Finish. Below I take Belnr as a key.

![](/legacyfs/online/storage/blog_attachments/2023/05/4-4.png)

* The entity types and entity sets will be created. Make sure the Media button in the entity type is enabled.

![](/legacyfs/online/storage/blog_attachments/2023/05/5-6.png)

* Generate the OData project and save it in a local object.

![](/legacyfs/online/storage/blog_attachments/2023/05/6-6.png)

* Go to RUNTIME ARTIFACTS => ZCL\_ZDEMO\_ODATA\_01\_DPC\_EXT. Redefine the method named **/IWBEP/IF\_MGW\_APPL\_SRV\_RUNTIME~GET\_STREAM.**

![](/legacyfs/online/storage/blog_attachments/2023/05/8-7.png)

* By using **IT\_KEY\_TAB,** Fetch the Invoice document number given by the user. Using That, Fetch data from the Database table and move it to the Overall structure.

```
    DATA: ls_str     TYPE zdemo_str_01,

          ls_str_itm TYPE zdemo_str_02.

    IF it_key_tab IS NOT INITIAL.

      DATA(lv_key_tab) = VALUE #( it_key_tab[ 1 ]-value ).

      SELECT belnr, gjahr, buzei,

             ebeln, matnr, werks,

             xblnr

        FROM rseg

        INTO TABLE @DATA(lt_ztab)

             WHERE belnr = @lv_key_tab.

      IF lt_ztab IS NOT INITIAL.

        DATA(ls_header) = VALUE #( lt_ztab[ 1 ] ).

        ls_str-invoicedocnum = ls_header-belnr.

        ls_str-plant         = ls_header-werks.

        LOOP AT lt_ztab INTO DATA(ls_ztab).

          ls_str_itm-purdocnum = ls_ztab-ebeln.

          ls_str_itm-fisyear   = ls_ztab-gjahr.

          ls_str_itm-itemcode  = ls_ztab-buzei.

          ls_str_itm-material  = ls_ztab-matnr.

          ls_str_itm-refnumber =  ls_ztab-xblnr.

          APPEND ls_str_itm TO ls_str-item.

          CLEAR ls_str_itm.

        ENDLOOP.

	     ENDIF.

    ENDIF.
```

* Call smart form **ZDEMO\_SFM\_01** by using Function module **SSF\_FUNCTION\_MODULE\_NAME**.

```
    DATA: lv_fm_name   TYPE rs38l_fnam,

          ls_cntl_prmt TYPE ssfctrlop,

          ls_op_opt    TYPE ssfcompop,

          ls_ssfcrescl TYPE ssfcrescl.

        CALL FUNCTION 'SSF_FUNCTION_MODULE_NAME'

          EXPORTING

            formname           = 'ZDEMO_SFM_01'

*           VARIANT            = ' '

*           DIRECT_CALL        = ' '

          IMPORTING

            fm_name            = lv_fm_name

          EXCEPTIONS

            no_form            = 1

            no_function_module = 2

            OTHERS             = 3.

        IF sy-subrc <> 0.

* Implement suitable error handling here

        ENDIF.

        ls_cntl_prmt-langu  = 'EN'.

        ls_cntl_prmt-getotf = abap_true.

        ls_cntl_prmt-preview = space.

        ls_cntl_prmt-no_dialog = abap_true.

        ls_op_opt-tddest    = 'LOCL'.

        ls_op_opt-xdfcmode  = abap_true.

        ls_op_opt-tdnewid   = abap_true.

        ls_op_opt-tdimmed   = abap_true.

        CALL FUNCTION lv_fm_name "'/1BCDWB/SF00000080'

          EXPORTING

            control_parameters = ls_cntl_prmt

            output_options     = ls_op_opt

            user_settings      = 'X'

            e_structure        = ls_str

          IMPORTING

*           DOCUMENT_OUTPUT_INFO       =

            job_output_info    = ls_ssfcrescl

*           JOB_OUTPUT_OPTIONS =

          EXCEPTIONS

            formatting_error   = 1

            internal_error     = 2

            send_error         = 3

            user_canceled      = 4

            OTHERS             = 5.

        IF sy-subrc <> 0.

* Implement suitable error handling here

        ENDIF.
```

* Convert the OTF file to a PDF file using the function module **CONVERT\_OTF**.

```
        DATA: lt_otf      TYPE TABLE OF itcoo,

              lv_bin_file TYPE xstring,

              lt_lines    TYPE TABLE OF tline,

              gs_stream   TYPE ty_s_media_resource.

        REFRESH lt_otf[].

        lt_otf[] = ls_ssfcrescl-otfdata[].

        CLEAR : lv_bin_file.

        CALL FUNCTION 'CONVERT_OTF'

          EXPORTING

            format                = 'PDF'

          IMPORTING

            bin_file              = lv_bin_file

          TABLES

            otf                   = lt_otf

            lines                 = lt_line...
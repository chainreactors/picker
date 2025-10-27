---
title: Automate printing of PDF documents received as email attachments in SAP
url: https://blogs.sap.com/2022/12/29/automate-printing-of-pdf-documents-received-as-email-attachments-in-sap/
source: SAP Blogs
date: 2022-12-30
fetch_date: 2025-10-04T02:44:14.948846
---

# Automate printing of PDF documents received as email attachments in SAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Automate printing of PDF documents received as ema...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161948&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Automate printing of PDF documents received as email attachments in SAP](/t5/technology-blog-posts-by-members/automate-printing-of-pdf-documents-received-as-email-attachments-in-sap/ba-p/13560539)

![yashoratna](https://avatars.profile.sap.com/c/4/idc4520ad6d4465fd45c038a2900b06cfb64d7202c13b5b692b5553c650090dcdd_small.jpeg "yashoratna")

[yashoratna](https://community.sap.com/t5/user/viewprofilepage/user-id/16294)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161948)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161948)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560539)

‎2022 Dec 29
9:54 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161948/tab/all-users "Click here to see who gave kudos to this post.")

5,503

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [NW ABAP Print and Output Management](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Print%2520and%2520Output%2520Management/pd-p/334558737810127171897316045257708)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [NW ABAP Print and Output Management

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BPrint%2Band%2BOutput%2BManagement/pd-p/334558737810127171897316045257708)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

**Summary :** In my [previous blog](https://blogs.sap.com/2022/12/29/save-incoming-e-mail-attachments-in-sap-and-auto-print-on-printer/) I have covered, how to process/save pdf documents (can have multiple) which are received in e-mail into SAP. In this blog, we will see how we can enable auto print functionality for PDF documents on dedicated physical printer or on local printer (LP01) in spool.

Additional Business requirement : All the PDF documents (if there are multiple attachments in e-mail) should get generated as one PDF in spool and in case of two-sided printing, one documents shouldn't get printed on back side of another one.

As per previous article, we have already implemented the two methods of Interface IF\_INBOUND\_EXIT\_BCS in inbound Exit(Z-class : ZCL\_BILLING\_EMAIL\_IN).

**Method : IF\_INBOUND\_EXIT\_BCS~CREATE\_INSTANCE** (Same as previous article)

```
*Create instance of the object with the class itself

    DATA(lo_ref_instance) = NEW zcl_billing_email_in( ).

    IF lo_ref_instance IS BOUND.

      ro_ref = lo_ref_instance.

    ENDIF.
```

**Method : IF\_INBOUND\_EXIT\_BCS~PROCESS\_INBOUND**

We need to write code in 2nd method of the interface to implement the printing functionality as per below code snippet with following steps.

1. Get the PDF documents (hex format) from the e-mail object

2. Convert hex format into XSTRING format

3. Get total no. of pages in each PDF document and identify if total no of pages are odd : Method - GET\_TOTAL\_PAGES.

4. Add additional blank page in PDF document if total no of pages are odd to avoid any issue in case of two sided printing. (Additional requirement) : Method - GET\_BLANK\_PDF\_PAGE

5. Merge all the XSTRING data

6. Print PDF document on printer : Method - PRINT\_PDF\_DOC

```
    CONSTANTS: lc_pdf TYPE char3 VALUE 'PDF'.        "Document Type PDF

    DATA: lv_printer      TYPE rspopshort,                "Spool: short name for output device

          lv_blank_page   TYPE xstring,

          lv_total_pages  TYPE i.

    CLEAR: e_retcode, es_t100msg.

lv_printer = 'LP01'. "Or any physical printer in SAP but with short name

*Extract Attachment from e-mail

    TRY .

        IF io_sreq IS BOUND.

* Get document

          DATA(lo_ref_document) = io_sreq->get_document( ).

          IF lo_ref_document IS BOUND.

* Find all the PDF attachments and process it.

              TRY.

* Create PDF Merge Object to be printed in spool as one document

                    TRY.

                        DATA(lo_ref_pdf_merger) = NEW cl_rspo_pdf_merge( ).

                      CATCH cx_rspo_pdf_merge INTO DATA(lv_merge_ex).

                    ENDTRY.

                    DO lo_ref_document->get_body_part_count( ) TIMES.

                      TRY.

                          DATA(lv_doc_type) = lo_ref_document->get_body_part_attributes( im_part = sy-index )-doc_type.

                          TRANSLATE lv_doc_type TO UPPER CASE.

* If Document type is PDF then only proceed as program needs to look into PDF attachments only

                          IF lv_doc_type = lc_pdf.

* Get the file name of attached document

                            DATA(lv_filename) = lo_ref_document->get_body_part_attributes( im_part = sy-index  )-filename.

* Get the content of attached file in hex format.

                            DATA(ls_body_part_content) = lo_ref_document->get_body_part_content( sy-index ).

                            IF lv_filename IS NOT INITIAL AND ls_body_part_content IS NOT INITIAL.

		      TRY.

*Convert Hex data into Xstring

                        CALL METHOD cl_bcs_convert=>xtab_to_xstring

                           EXPORTING

                              it_xtab    = iv_body_part_content-cont_hex

                           RECEIVING

                              rv_xstring = DATA(lv_xstring).

                      CATCH cx_bcs .

                         continue.

                      ENDTRY.

                              IF lv_xstring IS NOT INITIAL.

                                IF lo_ref_pdf_merger IS BOUND.

                                  lo_ref_pdf_merger->add_document( lv_xstring ).

                                ENDIF.

* Get total no of pages in PDF document

                                CALL METHOD me->get_total_pages

                                  EXPORTING

                                    iv_content   = lv_xstring

                                  IMPORTING

                                    ev_pages     = DATA(lv_pages)

                                    ev_odd_pages = DATA(lv_odd_flag).

                                lv_total_pages = lv_total_pages + lv_pages.

                                IF lv_odd_flag EQ abap_true.

* If there is odd number of pages, then add one blank PDF page at the end to avoid back to back printing

                                  IF lv_blank_page IS INITIAL.

                                    CALL METHOD me->get_blank_pdf_page

                                      IMPORTING

                                        ev_blank_content = lv_blank_page.

                                  ENDIF.

                                  IF lv_blank_page IS NOT INITIAL.

* Mer...
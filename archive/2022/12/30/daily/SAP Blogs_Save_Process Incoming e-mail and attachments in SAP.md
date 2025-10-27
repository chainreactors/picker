---
title: Save/Process Incoming e-mail and attachments in SAP
url: https://blogs.sap.com/2022/12/29/save-incoming-e-mail-attachments-in-sap-and-auto-print-on-printer/
source: SAP Blogs
date: 2022-12-30
fetch_date: 2025-10-04T02:44:41.915579
---

# Save/Process Incoming e-mail and attachments in SAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Save/Process Incoming e-mail and attachments in SA...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67490&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Save/Process Incoming e-mail and attachments in SAP](/t5/enterprise-resource-planning-blog-posts-by-members/save-process-incoming-e-mail-and-attachments-in-sap/ba-p/13556119)

![yashoratna](https://avatars.profile.sap.com/c/4/idc4520ad6d4465fd45c038a2900b06cfb64d7202c13b5b692b5553c650090dcdd_small.jpeg "yashoratna")

[yashoratna](https://community.sap.com/t5/user/viewprofilepage/user-id/16294)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67490)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67490)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556119)

‎2022 Dec 29
2:41 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67490/tab/all-users "Click here to see who gave kudos to this post.")

6,532

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Customer Relationship Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Relationship%2520Management/pd-p/01200615320800000556)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)

* [SAP Customer Relationship Management

  SAP Customer Relationship Management](/t5/c-khhcw49343/SAP%2BCustomer%2BRelationship%2BManagement/pd-p/01200615320800000556)
* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

Summary: This blog post will demonstrate how to handle incoming email with PDF attachments and save them against any transaction in SAP.

We will use GOS functionality to save the document but same kind of logiccan be used to save/process the attachments in the SAP system. I am taking an example of CRM billing document here.

(Since there is no designated space in CRM billing to store documents at the transaction level, we chosen to enable the GOS toolbar and save all transaction-related attachments there. For more information, see my blog post [Generic Object Services (GOS) toolbar in CRM Billing](https://blogs.sap.com/2022/09/28/generic-object-services-gos-toolbar-in-crm-billing/).)

First, we must confirm that the specified email domain is permitted by the T-code SCOT's settings for Inbound Messages. (Here it is \*, which denotes that it accepts all.)

![](/legacyfs/online/storage/blog_attachments/2022/12/SCOT_Settings.png)

In next step, under Inbound processing, enter recipient address ( generally it should be unique system address and should connect basis/security team before putting any email address over here, Just to demonstrate the solution, I am putting specific email ID), Exit Name ( Z-class ), calling sequence and save.

![](/legacyfs/online/storage/blog_attachments/2022/12/Inbound-Processings.png)

Now create same exit (class) in T-code SE24 and with interface IF\_INBOUND\_EXIT\_BCS.

![](/legacyfs/online/storage/blog_attachments/2022/12/Exit-Name.png)

Next implement both methods coming from interface as per below code snippet.

Method : IF\_INBOUND\_EXIT\_BCS~CREATE\_INSTANCE

```
*Create instance of the object with the class itself

    DATA(lo_ref_instance) = NEW zcl_billing_email_in( ).

    IF lo_ref_instance IS BOUND.

      ro_ref = lo_ref_instance.

    ENDIF.
```

Method : IF\_INBOUND\_EXIT\_BCS~PROCESS\_INBOUND

In order to read/parse the data and identify the transaction to work on, we requested that the sender provide a reference number in SAP (in this case, the CRM billing document) in the subject line.

```
  METHOD if_inbound_exit_bcs~process_inbound.

    CONSTANTS: lc_pdf               TYPE char3 VALUE 'PDF',        "Document Type PDF

               lc_hyphen            TYPE char01 VALUE '-'.

    DATA: lv_official_doc TYPE itl_official_docno.        "Billing Official Document

    CLEAR: e_retcode, es_t100msg.

*Extract Attachment from e-mail

    TRY .

        IF io_sreq IS BOUND.

* Get document

          DATA(lo_ref_document) = io_sreq->get_document( ).

          IF lo_ref_document IS BOUND.

* Get subject line of the e-mail

            SPLIT lo_ref_document->get_subject( ) AT lc_hyphen INTO DATA(lv_doc1) lv_official_doc.

* Find all the PDF attachments and process it.

            lv_official_doc = shift_left( lv_official_doc ).

            IF lv_official_doc IS NOT INITIAL.

* Extract all the billing details from official document in respect to billing

              TRY.

                  IF lv_billing_doc IS NOT INITIAL.

                    DO lo_ref_document->get_body_part_count( ) TIMES.

                      TRY.

                          DATA(lv_doc_type) = lo_ref_document->get_body_part_attributes( im_part = sy-index )-doc_type.

                          TRANSLATE lv_doc_type TO UPPER CASE.

* If Document type is PDF then only proceed as program needs to look into PDF attachments only

                          IF lv_doc_type = lc_pdf.

                            DATA(lv_pdffound_flag) = abap_true.

* Get the file name of attached document

                            DATA(lv_filename) = lo_ref_document->get_body_part_attributes( im_part = sy-index  )-filename.

* Get the content of attached file in hex format.

                            DATA(ls_body_part_content) = lo_ref_document->get_body_part_content( sy-index ).

                            IF lv_filename IS NOT INITIAL AND ls_body_part_content IS NOT INITIAL.

* Attach PDF documents against Billing document which would be shown under attachments section in GOS toolbar

                              CALL METHOD me->attach_docs_in_billing

                                EXPORTING

                                  iv_body_part_content = ls_body_part_content

                                  iv_billing_doc       = lv_billing_doc

                                  iv_objtype           = lv_objtype

                                  iv_filename          = lv_filename

                                IMPORTING

                                  ev_data_xstring      = DATA(lv_xstring).

                            ENDIF.

                          ENDIF.

                        CATCH cx_document_bcs.

                          CONTINUE.

                      ENDTRY.

                      CLEAR: lv_xstring,ls_body_part_content,

                             lv_doc_type, lv_filename.

                    ENDDO.

                  ENDIF.

                CATCH cx_abap_error_analyze.

                  e_retcode  = if_inbound_exit_bcs=>gc_continue.

              ENDTRY.

            ENDIF.

          ENDIF.

        ENDIF.

      CATCH cx_os_object_not_found.

        e_retcode  = if_inbound_exit_bcs=>gc_continue.

    ENDTRY.

  ENDMETHOD...
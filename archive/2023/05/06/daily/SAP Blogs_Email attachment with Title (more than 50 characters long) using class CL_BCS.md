---
title: Email attachment with Title (more than 50 characters long) using class CL_BCS
url: https://blogs.sap.com/2023/05/05/email-attachment-with-title-more-than-50-characters-long-using-class-cl_bcs/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:15.990842
---

# Email attachment with Title (more than 50 characters long) using class CL_BCS

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Email attachment with Title (more than 50 characte...

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6366&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Email attachment with Title (more than 50 characters long) using class CL\_BCS](/t5/crm-and-cx-blog-posts-by-members/email-attachment-with-title-more-than-50-characters-long-using-class-cl-bcs/ba-p/13569279)

![yashoratna](https://avatars.profile.sap.com/c/4/idc4520ad6d4465fd45c038a2900b06cfb64d7202c13b5b692b5553c650090dcdd_small.jpeg "yashoratna")

[yashoratna](https://community.sap.com/t5/user/viewprofilepage/user-id/16294)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6366)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6366)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569279)

‎2023 May 05
10:56 PM

[6
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6366/tab/all-users "Click here to see who gave kudos to this post.")

4,094

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

**Introduction:** In this blog post we will see how we can have a file attachment title when it is over 50 characters long.

If we use the CL\_BCS class to build email functionality, we use the method ADD\_ATTACHMENT from the class CL\_DOCUMENT\_BCS to attach any document.

Generally, we pass all the mandatory importing parameters including (I\_ATTACHMENT\_SUBJECT) which build the attached document's title. And since this parameter can take up to 50 characters(data element SO\_OBJ\_DES), obviously it truncates to fit it within the limit.

```
lo_document_ref->add_attachment(

    EXPORTING

      i_attachment_type     = 'xls'

      i_attachment_subject  = CONV so_obj_des( 'Check if we can accommodate an Attachment file with more than 50 characters long' )

      i_attachment_size     = CONV so_obj_len( out_length )

      i_attachment_language = sy-langu

      i_att_content_hex     = it_binary_tab ).
```

![](/legacyfs/online/storage/blog_attachments/2023/05/Attachment-Title.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/Data-Type50-2.png)

So, when we trigger an e-mail, the attachment title will get truncated in SAP.

![](/legacyfs/online/storage/blog_attachments/2023/05/title-in-SAPPNG.png)

And same issue will be outside SAP too.

![](/legacyfs/online/storage/blog_attachments/2023/05/outside-SAP-wrong.png)

To extend the attachment title by more than 50 characters, we can leverage the optional importing parameter I\_ATTACHMENT\_HEADER in the same method ADD\_ATTACHMENT of the class CL\_DOCUMENT\_BCS.

And need to pass a blank( space ) in the mandatory importing parameter (I\_ATTACHMENT\_SUBJECT) when calling the attachment method.

```
  DATA(lt_atta_hdr) = VALUE soli_tab( ( line = 'Check if we can accommodate an Attachment file with more than 50 characters long.xlsx' ) ).

lo_document_ref->add_attachment(

    EXPORTING

      i_attachment_type     = 'xls'

      i_attachment_subject  = space

      i_attachment_size     = CONV so_obj_len( out_length )

      i_attachment_header   = lt_atta_hdr

      i_attachment_language = sy-langu

      i_att_content_hex     = it_binary_tab ).
```

Though there is no attachment Title in the SAP

![](/legacyfs/online/storage/blog_attachments/2023/05/Attach-title-in-SAP.png)

But outside of SAP, we can see an attachment title in its entirety and uncut.

![](/legacyfs/online/storage/blog_attachments/2023/05/Capture2.png)

Please refer to the detailed code logic below.

```
PARAMETERS : p_email TYPE ad_smtpadr.   "abc@gmail.com

DATA: e_xstring TYPE xstring,

      mt_data       TYPE REF TO data,

      out_length    TYPE i,

      it_binary_tab TYPE solix_tab.

FIELD-SYMBOLS <tab> TYPE ANY TABLE.

SELECT bname,

       persnumber,

       addrnumber

       FROM usr21

       INTO TABLE @DATA(lt_usr21)

       UP TO 20 ROWS.

IF sy-subrc EQ 0.

  GET REFERENCE OF lt_usr21 INTO mt_data.

  ASSIGN mt_data->* TO <tab>.

  TRY .

      cl_salv_table=>factory(

      EXPORTING

        list_display = abap_false

      IMPORTING

        r_salv_table = DATA(mo_salv_table)

      CHANGING

        t_table      = <tab> ).

    CATCH cx_salv_msg.

  ENDTRY.

  "get colums & aggregation infor to create fieldcat

  DATA(mo_columns)  = mo_salv_table->get_columns( ).

  DATA(mo_aggreg)   = mo_salv_table->get_aggregations( ).

  DATA(mt_fcat)     =  cl_salv_controller_metadata=>get_lvc_fieldcatalog(

                                r_columns      = mo_columns

                                r_aggregations = mo_aggreg ).

  IF cl_salv_bs_a_xml_base=>get_version( ) EQ if_salv_bs_xml=>version_25 OR

     cl_salv_bs_a_xml_base=>get_version( ) EQ if_salv_bs_xml=>version_26.

    DATA(mo_result_data) = cl_salv_ex_util=>factory_result_data_table(

         r_data                      = mt_data

         t_fieldcatalog              = mt_fcat

     ).

    CASE cl_salv_bs_a_xml_base=>get_version( ).

      WHEN if_salv_bs_xml=>version_25.

        DATA(lv_version) = if_salv_bs_xml=>version_25.

      WHEN if_salv_bs_xml=>version_26.

        lv_version = if_salv_bs_xml=>version_26.

    ENDCASE.

    DATA(m_file_type) = if_salv_bs_xml=>c_type_xlsx.

    DATA(m_flavour) = if_salv_bs_c_tt=>c_tt_xml_flavour_export.

    "transformation of data to excel

    cl_salv_bs_tt_util=>if_salv_bs_tt_util~transform(

      EXPORTING

        xml_type      = m_file_type

        xml_version   = lv_version

        r_result_data = mo_result_data

        xml_flavour   = m_flavour

        gui_type      = if_salv_bs_xml=>c_gui_type_gui

      IMPORTING

        xml           = e_xstring ).

    CALL FUNCTION 'SCMS_XSTRING_TO_BINARY'

      EXPORTING

        buffer        = e_xstring

      IMPORTING

        output_length = out_length

      TABLES

        binary_tab    = it_binary_tab.

  ENDIF.

ENDIF.

DATA(lo_send_request_ref) = cl_bcs=>create_persistent( ).

*Populate sender name

DATA(lo_sender_ref) = cl_sapuser_bcs=>create( sy-uname ).

IF lo_send_request_ref IS BOUND.

  IF lo_sender_ref IS BOUND.

*Add sender to send request

    lo_send_request_ref->set_sender(

      EXPORTING

        i_sender = lo_sender_ref ).

  ENDIF.

ENDIF.

DATA(lo_recipient_ref) = cl_cam_address_bcs=>create_internet_address( p_email ).

IF lo_re...
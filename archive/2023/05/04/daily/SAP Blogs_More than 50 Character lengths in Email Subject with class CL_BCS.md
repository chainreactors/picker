---
title: More than 50 Character lengths in Email Subject with class CL_BCS
url: https://blogs.sap.com/2023/05/03/more-than-50-character-lengths-in-email-subject-with-class-cl_bcs/
source: SAP Blogs
date: 2023-05-04
fetch_date: 2025-10-04T11:39:38.955008
---

# More than 50 Character lengths in Email Subject with class CL_BCS

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* More than 50 Character lengths in Email Subject wi...

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6290&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [More than 50 Character lengths in Email Subject with class CL\_BCS](/t5/crm-and-cx-blog-posts-by-members/more-than-50-character-lengths-in-email-subject-with-class-cl-bcs/ba-p/13557089)

![yashoratna](https://avatars.profile.sap.com/c/4/idc4520ad6d4465fd45c038a2900b06cfb64d7202c13b5b692b5553c650090dcdd_small.jpeg "yashoratna")

[yashoratna](https://community.sap.com/t5/user/viewprofilepage/user-id/16294)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6290)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6290)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557089)

‎2023 May 03
10:40 PM

[5
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6290/tab/all-users "Click here to see who gave kudos to this post.")

16,275

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

**Introduction**: In SAP, the email subject line is limited to 50 characters only, but there may be circumstances where we need to have the subject line more than that.

In this article, I'd cover how we can get rid of this restriction.

If we use the CL\_BCS class to build email functionality, we have the importing parameter (I\_SUBJECT) with the data element SO\_OBJ\_DES (which is 50 characters long and can be used up to that limit) when creating a document (Method CREATE\_DOCUMENT of class CL\_DOCUMENT\_BCS).

```
DATA(lo_document_ref) = cl_document_bcs=>create_document(

i_type    = lc_doc_type

i_text    = lt_content_txt

 i_subject = lv_subject ).
```

![](/legacyfs/online/storage/blog_attachments/2023/05/cl_document_bcs-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/Data-Type50-1.png)

When we trigger an e-mail, the subject will get truncated in SAP.

![](/legacyfs/online/storage/blog_attachments/2023/05/SAP-Email-before-change.png)

And same issue will be outside SAP too.

![](/legacyfs/online/storage/blog_attachments/2023/05/snap422.png)

To extend the e-mail subject by more than 50 characters, we can leverage the method **SET\_MESSAGE\_SUBJECT** of class **CL\_BCS**.

And need to pass a blank( space ) in the mandatory importing parameter (I\_SUBJECT) when creating the document reference.

DATA(lo\_document\_ref) = cl\_document\_bcs=>create\_document(
i\_type    = lc\_doc\_type
i\_text    = lt\_content\_txt
**i\_subject = space** ).

```
DATA(lo_send_request_ref) = cl_bcs=>create_persistent( ).

    lo_send_request_ref->set_message_subject(

      EXPORTING

        ip_subject = CONV string( lv_subject ) ).
```

Though there is no Doc. Title in the SAP

![](/legacyfs/online/storage/blog_attachments/2023/05/SAP-Email-after-change.png)

But outside of SAP, we can see a subject line in its entirety and uncut.

![](/legacyfs/online/storage/blog_attachments/2023/05/snap423.png)

Please refer to the detailed code logic below.

```
PARAMETERS : p_email TYPE ad_smtpadr.    "abc@gmail.com

DATA: lv_subject TYPE char100 VALUE

      'Action Required: Check if you can put more than 50 characters'.

DATA(lo_send_request_ref) = cl_bcs=>create_persistent( ).

*Populate sender name

DATA(lo_sender_ref) = cl_sapuser_bcs=>create( sy-uname ).

IF lo_send_request_ref IS BOUND.

  IF lo_sender_ref IS BOUND.

*Add sender to send request

   lo_send_request_ref->set_sender(

      EXPORTING

        i_sender = lo_sender_ref ).

* If need to send more than 50 characters in length as a subject line

* Then set message in cl_bcs->set_message_subject

* else populate it in method cl_document_bcs=>create_document

    lo_send_request_ref->set_message_subject(

      EXPORTING

        ip_subject = CONV string( lv_subject ) ).

  ENDIF.

ENDIF.

DATA(lo_recipient_ref) = cl_cam_address_bcs=>create_internet_address( p_email ).

IF lo_recipient_ref IS BOUND.

*Add recipient to send request

  lo_send_request_ref->add_recipient(

    EXPORTING

      i_recipient = lo_recipient_ref

      i_express   = abap_true ).

ENDIF.

DATA(lt_content_txt) = VALUE soli_tab( ( line = 'Hello Team,' )

      ( line = 'This e-mail has been automatically generated. Please do not reply to this e-mail.' )

      ( line = 'Thank You!' ) ).

* Create document for e-mail content

DATA(lo_document_ref) = cl_document_bcs=>create_document(

                                        i_type    = 'TXT'

                                        i_text    = lt_content_txt

*                                       i_subject = CONV so_obj_des( lv_subject ) ).

                                        i_subject = space ).

IF lo_document_ref IS BOUND.

* Add document to send request

  lo_send_request_ref->set_document( lo_document_ref ).

ENDIF.

* Set parameter to send e-mail immediately

lo_send_request_ref->set_send_immediately(

  EXPORTING

    i_send_immediately = abap_true ).

* Send email

DATA(lv_sent_to_all) = lo_send_request_ref->send( ).

* If e-mail is successful then do commit work

IF lv_sent_to_all = abap_true.

  COMMIT WORK AND WAIT.

ENDIF.
```

This concludes the functionality.

Thank you for reading the article. I hope you found it interesting. Please feel free to share your insightful observations and suggestions.

* [CL\_BCS OOABAP](/t5/tag/CL_BCS%20OOABAP/tg-p/board-id/crm-blog-members)
* [Email](/t5/tag/Email/tg-p/board-id/crm-blog-members)
* [EmailUsingOOPs](/t5/tag/EmailUsingOOPs/tg-p/board-id/crm-blog-members)

8 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fcrm-and-cx-blog-posts-by-members%2Fmore-than-50-character-lengths-in-email-subject-with-class-cl-bcs%2Fba-p%2F13557089%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [What is planned for the 2505 release of SAP Variant Configuration and Pricing?](/t5/crm-and-cx-blog-posts-by-sap/what-is-planned-for-the-2505-release-of-sap-variant-configuration-and/ba-p/14078774)
  in [CRM and...
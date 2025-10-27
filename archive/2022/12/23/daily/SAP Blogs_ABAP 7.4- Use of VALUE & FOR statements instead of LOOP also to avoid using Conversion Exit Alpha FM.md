---
title: ABAP 7.4- Use of VALUE & FOR statements instead of LOOP also to avoid using Conversion Exit Alpha FM
url: https://blogs.sap.com/2022/12/22/abap-7.4-use-of-value-for-statements-instead-of-loop-also-to-avoid-using-conversion-exit-alpha-fm/
source: SAP Blogs
date: 2022-12-23
fetch_date: 2025-10-04T02:19:53.621727
---

# ABAP 7.4- Use of VALUE & FOR statements instead of LOOP also to avoid using Conversion Exit Alpha FM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* ABAP 7.4- Use of VALUE & FOR statements instead of...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67413&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ABAP 7.4- Use of VALUE & FOR statements instead of LOOP also to avoid using Conversion Exit Alpha FM](/t5/enterprise-resource-planning-blog-posts-by-members/abap-7-4-use-of-value-for-statements-instead-of-loop-also-to-avoid-using/ba-p/13554959)

![shrikantpatil](https://avatars.profile.sap.com/9/f/id9f9118dd1b6a174a9b2e57588f7929f7f66ac1e64f49be61d6f733ef4f5039f3_small.jpeg "shrikantpatil")

[shrikantpatil](https://community.sap.com/t5/user/viewprofilepage/user-id/41482)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67413)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67413)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554959)

‎2022 Dec 22
1:57 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67413/tab/all-users "Click here to see who gave kudos to this post.")

8,288

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

The ABAPers journey is incomplete without where we need to process Excel file data for further processing. In my experience, it is mostly for BAPI development i.e. getting the data from an Excel file and converting it to a suitable form.

Earlier I was using Loop, Endloop statements, and CONVERSION\_EXIT\_ALPHA\_INPUT function module for the same. It was long and messy coding.

And now using ABAP7.4 using **VALUE** & **FOR** statements code started looking literally beautiful.

Below is a code snippet using ABAP 7.4

```
CALL FUNCTION 'TEXT_CONVERT_XLS_TO_SAP'

  EXPORTING

    i_line_header        = 'X'

    i_tab_raw_data       = gt_file

    i_filename           = p_file

  TABLES

    i_tab_converted_data = gt_data

  EXCEPTIONS

    conversion_failed    = 1

    OTHERS               = 2.

IF sy-subrc <> 0.

  MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno

          WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4.

ENDIF.

IF gt_data[] IS NOT INITIAL.

  DATA(gt_final) = VALUE tt_final( FOR ls_final IN gt_data (   bukrs    = ls_final-bukrs

                                                               ebeln    = |{ ls_final-ebeln ALPHA = IN }|

                                                               bsart    = ls_final-bsart

                                                               ernam    = ls_final-ernam

                                                               aedat    = ls_final-aedat

                                                               lifnr    = |{ ls_final-lifnr ALPHA = IN }|

                          ) ).

ENDIF.
```

The data declaration as per below.

```
TYPES: BEGIN OF gty_final,

         bukrs TYPE bukrs,

         ebeln TYPE ebeln,

         bsart TYPE esart,

         ernam TYPE ernam,

         aedat TYPE erdat,

         lifnr TYPE lifnr,

       END OF gty_final,

       tt_final TYPE STANDARD TABLE OF gty_final WITH DEFAULT KEY.

DATA: gt_file TYPE truxs_t_text_data,

      gt_data TYPE STANDARD TABLE OF gty_final.
```

Actually, I am still learning ABAP 7.4 and OOPs concepts while coding.

Your inputs are welcome & if you have any blogs to add more, please feel free to comment.

Also, FYI this is my first blog, so if you find anything unusual please say it so I can improve myself.

Thanks,

Shrikant Patil

* [abap7.4](/t5/tag/abap7.4/tg-p/board-id/erp-blog-members)
* [sap abap](/t5/tag/sap%20abap/tg-p/board-id/erp-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fabap-7-4-use-of-value-for-statements-instead-of-loop-also-to-avoid-using%2Fba-p%2F13554959%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Mass Receive Rental Devices for Conversion](/t5/enterprise-resource-planning-q-a/mass-receive-rental-devices-for-conversion/qaq-p/14234352)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  5 hours ago
* [Tax statement item missing for tax code V0 in intercompany billing VF02](/t5/enterprise-resource-planning-q-a/tax-statement-item-missing-for-tax-code-v0-in-intercompany-billing-vf02/qaq-p/14234014)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  11 hours ago
* [SAP Enterprise Support Academy Newsletter October 2025](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-enterprise-support-academy-newsletter-october-2025/ba-p/14232476)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [Enhanced Variant Table Handling in PMEVC: Excel Download and Upload of Variant Tables](/t5/enterprise-resource-planning-blog-posts-by-sap/enhanced-variant-table-handling-in-pmevc-excel-download-and-upload-of/ba-p/14231777)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [Bank Statement via SOAP API with Posted status, the system creates Payment Allocation tasks](/t5/enterprise-resource-planning-q-a/bank-statement-via-soap-api-with-posted-status-the-system-creates-payment/qaq-p/14226483)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![former_member816598](https://avatars.profile.sap.com/former_member_small.jpeg "former_member816598")  former\_member816598](/t5/user/viewprofilepage/user-id/816598) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d...
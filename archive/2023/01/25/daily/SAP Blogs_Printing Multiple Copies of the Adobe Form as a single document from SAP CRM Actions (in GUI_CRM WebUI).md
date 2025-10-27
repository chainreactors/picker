---
title: Printing Multiple Copies of the Adobe Form as a single document from SAP CRM Actions (in GUI/CRM WebUI)
url: https://blogs.sap.com/2023/01/24/printing-multiple-copies-of-the-adobe-form-as-a-single-document-from-sap-crm-actions-in-gui-crm-webui/
source: SAP Blogs
date: 2023-01-25
fetch_date: 2025-10-04T04:43:29.408067
---

# Printing Multiple Copies of the Adobe Form as a single document from SAP CRM Actions (in GUI/CRM WebUI)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Printing Multiple Copies of the Adobe Form as a si...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160110&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Printing Multiple Copies of the Adobe Form as a single document from SAP CRM Actions (in GUI/CRM WebUI)](/t5/technology-blog-posts-by-members/printing-multiple-copies-of-the-adobe-form-as-a-single-document-from-sap/ba-p/13550401)

![yashoratna](https://avatars.profile.sap.com/c/4/idc4520ad6d4465fd45c038a2900b06cfb64d7202c13b5b692b5553c650090dcdd_small.jpeg "yashoratna")

[yashoratna](https://community.sap.com/t5/user/viewprofilepage/user-id/16294)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160110)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160110)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550401)

‎2023 Jan 24
9:35 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160110/tab/all-users "Click here to see who gave kudos to this post.")

14,426

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [NW ABAP Print and Output Management](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Print%2520and%2520Output%2520Management/pd-p/334558737810127171897316045257708)
* [SAP Interactive Forms by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Interactive%2520Forms%2520by%2520Adobe/pd-p/582573882271271216439685697820265)

* [NW ABAP Print and Output Management

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BPrint%2Band%2BOutput%2BManagement/pd-p/334558737810127171897316045257708)
* [SAP Interactive Forms by Adobe

  Software Product Function](/t5/c-khhcw49343/SAP%2BInteractive%2BForms%2Bby%2BAdobe/pd-p/582573882271271216439685697820265)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

**Introduction**: In my [previous blog](https://blogs.sap.com/2023/01/23/adobe-form-functionality-print-print-preview-in-sap-crm-actions/), I have demonstrated how to enable Adobe Form printing/preview in SAP CRM actions by creating a proxy to Smart Form.

**Requirement:** In this blog, I'll explain how to deal with printing multiple copies of an Adobe form in CRM actions and turn on the functionality to preview and print from the CRM WEBUI screen.

We need to apply same config/code from previous article but will modify method **EXEC\_ADOBE\_FORM** to establish the solution.

To print multiple copies of the adobe form in a one spool job or combining all the copies in a single document, we will open the PDF JOB (by function module FP\_JOB\_OPEN), call the Adobe form in a loop (number of times required to print) and close the PDF JOB (by function module FP\_JOB\_CLOSE). Let's outline the strategy step by step.

**Step 1:** Before invoking, FP\_JOB\_OPEN, we need to set some form processing output parameters as follows.

*ls\_fp\_outputparams-dest        = ls\_output\_options-tddest.*
*ls\_fp\_outputparams-nodialog = is\_control\_parameters-no\_dialog.*
*ls\_fp\_outputparams-reqnew   = ls\_output\_options-tdnewid.*
*ls\_fp\_outputparams-preview  = is\_control\_parameters-preview.*

Furthermore, if we want to print on a physical printer (in a spool), we'll need to set the additional o/p parameter (reqimm) as shown below.

*IF is\_control\_parameters-preview IS INITIAL.*
*ls\_fp\_outputparams-reqimm   = ls\_output\_options-tdimmed.             " To print on actuals*
*ENDIF.*

**Step****2:** The Adobe Function Module must then be invoked repeatedly while being given the control parameters listed below.

*ls\_control\_parameters-langu = lv\_sf\_langu.*
*ls\_control\_parameters-no\_open = abap\_true.*
*ls\_control\_parameters-no\_close = abap\_true.*
*ls\_control\_parameters-getotf = abap\_true.*

**Step 3:** To finish, execute FP JOB CLOSE to close down the spool job. Next, gather all of the results and give them through to the exporting parameter es job output info.

These three steps will complete the functionality, allowing us to view one document (one print/print preview) with multiple copies of the Adobe form in SAP GUI screen only, not on CRM WEBUI screen. Because WEBUI screen expects data in OTF format, and Adobe FM returns PDF data with type tfpcontent (Table with Multiple XFTs, XFDs, PDFs), so no luck in WEBUI.

In order to accomplish this feature, additional output parameters must be provided, and further steps must involve converting PDF data to OTF data (see to the [link](https://blogs.sap.com/2023/01/24/convert-pdf-format-data-to-otf-format/)).

**Step 4:** Check first to see if it is not a GUI screen call, and then set two further parameters:

GETPDF as 'M' and BUMODE as '-'

\* GUI connection enabled ?
*CALL FUNCTION 'RFC\_IS\_GUI\_ON'*
*EXPORTING*
*login\_check = abap\_false*
*IMPORTING*
*on          = lv\_gui.*

*IF lv\_gui NE 'Y' AND is\_control\_parameters-preview IS NOT INITIAL.*
*ls\_fp\_outputparams-getpdf   = 'M'.*
*ls\_fp\_outputparams-bumode   = '-'.*
*ENDIF.*

**Step 5:** Call function module FP\_GET\_PDF\_TABLE to get all the PDF data.

*IF lv\_gui NE 'Y' AND is\_control\_parameters-preview IS NOT INITIAL.*
*CALL FUNCTION 'FP\_GET\_PDF\_TABLE'*
*IMPORTING*
*e\_pdf\_table = lt\_pdf\_table.*
*ENDIF.*

**Step 6:**  Now transform the PDF data to OTF format, then send it as an exporting parameter. To view the code, please click on the method link.

*IF lv\_gui NE 'Y' AND is\_control\_parameters-preview IS NOT INITIAL.*
*LOOP AT lt\_pdf\_table ASSIGNING FIELD-SYMBOL(<fs\_pdf>).*
*CALL METHOD [get\_pdf\_to\_otf](https://blogs.sap.com/2023/01/24/convert-pdf-format-data-to-otf-format/)(*
*EXPORTING*
*iv\_pdf      = <fs\_pdf>*
*IMPORTING*
*et\_otf\_data = DATA(li\_otf) ).*
*ENDLOOP.*

*es\_job\_output\_info-otfdata[] = li\_otf.*
*ENDIF.*

For both GUI and WEBUI screens, kindly follow the whole code, which includes multiple copies of PDF in a single document.

```
DATA: lv_dummy(254)           TYPE c,

        ls_printer_profile_data TYPE tsppf_prpr_002,

        lv_adobe_fm_name        TYPE rs38l_fnam.

TRY .

      DATA(lv_adobe_form) = ip_smart_form.

      CALL FUNCTION 'FP_FUNCTION_MODULE_NAME'

        EXPORTING

          i_name     = lv_adobe_form

        IMPORTING

          e_funcname = lv_adobe_fm_name.

    CATCH cx_fp_api_repository

          cx_fp_api_usage

          cx_fp_api_internal.

      IF sy-subrc <> 0.

*   add an error message to processing protocol

        MESSAGE i015(sppf_media) WITH lv_adobe_form INTO lv_dummy.

        CALL METHOD cl_log_ppf=>add_message

          EXPORTING

            ip_problemclass = '1'

            ip_handle       = ip_application_log.

        RETURN.

      ENDIF.

  ENDTRY.

*-----------fill archive parameters for archive link -------------------

  IF is_output_options-tdarmod = '2'

     OR is_output_options-tdarmod = '3'.

*   archive_index_tab

    ASSIGN ct_archive_i...
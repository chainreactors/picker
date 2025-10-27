---
title: How to extract VIM DP Documents as PDF attachments from OpenText Archive server
url: https://blogs.sap.com/2023/02/09/how-to-extract-vim-dp-documents-as-pdf-attachments-from-opentext-archive-server/
source: SAP Blogs
date: 2023-02-10
fetch_date: 2025-10-04T06:13:57.602650
---

# How to extract VIM DP Documents as PDF attachments from OpenText Archive server

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to extract VIM DP Documents as PDF attachments...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162878&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to extract VIM DP Documents as PDF attachments from OpenText Archive server](/t5/technology-blog-posts-by-members/how-to-extract-vim-dp-documents-as-pdf-attachments-from-opentext-archive/ba-p/13566217)

![younmazz](https://avatars.profile.sap.com/1/4/id148fc9cd6f5873608a13eb04a0884e5de6893f4e5ea0f22b202d6b3eb7f9a074_small.jpeg "younmazz")

[younmazz](https://community.sap.com/t5/user/viewprofilepage/user-id/250)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162878)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162878)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566217)

‎2023 Feb 09
10:33 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162878/tab/all-users "Click here to see who gave kudos to this post.")

5,483

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Archiving and Document Access by OpenText](https://community.sap.com/t5/c-khhcw49343/SAP%2520Archiving%2520and%2520Document%2520Access%2520by%2520OpenText/pd-p/01200615320800000706)
* [SAP Document Access by OpenText](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520Access%2520by%2520OpenText/pd-p/01200615320800000707)
* [NW ABAP Data Archiving](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Data%2520Archiving/pd-p/777340172955087410686548844218124)
* [PLM Document Management System (DMS)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Document%2520Management%2520System%2520%28DMS%29/pd-p/318021688820573698933533760680517)

* [SAP Archiving and Document Access by OpenText

  SAP Archiving and Document Access by OpenText](/t5/c-khhcw49343/SAP%2BArchiving%2Band%2BDocument%2BAccess%2Bby%2BOpenText/pd-p/01200615320800000706)
* [SAP Document Access by OpenText

  SAP Archiving and Document Access by OpenText](/t5/c-khhcw49343/SAP%2BDocument%2BAccess%2Bby%2BOpenText/pd-p/01200615320800000707)
* [PLM Document Management System (DMS)

  Software Product Function](/t5/c-khhcw49343/PLM%2BDocument%2BManagement%2BSystem%2B%252528DMS%252529/pd-p/318021688820573698933533760680517)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [NW ABAP Data Archiving

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BData%2BArchiving/pd-p/777340172955087410686548844218124)

View products (5)

### Motivation

One of simple tasks that I had to do was to retrieve DP documents from OpenText Archive server using Archive link functions in order to attach them into GOS email services.

I found lots of examples of reading data from Archive link and all of them required writing files on a physical folder to attach them to email function . However I remember that I programed ABAP modules and objects in a SAP security project circa 2003 where I setup a Kpro server as SAP DMS and did DMS  configurations. The function modules I built at that time is reading data from Kpro DMS contents sever in MEMORY not as a physical file nor needed to write down a file on local folder wherever. Thee reason of that was the encrypted of RSA keys were to be added to the header of the footer of MS office (or Adobe) documents  as binary set which also worked only with binary document body. The documents I read as memory must be binary format for that reason. The decryption and validation process with CA  were done by opposite ways.

I am suspicious that there might be one among Archive link functions which I built. I did find it.

### **Development Example**

**Get Archive ID of DP document**

Create ABAP class ZCL\_VIM\_DP\_INVFILE\_SRV\_001->CONSTRUCTOR and read Archive ID  by using OpenText FM '/OPT/VIM\_VA2\_GET\_ARCH\_DATA'   or simply select from 1head table at method "constructor"

```
  SELECT SINGLE archiv_id

                arc_doc_id

           INTO (iv_archiv_id,

                iv_arc_doc_id)

           FROM /opt/vim_1head

          WHERE docid = iv_docid.
```

You can get Archive ID and Archive Document ID from DP document ID

```
    CALL FUNCTION '/OPT/VIM_VA2_GET_ARCH_DATA'

      EXPORTING

        iv_docid              = iv_docid

      IMPORTING

        iv_archiv_id          = gv_archiv_id

        iv_arc_doc_id         = gv_arc_doc_id

      EXCEPTIONS

        system_failure        = 1 error_message

        communication_failure = 2 error message.
```

Import parameter IV\_DOCID TYPE /OPT/DOCID

```
* read Archive ID

    IF iv_docid IS INITIAL.

      RAISE EXCEPTION TYPE zcx_vim_util EXPORTING textid = zcx_vim_util=>exp_id001.

    ENDIF.

    CALL FUNCTION '/OPT/VIM_VA2_GET_ARCH_DATA'

      EXPORTING

        iv_docid              = iv_docid

      IMPORTING

        iv_archiv_id          = gv_archiv_id

        iv_arc_doc_id         = gv_arc_doc_id

      EXCEPTIONS

        system_failure        = 1 error_message

        communication_failure = 2 error message.

    IF   gv_archiv_id IS INITIAL

      OR gv_arc_doc_id IS INITIAL.

      RAISE EXCEPTION TYPE zcx_vim_util EXPORTING textid = zcx_vim_util=>exp_id002.

    ENDIF.
```

**Read Document as memory** (Internal table)

Create a METHOD get\_dp\_image\_from\_cms\_x. with return parameter  RT\_SOLIX\_TAB  TYPE SOLIX\_TAB

CompID should be 'data' and need to pass Archive ID and Doc ID. Then need to convert the data type RAW 1024 of output into type RAW 255 which is compatible with the data format of email attachment.

Archive Link Document Class for the OpenText DP document is  '/OPT/V1001' : GC\_DP\_DOC\_TYPE

```
  METHOD get_dp_image_from_cms_x.

    CALL FUNCTION 'ARCHIVOBJECT_GET_TABLE'

      EXPORTING

        archiv_id                = gv_archiv_id

        document_type            = gc_dp_doc_type

        archiv_doc_id            = gv_arc_doc_id

*       ALL_COMPONENTS           =

*       SIGNATURE                = 'X'

        compid                   = 'data'

      IMPORTING

        length                   = ev_length

        binlength                = ev_binlength

      TABLES

        archivobject             = et_archivobject

        binarchivobject          = et_binarchivobject

      EXCEPTIONS

        error_archiv             = 1

        error_communicationtable = 2

        error_kernel             = 3

        OTHERS                   = 4.

    IF sy-subrc = 0.

      CALL METHOD cl_rmps_general_functions=>convert_1024_to_255

        EXPORTING

          im_tab_1024 = et_binarchivobject[]

        RECEIVING

          re_tab_255  = rt_solix_tab[].

    ENDIF.

  ENDMETHOD.
```

**Make a short form  with email attachment as PDF**

GP\_DEF\_ATTRIB = DP document id (type : /opt/docid )

```
** Create OBJ attachment -  DP Invoice PDF

DATA(lt_pdf_solix)

  = NEW zcl_vim_dp_invfile_srv_001( CONV /opt/docid( gp_...
---
title: EXCEL FILE READ FROM APPLICATION SERVER, MOVE FROM ONE FOLDER TO ANOTHER FOLDER AND DELETE FROM FOLDER
url: https://blogs.sap.com/2022/11/16/excel-file-read-from-application-server-move-from-one-folder-to-another-folder-and-delete-from-folder/
source: SAP Blogs
date: 2022-11-17
fetch_date: 2025-10-03T23:00:06.111300
---

# EXCEL FILE READ FROM APPLICATION SERVER, MOVE FROM ONE FOLDER TO ANOTHER FOLDER AND DELETE FROM FOLDER

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* EXCEL FILE READ FROM APPLICATION SERVER, MOVE FROM...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47606&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [EXCEL FILE READ FROM APPLICATION SERVER, MOVE FROM ONE FOLDER TO ANOTHER FOLDER AND DELETE FROM FOLDER](/t5/application-development-and-automation-blog-posts/excel-file-read-from-application-server-move-from-one-folder-to-another/ba-p/13569646)

![former_member677524](https://avatars.profile.sap.com/former_member_small.jpeg "former_member677524")

[former\_member677524](https://community.sap.com/t5/user/viewprofilepage/user-id/677524)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47606)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47606)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569646)

‎2022 Nov 16
7:41 PM

[2
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47606/tab/all-users "Click here to see who gave kudos to this post.")

25,557

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

**BUSINESS REQUIRNMENT**
Read Exel file from Application Server(T Code – AL11) put it to internal table , Move file from
one folder to other folder and delete file from folder.

**EXCEL UPLOAD FORMAT DEMO**

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-13-074913.png)

EXCEL FORMAT DEMO

**APPLICATION SERVER DIRECTORY TO UPLOAD**

![](/legacyfs/online/storage/blog_attachments/2022/11/2-37.png)

AL11 PATH

This path provided by SAP-BASIS team . It can vary as per system like :

p\_dir = ‘/usr/sap/attachments/’.

**CODE LOGIC**

To upload excel file in al11 first we have to create a structure as per excel format. In current scenario excel  contains eight columns so we first create a structure of eight fields and declare the data types .

```
DATA : LV_FILE TYPE EPS2FILNAM,

       p_file LIKE rlgrap-filename.

DATA : p_file_n TYPE localfile ,

       iv_file  TYPE string.

DATA: lt_dir1 TYPE TABLE OF eps2fili,

      wa_dir1 like LINE OF lt_dir1.

DATA : gs_final_t1 TYPE ty_daily,

       p_dir            TYPE salfile-longname,

       gt_final_t1 TYPE TABLE OF ty_daily.

DATA lv_return TYPE c.
```

```
TYPES: BEGIN OF ty_daily,

         col1 TYPE char18,

         col2 TYPE char18,

         col3 TYPE char18,

         col4 TYPE char18,

         col5 TYPE char18,

         col6 TYPE char30,

         col7 TYPE char18,

         col8 TYPE char18,

       END OF ty_daily.

DATA : BEGIN OF it_final occurs 0,

        a TYPE char20,

        b TYPE char20,

        c TYPE char20,

        d TYPE char20,

        e TYPE char20,

        f TYPE char30,

        g TYPE char20,

        h TYPE char20,

      END OF it_final.
```

Next we have to fetch the directory details of al11 using FM 'EPS2\_GET\_DIRECTORY\_LISTING'.

```
p_dir = ‘/usr/sap/otattachments/’. " al11 path

CALL FUNCTION 'EPS2_GET_DIRECTORY_LISTING'

  EXPORTING

    iv_dir_name = p_dir

  TABLES

    dir_list    = lt_dir1

  .

IF sy-subrc <> 0.

* Implement suitable error handling here

else.

  DELETE lt_dir1 WHERE rc <> '0000'.

ENDIF.

READ TABLE lt_dir1 INTO wa_dir1 INDEX 1.

IF sy-subrc eq 0.

  p_file_n = wa_dir1-name.

CONCATENATE p_path '/' wa_dir1-name INTO p_file.

LV_FILE = P_FILE. "File name path create
```

Now next step is open the file in al11 and fill it in our string

```
OPEN DATASET lv_file FOR INPUT IN BINARY MODE .

IF sy-subrc EQ 0.

  READ DATASET lv_file INTO lv_xls_xstr.

*  lv_xls_xstr = wa_str.

  IF sy-subrc NE 0.

*    MESSAGE e002 WITH lv_file.

  ENDIF.

ELSE.

*  MESSAGE e001 WITH lv_file.

ENDIF.
```

After filling the data in string we have to close dataset.

```
CLOSE DATASET lv_file.
```

Now next and challenging part is to convert the excel data properly without picking garbage value in internal table use that we manipulate in program according to our business logic. Various methods are available in other blogs but I get success only using this method.

```
lo_xlsx->if_fdt_doc_spreadsheet~get_worksheet_names(

  IMPORTING

    worksheet_names = DATA(lt_excel)

).

"

LOOP AT lt_excel INTO DATA(ls_excel).

  DATA(ir_ref) = lo_xlsx->if_fdt_doc_spreadsheet~get_itab_from_worksheet( ls_excel  ) .

  ASSIGN ir_ref->* TO FIELD-SYMBOL(<lfs_data_tab>).

  MOVE-CORRESPONDING <lfs_data_tab> TO it_final[].

ENDLOOP.

“ EXCEL DATA POPULATE IN IT FINAL.
```

Now if we want to Move this file from one folder to other like we want to move the file to archive folder  we can use below method using keyword transfer

```
DATA: V_OLD type localfile,

            V_NEW type localfile,

                L_NEWLINE(240) type c.

v_old = lv_file.

P_path_arc = ‘/usr/sap/otattachments/arc’

OPEN DATASET v_old FOR INPUT IN BINARY MODE .

IF sy-subrc eq 0.

  CONCATENATE p_path_arc '/' wa_dir1-name INTO p_file_arc.

  LV_FILE_ARC = p_file_arc.

  v_new = LV_FILE_ARC.

  OPEN DATASET v_new FOR OUTPUT IN BINARY MODE .

  IF sy-subrc eq 0.

    DO.

                                READ DATASET v_old INTO l_newline.

                                IF sy-subrc EQ 0.

                                              TRANSFER l_newline  TO v_new.

                                ELSE.

                                              if l_newline is not initial.

                                                      TRANSFER l_newline TO v_new.

                                              endif.

                                              EXIT.

                                ENDIF.

                ENDDO.

  ENDIF.

ENDIF.

  CLOSE DATASET v_new.

CLOSE DATASET v_old.
```

Now we want to delete file from previous folder . Its very easy and simple just using keyword we can achieve  that.

```
DELETE DATASET v_old. " v_old is the path from where we want to delete file
```

**Conclusion:**

I hope this blog post will help you and get the idea how to read the excel file  from application server (AL11) ,copy and delete .

Please like and share feedback or thoughts in comment. Follow my page for this type of ABAP related topics. Also follow <https://community.sap.com/topics/abap>  to enhance  knowledge in ABAP.

* [al11](/t5/tag/al11/tg-p/board-id/application-developmentblog-board)
* [excel file](/t5/tag/excel%20file/tg-p/boa...
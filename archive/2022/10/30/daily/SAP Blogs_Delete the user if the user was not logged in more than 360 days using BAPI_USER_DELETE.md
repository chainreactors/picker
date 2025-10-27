---
title: Delete the user if the user was not logged in more than 360 days using BAPI_USER_DELETE
url: https://blogs.sap.com/2022/10/29/delete-the-user-if-the-user-was-not-logged-in-more-than-360-days-using-bapi_user_delete/
source: SAP Blogs
date: 2022-10-30
fetch_date: 2025-10-03T21:19:04.116284
---

# Delete the user if the user was not logged in more than 360 days using BAPI_USER_DELETE

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Delete the user if the user was not logged in more...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46940&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Delete the user if the user was not logged in more than 360 days using BAPI\_USER\_DELETE](/t5/application-development-and-automation-blog-posts/delete-the-user-if-the-user-was-not-logged-in-more-than-360-days-using-bapi/ba-p/13558465)

![former_member774460](https://avatars.profile.sap.com/former_member_small.jpeg "former_member774460")

[former\_member774460](https://community.sap.com/t5/user/viewprofilepage/user-id/774460)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46940)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46940)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558465)

‎2022 Oct 29
5:44 PM

[3
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46940/tab/all-users "Click here to see who gave kudos to this post.")

1,672

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

Delete the user if the user was not logged in more than 360 days using BAPI\_USER\_DELETE

1..Give the import parameters as number of days and test flag

![](/legacyfs/online/storage/blog_attachments/2022/10/userdelete1.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/userdelete1-1.png)

2.Create the structure as per output pass into the export parameters ET\_RETURN.

![](/legacyfs/online/storage/blog_attachments/2022/10/userdelete2.png)

3.Structure as per your output.

![](/legacyfs/online/storage/blog_attachments/2022/10/userdelete3.png)

Now click on Source code write the below code

```
FUNCTION zuser_login_check360.

*"----------------------------------------------------------------------

*"*"Local Interface:

*"  IMPORTING

*"     VALUE(DTRDAT) TYPE  JBNTAGE DEFAULT 360

*"  EXPORTING

*"     REFERENCE(EX_RETURN) TYPE  ZT_USER

*"----------------------------------------------------------------------

* Data declarations

  DATA:  lv_last_logon_date TYPE xuldate,

         lv_days            TYPE vtbbewe-atage,

         ls_date            TYPE bapilogond,

         ls_flag            TYPE bapilogonx,

         lt_return          TYPE bapiret2_t,

         lv_dat             TYPE dats.

*   **--- Getting the last 180 days dates

  lv_dat = sy-datum - 360.

* Based on the last login date fetch the user details

  SELECT bname,trdat FROM usr02

                     INTO TABLE @DATA(lt_user)

                     WHERE  trdat LE @lv_dat.

  IF lt_user IS NOT INITIAL.

*    **--Fetch User details

    SELECT bname, name_first, name_last FROM user_addr

                                        INTO TABLE @DATA(lt_addr)

                                        FOR ALL ENTRIES IN @lt_user

                                        WHERE bname = @lt_user-bname.

    LOOP AT lt_addr ASSIGNING FIELD-SYMBOL(<fs_user>).

**--Update user valid to date

          CALL FUNCTION 'BAPI_USER_DELETE'

            EXPORTING

              username = <fs_user>-bname

            tables

              return   = lt_return.

          IF sy-subrc EQ 0.

            APPEND INITIAL LINE TO ex_return ASSIGNING FIELD-SYMBOL(<ls_return>).

            <ls_return>-username = <fs_user>-bname.

            <ls_return>-firstname = <fs_user>-name_first.

            <ls_return>-lastname = <fs_user>-name_last.

            READ TABLE lt_return INTO DATA(ls_return) WITH KEY type = 'S'.

             <ls_return>-status = 'User' && | | && <fs_user>-bname && | | && 'Deleted' .

          ELSE.

            <ls_return>-username = <fs_user>-bname.

            <ls_return>-firstname = <fs_user>-name_first.

            <ls_return>-lastname = <fs_user>-name_last.

            READ TABLE lt_return INTO ls_return WITH KEY type = 'E'.

            IF sy-subrc = 0.

              <ls_return>-status = ls_return-message .

            ENDIF.

        ENDIF.

    ENDLOOP.

  ENDIF.

ENDFUNCTION.
```

Now execute the function module we will get the deleted users.

**NOTE:**While testing the code please comment the BAPI\_USER\_DELETE, Otherwise users would be deleted from the system.

Thank you

Siva sidda.

1 Comment

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin
---
title: Block the user if the user not logged more than 90 days using BAPI_USER_CHANGE
url: https://blogs.sap.com/2022/10/29/block-the-user-if-the-user-not-logged-more-than-90-days-using-bapi_user_change/
source: SAP Blogs
date: 2022-10-30
fetch_date: 2025-10-03T21:19:09.786212
---

# Block the user if the user not logged more than 90 days using BAPI_USER_CHANGE

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Block the user if the user not logged more than 90...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46928&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Block the user if the user not logged more than 90 days using BAPI\_USER\_CHANGE](/t5/application-development-and-automation-blog-posts/block-the-user-if-the-user-not-logged-more-than-90-days-using-bapi-user/ba-p/13558393)

![former_member774460](https://avatars.profile.sap.com/former_member_small.jpeg "former_member774460")

[former\_member774460](https://community.sap.com/t5/user/viewprofilepage/user-id/774460)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46928)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46928)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558393)

‎2022 Oct 29
10:06 AM

[2
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46928/tab/all-users "Click here to see who gave kudos to this post.")

2,321

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

Block the user if the user not logged more than 90 days using BAPI\_USER\_CHANGE and validity date will updated with current date.

1.Give the import parameters as number of days and test flag

![](/legacyfs/online/storage/blog_attachments/2022/10/userblcok1-1.png)

2.Create the structure as per output pass into the export parameters ET\_RETURN.

![](/legacyfs/online/storage/blog_attachments/2022/10/userblcok2-1.png)

Structure as per your output.

![](/legacyfs/online/storage/blog_attachments/2022/10/userblock3.png)

```
  DATA: lv_last_logon_date TYPE xuldate,

        lv_days            TYPE vtbbewe-atage,

        ls_date            TYPE bapilogond,

        ls_flag            TYPE bapilogonx,

        lt_return          TYPE bapiret2_t,

        lv_dat             TYPE dats,

        lv_sysid           LIKE sy-sysid.

*DATA: lt_task_type type ty_task_type occurs 0 with header line,

*      task_text LIKE swwvpublic-wi_rhtext.

* Getting the last 90 days date

  lv_dat = sy-datum - im_dtrdat.

* Based on the last login date fetch the user details

  SELECT bname,trdat,ustyp,class FROM usr02

                     INTO TABLE @DATA(lt_user)

                     WHERE ( trdat LE @lv_dat AND ustyp = 'A' AND CLASS LIKE 'GRC%').

   delete lt_user WHERE trdat is INITIAL.

**  Function module to get the SYSTEMID

  CALL FUNCTION 'MSS_GET_SY_SYSID'

    IMPORTING

      sapsysid = lv_sysid.

  IF lt_user IS NOT INITIAL.

    LOOP AT lt_user ASSIGNING FIELD-SYMBOL(<fs_user>).

      APPEND INITIAL LINE TO et_return ASSIGNING FIELD-SYMBOL(<ls_return>).

***--Update user valid to date

      ls_date-gltgb = sy-datum.

      ls_flag-gltgb = 'X'.

        CALL FUNCTION 'BAPI_USER_CHANGE'

          EXPORTING

            username   = <fs_user>-bname

            logondata  = ls_date

            logondatax = ls_flag

          TABLES

            return     = lt_return.

      IF sy-subrc EQ 0.

        <ls_return>-userid = <fs_user>-bname.

        <ls_return>-last_logon = <fs_user>-trdat.

        <ls_return>-ustyp = <fs_user>-ustyp.

        <ls_return>-class = <fs_user>-class.

        <ls_return>-systemid = lv_sysid.

        <ls_return>-status = 'User' && | | && <fs_user>-bname && | | && 'Expried-Contact system Administator For Logon'.

      ELSE.

        <ls_return>-userid = <fs_user>-bname.

        <ls_return>-last_logon = <fs_user>-trdat.

        <ls_return>-ustyp = <fs_user>-ustyp.

        <ls_return>-systemid = lv_sysid.

        READ TABLE lt_return INTO DATA(ls_return) WITH KEY type = 'E'.

        IF sy-subrc = 0.

          <ls_return>-status = ls_return-message .

        ENDIF.

      ENDIF.

    ENDLOOP.

  ENDIF.

ENDFUNCTION.
```

Finally execute the function module, we will get the list of blocked users, updated validity date with current date.

![](/legacyfs/online/storage/blog_attachments/2022/10/userblcok4.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/userblcok5.png)

Note: Before you run this code please comment the BAPI\_USER\_CHANGE function module other wise users will effect with their logins.

Hope it will useful.

Thank you

Siva sidda.

1 Comment

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin
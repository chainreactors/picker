---
title: Field symbol in iteration expression
url: https://blogs.sap.com/2023/02/19/field-symbol-in-iteration-expression/
source: SAP Blogs
date: 2023-02-20
fetch_date: 2025-10-04T07:33:26.882698
---

# Field symbol in iteration expression

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Field symbol in iteration expression

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46662&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Field symbol in iteration expression](/t5/application-development-and-automation-blog-posts/field-symbol-in-iteration-expression/ba-p/13552449)

![JackGraus](https://avatars.profile.sap.com/1/4/id14c4b423208594a09922b0acaf529f4d72ef219f7e39ba15147c23904ad2fd5a_small.jpeg "JackGraus")

[JackGraus](https://community.sap.com/t5/user/viewprofilepage/user-id/225106)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46662)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46662)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552449)

‎2023 Feb 19
5:29 AM

[9
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46662/tab/all-users "Click here to see who gave kudos to this post.")

2,651

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

In table iteration expression (like the FOR expression) one can decide to either use a work area or field symbol.

```
... FOR wa|<fs> IN itab [INDEX INTO idx] [cond] [let_exp]  ...
```

The ABAP help does indicate: For each read line, the result is either assigned to a local work area wa1 or to a field symbol <fs>.

In my own developments I prefer to use reference variables over field symbols. In a table iteration expression only field symbol or work area can be used. Because of performance reason I prefer to use field symbols here. But not completely sure there is a difference in performance as the expression does get processed internally. I double check by a small test program: Using field symbol within a table iteration expression **does have a performance improvement**.

```
DATA:

  lt_mara            TYPE mara_tt,

  lt_matnr           TYPE table_matnr,

  lv_timestamp_start TYPE timestampl,

  lv_timestamp_end   TYPE timestampl,

  lv_timestamp       TYPE timestampl.

SELECT * FROM mara INTO TABLE lt_mara.

GET TIME STAMP FIELD lv_timestamp_start.

DO 1000 TIMES.

  lt_matnr = VALUE table_matnr( FOR ls_mara IN lt_mara ( ls_mara-matnr ) ).

ENDDO.

GET TIME STAMP FIELD lv_timestamp_end.

lv_timestamp = lv_timestamp_end - lv_timestamp_start.

WRITE / `Workarea: ` && lv_timestamp.

GET TIME STAMP FIELD lv_timestamp_start.

DO 1000 TIMES.

  lt_matnr = VALUE table_matnr( FOR <ls_mara> IN lt_mara ( <ls_mara>-matnr ) ).

ENDDO.

GET TIME STAMP FIELD lv_timestamp_end.

lv_timestamp = lv_timestamp_end - lv_timestamp_start.

WRITE / `Field symbol: ` && lv_timestamp.
```

```
Test

Workarea: 1.6138080

Field symbol: 0.5876100
```

4 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin
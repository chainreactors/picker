---
title: ABAP Object Services Technique
url: https://blogs.sap.com/2022/10/21/abap-object-services-technique-2/
source: SAP Blogs
date: 2022-10-22
fetch_date: 2025-10-03T20:35:42.711884
---

# ABAP Object Services Technique

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* ABAP Object Services Technique

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46588&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [ABAP Object Services Technique](/t5/application-development-and-automation-blog-posts/abap-object-services-technique/ba-p/13549946)

![roberto_forti](https://avatars.profile.sap.com/8/f/id8f396c2a910b81039183c46c1623253fdfdd4863d77cf5ef51e27491e4d117fa_small.jpeg "roberto_forti")

[roberto\_forti](https://community.sap.com/t5/user/viewprofilepage/user-id/411153)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46588)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46588)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549946)

‎2022 Oct 21
7:10 PM

[4
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46588/tab/all-users "Click here to see who gave kudos to this post.")

2,147

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

## ABAP Object Services

In this blog you are going to read some information about ABAP Object Services and how to create persistent class object with single-table using mapping assistant tool, create object instance with class agent, consumer perspective and record converted into database table.

### #1. Creating Persistent Object with single-table

SAP Community has introduced excellent Professionals to SAP world as well as providing opportunity for all to writing blog posts which has helped us to improve SAP knowledge.

One of many important SAP techniques which I have been reading about is **ABAP Object Services**applying object-oriented concept.

This *first* blog post will show a simple way of ***creating persistence class***working with single-table.

**1. ABAP Object Services – Creating Persistent Object with single-table**

* **Objective:** handling the ***synchronization*** of data stored in objects with database table creating a ***method to synchronize*** object data with a relational database table considering object relational mapping (ORM) tool.

* [Object Service](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abenobject_services_glosry.htm) by SAP documentation.

* Following simple steps to create persistence class.

**1.1. Creating Persistent Class (SE80)**

* Start transaction SE80 to create a Persistence class without “Final” class checked.

* [Persistent Class](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abenpersistent_class_glosry.htm) and [Final Class](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abenfinal_glosry.htm) by SAP documentation.

![](/legacyfs/online/storage/blog_attachments/2018/08/Persistent_Class.png)

* Confirm “Yes” to activate Class Agent – “*At runtime, Class Agent run between persistent objects and the ABAP Object Services”*.

![](/legacyfs/online/storage/blog_attachments/2018/08/class_actor.png)

* Agent ABAP Persistent Class implemented.

![](/legacyfs/online/storage/blog_attachments/2018/08/class_actor-1.png)

**1.2. Working with *single-table* using Mapping Assistant tool**

* Going to ***Persistence******Representing*** to add single-table

* [Database Table](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abendatabase_table_glosry.htm) by SAP documentation

![](/legacyfs/online/storage/blog_attachments/2018/08/Goto_Persistence_Representant.png)

* Insert table/structure for corresponding class.

![](/legacyfs/online/storage/blog_attachments/2018/08/class_actor-2.png)

* **By Business Key** – ABAP Dictionary tables which use exiting primary key.

* [Primary Key](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abenprimary_key_glosry.htm) by SAP documentation

![](/legacyfs/online/storage/blog_attachments/2018/08/class_actor-4.png)

* Mapping Assistant tool  – Click on **Generator Settings** button and uncheck the minimum Interface for methods *CREATE\_PERSISTENT* and *CREATE\_TRANSIENT.*

![](/legacyfs/online/storage/blog_attachments/2018/08/class_actor-6.png)

**1.3. Persistent objects – Consumer Perspective**

* Persistent objects are managed by object services.

* [Persistent Object](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abenpersistent_object_glosry.htm) by SAP documentation

![](/legacyfs/online/storage/blog_attachments/2018/08/Persistent_Object.png)

**1.4. Creating Persistent Object Instance with class agent**

* ABAP code example: Simple report with corresponding statement Persistent Class and Agent Class working with synchronization of data stored in objects with a relational database table.

```
*&---------------------------------------------------------------------*

*& Report ZABAP_PERSISTENT_OBJECT

*&---------------------------------------------------------------------*

REPORT zabap_persistent_object.

*&---------------------------------------------------------------------*

*& DATA OBJECT

*&---------------------------------------------------------------------*

DATA: lo_cl_persist TYPE REF TO zcl_single_table_persistent,

      lx_os_ex      TYPE REF TO cx_os_object_existing,

      lv_text       TYPE string.

*&---------------------------------------------------------------------*

*& START-OF-SELECTIONf)

*&---------------------------------------------------------------------*

START-OF-SELECTION.

  TRY.

      lo_cl_persist = zca_single_table_persistent=>agent->create_persistent(

                        i_char20 = 'TEST01'

                        i_int4   = 1

                        i_char50 = 'TEST-01'

                        i_fltp   = '100.50'

                        i_tims   = sy-uzeit ).

      COMMIT WORK.

    CATCH cx_os_object_existing INTO lx_os_ex.

      lv_text = lx_os_ex->get_text( ).

  ENDTRY.
```

*\* COMMIT WORK: Persistence Service convert in-memory record into the Database table.*

* [Commit Work](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abapcommit.htm) by SAP documentation

**1.5. Record converted into Database table**

* Transactions SE11, SE16 and SE16N to check it.

![](/legacyfs/online/storage/blog_attachments/2018/08/class_actor-5.png)

Certainly, learning **ABAP Object Services** technique will improve technical knowledge as well as makes the ABAP code flexible to implement persistence without writing SQL....
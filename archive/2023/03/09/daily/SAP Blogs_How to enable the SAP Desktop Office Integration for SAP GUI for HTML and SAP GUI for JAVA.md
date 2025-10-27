---
title: How to enable the SAP Desktop Office Integration for SAP GUI for HTML and SAP GUI for JAVA
url: https://blogs.sap.com/2023/03/08/how-to-enable-the-sap-desktop-office-integration-for-sap-gui-for-html-and-sap-gui-for-java/
source: SAP Blogs
date: 2023-03-09
fetch_date: 2025-10-04T09:01:20.470600
---

# How to enable the SAP Desktop Office Integration for SAP GUI for HTML and SAP GUI for JAVA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to enable the SAP Desktop Office Integration f...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163113&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to enable the SAP Desktop Office Integration for SAP GUI for HTML and SAP GUI for Java](/t5/technology-blog-posts-by-sap/how-to-enable-the-sap-desktop-office-integration-for-sap-gui-for-html-and/ba-p/13566119)

![christian_grail](https://avatars.profile.sap.com/1/4/id14de59b460ed77c5b8ee4177d07e41db1ea654096bef507470f2300e5961ab8a_small.jpeg "christian_grail")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[christian\_grail](https://community.sap.com/t5/user/viewprofilepage/user-id/225478)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163113)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163113)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566119)

‎2023 Mar 08
10:22 PM

[23
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163113/tab/all-users "Click here to see who gave kudos to this post.")

19,599

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [UI SAP GUI for Java](https://community.sap.com/t5/c-khhcw49343/UI%2520SAP%2520GUI%2520for%2520Java/pd-p/365168143769967368427513862901274)
* [UI SAP GUI for Windows](https://community.sap.com/t5/c-khhcw49343/UI%2520SAP%2520GUI%2520for%2520Windows/pd-p/345385326078662132058122667685214)
* [UI WebGUI and Internet Transaction Server (ITS)](https://community.sap.com/t5/c-khhcw49343/UI%2520WebGUI%2520and%2520Internet%2520Transaction%2520Server%2520%28ITS%29/pd-p/124125469642888240532580689115094)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [UI SAP GUI for Java

  Software Product Function](/t5/c-khhcw49343/UI%2BSAP%2BGUI%2Bfor%2BJava/pd-p/365168143769967368427513862901274)
* [UI SAP GUI for Windows

  Software Product Function](/t5/c-khhcw49343/UI%2BSAP%2BGUI%2Bfor%2BWindows/pd-p/345385326078662132058122667685214)
* [UI WebGUI and Internet Transaction Server (ITS)

  Software Product Function](/t5/c-khhcw49343/UI%2BWebGUI%2Band%2BInternet%2BTransaction%2BServer%2B%252528ITS%252529/pd-p/124125469642888240532580689115094)

View products (6)

The drop-in replacement has been developed to enable the SAP Desktop Office Integration (DOI) to run on more platforms and operating systems. The SAP Desktop Office Integration is a solution for application developers to integrate Office products like Microsoft Excel and Microsoft Word in their SAP GUI applications. This technology was developed in the 90s and is still heavily used by a lot of applications and customers. It is for example widely used to import and export data from and into an SAP system.

Until now the SAP Desktop Office Integration worked only on Microsoft Windows in combination with SAP GUI for Windows, because it relies on the OLE2 application interface which is only available to native applications like SAP GUI for Windows. With the shift to web applications and other operating systems like Apple macOS this has become an issue for customers who are using SAP GUI applications with SAP GUI for Java or SAP GUI for HTML.

If a customer tries to execute a program which is using the SAP Desktop Office Integration in SAP GUI for HTML or SAP GUI for Java, the program will terminate with the following exception:

```
Category:       ABAP programming error

Runtime Errors: RAISE_EXCEPTION

Short Text:     Exception condition "JAVABEANNOTSUPPORTED" raised.
```

## What Is the Drop-In Replacement of the SAP Desktop Office Integration?

A drop-in replacement is a component which can replace another component without any other code or configuration changes. The drop-in replacement for the SAP Desktop Office Integration keeps on using the same interfaces as the current solution, but enables applications to also run in the web browser in SAP GUI for HTML or SAP GUI for Java. The goal is to keep the migration effort as low as possible and in most cases it's a one-line code-change. The first version of the drop-in replacement for the SAP Desktop Office Integration will support the import and export scenario of data using Microsoft Excel.

![](/legacyfs/online/storage/blog_attachments/2023/03/drop-in-replacement-overview-1.png)

Overview of the Drop-In Replacement of the SAP Desktop Office Integration

## Code Example of the Current SAP Desktop Office Integration

With the original implementation you have to get the container control from the class C\_OI\_CONTAINER\_CONTROL\_CREATOR and call the method get\_container\_control( ) which returns the container control object implementing the interface I\_OI\_CONTAINER\_CONTROL. Using the container control object you've been able to get an instance of the document proxy through the method get\_document\_proxy( ) and on the document proxy instance you've been able to get an instance of the spreadsheet interface by calling the method get\_spreadsheet\_interface( ).

The code needed to set data in a sheet would look like the following:

```
c_oi_container_control_creator=>get_container_control(

  IMPORTING control = DATA(container_control) ).

...

container_control->get_document_proxy(

  EXPORTING document_type  = 'Excel.Sheet'

  IMPORTING document_proxy = DATA(document_proxy) ).

...

document_proxy->get_spreadsheet_interface(

  IMPORTING sheet_interface = DATA(spreadsheet) ).

...

spreadsheet->set_ranges_data( ... ).
```

## Required Code Change

To switch to the drop-in replacement for SAP Desktop Office Integration, you just have to change the initial call to obtain the container control. Instead of obtaining the container control from the class C\_OI\_CONTAINER\_CONTROL\_CREATOR, the container control will then be retrieved from the class CL\_SOVY\_CONTAINER\_CONTROL. The subsequent calls or application logic do not need to be changed.

To enable the in-memory office integration to work properly, an integration mode needs to be provided. This is necessary, because the drop-in replacement needs to now know how it is intended to be used. Previously this was not needed because the Office application was opened at the beginning of the process. Because this is no longer possible in a web application or with SAP GUI for Java, we needed to introduce an integration mode. Of all the possible use cases, we currently support the following integration modes:

+ soi\_mode\_export

  * For use cases ...
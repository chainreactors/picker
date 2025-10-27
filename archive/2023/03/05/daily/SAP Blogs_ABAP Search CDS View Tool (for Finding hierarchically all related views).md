---
title: ABAP Search CDS View Tool (for Finding hierarchically all related views)
url: https://blogs.sap.com/2023/03/04/abap-search-cds-view-tool-for-finding-hierarchically-all-related-views/
source: SAP Blogs
date: 2023-03-05
fetch_date: 2025-10-04T08:43:35.956659
---

# ABAP Search CDS View Tool (for Finding hierarchically all related views)

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* ABAP Search CDS View Tool Version 1 - Not supporte...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47150&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [ABAP Search CDS View Tool Version 1 - Not supported anymore](/t5/application-development-and-automation-blog-posts/abap-search-cds-view-tool-version-1-not-supported-anymore/ba-p/13563188)

![AlwinPut](https://avatars.profile.sap.com/1/7/id1790b96e88142c150749af450acf26ff9aa39fb936f2bd91681decf808d4ade7_small.jpeg "AlwinPut")

[AlwinPut](https://community.sap.com/t5/user/viewprofilepage/user-id/164553)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47150)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47150)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563188)

‎2023 Mar 04
5:59 PM

[41
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47150/tab/all-users "Click here to see who gave kudos to this post.")

19,818

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

> **4-1-2024: Version 2 is now released.**
> See blog post: <https://blogs.sap.com/2024/01/04/abap-search-cds-view-tool-version-2-also-finds-rap-objects/>
>
> **14-7-2023: New functionality** added for filtering on fields with field names, data elements and domain names. Also searching on fields without the "hierarchically search" is possible. See scenario ["Filter on field name, data element name or domain name"](#scenario_filter_on_field) to see how it works.

Searching for the right CDS view can be a time consuming task. A DB table / DDic View or CDS View can have hierarchically more than 8000 related views. DB table MARA has for example 8201 related views in S/4HANA 2022. Searching is also error prone, because searching based on naming does not always lead to the right view.

A good way to search is to find all related CDS views based on DB table, DDic view or CDS view which are directly and indirectly related. This can go up to 15 or more levels deep. So doing this manually by executing where-used list is not doable. Therefor I created the “ABAP Search CDS View Tool” which also can filter the found views.

The following scenarios explain how the tool works.

## Scenario: Find all related views of MARC

* Start program ZSCV\_SEARCH\_CDS\_VIEWS

* Fill "DDic table / view": **MARC
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen1.jpg)**

* Press F8

* The status bar will mention how many Views are found.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen2.jpg)

* The results will show 3 types of Views

  + **DDic Views**
    ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen3.jpg)

  + **DDic CDS Views**
    ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen4-3.jpg)
    See that the DDL Source Name and DDic View Name is filled.

  + **Entity CDS Views**
    ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen5.jpg)See that the DDic View Name is not filled.

## Scenario: Filter for ABAP allowed internal CDS views

Now I only want to see all CDS views which are allowed to be used in ABAP.

* Go back to selection screen

* Push the button "Internal API (C1)". Now the field "C1 Release state" will be filled with RELEASED and field "C1 In ABAP allowed" wil be checked.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen6.jpg)

* Push F8.
  Now 84 Views are found. Here are some views.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen7-1.jpg)

  + See that the DDic CDS views and Entity CDS views are found.

  + The views have all C1 RELEASED and have C1 Use in Cloud Platform selected.

  + Also other annotations are shown like Data Category, VDM View Type, Authorization check, Data Class and Contract Type.

  + See that some have Contract Type #PUBLIC\_LOCAL\_API.

## Scenario: Filter for #BASIC views

I want to search for the basic views for table MARC.

* Go back to selection screen and fill VDM View Type: #BASIC.

* Press F8.
  Now 13 views are found.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen8.jpg)

* In the description in SE11 we can see that the description of table MARC is "Plant Data for Material".
  So based on the naming the most basic CDS view for MARC is CDS View I\_PRODUCTPLANTBASIC.

## Scenario: Filter on Public API CDS views

Now I want to search for CDS views which are enabled and released for OData.

* Go back to selection screen and clear the VDM View Type.

* Push button "Public API (C2)". Now the filter for the C1 fields are cleared and field "C2 Released state" is filled.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen9.jpg)

* Press F8
  Click on the picture to enlarge it.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen10.jpg)
  See that all these CDS views have C2 status RELEASED. And also have Contract Type #PUBLIC\_REMOTE\_API. Also the view names start with A\_ which stands for API.

## Scenario: Filter on custom views

I want to know which custom views call directly or indirectly the DB table MARC.

* Go back to selection screen and clear the VDM View Type.

* Push button "All statuses", to clear all status fields.

* Fill ABAP View with Z\*.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen12.jpg)

* Press F8.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen13.jpg)
  Now DDic views (also DDic CDS views) and Entity CDS views starting with Z will be shown.

## Scenario: CDS views specified by SAP

For some database tables SAP defined in table ARS\_W\_API\_STATE the relation from the DB table to the CDS view.

* Go back to selection screen.

* Fill "DDic Table/View" AUFK.

* Press button "Successor CDS view".
  See that it finds de DDic name IORDER of DDic CDS view I\_ORDER.
  ![](/legacyfs/online/storage/blog_attachments/2023/03/Screen14.jpg)

* Press F8 to find all Views related to the CDS view I\_ORDER.

## Scenario: Filter on field name, data element name or domain name

In this scenario we are going to search for a field "Minimum Lot Size" (BSTMI) in table "Plant Data for Material" (MARC).

![](/legacyfs/online/storage/blog_attachments/2023/03/MARC_FIELD.jpg)

* Restart the program ZSCV\_SEARCH\_CDS\_VIEWS, so that you have a clean selection screen.

* Fi...
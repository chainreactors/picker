---
title: Create a simple CDS view and show data as an IDA reports (aka ALV on HANA)
url: https://blogs.sap.com/2023/08/23/create-a-simple-cds-view-and-show-data-as-an-ida-reports-aka-alv-on-hana/
source: SAP Blogs
date: 2023-08-24
fetch_date: 2025-10-04T12:01:19.567224
---

# Create a simple CDS view and show data as an IDA reports (aka ALV on HANA)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Create a simple CDS view and show data as an IDA r...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/69183&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create a simple CDS view and show data as an IDA reports (aka ALV on HANA)](/t5/enterprise-resource-planning-blog-posts-by-members/create-a-simple-cds-view-and-show-data-as-an-ida-reports-aka-alv-on-hana/ba-p/13580741)

![aamelin1](https://avatars.profile.sap.com/8/e/id8eacda0d2305d74a12c601ec075433bbe922d1383cf670a775c5368c0ec2b14e_small.jpeg "aamelin1")

[aamelin1](https://community.sap.com/t5/user/viewprofilepage/user-id/157733)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=69183)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/69183)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580741)

‎2023 Aug 23
10:24 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/69183/tab/all-users "Click here to see who gave kudos to this post.")

24,184

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

This post is about simple tutorial how to create own CDS view and show data via ALV IDA report.

# What is CDS and how can they be useful?

CDS stands for **Core Data Services**. This is a functionality that allows you to create views of data using the **DDL (Data Definition Language)** language .

In simple terms - you can create your own view based on SAP data table joins with additional logic for filling fields in this view.

For example, take one table as the main source, enrich it with data from related tables (via joins/associations), and add logic to populate individual columns in the generated view. As a result, you'll get a view with the data you need and then work with it directly, for example, make selections in ABAP programs or visualizate through SAP tools, such as through ALV IDA or a custom FIORI application through odata services.

[Description of CDS from SAP](https://help.sap.com/docs/btp/sap-abap-cds-development-user-guide/abap-cds-entities?locale=en-US)

# What is IDA aka ALV on HANA?

IDA is a data visualization tool in SAP GUI, stands for SAP List Viewer with **Integrated Data Access**. Also known as ALV on HANA.

The main essence of the tool is that you can transfer the name of the CDS view and additional restrictions to it (rather than a preselected datas in internal table, as is the case with the classic ALV), the system will select the necessary data and display them in the form of a table visually similar to the ALV Grid, but more functional.

Advantages of IDA:

* Building hierarchies, i.e. nested levels and subtotals over them

* All standard ALV functions are available (except editing and part of formatting)

* Great performance on big data (because it does not require prefetching all data)

* Ability to use text search

* Ability to add fields not from CDS (calculated fields)

The main differences between IDA and the classic ALV Grid:

|
  |
 SAP List Viewer |
 ALV with IDA |

|
 Data Retrieval |
 Responsibility of application, data is collected in an internal ABAP table (ITAB) |
 Responsibility of ALV, table name has to be transferred |

|
 Data Contents |
 All data from the ITAB |
 Visible area only |

|
 Roundtrip (e.g. scrolling) |
 From ALV perspective only operations on the ABAP Server, new area from the ITAB is displayed |
 Paging on the database, that is, new SQL statement is executed |

|
 Application ALV Services (sorting, filtering…) |
 On the ITAB (snapshot behavior) |
 New call to the database |

|
 Memory Consumption |
 Depends on the size of the ITAB |
 Visible area only, relating to columns and rows |

|
 Speed |
 Time required for all data to be transferred to the ITAB on first display |
 Time required for visible area to be transferred |

You may find more info here [https://help.sap.com/docs/SAP\_NETWEAVER\_AS\_ABAP\_FOR\_SOH\_740/b1c834a22d05483b8a75710743b5ff26/efeb734...](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_FOR_SOH_740/b1c834a22d05483b8a75710743b5ff26/efeb734c8e6f41939c39fa15ce51eb4e.html?version=7.40.29)

# How it works?

## Prerequisites

* You must have a SAP S/4HANA system

* Installed [Eclipse](https://www.eclipse.org/downloads/)

* Eclipse has the ADT plugin installed, see [SAP Dev Tools](https://tools.eu1.hana.ondemand.com/)

* Eclipse configured to connect to SAP development system

* You want to make a report based on data from SAP using the new features of S/4HANA

Useful links:

[Installing ABAP Development Tools](https://help.sap.com/doc/2e9cf4a457d84c7a81f33d8c3fdd9694/Cloud/en-US/inst_guide_abap_development_tools.pdf)

[Configuring the ABAP Back-end for ABAP Development Tools](https://help.sap.com/doc/2e65ad9a26c84878b1413009f8ac07c3/201909.001/en-US/config_guide_system_backend_abap_development_tools.pdf)

## Creating a Simple CDS

Let's start creating a simple CDS. To do this, open Eclipse, select the system (the development system and the required client), go to Z package (it's convenient to add it to your favorites for quick access) and right-click on the package name and create a new object

![image](https://user-images.githubusercontent.com/37226181/239619971-dbd88dd0-e14d-479c-85f3-69e0e321e5d6.png)

Select **core data services->data definition**:

![image](https://user-images.githubusercontent.com/37226181/239620149-0f8cb8e2-306f-46d8-8a11-0cd951aeaf8d.png)

Specify the name of the new CDS:

![image](https://user-images.githubusercontent.com/37226181/239620446-88f9d02a-7ea1-4766-a5e2-af4426b5c7b9.png)

And create a new transport request:

![image](https://user-images.githubusercontent.com/37226181/239621159-ccf8dbc2-d83d-4823-86a0-436222fab31a.png)

A template for a new CDS should appears:

```
@AbapCatalog.sqlViewName: ''

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #CHECK

@EndUserText.label: 'test CDS'

define view ZVFI_TEST as select from data_source_name

association [1] to target_data_source_name as _association_name

    on $projection.element_name = _association_name.target_element_name {

    _association_name // Make association public

}
```

let's make a CDS view with data on the chart of accounts (CoA) and GL account texts in two languages ​​at once. Those we need standard SAP tables:

* **SKA1** (GL account data)

* **SKAT** (text table)

The tables are connected by the fields ktopl and saknr. In skat-spras there is also a spras key field with a language for texts.

And the final table should be, with columns:

* CoA Chart of accounts (**SKA1...
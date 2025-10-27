---
title: How to Create Table and Push Data to ODBC/Remote Database using Native SQL with ABAP DB Connectivity (ADBC)
url: https://blogs.sap.com/2023/03/17/how-to-create-table-and-push-data-to-odbc-remote-database-using-native-sql-with-abap-db-connectivity-adbc/
source: SAP Blogs
date: 2023-03-18
fetch_date: 2025-10-04T09:57:11.501226
---

# How to Create Table and Push Data to ODBC/Remote Database using Native SQL with ABAP DB Connectivity (ADBC)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to Create Table and Push Data to ODBC/Remote D...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160258&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Create Table and Push Data to ODBC/Remote Database using Native SQL with ABAP DB Connectivity (ADBC)](/t5/technology-blog-posts-by-members/how-to-create-table-and-push-data-to-odbc-remote-database-using-native-sql/ba-p/13551466)

![kamilmirza](https://avatars.profile.sap.com/d/7/idd71ff2d5ffc2ed6faafc1e76c806dd2a54dcca3c6d73675b68244a01e9e40634_small.jpeg "kamilmirza")

[kamilmirza](https://community.sap.com/t5/user/viewprofilepage/user-id/15938)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160258)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160258)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551466)

‎2023 Mar 17
6:23 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160258/tab/all-users "Click here to see who gave kudos to this post.")

3,342

* SAP Managed Tags
* [Microsoft SQL Server](https://community.sap.com/t5/c-khhcw49343/Microsoft%2520SQL%2520Server/pd-p/891349005586930604519575996418053)
* [ABAP Connectivity](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Connectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [Microsoft SQL Server

  Database](/t5/c-khhcw49343/Microsoft%2BSQL%2BServer/pd-p/891349005586930604519575996418053)
* [ABAP Connectivity

  Programming Tool](/t5/c-khhcw49343/ABAP%2BConnectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

Recently I had a task to Push Data from SAP Reports to MS SQL DB, periodically, and to Create Tables of the required Reports in their MS SQL DB, as well

Being a complete novice ABAP developer, I learned about **ABAP DB Connectivity (ADBC) DDL and DML** methods, which helped me complete the task more dynamically, instead of using **EXEC SQL** with Placeholders ? for each field

*Before moving forward I would like to state the obvious that by no means my approach is best/optimal out there*

So lets start the code with the following objectives:

1. Create a Program to fetch data from SAP Report using SUBMIT

2. Create Table in MS SQL DB according to Report fields

3. Push Data in newly created Table

## 1. Create a Program to fetch data from SAP Report using SUBMIT

```
REPORT ZSCHEDULE.

DATA:

  CREATE_FIELDS TYPE STRING,

  CREATE_PKEY   TYPE STRING,

  INSERT_VALUES TYPE STRING,

  IT_INSERT     TYPE STRINGTAB,

  DATUM         TYPE DATUM,

  UZEIT         TYPE UZEIT.

FIELD-SYMBOLS: <LT_SALV> TYPE ANY TABLE,

               <VALUE>   TYPE ANY.

DATA:

  LS_VBAK TYPE VBAK,

  LS_VBAP TYPE VBAP.

SELECT-OPTIONS:

    SO_VKORG FOR LS_VBAK-VKORG,

    SO_VTWEG FOR LS_VBAK-VTWEG,

    SO_SPART FOR LS_VBAK-SPART,

    SO_VSTEL FOR LS_VBAP-VSTEL,

    SO_VKBUR FOR LS_VBAK-VKBUR.

START-OF-SELECTION.

TRY.

  CL_SALV_BS_RUNTIME_INFO=>SET( DISPLAY = ABAP_FALSE

                                METADATA = ABAP_TRUE

                                DATA = ABAP_TRUE ).

  SUBMIT Z_RPT_PROG

  WITH  SO_VKORG IN  SO_VKORG

  WITH  SO_VTWEG IN  SO_VTWEG

  WITH  SO_SPART IN  SO_SPART

  WITH  SO_VSTEL IN  SO_VSTEL

  WITH  SO_VKBUR IN  SO_VKBUR

    AND RETURN.

  DATA(SALV_META) = CL_SALV_BS_RUNTIME_INFO=>GET_METADATA( ).

  CL_SALV_BS_RUNTIME_INFO=>GET_DATA_REF( IMPORTING R_DATA = DATA(SALV_DATA) ).

  ASSIGN SALV_DATA->* TO <LT_SALV>.

  CL_SALV_BS_RUNTIME_INFO=>CLEAR_ALL( ).

...
```

I have used the formidable **CL\_SALV\_BS\_RUNTIME\_INFO** class to extract ALV Data from the SUBMIT program

## 2. Create Table in MS SQL DB according to Report fields

I have also fetched the **ALV Metadata** because I need **Field Catalog** of the SUBMIT program in order to create our DB Table fields

So I had to write a logic to create different Data type fields in SQL, to be used in **CREATE TABLE** Native SQL statement dynamically

```
...

  LOOP AT SALV_META-T_FCAT INTO DATA(WA_FCAT).

    REPLACE ALL OCCURRENCES OF '/' IN WA_FCAT-FIELDNAME WITH '_'. " forward slash / is considered COMMENT in SQL

    MODIFY SALV_META-T_FCAT FROM WA_FCAT TRANSPORTING FIELDNAME.

    CASE WA_FCAT-DATATYPE.

      WHEN 'CHAR'.

        CREATE_FIELDS = CREATE_FIELDS && |{ WA_FCAT-FIELDNAME } varchar({ WA_FCAT-INTLEN })|.

      WHEN 'CUKY'.

        CREATE_FIELDS = CREATE_FIELDS && |{ WA_FCAT-FIELDNAME } varchar(5)|.

      WHEN 'UNIT'.

        CREATE_FIELDS = CREATE_FIELDS && |{ WA_FCAT-FIELDNAME } varchar(3)|.

      WHEN 'DATS'.

        CREATE_FIELDS = CREATE_FIELDS && |{ WA_FCAT-FIELDNAME } date|.

      WHEN 'TIMS'.

        CREATE_FIELDS = CREATE_FIELDS && |{ WA_FCAT-FIELDNAME } time|.

      WHEN 'RAW'.

        CREATE_FIELDS = CREATE_FIELDS && |{ WA_FCAT-FIELDNAME } nvarchar(max)|.

      WHEN 'NUMC' OR 'INT4' OR 'DEC' OR 'QUAN' OR 'CURR'.

        CREATE_FIELDS = CREATE_FIELDS && |{ WA_FCAT-FIELDNAME } float|.

    ENDCASE.

    CREATE_FIELDS = CREATE_FIELDS && ','.

    IF WA_FCAT-KEY EQ 'X'.

      IF CREATE_PKEY IS NOT INITIAL.

        CREATE_PKEY = CREATE_PKEY && ','.

      ENDIF.

      CREATE_PKEY = CREATE_PKEY && |[{ WA_FCAT-FIELDNAME }]|.

    ENDIF.

  ENDLOOP.

  DATA(TABLE) = `SAP_ZREPORT`.

  IF CREATE_PKEY IS INITIAL.

    DATA(CREATE_TABLE) = |CREATE TABLE { TABLE } ( { CREATE_FIELDS } )|.

  ELSE.

    CREATE_TABLE = |CREATE TABLE { TABLE } ( { CREATE_FIELDS } PRIMARY KEY ({ CREATE_PKEY }) )|.

  ENDIF.

...
```

**CREATE TABLE** SQL DDL statement is ready with all fields in the Field Catalog, along with Primary Keys and ready to be executed with **ADBC EXECUTE\_DDL** statement

Since I was creating SQL DB table fields with SAP fieldnames, Client asked to have **Field Description** in the Comment section of every field for identification, like the following:

![](/legacyfs/online/storage/blog_attachments/2023/03/DB_fields-2.png)

So I used **ALTER TABLE** SQL DDL statement to add Description in the Comment field

```
...

  LOOP AT SALV_META-T_FCAT ASSIGNING FIELD-SYMBOL(<FIELD>).

    CASE <FIELD>-DATATYPE.

      WHEN 'CHAR'.

        <FIELD>-TOOLTIP = |varchar({ <FIELD>-INTLEN })|.

      WHEN 'CUKY'.

        <FIELD>-TOOLTIP = |varchar(5)|.

      WHEN 'UNIT'.

        <FIELD>-TOOLTIP = |varchar(3)|.

      WHEN 'DATS'.

        <FIELD>-TOOLTIP = |date|.

      WHEN 'TIMS'.

        <FIELD>-TOOLTIP = |time|.

      WHEN 'RAW'.

        <FIELD>-TOOLTIP = |nvarchar(max)|.

      WHEN 'NUMC' OR 'INT4' OR 'DEC' OR 'QUAN' OR 'CURR'.

        <FIELD>-TOOLTIP = |float|.

    ENDCASE.

    REPLACE ALL OCCURRENCES OF '/'  IN <FIELD>-SELTEXT WITH '-'. " forward slash / is considered COMMENT in SQL

    IF <FIELD>-SELTEXT IS INITIAL. " COMMENT/DESCRIPTION cannot be blank in ALTER TABLE statement

      <FIELD>-SELTEXT = <FIELD>-FIELD...
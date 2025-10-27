---
title: Range and Sets.
url: https://blogs.sap.com/2023/02/03/range-and-sets./
source: SAP Blogs
date: 2023-02-04
fetch_date: 2025-10-04T05:40:35.986106
---

# Range and Sets.

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Range and Sets.

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46644&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Range and Sets.](/t5/application-development-and-automation-blog-posts/range-and-sets/ba-p/13551912)

![19sandesht](https://avatars.profile.sap.com/1/2/id1242ec2ece3ef6580bdd4bda252ec1278358b31e85571603f30558c4b5533ada_small.jpeg "19sandesht")

[19sandesht](https://community.sap.com/t5/user/viewprofilepage/user-id/827620)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46644)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46644)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551912)

‎2023 Feb 03
6:28 PM

[3
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46644/tab/all-users "Click here to see who gave kudos to this post.")

39,396

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

###### Ranges in ABAP are similar to the internal table that saves group values or value intervals and has various applications like passing values in select Query and submitting reports with values. Sets are used for saving the values to avoid hard coding in the program, where values can be changed in any system  weather modifiable or not.

# Ranges.

The range is also a Kind of standard internal table which has SIGN, OPTION, HIGH and LOW.

**A sign** has two possible values

**I** Inclusion

**E** Exclusion.

**An Option** has eight possible values

**EQ** Equal

**NE** Not Equal

**GE** Greater Than or Equal

**GT** Greater Than

**LE** Less Than or Equal

**LT** Less Than

**CP** Contains a Pattern.

**LOW** and **HIGH** are used to store the data which is to be compared in the combination
of Sign and Option, the Comparison is made and accordingly, data is processed.

Working with SAP ABAP come across many situations where Ranges are required for various purposes like selecting data from the database, deleting entries from Internal
Table, differentiating and sorting data from Internal Tables, and many more.

## Declaration Of Range.

The syntax used to declare the range and use to fill the data into the range table.

```
TYPES:r_typ TYPE RANGE OF sy-datum.

DATA: r_dtm  TYPE rng_typ,

      wa_rng TYPE LINE OF rng_typ.

APPEND VALUE #( sign = 'I' option = 'EQ' low = dt_frm high = dt_to ) TO r_dtm.

LOOP AT 1lt_dt INTO wa.

  wa_rng-sing-sign = 'I'.

  wa_rng-option = 'EQ'.

  wa_rng-llow = wa-sfield.

  APPEND wa_rng TO r_dtm.

ENDLOOP.

r_dtm = VALUE #( FOR <wa> IN 1lt_dt "WHERE  ( sfield = ' ' )  "" Where Condition For Consitional Filling

                        LET lv_sign = 'I' lv_option = 'EQ' IN                    of Data In Range

                            sign   = lv_sign

                            option = lv_option

                          ( low   = <wa>-sfield ) ).
```

## Use Of Range.

Various use of Range in SAP ABAP.

#### Selecting Data From Database(Select Query).

```
SELECT belnr,

       gjahr,

       bukrs

  FROM bkpf

  INTO @tbl

   WHERE budat IN @r_dtm.
```

#### Deleting Data from Internal Table.

```
DELETE tbl WHERE budat IN r_dtm.
```

#### Loop On Internal Table.

```
LOOP AT tbl INTO wa WHERE budat IN r_dtm.

ENDLOOP.
```

#### Submit Program.

```
SUBMIT sap1000

WITH budat IN r_dtm

AND RETURN.
```

# Sets

Sets are the standard functionality that provides the privilege to avoid hard coding in
ABAP, the set is created in GS01, GS02 for change, and GS03 for Display.
There are four types of sets:
**1. Basic Sets** are used to store multiple values for the particular field of a table.
**2. Single Sets** are used to combine basic sets in Single sets.
**3. Multi sets** are used to combine basic sets or single sets into Single sets.
**4. Key Figures** are used for report painters.

Steps to Create Set.

![](/legacyfs/online/storage/blog_attachments/2023/01/GS01-Initail-Screen-1-1.png)

GS01- Initial Set Creation Screen

Provide a name to the set and also a table name and hit ‘Enter’.

A pop-up will appear asking for the field of the Set, provide the field name.

![](/legacyfs/online/storage/blog_attachments/2023/01/GS01-Values-Maintain.png)

Once the set is created we can maintain the values in it.
For changing the entries in Set T-code GS02 is used.

#### Adding Data Into Sets.

Whenever the Harcode is to be avoided from the code we can use a set there which can be maintained in PRD also so no code changes are required.

While Maintaining data in sets data can be in the form of from values to values and
also single value as multiple entries.

#### Getting Data From Sets.

##### Using FM.

```
DATA set_vallues TYPE STANDARD TABLE OF rgsb4.

CALL FUNCTION 'G_SET_GET_ALL_VALUES'

  EXPORTING

    client        = sy-mandt

    setnr         = 'ZTEST'

    table         = 'BKPF'

    fieldname     = 'BLART'

  TABLES

    set_values    = set_vallues

  EXCEPTIONS

    set_not_found = 1

    OTHERS        = 2.

IF sy-subrc <> 0.

* Implement suitable error handling here

ENDIF.
```

##### Selecting Directly into Range.

```
TYPES:r_typ TYPE RANGE OF bkpf-blart.

DATA: r_dtm TYPE rng_typ.

SELECT valsign AS sign,

       valoption AS option,

       valfrom AS low,

       valto AS high

  FROM setleaf

   INTO CORRESPONDING FIELDS OF TABLE @rng_typ

    WHERE setname = 'ZTEST'.
```

Other FM used for sets

G\_SET\_CREATION for creation of set.
G\_SET\_MAINTENANCE to maintain set.
G\_SET\_GET\_ID\_FROM\_NAME to get set ID.
G\_SET\_FETCH set value from set ID.

Finally, from an end-user point of view, it will be easy to maintain values in the set to get desired output.

I’m looking forward to hearing more. Feel free to comment and discuss.

Best regards, thanks for reading.

**Sandesh Thakare**

1 Comment

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin
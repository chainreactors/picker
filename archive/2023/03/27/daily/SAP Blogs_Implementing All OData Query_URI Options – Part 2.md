---
title: Implementing All OData Query/URI Options – Part 2
url: https://blogs.sap.com/2023/03/26/implementing-all-odata-query-uri-options-part-2/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:46:11.035753
---

# Implementing All OData Query/URI Options – Part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Implementing All OData Query/URI Options - Part 2

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160044&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Implementing All OData Query/URI Options - Part 2](/t5/technology-blog-posts-by-members/implementing-all-odata-query-uri-options-part-2/ba-p/13549957)

![nitinksh1](https://avatars.profile.sap.com/a/c/idacef170ce1e7f2f7c7ed45f61d80f3b3b4fa1466fcc18c01a0505b6b26d85535_small.jpeg "nitinksh1")

[nitinksh1](https://community.sap.com/t5/user/viewprofilepage/user-id/45127)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160044)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160044)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549957)

‎2023 Mar 26
12:54 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160044/tab/all-users "Click here to see who gave kudos to this post.")

40,501

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [NW ABAP Gateway (OData)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Gateway%2520%28OData%29/pd-p/181161894649260056016734803547327)
* [NW ABAP Web Services](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Web%2520Services/pd-p/99891761267046184358097136821575)

* [NW ABAP Gateway (OData)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BGateway%2B%252528OData%252529/pd-p/181161894649260056016734803547327)
* [NW ABAP Web Services

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BWeb%2BServices/pd-p/99891761267046184358097136821575)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (3)

## Introduction

In the previous blog, we have discussed about the URI calls which do not require any custom implementation. In this blog, we will go through the URI's which do require custom implementation.

## Steps

We can divide OData URI to 2 parts:

1. **Do Not Need Custom Implementation ([Implementing All OData Query/URI Options – Part 1](https://blogs.sap.com/2023/03/26/implementing-all-odata-query-uri-options-part-1/))**

   1. $select

   2. $count

   3. $expand

   4. $format

   5. $links

   6. $value

2. **Need Custom Implementation** (This Blog)

   1. $orderby

   2. $top

   3. $skip

   4. $filter

   5. $inlinecount

   6. $skiptoken

## Implementation

**1. $orderby:** The $orderby option is used to specify a sort order for the results of a query. It is used in the URL of an OData service to indicate how the results should be sorted.

The syntax for the $orderby option is as follows: *$orderby=propertyName [asc|desc]*, where propertyName is the name of the property by which the results should be sorted, and "asc" or "desc" is used to specify the sort order (ascending or descending, respectively).

For example, if we want to retrieve a list of customers and sort them by last name in descending order, the URL would look like this:

```
http://<host>/sap/opu/odata/sap/<service>/Customers?$orderby=LastName desc
```

It is also possible to sort by multiple properties using the $orderby option, by separating each property with a comma.

```
http://<host>/sap/opu/odata/sap/<service>/Customers?$orderby=LastName desc, FirstName asc
```

The code the $orderby can be written as:

```
  METHOD ekkoset_get_entityset.

*- To get data from DB

    SELECT * FROM ekko INTO TABLE @DATA(lt_ekko) UP TO 10 ROWS.

*- Check the $orderby in the Odata Query

    READ TABLE it_order INTO DATA(ls_order) INDEX 1.

    IF sy-subrc IS INITIAL.

      IF ls_order-order = 'desc'.

        SORT lt_ekko BY (ls_order-property) DESCENDING.

      ELSE.

        SORT lt_ekko BY (ls_order-property) ASCENDING.

      ENDIF.

    ENDIF.

*- Check the size of the table for $inlinecount

    IF io_tech_request_context->has_inlinecount( ) = abap_true.

      DESCRIBE TABLE lt_ekko LINES DATA(lv_size).

      es_response_context-inlinecount = lv_size.

    ENDIF.

    MOVE-CORRESPONDING lt_ekko TO et_entityset.

  ENDMETHOD.
```

Below is the output:

![](/legacyfs/online/storage/blog_attachments/2023/03/1.-orderby.png)

1. $orderby.jpg

Another better way to use the $orderby can be the standard way of using it, displayed below:

```
*- Check the $orderby in the Odata Query

    /iwbep/cl_mgw_data_util=>orderby(

      EXPORTING

        it_order =  it_order                " the sorting order

      CHANGING

        ct_data  = lt_ekko

    ).
```

**2. $top:** The $top option is used to specify the maximum number of results that should be returned in a query. It is used in the URL of an OData service to indicate how many results should be returned. The syntax for the $top option is as follows: $top=n, where n is an integer indicating the number of results that should be returned.

For example, if we want to retrieve the top 10 customers, the URL would look like this:

```
http://<host>/sap/opu/odata/sap/<service>/Customers?$top=10
```

The $top option can be used in combination with other options such as $filter, $select and $orderby to further refine the results of a query.

```
http://<host>/sap/opu/odata/sap/<service>/Customers?$filter=Country eq 'US'&$top=5&$orderby=LastName desc
```

It's important to note that the $top option is used to limit the number of records returned in one response and not to restrict the total number of records returned by the OData service.

```
  METHOD ekkoset_get_entityset.

*- To get data from DB

    SELECT * FROM ekko INTO TABLE @DATA(lt_ekko) UP TO 10 ROWS.

*- Check the $orderby in the Odata Query

    /iwbep/cl_mgw_data_util=>orderby(

      EXPORTING

        it_order =  it_order                " the sorting order

      CHANGING

        ct_data  = lt_ekko

    ).

*- For paging i.e. $top and $skip

    /iwbep/cl_mgw_data_util=>paging(

      EXPORTING

        is_paging = is_paging                " paging structure

      CHANGING

        ct_data   = lt_ekko

    ).

*- Check the size of the table for $inlinecount

    IF io_tech_request_context->has_inlinecount( ) = abap_true.

      DESCRIBE TABLE lt_ekko LINES DATA(lv_size).

      es_response_context-inlinecount = lv_size.

    ENDIF.

    MOVE-CORRESPONDING lt_ekko TO et_entityset.

  ENDMETHOD.
```

We can use it as below:

![](/legacyfs/online/storage/blog_attachments/2023/03/2.-top-1.png)

2. $top.jpg

**3. $skip:** The $skip option is used to specify the number of results that should be skipped before returning the results in a query. It is used in the URL of an OData service to indicate how many results should be skipped. The syntax for the $skip option is as follows: $skip=n, where n is an integer indicating the number of results that should be skipped.

For example, if we want to retrieve all customers but skip the first 10, the URL would look like this:

```
http://<host>/sap/opu/odata/sap/<service>/Customers?$skip=10
```

The $skip...
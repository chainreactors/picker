---
title: Arithmetic Operations with different data types in CDS views
url: https://blogs.sap.com/2023/03/29/arithmetic-operations-with-different-data-types-in-cds-views/
source: SAP Blogs
date: 2023-03-30
fetch_date: 2025-10-04T11:06:45.804194
---

# Arithmetic Operations with different data types in CDS views

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Arithmetic Operations with different data types in...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161784&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Arithmetic Operations with different data types in CDS views](/t5/technology-blog-posts-by-members/arithmetic-operations-with-different-data-types-in-cds-views/ba-p/13559944)

![Dhanasekar_C](https://avatars.profile.sap.com/6/d/id6d63904ba647dd6911d266d5c070a3208d3ad8ae2ca8e41950f9b6d301f4d94c_small.jpeg "Dhanasekar_C")

[Dhanasekar\_C](https://community.sap.com/t5/user/viewprofilepage/user-id/847331)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161784)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161784)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559944)

‎2023 Mar 29
11:12 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161784/tab/all-users "Click here to see who gave kudos to this post.")

12,576

* SAP Managed Tags
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

View products (1)

## **Introduction**

For the calculation of any two numbers, we need at least one Arithmetic Operator. It basically comprises operations such as Addition [+], Subtraction [-], Multiplication [\*], and Division [/]. And there are different data types such as INT, CHAR, DATS…

## **Content**

Usually, we can't perform a calculation with parameters whose datatypes are different. In this blog, we are going to see how to perform Arithmetic Operations with different data types in CDS views. In the below images, a list of datatypes and their conversion logic is given.

![](/legacyfs/online/storage/blog_attachments/2023/03/types-of-data.png)![](/legacyfs/online/storage/blog_attachments/2023/03/all-flow-1.png)

     If a built-in data type from ABAP Dictionary is specified for datatype, no further restrictions apply to combinations with "x". The following rules apply to the other combinations:

* In combinations using "y", the target data type must be long enough.

* In combinations using "z", the lengths of the data types must match exactly.

* In the case of combinations with "p" or "d", no built-in data type from ABAP Dictionary can be specified. A data element must be specified as the target data type instead.

1. 1. In combinations with "d", the data element can have a suitable target type in accordance with the table above and with any length.

   2. In combinations with "p", the data element must have the built-in data type and the same length as the data type of the operand.

```
{

//Division

  division(10,3,4)                 as value1, // [Ans:3.3333]

  div(55,5)                        as value2, // [Ans:11]

  (10.5  / 3.2)                    as value3, // [Ans:3.28125]

// multiplication

  (10  * 3)                        as value4, // [Ans:30]

  (10 *6 * 3)                      as value5, // [Ans:180]

//Modulo

  mod(2,3)                         as value6, // [Ans:2]

// Addition

  (2 +3)                           as value7, // [Ans:5]

  (2.2 + 3.7)                      as value8, // [Ans:5.9]

// (2 + 3.7) as value8--> is not possible as both are different data types

//subtraction

  (2 -3)                           as value9, // [Ans:-1]

  (21 -1)                          as value10, // [Ans:20]

  (21.5 - 1.7)                     as value11, // [Ans:1.98]

//(21.5 - 1) as value11--> is not possible as both are different data types

//BODMAS

  (2+3-4*3)                        as value12, // [Ans:-7]

  cast( 2+3-4*3 as abap.fltp)/ 2.0 as value13  // [Ans:-3.5]

// As ‘/’ only support fltp data type, we changed to fltp

}
```

Suppose we have a parameter1 as CHAR datatype but need to perform an Arithmetic operation like addition, we can’t directly change CHAR to INT as shown in the image.

![](/legacyfs/online/storage/blog_attachments/2023/03/cant-flow.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/flow-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/flow-2.png)

So, in such a case, we can change CHAR datatype to INT by having NUMC as intermediate,

CHAR --> NUMC --> INT

```
cast ( cast (parameter1 as abap.numc( 8 )) as  abap.int8)as datatype_int
```

## **Conclusion**

Using this blog post, it will be easy to understand the Arithmetic Operations with different data types and conversion logic between different data types, especially for beginners. Kindly share your feedback or doubts in a comment section and please follow my 24\_dhana for future posts. And feel free to ask any questions related to data and analytics in our [SAP Community](https://answers.sap.com/tags/87817424-f4e7-46f2-af14-88bf0f4ba034) forum and follow up for more related [blogs](https://blogs.sap.com/tags/87817424-f4e7-46f2-af14-88bf0f4ba034/).

Thank you

### Reference

[ABAP CDS - cast\_expr](https://help.sap.com/doc/abapdocu_751_index_htm/7.51/en-us/abencds_f1_cast_expression.htm)

### Related topics

[Casting](https://help.sap.com/doc/abapdocu_751_index_htm/7.51/en-us/abencasting_guidl.htm#:~:text=Casting%20refers%20to%20the%20process,as%20%27conversion%27%20in%20ABAP.)

[String Functions](https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/abencds_f1_sql_functions_character.htm)

* [Arithmetic Operations](/t5/tag/Arithmetic%20Operations/tg-p/board-id/technology-blog-members)
* [Arithmetic Operations with different data types in CDS views](/t5/tag/Arithmetic%20Operations%20with%20different%20data%20types%20in%20CDS%20views/tg-p/board-id/technology-blog-members)
* [CAST function in cds views](/t5/tag/CAST%20function%20in%20cds%20views/tg-p/board-id/technology-blog-members)
* [cds views](/t5/tag/cds%20views/tg-p/board-id/technology-blog-members)
* [cds views sap](/t5/tag/cds%20views%20sap/tg-p/board-id/technology-blog-members)
* [different data types in CDS views](/t5/tag/different%20data%20types%20in%20CDS%20views/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Farithmetic-operations-with-different-data-types-in-cds-views%2Fba-p%2F13559944%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [SAP S4HANA Plant Maintenance for dummi...
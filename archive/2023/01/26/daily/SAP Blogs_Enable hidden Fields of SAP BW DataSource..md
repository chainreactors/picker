---
title: Enable hidden Fields of SAP BW DataSource.
url: https://blogs.sap.com/2023/01/25/enable-hidden-fields-of-sap-bw-datasource./
source: SAP Blogs
date: 2023-01-26
fetch_date: 2025-10-04T04:51:43.509158
---

# Enable hidden Fields of SAP BW DataSource.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Enable hidden Fields of SAP BW DataSource

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160706&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enable hidden Fields of SAP BW DataSource](/t5/technology-blog-posts-by-members/enable-hidden-fields-of-sap-bw-datasource/ba-p/13554049)

![maheshsinghmony](https://avatars.profile.sap.com/b/3/idb365ed6e0985e7239e3af2b4539dc94c0166da0f51d7ce224372cb380e3568a2_small.jpeg "maheshsinghmony")

[maheshsinghmony](https://community.sap.com/t5/user/viewprofilepage/user-id/357842)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160706)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160706)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554049)

‎2023 Jan 25
10:26 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160706/tab/all-users "Click here to see who gave kudos to this post.")

7,554

* SAP Managed Tags
* [BW (SAP Business Warehouse)](https://community.sap.com/t5/c-khhcw49343/BW%2520%28SAP%2520Business%2520Warehouse%29/pd-p/242586194391178517100436979900901)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [BW SAP HANA Data Warehousing](https://community.sap.com/t5/c-khhcw49343/BW%2520SAP%2520HANA%2520Data%2520Warehousing/pd-p/337684911283545157914465705009179)

* [BW (SAP Business Warehouse)

  Software Product Function](/t5/c-khhcw49343/BW%2B%252528SAP%2BBusiness%2BWarehouse%252529/pd-p/242586194391178517100436979900901)
* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [BW SAP HANA Data Warehousing

  Software Product Function](/t5/c-khhcw49343/BW%2BSAP%2BHANA%2BData%2BWarehousing/pd-p/337684911283545157914465705009179)

View products (3)

## Fields hidden by SAP in Standard BW Data Sources

Many a times you would have observed that there are a few fields present in the extract structure of the SAP BW datasource but are not available in RSA6 or the data source which is replicated in BW.

This Article talks about all steps as to how can we enable fields present in the extract structure of the data source, make them visible in RSA3 and fetch the data in BW.

## Let's take an Example.

Here we take an example of a data source 0COMP\_CODE\_TEXT No. of Fields in the Extract structure is 7.

![](/legacyfs/online/storage/blog_attachments/2023/01/0Comp_code_text.png)
**No. of fields in RSA3 output of the Datasource is ‘2’:**

![](/legacyfs/online/storage/blog_attachments/2023/01/2-32.png)

**Fields present in RSA6 in the source system for the data source 0COMP\_CODE\_TEXT**

![](/legacyfs/online/storage/blog_attachments/2023/01/3-25.png)

**Data source in SAP BW.**

![](/legacyfs/online/storage/blog_attachments/2023/01/4-20.png)

**The Reason for this:**

The value for the field SELECTION of the table ROOSFIELD for the fields which are not visible in the Data source or RSA3 is maintained as ‘A’.

![](/legacyfs/online/storage/blog_attachments/2023/01/6-17.png)

If a request for a Data Source is scheduled in the Business Information Warehouse, selection conditions are specified across certain fields. The property that determines whether a selection in BW using a field is possible or required is established in the Data Source in the Source System.

In addition, the visibility of the field in BW can be set.

**Definition of the individual values:**

**'A'**: Field is hidden in OLTP and BW; property cannot be changed by the customer.

**'M'**: The Data Source requires a selection across this field before it is able to extract data (Required field for the generation of a request); property cannot be changed by the customer

**'X':** The Data Source can select across this field. The customer can change selections and visibility (the field is currently visible and selectable, compare with 'P', '3')

**'1'**: Pure selection field for the Data Source. The customer can change the selection, but not the visibility (the field is currently selectable, compare with '2').

**'2'**: Pure selection field for the Data Source. The customer can change the selection, but not the visibility (field is currently no selectable, compare with '1').

**'3**': The Data Source can select across this field. The customer can change selection and visibility (the field is currently not visible not selectable, compare with 'P', 'X')

**'4'**: The Data Source cannot select across this field. The customer can change visibility (the field is currently not visible, compare with ' ')

**Summary:**

|  |  |
| --- | --- |
| **Filed Attribute** | **Description** |
| A | Field in OLTP and BW Hidden by SAP |
| M | Selection Required, Visible |
|  | No Selection Possible, Visibility Set |
| P | Selection Adjustable, Visibility Set. |
| X | Selection Adjustable, Visibility Set |
| 1 | Pure Selection Field, Selection Set |
| 2 | Pure Selection Field, Selection Set |
| 3 | Selection Adjustable, Visibility Adjustable |
| 4 | No Selection Possible, Visibility Adjustable |

## Here are Steps to make the field visible in RSA3 and to populate data into BI.

Let’s consider the filed DATETO (Valid-to date) to be displayed in RSA3 and in the Data source so that the data can be extracted into BI.

**STEPS to be followed:**

1. Create a test program through the transaction SE38. Write the below code in the program. Activate it and then execute.

   ![](/legacyfs/online/storage/blog_attachments/2023/01/7-15.png)

1. After execution you would see that the value of the filed selection has been changed from ‘A’ to ‘P’.![](/legacyfs/online/storage/blog_attachments/2023/01/8-17.png)

1. Go to RSA6 and find the data source 0COMP\_CODE\_TEXT and select Change.
   ![](/legacyfs/online/storage/blog_attachments/2023/01/9-10.png)

1. Put a check in the checkbox Selection if you want it to be a part of the selection in RSA3 and in the Infopackage and Generate the data source.![](/legacyfs/online/storage/blog_attachments/2023/01/10-10.png)

1. Go to RSA3 and you will find the new filed DATETO in your output.

   PS. Note: If there is data it would automatically get populated in this case there isn’t any data in the new filed

   ![](/legacyfs/online/storage/blog_attachments/2023/01/11-10.png)

1. Go to the BI System find the data source and Replicate it.

   ![](/legacyfs/online/storage/blog_attachments/2023/01/12-7.png)

1. After replication the new field will appear in the data source.

   ![](/legacyfs/online/storage/blog_attachments/2023/01/13-6.png)

To Summarize following the above steps you can un-hide / enable the fields present in the Extract Structure of an SAP BW Datasource.

## Applies to:

ECC 6.0 and BI 3.x and 7.0, 7.3 etc.

**References & Related Links:** <https://answers.sap.com/questions/960374/unhide-fields-of-datasource.html?childToView=960565>

<https://answers.sap.com/questions/10055053/fields-hidden-by-sap-in-std-bc-data-sources.html>

**(Related SAP ...
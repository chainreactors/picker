---
title: Table Comparison Transform- SAP BODS
url: https://blogs.sap.com/2022/12/03/table-comparison-transform-sap-bods/
source: SAP Blogs
date: 2022-12-04
fetch_date: 2025-10-04T00:28:42.879558
---

# Table Comparison Transform- SAP BODS

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Table Comparison Transform- SAP BODS

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161574&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Table Comparison Transform- SAP BODS](/t5/technology-blog-posts-by-members/table-comparison-transform-sap-bods/ba-p/13558926)

![ashishpinjwani](https://avatars.profile.sap.com/7/6/id76b2b81b71aaa3f47a7e436cad34a38e695d2e5b31e62602db2f7d226828ccaa_small.jpeg "ashishpinjwani")

[ashishpinjwani](https://community.sap.com/t5/user/viewprofilepage/user-id/685096)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161574)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161574)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558926)

‎2022 Dec 03
9:24 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161574/tab/all-users "Click here to see who gave kudos to this post.")

24,356

* SAP Managed Tags
* [SAP Data Insight](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Insight/pd-p/01200314690800000360)
* [SAP Data Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Services/pd-p/01200314690800000395)

* [SAP Data Insight

  SAP Data Insight](/t5/c-khhcw49343/SAP%2BData%2BInsight/pd-p/01200314690800000360)
* [SAP Data Services

  SAP Data Services](/t5/c-khhcw49343/SAP%2BData%2BServices/pd-p/01200314690800000395)

View products (2)

Hello Readers,

***Purpose of this Blog :***

In our last blog we went through some commonly used platform transforms in bods, you can check that out on below link

<https://blogs.sap.com/2022/11/04/sap-bods-commonly-used-platform-transforms/>

Today, in this blog i will cover the data integration transform Table comparison with Map operation  in SAP BODS which is widely used to handle many data management scenarios.

***What’s in it for you?***

Table comparison and map operation together are extensively used to handle Slowly Changing Dimensions (SCD) scenarios, duplicate data issue etc

Lets deep dive into the table comparison and map operation -

***General Desc-***

Table comparison transform is used to compare 2 data sets based on some primary columns and generate opcodes (Insert, update or delete) based on comparison, These opcodes then are controlled using Map Operation to take the necessary/relevant action for those records based on user requirements.

***Implementation-***

To implement Table transform and map operation in BODS, use below instructions –

* Pull the source table with some relevant data

* Use query transform to pull the required fields

* Drag Table Comparison transform from data integration and map operation from platform transforms using local object library->transformations section.

* Create a permanent table as target table and connect as output to map transform.

![](/legacyfs/online/storage/blog_attachments/2022/11/TC_MO_DESIGN.png)

Table Comparison and Map Operation DF Design

* Now double click on table comparison transform to setup different options

  + First you need to provide comparison table in table name, you can select using your available datastores from dropdown window

  + Select the comparison method best suited for your requirement, comparison method plays significance in performance tuning for this transform. below are some details about each method

    - **Row by Row Select** - This comparison method follows linear search technique to compare records, it can be used with any number of records coming from source

    - **Cached Comparison** - This comparison method uses cache memory to compare the records and this is suitable for smaller number of records coming from source as cache memory is generally small in size

    - **Sorted Input** -  This comparison method follows binary search technique to compare records, it can be used with any number of records coming from source. This method requires input data to be sorted based on columns you are using as a part of primary column

***Note : Out of above comparison methods, most widely used is sorted input because of its performance, cached comparison should only be used when you have smaller comparison tables.***

* + Then provide input primary columns based on which record will be identified and provide compare columns which you want to compare values for.

The setup of table comparison transform to cover below cases would look like this-

![](/legacyfs/online/storage/blog_attachments/2022/12/TC1.png)

Table Comparison Setup1

![](/legacyfs/online/storage/blog_attachments/2022/12/TC2.png)

Table Comparison 2

I will cover below few basic scenarios to understand the working of these 2 transforms.

1. ***Identifying and working with new records***

2. ***Identifying existing records and handling the same***

Details :

1. ***Identifying and working with new records -***

Consider a below source data and target data.

![](/legacyfs/online/storage/blog_attachments/2022/11/source_tc.png)

Source Data

![](/legacyfs/online/storage/blog_attachments/2022/11/target_Tc.png)

Target Data

In this scenario,

1. Table comparison compares the source data with comparison table and identifies the records as insert as they are not present in the comparison table

2. These records are considered as new record and opcode with letter "I" will be used to denote these

3. In the next map operation can be used to handle this insert data scenario, we have 5 options to use from the list for opcode identified (see screenshot)

4. Using map operation options for a generated opcode you can actually decide whether you want to insert, update or delete records. In our case we have used insert to insert so that it can insert new records

![](/legacyfs/online/storage/blog_attachments/2022/12/mo_insert2.png)

Map Operation Setup

If you want to see generated opcodes, you would need to execute your job in debug mode then you can actually see output of table comparison transform and how it generates opcodes. (see below screenshot after job execution)

![](/legacyfs/online/storage/blog_attachments/2022/12/Insert-scenario.png)

Insert Scenario

After Execution - Source and Target data ouput

![](/legacyfs/online/storage/blog_attachments/2022/12/source_target_insert.png)

Now Lets deep dive into 2nd scenario where we will see how we can handle already existing records.

Here we will try to do two things -

a. We will update the existing records and

b.We will insert our updates as a new record

1. We will keep the table comparison setup same as above case.

2. We have updated 3rd row in our source data, we have changed emp\_city and emp\_country (see screenshot)

3. Now 3rd row will be marked with opcode update "U" and we will use map operation to handle the update opcode

4. First we will set update to update in map operation and check the ouput, refer below screenshots before and after execution of job.

**Before Job execution source and Target data- We updated the 3rd row.**

![](/legacyfs/online/storage/blog_attachments/2022/12/UPDATE_UPDATE.png)

...
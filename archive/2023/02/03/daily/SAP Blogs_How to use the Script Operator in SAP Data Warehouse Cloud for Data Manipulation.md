---
title: How to use the Script Operator in SAP Data Warehouse Cloud for Data Manipulation
url: https://blogs.sap.com/2023/02/02/how-to-use-the-script-operator-in-sap-data-warehouse-cloud-for-data-manipulation/
source: SAP Blogs
date: 2023-02-03
fetch_date: 2025-10-04T05:34:38.109748
---

# How to use the Script Operator in SAP Data Warehouse Cloud for Data Manipulation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to use the Script Operator in SAP Data Warehou...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161078&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to use the Script Operator in SAP Data Warehouse Cloud for Data Manipulation](/t5/technology-blog-posts-by-sap/how-to-use-the-script-operator-in-sap-data-warehouse-cloud-for-data/ba-p/13559651)

![P_Plazi](https://avatars.profile.sap.com/2/7/id2717e6bbc77dec8de1c22cfadccf7bef39f3076c00267b7e201b0190d1fc50eb_small.jpeg "P_Plazi")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[P\_Plazi](https://community.sap.com/t5/user/viewprofilepage/user-id/122578)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161078)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161078)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559651)

‎2023 Feb 02
10:34 PM

[19
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161078/tab/all-users "Click here to see who gave kudos to this post.")

4,727

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

Welcome to our blog on the SAP Data Warehouse Cloud *Script Operator*! As of the current release, the *Script Operator* is available to use and combines the usability of the commonly known python libraries [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) together with capabilities of SAP Data Warehouse Cloud to create Data Flows and individual views of information. It is a versatile operator that can be used for a wide range of tasks, such as data cleansing, data transformation, and many more. In this blog, we will be diving into the various capabilities by providing examples and best practices for SAP Data Warehouse Cloud projects.

The content of this Blogpost originates from a cooperation with niga0001 and s.morio.

**Note!**You can jump to any task in this post from the Agenda below. Each one works as a standalone solution to fulfil the underlying task.

Task 0 - Possibilities of the SAP Data Warehouse Cloud Script Operator

Task 1 - Classify numerical data as bins

Task 2 - Datatype conversion from Datetime to String

Task 3 - Extraction of Substrings

Task 4 - Generating unique Hash Keys

Task 5 - Unpivot Data

Task 6 - Filter with regular expressions

# Task 0 - Possibilities of the SAP Data Warehouse Cloud Script Operator

## Supported functions in Script Operator

The *Script Operator* comes with an interface to use python through a SAP Data Warehouse Cloud Data Flow. the included libraries are restricted to Pandas, NumPy and several built-in module operations. Within these libraries, there are some restrictions as shown in the operator's [documentation](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/c8a54ee704e94e15926551293243fd1d/73e8ba1a69cd4eeba722b458a253779d.html). Data given through a data flow is passed into the *Script Operator*in form of a pandas data frame. Thus said, it is possible to reach each entry through its Column Keys. When using one of the libraries given, there is no prefix necessary - in the form of pd.dataframe - to reach a function within. For example, in case of simple adding 10 to every data entry, there is a variable extracted by entering data.add(10) into the operator's console. If you are new to SAP Data Warehouse Cloud or the *Script Operator*, the video below can help you find the code editor for your script operations.

![](/legacyfs/online/storage/blog_attachments/2023/02/Untitled-Project.gif)

## The Script Operator

The SAP Data Warehouse Cloud Script Operator allows to write code into a dedicated python editor while allowing to delete or add columns in a panel below. Keep in mind that every calculated column populated through the script needs to be included manually in design time of the underlying data flow. As of the current release, there is no possibility to implement new columns in run time.

Every script has the same structure beginning with a function definition for the transformation of the passed data as a data frame. To exit the script and save the results, you need to use a return statement including the data frame to pass through the data flow. Like every SAP Data Warehouse Cloud data flow, you need a *Source Table* and a *Target Table.* After deploying the *Target Table* there is an option to decide whether data should be appended, truncated, or deleted. In case there is a script overwriting existing values due to data transformation, append will work the right way since it is only able to append new data to the data frame. If the intend is to overwrite existing data, make sure to choose truncate to delete the information in a first step and refill the data entries with new values. The Script below shows the basic structure of a python script within SAP Data Warehouse Cloud.

```
def transformation(data):

   # Fill in your scripts here with data as a source

   # and save the values into data as output

   return data
```

## Limitations through SAP Data Warehouse Cloud

As of today, SAP Data Warehouse Cloud has some major limitations when working with the script operator. Functions that require the dataset as a whole cannot be processed due to the batching in SAP Data Warehouse Cloud. Datasets have a maximum batch size of less than 100.000 entries and use an ideal batch size for the system. The description of this feature describes it as only using a manual number for batch size in case the manual data entry is less than the system's number. Therefore, it is not possible to simply drop duplicates by using the given function from pandas. In case there is a cut between the batches with a duplicate appearing once in different batches, they will not be detected as duplicates and the process ends up still having these duplicates. The preferred approach for this task is to use SQL-Script.

Another issue with SAP Data Warehouse Cloud is the requirement to have all Column Keys passed before executing the script. It is not possible to create new columns dynamically while executing the script as described before. One of the approaches affected by this limitation is the pivot functionality. There are several workarounds to think of, for example, you want to pivot from a Year and a Value Column, a simple CSV-File created in MS Excel might work using the [=SEQUENCE(row, column, start, end)] function in Excel. Cross joining this table with the *Source Table*results in a data frame containing every column necessary.

## The Importance of the Script Operator

The Script Operator finds some good use in preprocessing operations on data and is used for separate data manipulation in case SQL is not applicable or the user is more familiar with python. Instead of doing several steps for ordering data and ...
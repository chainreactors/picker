---
title: Using Formula in SAP ME data collection
url: https://blogs.sap.com/2023/02/15/using-formula-in-sap-me-data-collection/
source: SAP Blogs
date: 2023-02-16
fetch_date: 2025-10-04T06:45:41.332531
---

# Using Formula in SAP ME data collection

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* Using Formula in SAP ME data collection

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1418&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Formula in SAP ME data collection](/t5/product-lifecycle-management-blog-posts-by-members/using-formula-in-sap-me-data-collection/ba-p/13548531)

![t_ramkumar73](https://avatars.profile.sap.com/2/3/id2349005d8a07b217059d26d2085e6cb947606af7323717e1f0b11dfc614eb837_small.jpeg "t_ramkumar73")

[t\_ramkumar73](https://community.sap.com/t5/user/viewprofilepage/user-id/124644)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1418)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1418)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548531)

‎2023 Feb 15
11:16 PM

[7
Kudos](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1418/tab/all-users "Click here to see who gave kudos to this post.")

2,447

* SAP Managed Tags
* [SAP Manufacturing Execution](https://community.sap.com/t5/c-khhcw49343/SAP%2520Manufacturing%2520Execution/pd-p/01200615320800000731)

* [SAP Manufacturing Execution

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BManufacturing%2BExecution/pd-p/01200615320800000731)

View products (1)

Hello Everyone,

SAP ME provides a configurable feature to do data collection from the POD and record it for SFC numbers, resources, and work centers. The data collected will be stored in SAP ME WIP database which can be accessed and processed for further analysis. The collected data can be of type Numeric, Boolean, Formula, Text, and Data Field List.

In this blog, we will see how to use formula in the data collection process. When we use Formula as the DC data type, then user defined formula will be used to calculate the value for the DC parameter instead of the user keying-in the value.

## High-Level Overview

1. Using formula in Data collection with data collected from same DC group

2. Using formula in Data collection with data collected from different DC group

3. Using formula in Data collection with data being collected at different operation

## Prerequisite:

1. To use the data collection formula capabilities, you may need to enable the use of Java
   Script on the SAP ME server.

## SAP ME supports the below methods in DC formula:

1. **callEJB() :** use this method to call the Enterprise JavaBeans

2. **executeQuery() :** use this method to execute an SQL query on the SAP WIP database.

3. **findSingleParameter() :** use this method with arguments to read a value. Each argument must be enclosed either with single or double quotes.

4. **getEJBProperties() :** Use this method to retrieve one or more properties from the EJB.

5. **print() :** Use this method to print the string value of the variable. Use it for the debugging/testing purpose only. The print result can be seen in Log Viewer (Developer Traces view).

6. **printAll() :** Use this method to print all the variables available to the script. Use it for the debugging/testing purpose only. The printAll result can be seen in Log Viewer (Developer Traces view).

7. **exit() :** use this method to stop the script execution.

## Using formula in Data Collection:

### 1. Using formula in Data collection with data collected from same DC group

1. Create a DC group

2. Create required DC parameters (with data type as Numeric) and associate it to the dc group

3. Create one parameter with data types as Formula to calculate the value

4. Associate the dc group to the operation

5. Open standard POD-SFC and start and stop the operation by collecting the DC

6. The system automatically calculates the Volume Z\_VOLUME (4th DC Parameter) using the formula L \* W \* H

7. Verify the calculated parameter from Data Collection Results Report

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig1-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig2-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig3-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig4-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig5-2.jpg)

### 2. Using formula in Data collection with data collected from different DC group

1. Create DC Group Z\_LENGTH (Parameter Z\_LENGTH)

2. Create DC Group Z\_WIDTH (Parameter Z\_WIDTH)

3. Create DC Group Z\_HEIGHT (Parameter Z\_HEIGHT)

4. Create DC Group Z\_VOLUME (Parameter Z\_VOLUME)

5. All 4 DC groups must be assigned in the same operation

6. From the Pod-SFC, start the SFC and collect the DC

7. The user will enter the value in the 3 parameters at the same operation for Length, Width & Height

8. The system automatically calculates the Volume Z\_VOLUME (4th DC Parameter) using the formula L \* W \* H

9. Verify the calculated parameter from Data Collection Results Report

##### Note:

To read the value of the parameter from different DC group, we will use the findSingleParameter() method.

##### Syntax:

findSingleParameter("parameterName", "this", "itemName", "itemRevision", "operationName", "operationRevision", "resourceName", "last")

##### Example:

Z\_LENGTH = findSingleParameter("Z\_LENGTH", "this", FG Item (with in double quotes), "\*", Operation step (within double quotes), "A", "DEFAULT", "last");

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig2.1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig2.2.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig2.3.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig2.4.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig2.5.jpg)

### 3. Using formula in Data collection with data collected from different operation

1. Create a DC Group Z\_LENGTH (Parameter Z\_LENGTH) - Assign it to operation 1

2. Create a DC Group Z\_WIDTH (Parameter Z\_WIDTH) - Assign it to operation 2

3. Create a DC Group Z\_HEIGHT (Parameter Z\_HEIGHT) - Assign it to operation 3

4. Create a DC Group Z\_VOLUME (Parameter Z\_VOLUME) - Assign it to operation 4

5. From the Pod-SFC, start the SFC and collect the DC

6. The user will enter the value for 3 parameters - Length, Width & Height

7. The system automatically calculates the Volume in Z\_VOLUME (4th DC Parameter) using the formula L \* W \* H

8. Verify the calculated parameter from Data Collection Results Report

##### Note:

1) To read the value of the parameter from other DC group, we will use the findSingleParameter() method:
2) Different operation name is mapped to read each of the parameter value.

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig3.1.jpg)

Input DC values as 5 for Z\_LENGTH, Z\_WIDTH, Z\_HEIGHT.

![](/legacyfs/online/storage/blog_attachments/2023/02/Fig3.2-1.jpg)

### Conclusion:

To sum up, this blog details the use of a formula to automatically calculate the DC parameter out of the operator provided DC parameter values in various data collection scenarios.
Thank you for taking the time to read this post, and I hope this blog is useful to those who are ...
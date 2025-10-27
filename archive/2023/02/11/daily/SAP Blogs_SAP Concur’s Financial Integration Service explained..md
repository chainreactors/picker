---
title: SAP Concur’s Financial Integration Service explained.
url: https://blogs.sap.com/2023/02/10/sap-concurs-financial-integration-service-explained./
source: SAP Blogs
date: 2023-02-11
fetch_date: 2025-10-04T06:19:23.365713
---

# SAP Concur’s Financial Integration Service explained.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP Concur's Financial Integration Service explain...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51267&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Concur's Financial Integration Service explained.](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-concur-s-financial-integration-service-explained/ba-p/13556515)

![tim_chapman24](https://avatars.profile.sap.com/a/7/ida7d3d7556ac4549d40b1cd8c2e5193da36a48386932bd2dc531b4bec47e491d3_small.jpeg "tim_chapman24")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[tim\_chapman24](https://community.sap.com/t5/user/viewprofilepage/user-id/826513)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51267)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51267)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556515)

‎2023 Feb 10
8:34 PM

[17
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51267/tab/all-users "Click here to see who gave kudos to this post.")

11,322

* SAP Managed Tags
* [SAP Concur](https://community.sap.com/t5/c-khhcw49343/SAP%2520Concur/pd-p/3f613a69-f511-450e-82d3-943b2bb8ff50)

* [SAP Concur

  Additional Software Product](/t5/c-khhcw49343/SAP%2BConcur/pd-p/3f613a69-f511-450e-82d3-943b2bb8ff50)

View products (1)

I have been a Technical Consultant at SAP Concur for many years and work on the data interfaces between SAP Concur and its customers.  There are several mechanisms for obtaining expense information that can be used for financial posting into any ERP system as well as reimbursement to employees/cards.  These include:

+ Standard Accounting Extract - a flat file delivered via SFTP in a predefined format

+ Custom Extracts - a flat file delivered via SFTP in a format that you define

+ Cognos Reports - a flat file delivered via SFTP or email in a format that you define

+ Web Service APIs – a series of calls from a program to extract the data for immediate consumption.

The first 3 options are traditional ways of bulk transferring of data.  At the time, they served a purpose.  With no import available for providing feedback, customers had to build applications for storing and reprocessing expense reports. This increased maintenance costs and required yet another system to access.

SAP Concur has been working hard on innovations to streamline and improve processes as demonstrated by all the new v4 APIs.  In this post, I will explain how to use one set of APIs called “Financial Integration Service” (FIS) to provide near real time bi-directional integration between SAP Concur and your systems.  By providing feedback, it allows you to leverage Concur Expense for storing and reprocessing expense reports which reduces maintenance costs.

![](/legacyfs/online/storage/blog_attachments/2016/02/sapnwabline_885687.png)

## Prerequisites

This post will not discuss authentication with Concur Expense.  Please see [this post](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/introduction-to-web-services-for-concur-expense-authentication/ba-p/13554400) to get an explanation on authentication and application building within Concur Expense.  You will need an application with the following SCOPEs:

+ FISVC

In addition, to enable Financial Integration Service within Concur Expense, the following [configuration changes](https://help.sap.com/docs/SAP_CONCUR/be5c9913e66445efbef21f9653d308ca/bb4e99add95a497ab6fe4451cca1b39f.html) are necessary.

![](/legacyfs/online/storage/blog_attachments/2016/02/sapnwabline_885687.png)

## Introduction

Financial Integration Service consists of the following steps:

+ Get Financial Transactions

+ Acknowledge each Financial Transaction

+ Confirm each Financial Transaction posted (success or fail)

+ Mark each Financial Transaction as paid (optional but recommended)

If you noticed, I am using the term "Financial Transaction" and not "Expense Report".  That is because FIS supports more than just expense report postings.  It also supports cash advances, invoice, payroll, and obligations.  In all the API calls, there is a variable called **doctype** which identifies the type of Financial Transaction you are working with.

To understand the various deployment options and configuration requirements, please read the [FIS Setup Guide found here](https://help.sap.com/docs/SAP_CONCUR/be5c9913e66445efbef21f9653d308ca/bb4e99add95a497ab6fe4451cca1b39f.html?locale=en-US).  The complete Financial Integration Service API documentation [can be found here](https://developer.concur.com/api-reference/financial-integration/v4.financial-integration.html).  To help you understand Financial Integration Service APIs, I developed the following [Postman collection](https://github.com/SAP-samples/concur-web-services-financial-integration-service) as an example.  You can also view FIS on the SAP API Business Hub [here](https://api.sap.com/api/ConcurFinancialIntegration/overview).

![](/legacyfs/online/storage/blog_attachments/2016/02/sapnwabline_885687.png)

## Detailed Walkthrough

### **Get Financial Transactions**

Using the *GET /financialintegration/fi/....../transaction* API (reference ***1 – Get FIS Transactions – All*** in the postman collection), you request to receive all transactions waiting to be processed into your ERP [Step 1].  The response is a JSON with financially relevant data that you can use for posting and payment [Step 2].  For example, expense reports that are fully approved and in Pending Payment status.  Within the JSON is a variable called **docId**. **docId** is NOT the report ID, report number or report key within Concur. It is the *financial document* id that is generated every time an expense report is fully approved.  If the expense report fails posting and is resubmitted, it will have a new **docId**.

![](/legacyfs/online/storage/blog_attachments/2022/12/1.-GET-FT.jpg)

Get Financial Transactions

### **Acknowledge each Financial Transaction**

Using the *POST /financialintegration/fi/.../acknowledgements* API (reference ***3 – Post FIS Acknowledgements*** in the collection), you will POST [Step 3] each Financial Transaction using the **docId** returned in Step 2.  This locks the corresponding concur document (i.e., expense report) and prevents it from being changed. This request **could fail** if the document was cancelled or recalled back to the employee/processor between step 1 and step 3. If that is the case, **do not continue processing this financial document!**  It will come back through Step 1 when it is approved again.

I can't stress this enough.  This is a critical step in the posting flow, and it must occur.  If you post the data to your ERP before acknowledgement is successful, you could easily double book the transactions.

![](/legacyfs/online/storage/blog_attachments/2022/12/2.-POST-ack.jpg)

POST acknowledge

### **Confirm each Financial Transaction posted (success or fai...
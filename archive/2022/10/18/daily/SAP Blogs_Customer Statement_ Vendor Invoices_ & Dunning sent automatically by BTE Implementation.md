---
title: Customer Statement/ Vendor Invoices/ & Dunning sent automatically by BTE Implementation
url: https://blogs.sap.com/2022/10/17/customer-statement-vendor-invoices-dunning-sent-automatically-by-bte-implementation/
source: SAP Blogs
date: 2022-10-18
fetch_date: 2025-10-03T20:07:12.739855
---

# Customer Statement/ Vendor Invoices/ & Dunning sent automatically by BTE Implementation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Customer Statement/ Vendor Invoices/ & Dunning sen...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66642&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customer Statement/ Vendor Invoices/ & Dunning sent automatically by BTE Implementation](/t5/enterprise-resource-planning-blog-posts-by-members/customer-statement-vendor-invoices-dunning-sent-automatically-by-bte/ba-p/13545192)

![former_member225722](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225722")

[former\_member225722](https://community.sap.com/t5/user/viewprofilepage/user-id/225722)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66642)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66642)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13545192)

‎2022 Oct 17
8:48 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66642/tab/all-users "Click here to see who gave kudos to this post.")

5,797

* SAP Managed Tags
* [SAP Financial Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Financial%2520Supply%2520Chain%2520Management/pd-p/01200615320800000553)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP R/3](https://community.sap.com/t5/c-khhcw49343/SAP%2520R%252F3/pd-p/01200245450800000002)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [SAP R/3

  SAP R/3](/t5/c-khhcw49343/SAP%2BR%25252F3/pd-p/01200245450800000002)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP Financial Supply Chain Management

  SAP Financial Supply Chain Management](/t5/c-khhcw49343/SAP%2BFinancial%2BSupply%2BChain%2BManagement/pd-p/01200615320800000553)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (7)

**Introduction -**

A typical Business requirement in today's world is to send certain Finance Outputs via email automatically from SAP as soon as you generate them. In S/4 HANA on-premise (and ECC as well), to be able to achieve this. Here I am sharing the BTE (Business Transaction Event) which can help us to achieve this functionality.

This is very common requirement and will be consider as must to have process. There are different automatic processes in SAP that trigger outputs and when these are created, these BTEs will be called and eventually the generated outputs will be sent via email by SAP automatically.

Below, I will be talking about different important and key Finance Outputs:

* Vendor Payment Advice

* Customer Statement

* Dunning Notice

**Configuration for Customer Statement**

1. FM module ZFI\_ACC\_STMNT\_PROCESS\_00002310 created by copying the sample.

2. T/code FIBF -> Setting -> Products -> of a customer

Create new entry as below-

**Product          Text                                        Activation**

ACCSTAT      Account statement                  X

3. T/code FIBF -> Setting -> Process Modules -> of a customer

Create new entry as below-

**Process           Appl.   FM                                                                  Product**

00002310                    ZFI\_ACC\_STMNT\_PROCESS\_00002310   ACCSTAT

# Functional Specification:

|
 **Business Requirements Specifications** |

|
 Create and activate new FM ZFI\_ACC\_STATEMENT\_PROCESS\_00002310 with reference to FM SAMPLE\_PROCESS\_00002310 and do the below mentioned changes. |

1.    Apply code as mentioned in SAP note 328124      2.    Create table ZFI\_CORRESPONDENCE as mentioned below with maintenance allowed.

|
 **Field name** |
 **Description** |
 **Data type** |
 **Length** |
 **Input field** |

|
 BUKRS |
 Company code |
 CHAR |
 4 |
 T001-BUKRS |

|
 ZDUNNING |
 Dunning |
 CHAR |
 1 |
 Check box |

|
 ZACCSTAT |
 Account Statement |
 CHAR |
 1 |
 Check box |

3.    Check BUKRS in ZFI\_CORRESPONDENCE and select ZFI\_CORRESPONDENCE- ZACCSTAT if ZACCSTAT is equal to ‘X’ then proceed else exit.

4.    If BKORM-KOART is equal to “D” read data then get data from KNB1. Priority will beA.    emailB.    FaxC.   Printout

5.    If BKORM-KOART is equal to “K” read data then get data from LFB1. Priority will beA.    emailB.    FaxC.   Printout
We can comment the code if any of these functionality is not available with your client.
**Security and Authorization :**N/A

**We can use below mentioned BTE to achieve the different requirement.**

**Payment Advice**

Payment Advice has 2 processes 2040 and 2050.

**Process 2040**, allows you to manage Sender email address, Recipient email address, Mail Body Text and the type of Transmission Method

* c\_finaa-nacha = '1'  - Spool

* c\_finaa-nacha = 'I'  - Internet / Email

For this SAP gives you a "Sample" FM that you can use as a base to copy and insert you own custom code. This is **SAMPLE\_PROCESS\_00002040**.

**Process 2050**, allows you to manage email Subject

For this SAP gives you a "Sample" FM that you can use as a base to copy and insert you own custom code. This is **SAMPLE\_PROCESS\_00002050**.

### Customer Statement

**Process 2310**. This one allows you to manage Transmission method, Format (PDF), Mail Body, Mail Subject, Sender and Recipient email address.

For this SAP gives you a "Sample" FM that you can use as a base to copy and insert you own custom code. This is **SAMPLE\_PROCESS\_00002310**.

### Dunning Letter

**Process 1040**. This one allows you to manage Transmission method, Format (PDF), Mail Body, Mail Subject, Sender and Recipient email address.

For this SAP gives you a "Sample" FM that you can use as a base to copy and insert you own custom code. This is **SAMPLE\_PROCESS\_00001040**.

The specific ABAP code of each one of these Function Modules need to be done based on your client requirement which will be taken care by your ABAP team.

This document will be helpful for junior level consultant to implement the BTE as per client requirement.

These are the real time business scenarios which you can explain in your in...
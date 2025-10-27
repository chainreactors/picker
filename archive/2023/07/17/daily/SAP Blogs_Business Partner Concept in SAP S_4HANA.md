---
title: Business Partner Concept in SAP S/4HANA
url: https://blogs.sap.com/2023/07/16/business-partner-concept-in-sap-s-4hana/
source: SAP Blogs
date: 2023-07-17
fetch_date: 2025-10-04T11:52:46.390038
---

# Business Partner Concept in SAP S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Business Partner Concept in SAP S/4HANA

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161814&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Business Partner Concept in SAP S/4HANA](/t5/technology-blog-posts-by-members/business-partner-concept-in-sap-s-4hana/ba-p/13560054)

![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")

[mickaelquesnot](https://community.sap.com/t5/user/viewprofilepage/user-id/150004)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161814)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161814)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560054)

‎2023 Jul 16
9:53 AM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161814/tab/all-users "Click here to see who gave kudos to this post.")

121,488

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)

View products (5)

# Business Partner Concept in SAP S/4HANA

## 1.1      *What is Business Partner?*

In SAP S/4 HANA, Business Partner is the leading object and single-entry point to maintain Business Partner, Customer, and Supplier (formerly known as Vendor) master data.

<https://youtu.be/vWyBxLety4w>

Download PDF : <https://icedrive.net/s/APyBWPS1tfDC5XRWt6wgj4DwAWhV>

Business Partner allows maintenance of multiple addresses with corresponding address usages.

It is not a new terminology it is also in ECC

ECC have two options

1. Customer or vendor 2. Business Partner

* In SAP S/4 HANA is only Business Partner

* Business Partner is any entity is impact with our business and or impaction our business is known as business Partner

* The EWM, MDG, TM, CRM, SRM they are following Business Partner concept.

* Vendor customer is are the role which is done by business partner

* It is mandatory in conversion ECC to S/4HANA, Business Partner must be assign to customer and vendor in ECC.

### *1.1.1* *Which Table we are getting here*

* BUT000 – General Data

* BUT020 – Address

* BUT100 – BP Roles

* KNA1- Customer Data

* LFA1- Vendor Data

### 1.1.2     *Business Partner Role*

SAP Business Partner Screening for SAP S/4 HANA is used to centrally manage master data for business partners, customers, and vendors. Business Partner Application allows you to create, maintain, and manage business partners. You can also use this to perform integration with other functions and data exchange.

You can use the BP Role to carry out a business classification of a BP role on the basis of business transaction. The attributes of the BP role depend on the particular transaction involved.

In S/4 HANA we have three different categories

A Business Partner can be

* Organization

* Person- Individual

* Group- Group of person or partners

### 1.1.3     *Account Group*

An account group is a named collection of accounts. CSA uses account groups in financial statements to increase their flexibility and to enable you to use a financial statement for multiple clients. Some account group names are pre-defined, but account group definitions are client specific.

### 1.1.4     **Customer Account Group**

Customer account groups in SAP are used to classify customers into business partner functions that fit best the nature of the business transaction. Customer account groups control the customer hierarchy containing the customer master record. It determines the role of a customer and customer master data.

We create Customer Account Group in Financial Accounting

**Menu Path:**

SPRO-> SAP IMG Screen-> Financial Accounting-> Account Receivable & Payable->Customer Accounts-> Master Data-> Preparation for creating Customer Master Data-> Define Account Groups with screen layout (Customer) Master data

**Menu Path:**

SPRO-> SAP IMG Screen-> Financial Accounting-> Account Receivable & Payable->Customer Accounts-> Master Data-> Preparation for creating Customer Master Data-> Create Number ranges for Customer Account Group

**Menu Path:**

SPRO-> SAP IMG Screen-> Financial Accounting-> Account Receivable & Payable->Customer Accounts-> Master Data-> Preparation for creating Customer Master Data-> Assign Number ranges to Customer Account Group

**Vendor Account Group**

You use vendor groups to classify your vendor records into groups that share similar characteristics. You define vendor groups adding vendor records*.*

**Menu Path**

SPRO-> SAP IMG Screen-> Financial Accounting-> Account Receivable & Payable->Vendor Accounts-> Master Data-> Preparation for creating Vendor Master Data-> Define Account Groups with screen layout (Vendor) Master data

**Menu Path:**

SPRO-> SAP IMG Screen-> Financial Accounting-> Account Receivable & Payable->Vendor Accounts-> Master Data-> Preparation for creating Vendor Master Data-> Create Number ranges for Vendor Account Group

**Menu Path:**

SPRO-> SAP IMG Screen-> Financial Accounting-> Account Receivable & Payable->Customer Accounts-> Master Data-> Preparation for creating Vendor Master Data-> Assign Number ranges to Vendor Account Group

## 1.2      *Customer Vendor Integration*

###

Customer/Vendor Integration involves the following process phases: You process the business partner or customer/vendor. ... If a customer/vendor master record is assigned to the business partner, then the system updates the customer/vendor data in the business partner at the same time, irrespective of role.

**Work before conversion is as follows:**

* Archive redundant master data.

* Activate business functions.

* Integrate custom enhancements.

* Implement check reports (see below section for these standard tools).

* Configure **CVI** as customer/vendor to BP.

* Implement customer specific mapping, if necessary.

* Assign number ranges.

The Customer/Vendor Integration (CVI) component ensure the synchronization between the BP object and the Customer/Vendor objects. Aside from the mandatory Bus...
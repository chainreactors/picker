---
title: Customer receipts automation through payment service provider integration
url: https://blogs.sap.com/2023/03/28/customer-receipts-automation-through-payment-service-provider-integration/
source: SAP Blogs
date: 2023-03-29
fetch_date: 2025-10-04T11:00:44.415635
---

# Customer receipts automation through payment service provider integration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Customer receipts automation through payment servi...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161040&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customer receipts automation through payment service provider integration](/t5/technology-blog-posts-by-members/customer-receipts-automation-through-payment-service-provider-integration/ba-p/13556176)

![sivamothukuri84](https://avatars.profile.sap.com/8/2/id8215e409fbe308a10a0238ebdb255961bf6d5a60acdf20417e63cfd4b2a9f0d0_small.jpeg "sivamothukuri84")

[sivamothukuri84](https://community.sap.com/t5/user/viewprofilepage/user-id/129785)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161040)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161040)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556176)

‎2023 Mar 29
12:22 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161040/tab/all-users "Click here to see who gave kudos to this post.")

2,640

* SAP Managed Tags
* [SAP Analytics Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Hub/pd-p/73555000100800000638)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP Payment Approvals](https://community.sap.com/t5/c-khhcw49343/SAP%2520Payment%2520Approvals/pd-p/01200615320800003828)
* [SAP Payment Engine](https://community.sap.com/t5/c-khhcw49343/SAP%2520Payment%2520Engine/pd-p/01200615320800001129)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP Payment Approvals

  SAP Payment Approvals](/t5/c-khhcw49343/SAP%2BPayment%2BApprovals/pd-p/01200615320800003828)
* [SAP Payment Engine

  SAP Payment Engine](/t5/c-khhcw49343/SAP%2BPayment%2BEngine/pd-p/01200615320800001129)
* [SAP Analytics Hub

  SAP Analytics Hub](/t5/c-khhcw49343/SAP%2BAnalytics%2BHub/pd-p/73555000100800000638)

View products (4)

This document explains how to create an inbound interface between payment service providers and SAP. The solution focuses on the automation of customer payment transactions made via various payment methods on the client's e-commerce website.

This solution would be cost-effective and appropriate for customers who run their businesses in SAP ECC.

### **Business case:**

### Key Drivers for the automation of the process: -

* When processing the transaction into SAP, the client followed a manual process that was prone to errors.

* The Finance Business user logs into the payment provider website (PayPal, WorldPay, Amex & Klarna) and downloads a file containing payment transactions from a particular date, converts the file into a WinShuttle format, and then loads those transactions into SAP. A file downloaded today would contain sales from yesterday, since the user tends to check for and process the files on Mondays and Fridays, but with additional sensitivity around month-ends.

* Before uploading the files into SAP, the user must follow certain steps to manipulate the files downloaded from the payment provider's portal.

* The unloadable file should include a few standard transaction codes of the payment providers.

* Manual processing and file manipulation would depend on the solution designed to process the uploaded file.

* Payment transactions will be posted by the process file, calling SAP transaction code F-28, debiting the bank GL account and crediting the customer account. This process is not the same for all other payment providers. The receipt amount is net of the fee paid to the payment service providers.

* Additional transactions such as refunds, chargebacks, chargeback fees, etc, will also be captured and posted into finance along with receipt postings.

### Key Rationale:

* Reduce manual effort and remove risk of human error: The incoming transaction records are processed, manipulated and transformed into a loadable format with minimal human effort.

* Provide future-proofing in the event that sales transaction volumes increase.

* Provide a daily stock reconciliation process similar to the one already in place for the various integrated 3PLs.

* Improve stock and payment reconciliation (removing write-offs where data cannot currently be reconciled) by aligning BRUSA with Business Intelligence processes, especially in capturing data at the order level (rather than at the summary level).

### **Components of Integration –**

* In order to automate and integrate the Payment service providers with SAP, the development of SAG, PI, and SAP ECC is proposed.

* SAP PI can be integrated with the payment service provider's portal to retrieve transaction files from their SFTP folders. Based on the country in which the transactions were originated, the PSP will make the files available at pre-defined intervals and they will be transmitted to SAP AL11 folders for creation of Idocs.

* PI (Process Integration) integrates with SAP to process transaction files automatically.

* Through context types and mapping of source values to target values, the value mapping table can be used to derive certain important target parameters into the inbound interface. When mapping a transaction file to an Idoc, SAP PI will perform a lookup.

* Duplicate check functionality to prevent processing of transaction files more than once. In order to store all processed files, a bespoke table was created, and before processing any file, PI checks the bespoke table to see if any other files with the same name exist. If PI identifies a duplicate file, the file will not produce an IDOC.

### **PI -**

* Sender File Adapter with Content Conversion to maintain node names and field names as per the Payment Transaction file.

* Create Structure of the file in Enterprise Service Repository with field names based on the File Content Conversion Parameter defined in Integration Builder.

* Create Mapping transformation (Node & Field level mapping logics) from Payment Transaction file to IDOC structure in Enterprise Service Repository.

* Create Integrated Configuration with IDOC Receiver Adapter.

### **Value Mapping –**

* In Payment providers integration, the value mapping functionality plays a pivotal role in converting a parameter from a source format to target value format to populate the parameters into the FI Idocs.

* Context types are created to group the source information on the origin of the data

* In the current model, the value mapping replication happens from source system to the target PI (Process integration) system.

### **File Formats -**

* The payment transaction file from each payment service providers will be distinct.

* A complex data mapping should be designed, to read, transform and translate the source file format into a target application document (SAP Idoc & SAP document).

* Each field and column of the payment transaction files provided by the payment providers should be read by the data mapping design.

* Payment files ...
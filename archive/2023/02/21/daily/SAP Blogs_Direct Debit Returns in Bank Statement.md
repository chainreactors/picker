---
title: Direct Debit Returns in Bank Statement
url: https://blogs.sap.com/2023/02/20/direct-debit-returns-in-bank-statement/
source: SAP Blogs
date: 2023-02-21
fetch_date: 2025-10-04T07:37:18.151047
---

# Direct Debit Returns in Bank Statement

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Direct Debit Returns in Bank Statement

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67280&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Direct Debit Returns in Bank Statement](/t5/enterprise-resource-planning-blog-posts-by-members/direct-debit-returns-in-bank-statement/ba-p/13553683)

![Bohdan](https://avatars.profile.sap.com/7/3/id734646801e0751f4793baef6e38a5f65d7a31dc8216c06989ee6328558476ad9_small.jpeg "Bohdan")

[Bohdan](https://community.sap.com/t5/user/viewprofilepage/user-id/180051)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67280)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67280)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553683)

‎2023 Feb 20
8:45 PM

[13
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67280/tab/all-users "Click here to see who gave kudos to this post.")

15,367

* SAP Managed Tags
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)

* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)

View products (2)

Hello SAPers!

Here is my latest post, where I’d like to share some details about SAP’s functionality. It took me some time to prepare this post and it will take some time to read it through. I hope you will not regret this time. Please also check out my other posts.

## Introduction

**Direct debit** is a financial transaction, where the company sends the instruction to the bank to collect the payment directly from the debtor’s bank account. Properly implemented direct debit simplifies the debt collection for the company. This process is well described / documented. But as a rule, the documentation covers the regular process i.e., when the bank managed to collect the payment. Direct debit returns (cancellations / rejections) are not described properly. This post aims to fill this knowledge gap.

## Process Overview

Screenshot below provides high-level overview of the process around direct debit:

![](/legacyfs/online/storage/blog_attachments/2023/02/01_process_flow.jpg)

Direct debit is initiated in SAP via automated payment program (i.e., F110). The program generates the payment document that credits the customer account. This payment document automatically clears open items on customer’s account and generates an open item on clearing GL account for incoming bank payments. If everything goes fine, the bank will collect the payment from the customer and show the associated receipt in a bank statement. This is a simplified explanation, but I hope it provides a good explanation. Screenshot below provides an overview of the typical accounting postings.

![](/legacyfs/online/storage/blog_attachments/2023/02/02_regular_postings.jpg)

Let’s now consider the case of direct debit return. The return might happen due to a variety of reasons e.g., insufficient funds, incomplete / erroneous direct debit mandate etc. The bank charges a return fee for each operation. What is even more complicated, your bank might provide the information in bank statement in aggregated format i.e., operation amount (1005,00 EUR) will include the original payment amount (1000,00 EUR) + return fee (5,00 EUR). Screenshot below shows a sample bank statement with such aggregated operation.

![](/legacyfs/online/storage/blog_attachments/2023/02/03_bank_statement.jpg)

The screenshot below shows the expected postings in the bank statement with regards to direct debit return. Though we have only one line in bank statement, the system should be able to generate two separate postings:

* Direct debit return payment with 2 posting areas.

* Bank fee associated with direct debit return.

![](/legacyfs/online/storage/blog_attachments/2023/02/04_return_postings.jpg)

Let’s see how this process can be implemented in the system.

## Process Flow in the System

Automatic payment program generated a payment document 2000000006 for total amount of 1000,00 EUR. This payment document number will be provided in the note to payee for the returned direct debit in the bank statement. See the example above, where this value is highlighted.

![](/legacyfs/online/storage/blog_attachments/2023/02/05_payment_run_log.jpg)

Screenshot of the payment document is provided below:

![](/legacyfs/online/storage/blog_attachments/2023/02/06_payment_document.jpg)

This payment run automatically cleared open item associated with the customer invoice 1800000007:

![](/legacyfs/online/storage/blog_attachments/2023/02/07_OI_list_after_payment.jpg)

The interval of accounting document numbers should include the number range for payment documents. Screenshot below shows the appropriate selection screen block in the transaction FF\_5.
If you work with S4 HANA system and use Fiori App **F1680** “*Manage Incoming Payment Files*”, you’ll need to configure the parameter set, which stores the number ranges associated with bank statement. Please refer to my earlier [post](https://blogs.sap.com/2023/02/01/import-of-bank-statements-in-fiori/), that describes this configuration.

![](/legacyfs/online/storage/blog_attachments/2023/02/08_ff_5_sel_screen.jpg)

Screenshot below shows the import log associated with upload of this bank statement. As you can see, the program split one item into two different items, assigned different posting rules and automatically posted the documents in both posting areas.

![](/legacyfs/online/storage/blog_attachments/2023/02/09_import_log.jpg)

As you can see, the log for the second posting area shows that the program identified original payment document 2000000006/2023. The clearing was reset automatically. Besides, as you can see, the report shows the open item for customer invoice 1800000007. This invoice was cleared during the payment run, but is re-opened now.

![](/legacyfs/online/storage/blog_attachments/2023/02/10_OI_list_after_upload.jpg)

The screenshot below shows the posting associated with return of the direct debit:

![](/legacyfs/online/storage/blog_attachments/2023/02/11_return_posting.jpg)

The screenshot below shows both line items in bank statement (transaction FEBAN/FEB\_BSPROC):

![](/legacyfs/online/storage/blog_attachments/2023/02/12_FEBAN_list.jpg)

What is interesting, the upload program generates a binary relationship between the original line item and the new line for bank charges. You can review this relationship by double clicking on the line in bank statement and navigating to the menu “Relationships”:

![](/legacyfs/online/storage/blog_attachments/2023/02/13...
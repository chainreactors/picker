---
title: Import of Bank Statement in Fiori: Custom Formats
url: https://blogs.sap.com/2023/02/07/import-of-bank-statement-in-fiori-custom-formats/
source: SAP Blogs
date: 2023-02-08
fetch_date: 2025-10-04T05:58:18.730245
---

# Import of Bank Statement in Fiori: Custom Formats

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Import of Bank Statement in Fiori: Custom Formats

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68175&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Import of Bank Statement in Fiori: Custom Formats](/t5/enterprise-resource-planning-blog-posts-by-members/import-of-bank-statement-in-fiori-custom-formats/ba-p/13564903)

![Bohdan](https://avatars.profile.sap.com/7/3/id734646801e0751f4793baef6e38a5f65d7a31dc8216c06989ee6328558476ad9_small.jpeg "Bohdan")

[Bohdan](https://community.sap.com/t5/user/viewprofilepage/user-id/180051)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68175)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68175)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564903)

‎2023 Feb 07
9:03 PM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68175/tab/all-users "Click here to see who gave kudos to this post.")

8,638

* SAP Managed Tags
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)

* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)

View products (2)

Hello SAPers !

My previous [post](https://blogs.sap.com/2023/02/01/import-of-bank-statements-in-fiori/) focused on the baseline process around import of bank statements in Fiori. This post explores additional enhancements that are necessary if you want to upload bank statements in bank specific formats e.g., XML, CSV, JSON etc.

## Introduction

If your bank does not provide bank statements in a commonly recognized format (e.g., MT940, Multicash, BAI etc.), you can configure SAP to upload bank statements in any structured format. I’ve started exploring this topic in my previous posts and recommend checking them out. Configurations described in those posts are technical pre-requisites and will provide a good starting point for this post. The links to these posts are provided below:

* [Bank statement in XML format](https://blogs.sap.com/2019/12/09/bank-statement-in-xml-format/)

* [Bank statement in CSV format](https://blogs.sap.com/2019/12/30/bank-statement-in-csv-format/)

This post will describe how to upload a bank statement in CSV format, but it will focus on Fiori-specific settings & enhancements. However, the idea can be applied to bank statement in any structured i.e., machine-readable format.

This post does not describe the parsing logic for CSV file or how the resulting data should be mapped against standard SAP tables that store transactional details of bank statements. These details were described in separate [post](https://blogs.sap.com/2019/12/30/bank-statement-in-csv-format/) mentioned above.

Four separate enhancements (i.e., BADIs) are required before you can upload such bank statements to SAP. Two of these enhancements are specific to Fiori. One of these enhancements checks if the bank statement file is compliant with the list of configured formats. Another one – calculates the number of bank statements in the file. Two more enhancements are executed in backend and were described in my earlier post.

![](/legacyfs/online/storage/blog_attachments/2023/02/00_process_scheme.jpg)

## Baseline configuration of new bank statement format

Define new bank statement format in view VFIEB\_MAPP\_XCTRL. You can also use the following menu path for this configuration activity:

*SPRO → Financial Accounting → Bank Accounting → Business Transactions → Payment Transactions → Electronic Bank Statement → XML Format and Bank-Specific Formats.*

![](/legacyfs/online/storage/blog_attachments/2023/02/01_definition_of_custom_format.jpg)

Configure new bank statement format for upload of bank statement. Use the following menu path to configure the format. Alternatively, you can use t-code S\_ER9\_11000399 or maintenance view VC\_FAR\_IPF (via SM34) to configure it.

*SPRO → Financial Accounting → Bank Accounting → Business Transactions → Payment Transactions → Electronic Bank Statement → Configure Formats for Import (SAP Fiori).*

![](/legacyfs/online/storage/blog_attachments/2023/02/02_definition_of_format_for_fiori.jpg)

Essentially, you define a new bank-specific bank statement format (value “X” in drop-down list stands for bank-specific format) and link it to the format defined earlier (i.e., in view VFIEB\_MAPP\_XCTRL). Entry UA\_PRV in the configuration represents the transaction type (i.e., t-code OT83) that will be used for derivation of posting rules.

![](/legacyfs/online/storage/blog_attachments/2023/02/03_definition_of_transaction_type-1.jpg)

Configure a new parameter set to control the processing parameters for import of bank statement. You can use t-code S\_ER9\_11001563 or maintenance view VC\_FAR\_BSIMP\_PSETS (via SM34) to configure it. Relevant configuration activity is also available under the following menu path:

*SPRO → Financial Accounting → Bank Accounting → Business Transactions → Payment Transactions → Electronic Bank Statement → Define Parameter Sets.*

![](/legacyfs/online/storage/blog_attachments/2023/02/04_definition_of_parameter_set.jpg)

Apart from these configuration activities, implement BADIs FIEB\_GET\_BANK\_STMTS\_X & FIEB\_MAPPING\_X as described in my previous [post](https://blogs.sap.com/2019/12/30/bank-statement-in-csv-format/).

## Fiori-specific enhancements for custom bank statement format

If you maintained baseline configuration for custom bank statement format as described above, you can attempt to upload bank statement via Fiori App **F1680** “*Manage Incoming Payment Files*”. However, the app will throw an error message “No implementation was selected for the current BAdI. An exception was raised”. Unfortunately, the error message does not provide further details e.g., what BAdI was not implemented.

![](/legacyfs/online/storage/blog_attachments/2023/02/05_error_in_fiori_app.jpg)

Implement BADI **FAR\_IPF\_FORMAT\_RECOGNITION** to address this exception. The filter value for this enhancement should be the same as configured in view VFIEB\_MAPP\_XCTRL.

![](/legacyfs/online/storage/blog_attachments/2023/02/06_badi_filter_stmt_format.jpg)
Sample source code for the BADI:

```
  method if_far_ipf_badi_formats~is_compliant_format.

    data lv_bank_statement type string.

    call function 'LXE_COMMON_XSTRING_TO_STRING'

      exporting

        in_xstring = iv_bank_statement

      importing

        ex_string  = lv_bank_statement

     exceptions

       error       = 1

       others      = 2 .

    if sy-subrc <> 0.

      return.

    endif.

    split lv_bank_statement at ...
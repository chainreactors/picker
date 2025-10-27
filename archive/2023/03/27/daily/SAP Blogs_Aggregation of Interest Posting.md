---
title: Aggregation of Interest Posting
url: https://blogs.sap.com/2023/03/26/aggregation-of-interest-posting/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:45:51.826591
---

# Aggregation of Interest Posting

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Aggregation of Interest Posting

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67884&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Aggregation of Interest Posting](/t5/enterprise-resource-planning-blog-posts-by-members/aggregation-of-interest-posting/ba-p/13560127)

![Bohdan](https://avatars.profile.sap.com/7/3/id734646801e0751f4793baef6e38a5f65d7a31dc8216c06989ee6328558476ad9_small.jpeg "Bohdan")

[Bohdan](https://community.sap.com/t5/user/viewprofilepage/user-id/180051)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67884)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67884)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560127)

‎2023 Mar 26
8:40 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67884/tab/all-users "Click here to see who gave kudos to this post.")

3,156

* SAP Managed Tags
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)

* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)

View products (2)

Dear SAPers,

Here is a small post that explains how standard SAP logic groups line items for the purposes of interest calculation and how it builds accounting posting for interest calculated on overdue items.

### Overview of the scenario

Consider the following scenario: your company is charging the customers the interest on overdue items. The interest is calculated only on those open items that are overdue. From the system perspective, you’re using interest indicator of type “P” (Item Interest Calculation). You can check these settings in transaction code OB46 or via the following menu path:

*SPRO → Financial Accounting → Accounts Receivable and Accounts Payable → Business Transactions → Interest Calculation → Interest Calculation Global Settings → Define Interest Calculation Types.*

![](/legacyfs/online/storage/blog_attachments/2023/03/01.01_interest_calculation_indicator.jpg)

Additionally, your company is calculating interest not only on debit items (i.e., sales invoices), but also on credit items (i.e., credit memos). Relevant functionality can activated under the settings of the interest calculation indicator (transaction code OB82). Alternatively, you can use the following menu path to access the settings:

*SPRO → Financial Accounting → Accounts Receivable and Accounts Payable → Business Transactions → Interest Calculation → Interest Calculation Global Settings → Prepare Interest on Arrears Calculation.*

![](/legacyfs/online/storage/blog_attachments/2023/03/01.02_interest_calculation_indicator.jpg)

As a result, when you execute the interest calculation program (i.e. transaction FINT), the program assigns different transaction types (CREIR vs. DEBIR) to open items. Additional explanations behind the use of these transaction types are provided below (i.e., under “Additional notes”). The screenshot below provides an example of the calculation in test mode.

![](/legacyfs/online/storage/blog_attachments/2023/03/02_interest_calculation.jpg)

If you’re using standard GL accounts determination logic, items with transaction type DEBIR will generate the posting of interest income, whereas the items with transaction type CREIR will generate interest expense posting. The screenshot below shows how the posting will look like.

![](/legacyfs/online/storage/blog_attachments/2023/03/03_interest_posting_original.jpg)

The question is: is it possible to aggregate the posting, so that the program generates only one open items for the net amount of interest receivable? Answer is “Yes”. I’ve [reversed the interest run](https://blogs.sap.com/2023/03/22/reversal-of-interest-run/) for the month, adjusted the settings, and re-posted the interest run. The posting below shows the aggregated posting. As you can see, the program generated one open item for the net amount of interest receivable, which is offset by one aggregated P&L line for interest income.

![](/legacyfs/online/storage/blog_attachments/2023/03/04_interest_posting_aggregated-1.jpg)

### Overview of the system configuration

The screenshot below shows the standard system configurations for GL accounts determination. You can check these settings in transaction code OBV1 or via the following menu path:

*SPRO → Financial Accounting → Accounts Receivable and Accounts Payable → Business Transactions → Interest Calculation → Interest Posting → A/R: Calculation of Interest on Arrears.*

![](/legacyfs/online/storage/blog_attachments/2023/03/05_standard_gl_accounts_determination.jpg)

As you can see, there are two transaction keys:
- **1000** which corresponds to interest income (i.e., transaction type DEBIR in FINT).
- **2000** which corresponds to interest expense (i.e., transaction type CREIR in FINT).
Activate the compression of accounting postings as shown on the screenshot below. There is no need to adjust the assignment of GL accounts to account symbols.

![](/legacyfs/online/storage/blog_attachments/2023/03/06_adjusted_gl_accounts_determination.jpg)

In accordance with these settings, the program will aggregate both customer open items & interest income / expense items before the posting. The program will first calculate the net amount for the P&L item and then will fetch the GL account for the relevant account symbol (0001 or 0002).
There might be alternative combination. For instance, you might activate aggregation of customer open items only, while interest income / expense will not be compressed and will be posted to separate GL accounts.

### Additional notes

The screenshot of the simulation mode for transaction FINT showed two invoices & three credit memos. If you check the resulting entries carefully, you might wonder why two credit memos were assigned the category DEBIR, whereas only one of them (i.e., 1600000007) was assigned the transaction type CREIR? The explanation is rather simple: standalone credit memos will have the transaction type CREIR, whereas credit memos with the reference to original invoices will have the category DEBIR. Screenshot below shows how the references are displayed in the open item of the credit memo:

![](/legacyfs/online/storage/blog_attachments/2023/03/invoice_references.jpg)

From technical point of view, these references are stored in the table BSEG (fields REBZG / REBZJ / REBZZ / REBZT). See the screenshot from SE16N below:

![](/legacyfs/online/storage/blog_attachments/2023/03/invoice_references_bseg.jpg)

Hope this post was useful and you found something of val...
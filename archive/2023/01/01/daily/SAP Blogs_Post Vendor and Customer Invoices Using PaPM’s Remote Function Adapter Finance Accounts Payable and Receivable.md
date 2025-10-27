---
title: Post Vendor and Customer Invoices Using PaPM’s Remote Function Adapter Finance Accounts Payable and Receivable
url: https://blogs.sap.com/2022/12/31/post-vendor-and-customer-invoices-using-papms-remote-function-adapter-finance-accounts-payable-and-receivable/
source: SAP Blogs
date: 2023-01-01
fetch_date: 2025-10-04T02:50:42.913540
---

# Post Vendor and Customer Invoices Using PaPM’s Remote Function Adapter Finance Accounts Payable and Receivable

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* Post Vendor and Customer Invoices Using PaPM’s Rem...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7923&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Post Vendor and Customer Invoices Using PaPM’s Remote Function Adapter Finance Accounts Payable and Receivable](/t5/financial-management-blog-posts-by-sap/post-vendor-and-customer-invoices-using-papm-s-remote-function-adapter/ba-p/13558088)

![former_member674341](https://avatars.profile.sap.com/former_member_small.jpeg "former_member674341")

[former\_member674341](https://community.sap.com/t5/user/viewprofilepage/user-id/674341)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7923)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7923)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558088)

‎2022 Dec 31
2:44 PM

[6
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7923/tab/all-users "Click here to see who gave kudos to this post.")

3,266

* SAP Managed Tags
* [SAP Profitability and Performance Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Profitability%2520and%2520Performance%2520Management/pd-p/73555000100800000092)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)
* [FIN General Ledger](https://community.sap.com/t5/c-khhcw49343/FIN%2520General%2520Ledger/pd-p/141573396494884189617506284133567)

* [SAP Profitability and Performance Management

  SAP Profitability and Performance Management](/t5/c-khhcw49343/SAP%2BProfitability%2Band%2BPerformance%2BManagement/pd-p/73555000100800000092)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)
* [FIN General Ledger

  Software Product Function](/t5/c-khhcw49343/FIN%2BGeneral%2BLedger/pd-p/141573396494884189617506284133567)

View products (3)

It’s time to present the next Remote Function Adapters (RFA) delivered by SAP Profitability and Performance Management (PaPM), namely the **RFA Finance Accounts Payable (RFA FI-AP)** and **RFA Finance Accounts Receivable (RFA FI-AR)**.

These RFAs, along with other functions provided by PaPM, such as allocations, calculations, joins, can facilitate various business processes of calculating values and immediately booking them as for instance Accounts Payable and Receivable.

The RFAs not only allow for postings within one company code but also enables cross-company postings, what might be interesting for entities with some affiliated company codes. In that case, as in SAP standard, the system posts a separate document with its own document number in each of the company codes. And let's not forget that even postings between different SAP systems can be performed!

In this blogpost I am going to show you some basic information, how to use the RFA FI-AP and RFA FI-AR and also some small useful tips and tricks.

**Configuration of RFA Finance Accounts Payable and RFA Finance Account Receivable**

**Database Connection and RFC Destination**

As already mentioned in the previous blog posts written by my colleague and myself, the necessary condition would be to establish the RFC connection between SAP system(s) and PaPM. The RFC stands for Remote Function Call and is a standard SAP interface used to communicate between SAP systems. The connection needs to be set by SAP Basis guys, as it is considered as critical (SAP transaction SM59).

Once the necessary RFC set up has been configured, we need to define the destination system on PaPM side. In the On-Premise system we can do it at the environment level, in the Advanced tab. However, the creation of AP or AR might be addressed to different SAP Systems / Clients (RFC destinations). In that case, the RFC destination should be provided in the RFA function’s rules, either by mapping the component to the relevant field in the input function or hardcoded. The entry in the rule overwrites the entry in the environment.

In the Cloud you can set up the RFC connection either in the input table or it can be hardcoded directly in the RFA rule. There is no possibility currently to set up the connection on the level of the environment.

**RFA FI-AP / FI-AR Configuration**

Here is how to get started with the set up. In case of Accounts Payable and Accounts Receivable, you have a several possibilities delivered by PaPM.

Aside from the single RFA Finance Accounts Payable, corresponding to SAP FB60, which is the transaction used to post vendor invoices with no logistic background behind and RFA Finance Accounts Receivable, corresponding to FB70, used to post customer invoices, you can also choose the combined RFA Finance Accounts Payable/Receivable. As in SAP standard, the document type and the posting keys will be derived automatically by posting. The sign of the amount will determine the debit or credit side of the posting as well as the transaction type: Invoice or Credit Memo.

**Input Tab / Input Function**

The input function for the RFA FI-AP and RFA FI-AR might be a model table/view or result of any other function such as allocation, calculation, join, derivation, transfer structure. The data in the input function should contain the fields that will be mapped to the components of the RFA function.

Please see an example input function, where we store all fields necessary to create the AP / AR document:![](/legacyfs/online/storage/blog_attachments/2022/12/01-Input-1.jpg)

If you intend to calculate some values like dynamically derived posting date or tax amount, you need to calculate it in the input function. In the RFA rules, you can use only the standard functions provided in the formula, data from the input function or hardcoded values. It is not possible to define own syntax directly in the formula box within the RFA rules.

**Fields Mapping - the minimum necessary to be able to book the document**

When you start populating or mapping the fields, the components marked as mandatory will turn green when populated and orange when not populated.

**Rules tab for Accounts Payable:**

![](/legacyfs/online/storage/blog_attachments/2022/12/02-Rules-for-AP.png)

**Rules tab for Accounts Receivable:**

![](/legacyfs/online/storage/blog_attachments/2022/12/03-Rules-for-AR.png)

**Function Execution**

You can execute the posting in test run mode (header-doc\_status = 2) or in actual mode (header-doc\_status = empty).

In test run mode, standard SAP validations will be performed upon execution, but no documents will be posted in SAP.

In actual mode, standard SAP validations will be performed upon execution, and when the provided inputs pass the validations, relevant documents will be posted in SAP.

![](/legacyfs/online/storage/blog_attachments/2022/12/04-Execution-1-1.png)

One way to use the test / actua...
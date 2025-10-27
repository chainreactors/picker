---
title: Vendor and Customer Code in G/L Line Items for Accruals, Deferrals, and Provision Accounting Entries Enhanced Through In-App Extensibility
url: https://blogs.sap.com/2023/07/22/vendor-and-supplier-code-in-g-l-line-items-for-accruals-deferrals-and-provision-accounting-entries-enhanced-through-in-app-extensibility/
source: SAP Blogs
date: 2023-07-23
fetch_date: 2025-10-04T11:51:46.340424
---

# Vendor and Customer Code in G/L Line Items for Accruals, Deferrals, and Provision Accounting Entries Enhanced Through In-App Extensibility

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Vendor and Customer Code in G/L Line Items for Acc...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68167&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Vendor and Customer Code in G/L Line Items for Accruals, Deferrals, and Provision Accounting Entries Enhanced Through In-App Extensibility](/t5/enterprise-resource-planning-blog-posts-by-members/vendor-and-customer-code-in-g-l-line-items-for-accruals-deferrals-and/ba-p/13564795)

![Shakeel_Ahmed1](https://avatars.profile.sap.com/a/0/ida05db341bb3f9b845fc5a71a2009dbee7b7cfa230867952f598f51cc413976f8_small.jpeg "Shakeel_Ahmed1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Shakeel\_Ahmed1](https://community.sap.com/t5/user/viewprofilepage/user-id/146265)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68167)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68167)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564795)

‎2023 Jul 22
11:14 AM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68167/tab/all-users "Click here to see who gave kudos to this post.")

3,793

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (7)

![](/legacyfs/online/storage/blog_attachments/2023/07/00.jpg)

### **Introduction**

In your business operations, it is customary to manage manual accruals, deferrals, and provision accounting adjustments by utilizing the automatic reversal feature when posting general journal entries. These transactions take place at the G/L level without involving specific vendors or customers, making it challenging to generate vendor or customer-wise reports for accruals, deferrals, and provision accounting when required.

However, fear not! We are about to explore a solution that enables you to obtain supplier and customer details for such transactions related to accruals, deferrals, and provision accounting.

Thanks to the In-App Extensibility of S/4HANA Cloud, Public Edition, you can achieve the necessary such reporting. So, get ready to unlock the power of customization and enhance your financial reporting capabilities like never before!

Please note that the scenario discussed for accruals, deferrals, or provisions involves manual entries where no purchase order exists.

### **Solution Approach**

To implement this feature, we will leverage the power of In-App Extensibility. Our plan is to create Supplier and Customer Fields, enriched with standard F4 Values containing details of all suppliers and customers. This strategic customization will enable us to seamlessly enhance the functionality and cater to the specific reporting needs for accruals, deferrals, and provision accounting entries.

### **Following Fiori Apps or Transactions Included in This Blog**

* Post General Journal Entries App

* Post General Journal Entries App (with Posting Template: STANDARD\_5 for manual accruals, deferrals, and provision accounting entries)

* Manage Journal Entries App

* Manage Recurring Entries App (for manual Accrual and Deferral postings)

* Display Line Items in General Ledger App

* Trial Balance App

* Cost Center Actuals App

* Profit Center Actuals App

### **Procedure for Adding Custom Fields**

* **Custom Fields App**

Supplier Field

![](/legacyfs/online/storage/blog_attachments/2023/07/P0.jpg)

Click> + (Create)

![](/legacyfs/online/storage/blog_attachments/2023/07/P1-2.jpg)

Below selections are very Important while defining custom fields

**Business Context:** Accounting: Coding Block (FINS\_CODING\_BLOCK)

**Type**: Code List Based on CDS View

**Value Help View**: I\_Supplier\_VH

Click: **Create and Edit**

![](/legacyfs/online/storage/blog_attachments/2023/07/P2.0.jpg)

Enable services as per the requirement and save.

Once satisfied with field and selections PUBLISH it.

![](/legacyfs/online/storage/blog_attachments/2023/07/P2-2.jpg)

**We have activated below services:**

C\_COSTCENTERQ2001\_CDS: Cost Centers Actuals

C\_PROFITCENTERQ2701\_CDS: Profit Centers Actuals

C\_TRIALBALANCEQ0001\_CDS: Trial Balance

FAC\_FINANCIAL\_DOCUMENT\_SRV\_01: Manage Journal Entries

FAC\_GL\_DOCUMENT\_POST\_SRV: Post General Journal Entries

FAC\_GLV\_GL\_ACCOUNT\_LINE\_ITEMS\_SRV: Display Line Items in General Ledger

FAC\_RECURRING\_ACCOUNTING\_DOC\_SRV: Manage Recurring Journal Entries

**You have possibility to activate these custom fields in CDS views, APIs etc.**

### **Utilization of the Custom Fields in Diverse Applications**

* **Post General Journal Entries**

![](/legacyfs/online/storage/blog_attachments/2023/07/P3-2.jpg)

* **Manage Journal Entries**

![](/legacyfs/online/storage/blog_attachments/2023/07/P4-2.jpg)

* **Display Line Item General Ledger**

![](/legacyfs/online/storage/blog_attachments/2023/07/P5-2.jpg)

* **Cost Center Actuals**

![](/legacyfs/online/storage/blog_attachments/2023/07/cost-cen.png)

* **Post General Journal Entries App (with Posting Template: STANDARD\_5 for manual accruals, deferrals, and provision accounting entries)**
...
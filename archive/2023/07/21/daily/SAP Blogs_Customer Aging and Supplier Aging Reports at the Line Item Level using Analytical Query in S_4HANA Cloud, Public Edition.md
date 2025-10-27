---
title: Customer Aging and Supplier Aging Reports at the Line Item Level using Analytical Query in S/4HANA Cloud, Public Edition
url: https://blogs.sap.com/2023/07/20/creating-customer-aging-and-supplier-aging-reports-at-the-line-item-level-using-analytical-query-in-s-4hana-cloud-public-edition/
source: SAP Blogs
date: 2023-07-21
fetch_date: 2025-10-04T11:53:46.121291
---

# Customer Aging and Supplier Aging Reports at the Line Item Level using Analytical Query in S/4HANA Cloud, Public Edition

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Customer Aging and Supplier Aging Reports at the L...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68126&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customer Aging and Supplier Aging Reports at the Line Item Level using Analytical Query in S/4HANA Cloud, Public Edition](/t5/enterprise-resource-planning-blog-posts-by-members/customer-aging-and-supplier-aging-reports-at-the-line-item-level-using/ba-p/13563839)

![Shakeel_Ahmed1](https://avatars.profile.sap.com/a/0/ida05db341bb3f9b845fc5a71a2009dbee7b7cfa230867952f598f51cc413976f8_small.jpeg "Shakeel_Ahmed1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Shakeel\_Ahmed1](https://community.sap.com/t5/user/viewprofilepage/user-id/146265)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68126)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68126)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563839)

‎2023 Jul 20
6:19 PM

[18
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68126/tab/all-users "Click here to see who gave kudos to this post.")

20,683

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

![](/legacyfs/online/storage/blog_attachments/2023/07/P13.jpg)

### **Introduction**

Functional consultant or a business key user can effortlessly generate supplier and customer aging reports using the Custom Analytical Queries App for the scenarios outlined below.

**Scenario - Accounts Payable Aging:**

Your client requires a supplier aging report that displays the aging at different levels: Supplier level, Reconciliation G/L level, Supplier Region level, and Profit Center level. Additionally, they would like the option to access the aging information at the accounting document level in the same report.

**Scenario - Accounts Receivable Aging:**

Your client requires a customer aging report that displays the aging at different levels: Customer level, Reconciliation G/L level, Customer Region level, and Profit Center level. Additionally, they would like the option to access the aging information at the accounting document level in the same report.

You will have the various other options to select or deselect for your reporting as per your needs.

In this article, we will demonstrate how to create the Supplier Aging report, as described in the "Scenario - Accounts Payable Aging." The process and steps will remain consistent for other reports, such as "Scenario - Accounts Receivable Aging" or any other reports you wish to generate.

The reports created here will be capable of providing outputs for the following types of aging reports:

1. Aging at the company code with business partner level.

2. Aging at the accounting document with business partner level.

3. Aging at the reconciliation G/L with business partner level.

4. Aging at the profit center level with business partner level.

5. Aging at the region level with business partner.

**Report Creation Would Require Following Steps:**

* **Custom Analytical Queries** app:

  + Create a custom query by creating the existing most suitable query.

  + Field Selection: Incorporate field selections,

  + Display: Change field name, field sequencing

  + Filter: Set filters as required.

* **View Browser** app: Create a dedicated app for your custom query.

* **Custom Catalog Extensions** app: Add your custom app to the appropriate catalog.

* **Execute the Custom Report**: Utilize your custom report to generate the desired results.

**Custom Analytical Queries****app**

* **Search with appropriate / most suitable key word(s) as highlighted above:**

![](/legacyfs/online/storage/blog_attachments/2023/07/P1-1.jpg)

C\_APJRNLENTRITMAGINGGRID: for Supplier Aging

C\_ARJRNLENTRITMAGINGGRID: for Customer Aging

* **Create: Create by copy from an existing suitable query**

![](/legacyfs/online/storage/blog_attachments/2023/07/P2-1.jpg)

Copy from C\_APJRNLENTRITMAGINGGRID

Click OK, and change the label (Description)

![](/legacyfs/online/storage/blog_attachments/2023/07/P3-1.jpg)

* **Field Selection: Select and deselect fields in your query**

![](/legacyfs/online/storage/blog_attachments/2023/07/Field-Selection-1.png)

In this query, all fields are already selected; I haven't chosen or removed any fields. The standard configuration perfectly suits our needs.

* **Display: Sequence of your fields and rename field name etc.**

![](/legacyfs/online/storage/blog_attachments/2023/07/P4-1.jpg)

Here, also we are going with standard. However, you have the capability to change the sequences of the field, change standard field name or hide not required field ‘**Measure Structure’** etc.

* **Filters: User Inputs, Multiple Selection, Mandatory or Optional, Default Values etc.**

Company Code: As mandatory selection criteria with a default value

Select a Label (Field) and click on Filter Sign then page on the right-hand side will open

![](/legacyfs/online/storage/blog_attachments/2023/07/P5-1.jpg)

* **Supplier: As an optiona...
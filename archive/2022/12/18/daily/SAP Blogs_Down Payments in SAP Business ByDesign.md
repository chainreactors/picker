---
title: Down Payments in SAP Business ByDesign
url: https://blogs.sap.com/2022/12/17/down-payments-in-sap-business-bydesign/
source: SAP Blogs
date: 2022-12-18
fetch_date: 2025-10-04T01:51:47.866543
---

# Down Payments in SAP Business ByDesign

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Issued Down Payments in SAP Business ByDesign

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50737&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Issued Down Payments in SAP Business ByDesign](/t5/enterprise-resource-planning-blog-posts-by-sap/issued-down-payments-in-sap-business-bydesign/ba-p/13552558)

![Manjushree96](https://avatars.profile.sap.com/0/9/id098862d625f71e8fc3a5fc74286a8951211b02ef9680cc8a2cd215e49dbf99fe_small.jpeg "Manjushree96")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[Manjushree96](https://community.sap.com/t5/user/viewprofilepage/user-id/37976)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50737)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50737)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552558)

‎2022 Dec 17
8:45 AM

0
Kudos

1,619

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)
* [SAP Cloud Applications Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Applications%2520Studio/pd-p/67837800100800006741)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)
* [SAP Cloud Applications Studio

  SAP Cloud Applications Studio](/t5/c-khhcw49343/SAP%2BCloud%2BApplications%2BStudio/pd-p/67837800100800006741)

View products (2)

This blog explains down payment requests; down payment invoices are not supported in SAP Business ByDesign, but down payment requests are. For more information about the down payment process and business background, refer, [Down Payments Received in Financials](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2ce7a03a722d1014a5d9a6de95f9f1e4.html).

The workaround described in this document was created/designed based on project experience in Bosnia, Croatia, and Slovenia, countries/regions where down payment invoices are required for tax purposes.

*The following scenarios are possible for issued down payments:*

1. For all the scenarios, the down payment is made, and the final invoice is done within one month. In this case, the payment is posted to the supplier without a down payment request having been created (therefore, no tax is calculated, and the payment is not considered in tax reporting). The final invoice (containing the full amount) is created within the same month and will therefore be included in tax reporting.

2. The down payment made in one month and the final invoice in the next month. The supplier issues the down payment invoice at the end of the month. In this case, the payment is posted to the supplier without a down payment request having been created (therefore, no tax is calculated so far). At month end, the company receives a down payment invoice from the supplier. The down payment invoice is then posted as a down payment request and cleared with the down payment (tax for down payment will be included in tax reporting). In the next month, the final invoice (containing the full amount) is received and created. You clear the invoice with the down payment. This means that there will be a tax entry for the invoice and an automatic clearing document between the invoice and the down payment (both entries are considered in tax reporting).

3. The down payment is made in one month and the final invoice in the next month. The supplier does not issue a down payment invoice at the end of the month. In this case, the down payment will not be included in tax reporting. The only thing that needs to be considered is, if the country has a fixed chart of account and has a special account for this case, such as is the case for Bosnia, then a manual reposting may become necessary to the respective general ledger account, depending on local requirements.

**Business Scenario.**

The following diagram outlines the steps in the Procure-to-Pay (Service) business scenario

When a retail company procures a service, a down payment is required. The steps in this scenario are as follows:

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture1-2.jpg)

1. Create a purchase order.

2. Process the down payment.

3. Process the down payment request (when the down-payment invoice is sent by the supplier).

4. Clear the down payment with the down payment request. A down payment invoice is then posted as a down payment request and a tax entry is created as the tax for the down payment will be considered in tax reporting.

5. Confirm the service receipt.

6. Process the supplier invoice.

7. Process the residual payable and payment.

8. Complete clearing on the GR/IR accounts. Since the tax item must not be declared before the down payment invoice is received from the supplier, the down payment is created first and the down payment request is created only when the down payment invoice is received

**Steps for Business Scenario.**

Below steps details the paradigm of business scenario in SAP Business ByDesign, that is, a down payment is issued and a down payment invoice is received by the supplier.

1. Create a purchase order with the following values:

**Purchase Order:**

* Supplier GCATS20123: 600,00 €

* Tax base amount = 500 €

* Tax amount = 100 €

2. Process the down payment.

**Outgoing Bank Transfer: Down payment**

* Supplier GCATS20123: 300,00 €

3. Process the down payment request (when a down payment invoice is sent by the supplier).

**Down Payment Request:**

* Supplier GCATS20123: 300,00 €

* Tax base amount = 250 €

* Tax amount = 50 €

4. Clear the down payment with the down payment request, thereby creating a tax entry.

**Clearing:**

* Supplier GCATS20123: 300,00 €

* Tax base amount = 250 €

* Tax amount = 50 €

5. Process the supplier invoice.

**Supplier Invoice:**

* Supplier GCATS20123: 600,00 €

* Tax base amount = 500 €

* Tax amount = 100 €

6. **Clearing: Supplier invoice with down payment**

* Prepayments are issued and tax from down payment is taken back

* Tax base amount = 250 €

* Tax amount = 50 €

7. Process the residual payable and payment.

* **Outgoing Bank Transfer:**

* Supplier GCATS20123: 300,00 €

8. Clear the GR/IR accounts.

9. Clear any unbilled payables with Purchases in Transit.

**Note**: GR/IR Clearing is part of the Closing Scenario and is not necessarily performed here. As long as the transaction period is in the future, clearing cannot be processed.

**Scenario Variants**

The following variants exist for the described scenario and the following differences apply depending on the variant:

Scenario variant: Business transactions are run in the same period.

* In this case, the supplier will not issue a down payment invoice and therefore no down payment request is created. Tax will only be considered with the final invoice.

Scenario variant: Business transactions are run across periods and the supplier issues a down payment invoice.

* Refer to the...
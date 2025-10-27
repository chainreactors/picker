---
title: Accrual and Deferral Posting with Purchase Order in S/4HANA Cloud, Public Edition
url: https://blogs.sap.com/2023/07/15/accrual-and-deferral-posting-with-purchase-order-in-s-4hana-cloud-public-edition/
source: SAP Blogs
date: 2023-07-16
fetch_date: 2025-10-04T11:52:27.554832
---

# Accrual and Deferral Posting with Purchase Order in S/4HANA Cloud, Public Edition

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Accrual and Deferral Posting with Purchase Order i...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67788&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Accrual and Deferral Posting with Purchase Order in S/4HANA Cloud, Public Edition](/t5/enterprise-resource-planning-blog-posts-by-members/accrual-and-deferral-posting-with-purchase-order-in-s-4hana-cloud-public/ba-p/13559659)

![Shakeel_Ahmed1](https://avatars.profile.sap.com/a/0/ida05db341bb3f9b845fc5a71a2009dbee7b7cfa230867952f598f51cc413976f8_small.jpeg "Shakeel_Ahmed1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Shakeel\_Ahmed1](https://community.sap.com/t5/user/viewprofilepage/user-id/146265)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67788)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67788)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559659)

‎2023 Jul 15
8:15 AM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67788/tab/all-users "Click here to see who gave kudos to this post.")

14,181

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [SAP S/4HANA Cloud front end](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520front%2520end/pd-p/73555000100800000362)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA Cloud front end

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2Bfront%2Bend/pd-p/73555000100800000362)

View products (7)

![](/legacyfs/online/storage/blog_attachments/2023/07/P2.jpg)

### **Introduction**

The Purchase Order Accruals application automates the calculation and posting of accruals and deferrals in General Ledger Accounting.

Data from the Materials Management component is automatically transferred to the Accrual Engine, where it is converted from purchase order items to accrual items. Using this data, the system calculates the accrual or deferral amounts for each purchase order item. Simulations of these amounts are also possible. Periodically, an accrual or deferral run can be initiated to post all accruals or deferrals for the relevant business transactions.

Purchase order accrual process is part of 2VB scope items under finance area. it provides monthly accrual and deferral review, and monitoring with approval capabilities.

Scope Item 63L (Service Entry Sheet Based Accruals) offers similar functionality related to submitted service entry sheets but not approved.

### **Concepts: Accruals & Deferrals**

* **Accruals** recognize revenues or expenses before cash is received or paid, reflecting the true economic activity.

* **Deferrals** recognize revenues or expenses after cash is received or paid, deferring recognition to a later period.

### **Supported Purchase Types in System**

**Supported in Accrual and Deferral:**

* **Non-Valuated Material** is maintained as per quantity and not based on its value

* **Non-Stock Material** are immediately consumed after the procurement and not marinated in stock

* **Valuated Stock Material** is generally maintained with Quantity and Valuation

* **Service Masters**

All the above product masters and service masters are supported in Accrual and Deferral Posting with below conditions:

* Purchase orders with cost centers or projects will be transferred to the Accrual Engine for processing. This generally applies office materials, or the purchasing of services, other consumable purchase orders categorized under

  + Product Type Group (Product/Material Master)

  + Item Category: Blank, E and Consignment

  + Account Assignment Category (Wherever applicable): Cost Center, Project etc.

  + Purchase orders for service which requires a service entry sheet

  + Product Type Group 2 (Service Master).

  + Lean Service PO

  + Enhanced Limit PO with Item Category E

**Not Supported in Accrual and Deferral (In Standard):**

* Purchase orders related to Inventory (Valuated GR) Raw Material and Fixed Assets are excluded from transferring to the Accrual Engine as they do not generate expenses. These purchase orders do not impact the profit and loss (P&L) items. It is the case where there is no Cost center or projects/wbs elements in account assignment tab of the Purchase Order.

[Available BAdis for Purchase Order Accruals](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/8d2d7d62dbf54cdf9c4ec53be2a40abf.html): for further amendments

### **How Accrual Objects and Items are created in Accrual Engine**

* **Creation of Accrual Object**

  + Once a purchase order is approved, eligible POs are automatically moved to the Accrual Engine.

  + Each purchase order generates a single accrual object, while sub-objects/items are created based on the number of line items within the purchase order.

* **Start and End Dates of Accrual Objects**

  + **Scenario 1:** If a purchase order is created on August 8, 2023, with a delivery date of October 31, 2023, the system will use these dates for the accrual object. The start of the accrual object's life will be the PO creation date (August 8, 2023), and the end of its life will be the delivery date (October 31, 2023). This applies generally to **consumable PO** with **Product Type Group 2** (with a cost center) and ad hoc service-related or **...
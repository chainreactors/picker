---
title: SAP RAR Optimized Contract Management: Customer Invoice Fulfillment Business Use Case
url: https://blogs.sap.com/2022/12/14/sap-rar-optimized-contract-management-customer-invoice-fulfillment-business-use-case/
source: SAP Blogs
date: 2022-12-15
fetch_date: 2025-10-04T01:32:14.949831
---

# SAP RAR Optimized Contract Management: Customer Invoice Fulfillment Business Use Case

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP RAR Optimized Contract Management: Customer In...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68570&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP RAR Optimized Contract Management: Customer Invoice Fulfillment Business Use Case](/t5/enterprise-resource-planning-blog-posts-by-members/sap-rar-optimized-contract-management-customer-invoice-fulfillment-business/ba-p/13571140)

![Jitakshi_Sarmah](https://avatars.profile.sap.com/6/4/id642281c59a5982d8db1538dec5ed510c43e269799f646e1235d65a32ceb28581_small.jpeg "Jitakshi_Sarmah")

[Jitakshi\_Sarmah](https://community.sap.com/t5/user/viewprofilepage/user-id/45591)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68570)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68570)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571140)

‎2022 Dec 14
7:47 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68570/tab/all-users "Click here to see who gave kudos to this post.")

4,186

* SAP Managed Tags
* [SAP Revenue Accounting and Reporting](https://community.sap.com/t5/c-khhcw49343/SAP%2520Revenue%2520Accounting%2520and%2520Reporting/pd-p/67837800100800005219)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Revenue Accounting and Reporting

  SAP Revenue Accounting and Reporting](/t5/c-khhcw49343/SAP%2BRevenue%2BAccounting%2Band%2BReporting/pd-p/67837800100800005219)

View products (2)

In this blog post I will be focusing on SAP Revenue accounting and reporting (RAR) Event-Based Fulfillment Type – Customer Invoice of Performance Obligation. A performance obligation (POB) can be fulfilled when a specified event happens which is Event-Based Fulfillment. A performance obligation can also be fulfilled over a period of time which is Time-Based Fulfillment.

### **Performance Obligation Types**

The goods or services that are promised in the contract represent a single performance obligation. SAP RAR has performance obligation types, and this represents data which addresses queries on fulfillment type; if it is Time or Event Based, and also specifies about the duration.

**IMG Path - Financial Accounting > Revenue Accounting > Revenue Accounting Contracts > Define Performance Obligation Types![](/legacyfs/online/storage/blog_attachments/2022/12/1-71.png)**

**Fulfillment Event Types**

On the occurrence of an event, Performance obligations can be fulfilled. They can also be fulfilled over a period of time, starting from the occurrence of an event.

**IMG Path - Financial Accounting > Revenue Accounting >Revenue Accounting Contracts > Define Fulfilment Event Types![](/legacyfs/online/storage/blog_attachments/2022/12/2-49.png)**

### **Customer Invoice and Time Based**

One can fulfill performance obligations (POBs) upon customer invoice getting generated.

**Use Case**

Company enters into a contract with customer (17100002) for 21,000 USD for providing Hi-Tech Equipment (TG13) and Warranty (SM001) of during contract validity from 14th October 2022 to 17th April 2023 (6 months).

|
 **Items** |
 **Qty** |
 **SO Rate** |
 **SSP** |
 **Contractual Price** |
 **Total SSP** |
 **Allocated Amount** |
 **Allocation Effect** |

|
 **TG13** |
 **1** |
 **20,000** |
 **17,000** |
 **20,000** |
 **17,000** |
 **20,284.09** |
 **284.09** |

|
 **SM0001** |
 **1** |
 **1,000** |
 **600** |
 **1,000** |
 **600** |
 **715.91** |
 **(284.09)** |

|
  |
  |
  |
  |
 **21,000** |
 **17,600** |
 **21,000** |
 **0** |

**Calculation Check Points:**

* Allocated Amount = Standalone Selling Price of Item X Complete Contractual Price / (Sum of all Stand-Alone Selling Price (SSP))

* Allocation Effect = Allocated Amount – Contractual Price of Item

**Step 1: Value Contract**

We start with Value Contract creation with materials & services associated with agreement.![](/legacyfs/online/storage/blog_attachments/2022/12/3-46.png)

**Step 2: Sales Order**

Next, with reference to value contract further Sales Order is created and condition type PPR0, Standalone Sales Price (SSP) will be manually updated at every item level for testing but without SSP system will not save the Sales Order.![](/legacyfs/online/storage/blog_attachments/2022/12/4-35.png)

**Step 3: Process Revenue Accounting Item’s related to Sales Order** **(Step 1)**

For many entities, Step 1 will be straight forward; the key point is to determine when a contract exists. Using Tcode *FARR\_RAI\_MON* or Fiori App *Manage Revenue Accounting Items,* all sales order items will be showcase initially as processable RAI’s. Then all such processable RAI’s are transferred using default sender integration component as *SD* with RAI class as *SD01* with source document item type as *SDOI* to RAR.![](/legacyfs/online/storage/blog_attachments/2022/12/5-32.png)![](/legacyfs/online/storage/blog_attachments/2022/12/6-27.png)

**View RAR Contract and Performance Obligations (POB’s)****(Step 2)**

All processable RAI’s are further transferred collectively or individually transfer to RAR. Once RAI’s are processed successfully, in 1st step system will automatically create one Revenue Recognition Contract 1000000301 against one Sales Order and in 2nd step Performance Obligations 2000003003/04 for each Sales Order Items.![](/legacyfs/online/storage/blog_attachments/2022/12/7-21.png)

**RAR Contract – Price Allocation****(Step 3, 4)**

As per IFRS 15 prerequisite, RAR component will automatically perform the allocation amount and allocation effect against each Performance Obligation. This determines transaction price and allocate to the separate POB’s level.![](/legacyfs/online/storage/blog_attachments/2022/12/8-20.png)

**RAR Contract – Revenue Schedule (Before Fulfillment)**

RAR Contract will calculate detail revenue schedule with status of each POB’s fulfillment type and status.![](/legacyfs/online/storage/blog_attachments/2022/12/9-19.png)

**Step 4: SD – Outbound Delivery and Post Goods Issue**

With reference to Sales Order, Outbound Delivery and PGI done for material relevant order items.**![](/legacyfs/online/storage/blog_attachments/2022/12/10-18.png)**

**Step 5: Revenue Accounting Item’s related to PGI**

In transaction *FARR\_RAI\_MON* or Fiori App *Manage Revenue Accounting Items,* all fulfillment items related to order will be showcase initially as processable RAI’s. Then all such processable RAI’s are transferred using default sender integration component as *SD* with RAI class as *SD02* with source document item type as *SDFI* to RAR.

**Step 6: Customer Billing**

Customer billing is posted.![](/legacyfs/online/storage/blog_attachments/2022/12/1-39.png)

**Step 7: Process Revenue Accounting Item’s related to Fulfillment Process**

All processable RAI’s are transferred using default sender integration component as *SD* with RAI class as *SD...
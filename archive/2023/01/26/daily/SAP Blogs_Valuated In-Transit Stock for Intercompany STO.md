---
title: Valuated In-Transit Stock for Intercompany STO
url: https://blogs.sap.com/2023/01/25/valuated-in-transit-stock-for-intercompany-sto/
source: SAP Blogs
date: 2023-01-26
fetch_date: 2025-10-04T04:51:53.213319
---

# Valuated In-Transit Stock for Intercompany STO

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Valuated In-Transit Stock for Intercompany STO

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67332&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Valuated In-Transit Stock for Intercompany STO](/t5/enterprise-resource-planning-blog-posts-by-members/valuated-in-transit-stock-for-intercompany-sto/ba-p/13554092)

![sudhir](https://avatars.profile.sap.com/f/3/idf34b10a853331f90f4c9a6bd0fc024bceecc20eabba2a211afe313ccd5d3ed1c_small.jpeg "sudhir")

[sudhir](https://community.sap.com/t5/user/viewprofilepage/user-id/149488)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67332)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67332)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554092)

‎2023 Jan 25
7:31 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67332/tab/all-users "Click here to see who gave kudos to this post.")

15,123

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

**Background: -**

Large Companies set up Global Supply Chain Network for Operational Efficiency, Cost Benefits, and optimum resource usage.

With three quarters (or more) of all business-to-business transactions globally taking place between parties that are related to or affiliated with one another (i.e.one subsidiary sells a product to another, or a parent company provides services to a subsidiary), getting those transactions structured and carried out (i.e., designed and executed) timely, accurately, and transparently is at the top of every company’s priority list.

Intercompany Stock Transfers Optimize Inventory by Leveraging the stock balance between companies and reduce the storage value.

SAP S/4 HANA has delivered several best practices to help implement Inter/Cross Company Transactions.

|
 Best Practice Scope ID |
 Process Scenario |

|
 1P9 |
 Intercompany Stock Transfer- the movement of product & services from the plant of one company to the plant of another company. Both Domestic and International Scenarios are supported. |

|
 1MX/ 1HO |
 Intercompany Sales International (1MX)/ Intercompany Sales Domestic (1HO)    Create sales order with supplying plant from different company code than the sales organization.    Deliver from supplying plant.    Invoice customer from sales organization    Perform intercompany invoicing sales organization from the supplying plant. |

In this blog we will mainly focus on 1P9- Intercompany Stock transfer process with Valuated Stock in Transit.

**Valuated Stock In-Transit**

In a cross-company-code or intra-company-code stock transfer, valuated stock in transit allows you to retain the quantity and value of a material that has already left the issuing plant but has not yet reached the receiving plant. The functions are also available for the corresponding intra-company-code and cross-company-code return stock transfers. In addition, in sales processes to external customers, you can post the quantity and value of a material to issuing valuated stock in transit initially, and then remove it when proof of delivery arrives.

This allows you to specify the transfer of title for the material in valuated stock in transit precisely. Material quantity and material value remain transparent throughout the process. You can call the data in the stock overview, the purchase order history, or in the relevant stock accounts.

Valuated stock in transit is available in the following intra-company-code and cross-company-code processes.

* Stock transfers with valuated stock in transit

  + Stock transfer with transfer of title at goods issue

  + Stock transfer with transfer of title at goods receipt

  + Stock transfer with transfer of title during transit

* Returns stock transfers with valuated stock in transit.

  + Returns stock transfer with transfer of title at goods receipt.

  + Returns stock transfer with transfer of title at goods issue.

  + Returns stock transfer with transfer of title during transit.

* Though it depends on the Company’s Policy, but the Industry Best Practice is to Transfer the Title of Goods/ Ownership from the Issuing Plant to the Receiving Plant at the time of Goods Issue. Movement Types and Financial Posting for this scenario will be covered later in the blog.

* Additionally, generally accepted best practice is to follow the Shipper’s rule in case of any discrepancy on the Quantity Shipped vs Quantity Received. For example, if Issuing Plant has shipped 10 Pcs but the Receiving Plant receives 9 Pcs, then Shipper’s rule should prevail, and Receiving Plant should post the Goods Receipt for 10 Pcs and account for 1 Pc as scrap or damaged goods.

**Valuated Stock in Transit Set Up.**

![](/legacyfs/online/storage/blog_attachments/2023/01/Valuated-Stock-In-Transit-Set-Up.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/Valuated-Stock-In-Transit-Set-Up1.jpg)

Above set up is pictorially shown below: -

Schedule Line Category

N1- Transfer of Title at Goods Issue

N2- Transfer of Title at Goods Receipt

N3- Transfer of Title in Transit

![](/legacyfs/online/storage/blog_attachments/2023/01/Valuated-Stock-In-Transit-Set-Up3.jpg)

**Process Steps**

* Buying/ Receiving Company creates a Cross Company Stock Transport Order (STO) with Selling/Issuing Plant as the Supplier.

* Selling/Issuing Plant creates Outbound Delivery, Pick/Pack and Ship Goods.

* Goods Issue puts the Stock In-Transit, and the Title of Goods/ Ownership is transferred from the Issuing to the Receiving Plant (Financial Ownership).

* Goods Issue automatically creates Inbound Delivery using Message Type SPED.

* Goods Receipt is posted when Goods arrive at the Receiving Plant. This moves the Stock from In-Transit to Receiving Plant (Logistics/Physical Ownership).

* Issuing Plant creates an Intercompany Billing to the Receiving Plant. Billing Output Message RD04 automatically creates Logistics Invoice.

* Intercompany Reconciliation is done using the Trading Partner in the Business Partner Set Up.

![](/legacyfs/online/storage/blog_attachments/2023/01/Valuated-Stock-In-Transit-Set-Up4.jpg)

**Conclusion**

Implementing Cross Company and Intracompany Transfer Processes is extremely important to many organizations with Global Manufacturing/ Supply Chain footprint. Hope this blog will help guide on how to set up Stock Transfer Process with Valuated in Transit using Standard Best Practices on S/4 HANA.

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fvaluated-in-transit-stock-for-intercom...
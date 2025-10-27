---
title: Item category determination in SAP S/4HANA Cloud
url: https://blogs.sap.com/2023/06/17/item-category-determination-in-sap-s-4hana-cloud/
source: SAP Blogs
date: 2023-06-18
fetch_date: 2025-10-04T11:46:06.231549
---

# Item category determination in SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Item category determination in SAP S/4HANA Cloud

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52231&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Item category determination in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/item-category-determination-in-sap-s-4hana-cloud/ba-p/13562744)

![varunvenkat](https://avatars.profile.sap.com/6/d/id6d9836d543f88d438477c8e54903aa6ba4a079c87ec08d808dc512a637a4c55f_small.jpeg "varunvenkat")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[varunvenkat](https://community.sap.com/t5/user/viewprofilepage/user-id/83606)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52231)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52231)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562744)

‎2023 Jun 17
12:09 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52231/tab/all-users "Click here to see who gave kudos to this post.")

9,289

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Sales](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)
* [SAP S/4HANA Cloud Public Edition Service](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Service/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)
* [SAP S/4HANA Cloud Public Edition Master Data](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Master%2520Data/pd-p/771f6577-e8ec-415f-99a7-6b73add46c47)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition Sales

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)
* [SAP S/4HANA Cloud Public Edition Service

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BService/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)
* [SAP S/4HANA Cloud Public Edition Master Data

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BMaster%2BData/pd-p/771f6577-e8ec-415f-99a7-6b73add46c47)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (4)

In my previous blog about [product master data](https://blogs.sap.com/2023/05/29/product-master-data-a-cheat-code-to-optimize-your-search-and-save-time/), I showed a possibility to create your own view of product master data with its important attributes such as product type, product group and item category group. In this blog post, I want to go into a bit more detail into the relevance of the Item category group especially, as this is a quite an important topic, especially in the Sales and Service Lines of Business in SAP S/4HANA Cloud. In a nutshell, the item category is responsible for determining how a particular product is processed in a Sales (or Service) order. For example, in a standard sales order, a product with an item category TAN will be processed a standard item, which means it will be relevant for billing later on. On the other hand, an item category CBLN represents a free of charge item, which means a product with that item category won’t be billed later on. This procedure is known as item category determination – you can read more about it [here](https://www.veonconsulting.com/item-category-determination/#:~:text=Item%20category%20notifies%20the%20behavior,category%20group%20of%20a%20material.).

In essence, it is important to understand the different item categories and their role in the system while processing products in sales or service transactions. The logic to decide which item categories will be available to choose from is as follows:

* The S/4HANA Cloud system reads the sales document type from the sales document in process. For example, a standard sales order has the OR document type.

* The system also reads the item category group from the product master record of the line item being processed in the sales order. For example, the commonly used product TG12 has the item category group NORM.

* Using the two attributes above, the system allows us to configure various possible combinations to determine the item category. This can be done in the SSCUI # 353572 (“Assign item categories”) in the “Configure your Solution” app (or in CBC). Here, we can for example define that the combination of Sales document type **OR** + item category group **NORM** will result in the default item category **TAN** being determined.

The takeaway from this is to understand what purpose item categories serve and how they are determined. Now that the theoretical concept has been explained, let’s look at a practical example of how the item category determination affects the processing (or rather lack of processing) of certain products in sales and service orders. To illustrate this, I’m going to use the following 2 examples:

1. Create a Service Order with the service product item SRV\_01. This works because SRV\_01 has the item category group SRVP. The combination of document type SVO1 (service order) and SRVP has multiple item category determination rules for the combination of sales document type SVO1 (service order) and SRVP in the system.![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-36.png)

On the other hand, products having the item category group SRVP cannot be processed in a standard sales document type (OR), as there is no item category determination rule for this combination. Let’s look at exactly this scenario in example 2 and see what happens.

2. Create a standard Sales Order (OR) with the product SRV\_01

   * When we try to create a sales order and add SRV\_01 as an item, the system throws an error, as there is no item category determination for the combination OR and SRVP.![](/legacyfs/online/storage/blog_attachments/2023/06/Picture2-26.png)

* + The workaround to use service product items in a sales order is to use products having an item category group **SERV**. This item category group is specifically for the ‘sale of services’ scenario, which is why this combination of OR and SERV has an item category determination rule maintained in the system.![](/legacyfs/online/storage/blog_attachments/2023/06/Picture3-27.png)

  + To achieve this, the solution is to use the product SM0001, which has the right item category group SERV that allows an item category to be determined for usage in a Sales Order. In this case, the item can be used in the Sales order without any errors![](/legacyfs/online/storage/blog_attachments/2023/06/Picture4-21.png)

The examples ab...
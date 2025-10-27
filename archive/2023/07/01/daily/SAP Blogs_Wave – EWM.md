---
title: Wave – EWM
url: https://blogs.sap.com/2023/06/30/wave-ewm/
source: SAP Blogs
date: 2023-07-01
fetch_date: 2025-10-04T11:53:56.499833
---

# Wave – EWM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Wave - EWM

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4512&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Wave - EWM](/t5/supply-chain-management-blog-posts-by-members/wave-ewm/ba-p/13548690)

![former_member314853](https://avatars.profile.sap.com/former_member_small.jpeg "former_member314853")

[former\_member314853](https://community.sap.com/t5/user/viewprofilepage/user-id/314853)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4512)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4512)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548690)

‎2023 Jun 30
10:03 PM

[7
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4512/tab/all-users "Click here to see who gave kudos to this post.")

24,917

* SAP Managed Tags
* [EWM - Basic Functions](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Basic%2520Functions/pd-p/212269919429502086862800135639950)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)
* [EWM - Master Data](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Master%2520Data/pd-p/428351855965480178787051895911518)
* [EWM - Shipping and Receiving](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Shipping%2520and%2520Receiving/pd-p/551700313515132864819929295213440)

* [EWM - Basic Functions

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BBasic%2BFunctions/pd-p/212269919429502086862800135639950)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)
* [EWM - Master Data

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BMaster%2BData/pd-p/428351855965480178787051895911518)
* [EWM - Shipping and Receiving

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BShipping%2Band%2BReceiving/pd-p/551700313515132864819929295213440)

View products (5)

Wave Management:

In this blog post, below topics related to waves are covered:

1. Waves brief overview

2. Configuration and master data settings

3. Process (testing of 2 scenarios covered)

**Waves:**

Waves comes under the outbound process in EWM. Using the wave function in EWM, you can combine items or split items from warehouse requests for outbound deliveries into waves. These waves can then be used to further create warehouse tasks/orders for picking process. By releasing the waves and confirming the warehouse tasks, you are simply confirming the picking process. Waves can be triggered or generated based on numerous parameters e.g., warehouse number, product, route, activity areas etc, which will be discussed in the configuration part.

The task of wave is to create warehouse tasks automatically at a certain time defined by the user. It will not automatically combine multiple warehouse tasks into one warehouse order (for this WOCR must be set up).

**Configuration and master data settings required:**

1. **Maintain Wave types**

2. **Maintain Wave categories**

3. **Set Automatic Wave generation for Warehouse process type**

4. **Define Field Catalogue**

5. **Define Condition Tables**

6. **Define Access Sequences**

7. **Define Condition Types**

8. **Define Determination Procedure**

9. **Assign Procedure to Document Type**

10. **Define Condition Maintenance Group**

**Additionally, there are few master data settings that are needed**

11. **Maintain Wave templates**

12. **Maintain conditions for Determining Wave Templates**

**Configuration screen shots:**

1. **Maintain Wave types![](/legacyfs/online/storage/blog_attachments/2023/06/Maintain-Wave-Types.png)**

2. **Maintain Wave categories![](/legacyfs/online/storage/blog_attachments/2023/06/Maintain-Wave-categories.png)**

3. **Set Automatic Wave generation for Warehouse process type**

* Please note that here I am using a specific warehouse process type and in-order for the product to trigger this WPT, there are other configurations and master data settings needed e.g., WPT Determination, WPT indicators etc. which will not be discussed here.![](/legacyfs/online/storage/blog_attachments/2023/06/Set-Automatic-Wave.png)

4. **Define Field Catalogue**

* Here, the user can create new fields which can be used to trigger a wave template. But in this blog, I will be using the standard fields, which are Warehouse number and Product.![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Field-Catalogue.png)

5. **Define Condition Tables**

* Here, I have created a new condition table with 2 fields from the field catalogue, namely warehouse number and product.![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Condition-Tables.png)

6. **Define Access Sequences![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Access-Sequences.png)![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Access-Sequences-2.png)**

7. **Define Condition Types![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Condition-Types.png)**

8. **Define Determination Procedure![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Determination-Procedure.png)![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Determination-Procedure-2.png)**

9. **Assign Procedure to Document Type![](/legacyfs/online/storage/blog_attachments/2023/06/Assign-Procedure-to-Document-Type.png)**

10. **Define Condition Maintenance Group![](/legacyfs/online/storage/blog_attachments/2023/06/Define-Condition-Maintenance-Group.png)**

**Once the above configurations are complete, there are certain master data which needs to be maintained.**

11. **Maintain Wave templates![](/legacyfs/online/storage/blog_attachments/2023/06/Maintain-Wave-templates.png)![](/legacyfs/online/storage/blog_attachments/2023/06/Maintain-Wave-templates-2.png)**

Note: Please note that during the creation of wave template, the cutoff date and time needs to be maintained. Else the user will get error during wave creation Refer **SAP Note: 3205144**

12. **Maintain conditions for Determining Wave Templates![](/legacyfs/online/storage/blog_attachments/2023/06/Maintain-conditions-for-Determining.png)**

**This ends the configuration and master data part.**

Additional remark: If the user needs to have multiple warehouse tasks under one warehouse order in a wave, there are other settings needed at warehouse order creation rule level. This can also be discussed later.

**End to End Process Testing:**

First, I would like to add stock into the warehouse with a simple inbound process by:

* **Creation of purchase order, inbound delivery and putaway.**

After the inbound process, I would like to run 2 scenarios related to wave. ...
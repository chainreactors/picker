---
title: Split Valuation for a material on a quality/grade basis
url: https://blogs.sap.com/2023/06/07/split-valuation-for-a-material-on-a-quality-grade-basis/
source: SAP Blogs
date: 2023-06-08
fetch_date: 2025-10-04T11:47:23.322194
---

# Split Valuation for a material on a quality/grade basis

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Split Valuation for a material on a quality/grade ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67314&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Split Valuation for a material on a quality/grade basis](/t5/enterprise-resource-planning-blog-posts-by-members/split-valuation-for-a-material-on-a-quality-grade-basis/ba-p/13553871)

![arahanth_127](https://avatars.profile.sap.com/c/b/idcb0d605ebba0717e041d5026659d79c8ff2e5a2a810bae4b703b1f404dbf0c72_small.jpeg "arahanth_127")

[arahanth\_127](https://community.sap.com/t5/user/viewprofilepage/user-id/793920)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67314)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67314)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553871)

‎2023 Jun 07
10:55 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67314/tab/all-users "Click here to see who gave kudos to this post.")

7,735

* SAP Managed Tags
* [MM Inventory Management](https://community.sap.com/t5/c-khhcw49343/MM%2520Inventory%2520Management/pd-p/402489426158095572469338199787586)
* [MM Purchasing](https://community.sap.com/t5/c-khhcw49343/MM%2520Purchasing/pd-p/507573428100543543566493124410813)

* [MM Inventory Management

  Software Product Function](/t5/c-khhcw49343/MM%2BInventory%2BManagement/pd-p/402489426158095572469338199787586)
* [MM Purchasing

  Software Product Function](/t5/c-khhcw49343/MM%2BPurchasing/pd-p/507573428100543543566493124410813)

View products (2)

**Split valuation** enables you to valuate sub-stocks (part of the total stock) of a material in different ways. The reason for split valuation includes
• The material has different origins
• The material is acquired via different types of procurement
• The material has different categories of quality

Split valuation is used only with the moving average price control, and materials subjected to split valuation can be valuated only via the moving average price method. With split valuation, we can see the total stock quantity and stock value at plant as well as the material valuation based on different grades of the material.

The **valuation category** indicates whether a material’s stock should be valuated as one unit or in parts. This category also a key that indicates the criteria for defining partial stock and determines which valuation type is allowed.

A **valuation type** is a key that identifies split-valuated stocks of a material and indicates the characteristic of a partial stock. The valuation category is assigned in the material master record, and the valuation type is selected during material transactions, such as goods issue and goods receipts.

**Configuration**

SPRO –> IMG—> Materials Management –> Valuation and Account Assignment –> Split Valuation

**1. Activate Split Valuation**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-10.png)

Select **‘Split material valuation active’**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture4-5.png)

**2. Configure Split Valuation**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture5-2.png)

**2.1 Global Types**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture6-4.png)

Click on **Create**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture7-3.png)

**For example enter**
Valuation Type – GRADE 1
Ext. Purchase Orders – 2 (External purchase orders allowed)
Acct cat. Reference – 0001 (reference for raw materials)
Click on create and save it

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture8-5.png)

**Create another valuation type as GRADE 2**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture9-2.png)

**2.2 Global Categories**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture10-2.png)

Click on **Create**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture11-2.png)

**For example enter**
Valuation Category – G
Description – Grade

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture12-2.png)

Click on **save** and then on **back**

Now place **cursor on G** and click on **Types -> Cat.**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture13-2.png)

Now place cursor on GRADE 1 and click on Activate
Then place cursor on GRADE 2 and click on Activate

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture14-3.png)

Now in the same screen click on **Cat -> OUs**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture15-1.png)

Select the **plant** and click on **activate**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture16-1.png)

**Save** it.
These steps activate the split valuation for external procurement.

**Process Steps**

**1. Create Material Master**
Create material by selecting required views
In Accounting1 view, select **Valuation Category as G** and maintain **Price control as V**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture17-1.png)

**Save** the material

**2. Extend the same material via MM01**
Enter the created material number
Select **Accounting1 view**
Now input the **plant and Valuation Type – GRADE 1**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture18-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture19-1.png)

**Save it**

**Enter material number again**
Select **Accounting1 view**
Now input the **plant and Valuation Type – GRADE 2**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture20-1.png)**Save it**

**3. Create PO**
Create PO for the material and select valuation type as **GRADE 1 in Delivery Tab**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture21-1.png)

Create **another PO** for the material and select valuation type as **GRADE 2 in Delivery Tab**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture22-1.png)

**4. Post GR for both POs**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture23-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture24.png)

**5. Check the Stock Overview - MMBE**

Stock will be displayed in two different valuation types

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture25.png)

**Conclusion:**

From the above steps, one can understood how the split valuation works for a material having different grades, and how to use this process for three different reasons to meet the business requirement. with the help of this, we can now configure the split valuation process according to the client requirement.

**References:**

[https://help.sap.com/viewer/3db8848948314edeabbea684714e1055/6.18.latest/en-US/25feb753128eb44ce1000...](https://help.sap.com/viewer/3db8848948314edeabbea684714e1055/6.18.latest/en-US/25feb753128eb44ce10000000a174cb4.html?q=batch%20determination%20in%20inventory)

**Pre requisite:** Should have Basic knowledge of materials management.

Please like, share and comment for any queries through add comment button which is displayed at bottom of the blog-post.
...
---
title: Subcontracting in SAP Business  ByDesign – Part II
url: https://blogs.sap.com/2022/12/29/subcontracting-in-sap-business-bydesign-part-ii/
source: SAP Blogs
date: 2022-12-30
fetch_date: 2025-10-04T02:44:39.777855
---

# Subcontracting in SAP Business  ByDesign – Part II

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Subcontracting in SAP Business ByDesign - Part II

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51819&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Subcontracting in SAP Business ByDesign - Part II](/t5/enterprise-resource-planning-blog-posts-by-sap/subcontracting-in-sap-business-bydesign-part-ii/ba-p/13560143)

![stefan_resag](https://avatars.profile.sap.com/3/b/id3ba27eb0a2e456a95d4e0bac292d409c5e419aa0d9bf98896c8aec397a6bbf85_small.jpeg "stefan_resag")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[stefan\_resag](https://community.sap.com/t5/user/viewprofilepage/user-id/195754)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51819)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51819)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560143)

‎2022 Dec 29
2:56 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51819/tab/all-users "Click here to see who gave kudos to this post.")

3,119

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)

View products (1)

You might be familiar with the blog post of my colleague about [Subcontracting in Business ByDesign,](https://blogs.sap.com/2017/04/12/subcontracting-in-business-bydesign/) that mainly focuses on how the logistics material flow in a subcontracting process can be modelled using two different sites in SAP Business ByDesign.

In this blog post I want to have a deeper look into how one could set up the system to better align the production process with the service purchasing process.

Let me start with an overview of the subcontracting process using two sites: (Subcon1.PNG)

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon1.png)

The following steps need to be executed to run the process (more details can be found in the blog mentioned above):

1. Create a sales order for the finished product (Painted Sheet).

2. Run the MRP in site P1100 to create a stock transfer proposal to cover the sales demand.

3. Run the multi-level MRP in subcontractor site SR1100 to create a production order for the painted sheet and a stock transfer proposal for the sheet and paint to cover the production component demand.

4. Run the MRP in P1100 to create a purchase proposal for the sheet and paint, order the components, and post the goods receipt.

5. Create a purchase order for the subcontracting service.

6. Release the stock transfer proposal for the sheet and paint, and post the goods issue and goods receipt to move the sheet and paint from site P1100 to site SR1100.

7. Release the production proposal and release the production order.

8. Confirm the purchase order of the subcontracting service and confirm the production order in site SR1100 to create the painted sheet.

9. Release the stock transfer proposal for the painted sheet and post the goods issue and goods receipt to move the painted sheet from site SR1100 to site P1100.

10. Post invoice for the subcontracting service.

11. Ship the painted sheet to the customer.

In this modelling approach the subcontracting process is mainly divided into two separate processes:

1. The logistics process to model the flow of materials.

2. The service purchasing and invoicing process

When running the subcontracting process, the company must ensure that the logistics process and the purchasing process are as much in sync as possible:

* The purchasing costs and the production order service costs should be in sync, to have a proper material cost estimate and production lot costing.

* The quantity of the painted sheet delivered by the subcontractor should be in sync with the quantity of the service invoiced.

In the following I want to propose some modelling approaches that could help to simplify this synchronization.

Let me start with the service master data. In subcontracting it is a common practice that a price is defined based on the unit of measure of the good received by the subcontractor. In my example, a subcontractor might invoice for the number of sheets that got painted. As a consequence the service UoM could be defined in ‚Each (EA)‘.

Next the service purchasing costs normally need to be assigned directly to the production lot. However, the production lot is not supported as an account assignment object in purchasing documents. As a workaround, you could use the same cost center in the production resource master data and the purchasing documents.

When the service valuation is kept in sync with the purchasing price, the costs would then be implicitly moved from the purchasing document via the cost center onto the production lot. In addition, by defining the production resource consumption being proportional to the operation quantity, I create a direct link between the quantities produced by the subcontractor and the production service costs.

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon2.png)

In the following I will guide you through all master data and an end-to-end process with the above modelling approaches.

I have set up a service ‘SR\_PAINTING’ with a base UoM = EA and a cost rate, that should reflect the purchasing price of the service.

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon3.png)

In the service list price, I have maintained an amount identical to the service valuation costs.

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon4.png)

Next, let’s look at the production model.

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon4-1.png)

Since the painting operation is executed at the subcontracting side, I have assigned the production model to my subcontracting site SR1100. The Bill-of-Operations (BoO) is defined for a quantity of 1 EA for the output product SR\_SC\_FG\_01.

Next, let me have a look at the production activity, specifically at the services. Here, I use the same service, for which I have defined the list price. Since I want to calculate the service costs in EA, I set the ‘Calculation Method’ to ‘Proportional to Operation Quantity’, and the ‘Variable Quantity’ to 1 EA.

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon5.png)

Now we need to understand the relationship between the bill of operation activity and the resource master data. In my bill of operation activity, I have used a new activity type ‘Painting’.

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon6.png)

These activity types can be defined in the business option ‘Activity Types for Bills of Operations’, which you can find in the ‘Fine Tuning’ section of business configuration.

![](/legacyfs/online/storage/blog_attachments/2022/12/Subcon7.png)

Now let’s check the resource master data. Since the resource is used in Sit...
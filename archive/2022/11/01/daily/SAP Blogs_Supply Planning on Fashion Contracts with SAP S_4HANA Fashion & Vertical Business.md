---
title: Supply Planning on Fashion Contracts with SAP S/4HANA Fashion & Vertical Business
url: https://blogs.sap.com/2022/10/31/supply-planning-on-fashion-contracts-with-sap-s-4hana-fashion-vertical-business/
source: SAP Blogs
date: 2022-11-01
fetch_date: 2025-10-03T21:25:40.798626
---

# Supply Planning on Fashion Contracts with SAP S/4HANA Fashion & Vertical Business

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Supply Planning on Fashion Contracts with SAP S/4H...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67576&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Supply Planning on Fashion Contracts with SAP S/4HANA Fashion & Vertical Business](/t5/enterprise-resource-planning-blog-posts-by-members/supply-planning-on-fashion-contracts-with-sap-s-4hana-fashion-vertical/ba-p/13557346)

![arijitm09021](https://avatars.profile.sap.com/7/6/id765e671582509de1599504357a54d322389ad35f3cc49e3d88b4d6b09999d08e_small.jpeg "arijitm09021")

[arijitm09021](https://community.sap.com/t5/user/viewprofilepage/user-id/819416)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67576)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67576)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557346)

‎2022 Oct 31
7:41 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67576/tab/all-users "Click here to see who gave kudos to this post.")

4,189

* SAP Managed Tags
* [SAP Demand Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Demand%2520Management/pd-p/01200615320800000690)
* [SAP ERP add-on for retail](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520add-on%2520for%2520retail/pd-p/01200615320800000172)
* [SAP Fashion Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fashion%2520Management/pd-p/67838200100800006229)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP ERP add-on for retail

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2Badd-on%2Bfor%2Bretail/pd-p/01200615320800000172)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fashion Management

  SAP Fashion Management](/t5/c-khhcw49343/SAP%2BFashion%2BManagement/pd-p/67838200100800006229)
* [SAP Demand Management

  SAP Demand Management](/t5/c-khhcw49343/SAP%2BDemand%2BManagement/pd-p/01200615320800000690)

View products (4)

Introduction:

This blog will elaborate on how Fashion Contract solves the demand management problem for fashion products manufacturer. To understand the SAP solution, we need to get a brief understanding of the fashion industry terminology and the demand flow process.

![](/legacyfs/online/storage/blog_attachments/2022/10/Image1-11.png)

                                                                Illustration 1: Terminology & Demand Flow

The Readymade Garments brand owner places a speculative order to the manufacturer (Vendor for the brand owner) to help them book the main raw material (fabric) beforehand. It’s because of the high lead time of fabric manufacturing along with the seasonality of fashion (garments) products. The other most critical parameter where is launch date. The brand owners or retailers decide a specific launch date of new style based on market perception. This is a mandatory date to follow. Else, market perception will be adversely impacted and the retailers will have huge dead stock. SO, the availability of fabric is very crucial to allow the garments manufacturer to complete and ship the goods.

Furthermore, the manufacturer needs the confirm orders (Sales Orders) which are derivation of the main speculative order to start the manufacturing cycle and shipment. The other complexity is shade (color) of garments, which calls for numerous shades and types of fabric. This mix is very complex. So, the manufacturer faces a great amount of challenge to allocate fabric orders to the firm orders. Here we should keep in mind that Fashion Industry works in demand driven environment. So, it is imperative to connect all fabric procurements to the sales orders.

The below illustration helps us to understand the role-based process flow between the retailer and its vendor.

![](/legacyfs/online/storage/blog_attachments/2022/10/Image2-6.png)

Illustration 2: Process Flow – Flow of Demands from Retailer & Manufacturer

Core Solution

There 2 challenges in the problem statement. The first one is to plan main raw material fabric based on a speculative order. The second one is after receiving the firm orders (Sales Orders), manual & time-consuming effort to assign & distribute fabric purchase requisitions / purchase orders to it.

There are specific solutions for these challenges in SAP S/4HANA with IS solution Fashion & Vertical Business (FVB). To understand why SAP S/4HANA came up with a solution, we must look into the gap we had in SAP ECC for challenges like this. The below illustration will elaborate the gaps in SAP ECC and current solution in SAP S/4HANA FVB.

![](/legacyfs/online/storage/blog_attachments/2022/10/Image3-7.png)

                                                Illustration 3: Comparison of Solutions in ECC & S/4HANA

SAP S/4HANA with IS solution Fashion & Vertical Business solves the first challenge with Fashion Contract. Fashion contract is a sales contract with advance features in SAP S/4HANA Fashion & Vertical Business environment. The advance feature is that we can mark fashion contract relevant to MRP live through configuration. Thus, one can create a fashion article and it’s BOM to capture fabric consumption. Then create a fashion contract with the article and quantity to capture the speculative order. The next step MRP live will create a Purchase Requisition for fabric.

The solution for the automatic assignment of dependent requirement of Fabrics like Purchase Requestions or Purchase Orders from Fashion Contract to Sales Orders by Segmentation. Let us take an example that the retailer purchase order for speculative order is TBA-ORDER-01. This will be a fashion contract. Now, the retailer converts a part of this speculative order to sales order through a purchase order ITALY-ORDER-01. This will be a sales order in SAP. Now, the fabric purchase requisition by first MRP run will have segment TBA-ORDER-01. This will be auto assigned with distributed quantity to the sales order segment ITALY-ORDER-01.

To achieve the solution for the solution for second part, we must mention the segment values in SGTC in a fashion illustrated below. It shows the sales order segment must be linked to fashion contract segment.

![](/legacyfs/online/storage/blog_attachments/2022/10/Image4-8.png)

Illustration 4: Fashion Contract to Sales Order Segment mapping

The step-by-step solution provided below. It indicates automated outcome of SAP to provide benefits to fashion clients.

![](/legacyfs/online/storage/blog_attachments/2022/10/Image5-7.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Image5A.png)

                Illustration 5: Process Flow Diagram in SAP S/4HANA Fashion & Vertical Business

The transactional flow of this SAP solution provided below.

Step 1: Fashion Contract with a Garment Article FASHION\_SHIRT with 10000 Pieces as quantity.

![](/legacyfs/online/storage/blog_attachments/2022/10/Image6-7.png)

                                              ...
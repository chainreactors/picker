---
title: SAP® Extended Warehouse Management in SAP S/4HANA 2022 – What’s New
url: https://blogs.sap.com/2022/10/30/sap-extended-warehouse-management-in-sap-s-4hana-2022-whats-new/
source: SAP Blogs
date: 2022-10-31
fetch_date: 2025-10-03T21:21:06.174074
---

# SAP® Extended Warehouse Management in SAP S/4HANA 2022 – What’s New

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* SAP® Extended Warehouse Management in SAP S/4HANA ...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/4896&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP® Extended Warehouse Management in SAP S/4HANA 2022 – What’s New](/t5/supply-chain-management-blog-posts-by-sap/sap-extended-warehouse-management-in-sap-s-4hana-2022-what-s-new/ba-p/13558228)

![florian_kuchta2](https://avatars.profile.sap.com/0/5/id05688489d223a17638a09c573df6654136fc2d2ce6e2c4f7236884d78fa05e5c_small.jpeg "florian_kuchta2")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[florian\_kuchta2](https://community.sap.com/t5/user/viewprofilepage/user-id/444385)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=4896)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/4896)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558228)

‎2022 Oct 30
9:19 AM

[28
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/4896/tab/all-users "Click here to see who gave kudos to this post.")

38,788

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)

View products (1)

We are once again in the final quarter of the year, which means that it is time to share with you the latest updates to [SAP EWM that came with the SAP S/4HANA 2022 release](https://d.dam.sap.com/a/FXnQfZM/EWM_2022_Whats_New_V1_FINAL_VERSION.pdf?rc=10).

This release represents a massive endeavour by our development teams, and I want to thank them for their commitment and efforts to deliver such a feature rich release.

In this year’s release we continued to invest in stronger integration with Quality Management, Manufacturing and Transportation solutions, delivered features tailored for the retail/wholesale/fashion automotive & oil and gas industries, worked on enhancing usability and user experience and much more. In the following article, we will go through the areas of our investments for this release as well as some of the highlights in each area. And we begin with one of our key focus areas of this release, Integration.

**INTEGRATION**

**Automatic Packing with Unified Package Builder**

In the SAP S/4HANA 2021 release we delivered the Unified Package Builder, a generic packaging layer that allows the creation of packages via different unified package building engines, such as: Package building with the package builder; Packing Instruction; Packaging specification.

In this year’s release, we provide warehouse operators the ability to use unified package building in even more processes to automatically pack unpacked delivery items in the “Change Inbound Deliveries” apps and in the “Unloading” and “Receiving Handling Units” Radio Frequency (RF) transactions.

![](/legacyfs/online/storage/blog_attachments/2022/10/UPB-Flow-Chart-1.png)

Usage of the UPB in additional SAP EWM processes

An example use case for this feature is the scenario when a vendor sends an inbound delivery that does not contain any packing information about the handling units (HUs). Users can then specify that the system automatically packs any unpacked delivery items by using one of the package building engines available in the UPB.

**Customer Defined Picking and Packing**

In some industries, it is quite common for finished goods to be packaged according to customer specifications. However, it was not possible to specify customer specific packing for outbound deliveries. With the SAP S/4HANA 2022 release we can now ensure that during customer-defined packing and picking, only those handling units are picked that were created with a reference to a specific sales scheduling agreement and according to a specific packing instruction (PI) or packaging specification (PS). Accordingly, it is also now possible to protect the required HUs from any changes. This process can be activated by a new indicator in the SD scheduling.

**Quality Management Enhancements**

As with every major release, we continue to improve integration with Quality Management functionalities. In SAP S/4HANA 2022, we deliver the following enhancements:

* **Quality Inspections for Synchronous Goods Receipt Postings**

With this feature, customers with QM requirements can now directly post synchronous goods receipts from other parts of SAP S/4HANA into Extended Warehouse Management (EWM) for goods procured externally or goods from in-house production. The system creates an inspection lot in any ERP transactions where a goods receipt can be posted for a product that's inspection-relevant, for example, in the “Post Goods Movements” app. Inspection lot summary, skip lots and cancellations are supported as well. Note that this feature is available only for EWM embedded in SAP S/4HANA.

![](/legacyfs/online/storage/blog_attachments/2022/10/QM-in-Sync-GR-Postings-1.png)

Quality Inspection Supported Transactions

* **for Goods Receipt**

For compliance purposes, users can now capture the existence of external quality certificates when receiving goods procured from suppliers. The system ensures the receipt of the quality certificate before it is possible to record a usage decision. The existence of these certificates can then be passed via an inbound delivery to SAP ERP QM inspection lot.

![](/legacyfs/online/storage/blog_attachments/2022/10/Quality-Certificates-for-GR-1.png)

Quality Certificate Document Flow

* **Skipping of Quality Inspections in Decentralized SAP EWM**

Also in this release, we made it possible to skip quality inspections if the goods don't need to be inspected because of the current quality level. When skipping inspections, the system still creates inspection documents but posts the goods from quality stock to unrestricted-use stock without performing an inspection. Note that this feature is new for decentralized Extended Warehouse Management (EWM) based on SAP S/4HANA but it's already available for EWM embedded in SAP S/4HANA.

* **Inspection Lot Summary** **per Delivery Item**

Before SAP S/4HANA 2022 the summary of complete inbound delivery was placed into one inspection lot in case of multiple items with the same material/batch combination. With the 2022 release, users of embedded EWM in SAP S/4HANA can switch to have one inspection lot per delivery item via the IMG Activity “Define and Activate Warehouse-Dependent IOTs”.

**Advanced Shipping & Receiving Enhancements**

Since the SAP S/4HANA 2020 FPS01 release of the new integration between SAP EWM and SAP TM, Advanced Shipping & Receiving, SAP has worked on feature enhancements in every mainline SAP S/4HANA update. The 2022 release is no different, and to that end, for SAP EWM we delivered the following:

* **Order Based Planning**

We d...
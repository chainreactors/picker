---
title: SAP S/4HANA 2022: New BAdI to influence MRP elements in MRP Live and Classic MRP
url: https://blogs.sap.com/2023/08/03/sap-s-4hana-2022-new-badi-to-influence-mrp-elements-in-mrp-live-and-classic-mrp/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:27.158069
---

# SAP S/4HANA 2022: New BAdI to influence MRP elements in MRP Live and Classic MRP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA 2022: New BAdI to influence MRP elemen...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53123&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA 2022: New BAdI to influence MRP elements in MRP Live and Classic MRP](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-2022-new-badi-to-influence-mrp-elements-in-mrp-live-and-classic/ba-p/13568425)

![Caetano](https://avatars.profile.sap.com/7/6/id767c5ebe9a965d28133f046fc58a01b457d6863b7ec5004dcfbda060c6fd896d_small.jpeg "Caetano")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Caetano](https://community.sap.com/t5/user/viewprofilepage/user-id/121014)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53123)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53123)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568425)

‎2023 Aug 03
8:59 PM

[31
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53123/tab/all-users "Click here to see who gave kudos to this post.")

26,434

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [MAN (Manufacturing)](https://community.sap.com/t5/c-khhcw49343/MAN%2520%28Manufacturing%29/pd-p/9aaa6d7b-e017-4ddc-805d-9bbd02a6c46d)
* [MAN Material Requirements Planning](https://community.sap.com/t5/c-khhcw49343/MAN%2520Material%2520Requirements%2520Planning/pd-p/320517996275254407406398077757010)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [MAN Material Requirements Planning

  Software Product Function](/t5/c-khhcw49343/MAN%2BMaterial%2BRequirements%2BPlanning/pd-p/320517996275254407406398077757010)
* [MAN (Manufacturing)

  Software Product Function](/t5/c-khhcw49343/MAN%2B%252528Manufacturing%252529/pd-p/9aaa6d7b-e017-4ddc-805d-9bbd02a6c46d)

View products (6)

SAP S/4HANA introduced the new BAdI PPH\_SUPPLY\_DEMAND\_LIST, which allows us to change, add or exclude MRP elements from the MRP run in both MRP Live and Classic MRP. This BAdI is also called in MRP evaluation transactions (such as MD04) and the MRP Cockpit Fiori Apps. This blog provides more details about this BAdI, explaining why it was created and the benefits of using this BadI.

**Manipulating MRP elements using BAdIs**

Influencing MRP elements is a very common requirement for companies running MRP, and very often enhancements are implemented to make a specific element not relevant to MRP, or to change specific attributes of an MRP element, such as date and quantity.

In the old ECC world, we could use BAdI MD\_CHANGE\_MRP\_DATA to easily implement a custom code that would influence an MRP element, and I even wrote a [blog](https://blogs.sap.com/2014/10/01/making-an-element-not-relevant-to-mrp-using-badi-mdchangemrpdata/) explaining how this BAdI could be used to make an MRP element not relevant to MRP.

In the S/4HANA world, however, this BAdI is no longer relevant. In classic MRP, this BAdI was called when MRP was reading the planning elements from the database, and this logic was pushed down into the HANA layer, in order to improve the MRP performance, and MRP Live runs completely in HANA, so an ABAP BAdI cannot be called.

Until now, the alternative was to use ABAP BAdI MD\_ADD\_ELEMENTS, which would work in classic MRP and MRP evaluation transaction (such as MD04) and the AMDP BAdI PPH\_MRP\_RUN\_BADI in MRP Live (AMDP stands for **A**BAP **M**anaged **D**atabase **P**rocedures, and it is a procedure executed directly in the HANA database).

While those BAdIs were very handy, there were two downsides of implementing them in SAP S/4HANA: In most cases MRP Live plans a material in HANA, and the AMDP BAdI is called, but there are situations where MRP Live needs to plan a material in ABAP, and the AMDP BAdI won't work. It means that both BAdIs had to be implemented, leading to additional development efforts and costs. In addition to that, the ABAP BAdI is called in the MRP evaluation transactions, such as MD04, but it is not called in the MRP Fiori Apps, which means that user would see different results depending on the transaction or app that was used.

**New BadI PPH\_SUPPLY\_DEMAND\_LIST**

In order to resolve those problems, SAP S/4HANA 2022 introduced the new BAdI PPH\_SUPPLY\_DEMAND\_LIST. This is an AMDP BAdI, which means that it runs directly in the HANA database, and it will work in **Classic MRP**, **MRP Live**, **MRP Fiori Apps** and **Stock/Requirements List (MD04)**.

![](/legacyfs/online/storage/blog_attachments/2023/08/BAdI-1.png)

This BAdI brings only one method called MODIFY\_SUPPLY\_DEMAND\_LIST, which is called by the stored procedures that will read the planning elements from the database, which means that we can change attributes of a planning element, add new planning elements, or even make planning elements not relevant for MRP.

There are several import parameters to the BAdI method, as you can see in the following figure, which will bring useful information, like the user or the planning date. There is one changing parameter called CT\_SUPPLYDEMANDITEMLIST, which will bring the list of supply and demand elements (sales orders, production orders, planned orders, purchase requisitions, etc...) that MRP read from the database for a specific material.

![](/legacyfs/online/storage/blog_attachments/2023/08/blog2.png)

It is important to mention that changes in planning elements made by an implementation of this BAdI will only be considered by MRP during the planning run, and they will not be saved into the database. For example, if you use this BAdI to change a planned order date, MRP will consider the adjusted date for this planned order during the planning run, but the dates won't be changed in table PLAF.

Also, any changes implemented by this BAdI are taken into consideration by MRP during net requirements calculation, and no consistency check is carried out after the BAdI execution. Therefore, if you adjust the quantity of a plannin...
---
title: Live Loading or Direct Loading using DirODO STO delivery
url: https://blogs.sap.com/2022/12/03/live-loading-or-direct-loading-using-dirodo-sto-delivery/
source: SAP Blogs
date: 2022-12-04
fetch_date: 2025-10-04T00:28:52.457228
---

# Live Loading or Direct Loading using DirODO STO delivery

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Live Loading or Direct Loading using DirODO STO de...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4860&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Live Loading or Direct Loading using DirODO STO delivery](/t5/supply-chain-management-blog-posts-by-members/live-loading-or-direct-loading-using-dirodo-sto-delivery/ba-p/13565691)

![shailesh_mishra5](https://avatars.profile.sap.com/f/6/idf67309dd2c1615e42ecc904385bfe07e45eb89980327c6f0361f1b8d135c9ced_small.jpeg "shailesh_mishra5")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[shailesh\_mishra5](https://community.sap.com/t5/user/viewprofilepage/user-id/212388)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4860)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4860)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565691)

‎2022 Dec 03
1:26 AM

[11
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4860/tab/all-users "Click here to see who gave kudos to this post.")

7,432

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)
* [EWM - Interfaces](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Interfaces/pd-p/828895203045710275663878834115743)
* [EWM - Radio Frequency](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Radio%2520Frequency/pd-p/382876162660666448662353059935346)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)
* [EWM - Interfaces

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BInterfaces/pd-p/828895203045710275663878834115743)
* [EWM - Radio Frequency

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BRadio%2BFrequency/pd-p/382876162660666448662353059935346)

View products (6)

### ***Conception***

In past, I have already written a blog on Direct ODO creation from EWM which creates replenishment delivery and corresponding STO PO between 2 Plants. The current blog is an attempt to explain how **DirODO can be integrated with Shipping and Receiving** functionality with Pallets build up at Production supply Area using Advanced Production Integration with RF capability. More often than note, customers are keen to use this process directly on RF instead of desktop based transaction. SAP standard provides a very generic solution on this which often needs to be altered as per customer requirement.

### ***Definition***

The scenario is checking homogenous full pallets of finished goods arriving from production and Finished Goods after palletization are directly loaded into truck without storing the Pallets into final storage because of Short shelf life of Products( Bakery industry) or because of storage bottleneck.

The '**Direct Loading**' scenario is checking homogenous full pallets of finished goods that have been received from production. The idea of the direct loading is very much close with **Shuttle Service** process relates to a regular traffic between a manufacturing unit and one or more related warehouses.

![](/legacyfs/online/storage/blog_attachments/2022/12/PIC1-1.png)

In the above example, HUs are received against manufacturing order which is directly GRed and Putawayed into PSA Line. Here, production operator will label the FG pallets which are ready to be shipped and loaded directly into the truck. The shipments are stock transferred from production Site( Plant or SLOC) to another Plant or Sloc.

This blog is written on Direct ODO STO delivery between 2 storage location as plant to plant I had already covered in past.

### ***Replication Steps***

**Consideration**

1) Advanced production Integration is implemented.

2) Basic set of Shipping & Receiving is implemented.

3) STO set up between 2 storage location of Plant connected to 2 different Whse.

4) Business Partner and master datas.

Production Operators start receiving Products at PSA and start palletization against manufacturing Order

![](/legacyfs/online/storage/blog_attachments/2022/12/pic2-1.png)

3 HUs have been received and Putawayed into PSA Line 1

![](/legacyfs/online/storage/blog_attachments/2022/12/pic3-1.png)

To integrate with Shipping & Receiving, use the below BC sets which allows Pallets loading on TU. Remember you should take Document type **ODSH only and** latter you can switch off the picking status only Loading functionality is required.

![](/legacyfs/online/storage/blog_attachments/2022/12/pic4-1.png)

Warehouse Operators has the visibility of Pallets which are received and which are in Process. **Warehouse Mon View.**

![](/legacyfs/online/storage/blog_attachments/2022/12/pic5-1.png)

Create DirODO with /SCWM/PRDO, enter BP as Plant( Here Sending and Receiving Plant is same) but Receiving S4 Storage location is customer.

3 HUs from PSA have been assigned to **DIrODO 1822 which is ready for loading.**

![](/legacyfs/online/storage/blog_attachments/2022/12/pic6-1.png)

Create aTU, assign the delivery 1822, perform TU docking at Door in /SCWM/TU. Ofcourse, there can be an enhancement of auto TU creation, I did not find any standard option of creating TU directly from ODO delivery.

Once HUs are assigned to TU, and TU is arrived at Door, ensure to activate a PPF for auto Loading WT from PSA to Door.Loading creates HU WTs from the PSA area to the door for the ODSH delivery. Since TU is docked at the door, when confirming WT in RF, **destination of WT is changed directly to the TU.**

Perform Loading of HUs with RF.

![](/legacyfs/online/storage/blog_attachments/2022/12/pic7-1.png)

In below examples, 2 HUS are loaded to trailer and one is remain to be loaded. This gives warehouse operator a high level of visibility of how many Pallets have been loaded into Trailer.

![](/legacyfs/online/storage/blog_attachments/2022/12/pic8-1.png)

Once loading is completed, Auto GI can be triggered if auto GI at TU level ...
---
title: Quality Inspection of Nested HUs with follow up task for Top & Sub HU level
url: https://blogs.sap.com/2023/01/21/quality-inspection-of-nested-hus-with-follow-up-task-for-top-sub-hu-level/
source: SAP Blogs
date: 2023-01-22
fetch_date: 2025-10-04T04:33:30.126784
---

# Quality Inspection of Nested HUs with follow up task for Top & Sub HU level

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Quality Inspection of Nested HUs with follow up ta...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4534&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Quality Inspection of Nested HUs with follow up task for Top & Sub HU level](/t5/supply-chain-management-blog-posts-by-members/quality-inspection-of-nested-hus-with-follow-up-task-for-top-sub-hu-level/ba-p/13549495)

![shailesh_mishra5](https://avatars.profile.sap.com/f/6/idf67309dd2c1615e42ecc904385bfe07e45eb89980327c6f0361f1b8d135c9ced_small.jpeg "shailesh_mishra5")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[shailesh\_mishra5](https://community.sap.com/t5/user/viewprofilepage/user-id/212388)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4534)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4534)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549495)

‎2023 Jan 21
2:27 AM

[12
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4534/tab/all-users "Click here to see who gave kudos to this post.")

5,585

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)
* [EWM - Master Data](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Master%2520Data/pd-p/428351855965480178787051895911518)
* [PLM Quality Management (QM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Quality%2520Management%2520%28QM%29/pd-p/484135010855456218597016630642366)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [PLM Quality Management (QM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BQuality%2BManagement%2B%252528QM%252529/pd-p/484135010855456218597016630642366)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)
* [EWM - Master Data

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BMaster%2BData/pd-p/428351855965480178787051895911518)

View products (5)

### ***Objective:***

* To establish a flow how nested HU can be relevant for Quality inspection for Inbound receiving process considering a shipment is arriving in Pre-Packed form at Pallet level and at box level.

* Figure out how Usage decision can be conducted at Top HU level and at Sub HU level.

* Address the core issues of Warehouse task creation at Top HU level or Sub HU level or Product WT creation with Top & Sub HU.

* Address why Top HU is getting deleted in Non POSC scenarios and explore all the possibilities of top HU retention in system.

In below example, a nested HU is depicted which is relevant for quality inspection. The main objective of the blog is to figure out different behaviours of Warehouse task creation with Direct Putaway and with complex putaway including Unload, Quality Inspection & Putaway.

![](/legacyfs/online/storage/blog_attachments/2023/01/pic1-2.png)

***Scenario I: Direct Putaway: Product WT with Sub HU after UD:***

Nested HU is received in staging area, posted GR and relevant for quality activity.**( Process 2 in flow).**Product is packed into Top( Pallet level) and Sub( Box) level HU and posted GR at staging area.

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC2-6.png)

Perform QI UD from Staging area( Only Embedded EWM allows Partial UD, EWM inspection from Staging area). UD is performed at top level HU ending with **469.**

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC3-5.png)

Once UD is completed & saved, partial UD set can be seen how it is fetched.

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC4-3.png)

On completion of UD,  **Product Warehouse task is created with Sub HU**

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC5-1.png)

The top HU ending with **469** is **deleted once UD is performed**. This process leaves business  with no option of having flexibility of **HU WT at top HU.**

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC6-1.png)

In the final Bin, stock is updated at **Sub HU level ending with 452.**

![](/legacyfs/online/storage/blog_attachments/2023/01/pic7-1.png)

***Case II: Introduce a POSC with QIS step.( Process 1 as depicted in above diagram). HU wt with Top HU***

For the below example, POSC has been set up as Unload+ QIS+Putaway. Once UD is performed for Top level HU having QIS step wired into it, it cancelled a previous Task and created **Top HU WT.**

![](/legacyfs/online/storage/blog_attachments/2023/01/pic8-1.png)

The Top HU is retained in system as depicted below and allows Pallet level  ending with **438** & Box level ending with **445** inventory in warehouse stock.

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC8A1-1.png)

***Case III: Product WT with Top HU( Process 2 shown in diagram)***

Change the Internal action as blank in follow up action. This will trigger only posting change when UD is completed. Then the product WTs can be created automatically after the HU is closed on the workcenter.

![](/legacyfs/online/storage/blog_attachments/2023/01/pic9-2.png)

Fore this process, created a Unloading WT from Door to staging area and confirmed all relevant activity task required.

![](/legacyfs/online/storage/blog_attachments/2023/01/pic10-1.png)

Before UD, **a Product WT is created with Top HU with waiting status( Process number 2 in diagram)**

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC11-1.png)

Top HU ending with **476** and Sub HU ending with **483** is shown as below

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC12-1.png)

Perform UD at top level HU.

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC13-2.png)

Product WT is created with Top level HU as below( Process 2 diagram) with open status.

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC14-1.png)

Inventory is updated at pallet level and box level as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/01/pic15-1.png)

It would be noteworthy to evaluate in business process whether the subHUs are required at all in this process. If complete stock is put into the topHU,  and requirement is to only  enter one usage decision for the complete stock then the follow up action will create **one WT for this topHU.** If necessary, the stock could also be repacked after the usage decision has been made.
...
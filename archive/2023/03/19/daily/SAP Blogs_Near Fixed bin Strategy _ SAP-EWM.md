---
title: Near Fixed bin Strategy : SAP-EWM
url: https://blogs.sap.com/2023/03/18/near-fixed-bin-strategy-sap-ewm/
source: SAP Blogs
date: 2023-03-19
fetch_date: 2025-10-04T10:02:21.426381
---

# Near Fixed bin Strategy : SAP-EWM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Near Fixed bin Strategy : SAP-EWM

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4613&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Near Fixed bin Strategy : SAP-EWM](/t5/supply-chain-management-blog-posts-by-members/near-fixed-bin-strategy-sap-ewm/ba-p/13552656)

![ewmbee786](https://avatars.profile.sap.com/9/f/id9f4b343e7866180fba6d2539c75c83d94b746b8d7e069032f4fe5d8fbe24ae8f_small.jpeg "ewmbee786")

[ewmbee786](https://community.sap.com/t5/user/viewprofilepage/user-id/674425)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4613)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4613)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552656)

‎2023 Mar 18
1:36 PM

[16
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4613/tab/all-users "Click here to see who gave kudos to this post.")

12,606

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Basic Functions](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Basic%2520Functions/pd-p/212269919429502086862800135639950)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)
* [EWM - Interfaces](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Interfaces/pd-p/828895203045710275663878834115743)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Basic Functions

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BBasic%2BFunctions/pd-p/212269919429502086862800135639950)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)
* [EWM - Interfaces

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BInterfaces/pd-p/828895203045710275663878834115743)

View products (5)

Introduction : To increase the efficiency of the picking process , warehouses are opting picking from fixed bins and when ever required doing the replenishment from the reserve are to fixed bins.

So in order to replenish the qty from reserve to fixed bins, businesses are expecting to put away  the stock at near fixed bins , so that it will be easier to replenish from reserve to fixed bin.

We will consider a business case where a fixed bins in level 1 and high rack set up is above fixed bin from level 2 to level 5 as shown below.

Fixed bin Structure  is : YFIX

Bin structure:  AA SS L

Bin Start value: 50-01-1

Bin End value:  59-05-1

Reserve area storage bin structure: VF01

Bin structure:  AA SS L

Bin Start value: 50-01-2

Bin End value:  59-05-5

![](/legacyfs/online/storage/blog_attachments/2023/03/D1.png)

To achieve above requirement we need to follow below steps

1. Configuration steps

* Configure the Reserve Storage type

* Configure the Fixed storage type

* Define WPT

* Determine WPT

* Put away strategies ( STSS,PACI and Bin structure) s

* Fixed bin assignment to product

* Product master Extension.

* Define the Near fixed bin put away rule .

2.Testing

* Create PO

* Create IBD

* Process IBD to create the put away WT.

Configurations:

* Storage type Configuration for Reserve area ( High Rack above the fixed bin storage type)

Put away rule- 5 , Next empty bin

SrchRule Empty bin-1 Near fixed bin

Storage behavior- Standard Warehouse.

![](/legacyfs/online/storage/blog_attachments/2023/03/1-48.png)

* Fixed bin storage type configurations:

Use Fixed bin – Tick the box

![](/legacyfs/online/storage/blog_attachments/2023/03/2-27.png)

* Define Warehouse Process Type – VF10

![](/legacyfs/online/storage/blog_attachments/2023/03/3-29.png)

* Determine WPT.

![](/legacyfs/online/storage/blog_attachments/2023/03/4-21.png)

* Put away Strategies.

5.1)Storage Type Search Sequence:

![](/legacyfs/online/storage/blog_attachments/2023/03/5.1.png)

5.2)  Put away control indicator:

![](/legacyfs/online/storage/blog_attachments/2023/03/5.2.png)

5.3) Assign Storage types to Storage type Search sequence.

![](/legacyfs/online/storage/blog_attachments/2023/03/5.3.png)

5.4) Specify Storage type search Sequence for put away.

![](/legacyfs/online/storage/blog_attachments/2023/03/5.4.png)

5.5) Storage bin structure of Fixed storage type -YFIX.

![](/legacyfs/online/storage/blog_attachments/2023/03/5.5.png)

5.6) Storage bin structure of Fixed storage type – VF01

![](/legacyfs/online/storage/blog_attachments/2023/03/5.6.png)

* Now Do the fixed bin assignment to the product as below.

Product -5001031 is assigned to the bin 50-05-01.

![](/legacyfs/online/storage/blog_attachments/2023/03/6-17.png)

* Assign PTDI and PACI to product master.

![](/legacyfs/online/storage/blog_attachments/2023/03/7-15.png)

* Define the Near fixed bin put away rule as below.

SPR0-> IMG SETTINGS-> SCM EWM-> EWM-> GOODS RECIPT-> STRATEGIES-> PUT AWAY RULES-> SORTING NEAR TO PICKING BIN->  STORAGE TYPE CONTROL- NEAR TO PICKING FIXED BIN

![](/legacyfs/online/storage/blog_attachments/2023/03/8-10.png)

Here assign the warehouse number with fixed bin storage type and reserve storage type with Bin structure.

Testing :

Now the product is assigned to the bin 50-01-05 there are multiple other bins are in the sort sequence but as per the structure system should determine the near fixed bin which is 50-01-2.

![](/legacyfs/online/storage/blog_attachments/2023/03/T1.jpg)

From above screen shot , we can observe there are multiple empty bins are available to occupy the product but system has to determine the bin 50-05-2 which is exactly the top of the bin 50-05-1 which is assigned to the product as fixed bin.

* Create PO in

![](/legacyfs/online/storage/blog_attachments/2023/03/9-12.png)

* Create Inbound delivery in VL31n.

![](/legacyfs/online/storage/blog_attachments/2023/03/10-14.png)

* Now we are processing this Inbound delivery in /N/SCWM/PRDI.

After Unloading and GR , we are trying to create the Put away WT.

![](/legacyfs/online/storage/blog_attachments/2023/03/11.1.jpg)

As we expected system determined the bin 50-05-2 which is exactly above the fixed bin .

Conclusion: As seen above ,I hope you understand the Near fixed bin storage type strategy.

Regards

Rohela.

* [EWM](/t5/tag/EWM/tg-p/board-id/scm-blog-members)
* [SAPCommnity](/t5/tag/SAPCommnity/tg-p/board-id/scm-blog-members)
* [sapewm](/t5/tag/sapewm/tg-p/board-id/scm-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* ...
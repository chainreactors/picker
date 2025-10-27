---
title: Reason code and movement type in SAP EWM
url: https://blogs.sap.com/2023/01/05/reason-code-and-movement-type-in-sap-ewm/
source: SAP Blogs
date: 2023-01-06
fetch_date: 2025-10-04T03:09:36.090087
---

# Reason code and movement type in SAP EWM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Reason code and movement type in SAP EWM

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4732&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Reason code and movement type in SAP EWM](/t5/supply-chain-management-blog-posts-by-members/reason-code-and-movement-type-in-sap-ewm/ba-p/13560996)

![P887913](https://avatars.profile.sap.com/9/6/id96959b749dd996c53369030e201e1fd4bb4d20afaec21cbd65e929478d0cc2d8_small.jpeg "P887913")

[P887913](https://community.sap.com/t5/user/viewprofilepage/user-id/47014)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4732)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4732)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560996)

‎2023 Jan 05
7:43 PM

[9
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4732/tab/all-users "Click here to see who gave kudos to this post.")

29,615

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Basis](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Basis/pd-p/192798129450263425409096799593312)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)
* [EWM - Interfaces](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Interfaces/pd-p/828895203045710275663878834115743)
* [EWM - Radio Frequency](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Radio%2520Frequency/pd-p/382876162660666448662353059935346)
* [EWM - Shipping and Receiving](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Shipping%2520and%2520Receiving/pd-p/551700313515132864819929295213440)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Basis

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BBasis/pd-p/192798129450263425409096799593312)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)
* [EWM - Interfaces

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BInterfaces/pd-p/828895203045710275663878834115743)
* [EWM - Radio Frequency

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BRadio%2BFrequency/pd-p/382876162660666448662353059935346)
* [EWM - Shipping and Receiving

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BShipping%2Band%2BReceiving/pd-p/551700313515132864819929295213440)

View products (7)

Reason code and movement type in SAP EWM

Introduction-

Warehouse operation team, be it warehouse operator or warehouse supervisor executes warehouse internal business process such as scrapping of a damage pallet physical inventory or stock posting change in EWM. As this business transaction process completes in EWM system, relevant goods movements posting gets performed in ECC. Quite often it is ask from business to see the reason code in goods movement (material document) in ECC. The user can enter reason code for the warehouse movement in SAP EWM and it should reflect in ECC.

Although as per SAP documentations, it is not mandatory to enter a reason for movement in SAP EWM, however specific movement types in SAP ERP might require a reason for movement or responsible operational team might want to record the reason for certain movements for later analysis of why goods movement was posted.

In this blog, we will see the following scenario’s

* User enters reason for the goods movement in EWM and the same reason is reflected in goods movement document in ECC.

* User enters reason for the goods movement in EWM and goods movement document in ECC do not have reason.

**Configuration needed for these business scenario’s-**

* Define Reason for warehouse movements

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC1.png)

* Manage reason for goods movement

Reason Group-

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC2.png)

Reason for movement

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC3.png)

Map EWM Reason code to ERP Reason code

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC4.png)

Movement reason defined in the above screenshot should be same in Movement reason in ECC. Please refer following screenshot.

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC5.png)

Now let’s do testing for the business scenario’s

* User enters movement reason for the goods movement in EWM and the same reason is reflected in goods movement document in ECC.

User enters movement reason for ‘**Scrapping process’**

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC6.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC7.png)

Display goods movement document in EWM

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC8.png)

Display goods movement document in ECC

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC9.png)

* User enters movement reason for the goods movement in EWM and goods movement document in ECC do not have reason.

User enter movement reason for ‘**Posting change process’**

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC10.png)

Display goods movement document in EWM

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC11.png)

Display goods movement document in ECC

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC12.png)

Reason for movement is not getting appeared on Material document.

In order to map the reason from EWM, which is not maintained in ECC, we need to set up extra configurations in ECC (MM configuration) as below,

Let’s take example of movement type 322 here

Control: Reason for movement

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC13.png)

Reason for movement

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC14.png)

Map EWM Reason code to ECC reason for movement (EWM configuration)

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC15.png)

Again, testing for configuration for above scenario-

Posting change in EWM-

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC16.png)

Goods movement document in ECC-

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC17.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/PIC18.png)

Alternately, reason for movement can be maintained in EWM

BAdI /SCWM/EX\_ERP\_GOODSMVT\_EXT.

Method name /SCWM/IF\_EX\_ERP\_GOODSMVT~CHANGE\_MATDOC.

This blog is based on my personal test in S/4HANA 2021 release. I will appreciate your feedback/ comments for the same.

Thanks,

Shailesh Patil

* [ewm-basic](/t5/tag/ewm-bas...
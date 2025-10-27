---
title: Backflush of single order materials using synchronous goods movement
url: https://blogs.sap.com/2023/01/06/backflush-of-single-order-materials-using-synchronous-goods-movement/
source: SAP Blogs
date: 2023-01-07
fetch_date: 2025-10-04T03:15:03.674148
---

# Backflush of single order materials using synchronous goods movement

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Backflush of single order materials using synchron...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4790&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Backflush of single order materials using synchronous goods movement](/t5/supply-chain-management-blog-posts-by-members/backflush-of-single-order-materials-using-synchronous-goods-movement/ba-p/13563180)

![narsimha_namburi](https://avatars.profile.sap.com/9/d/id9d5557d6c55837dfd912b0099ec21a90b449299047adb5988fdedbd1346f46e1_small.jpeg "narsimha_namburi")

[narsimha\_namburi](https://community.sap.com/t5/user/viewprofilepage/user-id/559130)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4790)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4790)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563180)

‎2023 Jan 06
9:26 PM

[9
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4790/tab/all-users "Click here to see who gave kudos to this post.")

6,224

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Goods Movement](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Goods%2520Movement/pd-p/866234868597946653151414257432264)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Goods Movement

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BGoods%2BMovement/pd-p/866234868597946653151414257432264)

View products (2)

SAP continuously improvising the functionalities in EWM to simplify the processes in every new release. One such functionality is synchronous goods movements.

This blog explains the benefits of synchronous goods movements in production consumption for single order staging related components.

In older versions, if a material is treated as single order staging relevant component, consumption using backflush is not possible. The reason being, when the material is staged for PMR, stock will have reference of the PMR.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture1-2.png)

If we try to perform the production confirmation, consumption delivery will be created and distributed to EWM to perform the direct goods issue from PSA Bin.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture2-3.png)

Component consumption will fail even though stock available in PSA bin

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture3-2.png)

Enable synchronous movements at production scheduling profile

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture4-2.png)

After the synchronous movements are enabled if we try to process the COGI error, we can see the goods movement posted for the component.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture5-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture6.png)

Along with consumption of single order components, synchronous goods movements will also provide flexibility of not generating deliveries there by reducing back and forth communication between ERP & EWM.

Another benefit is the clarity of the error message. Before synchronous movements, we don’t have the proper visibility of the failures in COGI. But with synchronous movements, we can get the exact error information. This is same irrespective of staging method in EWM.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture7.png)

This functionality will work only with embedded EWM but not decentralized EWM.

PS: This is personal observation based on pain points in older versions and this blog is based on S4 HANA 2022 version.

Thank you for reading the post, please share thoughts and feedback.

Follw <https://community.sap.com/topics/extended-warehouse-management> for more content.

Follow Narsimha Namburi for more updates.

References

<http://help.sap.com>

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-members%2Fbackflush-of-single-order-materials-using-synchronous-goods-movement%2Fba-p%2F13563180%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP WM Public cloud storage bin Capacity check planning for putway.](/t5/supply-chain-management-q-a/sap-wm-public-cloud-storage-bin-capacity-check-planning-for-putway/qaq-p/14226191)
  in [Supply Chain Management Q&A](/t5/supply-chain-management-q-a/qa-p/scm-questions)  a week ago
* [How the capacity planning works in warehouse management (public cloud)?](/t5/supply-chain-management-q-a/how-the-capacity-planning-works-in-warehouse-management-public-cloud/qaq-p/14192184)
  in [Supply Chain Management Q&A](/t5/supply-chain-management-q-a/qa-p/scm-questions)  2025 Aug 26
* [HU based backflush from PSA using Synchronous Posting - BAdI /SCWM/EX\_EWM\_GI\_SORT\_STOCK](/t5/supply-chain-management-blog-posts-by-sap/hu-based-backflush-from-psa-using-synchronous-posting-badi-scwm-ex-ewm-gi/ba-p/14183260)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  2025 Aug 19
* [Building a Hybrid Landscape: Decentralized SAP EWM with S/4HANA Cloud Public Edition](/t5/supply-chain-management-blog-posts-by-members/building-a-hybrid-landscape-decentralized-sap-ewm-with-s-4hana-cloud-public/ba-p/14113490)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  2025 May 28
* [Single Order Staging in Adcanced Production Integration vs Backflush](/t5/supply-chain-management-q-a/single-order-staging-in-adcanced-production-integration-vs-backflush/qaq-p/14054369)
  in [Supply Chain Management Q&A](/t5/supply-chain-management-q-a/qa-p/scm-questions)  2025 Mar 24

Top kudoed authors

| User | Count |
| --- | --- |
| [![former_member8860](https://avatars.profile.sap.com/former_member_small.jpeg "former_member8860")  former\_member8860](/t5/user/viewprofilepage/user-id/8860) | 1 |
| [![Omar_Ossama](https://avatars.profile.sap.com/6/0/id60770dc14b33e6d35123a7bd2eaa3d06dbba849d4621ca8fc61220b1d4cbdcc7_small.jpeg "Omar_Ossama")  Omar\_Ossama](/t5/user/viewprofilepage/user-id/145202) | 1 |
| [![former_member788724](https://avatars.profile.sap.com/former_member_small.jpeg "former_member788724")  former\_member788724](/t5/user/viewprofilepage/user-id/788724) | 1 |
| [![Rahul_Gandi1](https://avatars.profile.sap.com/8/8/id88f3b6bb61a7ae49c61dc9fe258f8832a55ef6620c927ff171b95b71a8d75933_small.jpeg "Rahul_Gandi1")  Rahul\_Gandi1](/t5/user/viewprofilepage/user-id/1877178) | 1 |
| [![Sumit...
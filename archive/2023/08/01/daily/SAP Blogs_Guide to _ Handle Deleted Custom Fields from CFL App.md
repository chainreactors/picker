---
title: Guide to : Handle Deleted Custom Fields from CFL App
url: https://blogs.sap.com/2023/07/31/guide-to-handle-deleted-custom-fields-from-cfl-app/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T16:59:48.506433
---

# Guide to : Handle Deleted Custom Fields from CFL App

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Guide to : Handle Deleted Custom Fields from CFL A...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68413&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Guide to : Handle Deleted Custom Fields from CFL App](/t5/enterprise-resource-planning-blog-posts-by-members/guide-to-handle-deleted-custom-fields-from-cfl-app/ba-p/13568171)

![vrishtijain](https://avatars.profile.sap.com/6/c/id6cc96a5e13dd7f47c265849c324cbc84ae7772efcd0f9cd4c17129de9166d7f7_small.jpeg "vrishtijain")

[vrishtijain](https://community.sap.com/t5/user/viewprofilepage/user-id/421557)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68413)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68413)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568171)

‎2023 Jul 31
11:37 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68413/tab/all-users "Click here to see who gave kudos to this post.")

4,839

* SAP Managed Tags
* [SAP Fiori Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Cloud/pd-p/73554900100800000375)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori Cloud

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BCloud/pd-p/73554900100800000375)

View products (2)

**Problem Statement:** You created Custom fields in CFL APP and transported the same to next landscape. Then, you deleted the fields and created new. Ideally the deletion should get captured in the transport automatically but you see it is not captured. Once you move the transport to quality, you see new fields but the old fields still sitting in quality system although you deleted them from Development system.

**Solution:** This is relevant for S/4 HANA 2022 version as in earlier version this was not possible but now SAP has supported this feature. Either your changes will capture automatically in the transport (Depends upon settings in S\_ATO\_SETUP) . But if  you missed it and want to take up this manually ,please refer to below guide.

Goto Transaction "S\_ATO\_SUPPORT"

Click on "Show objects of Item"

![](/legacyfs/online/storage/blog_attachments/2023/07/download-7.png)

Then select check box "Include History"

Select Item type : CFDF (custom field)

Put your field name and execute.

![](/legacyfs/online/storage/blog_attachments/2023/07/download-8.png)

You will get list of R3TR entries. Copy all of them and add into the transport (Workbench) manually.

Now when you will move this transport to next landscape it will delete those unwanted fields and make your system consistence with dev box.

This will help to remove in-consistency from the system.

Thanks for reading the post. Happy learning.

* [cfl](/t5/tag/cfl/tg-p/board-id/erp-blog-members)
* [custom fields and logic](/t5/tag/custom%20fields%20and%20logic/tg-p/board-id/erp-blog-members)
* [SAP S4HANA 2022](/t5/tag/SAP%20S4HANA%202022/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fguide-to-handle-deleted-custom-fields-from-cfl-app%2Fba-p%2F13568171%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-s-4hana-public/ba-p/14234546)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Friday
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [Cannot Post Goods Receipt (Movement Type 101) against PO using released APIs in S/4HANA Cloud Public](/t5/enterprise-resource-planning-q-a/cannot-post-goods-receipt-movement-type-101-against-po-using-released-apis/qaq-p/14230305)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Monday
* [Cannot Post Goods Receipt (Movement Type 101) against PO using released APIs in S/4HANA Cloud Public](/t5/enterprise-resource-planning-q-a/cannot-post-goods-receipt-movement-type-101-against-po-using-released-apis/qaq-p/14230254)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [SAP MDG-M Custom UI Configuration Performance Comparison and Gains](/t5/enterprise-resource-planning-blog-posts-by-members/sap-mdg-m-custom-ui-configuration-performance-comparison-and-gains/ba-p/14209898)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![AhmetZ](https://avatars.profile.sap.com/9/b/id9bd18482b8f2b410b8d0206e72935dc3ca0fb940d648a21e9d1a809de3dd235c_small.jpeg "AhmetZ")  AhmetZ](/t5/user/viewprofilepage/user-id/1882423) | 2 |
| [![faisal_aslam12478](https://avatars.profile.sap.com/2/5/id256f07037a2e3a4963aba48ad71ecb6111b9605c9e426c58d4646eed5c8edd30_small.jpeg "faisal_aslam12478")  faisal\_aslam12478](/t5/user/viewprofilepage/user-id/826267) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d3f8232_small.jpeg "arghadipkar3013")  arghadipkar3013](/t5/user/viewprofilepage/user-id/686417) | 2 |
| [![vianshu](https://avatars.profile.sap.com/7/3/id73f851dd2d601f9bd347d78ecfa46602245b7e89d831c26845276966f760a654_small.jpeg "vianshu")  vianshu](/t5/user/viewprofilepage/user-id/19840) | 2 |
| [![neeraj_putluru](https://avatars.profile.sap.com/9/5/id9528d21dfd4f646e746f147661a0c73ef87e9d5e9abf3957566a2a761924642f_small.jpeg "neeraj_putluru")  neeraj\_putluru](/t5/user/viewprofi...
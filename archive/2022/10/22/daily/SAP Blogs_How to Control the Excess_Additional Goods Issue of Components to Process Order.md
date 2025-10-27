---
title: How to Control the Excess/Additional Goods Issue of Components to Process Order
url: https://blogs.sap.com/2022/10/21/how-to-control-the-excess-additional-goods-issue-of-components-to-process-order/
source: SAP Blogs
date: 2022-10-22
fetch_date: 2025-10-03T20:35:47.560145
---

# How to Control the Excess/Additional Goods Issue of Components to Process Order

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to Control the Excess/Additional Goods Issue o...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67181&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Control the Excess/Additional Goods Issue of Components to Process Order](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-control-the-excess-additional-goods-issue-of-components-to-process/ba-p/13552243)

![Raja_S_Reddy_B](https://avatars.profile.sap.com/7/a/id7a7408c1bcc4280b101e813570152a984b6b532ecbb279e3d67dd43128a5c4e1_small.jpeg "Raja_S_Reddy_B")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Raja\_S\_Reddy\_B](https://community.sap.com/t5/user/viewprofilepage/user-id/198700)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67181)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67181)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552243)

‎2022 Oct 21
6:21 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67181/tab/all-users "Click here to see who gave kudos to this post.")

3,781

* SAP Managed Tags
* [SAP Manufacturing Execution](https://community.sap.com/t5/c-khhcw49343/SAP%2520Manufacturing%2520Execution/pd-p/01200615320800000731)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)

* [SAP Manufacturing Execution

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BManufacturing%2BExecution/pd-p/01200615320800000731)
* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)

View products (2)

**Business Scenario:**During the Confirmation of the Process Order, which is activated with Backflush (Auto GI, during the confirmation), System is not allowing the Additional Good issues/increase the Component Quantity manually. Getting the Error message, when saving the Confirmation.

**Execution Steps as follws below****Create the Process Order using the T Code: COR1**In this Process Order, Components are activated with Backflush Indicator, which will enable automatic goods issue during the confirmation. The Component Quantities are 5 L for each of the component

![](/legacyfs/online/storage/blog_attachments/2022/10/1-77.png)**Release the Process Order using theT Code: COR2**

![](/legacyfs/online/storage/blog_attachments/2022/10/2-33.png)This order is in the Released & saved in the change mode.
**Confirm the Process Order using the T Code: COR6N**![](/legacyfs/online/storage/blog_attachments/2022/10/3-30.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/4-25.png)

During the confirmation, User is trying to add the additional goods issue (or) increasing the Component Quantity manually.
In the Goods movement tab>>Increasing the component Qty from 5 to 10 (more than 5)

 After manually Increasing Component Quantity, then Click on Save >> Getting the below Screen
![](/legacyfs/online/storage/blog_attachments/2022/10/5-27.png)

If we look at the Error details
System tis throwing the Error, for this additional Goods Issue, changed manually![](/legacyfs/online/storage/blog_attachments/2022/10/6-29.png)

**Root cause of this Error**
Look at the System Message control stetting in the Configuration using  T Code: OMCQ
**![](/legacyfs/online/storage/blog_attachments/2022/10/7-20.png)**

**Solution Proposed:**
If we change **Error message to Warning message**, (E to W) System will allow the Additional (or) Excess Goods issue of the Component Quantities manually, during the Confirmation.

Hope, this is of some Useful Info. Kindly update with your  Valuable Feedback/Comments/Inputs.
Thanks & Regards
Raja Sekhara Reddy Bannuru

7 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fhow-to-control-the-excess-additional-goods-issue-of-components-to-process%2Fba-p%2F13552243%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Int4 Suite Agents Empowers Functional Consultants To Test Integrated SAP S/4HANA Business Processes](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-agents-empowers-functional-consultants-to-test-integrated-sap-s/ba-p/14234100)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  3 hours ago
* [Table with customer contacts FSCM Process receivables](/t5/enterprise-resource-planning-q-a/table-with-customer-contacts-fscm-process-receivables/qaq-p/14234125)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  3 hours ago
* [MD01N Behavior: Issuing Storage Location Not Set in Stock Transport Requisitions](/t5/enterprise-resource-planning-q-a/md01n-behavior-issuing-storage-location-not-set-in-stock-transport/qaq-p/14234045)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  4 hours ago
* [Tax statement item missing for tax code V0 in intercompany billing VF02](/t5/enterprise-resource-planning-q-a/tax-statement-item-missing-for-tax-code-v0-in-intercompany-billing-vf02/qaq-p/14234014)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  5 hours ago
* [How to trigger HU label print in S/4HANA Cloud Public Edition (API\_FORM\_PRINT\_SRV not available)](/t5/enterprise-resource-planning-q-a/how-to-trigger-hu-label-print-in-s-4hana-cloud-public-edition-api-form/qaq-p/14233989)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  6 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![former_member816598](https://avatars.profile.sap.com/former_member_small.jpeg "former_member816598")  former\_member816598](/t5/user/viewprofilepage/user-id/816598) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d3f8...
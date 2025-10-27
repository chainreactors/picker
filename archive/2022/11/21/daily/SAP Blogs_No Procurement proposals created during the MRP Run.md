---
title: No Procurement proposals created during the MRP Run
url: https://blogs.sap.com/2022/11/20/no-procurement-proposals-created-during-the-mrp-run/
source: SAP Blogs
date: 2022-11-21
fetch_date: 2025-10-03T23:19:19.145567
---

# No Procurement proposals created during the MRP Run

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* No Procurement proposals created during the MRP Ru...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67228&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [No Procurement proposals created during the MRP Run](/t5/enterprise-resource-planning-blog-posts-by-members/no-procurement-proposals-created-during-the-mrp-run/ba-p/13552694)

![Raja_S_Reddy_B](https://avatars.profile.sap.com/7/a/id7a7408c1bcc4280b101e813570152a984b6b532ecbb279e3d67dd43128a5c4e1_small.jpeg "Raja_S_Reddy_B")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Raja\_S\_Reddy\_B](https://community.sap.com/t5/user/viewprofilepage/user-id/198700)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67228)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67228)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552694)

‎2022 Nov 20
4:31 AM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67228/tab/all-users "Click here to see who gave kudos to this post.")

3,832

* SAP Managed Tags
* [SAP Manufacturing Execution](https://community.sap.com/t5/c-khhcw49343/SAP%2520Manufacturing%2520Execution/pd-p/01200615320800000731)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)

* [SAP Manufacturing Execution

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BManufacturing%2BExecution/pd-p/01200615320800000731)
* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)

View products (2)

**This is the Most commonly faced/reported issue during MRP run
Issue Reported**
During the MRP run, System not creating any Procurement proposals and getting the message “No procurement proposals changed” even though there is a clear requirement.
**More details of the issue:**
Current requirements are reflecting in MD04 Screen (PIRs of quantities 1000,2000,3000). for the Material : FERT4, in the Plant 1710

![](/legacyfs/online/storage/blog_attachments/2022/11/Pic-2.jpg)

Now if we run the MRP through MD02 transaction we can observe that
![](/legacyfs/online/storage/blog_attachments/2022/11/pic-3-1.jpg)

**Analysis Done:**
Based on the quick analysis for this reported issue, Checked the Results of the last MRP run, using MD05 transaction (MRP list).
![](/legacyfs/online/storage/blog_attachments/2022/11/pic-4-1.jpg)

**Root Cause of the Issue**
From this we can understand the issue with the exceeding maximum number of proposals that can be created. this happens when the number of procurement proposals are more than the Maximum number of order proposals that were maintained in the Configuration (T Code: OPPQ: Plant Parameters >> Error Handling)
**Solution Proposed:**To resolve this issue, there are two possible solutions
1. By Change/ increasing the Lot size, so that no. of proposals should not exceed 50, as per the curent config. setting
2. Increase the Max. No of Proposal limit to more than 50, at the config.
![](/legacyfs/online/storage/blog_attachments/2022/11/Pic5.jpg)

If we have constraints in changing lot sizing procedures or increasing lot size then we can change the maximum number of proposals in configuration by using OPPQ transaction
![](/legacyfs/online/storage/blog_attachments/2022/11/Pic6-2.jpg)

In the Error Handling option, we can increase the maximum number of proposals to the required number.
In this case, we changed the Lot Size, from 10 to 100 & Executed the MRP again![](/legacyfs/online/storage/blog_attachments/2022/11/Pic7.jpg)

MRP Run executed successfully
![](/legacyfs/online/storage/blog_attachments/2022/11/pic8.jpg)

**Conclusion:** Issue got resolved, by increasing the Lot Size, to avoid the maximum no. of proposals limit set at the configuration
Shae your valuable feedback/comments, if any
Thanks & Regards : Raja Sekhara Reddy Bannuru

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fno-procurement-proposals-created-during-the-mrp-run%2Fba-p%2F13552694%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [Why asset doest not have material code in SAP ERP?](/t5/enterprise-resource-planning-q-a/why-asset-doest-not-have-material-code-in-sap-erp/qaq-p/14231693)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Tuesday
* [Sales\_Q&A - Bulgaria EUR Transition for S/4HANA Cloud Public Cloud Live Customers](/t5/enterprise-resource-planning-blog-posts-by-sap/sales-q-amp-a-bulgaria-eur-transition-for-s-4hana-cloud-public-cloud-live/ba-p/14230125)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday
* [How to force planning of semi-finished goods in MRP planning, regardless of available Stock](/t5/enterprise-resource-planning-q-a/how-to-force-planning-of-semi-finished-goods-in-mrp-planning-regardless-of/qaq-p/14226914)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [Lean Service Procurement for Project Network in SAP S/4 Hana](/t5/enterprise-resource-planning-blog-posts-by-members/lean-service-procurement-for-project-network-in-sap-s-4-hana/ba-p/14217832)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  3 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![former_member816598](https://avatars.profile.sap.com/former_member_small.jpeg "former_member816598")  former\_member816598](/t5/us...
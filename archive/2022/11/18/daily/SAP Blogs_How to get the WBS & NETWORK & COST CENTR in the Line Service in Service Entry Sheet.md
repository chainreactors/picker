---
title: How to get the WBS & NETWORK & COST CENTR in the Line Service in Service Entry Sheet
url: https://blogs.sap.com/2022/11/17/how-to-get-the-wbs-network-cost-centr-in-the-line-service-in-service-entry-sheet/
source: SAP Blogs
date: 2022-11-18
fetch_date: 2025-10-03T23:06:18.502894
---

# How to get the WBS & NETWORK & COST CENTR in the Line Service in Service Entry Sheet

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to get the WBS & NETWORK & COST CENTR in the L...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68372&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to get the WBS & NETWORK & COST CENTR in the Line Service in Service Entry Sheet](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-get-the-wbs-network-cost-centr-in-the-line-service-in-service-entry/ba-p/13567335)

![OsamaHussein](https://avatars.profile.sap.com/a/9/ida9098d79ad5a552dd93c19168b70afd6f5b79c7ef862a725fcc862ac58c70340_small.jpeg "OsamaHussein")

[OsamaHussein](https://community.sap.com/t5/user/viewprofilepage/user-id/157444)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68372)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68372)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567335)

‎2022 Nov 17
7:28 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68372/tab/all-users "Click here to see who gave kudos to this post.")

2,568

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)

View products (2)

In this Blog we will show how we can get the Account Assignment (WBS & Network & Cost Center) for each item in the Service Entry Sheet .

We will use different tables to get the account assignment (ESSR – ESLL – ESKL – ESKN)

Service Entry Sheet Number is 1000000738

Use the Service Entry Sheet Number to get the Package Number

– Go to the ESSR Table and put the Entry Sheet Number 1000000738 in the LBLNI Field and Execute
![](/legacyfs/online/storage/blog_attachments/2022/11/Capture1-2.png)

Figure 1: You will find the Package number in PACKNO Field 9167
![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-09-174043.png)
Figure 2: We will take the Package Number 9167 and go to the ESLL Table in PACKNO Field

![](/legacyfs/online/storage/blog_attachments/2022/11/Capture2.png)
Figure 3: Then we will take the value in the SUB\_PACKNO Field and go back to the selection of ESLL Table and put the value that we has token from SUB\_PACKNO Field to the PACKNO Field

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-09-183254.png)
![](/legacyfs/online/storage/blog_attachments/2022/11/Capture3.png)
![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-09-183856.png)
Figure 4: Now we can see the Line of service item in the Service Entry Sheet then we will take the all value in the INTROW field 2 ، 3 and go to the ESKL Table

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-09-184530.png)
Figure 5: We will Put the value in the INTROW field 2 ، 3 and the Package Number 9168 in the PACKNO Field

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-09-190346.png)
Figure 6: After Execute we will copy all the Value of the Seq.No.Acc Assgt (ZEKKN) Field then go to the ESKN Table

![](/legacyfs/online/storage/blog_attachments/2022/11/Capture4.png)
Figure 7: We will put the value that we have token from ESKL – ZEKKN (1 ، 2) Into ESKN – ZEKKN and Service Entry Sheet Number into PECKNO and Execute

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-09-203405-1.png)
Figure 8: Now we can see all the Account Assignment Data for each Service item in the Service Entry Sheet

* At the end hope to give your feedback in the comments and if you have any questions put it in the comments

* Please follow my profile for future posts click osamakhoder

* For More Blogs on SAP S/4HANA, click [here](https://blogs.sap.com/tags/73554900100800000266/)

* For More Blogs on MM (Material Management) click [here](https://blogs.sap.com/tags/477297786799213261950044802925335/)

# **THANKS**

Osama Hussein

SAP MM / WM Consultant

* [MM (Material Management)](/t5/tag/MM%20%28Material%20Management%29/tg-p/board-id/erp-blog-members)
* [sap s4hana](/t5/tag/sap%20s4hana/tg-p/board-id/erp-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fhow-to-get-the-wbs-network-cost-centr-in-the-line-service-in-service-entry%2Fba-p%2F13567335%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Goods issue not available in Service and Asset Manager Demo Version - Inventory Clerk](/t5/enterprise-resource-planning-q-a/goods-issue-not-available-in-service-and-asset-manager-demo-version/qaq-p/14234330)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 hours ago
* [Max line items in service contract in public cloud 2508](/t5/enterprise-resource-planning-q-a/max-line-items-in-service-contract-in-public-cloud-2508/qaq-p/14233931)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  10 hours ago
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [AI-assisted scoping and configuration services (CBC AIX) are activated by an AI unit contract](/t5/enterprise-resource-planning-q-a/ai-assisted-scoping-and-configuration-services-cbc-aix-are-activated-by-an/qaq-p/14232958)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday
* [Van stock visibility without using storage locations](/t5/enterprise-resource-planning-q-a/van-stock-visibility-without-using-storage-locations/qaq-p/14232928)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB6969...
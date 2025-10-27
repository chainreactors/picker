---
title: Post automatically general ledgers adjustments method
url: https://blogs.sap.com/2023/08/25/post-automatically-general-ledgers-adjustments-method/
source: SAP Blogs
date: 2023-08-26
fetch_date: 2025-10-04T12:00:03.612210
---

# Post automatically general ledgers adjustments method

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Post automatically general ledgers adjustments met...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68601&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Post automatically general ledgers adjustments method](/t5/enterprise-resource-planning-blog-posts-by-members/post-automatically-general-ledgers-adjustments-method/ba-p/13571754)

![ESAITEJA](https://avatars.profile.sap.com/4/4/id44c5dcb0759916027d4425b9efde885bff9c461e806bb57fbb9dcacc5b41dda3_small.jpeg "ESAITEJA")

[ESAITEJA](https://community.sap.com/t5/user/viewprofilepage/user-id/126657)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68601)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68601)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571754)

‎2023 Aug 25
9:15 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68601/tab/all-users "Click here to see who gave kudos to this post.")

1,601

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN General Ledger](https://community.sap.com/t5/c-khhcw49343/FIN%2520General%2520Ledger/pd-p/141573396494884189617506284133567)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN General Ledger

  Software Product Function](/t5/c-khhcw49343/FIN%2BGeneral%2BLedger/pd-p/141573396494884189617506284133567)

View products (4)

**Introduction**

At the time of inventory auditing, inventory general ledgers adjusted manually. Here inventory general ledger master without untick post automatically option system not allow the manual transactions.

The exception has been made for the accounts specified for the valuation postings when it comes to the 'Post Automatically Only' flag so that manual adjustments can be made to the valuation adjustment accounts via FBB1.

In this level it is possible to manually post to these accounts even though the XINTB (Post automatically only) flag has been set in the master record.

**How to works post automatically without untick**

![](/legacyfs/online/storage/blog_attachments/2023/08/gl-capture-1.png)

Transaction FBB1 is explicitly excluded from the check **XINTB (Post automatically only)** you can also identify in source code at (MF05AFB0\_BSCHL\_KONTO\_BEARBEITU)

**Go to FBB1 Transaction code**

![](/legacyfs/online/storage/blog_attachments/2023/08/png-2.png)

Check the report level for example  FBL3N

![](/legacyfs/online/storage/blog_attachments/2023/08/png-3.png)

**Conclusion**

FBB1 Transaction very helpful Accounting people. This type of transactions not disturb MM integration point of view.

* [fico](/t5/tag/fico/tg-p/board-id/erp-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fpost-automatically-general-ledgers-adjustments-method%2Fba-p%2F13571754%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Supply Chain Management in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/supply-chain-management-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14214877)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [Date Constraints in SAP Project and Resource Management](/t5/enterprise-resource-planning-blog-posts-by-sap/date-constraints-in-sap-project-and-resource-management/ba-p/14213305)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago
* [SAP Fiori for SAP S/4HANA – Adding a GUI transaction to the launchpad in SAP S/4HANA 2023 or higher](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-fiori-for-sap-s-4hana-adding-a-gui-transaction-to-the-launchpad-in-sap/ba-p/14207175)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  a month ago
* [ATP vs Advanced ATP in SAP S/4HANA Cloud Private edition 2023](/t5/enterprise-resource-planning-blog-posts-by-sap/atp-vs-advanced-atp-in-sap-s-4hana-cloud-private-edition-2023/ba-p/14192587)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Sep 01
* [How to Prepare for SAP S/4 HANA Private Edition Certification (with Sample Questions)](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-prepare-for-sap-s-4-hana-private-edition-certification-with-sample/ba-p/14197612)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  2025 Aug 29

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![faisal_aslam12478](https://avatars.profile.sap.com/2/5/id256f07037a2e3a4963aba48ad71ecb6111b9605c9e426c58d4646eed5c8edd30_small.jpeg "faisal_aslam12478")  faisal\_aslam12478](/t5/user/viewprofilepage/user-id/826267) | 2 |
| [![AhmetZ](https://avatars.profile.sap.com/9/b/id9bd18482b8f2b410b8d0206e72935dc3ca0fb940d648a21e9d1a809de3dd235c_small.jpeg "AhmetZ")  AhmetZ](/t5/user/viewprofilepage/user-id/1882423) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d3f8232_small.jpeg "arghadipkar3013")  arghadipkar3013](/t5/user/viewprofilepage/user-id/686417) | 2 |
| [![vianshu](https://avatars.profile.sap.com/7/3/id73f851dd2d601f9bd347d78ecfa46602245b7e89d831c26845276966f760a654_small.jpeg "vianshu")  vianshu](/t5/user/viewprofilepage/user-id/19840) |...
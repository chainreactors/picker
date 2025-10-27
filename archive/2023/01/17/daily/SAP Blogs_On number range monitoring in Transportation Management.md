---
title: On number range monitoring in Transportation Management
url: https://blogs.sap.com/2023/01/16/on-number-range-monitoring-in-transportation-management/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:47.818510
---

# On number range monitoring in Transportation Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* On number range monitoring in Transportation Manag...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/5070&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [On number range monitoring in Transportation Management](/t5/supply-chain-management-blog-posts-by-sap/on-number-range-monitoring-in-transportation-management/ba-p/13567184)

![bernd_dittrich](https://avatars.profile.sap.com/3/a/id3a8adee9a04c0a57954e3eed25fb0646e388d321051846113d1d68872611ba0a_small.jpeg "bernd_dittrich")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[bernd\_dittrich](https://community.sap.com/t5/user/viewprofilepage/user-id/182222)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=5070)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/5070)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567184)

‎2023 Jan 16
12:19 PM

[3
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/5070/tab/all-users "Click here to see who gave kudos to this post.")

1,254

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)

* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

TM transactional documents do have numbers, which are typically drawn from an internal number range. This number range is finite, and the status should be monitored.

This [note](https://launchpad.support.sap.com/#/notes/2292041) describes how to monitor the current status using the report RSNUMHOT.

**Important:** As most other SAP number ranges, the TM number ranges are defined as rolling, meaning, that this needs to be considered in the selection. BTW: Rolling means, that the number range starts again with the start number, once the last number from the numberrange is consumed. As we do check for duplicate numbers, the old documents  must have been archived, when the Rolling applies.

But of course, all of this should rarely be relevant for you. The number range should be defined large enough for the expected usage!

Labels

* [Technology Updates](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap/label-name/technology%20updates)

* [Number range](/t5/tag/Number%20range/tg-p/board-id/scm-blog-sap)
* [Number range alert](/t5/tag/Number%20range%20alert/tg-p/board-id/scm-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-sap%2Fon-number-range-monitoring-in-transportation-management%2Fba-p%2F13567184%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Advanced Intercompany Sales in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/advanced-intercompany-sales-in-sap-s-4hana/ba-p/14234227)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  9 hours ago
* [What's New in SAP Asset Performance Management 2509](/t5/supply-chain-management-blog-posts-by-sap/what-s-new-in-sap-asset-performance-management-2509/ba-p/14229539)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  Tuesday
* [How SAP Intelligent Asset Management helps companies comply with ISO 55001](/t5/supply-chain-management-blog-posts-by-sap/how-sap-intelligent-asset-management-helps-companies-comply-with-iso-55001/ba-p/14228660)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  Tuesday
* [Logistics at Supply Chain Connect, 6-8 October 2025, Las Vegas](/t5/supply-chain-management-blog-posts-by-sap/logistics-at-supply-chain-connect-6-8-october-2025-las-vegas/ba-p/14227184)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  a week ago
* [A Comprehensive Guide to SAP S/4HANA Extended Warehouse Management (EWM)](/t5/supply-chain-management-blog-posts-by-members/a-comprehensive-guide-to-sap-s-4hana-extended-warehouse-management-ewm/ba-p/14225196)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![kate_dowle](https://avatars.profile.sap.com/f/c/idfc854da326a06cca0f63ca5fb0dcea757a20811766bb7013ac3a93ea3692ddd7_small.jpeg "kate_dowle")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") kate\_dowle](/t5/user/viewprofilepage/user-id/604799) | 5 |
| [![Danisosa](https://avatars.profile.sap.com/1/b/id1bb8819edb98e458340e58d0d00efcb6fa3054da6548bd2490d5f730e4aef9c2_small.jpeg "Danisosa")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Danisosa](/t5/user/viewprofilepage/user-id/2049459) | 4 |
| [![guglanigaurav198768](https://avatars.profile.sap.com/2/f/id2f94def7e6a391e4c857ba615aa6bfe1a522be65ebefa67dcef6ea45e1e6789c_small.jpeg "guglanigaurav198768")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") guglanigaurav198768](/t5/user/viewprofilepage/user-id/821128) | 3 |
| [![DzmitryCharniakevich](https://avatars.profile.sap.com/f/4/idf42b01a57aeb80f42b8efa79093a2c033db2940289071e293e7f5cab26d79207_small.jpeg "DzmitryCharniakevich")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") DzmitryCharniakevich](/t5/user/viewprofilepage/user-id/1946942) | 2 |
| [![Holger_Wittmer](https://avatars.profile.sap.com/d/2/idd22a7385812477a8833c6928b0fbf69bbfa0e8c13077bd4bd6a58d707b4927a2_small.jpeg "Holger_Wittmer")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") Holger\_Wittmer](/t5/user/viewprofilepage/user-id/46980) | 2 |
| [![rafael_brustolin1](https://avatars.profile.sap.com/0/f/id0f1752ac4a22d676538536793812683e88c7043b10013c852e4b1b408b1fbd2a_small.jpeg "rafael_brustolin1")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") rafael\_brustolin1](/t5/user/viewprofilepage/user-id/625271) | 1 |
| [![ManoelCosta](https://avatars.profile.sap.com/...
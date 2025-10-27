---
title: Core hybrid Replication: Generation of different CP ID in case of Mutiple Employments.
url: https://blogs.sap.com/2023/08/11/core-hybrid-replication-generation-of-different-cp-id-in-case-of-mutiple-employments./
source: SAP Blogs
date: 2023-08-12
fetch_date: 2025-10-04T12:01:33.140308
---

# Core hybrid Replication: Generation of different CP ID in case of Mutiple Employments.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Core hybrid Replication: Generation of different C...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164970&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Core hybrid Replication: Generation of different CP ID in case of Mutiple Employments.](/t5/technology-blog-posts-by-members/core-hybrid-replication-generation-of-different-cp-id-in-case-of-mutiple/ba-p/13578296)

![PrakashB](https://avatars.profile.sap.com/d/2/idd2d9c2961aa5446e5a35ca774797714a77ad4558ed8cb4951b2a227f9487cd93_small.jpeg "PrakashB")

[PrakashB](https://community.sap.com/t5/user/viewprofilepage/user-id/54682)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164970)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164970)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13578296)

‎2023 Aug 11
1:07 PM

0
Kudos

501

* SAP Managed Tags
* [SAP Integration Strategy](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Strategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)

* [SAP Integration Strategy

  Topic](/t5/c-khhcw49343/SAP%2BIntegration%2BStrategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)

View products (1)

In SAP Standard Core Hybrid Employee Master data replication Same CP will be generated in case of Multiple Employments. If same CP generated for different Employments and you're not using concurrent employment and Global assignments in SAP HCM, then it will create an issue in core hybrid replication while replicating Employee master data from SF EC to SAP HCM with an error "*Online maintenance is locked in payroll area*" as per SAP note <https://me.sap.com/notes/2697589> This is a Standard SAP behavior.

![](/legacyfs/online/storage/blog_attachments/2023/08/Locked-message.png)

Message in Employee Replication

To Overcome the above issue, we have Implement below mentioned implicit enhancement to allow the system to generate different CP ID in case of Mutiple employments scenario.

![](/legacyfs/online/storage/blog_attachments/2023/08/Enhancement.png)

Implicit enhancement

Please ensure you have mapped user ID to CP in Map External CP BADI as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/08/Map-External-CP-BADI.png)

Map External CP BADI

Now Employee master data replication will generate different CP ID for each employment.

Please share your feedback with us in comments.

the SAP Integration Strategy environment Topic page: <https://community.sap.com/topics/integration-strategy>,

post and answer questions: <https://answers.sap.com/tags/e26e2f63-fcc1-42a7-af06-decec0762b90>

* [SAP Core Hybrid](/t5/tag/SAP%20Core%20Hybrid/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcore-hybrid-replication-generation-of-different-cp-id-in-case-of-mutiple%2Fba-p%2F13578296%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [What’s New in SAP HANA Cloud – September 2025](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-hana-cloud-september-2025/ba-p/14228564)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [Top Reasons to Modernize with SAP HANA Cloud – Blog #4 in the Series](/t5/technology-blog-posts-by-sap/top-reasons-to-modernize-with-sap-hana-cloud-blog-4-in-the-series/ba-p/14206255)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [Building Enterprise Ready Data Products with SAP Business Data Cloud](/t5/technology-blog-posts-by-members/building-enterprise-ready-data-products-with-sap-business-data-cloud/ba-p/14223082)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [Generation of Sybase and Replication Server licenses due to server changed](/t5/technology-q-a/generation-of-sybase-and-replication-server-licenses-due-to-server-changed/qaq-p/14213855)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  3 weeks ago
* [Top Reasons to Modernize with SAP HANA Cloud – Blog #2 in the Series](/t5/technology-blog-posts-by-sap/top-reasons-to-modernize-with-sap-hana-cloud-blog-2-in-the-series/ba-p/14206244)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  3 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 5 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f718f5dd57231fae9_small.jpeg "smarchesini")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") smarchesini](/t5/user/viewprofilepage/user-id/125739) | 3 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/user/viewprofilepage/user-id/1557162) | 3 |
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b60703442ad43de8fe0e22782d75a73afb_small.jpeg "dylan-drummond")  dylan-drummond](/t5/user/viewprofilepage/user-id/197587) | 3 |
| [![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d875310cb4cfc1b63341690484fa5a6c39220ef7d6ff0f1de992d174_small.jpeg "Sharathmg")  Sharathmg](/t5/user/viewprofilepage/user-id/174516) | 2 |
| [![sushilgupta857](https://avatars.profile.sap.com/d/8/idd870f8b6a822e869da88c28c1ee253fe14335fdd6eaee1cb950742dc89d4a304_small.jpeg "sushilgupta857"...
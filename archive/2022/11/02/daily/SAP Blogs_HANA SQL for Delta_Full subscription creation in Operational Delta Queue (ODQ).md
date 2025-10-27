---
title: HANA SQL for Delta/Full subscription creation in Operational Delta Queue (ODQ)
url: https://blogs.sap.com/2022/11/01/hana-sql-for-delta-full-subscription-creation-in-operational-delta-queue-odq/
source: SAP Blogs
date: 2022-11-02
fetch_date: 2025-10-03T21:31:46.511372
---

# HANA SQL for Delta/Full subscription creation in Operational Delta Queue (ODQ)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* HANA SQL for Delta/Full subscription creation in O...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161824&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HANA SQL for Delta/Full subscription creation in Operational Delta Queue (ODQ)](/t5/technology-blog-posts-by-members/hana-sql-for-delta-full-subscription-creation-in-operational-delta-queue/ba-p/13560091)

![Subhendu](https://avatars.profile.sap.com/7/7/id777365d8c270e133bcc43ef3c4c14e8920bf9602ba8729e439c4edb88df6a54a_small.jpeg "Subhendu")

[Subhendu](https://community.sap.com/t5/user/viewprofilepage/user-id/13399)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161824)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161824)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560091)

‎2022 Nov 01
6:30 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161824/tab/all-users "Click here to see who gave kudos to this post.")

1,593

* SAP Managed Tags
* [SQL](https://community.sap.com/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)
* [BW Content and Extractors](https://community.sap.com/t5/c-khhcw49343/BW%2520Content%2520and%2520Extractors/pd-p/144344546671011469492893748922901)

* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)
* [BW Content and Extractors

  Software Product Function](/t5/c-khhcw49343/BW%2BContent%2Band%2BExtractors/pd-p/144344546671011469492893748922901)
* [SQL

  Programming Tool](/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)

View products (3)

Recently I have been working on a POC in HANA Cloud & S/4HANA for one of the product client, I got an opportunity to explore this new feature of SDI flowgraph and I like to share few interesting information on the same.

The conventional way to create a subscription is navigating to the Data Source of a SAP HANA SDI Flowgraph and then clicking on Custom Parameter option then providing the Extraction name.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture1-1.png)

Now as an alternate approach of the above step we can write a HANA SQL statement for that like below

*select count(\*) from "ZEXI\_S4H\_ADRC" T*

*with dataprovisioning parameters*

*('<PropertyGroup name="\_\_DP\_TABLE\_OPTIONS\_\_">*

*<PropertyGroup name="T">*

*<PropertyEntry name="extractionmode">D</PropertyEntry>*

*<PropertyEntry name="extractionname">ADRC</PropertyEntry>*

*</PropertyGroup>*

*</PropertyGroup>');*

![](/legacyfs/online/storage/blog_attachments/2022/11/SQL-Query.png)

SQL Query

Here extractionmode can be D (Delta) or F (Full).

Once we execute the query above it will create a subscription in ODQMON.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture2-2.png)

ODQMON subscription

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhana-sql-for-delta-full-subscription-creation-in-operational-delta-queue%2Fba-p%2F13560091%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  23m ago
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  54m ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/user/viewprofilepage/user-id/1557162) | 3 |
| [![MioYasutake](https://avatars.profile.sap.com/5/e/id5e79c604027d7add255f696da403a5a6dc6fa0244486f41819b07572e8c1330c_small.jpeg "MioYasutake")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") MioYasutake](/t5/user/viewprofilepage/user-id/789) | 3 |
| [![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d875310cb4cfc1b63341690484fa5a6c39220ef7d6ff0f1de992d174_small.jpeg "Sharathmg")  Sharathmg](/t5/user/viewprofilepage/user-id/174516) | 3 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 3 |
| [![dylan-dr...
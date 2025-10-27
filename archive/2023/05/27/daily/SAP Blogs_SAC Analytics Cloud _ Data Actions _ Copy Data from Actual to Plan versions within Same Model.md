---
title: SAC Analytics Cloud : Data Actions : Copy Data from Actual to Plan versions within Same Model
url: https://blogs.sap.com/2023/05/26/sac-analytics-cloud-data-actions-copy-data-from-actual-to-plan-versions-within-same-model/
source: SAP Blogs
date: 2023-05-27
fetch_date: 2025-10-04T11:39:52.202648
---

# SAC Analytics Cloud : Data Actions : Copy Data from Actual to Plan versions within Same Model

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAC Analytics Cloud : Data Actions : Copy Data fro...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162922&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAC Analytics Cloud : Data Actions : Copy Data from Actual to Plan versions within Same Model](/t5/technology-blog-posts-by-members/sac-analytics-cloud-data-actions-copy-data-from-actual-to-plan-versions/ba-p/13566583)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162922)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162922)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566583)

‎2023 May 26
6:09 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162922/tab/all-users "Click here to see who gave kudos to this post.")

3,644

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)

View products (1)

In this session I will discuss about the Data Actions which will copy  sates from Actual to Plan versions within Same Model for 2024.

**Data Action** : It is a set of action or operations like Copy, Allocation and copying data from one model to another etc. to manipulate data within model , same version or cross version. For example, we can copy a sales data version from to a financial model version based on some mapping.

In this sections we will discuss about a data action for Cross Model Copy operation from Sales to Financial Modeler version.

**Step 1 :**  The Copy from Sales Plan Version which we created in earlier blogs has the below fields (), But this time we will generate the Plan sales version using Actual Sales Version using data action –

**A. Create Data action :**

![](/legacyfs/online/storage/blog_attachments/2023/05/DACOPY.png)

**B.** Create a data Action to Copy to Actual Sales Version to Plan version.

![](/legacyfs/online/storage/blog_attachments/2023/05/DA2.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/DA1.png)

**C.** While copying we have not copied the same value to Plan version , we added a formula with a factor and created the Plan version value which used a multiplication factor . While we trigger Data Action the multiplication factor we will provide as input and the generate the output plan value.

![](/legacyfs/online/storage/blog_attachments/2023/05/Formula.png)

**D.** Create a Data action trigger button and add the Data Action and execute it . Plan version data will be copied.

![](/legacyfs/online/storage/blog_attachments/2023/05/Data-Trigger.png)

**E.** If you hit the Button “**Copy Sales Actual to Plan**” the data will be copied to plan by multiplying with the factor as copped by the screenshot. We can schedule the Copy operation data action via the calendar which we will do latter as a planning automation exercise.

Hope This will help.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsac-analytics-cloud-data-actions-copy-data-from-actual-to-plan-versions%2Fba-p%2F13566583%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [From REST to Datasphere: A CAP-based Integration Approach](/t5/technology-blog-posts-by-members/from-rest-to-datasphere-a-cap-based-integration-approach/ba-p/14218922)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Choosing the Right SAP Analytics Tool: Features, Benefits, and Strategy](/t5/technology-blog-posts-by-sap/choosing-the-right-sap-analytics-tool-features-benefits-and-strategy/ba-p/14230016)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f718f5dd57231fae9_small.jpeg "smarchesini")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") smarchesini](/t5/user/viewprofilepage/user-id/125739) | 3 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/user/viewprofilepage/user-id/1557162) | 3 |
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b...
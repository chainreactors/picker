---
title: Building an override from a lookup table with 0 as an accepted value
url: https://blogs.sap.com/2023/03/11/building-an-override-from-a-lookup-table-with-0-as-an-accepted-value/
source: SAP Blogs
date: 2023-03-12
fetch_date: 2025-10-04T09:21:59.454465
---

# Building an override from a lookup table with 0 as an accepted value

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Building an override from a lookup table with 0 as...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/6347&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Building an override from a lookup table with 0 as an accepted value](/t5/human-capital-management-blog-posts-by-sap/building-an-override-from-a-lookup-table-with-0-as-an-accepted-value/ba-p/13570081)

![xavierlegarrec](https://avatars.profile.sap.com/e/1/ide191ffbd1506acbea27fa713f7d40cc166155c1a67fd472acb8c46fa0863e44a_small.jpeg "xavierlegarrec")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[xavierlegarrec](https://community.sap.com/t5/user/viewprofilepage/user-id/20879)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=6347)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/6347)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570081)

‎2023 Mar 11
12:01 AM

[8
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/6347/tab/all-users "Click here to see who gave kudos to this post.")

1,338

* SAP Managed Tags
* [SAP SuccessFactors Compensation](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Compensation/pd-p/73555000100800000771)

* [SAP SuccessFactors Compensation

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BCompensation/pd-p/73555000100800000771)

View products (1)

**Introduction**

When building override options for customers in Variable Pay or Compensation it is better to build them through lookup tables or MDF objects so that in case worksheets get deleted and relaunched Comp Admin doesn't lose any data already entered on screen.

**Solution**

In this particular business case we look at how to build an override section where 0 is an accepted value which was harder to build than I first thought due to system limitations when building formulas referencing other fields calling lookup tables in them.

<https://youtu.be/tTN9SnoHCGQ>

--

All the best,

Xavier

*(If you found this blog useful please consider giving it a Like)*

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [Compensation](/t5/tag/Compensation/tg-p/board-id/hcm-blog-sap)
* [override](/t5/tag/override/tg-p/board-id/hcm-blog-sap)
* [override compensation](/t5/tag/override%20compensation/tg-p/board-id/hcm-blog-sap)
* [override from lookup](/t5/tag/override%20from%20lookup/tg-p/board-id/hcm-blog-sap)
* [override variable pay](/t5/tag/override%20variable%20pay/tg-p/board-id/hcm-blog-sap)
* [Variable Pay](/t5/tag/Variable%20Pay/tg-p/board-id/hcm-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fbuilding-an-override-from-a-lookup-table-with-0-as-an-accepted-value%2Fba-p%2F13570081%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Navigating Saudi Arabia’s Data Protection Framework: Part 2 – Personal Data Protection Law (PDPL)](/t5/human-capital-management-blog-posts-by-sap/navigating-saudi-arabia-s-data-protection-framework-part-2-personal-data/ba-p/13876105)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  2024 Sep 24
* [Job Application Field Overrides](/t5/human-capital-management-q-a/job-application-field-overrides/qaq-p/13851195)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2024 Sep 02
* [Demystifying SAP SuccessFactors Suite Abbreviations and Terms for New Users](/t5/human-capital-management-blog-posts-by-members/demystifying-sap-successfactors-suite-abbreviations-and-terms-for-new-users/ba-p/13630504)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2024 Mar 11
* [Elevating Internal Transfers Transitions through SAP SuccessFactors Onboarding for Internal Hires](/t5/human-capital-management-blog-posts-by-sap/elevating-internal-transfers-transitions-through-sap-successfactors/ba-p/13579221)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  2023 Oct 19

Top kudoed authors

| User | Count |
| --- | --- |
| [![ThomasBilbaugh](https://avatars.profile.sap.com/e/0/ide0070e22003039d74134e36021e60621f3d8092be5f11f8ea807d3b320997975_small.jpeg "ThomasBilbaugh")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") ThomasBilbaugh](/t5/user/viewprofilepage/user-id/18281) | 31 |
| [![jenny_geipel](https://avatars.profile.sap.com/2/b/id2bfd2cb1406b6274e78674658af9d916a0ca15fb66ab4e6793400a0a524f93e2_small.jpeg "jenny_geipel")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jenny\_geipel](/t5/user/viewprofilepage/user-id/17811) | 4 |
| [![safina](https://avatars.profile.sap.com/d/8/idd888a4b25efd80039c6b8e8e7a87dc02042f00bd3864ea2a1c61146f4e9de6a1_small.jpeg "safina")  safina](/t5/user/viewprofilepage/user-id/167381) | 2 |
| [![Rosina](https://avatars.profile.sap.com/a/e/idae39fc50de844f762ae9a41561ca7db5605cb681ac7aad154bcf9d87697c15ac_small.jpeg "Rosina")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Rosina](/t5/user/viewprofilepage/user-id/1577832) | 2 |
| [![walters-alison88](https://avatars.profile.sap.com/3/9/id393597bc39c8fd01b68061b0ec52d8c725947345164f71b6925ef0fd71126f09_small.jpeg "walters-alison88")  walters-alison88](/t5/user/viewprofilepage/user-id/116904) | 2 |
| [![Vasudha12](https://avatars.profile.sap.com/b/3/idb36c520109294294b5e91630f0977a6114de6aaef8a3f4e89c370b0a2fd3a0db_small.jpeg "Vasudha12")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") Vasudha12](/t5/user/viewprofilepage/user-id/7787) | 2 |
| [![jonasben](https://avatars.profile.sap.com/b/4/idb43311541d18f6b902f79e18d90867f78094ec5442a5bb85a366ad4d6874869b_small.jpeg "jonasben")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jonasben](/t5/user/viewprofilepage/user-id/81395) | 2 |
| [![NoemiFloris](https://avatars.profile.sap.com/a/2/ida2b77af318ae4753da37b6981d605a83e1b89bf61db1b3398b1a6ec1bbfec318_small.jpeg "NoemiFloris")  ![Product and Topic Expert](/html...
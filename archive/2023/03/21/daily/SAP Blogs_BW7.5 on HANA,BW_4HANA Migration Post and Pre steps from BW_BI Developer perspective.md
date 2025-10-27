---
title: BW7.5 on HANA,BW/4HANA Migration Post and Pre steps from BW/BI Developer perspective
url: https://blogs.sap.com/2023/03/20/bw7.5-on-hanabw-4hana-migration-post-and-pre-steps-from-bw-bi-developer-perspective/
source: SAP Blogs
date: 2023-03-21
fetch_date: 2025-10-04T10:08:32.011400
---

# BW7.5 on HANA,BW/4HANA Migration Post and Pre steps from BW/BI Developer perspective

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* BW7.5 on HANA,BW/4HANA Migration Post and Pre step...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160632&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BW7.5 on HANA,BW/4HANA Migration Post and Pre steps from BW/BI Developer perspective](/t5/technology-blog-posts-by-members/bw7-5-on-hana-bw-4hana-migration-post-and-pre-steps-from-bw-bi-developer/ba-p/13553331)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160632)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160632)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553331)

‎2023 Mar 20
9:40 PM

0
Kudos

1,436

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

**Today I am going to discuss about BW7.5 on HANA**,**BW/4HANA** Migration Post and pre steps from **BW/BI** development perspective. Most of the work done by the SAP basis team of any project but some responsibility also rely on **SAP BW/BI** consultant.

The standard Steps is given below -

```
1	Pre-Cutover	First of all create a Process chain where put all the Extractor DTP sequentially.

                        Name it like - ZPC_DELTA_01

2	Pre-Cutover	BW: Capture before snapshot of BW queries in OLD_BW_LANDSCAPE

3	Pre-Cutover	ECC/S4HANA : LBWE Cockpit Screen shot in OLD_ECC_LANDSCAPE

4	Ramp-Down	BW : Release BI LO Cockpit Jobs after user lock

5	Ramp-Down	BW Run Delta Process chain - ZPC_DELTA_01 utill the queue cleared.

6	Ramp-Down	ECC/S4HANA : Check ODQMON in OLD_ECC_LANDSCAPE to make sure Delta entries

                        are cleared.

7	Ramp-Down	BWValidate all BW related Jobs are Complete & BW dataloads are complete

8	Cutover	        BW: Validate system readiness (RSA1, RSPC, LISTCUBE, RSTRT, RSRV)

9	Cutover	        BW: Setup RFC connection between BW & APO

10	Cutover	        BW: Perform WE20 Partner Profiles Config. Changes

11	Cutover	        BW: Update Assignment of Source System & Validate

12	Cutover	        BW: Validate TRFN/DTP Migration issues if any

13	Cutover	        BW: Activate Data sources

14	Cutover	        BW: Activate Transfer rules

15	Post Cutover	BW: Activate Transformations/DTP's

16	Post Cutover	BW: Validate Eclipse Connection

17	Post Cutover	BW: Check the subscriptions in ODQMON in AWS/AZURE ECC Prod

18	Post Cutover	BW: Execute the Bex reports in RSRT

19	Post Cutover	BW: Execute the reports through Analysis for Office

20	Post Cutover	BW: Transport the Landscape BW Package

21	Post Cutover	BW: Resume the LO - V3 jobs to schedule in ASW ECC Prod

24	Post Cutover	BW: Run DTP offor all  Master data one by one

25	Post Cutover	BW: Transport Process chain Changes / Functional changes

26	Post Cutover	Run the  process chains to load the Transactional Data
```

Hope this will help.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fbw7-5-on-hana-bw-4hana-migration-post-and-pre-steps-from-bw-bi-developer%2Fba-p%2F13553331%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensibility-in-the-age-of-ai-why-abcd-is-easier-and-smarter-than-you/ba-p/14234516)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday

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
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b60703442ad43de8fe0e22782d75a73afb_small.jpeg "dylan-dr...
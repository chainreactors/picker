---
title: How to schedule application jobs from a RAP-based business object
url: https://blogs.sap.com/2022/12/16/how-to-schedule-application-jobs-from-a-rap-based-business-object/
source: SAP Blogs
date: 2022-12-17
fetch_date: 2025-10-04T01:45:59.889074
---

# How to schedule application jobs from a RAP-based business object

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to schedule application jobs from a RAP-based ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159068&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to schedule application jobs from a RAP-based business object](/t5/technology-blog-posts-by-sap/how-to-schedule-application-jobs-from-a-rap-based-business-object/ba-p/13553507)

![Andre_Fischer](https://avatars.profile.sap.com/a/6/ida655827d8a31777be0763b58b458b654e4e62b0aa9c88ee1658ce78b56fe5810_small.jpeg "Andre_Fischer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Andre\_Fischer](https://community.sap.com/t5/user/viewprofilepage/user-id/55)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159068)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159068)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553507)

‎2022 Dec 16
11:38 PM

[25
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159068/tab/all-users "Click here to see who gave kudos to this post.")

19,736

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (4)

Beside the option to start and schedule application jobs from within the Application Job App there might be the need to start an application job from within an application based on a RAP business object.

Scheduling an application job using the API's provided by the underlying ABAP platform framework can be tricky when doing so from within a RAP business object. This is because during it can happen that during the interaction phase implict commits are performed by the underlying frameworks. As a result the application job should only be scheduled within the save sequence to avoid that a job is scheduled unintentionally.

Therefore I have built working sample code that allows you to start an application job via an action of the RAP business object. The sample code shows in addition what needs to be implemented to display the job status in nice way in the Fiori UI using virtual fields. This way it is possible to always reflect the current status highlighting the criticality (aborted, running, finished and others statuses) and the job status text in the Fioir list report using different colours.

The technical information and the source code can be downloaded from GitHub.

<https://github.com/SAP-samples/abap-platform-application-jobs>

---

![](/legacyfs/online/storage/blog_attachments/2022/12/z_demo_appl_jobs_000.png)

---

![](/legacyfs/online/storage/blog_attachments/2022/12/z_demo_appl_jobs_010.png)

---

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

9 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fhow-to-schedule-application-jobs-from-a-rap-based-business-object%2Fba-p%2F13553507%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [HCM pernr and business partner sync issue](/t5/technology-q-a/hcm-pernr-and-business-partner-sync-issue/qaq-p/14234482)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  48m ago
* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2 hours ago
* [SAC Application script multi selection in table onSelect script](/t5/technology-q-a/sac-application-script-multi-selection-in-table-onselect-script/qaq-p/14234372)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  3 hours ago
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  5 hours ago
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  5 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jeet\_kapase](/t5/user/viewprofilepage/user-id/16635) | 11 |
| [![FranciscoHurtado](https://avatars.profile.sap.com/c/7/idc7445eb9fe40fe17679b80e46c92d9e3f68656d9bae139d019c063457dbe84b4_small.jpeg "FranciscoHurtado")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") FranciscoHurtado](/t5/user/viewprofilepage/user-id/170459) | 10 |
| [![marc_steinert](https://avatars.profile.sap.com/e/8/ide87ef5876c7e6b7e3cd441b0a163b602ce92b8fde548577e3274e0845485f23b_small.jpeg "marc_steinert")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-1...
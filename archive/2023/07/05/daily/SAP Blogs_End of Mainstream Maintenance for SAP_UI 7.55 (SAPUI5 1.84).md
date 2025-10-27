---
title: End of Mainstream Maintenance for SAP_UI 7.55 (SAPUI5 1.84)
url: https://blogs.sap.com/2023/07/04/end-of-mainstream-maintenance-for-sap_ui-7.55-sapui5-1.84/
source: SAP Blogs
date: 2023-07-05
fetch_date: 2025-10-04T11:53:35.157334
---

# End of Mainstream Maintenance for SAP_UI 7.55 (SAPUI5 1.84)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* End of Mainstream Maintenance for SAP\_UI 7.55 (SAP...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158628&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [End of Mainstream Maintenance for SAP\_UI 7.55 (SAPUI5 1.84)](/t5/technology-blog-posts-by-sap/end-of-mainstream-maintenance-for-sap-ui-7-55-sapui5-1-84/ba-p/13552433)

![OliverGraeff](https://avatars.profile.sap.com/0/5/id058a949080f65d4d95bbcb641eecc9bfeb7a373b88163622100a70c0b9d7e405_small.jpeg "OliverGraeff")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[OliverGraeff](https://community.sap.com/t5/user/viewprofilepage/user-id/4124)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158628)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158628)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552433)

‎2023 Jul 04
4:15 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158628/tab/all-users "Click here to see who gave kudos to this post.")

3,009

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [User Interface](https://community.sap.com/t5/c-khhcw49343/User%2520Interface/pd-p/378427990965467211484671270864901)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [User Interface

  Topic](/t5/c-khhcw49343/User%2BInterface/pd-p/378427990965467211484671270864901)

View products (3)

![](/legacyfs/online/storage/blog_attachments/2023/07/UI5Officialheader.png)

**Update December 4, 2023:** SAP decided to extend the maintenance period of SAP Fiori FES 2020 and 2021. Details will be published in the notes linked below. As a consequence, this blog post is obsolete.

Working with a complex system with different components and their respective versions is often a challenge. The respective information on SAPUI5 versions is provided by SAP, see the [SAPUI5 versioning concept](https://ui5.sap.com/#/topic/91f021426f4d1014b6dd926db0e91070) and e.g. my blog “[Fresh UI5 innovations every month](https://blogs.sap.com/2018/11/08/fresh-ui5-innovations-every-month/)“. Also see the [SAPUI5 version overview](https://ui5.sap.com/versionoverview.html) and [SAPUI5 versions in the ABAP platform](https://launchpad.support.sap.com/#/notes/2217489).

![](/legacyfs/online/storage/blog_attachments/2023/07/284124_Barricade_R_orange.png)

**I want to make you aware of the fact that the SAPUI5 long-term maintenance version 1.84 has its end of maintenance at the end on 31.12.2023.** For end of mainstream maintenance for SAP\_UI 7.55 (SAPUI5 1.84) see note [3349678](https://me.sap.com/notes/3349678), for general information on SAP Fiori FES 2020 for SAP S/4HANA see note [2919182](https://me.sap.com/notes/2919182).
Related to this end of maintenance is the scheduled deletion of SAPUI5 1.84 (in Q4/2024) and its patches before 1.84.34 (in Q2/2024) from the SAPUI5 CDN. This is according to the plans outlined in [Removing outdated UI5 versions from UI5 CDN](https://blogs.sap.com/2021/01/26/removing-outdated-ui5-versions-from-ui5-cdn/).

Most customers want to receive latest SAPUI5 innovations and at the same time ensure standard support. Therefore, SAP does not recommend starting new implementations with SAP\_UI 7.55, but instead taking the required steps for an upgrade to a more recent version.

![](/legacyfs/online/storage/blog_attachments/2023/07/282560_Linear_flowchart_R_orange-1.png)

SAP recommends upgrading your front-end server according to the Maintenance and Update Strategy for SAP Fiori Front-End Server (see note [2217489](https://launchpad.support.sap.com/#/notes/2217489)).

For upgrade information see [SAP Maintenance Strategy](https://support.sap.com/release-upgrade-maintenance/maintenance-strategy.html), [SAP Maintenance Planner](https://support.sap.com/solution-manager/processes/maintenance-management/maintenance-planner.html) and [Software Logistics Tools](https://support.sap.com/sltoolset). Before an upgrade, please check the target release information and notes referenced in note [2217489](https://me.sap.com/notes/2217489), and also check if the installed applications support the new target landscape.

![](/legacyfs/online/storage/blog_attachments/2023/07/UI5Officialend.png)

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [ui5official](/t5/tag/ui5official/tg-p/board-id/technology-blog-sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fend-of-mainstream-maintenance-for-sap-ui-7-55-sapui5-1-84%2Fba-p%2F13552433%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Business Intelligence - Statement of Direction Update](/t5/technology-blog-posts-by-members/sap-business-intelligence-statement-of-direction-update/ba-p/14226077)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [Reducing Weeks to Minutes: AI, ABAP, and Low-Code in SAP Development](/t5/technology-blog-posts-by-members/reducing-weeks-to-minutes-ai-abap-and-low-code-in-sap-development/ba-p/14221758)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [SAP Cloud ALM & Integrated Toolchain: Your Ultimate Learning Path](/t5/technology-blog-posts-by-sap/sap-cloud-alm-amp-integrated-toolchain-your-ultimate-learning-path/ba-p/14205152)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  4 weeks ago
* [Evaluating SAP’s new MCP servers: UI5, CAP, and Fiori tools in practice](/t5/technology-blog-posts-by-members/evaluating-sap-s-new-mcp-servers-ui5-cap-and-fiori-tools-in-practice/ba-p/14205611)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a month ago
* [Tree-Table Support in CAP is Now Generally Available](/t5/technology-blog-posts-by-sap/tree-table-support-in-cap-is-now-generally-available/ba-p/14202772)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2025 Sep 01

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A...
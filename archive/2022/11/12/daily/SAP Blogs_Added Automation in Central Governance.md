---
title: Added Automation in Central Governance
url: https://blogs.sap.com/2022/11/11/added-automation-in-central-governance/
source: SAP Blogs
date: 2022-11-12
fetch_date: 2025-10-03T22:31:33.837173
---

# Added Automation in Central Governance

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Added Automation in Central Governance

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163264&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Added Automation in Central Governance](/t5/technology-blog-posts-by-sap/added-automation-in-central-governance/ba-p/13566546)

![Mark63](https://avatars.profile.sap.com/6/3/id6345f48fc93c47ef5d6f5f04c833ab30513f1fb1fdf8cd9d9828fc85ca6ff776_small.jpeg "Mark63")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Mark63](https://community.sap.com/t5/user/viewprofilepage/user-id/6240)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163264)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163264)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566546)

‎2022 Nov 11
8:27 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163264/tab/all-users "Click here to see who gave kudos to this post.")

2,265

* SAP Managed Tags
* [SAP Master Data Governance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Master%2520Data%2520Governance/pd-p/67837800100800004488)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Master Data Governance

  SAP Master Data Governance](/t5/c-khhcw49343/SAP%2BMaster%2BData%2BGovernance/pd-p/67837800100800004488)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

Speeding up processing time while ensuring master data quality is key for master data specialists. In this context, sabine.stellmacher pointed out in her recent [blog post](https://blogs.sap.com/2022/05/19/automate-your-master-data-process-with-derivation-scenarios-in-sap-master-data-governance-on-sap-s-4hana/) that [derivation scenarios in SAP Master Data Governance on SAP S/4HANA](https://sapvideoa35699dc5.hana.ondemand.com/?entry_id=1_lywvk6rb) are a perfect means to further automate master data processing.

### Derivation scenarios also in central governance

Using the data quality management capabilities in SAP Master Data Governance, derivation logic can be built in derivation rules which then come into play in master data processing. Derivation scenarios were introduced with SAP S/4HANA 2021 Feature Pack Stack 01 for Product and Business Partner data being applicable in consolidation and mass processing. With SAP S/4HANA 2022 we extended the applicability of this feature from usage in consolidation and mass processing to central governance.

See also the [documentation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/7b586ec9ab7f4d9ba5c240ddac4f3a92.html) in SAP Help Portal.

### Example use case

A master data specialist requests a finished-good product including Sales Area data.  A derivation scenario is applied to a change request in a background step. It derives the corresponding plants from the Sales Area, creates these plant assignments and automatically derives values for mandatory and additional fields.

### Prerequisite

The integration of derivation scenarios with central governance requires SAP S/4HANA release 2022. It is based on a background step in the rule-based workflow, a custom BAdI implementation, a new API (CL\_MDG\_MDQ\_RBWF\_DERIVE), and corresponding customizing.​

### How to implement

A new guide explains in detail how to set up central governance to use derivation scenarios. It also contains tips and tricks for implementing more complex derivation scenarios:

Here, you can directly access the **[Set Up Central Governance to Use Data Quality Management Derivation Scenarios Guide](https://www.sap.com/documents/2022/11/643c8f3a-4e7e-0010-bca6-c68f7e60039b.html)**.

It will also published on our [MDG how-to information](https://community.sap.com/topics/master-data-governance/how-to) page.

To **stay up to date** with what’s going on in the SAP Master Data Governance, simply follow the [SAP Community Topic Page for SAP Master Data Governance](https://community.sap.com/topics/master-data-governance) and join the [Q&A and discussion forum](https://answers.sap.com/tags/67837800100800004488).

Best,

Markus

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [MDGupdates2022](/t5/tag/MDGupdates2022/tg-p/board-id/technology-blog-sap)
* [SAPTipsandTricks](/t5/tag/SAPTipsandTricks/tg-p/board-id/technology-blog-sap)

9 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fadded-automation-in-central-governance%2Fba-p%2F13566546%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 hours ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  3 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Unlocking SAP Fiori and other business content on Mobile: A Practical Guide](/t5/technology-blog-posts-by-sap/unlocking-sap-fiori-and-other-business-content-on-mobile-a-practical-guide/ba-p/14230532)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D...
---
title: Fiori Tile Creation for Custom Transaction Codes/Reports
url: https://blogs.sap.com/2023/02/02/fiori-tile-creation-for-custom-transaction-codes-reports/
source: SAP Blogs
date: 2023-02-03
fetch_date: 2025-10-04T05:34:35.166302
---

# Fiori Tile Creation for Custom Transaction Codes/Reports

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Fiori Tile Creation for Custom Transaction Codes/R...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161509&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Fiori Tile Creation for Custom Transaction Codes/Reports](/t5/technology-blog-posts-by-members/fiori-tile-creation-for-custom-transaction-codes-reports/ba-p/13558745)

![former_member785629](https://avatars.profile.sap.com/former_member_small.jpeg "former_member785629")

[former\_member785629](https://community.sap.com/t5/user/viewprofilepage/user-id/785629)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161509)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161509)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558745)

‎2023 Feb 02
10:37 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161509/tab/all-users "Click here to see who gave kudos to this post.")

38,864

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

**Overview:**

SAP Fiori provides an easier, more intuitive way to run SAP applications in your organization.For SAP Projects we often deal with custom solutions/enhancements.This blog will help to create the Fiori tile for custom transaction codes or custom reports for sap object. This will be divided in mainly four parts:

* Create Semantic Object

* Create Catalog

* Create Group

* Create Role

**Prerequisite:**

* Custom transaction code should be working in SAP system

* Necessary authorizations should be provided to user to create Fiori tiles/groups

**Process:**

1. Create semantic object using Transaction Code SPRO.
   SPRO >> SAP NetWeaver >> UI Technologies >> SAP Fiori >> Setting up Launchpad Content >> Setting up technical Catalogues >> Define custom semantic objects

2. Create new semantic object for Tcode & enter the description

3. Now create catalog using transaction code /n/UI2/FLPD\_CUST.Click + and Enter Title & ID

4. Go to Target mapping and Click on Create target mapping

5. Enter relevant details and click on save

6. Go back to tiles and click on + to add tile

7. Click on App launcher Static, Enter the relevant details as shown below and save

8. Now to create groups, Go to Groups and click +

9. Enter the Title and ID, Click on show as tile and add the tile

10. Now to create a role,Go to PFCG and create new role

11. Go to add transaction then SAP Fiori Launchpad and first add catalog

12. Enter the catalog ID

13. Now go to add transaction then SAP Fiori Launchpad and now add group

14. Enter group ID

15. Assign respective user to the role

16. Now test it using Fiori launchpad

17. New tile should be available to homepage

**Summary:**

By following above steps you can create Fiori tile for any custom transaction code or report

**Conclusion:**

Hope you will find this information useful.

Thank you for reading the blog and please do let me know your thoughts in the comments if this content helps.

Follow the [SAP Fiori environment](https://community.sap.com/topics/fiori)
Post and answer [SAP Fiori relevant questions](https://answers.sap.com/tags/73554900100700000977)
Read other posts on the topic [SAP Fiori Blogs](https://blogs.sap.com/tags/73554900100700000977/)

Happy Learning!

* [@Fiori](/t5/tag/%40Fiori/tg-p/board-id/technology-blog-members)
* [Fiori](/t5/tag/Fiori/tg-p/board-id/technology-blog-members)
* [sap fiori](/t5/tag/sap%20fiori/tg-p/board-id/technology-blog-members)

6 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Ffiori-tile-creation-for-custom-transaction-codes-reports%2Fba-p%2F13558745%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  6 hours ago
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  8 hours ago
* [Incorrect Creation Time Displayed in Billing Document (VF01), Sales Document(VA01) Etc.](/t5/technology-q-a/incorrect-creation-time-displayed-in-billing-document-vf01-sales-document/qaq-p/14234311)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  9 hours ago
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  9 hours ago
* [SAP GUI Automation within SAP BPA Workflow Process](/t5/technology-q-a/sap-gui-automation-within-sap-bpa-workflow-process/qaq-p/14234302)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  9 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d8...
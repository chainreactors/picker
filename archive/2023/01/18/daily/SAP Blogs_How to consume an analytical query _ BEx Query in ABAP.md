---
title: How to consume an analytical query / BEx Query in ABAP
url: https://blogs.sap.com/2023/01/17/how-to-consume-an-analytical-query-bex-query-in-abap/
source: SAP Blogs
date: 2023-01-18
fetch_date: 2025-10-04T04:08:56.882661
---

# How to consume an analytical query / BEx Query in ABAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to consume an analytical query / BEx Query in ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164515&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to consume an analytical query / BEx Query in ABAP](/t5/technology-blog-posts-by-sap/how-to-consume-an-analytical-query-bex-query-in-abap/ba-p/13570280)

![martin_mayer](https://avatars.profile.sap.com/d/9/idd9778aa970a8fe47407f0baaaaeda7211f5d89e2bd5aa4be922a76ddf225a47b_small.jpeg "martin_mayer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[martin\_mayer](https://community.sap.com/t5/user/viewprofilepage/user-id/191669)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164515)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164515)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570280)

‎2023 Jan 17
6:59 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164515/tab/all-users "Click here to see who gave kudos to this post.")

6,368

* SAP Managed Tags
* [BW (SAP Business Warehouse)](https://community.sap.com/t5/c-khhcw49343/BW%2520%28SAP%2520Business%2520Warehouse%29/pd-p/242586194391178517100436979900901)
* [SAP BW/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520BW%252F4HANA/pd-p/73554900100800000681)
* [BW Business Explorer (SAP BEx)](https://community.sap.com/t5/c-khhcw49343/BW%2520Business%2520Explorer%2520%28SAP%2520BEx%29/pd-p/834511320631052684142696158061592)

* [SAP BW/4HANA

  SAP BW/4HANA](/t5/c-khhcw49343/SAP%2BBW%25252F4HANA/pd-p/73554900100800000681)
* [BW (SAP Business Warehouse)

  Software Product Function](/t5/c-khhcw49343/BW%2B%252528SAP%2BBusiness%2BWarehouse%252529/pd-p/242586194391178517100436979900901)
* [BW Business Explorer (SAP BEx)

  Software Product Function](/t5/c-khhcw49343/BW%2BBusiness%2BExplorer%2B%252528SAP%2BBEx%252529/pd-p/834511320631052684142696158061592)

View products (3)

### How can I consume an analytical query in ABAP ?

Normally analytical queries are used with reporting tools like SAC, Analysis Office, WebDynpro Grid,  or RSRT in backend.

This post show how to directly access and use the query within your own ABAP application by the use of **L**ightweight **B**ICS **A**PI ( LBA ) .

It's really easy and needs only 2 ABAP calls . Development was driven by the need for testing the query with unit test. But for sure this approach also fits to others usecase where you want to use the query in your ABAP application.

This example show the most simple case. Calling a query without variables.

```
DATA(lr_std_query) = NEW cl_lba_std_query( i_query_name = 'MyQueryName' ).

lr_std_query->get_resultset(

               "EXPORTING i_t_requested_columns = lt_requested_columns       "dimensions&keyfigures for resultset

               "          i_t_variable_values   = lt_variable                "mandatory and optional variables

               "          i_t_filter_values     = lt_filter                  "additional filters

                IMPORTING e_r_resultset         = DATA(lr_resultset)         "resultset table

                          e_t_column_catalog    = DATA(lt_column_catalog) ). "resultset description
```

LBA comes also with a 2nd flavours to call the CDS based query.

```
DATA(lr_std_query) = NEW cl_lba_cds_query( i_view_name = 'MyCDSview' ).

lr_cds_query->get_resultset(  ...
```

Query in this context means BW modelled queries:

* CDS based analytical queries ,

* Query modelled using BW modelling tools ( BWMT )

* Query modelled using BEx Query Designer

[Note 3269710](https://i7p.wdf.sap.corp/sap/support/notes/0003269710) contain further details like available releases and has 2 attachments
with several sample cases for CDS based queries and classical analytical queries.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [abap analytics](/t5/tag/abap%20analytics/tg-p/board-id/technology-blog-sap)
* [analytics](/t5/tag/analytics/tg-p/board-id/technology-blog-sap)

7 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fhow-to-consume-an-analytical-query-bex-query-in-abap%2Fba-p%2F13570280%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Exploring CDS based Analytical Models with the Relation Explorer - analytical view/perspective](/t5/technology-blog-posts-by-sap/exploring-cds-based-analytical-models-with-the-relation-explorer-analytical/ba-p/14229070)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Unlocking SAP Fiori and other business content on Mobile: A Practical Guide](/t5/technology-blog-posts-by-sap/unlocking-sap-fiori-and-other-business-content-on-mobile-a-practical-guide/ba-p/14230532)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [From REST to Datasphere: A CAP-based Integration Approach](/t5/technology-blog-posts-by-members/from-rest-to-datasphere-a-cap-based-integration-approach/ba-p/14218922)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 Start the Real-Time Transformation](/t5/technology-blog-posts-by-members/sap-s-4hana-stop-the-interapplication-spaghetti-start-the-real-time/ba-p/14229514)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jeet\_kapase](/t5/user/viewprofilepage/user-id/16635) | 11 |
| [![FranciscoHurtado](https://avatars.profile.sap.com/c/7/idc7445eb9fe40fe17679b80e46c92d9e3f68656d9bae139d019c063457dbe84b4_small.jpeg "FranciscoHurtado") ...
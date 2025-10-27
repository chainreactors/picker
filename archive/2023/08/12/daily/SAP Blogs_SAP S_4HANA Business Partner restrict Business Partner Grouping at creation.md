---
title: SAP S/4HANA Business Partner restrict Business Partner Grouping at creation
url: https://blogs.sap.com/2023/08/11/sap-s-4hana-business-partner-restrict-business-partner-grouping-at-creation/
source: SAP Blogs
date: 2023-08-12
fetch_date: 2025-10-04T12:01:29.296027
---

# SAP S/4HANA Business Partner restrict Business Partner Grouping at creation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Business Partner restrict Business Par...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/54666&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Business Partner restrict Business Partner Grouping at creation](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-business-partner-restrict-business-partner-grouping-at-creation/ba-p/13578293)

![Andi_M](https://avatars.profile.sap.com/3/a/id3a5d140ec7baa422d46629af5881b8299f397cf27a68241232baf1edaa302e7d_small.jpeg "Andi_M")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Andi\_M](https://community.sap.com/t5/user/viewprofilepage/user-id/181182)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=54666)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/54666)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13578293)

‎2023 Aug 11
3:31 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/54666/tab/all-users "Click here to see who gave kudos to this post.")

5,135

* SAP Managed Tags
* [APP PLATFORM Business Partner](https://community.sap.com/t5/c-khhcw49343/APP%2520PLATFORM%2520Business%2520Partner/pd-p/397511424400755828374365287279243)
* [SAP S/4HANA Cloud Private Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Private%2520Edition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

* [APP PLATFORM Business Partner

  Software Product Function](/t5/c-khhcw49343/APP%2BPLATFORM%2BBusiness%2BPartner/pd-p/397511424400755828374365287279243)
* [SAP S/4HANA Cloud Private Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPrivate%2BEdition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

View products (2)

At Business Partner creation process you have to decide whether to create a Business Partner as person or organization (and very seldom as group).

Unfortunately there is no restriction of Business Partner Grouping depending on Business Partner Type person or organization. Independent on Business Partner Type you will always see all defined Business Partner Groupings.

In this blog I will describe a way how to reduce available Business Partner Groupings based on selected Business Partner Type. With this solution you can restrict available Business Groupings dependent on selected Business Partner Type (person, organization).

# Introduction

The purpose of this blog is to describe how to influence available Business Partner Groupings at Business Partner creation with transaction BP.

**Target audience:** Functional Experts

**Version:** SAP S/4HANA On Premise 1610 and higher

A detailed description of used BAdI BUPA\_NUMBER\_GROUP you will find at SAP Note [995155 - Filtering the values in the number grouping dropdown](https://me.sap.com/notes/995155)

# Starting Point

If you run transaction BP and create a person you will get a screen like this.

![](/legacyfs/online/storage/blog_attachments/2023/08/01-BP-transaction.jpg)

As you can see there are all defined Business Partner Groupings listed.

Target is to reduce available values just to this two entries if you create a person:

0170 Consumer

0200 Contact Person

Foundation is a custom customizing table where possible combinations of Business Partner Type and Business Partner Groupings are stored.

# Create control table

To define allowed Business Partner Groupings per Business Partner Type you have to create customizing table (inclusive table maintenance screen) in customer name space which you can maintain via transaction SM30.

![](/legacyfs/online/storage/blog_attachments/2023/08/02-Z-Table.jpg)

At this example I defined only Business Partner Groupings 0170 and 0200 for persons:

![](/legacyfs/online/storage/blog_attachments/2023/08/03-Z-Table-entries.jpg)

As you can see only person (Business Partner Type 1) is entered for Business Partner Groupings 0170 and 0200.

# BAdI Implementation

Create an implementation for BAdI BUPA\_NUMBER\_GROUP at transaction SE19.

Implement following example coding at method  IF\_EX\_BUPA\_NUMBER\_GROUP~VALID\_NUMBER\_GROUP

```
  METHOD if_ex_bupa_number_group~valid_number_group.

    DATA: lt_group     TYPE TABLE OF zbp_type_group,

          lv_type      TYPE bu_type,

          ls_values    TYPE LINE OF bus_screen-dropdown_values,

          lv_sytabix   TYPE sy-tabix.

    lv_type = iv_request->gs_navigation-bupa-creation_type.

    SELECT * FROM zbp_type_group INTO TABLE lt_group WHERE type = lv_type.

    LOOP AT et_dropdown_values INTO ls_values.

      lv_sytabix = sy-tabix.

      READ TABLE lt_group WITH KEY bu_group = ls_values-key TRANSPORTING NO FIELDS.

      IF sy-subrc NE 0.

        DELETE et_dropdown_values INDEX lv_sytabix.

      ELSE.

        lv_sytabix = lv_sytabix + 1.

      ENDIF.

    ENDLOOP.

  ENDMETHOD.
```

# Test transaction BP

If you now run transaction BP and create a person you will see the reduced available Business Partner Groupings.

![](/legacyfs/online/storage/blog_attachments/2023/08/04-result.jpg)

# Further Improvement

To reduce available Business Partner Roles based on selected Business Partner Grouping please have a look at blog

[SAP S/4HANA Business Partner restrict Business Partner Roles based on Grouping at creation](https://blogs.sap.com/2023/08/15/sap-s-4hana-business-partner-restrict-business-partner-roles-based-on-grouping-at-creation/)

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [business partner](/t5/tag/business%20partner/tg-p/board-id/erp-blog-sap)
* [s4hana 2022](/t5/tag/s4hana%202022/tg-p/board-id/erp-blog-sap)
* [S4HANA RIG](/t5/tag/S4HANA%20RIG/tg-p/board-id/erp-blog-sap)
* [SAP S4HANA 2022](/t5/tag/SAP%20S4HANA%202022/tg-p/board-id/erp-blog-sap)
* [sap s4hana rig](/t5/tag/sap%20s4hana%20rig/tg-p/board-id/erp-blog-sap)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsap-s-4hana-business-partner-restrict-business-partner-grouping-at-creation%2Fba-p%2F13578293%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-s-4hana-public/ba-p/14234546)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  yesterday
* [MD01N Behavior: Issuing Storage Location Not Set in Stock Tran...
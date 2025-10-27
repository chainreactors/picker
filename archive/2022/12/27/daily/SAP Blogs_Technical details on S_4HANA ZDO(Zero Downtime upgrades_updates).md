---
title: Technical details on S/4HANA ZDO(Zero Downtime upgrades/updates)
url: https://blogs.sap.com/2022/12/26/technical-details-on-s-4hana-zdozero-downtime-upgrades-updates/
source: SAP Blogs
date: 2022-12-27
fetch_date: 2025-10-04T02:32:49.782653
---

# Technical details on S/4HANA ZDO(Zero Downtime upgrades/updates)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Technical details on S/4HANA ZDO(Zero Downtime upg...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67674&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Technical details on S/4HANA ZDO(Zero Downtime upgrades/updates)](/t5/enterprise-resource-planning-blog-posts-by-members/technical-details-on-s-4hana-zdo-zero-downtime-upgrades-updates/ba-p/13558699)

![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")

[rajarajeswari\_kaliyaperum](https://community.sap.com/t5/user/viewprofilepage/user-id/654809)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67674)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67674)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558699)

‎2022 Dec 26
3:07 PM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67674/tab/all-users "Click here to see who gave kudos to this post.")

17,236

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA, platform edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520platform%2520edition/pd-p/01200314690800001945)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA, platform edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bplatform%2Bedition/pd-p/01200314690800001945)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (4)

In this blog, I wish to discuss the high-level technical details on ZDO upgrades/updates that can be performed by any basis expert who has completed the learning journey and assessment ADM330.

```
NOTE: Below blog has been written based on the Public reference  from SAP:

Reference:https://help.sap.com/doc/b4e092bbef2a48db867e5b0095a6559a/zdosum20.latest/en-US/zdo_sum20_s4hana.pdf
```

If you want to have a quick overview on what this assessment is about, do check out my other blog =>"Why should a basis admin pass ADM330(ZDO for S/4HANA updates and upgrades) assessment"

[https://blogs.sap.com/2022/12/26/why-should-a-basis-admin-pass-adm330zdo-for-s-4hana-updates-and-upg...](https://blogs.sap.com/2022/12/26/why-should-a-basis-admin-pass-adm330zdo-for-s-4hana-updates-and-upgrades-assessment/)

NOTE: This blog must be used to attain high-level knowledge of ZDO upgrades. Basis experts must complete the ADM330 course to attain complete details in this regard.

```
This blog is targeted to answer the below questions.

1. What is a ZDO upgrade/update and how does this attain Zero technical downtime?

2. What is a bridge subsystem?

3. How does ZDO operates together with the original and bridge subsystem to attain zero technical downtime during upgrades?

4. What are the different subsystems involved with ZDO upgrades?

5. How does the bridge subsystem operate with a list of views that are pointing to different versions of the same table in the original system?

6. What are the available table classifications during ZDO run?

7. How does SUM arrive at the above classification?

8. How to download the table statistics for SUM Impact Analysis from the production environment?

9. What are the preliminary ZDO readiness process that must be executed in a S/4HANA system?

10.How is SLT-enabled S/4HANA systems handled during ZDO upgrades?

11.How does ZDO perform application data migration? How is this approach different from a normal standard upgrade?

12.How is the reset procedure handled in ZDO?

13.What does it takes to execute a ZDO in a landscape until production?

14.How is ZDO different from nZDM and the standard approach?
```

**1. What is a ZDO upgrade/update and how does this attain Zero technical downtime?**

ZDO revolves around the concept of running an update/upgrade without technical downtime along with minimal business downtime. This is attained with the help of the bridge subsystem. The technical downtime only involves restarting the application server without a need to restart the database. Usually, the restart takes approximately 5 to 15 minutes based on the number of application servers involved. Both original and bridge subsystems will be running on the same database.

SAP has enabled ZDO upgrades starting from S/4HANA2020. This upgrade does not need a separate license. The basis expert must have cleared the assessment ADM330 and must hold an SAP-generated password for the specific SID.

**2. What is a bridge subsystem?**
In my own words, this is a clone-like version of the original source system and will be running on the source version where business users get reconnected to continue their task when the original system gets into technical downtime for an upgrade to the target version by SUM2.0.

The reason behind calling this a clone-like instead of the clone is due to the fact that this bridge subsystem *only has the views that are pointing to the tables in the original system*. However, the original system will have shared tables that could be shared between the original and bridge system or might have a clone of the table with 2 different versions(one pointing to the source version=>to be accessed by business users in the bridge subsystem) and the other pointing to the target version=>to be accessed by SUM)). These table clone requirements are determined based on the type of change the upgrade is going to bring into this table and SUM uses the process called Impact Analysis to arrive at the specified table classification.

Refer to question "**7. How does SUM arrive at the above classification?** " for more details in this blog.

**3. How does ZDO operates together with the original and bridge subsystem to attain zero technical downtime during upgrades?**

![](/legacyfs/online/storage/blog_attachments/2022/12/1-26.jpg)

Reference: Page 12 for public guide below. <https://help.sap.com/doc/b4e092bbef2a48db867e5b0095a6559a/zdosum20.16/en-US/zdo_sum20_s4hana.pdf>

Business users will work on the original system in release 1 which is the actual source release. In the same system, SUM processing will be started. After the uptime processing in the original system, SUM will perform rollover of the business users to the bridge subsystem which will be in source release as the target version is yet to be finalized. Transitioning of the users to the bridge subsystem happens in a controlled manner, thus enabling the business users to continue their work in the bridge system seamlessly. While the business continues to operate in t...
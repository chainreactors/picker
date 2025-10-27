---
title: Collected information about reclaim / shrink / defragmentation topic in context of SAP HANA persistence (with example)
url: https://blogs.sap.com/2023/01/16/collected-information-about-reclaim-shrink-defragmentation-topic-in-context-of-sap-hana-persistence-with-example/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:39.562682
---

# Collected information about reclaim / shrink / defragmentation topic in context of SAP HANA persistence (with example)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Collected information about reclaim / shrink / def...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164534&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Collected information about reclaim / shrink / defragmentation topic in context of SAP HANA persistence (with example)](/t5/technology-blog-posts-by-sap/collected-information-about-reclaim-shrink-defragmentation-topic-in-context/ba-p/13570397)

![Laszlo_Thoma](https://avatars.profile.sap.com/9/0/id90e702a1d83a67b7a2fde409bf21a6d43811f8e390c7650756fae929ea4a3e5d_small.jpeg "Laszlo_Thoma")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Laszlo\_Thoma](https://community.sap.com/t5/user/viewprofilepage/user-id/170406)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164534)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164534)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570397)

‎2023 Jan 16
3:17 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164534/tab/all-users "Click here to see who gave kudos to this post.")

8,376

* SAP Managed Tags
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520studio/pd-p/67838200100800004076)
* [SAP HANA, express edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520express%2520edition/pd-p/73555000100800000651)
* [SAP HANA, platform edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520platform%2520edition/pd-p/01200314690800001945)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA studio

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bstudio/pd-p/67838200100800004076)
* [SAP HANA, express edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bexpress%2Bedition/pd-p/73555000100800000651)
* [SAP HANA, platform edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bplatform%2Bedition/pd-p/01200314690800001945)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (6)

* [Introduction](#toc-hId-834753318)
* [Task 1. – Exercise](#toc-hId-638239813)
* [Prerequisites](#toc-hId-570809027)
* [Background](#toc-hId-374295522)
* [Exercise](#toc-hId-177782017)
* [Conclusion](#toc-hId--18731488)
* [Task 2. – Documentation Library](#toc-hId--344327712)
* [Where to find documentations in SAP Help Portal?](#toc-hId--411758498)
* [Which is the master SAP Knowledge Base Article of the SAP HANA persistence?](#toc-hId--608272003)
* [When (in general) and after what action, the fragmentation needs to be checked?](#toc-hId--804785508)
* [Which other documentation is important in context of monitoring SAP HANA persistence?](#toc-hId--654044656)
* [Which other documentation is important regarding SAP HANA reclaim / shrink / defragmentation topic?](#toc-hId--850558161)
* [Which SAP HANA Alert IDs belongs to the topic?](#toc-hId--1047071666)
* [What are the available tools for defragmentation?](#toc-hId--1243585171)
* [What is the typical scenario after data deletion?](#toc-hId--1440098676)
* [What are the known issues?](#toc-hId--1636612181)
* [Automatic Data Volume Reclaim](#toc-hId--1833125686)
* [What blog posts can be helpful?](#toc-hId--2029639191)
* [Other articles in this series](#toc-hId-2068814600)
* [Other articles in connected series](#toc-hId-1872301095)
* [Useful bookmark](#toc-hId-1843971281)
* [Do you have further questions?](#toc-hId-1940860783)
* [Contribution](#toc-hId-1744347278)

**![banner.png](/t5/image/serverpage/image-id/58286i321320936737CD72/image-size/large?v=v2&px=999 "banner.png")**

last updated: 2025-09-30

# **Introduction**

There is huge knowledge available about SAP HANA reclaim / shrink / defragmentation topic, but the knowledge is very fragmented (Help Portal, Blog post, SAP KBA, SAP Note, other). In order to simply and make content consumption easier I have created a centralized page, a single source of the available information regarding SAP HANA persistence. Further I would like to help you with shrinking exercise in SAP HANA, express edition to demonstrate the process.

![banner2.png](/t5/image/serverpage/image-id/58288iA26D8303B7B3B934/image-size/large?v=v2&px=999 "banner2.png")
[What is SAP HANA?](https://www.sap.com/products/technology-platform/hana/what-is-sap-hana.html)

# **Task 1. – Exercise**

## **Prerequisites**

* Hypervisor (VMware Workstation Player 16)
* SAP HANA, express edition (db version: 2.00.061)
  [Install SAP HANA 2.0, express edition on a Preconfigured Virtual Machine (with SAP HANA XS Advanced)](https://developers.sap.com/group.hxe-install-vm-xsa.html)
* SAP HANA Studio (version: 2.3.63)
* [Frequently Asked Questions About SAP HANA®, Express Edition](https://www.sapstore.com/medias/HANA-express-edition-FAQ?context=bWFzdGVyfHJlc291cmNlc3wxMzcwNzY0fGFwcGxpY2F0aW9uL3BkZnxyZXNvdXJjZXMvaDY0L2hkNS8xMzI2NjIwMzE4MTA4Ni5wZGZ8YjI5ZTkwOWZhZTEzNDllZmY0OTgyNjM1ZmZkNzU1NzBkYTUyMDIwNWJkYTY1ODEyNzk1ZjdmNDZlMTcyZGMyNw)

## **Background**

During the exercises I will use test database SFLIGHT. More information can be find:
[SAP HANA, express edition and SFLIGHT demo database, modeling – Complete Tutorial](https://blogs.sap.com/2022/04/26/sap-hana-express-edition-and-sflight-demo-database-modeling-complete-tutorial/)

The SFLIGHT schema is in the Catalog folder.

![](/legacyfs/online/storage/blog_attachments/2023/01/1-2.png)

## **Exercise**

The actual fragmentation can be identified with the following SQL Statement: *"HANA\_Disks\_Overview"*.

* [1969700](https://launchpad.support.sap.com/#/notes/1969700) - SQL Statement Collection for SAP HANA
* [3293572](https://launchpad.support.sap.com/#/notes/3293572) - SQL Statement Collection: "HANA\_Disks\_Overview" report for SAP HANA

![](/legacyfs/online/storage/blog_attachments/2023/01/1-42.png)

In production system the fragmentation (~30%) is accepted, should not do reclaim. It will be defragmented to demonstrate the process (test system).

```
ALTER SYSTEM RECLAIM DATAVOLUME 120 DEFRAGMENT;
```

![](/legacyfs/online/storage/blog_attachments/2023/01/2-22.png)

The following values (all) had been decreased: TOTAL\_GB, UNUSED\_GB, FRAG\_PCT.

**![:exclamation_mark:](/html/@8C09647FB84AEB056251BD826555DBE2/emoticons/2757.png ":exclamation_mark:")Best Practice**: the RECLAIM process can be scheduled when the system ...
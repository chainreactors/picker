---
title: HANA Workload Management deep dive part II
url: https://blogs.sap.com/2023/01/09/hana-workload-management-deep-dive-part-ii/
source: SAP Blogs
date: 2023-01-10
fetch_date: 2025-10-04T03:25:14.865724
---

# HANA Workload Management deep dive part II

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* HANA Workload Management deep dive part II

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162658&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HANA Workload Management deep dive part II](/t5/technology-blog-posts-by-members/hana-workload-management-deep-dive-part-ii/ba-p/13565053)

![jgleichmann](https://avatars.profile.sap.com/4/9/id4917548940ddeab8c16ae9f19696579afcbb6e3251e79a83d9fd5f2cf89638cd_small.jpeg "jgleichmann")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[jgleichmann](https://community.sap.com/t5/user/viewprofilepage/user-id/139000)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162658)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162658)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565053)

‎2023 Jan 09
5:26 PM

[21
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162658/tab/all-users "Click here to see who gave kudos to this post.")

9,336

* SAP Managed Tags
* [SAP BW/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520BW%252F4HANA/pd-p/73554900100800000681)
* [SAP enhancement package for SAP ERP, version for SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520enhancement%2520package%2520for%2520SAP%2520ERP%252C%2520version%2520for%2520SAP%2520HANA/pd-p/67838200100800004843)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA, platform edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520platform%2520edition/pd-p/01200314690800001945)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [BW SAP HANA Data Warehousing](https://community.sap.com/t5/c-khhcw49343/BW%2520SAP%2520HANA%2520Data%2520Warehousing/pd-p/337684911283545157914465705009179)

* [SAP BW/4HANA

  SAP BW/4HANA](/t5/c-khhcw49343/SAP%2BBW%25252F4HANA/pd-p/73554900100800000681)
* [SAP enhancement package for SAP ERP, version for SAP HANA

  SAP ERP](/t5/c-khhcw49343/SAP%2Benhancement%2Bpackage%2Bfor%2BSAP%2BERP%25252C%2Bversion%2Bfor%2BSAP%2BHANA/pd-p/67838200100800004843)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA, platform edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bplatform%2Bedition/pd-p/01200314690800001945)
* [BW SAP HANA Data Warehousing

  Software Product Function](/t5/c-khhcw49343/BW%2BSAP%2BHANA%2BData%2BWarehousing/pd-p/337684911283545157914465705009179)

View products (6)

**last updated: 2023-01-09 18:00 CEST**

Ok, you already read [part I](https://blogs.sap.com/2022/09/08/hana-workload-management-deep-dive-part-i) of the deep dive series of HANA workload management. You are waiting for more insides after you identified some HANA resource bottlenecks? Then you are on the right track. In this part I will describe how you can get an overview of your systems workload and how to handle it with different methods.

It is important to know the behavior and the load if the system. Every system is used in another way. Means you have to analyze, interpret and understand the workload. You have to know if it was just a one-time occurrence or a frequent behavior.

Most common scenarios:

1. The system is overloaded and cannot fulfill the request - means the DB can no longer respond

2. Performance issues for certain queries

3. System is not using the defined thresholds

HANA workload management deep dive part II

1. 1. [General workload management](#general)

   2. [Admission Control](#admission)
   [back to part I](https://blogs.sap.com/2022/09/08/hana-workload-management-deep-dive-part-i)
   [forward to part III](https://blogs.sap.com/2023/04/11/hana-workload-management-deep-dive-part-iii//)

---

## **General workload management**

There are multiple ways to consume your resources efficiently. I will only describe the common methods and go not too deep into details of NUMA and CPU affinities.

If a statement is not limited by a parameter or a workload class, it can use all resources if the optimizer choose a execution plan with parallel threads. This resources will be granted directly after the connect of the session.

First of all how to identify such resource bottlenecks? Again please use and study the scripts of Martin Frauendorfer in note 1969700. It is worth to spend the time to know how to use them.

Identify the time frames when the CPU goes over 70% for a long-time span is a good indicator. Please keep in mind that there might be some short critical time frames which are **not** included in the thread sampling of the HANA. It is not exactly documented by SAP how the HANA is getting the resource details from the OS process and how grading works. But by default if the tracking (service\_thread\_sampling\_monitor\_enabled) is activated in newer revisions (Rev. 55), but as the name says it is just sampling and no exact measurement. This means short peaks below 2-3 seconds can get lost, but the admission control can be activated due to another measurement method. Here an expert monitoring is needed. But back to 90% of the cases:

![](/legacyfs/online/storage/blog_attachments/2023/01/Performance_Monitor_CPU2.png)

There is CPU time divided into CPU(host and indexserver) and SYS (System).

**CPU** on **host** level means the CPU time outside of HANA, e.g. third-party tools like AV, FS Backup etc.

**CPU** on **indexserver** means the CPU time of the indexserver without the interrupts and OS kernel time.

**SYS** is including the interrupts (I/O, network, etc.).

Other tools like nmon, top or the SQL collection will only break it down to CPU and SYS. Means indexserver CPU as **CPU** and all third party and interrupts as **SYS.**

HANA\_LoadHistory\_Services\_\*

|
 ``` SNAPSHOT_TIME HOST   PORT   PING_MS       CPU    SYS    USED_GB       SWAP_MB       CONNS  TRANS  BTRANS STMT_PS       ACT_THR       WAIT_THR     wait_thr_in_% ACT_SQL       WAIT_SQL      wait_sql_in_% PEND_SESS    VERSIONS      COM_RANGE    HANDLES       MERGES       UNLOADS    2022/08/03 10:02:00 hanahost00   any    26     83     1      2738,65       0      753    250    0      2098   397    55,66  14     48,16       42,16  88     0.00   108053 34376  2003   12     0    2022/08/03 04:47:00 hanahost00   any    42     70     1      2710,83       0      607    191    0      76     527,83 216,16 41     7,66       7,16   93     0.00   1503   574    1847   0      0    2022/08/03 04:46:00 hanahost00   any    45     81     1      2740,91       0      606    192    0      120    514,83 209,83 41     12,83       12,16  95     0.00   3044   922    1839   6      0    2022/08/03 04:45:00 hanahost00   any    55     92     1      2757,53       0      600    183    0      86     690,83 293,83 43     13,16       12,83  97     0.00   3724   866    1838   0      0    2022/08/03 04:44:00 han...
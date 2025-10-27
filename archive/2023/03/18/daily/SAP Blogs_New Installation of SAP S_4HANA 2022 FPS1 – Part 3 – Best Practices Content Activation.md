---
title: New Installation of SAP S/4HANA 2022 FPS1 – Part 3 – Best Practices Content Activation
url: https://blogs.sap.com/2023/03/17/new-installation-of-sap-s-4hana-2022-fps1-part-3-best-practices-content-activation/
source: SAP Blogs
date: 2023-03-18
fetch_date: 2025-10-04T09:57:18.499888
---

# New Installation of SAP S/4HANA 2022 FPS1 – Part 3 – Best Practices Content Activation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* New Installation of SAP S/4HANA 2022 FPS1 – Part 3...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51052&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [New Installation of SAP S/4HANA 2022 FPS1 – Part 3 – Best Practices Content Activation](/t5/enterprise-resource-planning-blog-posts-by-sap/new-installation-of-sap-s-4hana-2022-fps1-part-3-best-practices-content/ba-p/13554923)

![mahesh_sardesai](https://avatars.profile.sap.com/8/a/id8add3238dfb86754123fab2374437646e50fe79a842990baf674e3f6f49e0e6e_small.jpeg "mahesh_sardesai")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[mahesh\_sardesai](https://community.sap.com/t5/user/viewprofilepage/user-id/755)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51052)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51052)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554923)

‎2023 Mar 17
6:12 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51052/tab/all-users "Click here to see who gave kudos to this post.")

10,223

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

This blog is created with joint team work between **Hanuma Rupakula** and**Mahesh Sardesai**.

Please refer [SAP Note 3268525 - Jump Start Your SAP S/4HANA 2022 Implementation by Activating SAP Best Practices](https://launchpad.support.sap.com/#/notes/3268525) which will guide you in preparing for implementation of S/4HANA using SAP Best Practices content.

**WARNING:** This blog provides guidance for activating S/4HANA 2022 FPS1 Best Practices when a client is setup as Best Practice client. If you set up a merged client as per Alternative 2 - Setting up a merged client (all client 000 reference settings), follow the activation guidance as per [SAP Note 3228633 - Implementation of SAP S/4HANA SAP Best Practices 2022 (private cloud & on premise...](https://launchpad.support.sap.com/#/notes/3228633) **(steps shown in this color)**

**NOTE:** for Best practices activation purpose we recommend to use latest SAPGui, In case you are using SapGui version 7.50, you need to uncheck **"Accept Belize theme"**. Once the Best practices activation is completed, you can activate the SAP Fiori visual theme back. This is shown later under SAP SAPGUI settings.

Please find other blogs as follows at [S/4HANA SQUARE ONE](https://blogs.sap.com/2019/08/29/s4hana-square-one/)

|
 **SAP S/4HANA  SQUARE  ONE** |

|
 **NEW INSTALLATION** |
 **PART1 - MP** |
 **PART2 -** **Installation** |
 **PART3 -** **BP Activation** |
 **PART4 - Fiori Activation** |
 **PART5 - DATA MIGRATION** |

|
 **S/4HANA 2022** |
 [fps1](https://blogs.sap.com/2023/02/23/new-installation-of-sap-s-4hana-2022-fps1-part-1-maintenance-planner/) [fps0](https://blogs.sap.com/2022/10/12/new-installation-of-sap-s-4hana-2022-fps0-part-1-maintenance-planner/) |
 [fps1](https://blogs.sap.com/2023/02/23/new-installation-of-sap-s-4hana-2022-fps1-part-2-installation/) [fps0](https://blogs.sap.com/2022/10/12/new-installation-of-sap-s-4hana-2022-fps0-part-2-installation/) |
 [fps1](https://blogs.sap.com/2023/03/17/new-installation-of-sap-s-4hana-2022-fps1-part-3-best-practices-content-activation/) [fps0](https://blogs.sap.com/2022/10/14/new-installation-of-sap-s-4hana-2022-fps0-part-3-best-practices-content-activation/) |
 [fps1](https://blogs.sap.com/2023/03/17/new-installation-of-sap-s-4hana-2022-fps1-part-4-rapid-activation-for-fiori/) [fps0](https://blogs.sap.com/2022/10/26/new-installation-of-sap-s-4hana-2022-fps0-part-4-rapid-activation-for-fiori/) |
  |

|
 **S/4HANA 2021** |
 [fps2](https://blogs.sap.com/2022/05/25/new-installation-of-sap-s-4hana-2021-fps2-part-1-maintenance-planner/) [fps1](https://blogs.sap.com/2022/02/23/new-installation-of-sap-s-4hana-2021-fps1-part-1-maintenance-planner/) [fps0](https://blogs.sap.com/2021/10/13/new-installation-of-sap-s-4hana-2021-fps0-part-1-maintenance-planner/) |
 [fps2](https://blogs.sap.com/2022/05/26/new-installation-of-sap-s-4hana-2021-fps2-part-2-installation/) [fps1](https://blogs.sap.com/2022/02/24/new-installation-of-sap-s-4hana-2021-fps1-part-2-installation/) [fps0](https://blogs.sap.com/2021/10/14/new-installation-of-sap-s-4hana-2021-fps0-part-2-installation/) |
 [fps2](https://blogs.sap.com/2022/05/27/new-installation-of-sap-s-4hana-2021-fps2-part-3-best-practices-content-activation/) [fps1](https://blogs.sap.com/2022/02/25/new-installation-of-sap-s-4hana-2021-fps1-part-3-best-practices-content-activation/) [fps0](https://blogs.sap.com/2021/10/23/new-installation-of-sap-s-4hana-2021-fps0-part-3-best-practices-content-activation/) |
 [fps2](https://blogs.sap.com/2022/05/28/new-installation-of-sap-s-4hana-2021-fps2-part-4-rapid-activation-for-fiori/) [fps1](https://blogs.sap.com/2022/03/02/new-installation-of-sap-s-4hana-2021-fps1-part-4-rapid-activation-for-fiori/) [fps0](https://blogs.sap.com/2021/10/23/new-installation-of-sap-s-4hana-2021-fps0-part-4-rapid-activation-for-fiori/) |
  |

|
 **S/4HANA 2020** |
 [fps2](https://blogs.sap.com/2021/05/25/new-installation-of-sap-s-4hana-2020-fps2-part-1-maintenance-planner/) [fps1](https://blogs.sap.com/2021/02/24/new-installation-of-sap-s-4hana-2020-fps1-part-1-maintenance-planner/) [fps0](https://blogs.sap.com/2020/10/07/new-installation-of-s-4hana-2020-fps0-part-1-maintenance-planner/) |
 [fps2](https://blogs.sap.com/2021/05/27/new-installation-of-sap-s-4hana-2020-fps2-part-2-installation/) [fps1](https://blogs.sap.com/2021/02/25/new-installation-of-sap-s-4hana-2020-fps1-part-2-installation/) [fps0](https://blogs.sap.com/2020/10/09/new-installation-of-s-4hana-2020-fps0-part-2-installation/) |
 [fps2](https://blogs.sap.com/2021/06/04/new-installation-of-sap-s-4hana-2020-fps2-part-3-best-practices-content-activation/) [fps1](https://blogs.sap.com/2021/02/26/new-installation-of-sap-s-4hana-2020-fps1-part-3-best-practices-content-activation/) [fps0](https://blogs.sap.com/2020/10/14/new-installation-of-s-4hana-2020-fps0-part-3-best-practices-content-activation/) |
 [fps2](https://blogs.sap.com/2021/05/31/new-installation-of-sap-s-4hana-2020-fps2-part-4-rapid-activation-for-fiori/) [fps1](https://blogs.sap.com/2021/02/27/new-installation-of-sap-s-4hana-2020-fps1-part-4-rapid-activation-for-fiori/) [fps0](https://blogs.sap.com/2020/10/21/new-installation-of-s-4hana-2020-fps0-part-4-rapid-activation-for-fiori/) |
 [fps0](https://blogs.sap.com/2020/10/31/new-installation-of-sap-s-4hana-2020fps0-part-5-direct-data-transfer-using-migration-cockpit/) |

|
 **UPGRADE** |
 **t1-RC** |
 **t2 -****MP** |
 **t3 -** **SIC** |
 **t4 - CCM** |
 **t5 - SUM** |

|
 **S/4HANA 1809+** |
 [rcu](https://blogs.sap.com/2021/11/01/upgrade-to-s-4hana-t1-readiness-check/)  [iop](https://blogs.sap.com...
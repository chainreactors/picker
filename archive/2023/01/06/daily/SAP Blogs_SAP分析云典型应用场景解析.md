---
title: SAP分析云典型应用场景解析
url: https://blogs.sap.com/2023/01/05/sap%e5%88%86%e6%9e%90%e4%ba%91%e5%85%b8%e5%9e%8b%e5%ba%94%e7%94%a8%e5%9c%ba%e6%99%af%e8%a7%a3%e6%9e%90/
source: SAP Blogs
date: 2023-01-06
fetch_date: 2025-10-04T03:09:31.231137
---

# SAP分析云典型应用场景解析

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP分析云典型应用场景解析

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158464&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP分析云典型应用场景解析](/t5/technology-blog-posts-by-sap/sap%E5%88%86%E6%9E%90%E4%BA%91%E5%85%B8%E5%9E%8B%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF%E8%A7%A3%E6%9E%90/ba-p/13552019)

![Martin_Xie1](https://avatars.profile.sap.com/c/4/idc4a844b9efddad0013fa58517bdd1665accd299849df3ff002fc90a3b9119011_small.jpeg "Martin_Xie1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Martin\_Xie1](https://community.sap.com/t5/user/viewprofilepage/user-id/174751)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158464)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158464)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552019)

‎2023 Jan 05
9:02 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158464/tab/all-users "Click here to see who gave kudos to this post.")

1,484

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)
* [SAP Analytics Cloud, augmented analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520augmented%2520analytics/pd-p/2221d1b0-d759-4b24-9333-f72da4d263da)
* [SAP Analytics Cloud, data modeling](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520data%2520modeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)
* [SAP Analytics Cloud, analytics designer](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520analytics%2520designer/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [SAP Analytics Cloud, add-in for Microsoft Office](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520add-in%2520for%2520Microsoft%2520Office/pd-p/73555000100800001621)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)
* [SAP Analytics Cloud, analytics designer

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Banalytics%2Bdesigner/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [SAP Analytics Cloud, add-in for Microsoft Office

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Badd-in%2Bfor%2BMicrosoft%2BOffice/pd-p/73555000100800001621)
* [SAP Analytics Cloud, augmented analytics

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Baugmented%2Banalytics/pd-p/2221d1b0-d759-4b24-9333-f72da4d263da)
* [SAP Analytics Cloud, data modeling

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Bdata%2Bmodeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)

View products (6)

引言：大家好，当你看到这篇博客的时候，恭喜你，你捡到宝了！今天我来谈一谈我见到过的SAP Analytics Cloud的典型应用场景

SAP 分析云SAP Analytics Cloud（在中国被简称SAC）是SAP为了适应大数据时代消费级、体验BI的趋势，基于SAP BTP业务技术云平台推出的新一代商务分析平台。SAP Analytics Cloud继承了之前SAP分析产品的优势，并进行了更多的增强和应用；SAP Analytics Cloud是目前市场上唯一整合分析、预测、预算为一体的分析平台，提供了用户需要的所有分析能力。截止目前，SAP Analytics Cloud已经在国内落地了6年了，6年来SAP Analytics Cloud经历了从小白到大白的华丽转身，在前有堵截(Power BI)、后有追兵(FineBI)的市场环境下，取得了显著的业务成效，为SAP BTP打开了一片新的天地。下面我就将典型的应用场景做一下简要的介绍，并且将经验教训做一个梳理。

1、传统的BI应用

传统的BI应用，展现形式上主要是格式化报表，拖拉拽自助式报表分析，按主题的数据展现。这部分客户的典型特征是相对成熟的2B领域客户，其体量相对大，思路转变相对慢，用户对新鲜事物的接受度有限。典型的应用场景包括人力(人员构成分布/人效指标分析)、财务(总账/资金/应收/应付/固定资产)、采购(采购量价分析/供应商分析)、库存(进销存/特殊库存)、生产(计划/进度/产出)、销售(销售量价/客户分析)。

2、基于大屏的实时生产调度

这一典型应用主要以调度指挥大屏为主要依托，应用内容包括工厂的实时状况，包括投料、生产、计划、安灯呼叫等。这种客户往往体量不会特别巨大，属于专精特新类企业，有较为完整的IT体系，比如ERP、MES、IoT比较健全。典型的应用场景包括主要机器设备的实时数据监控展示、IT部门的内部项目/系统运行状态展示、工厂的整体投料/在制/产出、工厂的环境保护指标实时显示。

3、基于SAP Analytics Cloud的全面预算管理

全面预算管理是企业，特别是集团企业实现战略目的的重要手段，因此具有强烈的刚需市场。这部分客户的典型特征就是IT基础设施比较完备，ERP核算系统已经就绪，特别是以SAP ERP为主，希望有比较灵活的预算编制、分析环境。典型的应用场景包括业务预算编制、财务预算编制、数据分发控制(控制过程在执行系统或OA系统)、实际数据收集分析。

4、Business Planning and Consolidation-SAP Analytics Cloud的混合部署

从2008年BPC在中国销售以来，我们的BPC客户数以百计，他们在使用的过程中遇到了或多或少的问题，特别是现在的居家办公、远程办公、移动办公等新时代的需求，导致BPC的适用性一般，客户迫切需要灵活的预算编制方案。这部分客户的现行特征就是体量相对来说很大，员工的预算编制环境各异(电脑、办公软件、网络)，需要灵活便捷的业务预算平台，还能与BPC有良好的集成。典型的应用场景包括销售预算编制、员工居家办公灵活录入、对不支持的Excel版本的替换方案、做完预算之后数据写回BPC，考虑到数据的保密性，很多企业可能会删除掉云端的数据。

5、利用SAP Analytics Cloud的在线模拟测算功能

有些公司已经使用了FineBI、Tableau等，但是由于他们只有BI的功能做图表的动态分析，在xP&A领域实际上没有太多的探索，因此可以使用SAP Analytics Cloud的在线模拟功能实现对经营的提前模拟测算。这部分客户的典型特点就是BI系统已经应用多年，有足够的经验，具有xP&A的想法，只是缺少做经营分析的支撑工具。典型的应用场景包括单品成本的测算模拟、销售收入的测算模拟、收入/利润的测算模拟，同时会结合预测功能进行数据的预测，以此作为基本的模拟输入，比较符合SAP Analytics Cloud的功能特点和SAP xP&A的经营理念。对于四资企业(外商独资、中外合资、中外合作、民营资本)可以接受云端数据存储，对于其他大/中企业会考虑把云端数据删除，有个“最小化数据上云”的全新概念提出。

篇幅有限，今天就聊到这里，后续有了更多发现，咱们继续畅聊。也欢迎大家市场回家来坐坐：<https://community.sap.com/zh/topics/cloud-analytics>

Labels

* [Life at SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/life%20at%20sap)

* [@SAP Analytics Cloud](/t5/tag/%40SAP%20Analytics%20Cloud/tg-p/board-id/technology-blog-sap)
* [extended planning and analysis](/t5/tag/extended%20planning%20and%20analysis/tg-p/board-id/technology-blog-sap)
* [Financial Planning and Analysis](/t5/tag/Financial%20Planning%20and%20Analysis/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap%25E5%2588%2586%25E6%259E%2590%25E4%25BA%2591%25E5%2585%25B8%25E5%259E%258B%25E5%25BA%2594%25E7%2594%25A8%25E5%259C%25BA%25E6%2599%25AF%25E8%25A7%25A3%25E6%259E%2590%2Fba-p%2F13552019%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Problems to web build](/t5/technology-q-a/problems-to-web-build/qaq-p/14234583)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  21m ago
* [Resource Injection Failed: Error while pushing files. Cause: Request not supported. CPI error.](/t5/technology-q-a/resource-injection-failed-error-while-pushing-files-cause-request-not/qaq-p/14234547)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  48m ago
* [Extensibility in the Age of AI: Why ABCD Is Easier (and Smarter) Than You Think](/t5/technology-blog-posts-by-sap/extensibility-in-the-age-of-ai-why-abcd-is-easier-and-smarter-than-you/ba-p/14234516)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  an hour ago
* [SAP BTP CI CD service for on premise S4 HANA systems RICEFW applications](/t5/technology-q-a/sap-btp-ci-cd-service-for-on-premise-s4-hana-systems-ricefw-application...
---
title: SAP 分析云 2023.11版新功能抢先看
url: https://blogs.sap.com/2023/06/25/sap-%e5%88%86%e6%9e%90%e4%ba%91-2023.11%e7%89%88%e6%96%b0%e5%8a%9f%e8%83%bd%e6%8a%a2%e5%85%88%e7%9c%8b/
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:45:54.932742
---

# SAP 分析云 2023.11版新功能抢先看

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP 分析云 2023.11版新功能抢先看

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164115&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP 分析云 2023.11版新功能抢先看](/t5/technology-blog-posts-by-sap/sap-%E5%88%86%E6%9E%90%E4%BA%91-2023-11%E7%89%88%E6%96%B0%E5%8A%9F%E8%83%BD%E6%8A%A2%E5%85%88%E7%9C%8B/ba-p/13569117)

![William_Yu1](https://avatars.profile.sap.com/b/e/idbec53017157fe078365abe56ea13aec0f09a41a4130c197ba619ff74fbf379f6_small.jpeg "William_Yu1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[William\_Yu1](https://community.sap.com/t5/user/viewprofilepage/user-id/62666)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164115)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164115)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569117)

‎2023 Jun 26
12:32 AM

0
Kudos

774

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)
* [SAP Analytics Cloud, data modeling](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520data%2520modeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)
* [SAP Analytics Cloud, data modeling

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Bdata%2Bmodeling/pd-p/3ecbe2ed-7fe9-4831-924a-77987d1a4259)

View products (3)

[SAP 分析云](https://www.sap.cn/products/cloud-analytics.html)是一款先进的商务分析云解决方案，集商业智能 (BI)、增强分析、预测分析和企业规划功能于一体，消除单点解决方案和数据孤岛挑战，能提供你需要的全面云分析功能。

本文介绍了SAP 分析云2023.07版本的新功能。这些新功能已经在SAP 分析云FastTrack 客户的系统上线。对于 SAP 分析云季度发布周期 (QRC) 客户，此版本及其功能将作为 QRC 2023 年第2季度版本的一部分提供。

## **系统和技术要求**

尽管不是必需的，我们推荐您升级到最新的 SAP 分析云代理版本 **1.0.372**，利用所有数据采集类型。

除以下情况外，您的代理需要1.0.75或以上版本：

* SAP ERP/SQL 数据库版本 1.0.99

* SAP Universe (UNX)版本1.0.365（ SAP分析云代理需要额外的设置步骤，有关详细信息，请参阅 SAP 说明[3262098](https://launchpad.support.sap.com/#/notes/3262098)）

* SAP Business Warehouse (BW)版本 1.0.353

* SAP HANA View版本 1.0.235

* File Server版本 1.0.248

更多详细信息，请参阅 [系统要求和技术先决条件](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/11b4e5ff76eb4747bc255d7037be1f01.html?locale=zh-CN)。

有关将 SAP BW 与 SAP 分析云集成的受支持功能和所需更新，请参阅 2541557  以了解更多详细信息。

有关通过 SAP BusinessObjects Live Data Connect 与 SAP分析云来实时访问 Universe 时的受支持功能和所需更新，请参阅 2771921  以了解更多详细信息。

请从**“Service Marketplace”**下载最新版本的**“简易部署工具箱”**。

* 为避免下载旧版本并可能让用户面对 Cloud Connector 与 SAPJVM 或 Apache Tomcat 的绑定不当带来的漏洞，只有三个最新版本可供下载。

关于云代理的版本变更管理细节，请参考SAP Note 3264839。

## **更新亮点**

* 仪表盘和故事设计

  + [消除图表中平面表示方法下的时间成员歧义](https://blogs.sap.com/2023/06/25/sap-%E5%88%86%E6%9E%90%E4%BA%91-2023.11%E7%89%88%E6%96%B0%E5%8A%9F%E8%83%BD%E6%8A%A2%E5%85%88%E7%9C%8B/#1)

* 数据集成

  + [BPC实时连接中支持IBCS格式](https://blogs.sap.com/2023/06/25/sap-%E5%88%86%E6%9E%90%E4%BA%91-2023.11%E7%89%88%E6%96%B0%E5%8A%9F%E8%83%BD%E6%8A%A2%E5%85%88%E7%9C%8B/#2)

* 企业计划

  + [数据操作-使用启用了“所有成员”参数的筛选器](https://blogs.sap.com/2023/06/25/sap-%E5%88%86%E6%9E%90%E4%BA%91-2023.11%E7%89%88%E6%96%B0%E5%8A%9F%E8%83%BD%E6%8A%A2%E5%85%88%E7%9C%8B/#3)

  + [计划触发器-附加格式选项](https://blogs.sap.com/2023/06/25/sap-%E5%88%86%E6%9E%90%E4%BA%91-2023.11%E7%89%88%E6%96%B0%E5%8A%9F%E8%83%BD%E6%8A%A2%E5%85%88%E7%9C%8B/#4)

  + [筛选个别日历事件](https://blogs.sap.com/2023/06/25/sap-%E5%88%86%E6%9E%90%E4%BA%91-2023.11%E7%89%88%E6%96%B0%E5%8A%9F%E8%83%BD%E6%8A%A2%E5%85%88%E7%9C%8B/#5)

## **仪表盘和故事设计**

### **消除图表中平面表示方法下的时间成员歧义**

在优化故事体验中，我们改进了图表中平面表示方法下的时间成员消歧功能，以消除图表与表格之间的差异：

* 现在，对于平面表示方法下的时间层级而言，图表与表格之间的时间标签是一致的。

* 故事设计者可以在图表中同时看到以3个字母表示的月份以及年份。

## ![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-51.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture2-39.png)

## **数据集成**

### **BPC实时连接中支持IBCS格式**

BPC实时连接： 现在表格已支持IBCS格式。

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture3-45.png)

## **企业计划**

### **数据操作****-使用启用了“所有成员”参数的筛选器**

现在，输入控件和故事筛选器都可以被定义为选择“所有成员”。当至少有一个成员被取消选择时，用户仍然可以通过数据和多步操作触发器使用输入控件和故事筛选器。因此，每当用户向相关维度添加新成员时，用户将无需对输入控件或故事筛选器进行调整——新成员将立即可用，并且可以通过触发器使用。

这在优化故事体验中可用。

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture4-32.png)

### **计划触发器****-附加格式选项**

在故事中使用优化故事体验时，用户现在可以为多个操作、数据操作或BPC计划序列的计划触发器进行格式化和自定义。附加格式选项包括选择触发按钮、图标颜色、上传图表以及选择触发文本的字体、大小。

自定义触发按钮拓展了设计灵活性，使得触发器外观能够同用户喜爱的主题与设计相匹配，从而营造出更加协调一致的视觉体验。

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture5-23.png)

### **筛选个别日历事件**

为了聚焦于特定的日历事件或者系列，用户目前可以对日历或者列表工作区进行筛选，使其仅显示所需事件。如果用户选择某个流程作为筛选条件，那么其子事件也将一并显示。此外，用户还能够通过内置的搜索功能进一步缩小特定事件的范围。

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture6-27.png)

**结语**

本文仅提供 SAP 分析云的最新功能和增强功能的高级概述。有关这些功能的更多详细信息，请访问 [SAP分析云帮助门户](https://help.sap.com/viewer/product/SAP_ANALYTICS_CLOUD/release/en-US)。您还可以访问[SAP Road Map Explorer](https://roadmaps.sap.com/board?PRODUCT=67838200100800006884&amp;range=CURRENT-LAST&range=CURRENT-LAST)查看 SAP分析云即将推出的功能。

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [SAP 分析云](/t5/tag/SAP%20%E5%88%86%E6%9E%90%E4%BA%91/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-%25E5%2588%2586%25E6%259E%2590%25E4%25BA%2591-2023-11%25E7%2589%2588%25E6%2596%25B0%25E5%258A%259F%25E8%2583%25BD%25E6%258A%25A2%25E5%2585%2588%25E7%259C%258B%2Fba-p%2F13569117%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [How to get "full control" on columns design in a SAP Analytics cloud table ?](/t5/technology-q-a/how-to-get-quot-full-control-quot-on-columns-design-in-a-sap-analytics/qaq-p/13635839)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2024 Mar 12
* [SAC- Advanced Formulas-Sum the year so far and project last months](/t5/technology-q-a/sac-advanced-formulas-sum-the-year-so-far-and-project-last-months/qaq-p/12819871)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2024 Jan 15
* [Webi report - Automatically calculate values ​​at prompts](/t5/technology-q-a/webi-report-automatically-calculate-values-at-prompts/qaq-p/12794383)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2023 Nov 02

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4...
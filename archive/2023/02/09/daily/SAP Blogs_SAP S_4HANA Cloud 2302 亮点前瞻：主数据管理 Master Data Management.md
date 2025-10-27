---
title: SAP S/4HANA Cloud 2302 亮点前瞻：主数据管理 Master Data Management
url: https://blogs.sap.com/2023/02/08/sap-s-4hana-cloud-2302-%e4%ba%ae%e7%82%b9%e5%89%8d%e7%9e%bb%ef%bc%9a%e4%b8%bb%e6%95%b0%e6%8d%ae%e7%ae%a1%e7%90%86-master-data-management/
source: SAP Blogs
date: 2023-02-09
fetch_date: 2025-10-04T06:07:08.237572
---

# SAP S/4HANA Cloud 2302 亮点前瞻：主数据管理 Master Data Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Cloud 2302 亮点前瞻：主数据管理 Master Data Mana...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51851&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Cloud 2302 亮点前瞻：主数据管理 Master Data Management](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-cloud-2302-%E4%BA%AE%E7%82%B9%E5%89%8D%E7%9E%BB-%E4%B8%BB%E6%95%B0%E6%8D%AE%E7%AE%A1%E7%90%86-master-data-management/ba-p/13560338)

![Huang_Mingkang](https://avatars.profile.sap.com/a/1/ida1a11841096180f76c7285c0e4cd0e26f3ae0afbf8cb4b7335b9b6fc017dbb5c_small.jpeg "Huang_Mingkang")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Huang\_Mingkang](https://community.sap.com/t5/user/viewprofilepage/user-id/131906)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51851)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51851)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560338)

‎2023 Feb 08
10:42 PM

0
Kudos

983

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Master Data](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Master%2520Data/pd-p/771f6577-e8ec-415f-99a7-6b73add46c47)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud Public Edition Master Data

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BMaster%2BData/pd-p/771f6577-e8ec-415f-99a7-6b73add46c47)

View products (2)

本篇博客旨在列举 SAP S/4HANA Cloud 2302 当中**主数据管理 Master Data Management**版块发布的关于产品主数据管理相关的新功能，覆盖了以下特点：

* ###### [“定义过滤条件”应用中的产品主数据过滤条件允许跨系统传输](#fcmdt)

* ###### [在产品主数据的相关应用中启用了 MPN（制造商零件编号） 功能](#mdmpn)

* ###### [迁移场景中扩展了产品主数据的Unified API：PSTAT](#mdmapipstat)

## “定义过滤条件”应用中的产品主数据过滤条件允许跨系统传输

当我们使用DRF在系统间进行数据复制的时候，我们需要应用“定义过滤条件”来定义产品主数据筛选过滤条件，以实现可筛选的产品主数据复制。**过去**，用户不能在类似于Q2P的场景中传输已定义好的产品主数据筛选过滤条件，而只能在每个系统中反复维护同一套产品主数据筛选过滤条件。

随着本次2302的版本发布，借助新的“传输功能”，用户可以将产品主数据筛选对象和相应的产品主数据筛选条件的详细信息从一个系统传输到另一个系统。我们不必在每个系统中重新创建产品主数据筛选过滤条件，而是使用新的传输机制来复制产品主数据筛选过滤条件。

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-38.png)

源系统中的产品主数据筛选过滤条件

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-18.png)

目标系统中的产品主数据筛选过滤条件

## 在产品主数据的相关应用中启用了 MPN（manufacturer part number制造商零件编号） 功能

使用产品主数据应用，客户想要维护产品主数据中的制造商零件编号，以连接内部物料编号和供应商物料编号。
客户现在可以创建“HERS”物料类型和字段，以维护 MPN 详细信息。
由于这些功能主要用于采购相关的应用，因此最佳实践内容将与采购相关的Scope Item一起提供。在客户系统中激活相应的Scope Item后，所有 MPN 字段都将可见。

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-40.png)

“HERS”物料类型

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-20.png)

维护 MPN 详细信息

## 迁移场景中扩展了产品主数据的Unified API：PSTAT

通过 SAP S/4HANA Cloud 中的简化数据模型，产品主数据中多个字段的 PSTAT做了减少，并为大多数产品主数据字段维护了单个 PSTAT。在某些情况下，对于将产品主数据从 ECC 迁移或集成到 S/4 HANA  Cloud系统，用户将会会丢失某些产品主数据字段的 PSTAT。
借助新功能，用户现在，可以在产品主数据复制后避免维护/创建缺少的产品主数据 PSTAT 。通过使用Unified API 进行到 SAP S/4 HANA Cloud 系统的产品数据迁移，用户将能够看到客户定义的字段的所有 PSTAT 值。

## ![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-41.png)

## **更多关于** **SAP****S/4HANA Cloud :**

* 引导解决决策树关键字汇总 [查看](https://blogs.sap.com/?p=1662438)

* 提报事件之前可以查看的小建议：[查看](https://d.dam.sap.com/a/5v2BUrq/SAP%20S4HC%20Steps%20Before%20Raising%20an%20Incident.pdf)

### 【以下为英文内容】

* Highlights of the SAP S/4HANA Cloud, Public Edition 2302 Release [here](https://blogs.sap.com/2023/01/25/highlights-of-the-sap-s-4hana-cloud-public-edition-2302-release/)

* SAP S/4HANA Cloud, public edition release info [here](https://community.sap.com/topics/s4hana-cloud/product-releases)

* Latest SAP S/4HANA Cloud, public edition release blog posts [here](https://blogs.sap.com/tag/pscc_enablement/)and previous release highlights [here](https://blogs.sap.com/2018/06/01/sap-s4hana-cloud-the-intelligent-erp-link-collection/)

* Product videos on our [SAP S/4HANA Cloud, Public Edition](https://www.youtube.com/playlist?list=PLWV533hWWvDnnyN2j-CcUheNN-GaNCb3H) and [SAP S/4HANA](https://www.youtube.com/playlist?list=PLWV533hWWvDnmdq6Ps2LZLybNjZWy5A2b) YouTube playlist

* SAP S/4HANA PSCC Digital Enablement Wheel [here](https://chart-bdmaicr0au.dispatcher.eu2.hana.ondemand.com/index.html?hc_reset)

* Early Release Webinar Series [here](https://blogs.sap.com/2020/11/11/sap-s-4hana-cloud-early-release-series-watch-replays-on-demand/?preview_id=1218772)

* Inside SAP S/4HANA Podcast [here](https://open.sap.com/static/inside-sap/index.php?p=archive)

* openSAP Microlearnings for SAP S/4HANA [here](https://microlearning.opensap.com/)

* Best practices for SAP S/4HANA Cloud, public edition [here](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud)

* SAP S/4HANA Cloud, Public Edition Community: [here](https://community.sap.com/topics/s4hana-cloud)

* Feature Scope Description [here](https://help.sap.com/doc/7c9e0bbbd1664c2581b2038a1c7ae4b3/latest/)

* What’s New [here](https://help.sap.com/doc/ce01d82756b947a1a043a5d5a3204226/latest/)

* Help Portal Product Page [here](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD)

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [PSCC\_CCC\_CN](/t5/tag/PSCC_CCC_CN/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsap-s-4hana-cloud-2302-%25E4%25BA%25AE%25E7%2582%25B9%25E5%2589%258D%25E7%259E%25BB-%25E4%25B8%25BB%25E6%2595%25B0%25E6%258D%25AE%25E7%25AE%25A1%25E7%2590%2586-master-data-management%2Fba-p%2F13560338%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [ENGINEERING CHANGE MANAGEMENT(ECM)](/t5/enterprise-resource-planning-blog-posts-by-members/engineering-change-management-ecm/ba-p/14163252)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Monday
* [5 Essential Points for Successfully Closing EXPLORE in SAP S/4HANA Cloud Private Edition Projects](/t5/enterprise-resource-planning-blog-posts-by-...
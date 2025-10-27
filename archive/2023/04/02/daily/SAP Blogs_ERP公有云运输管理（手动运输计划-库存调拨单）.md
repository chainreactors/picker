---
title: ERP公有云运输管理（手动运输计划-库存调拨单）
url: https://blogs.sap.com/2023/04/01/erp%e5%85%ac%e6%9c%89%e4%ba%91%e8%bf%90%e8%be%93%e7%ae%a1%e7%90%86%ef%bc%88%e6%89%8b%e5%8a%a8%e8%bf%90%e8%be%93%e8%ae%a1%e5%88%92-%e5%ba%93%e5%ad%98%e8%b0%83%e6%8b%a8%e5%8d%95%ef%bc%89/
source: SAP Blogs
date: 2023-04-02
fetch_date: 2025-10-04T11:26:56.779528
---

# ERP公有云运输管理（手动运输计划-库存调拨单）

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* ERP公有云运输管理（手动运输计划-库存调拨单）

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52887&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ERP公有云运输管理（手动运输计划-库存调拨单）](/t5/enterprise-resource-planning-blog-posts-by-sap/erp%E5%85%AC%E6%9C%89%E4%BA%91%E8%BF%90%E8%BE%93%E7%AE%A1%E7%90%86-%E6%89%8B%E5%8A%A8%E8%BF%90%E8%BE%93%E8%AE%A1%E5%88%92-%E5%BA%93%E5%AD%98%E8%B0%83%E6%8B%A8%E5%8D%95/ba-p/13566412)

![Feng_Chen](https://avatars.profile.sap.com/b/5/idb510cba38534353e6e96c15e92188a99b8fc88c9077c6f14b97c3533231e8946_small.jpeg "Feng_Chen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Feng\_Chen](https://community.sap.com/t5/user/viewprofilepage/user-id/132169)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52887)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52887)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566412)

‎2023 Apr 01
7:36 AM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52887/tab/all-users "Click here to see who gave kudos to this post.")

1,354

* SAP Managed Tags
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (2)

建议先浏览Blogs: [EPR公有云运输管理初介绍](https://blogs.sap.com/2023/03/25/erp%E5%85%AC%E6%9C%89%E4%BA%91%E8%BF%90%E8%BE%93%E7%B3%BB%E7%BB%9F%E5%88%9D%E4%BB%8B%E7%BB%8D/)；[EPR公有云运输管理（手动运输计划-内向）](https://blogs.sap.com/2023/03/29/erp%E5%85%AC%E6%9C%89%E4%BA%91%E8%BF%90%E8%BE%93%E7%B3%BB%E7%BB%9F%EF%BC%88%E6%89%8B%E5%8A%A8%E8%BF%90%E8%BE%93%E8%AE%A1%E5%88%92-%E5%86%85%E5%90%91%EF%BC%89/)

## **业务流程（****5XD****）**

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD0.png)

## **创建库存调拨单**

这里是参考业务场景BME：含交货的库存转储，来创建库存调拨单的。所以建议先保证BME能够测通，您需要参考BME Set-Up Instructions把主数据和配置都完成后进行测试。

创建库存调拨单可以通过MRP创建也可以手动创建。

APP：创建采购订单-高级，采购组007

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD1.png)

装运类型01

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD2.png)

更改内向交货的确认控制，触发内向交货单

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD3.png)

## **执行手动计划**

APP：运输主控室

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD4.png)

选择货运单元，创建卡车类型并且选择，点击分配选定项目，点击保存生成右屏幕的货运订单

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD5-1.png)

## **执行承运方转包**

APP：管理货运订单，找到之前创建的货运订单，打开编辑在基本信息中输入承运方、采购组织、采购组，然后点击费用，根据实际业务输入相关运费类型和运费。

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD6.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD7.png)

点击转包更改状态，发送到运输公司，根据实际业务再更改成设置为“运输公司已确认”。

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD8.png)

## **监控货运订单触发交货创建**

APP: 管理货运订单，点击创建交货，您也可以选择批处理创建交货。

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD9.png)

通过凭证流查到内向交货单凭证号

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD10.png)

## **拣配库存调拨单**

APP：管理出库交货，或者APP：更改出库交货

## **设置货车已在装运点位置到达并已检入**

APP：监控执行-货运订单，点击执行状态选择设置为“已做好运输执行准备”

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD11.png)

根据实际卡车运输状态，在基本信息页面下的阶段，选择执行状态（源）设置为“已运达”，然后改成设置为“已检入”，保存后会提示费用计算已完成和成本分摊已完成。

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD12.png)

## **设置货车已在装运点位置到达并已检入**

APP：监控执行-货运订单，根据实际卡车运输状态，在基本信息页面下的阶段，选择执行状态（源）设置为“已检出”，然后改成设置为“已启运”，保存后会提示费用计算已完成和成本分摊已完成。

## **过账库存调拨单的发货**

APP：管理出库交货，或者APP：更改出库交货

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD13.png)

## **设置货车已在收货点位置到达并已检入**

APP：监控执行-货运订单，根据实际卡车运输状态，在基本信息页面下的阶段，选择执行状态（目标）设置为“已运达”，然后改成设置为“已检入”，保存后会提示费用计算已完成和成本分摊已完成。

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD14.png)

## **设置仓储准备就绪**

APP：监控执行-货运订单，在货运订单中编辑基本信息选项下阶段中选择阶段行项目，点击设置仓库处理就绪（目的地），点击保存

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD15.png)

## **设置货车已在收货点位置检出并已离开**

APP：监控执行-货运订单，根据实际卡车运输状态，在基本信息页面下的阶段，选择执行状态（目标）设置为“已检出”，然后改成设置为“已启运”，保存后会提示费用计算已完成和成本分摊已完成。

## **确认应计过账的货运订单**

APP：监控应计过账-货运凭证，您可以浏览货运凭证的详细信息比如运费，阶段等，然后点击确认过账。

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD16.png)

## **确认入库数量**

内向交货单号可以通过调拨单流程流里找到

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD17.png)

APP：更改入库交货，在卸下选项下输入入库数量，点击保存

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD18.png)

## **过账入库交货的收货**

APP：更改入库交货，点击过账收货

## **承运方结算**

### **创建供应商发票**

APP：创建供应商发票-高级

![](/legacyfs/online/storage/blog_attachments/2023/04/5XD19.png)

## **感谢您阅读这篇博文。请继续关注!**

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Ferp%25E5%2585%25AC%25E6%259C%2589%25E4%25BA%2591%25E8%25BF%2590%25E8%25BE%2593%25E7%25AE%25A1%25E7%2590%2586-%25E6%2589%258B%25E5%258A%25A8%25E8%25BF%2590%25E8%25BE%2593%25E8%25AE%25A1%25E5%2588%2592-%25E5%25BA%2593%25E5%25AD%2598%25E8%25B0%2583%25E6%258B%25A8%25E5%258D%2595%2Fba-p%2F13566412%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-s-4hana-public/ba-p/14234546)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  yesterday
* [Mass creation of RFQ in S/4 hana system](/t5/enterprise-resource-planning-q-a/mass-creation-of-rfq-in-s-4-hana-system/qaq-p/14234508)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [Multiple Account ID under one House Bank](/t5/enterprise-resource-planning-q-a/multiple-account-id-under-one-house-bank/qaq-p/14234496)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [Error in archiving for HRCUSTAX object](/t5/enterprise-resource-planning-q-a/error-in-archiving-for-hrcustax-object/qaq-p/14234432)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [Activation of Universal Parallel Accounting](/t5/enterprise-resource-planning-q-a/a...
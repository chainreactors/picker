---
title: 高级公司间销售和高级公司间库存转储 常见问题集锦
url: https://blogs.sap.com/2022/11/25/%e9%ab%98%e7%ba%a7%e5%85%ac%e5%8f%b8%e9%97%b4%e9%94%80%e5%94%ae%e5%92%8c%e5%ba%93%e5%ad%98%e8%bd%ac%e5%82%a8-%e5%b8%b8%e8%a7%81%e9%97%ae%e9%a2%98%e9%9b%86%e9%94%a6/
source: SAP Blogs
date: 2022-11-26
fetch_date: 2025-10-03T23:48:54.865524
---

# 高级公司间销售和高级公司间库存转储 常见问题集锦

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* 高级公司间销售和高级公司间库存转储 2208版本常见问题集锦

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51591&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [高级公司间销售和高级公司间库存转储 2208版本常见问题集锦](/t5/enterprise-resource-planning-blog-posts-by-sap/%E9%AB%98%E7%BA%A7%E5%85%AC%E5%8F%B8%E9%97%B4%E9%94%80%E5%94%AE%E5%92%8C%E9%AB%98%E7%BA%A7%E5%85%AC%E5%8F%B8%E9%97%B4%E5%BA%93%E5%AD%98%E8%BD%AC%E5%82%A8-2208%E7%89%88%E6%9C%AC%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E9%9B%86%E9%94%A6/ba-p/13558370)

![ecco_liu](https://avatars.profile.sap.com/9/a/id9a5e3aaf023973dbd36b33cdf3a3e9c8abef884bef43ad08075aa9427b58b8ab_small.jpeg "ecco_liu")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ecco\_liu](https://community.sap.com/t5/user/viewprofilepage/user-id/492951)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51591)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51591)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558370)

‎2022 Nov 25
4:41 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51591/tab/all-users "Click here to see who gave kudos to this post.")

4,693

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Supply Chain](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Supply%2520Chain/pd-p/253c6759-2b52-46f4-be45-e2ab78f2f420)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition Supply Chain

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSupply%2BChain/pd-p/253c6759-2b52-46f4-be45-e2ab78f2f420)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (2)

在上一篇博文中，我们介绍了S/4HANA Cloud上高级公司间销售和高级公司间库存转储的流程及系统演示，如上篇博文提到的，在本篇博文中我们将就S/4HANA Cloud 2208 delta training中产品收到的关于高级公司间销售和高级公司间库存转储的常见问题进行如下汇总。如果中国客户在使用高级公司间销售或高级公司间库存转储时也有如下疑问或困惑，希望以下问题集锦能对大家有所帮助。若有其他疑问点或需求，也可以留言告知我们。

申明：本博客仅供功能参考，请结合系统测试以测试结果为准，同时请关注产品持续的功能功能和可能的变更。

**1. 高级公司间销售是否使用普通凭证类型？**

卖方公司的销售订单使用常规销售订单类型（例如，OR）、普通项目类别（例如TAN）和常规计划行类别（例如CV）。卖方公司的采购订单使用新的采购订单类型。交货公司的销售订单使用以定制方式定制的新销售订单类型、项目类别和计划行类别，即与 ATP、MRP、产品合规性、贸易合规性、运输管理等无关。

**2.如果公司间采购订单和销售订单不是使用 MRP** **创建的，它们是否仍在“****库存需求/****覆盖范围监控”****应用中可见？**

只有销售公司的销售订单与 MRP 和 ATP 相关。公司间采购订单和公司间销售订单不可见。

**3. 如果流程中需要，是否可以使用附加步骤更新 VCM****？以金属行业示例，其中将根据产品的最终检验创建第二张发票。**
在当前版本的 VCM 中，客户无法添加额外的流程步骤，也无法定义自己的 E2E 流程。

**4.此流程是否支持集团评估？是否支持企业预置中的利润中心评估？**
支持集团评估，但不支持利润中心评估。利润中心评估已纳入产品路线图中，敬请期待。

**5.如何管理 SO2** **中的更改？后续凭证中是否存在自动更新？**

系统自动管理销售公司中销售订单的变更（VCM - 价值链监控框架），例如，如果更改确认数量，新的确认数量将分配到 PO3 和 SO4。或者，如果交货工厂从美国更改为加拿大，则将为现有 PO3 项目加删除标记，拒绝 SO4 项目，并在加拿大创建一个新的 PO3 和新的 SO4。更改的方向为 SO2 到 PO3 到 SO4。不支持相反方向。

**6.能否同时激活高级公司间销售和传统公司间销售？**

可以，高级公司间销售和传统公司间销售在配置层面可通过订单类型和行项目类别的组合进行区分，从而实现业务共存。但客户需要关心的核心问题是客户是否需要Group Valuation (5W2)，如果是，则不可激活传统公司间销售. 建议客户从业务上评估完整、测试后选择合适的公司间销售模式。

**7.更新 SO2** **中的交货工厂时，是否删除或取消 PO + SO****？**

如果交货工厂从美国更改为加拿大，则现有 PO3 项目将标记为删除，将拒绝 SO4 项目，并在加拿大创建一个新的 PO3 和新的 SO4。

**8.高级公司间销售场景中有哪些 FI** **报表功能？**
如果通用平行会计已激活，则为集团报表启用 Adv ICo Sales。此外，高级 ICo 销售支持常规 FI 报表，如产品成本核算、利润分析 (COPA)、分类账、财务报表等。通常来说，高级公司间销售支持基于分类账的所有报表。

**9.高级公司间销售/****库存转储是否与 GTS** **集成？**
高级公司间销售/库存转储和GTS 在技术上已集成。GTS 相关对象（例如，销售订单和交货）将调用 GTS，同时也和S/4HANA Cloud上的国际贸易管理，如禁运、证照检查、实体名单扫描无缝集成。

**10.是否计划拥有多个系统场景？**

产品已计划支持多系统场景，但暂未有详细计划安排。

**11.除了来自其他工厂的销售外，是否还可以应用客户退货？**

高级 ICo 销售只能用于销售流程。不包括客户退货，表示如果您参考高级 ICo 销售项目创建客户退货，则退货将以传统公司间样式运行。与S/4HANA cloud上的客户退货集成已在产品计划中，敬请期待。5D2/5MQ冲销请参考SAP KBA: KB0502656 （<https://itsm.services.sap/nav_to.do?uri=%2Fkb_view.do%3Fsysparm_article%3DKB0502656）>

**12.如何将第一个销售订单连接到 E2E** **凭证？**

VCM 将 E2E 流程直接涉及的所有文档连接起来。此外，凭证流存储在业务应用程序中。

**13.如何激活高级公司间销售或高级公司间库存转储流程？需要额外的许可证吗？**

在 S/4HANA cloud中，高级公司间销售需要提交专家配置完成必要配置的激活，高级公司间库存转储可使用SSCUI参考set-up guide配置文档完成相关所需配置的激活。在S/4HANA Cloud中无需额外的许可证，即可使用这两个场景。

**14. VCM** **框架是否不需要 IDOC****？**

VCM 不基于 IDOC。通过功能模块调用完成与业务应用程序的集成。VCM 不包含任何业务数据（例如，物料编号或数量），VCM 中仅包含凭证标识。

**15.发货与收货数量不同时的差异处理情况如何？框架是否支持 SIT** **的自动更正？**

属于交货项目的所有货物移动均以相同的数量完成。当前2208云版本不支持处理差异。

**16.公司间库存转储是否跨不同的 SAP** **系统运行？例如，当同一集团的两家公司都有自己的 S/4HANA** **系统时。**

高级 ICo 库存转储流程是单一系统流程。产品计划在未来使用双系统场景。

**17. 高级 ICo** **销售是否也可用于按订单生产流程？**

当前2208云版本的高级 ICo 销售适用于有限的场景，如按库存销售、序列号、批次（包括批次拆分和具有发票相关性的免费项目）。产品计划在未来支持更多场景，包括与 WBS 要素、按订单生产或使用项目库存的集成。含变式配置的按订单生产尚未计划，在 SAP 路线图中暂不可见。

**18.如果客户取消了某些销售订单或存在数量更改（比如增加销售数量或者减少销售数量），数据流会怎样？这些调整是自动支持还是需要手动去调整？**

内部公司间采购订单和内部公司间销售订单中的必要更改将由系统自动触发，例如，如果卖方公司销售订单中的收货方地址已更改，则交货公司采购订单和销售订单中的收货方地址也将更改。

**19.交货公司的发货是否在后台自动/****立即触发转运工厂的（虚拟）收货和发货，或者流程中是否存在延迟或不同的触发器？**

有时，客户会在货物离开工厂时就接收货物的货权转移（例如，由于国际贸易术语解释通则 EXW）。在这种情况下，系统 (VCM) 将立即连续触发所有货物移动，技术上与实物交接分离。通常，如果保存交货时控制日期的实际传输在过去，则将立即完成相应的货物移动（而不是由计划作业完成）。如果控制日期的计划传输在将来，则相应的货物移动将由 VCM 计划（由偏移延迟）并由后台作业（也是 VCM 框架的一部分）执行。

**20.“****监控价值链”****应用是否适用于传统的公司间传输？**

否，监控价值链应用将仅显示由 VCM 协调的流程。后台有底表控制哪些销售订单类型/行项目类别可以使用VCM框架，但并未开放SSCUI供客户配置。因此，即使激活了5MQ sale from stock in transit，也需要提交专家配置进行相关设置之后才可以在价值监控链中查看此类型的销售订单凭证流。

**21.高级公司间 STO** **是否可用于服务以及开箱即用？**

否，高级 ICo 销售仅用于库存管理物料。

**22.有关高级公司间以及与 TM** **集成的问题：如果 SalesOrder2** **将货运单位发送到 TM****，是否可以在 TM** **之外为销售订单 4****（针对供应公司）创建交货建议？**

只有销售公司的销售订单直接集成到 TM 中，意味着创建货运单位。TM 将根据外部国际贸易术语解释通则定义组织从交货工厂到收货方的完全运输。TM 使用内部和外部国际贸易术语解释通则来定义哪个段由哪个联营公司覆盖/组织，并相应分摊运费成本。外部国际贸易条款从卖方公司的销售订单中接收，内部国际贸易条款从销售公司的采购订单中接收。交货公司的销售订单在物流上不相关，因此物流上与交货无关。仅将此销售订单的 FI 数据复制到外向交货。

**23.在高级公司间销售中，采购订单 3** **是 STO** **还是 PO****？**

从技术角度讲，销售公司中的采购订单是采购订单。

**24.如何对这些自动步骤进行错误处理（例如，由于数据不完整，无法创建销售订单 4****）？**

该错误由 VCM 捕获。VCM 应用可用于问题检测（选择状态为“已处理，有错误”的流程），日志将显示错误，用户可以在问题解决后手动触发采购订单创建步骤，或者可以使用定期作业尝试自动重新处理失败的流程步骤。

**25.高级公司间销售是否使用新的移动类型？**

否，高级公司间销售使用现有的移动类型，通过已评估在途库存和公司间库存转储从库存中销售，请查看测试中使用到的不同凭证中的具体移动类型。

\* 有关当前功能（限制和常规信息）的详细信息，请参阅 SAP Note：

+ [3192584](https://launchpad.support.sap.com/) - SAP S/4HANA Cloud：高级公司间销售的限制和常规信息

+ [3192546](https://launchpad.support.sap.com/) - SAP S/4HANA Cloud：高级公司间库存转储的限制和常规信息

+ [3226683](https://launchpad.support.sap.com/) - SAP S/4HANA 2022：高级公司间销售的限制和常规信息（自 2022 年 10 月起）

+ [3226677](https://launchpad.support.sap.com/) - SAP S/4HANA 2022：高级公司间库存调拨的限制和常规信息（自 2022 年 10 月起）

\*最佳实践浏览器

+ [5D2 -](https://rapid.sap.com/bp/) [高级公司间销售](https://rapid.sap.com/bp/) (SAP S/4HANA Cloud)

+ [5HP -](https://rapid.sap.com/bp/) [高级公司间库存转储](https://rapid.sap.com/bp/) (SAP S/4HANA Cloud)

\*SAP 帮助 - 产品帮助

+ [SAP S/4HANA](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/6c2684455628425fbc5db2d0f0721f31.html?locale=en-US) [Cloud：高级公司间销售](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/6c2684455628425fbc5db2d0f0721f31.html?locale=en-US)

+ [SAP S/4HANA](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/136b810e1bf44faa991bd6b7bae14c50.html?locale=en-US) [Cloud：高级公司间](https://help...
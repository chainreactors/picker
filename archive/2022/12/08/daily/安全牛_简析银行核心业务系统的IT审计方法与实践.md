---
title: 简析银行核心业务系统的IT审计方法与实践
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651120720&idx=2&sn=af418f0b04d2d7b1013b211754e18f00&chksm=bd1454838a63dd95fe7ebaf13de0210a8cf36debb615df44bf6e1fe37eaf7f1a28fdf41da988&scene=58&subscene=0#rd
source: 安全牛
date: 2022-12-08
fetch_date: 2025-10-04T00:53:50.866216
---

# 简析银行核心业务系统的IT审计方法与实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD0cH3OYiaPN3D6SiapF1H2RW8nkOiaiajuqwbJYFKoIQUenM8lxJMpB8dpSp0zicPdibOic4xM7FZRnSDNA/0?wx_fmt=jpeg)

# 简析银行核心业务系统的IT审计方法与实践

安全牛

以下文章来源于ISACA
，作者Veronica N. Rose

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5pbwgfbqEFG6KjnytNoyNTNkTibmib1F4VetdD7KtV0ong/0)

**ISACA**
.

享誉全球的专业技术组织ISACA，致力于推动全球技术领域的人才、专业知识和学习的持续进步，构建全球化专业社区，助力个人的职业进步和企业的数字化转型。其颁发的CISA等认证受到安全、治理、审计、鉴证、风险、数据和隐私等领域从业者的高度认可。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAOg7QudcjnlUsdGACB8zJFWcjyxBOPbvzlCVBOhNKIQuWGia6z7cYrNHYYnarRZbiaCCARiaFhXTUgA/640?wx_fmt=jpeg)

对于信息系统审计师，经常会在工作中面临一个问题：如何去审计一套从未使用过的信息系统？每个人都是从新手成长起来的，笔者也不例外。本文根据笔者过往的信息系统内部审计经历，特别是针对金融行业的核心业务信息系统（CBS）审计，进行了一些实践经验总结和分享。

目前在银行业数字化业务开展过程中，运行着各种类型的银行核心业务信息系统，审计师需要针对组织正在使用的具体系统来定制合适的审计方案。以下控制测试方法可能会适用于您的组织正在使用的CBS。

由于金融服务行业受到高度监管，因此在开始信息系统审计之前，您需要花时间阅读并更深入地了解受监管的金融服务机构应遵守的各种法规。这些机构包括银行、金融科技公司、电信公司、征信机构（CRBs）、移动支付服务公司、小额信贷组织、投资集团等。在这种情况下，您必须了解您所在国家的中央银行，金融机构法案（FIA），证券交易委员会（SEC）的监管要求，以及监督金融机构活动的其他机构（如保险监管机构和税务机关）的法规。

根据您的审计范围和审计目标，您可以在已确定需要审查的领域确定将要执行的控制测试。这些可能包括：

* 审查有关CBS运营和后端管理的组织政策，程序和标准。

* 大多数系统项目都会失败或出现问题，具体取决于它们是如何开始的，因此在一切开始时都需要多些关注。如果CBS是外包的，请查看您与供应商签订的服务级别协议（SLA）或合同，并重点审查供应商支持服务条款（是否满足设定的矩阵，以及是否包含了对违反商定的矩阵/条款和条件的处罚）。在进一步审查SLA时，请确保存在审计权利条款，包括条款、订阅性质和许可证续订频率，并确保签署了保密协议（NDA）或保密协议（Confidentiality Agreement）或合同中存在这些条款（以及版本控制，如果适用）。

* 审查CBS版本控制的应用程序支持、脚本/开发和时间表，以及如何完成维护通信。在采购CBS之前，请确认是否已制定了业务案例并审查批准。确认CBS是否通过了用户验收测试（UAT），以及是否在实施六个月后进行了实施后评审（PIR）。确保对用户的培训已经完成或正在持续进行，并且供应商提供了技术手册和非用户手册。能证明服务提供商的认证也很重要。

* 审查已批准的企业设置、后端引擎管理或CBS的参数配置，与从CBS中提取的报告相对比。

* 了解本行的产品需求（贷款、透支、存款、储蓄等），并检查银行核心业务系统，验证每个产品需求是否在CBS中按原样配置。使用数据分析工具重新计算对每个产品收取的费率，以确保收取费用的透明度和配置的准确性。还要审查变更管理程序。

* 检查CBS的托管位置（在云、混合云或本地）也很重要，以了解托管的客户个人可识别信息的数据隐私和保护要求。出于业务连续性目的，您还需要确认主数据中心和恢复站点的安全性。

* 测试应用程序的逻辑访问控制（例如，查看当前系统用户/活动帐户和已停用帐户的数量与最新的员工名单相对比）。查看每个用户配置文件的权限。此外，在建立问责制的过程中，进行审查以核实是否存在职责分离（SoD）或授权人控制。此外，审查系统参数变更是否在获得相应用户的批准后实施

* 审查容量管理实践，以确保正确地规划了IT资源。

* 在向银行核心业务系统中输入财务数据之前，检查是否进行了人工对账，因为垃圾输入等于垃圾输出。这将使您能够保证数据的完整性和准确性。

* 确保本行在其新客申请表格中定义了客户调查（KYC）详细信息，以确保您了解银行收集，处理和存档的数据类型。同样，查看银行的隐私政策和隐私声明，以了解其如何处理个人可识别信息。查看应用程序中客户详细信息的更新频率。

* 查看备份计划，了解如何完成日初（SOD）和日终流程（EOD），监控未发布/无监督的交易，以及如何将其追溯到发起人或主管，并审查恢复时间表。

* 审查您的组织和 CBS 服务提供商的业务连续性计划（BCP）和灾难恢复计划（DRP）。

* 在CBS的模块和菜单中，查看CBS上是否有嵌入式审计模块 （EAM），以及信息安全团队或负责人员审查日志的频率。

* 审查组织的变更管理计划，并验证是否已在CBS和应用程序上实施了所有必要的安全控制。

* 审查与CBS集成的其他应用程序、渠道、商户或API的安全性。此外，找出哪些新技术和网络安全威胁是急需解决的，以保护整个组织在可接受的水平上免受网络攻击。

您可以在CBS上测试的控件列表是无穷无尽的，具体取决于您的审计范围和审计目标。因此，作为一名信息系统审计师，您有责任制定一个全面的审计计划，这将为您的组织增加价值并提供可靠的保证。

相关阅读

[如何提高网络安全审计的有效性？](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651119277&idx=3&sn=c1b034b95ffbd2230ce0e42bb32449ce&chksm=bd146e7e8a63e768806ad64150a82e2d8a3836ff61c3d7c0dddb731a7bea4a9244eb0e043523&scene=21#wechat_redirect)

[云计算安全审计概览](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651116701&idx=2&sn=908ac10e0e5ac4a1be36cc4719f40974&chksm=bd14644e8a63ed58c92320d0b56ad7128aac0ee9fe6a8d204261a549fc9b4f29cf04e22a0d1a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
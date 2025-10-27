---
title: Change Healthcare漏洞影响 1 亿美国人
url: https://www.anquanke.com/post/id/301450
source: 安全客-有思想的安全新媒体
date: 2024-11-01
fetch_date: 2025-10-06T19:15:09.292575
---

# Change Healthcare漏洞影响 1 亿美国人

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Change Healthcare漏洞影响 1 亿美国人

阅读量**75408**

发布时间 : 2024-10-31 11:35:57

**x**

##### 译文声明

本文是翻译文章，文章来源：krebsonsecurity

原文地址：<https://krebsonsecurity.com/2024/10/change-healthcare-breach-hits-100m-americans/>

译文仅供参考，具体内容表达以及含义原文为准。

Change Healthcare 表示，它已通知约 1 亿美国人，他们的个人、财务和医疗记录可能已在 2024 年 2 月的勒索软件攻击中被盗，这次攻击造成了有史以来最大的受保护健康信息数据泄露事件。

![]()图片： Tamer Tuncay，Shutterstock.com。

由于 Change Healthcare 在代表数千家机构处理付款和处方方面发挥着核心作用，2 月份第三周发生在该公司的勒索软件攻击迅速引发了整个美国医疗系统的混乱，并持续数月之久。

今年 4 月，Change 估计此次漏洞将影响 “美国相当一部分人”。10 月 22 日，这家医疗保健巨头通知美国卫生与人力资源部（HHS），“已经发出了大约 1 亿份关于此次漏洞的通知”。

Change Healthcare 的通知函称，此次漏洞涉及以下内容的窃取：

-健康数据： 医疗记录编号、医生、诊断、药品、检查结果、图像、护理和治疗；
-账单记录： 包括支付卡、财务和银行记录在内的记录；
-个人数据： 社会安全号；驾驶执照或州身份证号码；
-保险数据： 医疗计划/保单、保险公司、成员/团体 ID 编号以及医疗补助-医疗保险-政府付款人 ID 编号。

据《HIPAA 期刊》报道，在截至 2024 年 9 月 30 日的九个月中，Change 的母公司联合健康集团（United Health Group）直接违规响应成本为 15.21 亿美元，网络攻击总影响为 24.57 亿美元。

这些成本包括该公司承认向勒索者（一个名为 BlackCat 和 ALPHV 的勒索软件组织）支付的 2200 万美元，以换取销毁被盗医疗数据的承诺。

当允许 BlackCat 进入 Change 网络的附属公司称该犯罪团伙骗取了他们的赎金份额时，赎金的支付就出现了问题。之后，BlackCat 的整个勒索软件行动都停止了，他们卷走了所有拖欠受雇安装勒索软件的附属公司的钱款。

![]()
来自 Change Healthcare 的入侵通知。

BlackCat 内爆几天后，一个名为 RansomHub 的竞争勒索软件联盟组织出售了同样被盗的医疗保健数据。

RansomHub 的受害者羞辱博客于 4 月 16 日宣布：“受影响的保险提供商可以联系我们，以防止自己的数据泄露并[将其]从销售中删除。Change Health 和 United Health 为所有这些公司处理敏感数据的行为简直令人难以置信。对于大多数怀疑我们的美国人来说，我们可能掌握着你的个人数据。”

目前尚不清楚 RansomHub 是否出售过被盗的医疗数据。受此次漏洞影响的一家大型学术医疗系统的首席信息安全官告诉 KrebsOnSecurity，他们参加了与 FBI 的通话，并被告知第三方合作伙伴设法恢复了至少四兆字节的数据，这些数据是由网络犯罪集团从 Change 中流出的。联邦调查局拒绝对此发表评论。

Change Healthcare 的信息泄露通知函为收件人提供了两年的信用监控和身份盗窃保护服务，这些服务由一家名为 IDX 的公司提供。在信件中题为 “为什么会发生这种情况？”的部分，Change 仅表示 “一名网络罪犯未经我们允许访问了我们的计算机系统”。

但在 2024 年 6 月向参议院金融委员会提供的证词中显示，入侵者窃取或购买了用于远程访问的 Citrix 门户的凭证，而且该账户不需要多因素身份验证。

上个月，参议员 马克-华纳（Mark Warner）和罗恩-怀登（Ron Wyden）提出了一项法案，要求 HHS 为医疗服务提供商、医疗计划、信息交换中心和商业伙伴制定并执行一套严格的最低网络安全标准。该法案还将取消《健康保险可携性与责任法案》（Health Insurance Portability and Accountability Act）中现有的罚款上限，该上限严重限制了 HHS 对医疗服务提供商的经济处罚。

据《HIPAA 期刊》报道，迄今为止，因违反《HIPAA 法案》而受到的最大处罚是对保险公司安泰公司（Anthem Inc. 安泰公司 2015 年的营业收入约为 800 亿美元。

![]()
2024 年 4 月 8 日，RansomHub 发布的关于 Change breach 的帖子。图片： Darkbeast, ke-la.com.

对于医疗记录的泄露，此次漏洞的受害者几乎无能为力。不过，由于被泄露的数据中包含的信息足以让身份窃贼得逞，因此，如果您还没有对自己和家人的信用档案进行安全冻结，最好还是谨慎行事。

防止身份窃贼以您的名义创建新账户的最佳机制是冻结您在 Equifax、Experian 和 TransUnion 的信用档案。现在，所有美国人都可以免费办理这一手续，只需阻止潜在的债权人查看您的信用档案即可。父母和监护人现在也可以冻结子女或受抚养人的信用档案。

由于很少有债权人愿意在无法确定风险有多大的情况下授予新的信贷额度，因此冻结您在三大银行的信用档案是阻止各种身份盗窃诡计的好方法。冻结不会阻止您使用现有的信用额度，如信用卡、抵押贷款和银行账户。如果您需要访问您的信用档案，如申请贷款或新信用卡时，您需要提前与一个或多个统计局解除或暂时解冻冻结。

三家征信机构都允许用户在创建账户后以电子方式进行冻结，但它们都试图引导消费者不要进行冻结。取而代之的是，三家机构都希望消费者选择其名称令人困惑的 “信用锁定 ”服务，这种服务可以达到同样的效果，但允许三家机构继续向特定的合作伙伴出售您的文件访问权。

如果您有一段时间没有这样做了，现在是审查您的信用档案是否有任何问题或错误的最佳时机。根据法律规定，每个人都有权每 12 个月从三家信用报告机构免费获得一份信用报告。但联邦贸易委员会指出，三大信用局已永久延长了 2020 年颁布的一项计划，该计划允许您每周免费查看一次各机构的信用报告。

本文翻译自krebsonsecurity [原文链接](https://krebsonsecurity.com/2024/10/change-healthcare-breach-hits-100m-americans/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301450](/post/id/301450)

安全KER - 有思想的安全新媒体

本文转载自: [krebsonsecurity](https://krebsonsecurity.com/2024/10/change-healthcare-breach-hits-100m-americans/)

如若转载,请注明出处： <https://krebsonsecurity.com/2024/10/change-healthcare-breach-hits-100m-americans/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)
---
title: 性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线
url: https://www.anquanke.com/post/id/314100
source: 安全客-有思想的安全新媒体
date: 2025-12-29
fetch_date: 2025-12-30T03:25:28.424990
---

# 性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线

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

# 性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线

阅读量**20122**

发布时间 : 2025-12-29 15:39:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/the-performance-propeller-google-proposes-upstreaming-its-high-octane-optimizer-to-llvm/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌工程师提议将 Propeller 工具集成至 LLVM 核心代码库。Propeller 是一款基于剖面引导的优化器，通过重新优化程序各组件的布局结构及关联关系，实现大型应用的性能提速。
Propeller 工具已历经数年研发，基于 LLVM 构建，可支持对整个代码库开展全程序优化。谷歌在编译 Linux 内核时，已将 Propeller 与 AutoFDO 搭配部署，成功实现 5% 至 10% 的性能提升。
谷歌编译器团队的一名工程师已在 LLVM Discourse 论坛发布该提案。提案文件明确，Propeller 通过对函数及基本块进行精准布局，实现应用性能提升。LLVM 内部已具备支持 Propeller 运行的部分必要基础架构，包括 Clang 编译器与 LLD 链接器中的相关支持模块；但生成剖面文件的核心工具，目前仍存放在谷歌单独维护的代码仓库中。
当前使用 Propeller 需对接该外部代码仓库，给开发流程增加了额外繁琐操作。将该工具集成至 LLVM 主线代码库后，其可随标准工具集一同分发，大幅降低开发者的适配门槛。提案作者表示，Propeller 采用基于重链接的实现方案，在分布式构建与增量构建场景中具备出色的扩展性，该工具定位为 BOLT 等二进制重写框架的替代方案。

本文翻译自securityonline [原文链接](https://securityonline.info/the-performance-propeller-google-proposes-upstreaming-its-high-octane-optimizer-to-llvm/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314100](/post/id/314100)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-performance-propeller-google-proposes-upstreaming-its-high-octane-optimizer-to-llvm/)

如若转载,请注明出处： <https://securityonline.info/the-performance-propeller-google-proposes-upstreaming-its-high-octane-optimizer-to-llvm/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **870**

* 粉丝
* **6**

### TA的文章

* ##### [EmEditor 遭攻陷：“沃尔沙姆” 伪装者篡改官方安装包，植入间谍软件](/post/id/314096)

  2025-12-29 15:40:16
* ##### [性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线](/post/id/314100)

  2025-12-29 15:39:28
* ##### [圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元](/post/id/314091)

  2025-12-29 15:39:18
* ##### [70 美元芯片争夺战：谷歌缘何高管换人，苹果又为何要直面 230% 的价格暴涨](/post/id/314077)

  2025-12-29 15:38:41
* ##### [CVE-2025-54322（CVSS 10 分满分）：AI 智能体发现全球网络设备高危零日漏洞](/post/id/314086)

  2025-12-29 15:38:37

### 相关文章

* ##### [EmEditor 遭攻陷：“沃尔沙姆” 伪装者篡改官方安装包，植入间谍软件](/post/id/314096)

  2025-12-29 15:40:16
* ##### [圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元](/post/id/314091)

  2025-12-29 15:39:18
* ##### [70 美元芯片争夺战：谷歌缘何高管换人，苹果又为何要直面 230% 的价格暴涨](/post/id/314077)

  2025-12-29 15:38:41
* ##### [CVE-2025-54322（CVSS 10 分满分）：AI 智能体发现全球网络设备高危零日漏洞](/post/id/314086)

  2025-12-29 15:38:37
* ##### [终结 “内存占用税”：微软新方案让文件资源管理器搜索速度翻倍](/post/id/314084)

  2025-12-29 15:38:15
* ##### [黑客攻陷 Trust Wallet 谷歌浏览器插件，用户称数百万资产被盗](/post/id/314073)

  2025-12-29 15:37:47
* ##### [节假日 ColdFusion 攻击频发：遭 250 万次请求大规模猛攻](/post/id/314079)

  2025-12-29 15:37:21

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
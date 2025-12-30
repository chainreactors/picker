---
title: 圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元
url: https://www.anquanke.com/post/id/314091
source: 安全客-有思想的安全新媒体
date: 2025-12-29
fetch_date: 2025-12-30T03:25:30.392955
---

# 圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元

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

# 圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元

阅读量**20546**

发布时间 : 2025-12-29 15:39:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/the-christmas-drain-how-a-backdoor-in-trust-wallet-v2-68-stole-7m/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

知名加密货币钱包插件 Trust Wallet 近期疑似遭遇供应链攻击。攻击者通过某种方式攻陷该插件并植入恶意代码，专门窃取用户的恢复助记词。一旦获取助记词，攻击者便可恢复受害者的钱包，并将其中资产席卷一空。

截至本文撰写时，被盗加密货币价值已超 600 万美元，受影响用户规模或持续扩大。**强烈建议**所有使用该插件的用户，立即将资产转移至可信钱包中，以规避风险。区块链安全公司慢雾科技创始人余弦在社交平台发布了简要技术分析：

存在后门的版本为 **v2.68.0**，开发者紧急修复后推出的版本为 **v2.69.0**。代码对比结果显示，遭篡改的版本中植入了 PostHog 组件，用于收集钱包恢复助记词等高度敏感的用户数据，并将这些数据秘密传输至攻击者控制的服务器 `hxxp://api.metrics-trustwallet.com`。

域名注册记录显示，该恶意域名于 2025 年 12 月 8 日完成注册，可见攻击者早已开始筹备。后门程序于 12 月 22 日成功植入，随后攻击者进入潜伏状态。直至 12 月 25 日圣诞节当天，才开始大肆转移资产。

攻击者选择在圣诞节发动攻击，大概率是经过精心算计的：在西方国家的节假日期间，Trust Wallet 团队和大量用户的安全警惕性都可能下降。这使得攻击者能够在漏洞被发现、补丁发布以及用户采取资产保护措施前，获得更长的时间窗口来转移资产。

此次事件的最终损失规模尚未完全统计。值得注意的是，这并非 Trust Wallet 首次遭遇安全事故。2022 年 11 月 14 日至 23 日期间，该时间段内创建的钱包曾因伪随机数生成机制存在缺陷，导致攻击者可推导得出私钥。

彼时相关事件造成的损失约为 17 万美元，金额相对较小，Trust Wallet 已对受害者进行全额赔付。而此次损失已超 600 万美元，用户能否获得全额赔偿，目前仍是未知数。

本文翻译自securityonline [原文链接](https://securityonline.info/the-christmas-drain-how-a-backdoor-in-trust-wallet-v2-68-stole-7m/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314091](/post/id/314091)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-christmas-drain-how-a-backdoor-in-trust-wallet-v2-68-stole-7m/)

如若转载,请注明出处： <https://securityonline.info/the-christmas-drain-how-a-backdoor-in-trust-wallet-v2-68-stole-7m/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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
* ##### [性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线](/post/id/314100)

  2025-12-29 15:39:28
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
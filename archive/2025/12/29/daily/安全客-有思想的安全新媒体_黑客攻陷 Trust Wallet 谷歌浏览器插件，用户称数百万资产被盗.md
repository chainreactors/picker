---
title: 黑客攻陷 Trust Wallet 谷歌浏览器插件，用户称数百万资产被盗
url: https://www.anquanke.com/post/id/314073
source: 安全客-有思想的安全新媒体
date: 2025-12-29
fetch_date: 2025-12-30T03:25:37.546343
---

# 黑客攻陷 Trust Wallet 谷歌浏览器插件，用户称数百万资产被盗

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

# 黑客攻陷 Trust Wallet 谷歌浏览器插件，用户称数百万资产被盗

阅读量**0**

发布时间 : 2025-12-29 15:37:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/hackers-compromise-trust-wallet-chrome-extension/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络犯罪分子攻陷了 2025 年 12 月 24 日发布的 Trust Wallet 谷歌浏览器插件 2.68.0 版本，导致该钱包用户蒙受超 700 万美元的巨额损失。

此次攻击仅针对桌面端用户，恶意更新程序发布数小时内，数百个钱包便被洗劫一空。

区块链调查员扎克・XBT（ZachXBT）率先在社交平台 X 上披露了这一事件，他指出，用户在使用遭攻陷的插件后，受影响地址的未授权资金转移量随即出现可疑激增。

受害者从圣诞夜开始陆续上报失窃情况，还分享了截图，显示钱包中的以太坊、比特币、索拉纳币和币安币等资产已被悉数转走。

一名受害者称，他通过该插件完成常规授权操作后，短短几分钟内就损失了 30 万美元，被盗资产被转移至多个由攻击者控制的地址。

安全公司派盾（PeckShield）起初估算损失金额为 600 万美元，但 Trust Wallet 后续证实，此次事件波及数百个遭攻陷的钱包，被盗资金总额约达 700 万美元。

安全研究人员发现，一款名为 4482.js 的 JavaScript 文件中嵌入了恶意代码，该文件伪装成了正规的 PostHog 数据分析软件。

这段经过混淆处理的恶意脚本会在用户导入助记词时被激活，暗中将敏感的钱包凭证和恢复助记词发送至[api.metrics-trustwallet.com](https://api.metrics-trustwallet.com/)这个欺诈域名。该域名在攻击发生前数日才完成注册，其设计目的就是模仿 Trust Wallet 的官方基础设施。

此次攻击体现出攻击者的精密协同性，威胁行为者同时还通过[fix-trustwallet.com](https://fix-trustwallet.com/)等域名发起钓鱼攻击。

这些欺诈网站利用用户的恐慌心理，提供虚假的 “漏洞修复方案”，诱骗用户输入助记词，进而实现对钱包的即时洗劫。

Trust Wallet 于 12 月 25 日通过社交平台 X 承认了此次安全漏洞事件，并证实受影响的仅有 2.68.0 版本。

该公司要求用户立即关闭这款插件，并更新至 2.69 版本。

Trust Wallet 承诺对受害者进行全额赔付，同时警告用户切勿理会那些声称提供技术支持的非官方私信。

币安联合创始人赵长鹏暗示，此次事件可能涉及内部人员参与，这一说法也引发了外界对该公司内部安全管控机制的质疑。

该事件暴露出加密货币钱包插件存在的重大供应链漏洞 —— 自动更新功能可能会绕过用户的人工验证环节。

网络安全专家建议，受影响用户应创建新钱包，并对今后所有的插件更新进行严格核查。

本文翻译自gbhackers [原文链接](https://gbhackers.com/hackers-compromise-trust-wallet-chrome-extension/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314073](/post/id/314073)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/hackers-compromise-trust-wallet-chrome-extension/)

如若转载,请注明出处： <https://gbhackers.com/hackers-compromise-trust-wallet-chrome-extension/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元](/post/id/314091)

  2025-12-29 15:39:18
* ##### [70 美元芯片争夺战：谷歌缘何高管换人，苹果又为何要直面 230% 的价格暴涨](/post/id/314077)

  2025-12-29 15:38:41
* ##### [CVE-2025-54322（CVSS 10 分满分）：AI 智能体发现全球网络设备高危零日漏洞](/post/id/314086)

  2025-12-29 15:38:37
* ##### [终结 “内存占用税”：微软新方案让文件资源管理器搜索速度翻倍](/post/id/314084)

  2025-12-29 15:38:15
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
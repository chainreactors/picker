---
title: 恶意浏览器插件针对imToken用户窃取私钥
url: https://www.anquanke.com/post/id/315065
source: 安全客-有思想的安全新媒体
date: 2026-03-10
fetch_date: 2026-03-11T04:03:16.938626
---

# 恶意浏览器插件针对imToken用户窃取私钥

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

# 恶意浏览器插件针对imToken用户窃取私钥

阅读量**24479**

发布时间 : 2026-03-10 14:02:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/malicious-browser-add-on-targets-imtoken-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Socket 威胁研究团队发现一款**极具欺骗性的谷歌浏览器扩展程序**，专门用于窃取加密货币用户的**私钥与助记词**。

这款恶意插件名为 **lmΤoken Chromophore**（扩展 ID：bbhaganppipihlhjgaaeeeefbaoihcgi），对外伪装成面向开发者与数字艺术家的十六进制颜色可视化工具。

但其真实目的，是冒充目前广泛使用的**非托管钱包品牌 imToken**，从毫无防备的受害者手中窃取敏感的钱包恢复密钥。

该扩展在**安装后自动发起攻击**，且用户每次点击图标都会重复执行恶意流程。

自 2016 年推出以来，正版 imToken 钱包已在全球 150 多个国家积累了**超过 2000 万用户**。

由于 imToken **仅以移动 App 形式运营**，从未官方发布过浏览器扩展，因此成为黑客利用品牌知名度实施诈骗的重点目标。

Socket 威胁研究团队还发现，该恶意插件在应用商店页面**刻意伪造信任**：展示虚假五星好评，并使用官方钱包风格的品牌图片，快速骗取用户信任。

插件甚至附带一份声称**不会收集任何数据**的隐私政策，在受害者检查代码之前就营造出正规可信的假象。

---

### 钓鱼攻击技术分析

该攻击背后的黑客组织使用**高度复杂的规避手段**，绕过自动化检测工具与人工审核。

恶意插件本身**不包含明显的本地窃取逻辑**，仅作为轻量级浏览器重定向器运行。

安装后，扩展的后台 JavaScript 会**从硬编码的外部 JSONKeeper 配置地址静默获取目标 URL**。

随后，受害者会被立即跳转到黑客控制的钓鱼网站，域名为极具迷惑性的仿冒地址：[chroomewedbstorre-detail-extension.com](https://chroomewedbstorre-detail-extension.com)。

为进一步增强欺骗性，攻击者使用**混合字符集的 Unicode 同形字**，绕过简单的文本匹配与 URL 安全过滤规则。

钓鱼页面标题显示为 **“іmΤоken”**，而非正常的 “imToken”，用视觉上几乎一样的西里尔字母与希腊字母替换标准拉丁字符。

进入钓鱼页面后，用户会看到**高度仿真的钱包导入界面**，与官方应用完全一致。

界面诱导受害者直接输入 **12 位或 24 位助记词**，或明文私钥，所有信息都会直接上传至攻击者服务器。

一旦泄露上述任一关键密钥，攻击者可**立即完全控制对应钱包中的加密货币资产**。

为确保受害者对盗窃行为完全不知情，钓鱼流程会无缝跳转到一个**伪造的本地密码设置界面**。

这一步完美模仿正版钱包的初始化行为，并**额外收集一组密码**，供未来可能的攻击使用。

最后，页面会显示一个虚假的**钱包升级加载动画**，随后悄悄将用户跳转到正版官网 token.im。

这套精巧的收尾手段作为最终伪装，让受害者误以为自己成功使用了**官方 imToken 工具**。

---

### 威胁指标与缓解方案

安全分析人员需持续警惕**安装后自动拉取远程配置、或意外打开外部域名**的浏览器扩展。

由于攻击者采用**外部控制机制**，其核心攻击基础设施可随时切换或重定向，无需更新插件本身。

### 主要威胁指标（IoCs）

* 恶意扩展 ID：**bbhaganppipihlhjgaaeeeefbaoihcgi**
* 恶意扩展名称：**lmΤoken Chromophore**
* 主要钓鱼域名：**[chroomewedbstorre-detail-extension.com](https://chroomewedbstorre-detail-extension.com)**
* 配置地址：**[jsonkeeper.com/b/KUWNE](https://jsonkeeper.com/b/KUWNE)**

为有效防范此类安全风险，机构与个人必须将**所有浏览器扩展视为高风险第三方软件**。

管理员应严格限制敏感浏览器配置文件下的扩展安装行为，所有加密货币相关软件**必须通过官方渠道验证**。

若用户不慎在可疑页面输入过**助记词、私钥或钱包密码**，应立即认定该钱包**已完全沦陷**。

受影响用户必须**在攻击者转走资产前**，尽快将所有剩余数字资产转移到**全新生成、密钥完全独立**的新钱包中。

本文翻译自gbhackers [原文链接](https://gbhackers.com/malicious-browser-add-on-targets-imtoken-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315065](/post/id/315065)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/malicious-browser-add-on-targets-imtoken-users/)

如若转载,请注明出处： <https://gbhackers.com/malicious-browser-add-on-targets-imtoken-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1070**

* 粉丝
* **6**

### TA的文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18

### 相关文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [Viber即时通讯软件存在TLS漏洞，Cloak代理模式失效并导致用户暴露](/post/id/315068)

  2026-03-10 14:01:44
* ##### [黑客可利用间接提示注入攻击 借助外部内容操控AI智能体](/post/id/315071)

  2026-03-10 14:01:03
* ##### [海康威视与罗克韦尔自动化高危漏洞纳入CISA已知被利用漏洞清单](/post/id/315077)

  2026-03-10 14:00:36

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
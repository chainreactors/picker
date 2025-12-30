---
title: Livewire 框架高危漏洞致 Laravel 应用面临隐蔽远程代码执行风险，漏洞验证工具已公开
url: https://www.anquanke.com/post/id/314068
source: 安全客-有思想的安全新媒体
date: 2025-12-29
fetch_date: 2025-12-30T03:25:41.071347
---

# Livewire 框架高危漏洞致 Laravel 应用面临隐蔽远程代码执行风险，漏洞验证工具已公开

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

# Livewire 框架高危漏洞致 Laravel 应用面临隐蔽远程代码执行风险，漏洞验证工具已公开

阅读量**16013**

发布时间 : 2025-12-29 15:37:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-flaw-in-livewire-exposes-laravel-apps-to-stealthy-rce-poc-releases/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

对于依赖 Livewire 框架开发 Laravel 动态交互界面的开发者而言，一场严峻的安全考验已悄然降临。安全公司 Synacktiv 的深度分析显示，Livewire 框架存在一个高危漏洞及一项固有设计缺陷，攻击者可借此在全球超 13 万个基于该框架的应用服务器上执行任意代码。

该漏洞编号为 **CVE-2025-54068**，其攻击原理是利用 Livewire 框架内部的 “状态还原” 机制 —— 这一机制原本用于实现服务器与浏览器之间的状态同步。尽管官方已发布漏洞补丁，但研究人员警告称，框架的一项核心设计特性仍如同定时炸弹，一旦应用程序的密钥泄露，便会触发严重风险。

Livewire 框架的普及率极高，超过 30% 的全新 Laravel 项目都会采用它，仅需少量 JavaScript 代码就能构建交互式前端页面。其工作机制是先将组件状态 “序列化” 为特定格式并发送至客户端，待客户端回传数据时再进行 “反序列化还原”。

Synacktiv 的研究人员发现，这一机制存在可被操纵的空间。他们通过梳理 PHP 反序列化函数 `unserialize()` 的调用链，找到了实现 \*\*“隐蔽式远程代码执行”\*\* 的攻击路径。

漏洞的核心成因在于 Livewire 框架处理组件更新的方式。报告指出：“默认情况下，如果开发者未对组件参数设置严格的类型校验，应用就会面临变量类型欺骗攻击的风险。” 攻击者可构造特制请求，将原本的整数计数器变量强制转换为恶意数组，从而诱骗服务器执行恶意代码。

理论上，Livewire 框架会通过应用程序的 `APP_KEY` 密钥生成校验和，以此保护组件状态数据不被篡改。然而，CVE-2025-54068 漏洞使得攻击者能够完全绕过这一防护机制。

研究人员表示：“CVE-2025-54068 漏洞的发现进一步暴露了框架的致命缺陷：攻击者可通过更新机制植入自定义序列化处理器，彻底规避对 `APP_KEY` 密钥的依赖。”

这意味着，即便没有获取到应用密钥，攻击者依然可以注入恶意对象 —— 具体可借助 `GuzzleHttp\Psr7\FnStream` 类及 PHP 的析构魔术方法 —— 触发远程代码执行攻击。

尽管 Livewire 3.6.4 及以上版本已修复 CVE-2025-54068 漏洞，但更深层次的风险依然存在。研究报告强调，一旦攻击者获取到 `APP_KEY` 密钥（此类泄露事件在密钥配置不当或使用默认值时极易发生），基于该框架的应用程序将彻底丧失防御能力，无法抵御远程代码执行攻击。

“需要借助 `APP_KEY` 密钥才能触发的攻击路径并未被修复，因为该路径利用的是 Livewire 框架的原生设计逻辑……Livewire 开发团队甚至不认为这属于安全漏洞。”

Synacktiv 公司对此持反对观点，认为开发团队严重低估了风险，其指出：“对于基于 3.x 版本 Livewire 框架搭建的应用程序，一旦攻击者掌握 `APP_KEY` 密钥，就能完全攻陷整个系统。”

为佐证这些漏洞的严重危害，Synacktiv 公司已公开一款名为 **Livepyre** 的漏洞验证工具。该工具可自动化完成漏洞检测与恶意载荷投放的全过程。

报告明确说明：“我们开发了 Livepyre 工具，无论攻击者是否掌握 `APP_KEY` 密钥，都能通过这款工具快速完成漏洞利用。”

安全建议：开发者应立即将 Livewire 框架升级至最新版本，以修复 CVE-2025-54068 漏洞。但报告同时发出警示，提醒开发者正视框架的架构性风险。

“Livewire 框架的案例为所有开发者敲响警钟：基于弱类型校验与隐式信任机制构建的创新功能，极有可能沦为攻击者的‘万能攻击链’。”

研究人员强烈建议开发者，务必为所有组件属性设置严格的类型校验，并将 `APP_KEY` 密钥视为核心机密妥善保管 —— 一旦密钥泄露，任何补丁都将无力回天。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-flaw-in-livewire-exposes-laravel-apps-to-stealthy-rce-poc-releases/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314068](/post/id/314068)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-flaw-in-livewire-exposes-laravel-apps-to-stealthy-rce-poc-releases/)

如若转载,请注明出处： <https://securityonline.info/critical-flaw-in-livewire-exposes-laravel-apps-to-stealthy-rce-poc-releases/>

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
* ##### [黑客攻陷 Trust Wallet 谷歌浏览器插件，用户称数百万资产被盗](/post/id/314073)

  2025-12-29 15:37:47

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
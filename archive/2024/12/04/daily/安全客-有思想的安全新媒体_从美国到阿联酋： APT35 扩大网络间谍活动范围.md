---
title: 从美国到阿联酋： APT35 扩大网络间谍活动范围
url: https://www.anquanke.com/post/id/302378
source: 安全客-有思想的安全新媒体
date: 2024-12-04
fetch_date: 2025-10-06T19:37:25.784735
---

# 从美国到阿联酋： APT35 扩大网络间谍活动范围

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

# 从美国到阿联酋： APT35 扩大网络间谍活动范围

阅读量**55009**

发布时间 : 2024-12-03 11:35:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/from-us-to-uae-apt35-expands-reach-in-cyber-espionage/>

译文仅供参考，具体内容表达以及含义原文为准。

![APT35]()

ThreatBook 研究和响应小组揭露了 APT35（又称 Magic Hound 或 Charming Kitten）针对美国、泰国和阿联酋等多个国家的航空航天和半导体行业发起的复杂活动。这个由伊朗支持的组织隶属于伊斯兰革命卫队（IRGC），早在 2014 年就曾发动过引人注目的网络攻击。

在其中一次活动中，APT35 推出了一个虚假招聘网站，特别针对泰国航空航天领域的无人机设计专家。该网站发布了高薪招聘信息，为这一骗局增添了合法性。据 ThreatBook 称，攻击者在其 “授权访问 ”产品中混入了合法程序和恶意模块： “网站提供的授权访问程序中混入了一白一黑两种恶意样本，其中SignedConnection.exe是合法的OneDrive程序，secur32.dll、Qt5Core.dll分别是第一阶段和第二阶段的恶意程序。”

![]()
悄悄加载恶意程序 | 图片： ThreatBook

用 C# 编写的恶意模块 secur32.dll 利用字符串重构等混淆技术逃避检测，悄无声息地加载了更多阶段的恶意软件。

APT35 的方法包括通过重命名文件和注册表键操作来部署复杂的多级有效载荷，以实现持久性。该组织还利用谷歌云、GitHub 和 OneDrive 等合法平台进行命令与控制 (C&C) 通信。

ThreatBook 报告说：“ThreatBook 通过分析相关样本、IP 和域名，提取了多个相关 IOC，用于威胁情报检测。”

该恶意软件还利用了 GitHub 存储库和预先配置的备份 C&C 域，以确保在主地址被封锁时的连接性。这种适应性表明 APT35 致力于保持业务弹性。

另一个值得注意的策略涉及针对半导体公司的虚假 VPN 程序。VPN 安装程序被伪装成加载名为 msvcp.dll 的恶意 DLL 模块，作为下载器从合法云平台上托管的 C&C 服务器获取其他有效载荷。

ThreatBook指出：“利用VPN访问程序加载恶意DLL模块msvcp.dll，它与Qt5Core.dll是同一类型的下载程序。”

APT35 的行动表明，它有能力利用对 OneDrive 和 GitHub 等知名品牌和工具的信任，渗透到高价值行业。该组织广泛使用社交工程策略，再加上技术上的复杂性，突出表明处理敏感技术的行业需要提高警惕。

本文翻译自securityonline [原文链接](https://securityonline.info/from-us-to-uae-apt35-expands-reach-in-cyber-espionage/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302378](/post/id/302378)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/from-us-to-uae-apt35-expands-reach-in-cyber-espionage/)

如若转载,请注明出处： <https://securityonline.info/from-us-to-uae-apt35-expands-reach-in-cyber-espionage/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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
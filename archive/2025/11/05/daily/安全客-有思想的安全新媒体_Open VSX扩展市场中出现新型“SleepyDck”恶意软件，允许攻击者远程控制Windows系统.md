---
title: Open VSX扩展市场中出现新型“SleepyDck”恶意软件，允许攻击者远程控制Windows系统
url: https://www.anquanke.com/post/id/313027
source: 安全客-有思想的安全新媒体
date: 2025-11-05
fetch_date: 2025-11-06T03:12:31.506523
---

# Open VSX扩展市场中出现新型“SleepyDck”恶意软件，允许攻击者远程控制Windows系统

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

# Open VSX扩展市场中出现新型“SleepyDck”恶意软件，允许攻击者远程控制Windows系统

阅读量**16327**

发布时间 : 2025-11-05 17:52:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-sleepyduck-malware-in-open-vsx-marketplace/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款名为**SleepyDuck**的复杂远程访问木马已侵入**Open VSX IDE扩展市场**，针对使用Cursor和Windsurf等代码编辑器的开发者。

该恶意软件伪装成名为**juan-bianco.solidity-vlang** 的合法Solidity扩展，利用**名称抢注技术**欺骗毫无防备的用户。

该扩展最初于10月31日以0.0.7版本发布，看似无害；但在11月1日被恶意更新至0.0.8版本，在累积**14,000次下载**后获得恶意功能。

它伪装成Solidity编程语言的开发工具——Solidity常用于区块链和智能合约开发，攻击者利用这一热门领域扩大针对加密货币开发者和区块链工程师的受害群体。

此威胁的特别危险性在于：它能**持久化远程控制受感染Windows系统**，同时通过多种规避技术保持隐蔽。

Secure Annex分析师发现，该恶意软件的独特持久化机制利用**以太坊区块链合约**维持命令与控制（C2）基础设施。

这种创新方法使攻击者即使在主域名被查封或下线后，仍能**更新控制服务器地址**。

![]()

恶意软件默认与**sleepyduck[.]xyz**通信，以30秒轮询间隔接收威胁 actor 的指令。

![]()

### **感染流程：从激活到数据窃取**

当用户打开新代码编辑器窗口或选择.sol文件时，扩展被激活并触发感染。

恶意软件会收集关键机器信息，包括**主机名、用户名、MAC地址和时区数据**，以此规避安全研究员常用的沙箱分析环境。

### **以太坊驱动的持久化机制**

SleepyDuck通过区块链技术实现高级持久化，代表了恶意软件基础设施的危险进化。

威胁通过将备用配置数据存储在以太坊合约地址**0xDAfb81732db454DA238e9cFC9A9Fe5fb8e34c465**维持韧性。

当与主C2服务器连接失败时，恶意软件会查询此**不可篡改的区块链合约**，获取所有受感染端点的**更新服务器地址、轮询间隔甚至紧急命令**。

恶意软件的激活函数会创建锁定文件确保单次执行，随后调用伪装的**webpack.init() 函数**初始化恶意载荷。

初始化阶段，它从硬编码列表中选择最快的以太坊RPC提供商，通过`vm.createContext(sandbox)` 建立命令执行沙箱，然后启动轮询循环等待攻击者指令。

这种架构使攻击者完全远程控制受感染系统，同时通过**无法轻易摧毁的去中心化基础设施**维持运营安全。

**防御建议**：

1. 立即检查Open VSX扩展，卸载**juan-bianco.solidity-vlang** （尤其是0.0.8版本）。
2. 对Solidity开发工具仅从官方市场（如VS Code Marketplace）下载，并验证开发者身份。
3. 监控与**sleepyduck[.]xyz**的网络连接，阻止以太坊合约地址**0xDAfb81732db454DA238e9cFC9A9Fe5fb8e34c465**的交互。
4. 启用代码编辑器的扩展权限审计，限制未知扩展的系统访问权限。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-sleepyduck-malware-in-open-vsx-marketplace/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313027](/post/id/313027)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-sleepyduck-malware-in-open-vsx-marketplace/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-sleepyduck-malware-in-open-vsx-marketplace/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **653**

* 粉丝
* **6**

### TA的文章

* ##### [一文读懂香港金融科技周：DART将带领香港金融科技驶向何方？](/post/id/313039)

  2025-11-05 18:35:34
* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法](/post/id/313007)

  2025-11-05 17:54:36
* ##### [新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷](/post/id/313012)

  2025-11-05 17:54:19
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59

### 相关文章

* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法](/post/id/313007)

  2025-11-05 17:54:36
* ##### [新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷](/post/id/313012)

  2025-11-05 17:54:19
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59
* ##### [全球网络间谍组织利用ZipperDown漏洞及Android零日漏洞，通过邮件客户端实现一键远程代码执行与账户接管](/post/id/313018)

  2025-11-05 17:53:37
* ##### [React Native CLI 中存在严重漏洞（CVE-2025-11953，CVSS 9.8），攻击者可经由暴露的Metro开发服务器实现RCE](/post/id/313021)

  2025-11-05 17:53:18
* ##### [Bugcrowd收购自动化测试工具Mayhem，以强化其应用安全测试平台能力](/post/id/313024)

  2025-11-05 17:52:48

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
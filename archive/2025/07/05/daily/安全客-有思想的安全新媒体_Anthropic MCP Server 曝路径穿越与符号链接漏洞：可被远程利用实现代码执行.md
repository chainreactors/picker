---
title: Anthropic MCP Server 曝路径穿越与符号链接漏洞：可被远程利用实现代码执行
url: https://www.anquanke.com/post/id/309424
source: 安全客-有思想的安全新媒体
date: 2025-07-05
fetch_date: 2025-10-06T23:16:36.969512
---

# Anthropic MCP Server 曝路径穿越与符号链接漏洞：可被远程利用实现代码执行

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

# Anthropic MCP Server 曝路径穿越与符号链接漏洞：可被远程利用实现代码执行

阅读量**81830**

发布时间 : 2025-07-04 15:07:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/anthropic-mcp-server-flaws-path-traversal-symlink-attacks-allow-rce/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Cymulate Research Labs 近日披露了 Anthropic 的 Filesystem MCP Server 中存在的两个高危漏洞。漏洞编号为 **CVE-2025-53110** 和 **CVE-2025-53109**，攻击者可利用该漏洞实现未授权访问、权限提升，甚至远程代码执行（RCE）。

研究人员在报告中警示道：“**随着 AI 基础设施热度不断攀升，我们更应警惕其潜藏的安全风险**。”

MCP 被称为“AI 的 USB-C 接口”，是一种统一框架，用于让大语言模型（LLM）通过标准化的服务端接口连接文件系统、API 和数据库。而其中的 Filesystem MCP Server 是一个基于 Node.js 的模块，允许执行诸如文件读取、写入与目录列出等操作——理论上仅限于配置文件中定义的“允许目录”范围内。

但这种目录沙箱机制，在实践中却存在严重破绽。

### 漏洞一：路径验证绕过（CVE-2025-53110，CVSS 7.3）

该漏洞源于 MCP Server 对路径合法性验证的方式存在严重缺陷：仅通过 `startswith`（前缀匹配）判断请求路径是否属于允许目录。

报告指出：“**攻击者可以构造一个路径名，该路径虽然以允许目录为前缀，但实际位置却跳出了目录范围，从而绕过访问控制。**”

该漏洞允许攻击者访问本应被沙箱隔离的系统敏感文件，彻底打破原有的安全边界。

### 漏洞二：符号链接攻击（CVE-2025-53109，CVSS 8.2）

第二个漏洞危害更大。攻击者可利用符号链接配合上述路径绕过机制，获取任意文件的读写权限——包括系统关键文件如 `/etc/sudoers`。

报告指出：“**若 MCP 服务或 Claude 进程以 root 身份运行，攻击者甚至可实现完全系统接管。**”

在 PoC 中，研究人员将恶意 `.plist` 文件注入 macOS 的 LaunchAgents 目录，并成功在登录时自动执行 Calculator 应用。虽然演示使用的是无害软件，但在实际攻击中，这一方法完全可用于部署勒索软件或数据窃取工具。

### 根因分析

漏洞根源在于**错误的异常处理逻辑**。当服务器验证路径失败时，并未跟进检查符号链接的真实目标，而是错误地回退到对其**符号路径的父目录**进行判断，导致绕过成功。

报告总结称：“**错误的路径解析和符号链接处理，使得整个沙箱模型形同虚设。**”

### 官方响应与修复

Anthropic 已于 **2025 年 7 月 1 日** 发布安全补丁，所有使用 Filesystem MCP Server 的用户强烈建议立即升级至 **版本 2025.7.1**。

报告最后表示：“我们已观察到新版本的快速部署，这大大降低了漏洞被利用的风险。”

本文翻译自securityonline [原文链接](https://securityonline.info/anthropic-mcp-server-flaws-path-traversal-symlink-attacks-allow-rce/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309424](/post/id/309424)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/anthropic-mcp-server-flaws-path-traversal-symlink-attacks-allow-rce/)

如若转载,请注明出处： <https://securityonline.info/anthropic-mcp-server-flaws-path-traversal-symlink-attacks-allow-rce/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

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
* **545**

* 粉丝
* **5**

### TA的文章

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